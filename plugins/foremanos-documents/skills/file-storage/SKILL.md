---
name: file-storage
description: ForemanOS file storage patterns. Use when working with S3/R2 uploads, presigned URLs, virus scanning, OneDrive sync, or photo retention.
---

# File Storage for ForemanOS

## When to Use This Skill
- Uploading files to S3/Cloudflare R2
- Generating presigned URLs for direct browser uploads
- Downloading files from S3
- Implementing virus scanning for uploads
- Working with OneDrive integration
- Managing photo retention and archival

## Core Patterns

### Pattern 1: S3/R2 Client Setup

ForemanOS uses a singleton S3 client compatible with both AWS S3 and Cloudflare R2:

```typescript
// lib/aws-config.ts
import { S3Client } from "@aws-sdk/client-s3";

export function getBucketConfig() {
  return {
    bucketName: process.env.AWS_BUCKET_NAME ?? "",
    folderPrefix: process.env.AWS_FOLDER_PREFIX ?? "",
  };
}

export function createS3Client() {
  const endpoint = process.env.S3_ENDPOINT;
  const accessKeyId = process.env.AWS_ACCESS_KEY_ID;
  const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY;

  return new S3Client({
    region: process.env.AWS_REGION || 'auto',
    ...(endpoint && { endpoint, forcePathStyle: true }),
    ...(accessKeyId && secretAccessKey && {
      credentials: { accessKeyId, secretAccessKey },
    }),
  });
}
```

The client is cached as a singleton in `lib/s3.ts` with `resetS3Client()` for auth error recovery.

### Pattern 2: File Upload with Retry and Timeout

```typescript
// lib/s3.ts
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";

export async function uploadFile(
  buffer: Buffer,
  fileName: string,
  isPublic: boolean = false,
  timeoutMs: number = 120000,
  retries: number = 2
): Promise<string> {
  const { bucketName, folderPrefix } = getBucketConfig();

  // Generate S3 key
  const timestamp = Date.now();
  const sanitizedFileName = fileName.replace(/[^a-zA-Z0-9.-]/g, "_");
  const cloud_storage_path = isPublic
    ? `${folderPrefix}public/uploads/${timestamp}-${sanitizedFileName}`
    : `${folderPrefix}uploads/${timestamp}-${sanitizedFileName}`;

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const command = new PutObjectCommand({
        Bucket: bucketName,
        Key: cloud_storage_path,
        Body: buffer,
        ContentType: getContentType(fileName),
      });

      // Race between upload and timeout
      const timeoutPromise = new Promise<never>((_, reject) => {
        setTimeout(() => reject(new Error(`S3 upload timeout after ${timeoutMs}ms`)), timeoutMs);
      });

      await Promise.race([getS3Client().send(command), timeoutPromise]);
      return cloud_storage_path;
    } catch (error) {
      if (isS3AuthError(error)) {
        resetS3Client();  // Reset client on auth errors
      }
      if (attempt < retries) {
        await new Promise(resolve => setTimeout(resolve, (attempt + 1) * 1000));
      }
    }
  }
  throw new Error(`S3 upload failed after ${retries + 1} attempts`);
}
```

### Pattern 3: Presigned Upload URLs

Generate presigned URLs for direct browser-to-S3 uploads:

```typescript
import { PutObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

export async function generatePresignedUploadUrl(
  fileName: string,
  contentType: string,
  isPublic: boolean = false,
  expiresIn: number = 3600
): Promise<{ uploadUrl: string; cloud_storage_path: string }> {
  const { bucketName, folderPrefix } = getBucketConfig();

  const timestamp = Date.now();
  const sanitizedFileName = fileName.replace(/[^a-zA-Z0-9.-]/g, "_");
  const cloud_storage_path = isPublic
    ? `${folderPrefix}public/uploads/${timestamp}-${sanitizedFileName}`
    : `${folderPrefix}uploads/${timestamp}-${sanitizedFileName}`;

  const command = new PutObjectCommand({
    Bucket: bucketName,
    Key: cloud_storage_path,
    ContentType: contentType,
  });

  const uploadUrl = await getSignedUrl(getS3Client(), command, { expiresIn });
  return { uploadUrl, cloud_storage_path };
}
```

### Pattern 4: File Download and Signed URL Generation

```typescript
import { GetObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

// Get URL for accessing a file
export async function getFileUrl(
  cloud_storage_path: string,
  isPublic: boolean,
  expiresIn: number = 3600
): Promise<string> {
  const { bucketName } = getBucketConfig();

  if (isPublic && !process.env.S3_ENDPOINT) {
    // AWS-style public URL (not R2)
    return `https://${bucketName}.s3.${AWS_REGION}.amazonaws.com/${cloud_storage_path}`;
  }
  // Generate signed URL
  const command = new GetObjectCommand({ Bucket: bucketName, Key: cloud_storage_path });
  return await getSignedUrl(getS3Client(), command, { expiresIn });
}

// Download file as Buffer
export async function downloadFile(cloud_storage_path: string): Promise<Buffer> {
  const { bucketName } = getBucketConfig();
  const command = new GetObjectCommand({ Bucket: bucketName, Key: cloud_storage_path });
  const response = await getS3Client().send(command);

  const chunks: Uint8Array[] = [];
  const stream = response.Body as NodeJS.ReadableStream;
  return new Promise((resolve, reject) => {
    stream.on('data', (chunk: Uint8Array) => chunks.push(chunk));
    stream.on('end', () => resolve(Buffer.concat(chunks)));
    stream.on('error', reject);
  });
}
```

### Pattern 5: Virus Scanning (VirusTotal)

Graceful degradation when API key is not configured:

```typescript
// lib/virus-scanner.ts
interface VirusScanResult {
  clean: boolean;
  engine: string;
  threat?: string;
  scanId?: string;
  timestamp: Date;
}

export async function scanFileBuffer(
  buffer: Buffer,
  fileName: string,
  options?: { timeout?: number; skipIfMissingKey?: boolean }
): Promise<VirusScanResult> {
  const apiKey = process.env.VIRUSTOTAL_API_KEY;

  // Graceful degradation if API key missing
  if (!apiKey) {
    if (options?.skipIfMissingKey ?? true) {
      return { clean: true, engine: 'none', timestamp: new Date() };
    }
    throw new Error('VirusTotal API key not configured');
  }

  // Upload to VirusTotal with timeout
  const form = new FormData();
  form.append('file', buffer, { filename: fileName });

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), options?.timeout || 30000);

  const response = await fetch('https://www.virustotal.com/api/v3/files', {
    method: 'POST',
    headers: { 'x-apikey': apiKey, ...form.getHeaders() },
    body: form as any,
    signal: controller.signal,
  });
  clearTimeout(timeoutId);

  // Handle rate limiting gracefully
  if (response.status === 429) {
    return { clean: true, engine: 'virustotal', timestamp: new Date() };
  }

  const result = await response.json();
  const scanId = result.data?.id;

  // Poll for results
  return await getScanResult(scanId);
}
```

### Pattern 6: OneDrive Integration

Per-project document sync via Microsoft Graph API:

```typescript
// lib/onedrive-service.ts
export class OneDriveService {
  private accessToken: string;
  private projectId: string;

  private static readonly CLIENT_ID = process.env.ONEDRIVE_CLIENT_ID || '';
  private static readonly CLIENT_SECRET = process.env.ONEDRIVE_CLIENT_SECRET || '';
  private static readonly TENANT_ID = process.env.ONEDRIVE_TENANT_ID || 'common';

  // Factory method
  static async fromProject(projectId: string): Promise<OneDriveService> {
    // Load tokens from database
    const project = await prisma.project.findUnique({
      where: { id: projectId },
      select: {
        oneDriveAccessToken: true,
        oneDriveRefreshToken: true,
        oneDriveTokenExpiry: true,
        oneDriveFolderId: true,
      },
    });
    return new OneDriveService({ projectId, ...project });
  }

  // Sync files from OneDrive folder
  async syncFolder(): Promise<SyncResult> { /* ... */ }

  // Upload file to OneDrive
  async uploadFile(buffer: Buffer, fileName: string, folderId?: string) { /* ... */ }
}
```

### Pattern 7: Photo Retention Service

7-day tiered retention with OneDrive archival:

```typescript
// lib/photo-retention-service.ts
export interface PhotoMeta {
  s3Key: string;
  fileName: string;
  uploadedAt: string;
  expiresAt: string;
  onedriveSynced?: boolean;
  thumbnailKey?: string;
  fullResDeleted?: boolean;
  size?: number;
}

// Add expiration metadata to photos
export function addExpirationToPhotos(
  photos: Array<{ s3Key: string; fileName: string }>,
  retentionDays: number = 7
): PhotoMeta[] {
  const now = new Date();
  return photos.map(photo => ({
    ...photo,
    uploadedAt: now.toISOString(),
    expiresAt: new Date(now.getTime() + retentionDays * 24 * 60 * 60 * 1000).toISOString(),
    onedriveSynced: false,
  }));
}

// Generate thumbnail S3 key
export function generateThumbnailKey(s3Key: string): string {
  const lastDot = s3Key.lastIndexOf('.');
  if (lastDot === -1) return `${s3Key}-thumb`;
  return `${s3Key.substring(0, lastDot)}-thumb${s3Key.substring(lastDot)}`;
}
```

## Content Type Mapping

```typescript
function getContentType(fileName: string): string {
  const ext = fileName.split(".").pop()?.toLowerCase();
  const contentTypes: Record<string, string> = {
    pdf: "application/pdf",
    docx: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    doc: "application/msword",
    xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    xls: "application/vnd.ms-excel",
    png: "image/png",
    jpg: "image/jpeg",
    jpeg: "image/jpeg",
    gif: "image/gif",
    txt: "text/plain",
    csv: "text/csv",
  };
  return contentTypes[ext || ""] || "application/octet-stream";
}
```

## Environment Variables

```bash
# S3 / Cloudflare R2
S3_ENDPOINT=https://<account-id>.r2.cloudflarestorage.com  # Required for R2
AWS_REGION=auto                     # 'auto' for R2, region for S3
AWS_BUCKET_NAME=foremanos-documents
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>
AWS_FOLDER_PREFIX=foremanos/        # Optional prefix

# Virus Scanning
VIRUSTOTAL_API_KEY=<key>            # Optional, graceful degradation

# OneDrive
ONEDRIVE_CLIENT_ID=<id>
ONEDRIVE_CLIENT_SECRET=<secret>
ONEDRIVE_TENANT_ID=common
```

## Key Files

| File | Purpose |
|------|---------|
| `lib/aws-config.ts` | S3 client creation, bucket config, connectivity test |
| `lib/s3.ts` | Upload, download, delete, presigned URLs, content types |
| `lib/virus-scanner.ts` | VirusTotal integration with graceful degradation |
| `lib/onedrive-service.ts` | OneDrive sync via Microsoft Graph API |
| `lib/photo-retention-service.ts` | 7-day photo retention with archival |
| `lib/daily-report-onedrive-sync.ts` | Auto-upload reports to OneDrive on approval |
| `app/api/documents/presign/route.ts` | Presigned URL API endpoint |
| `app/api/conversations/[id]/photos/presigned/route.ts` | Photo upload presigned URLs |

## Anti-Patterns

- **Never use `forcePathStyle: false` with R2** — Cloudflare R2 requires `forcePathStyle: true`.
- **Don't hardcode bucket names** — Always use `getBucketConfig()`.
- **Don't skip virus scanning in production** — Even with graceful degradation, log security events.
- **Don't create presigned URLs with long expiry** — Default to 1 hour (3600s), maximum 7 days.
- **Don't upload without sanitizing filenames** — Use `fileName.replace(/[^a-zA-Z0-9.-]/g, "_")`.
- **Don't ignore S3 auth errors** — Call `resetS3Client()` on 403/auth failures for credential rotation.

## Quick Reference

```typescript
// Upload file
const path = await uploadFile(buffer, 'doc.pdf', false);

// Get signed download URL
const url = await getFileUrl(path, false, 3600);

// Generate presigned upload URL
const { uploadUrl, cloud_storage_path } = await generatePresignedUploadUrl('doc.pdf', 'application/pdf');

// Delete file
await deleteFile(cloud_storage_path);

// Download file
const buffer = await downloadFile(cloud_storage_path);

// Scan file for viruses
const result = await scanFileBuffer(buffer, 'upload.pdf');
if (!result.clean) { /* reject upload */ }
```
