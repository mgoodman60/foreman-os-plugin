---
name: pdf-generation
description: ForemanOS PDF generation patterns. Use when creating PDFs with @react-pdf/renderer, filling PDF forms with pdf-lib, or generating daily report PDFs.
---

# PDF Generation for ForemanOS

## When to Use This Skill
- Creating new PDF report templates
- Generating daily report PDFs
- Filling PDF form fields (G702/G703, AIA documents)
- Building bulk export PDFs (room sheets, project summaries)
- Debugging PDF rendering issues

## Core Patterns

### Pattern 1: React PDF Components (@react-pdf/renderer)

ForemanOS uses `@react-pdf/renderer` for all new PDF generation. The main template is `lib/pdf-template.tsx`:

```tsx
import React from 'react';
import {
  Document,
  Page,
  Text,
  View,
  Image,
  StyleSheet,
  Font,
  pdf,
} from '@react-pdf/renderer';

// Register custom fonts
Font.register({
  family: 'Roboto',
  fonts: [
    { src: 'https://cdnjs.cloudflare.com/ajax/libs/ink/3.1.10/fonts/Roboto/roboto-light-webfont.ttf', fontWeight: 300 },
    { src: 'https://cdnjs.cloudflare.com/ajax/libs/ink/3.1.10/fonts/Roboto/roboto-regular-webfont.ttf', fontWeight: 400 },
    { src: 'https://cdnjs.cloudflare.com/ajax/libs/ink/3.1.10/fonts/Roboto/roboto-medium-webfont.ttf', fontWeight: 500 },
    { src: 'https://cdnjs.cloudflare.com/ajax/libs/ink/3.1.10/fonts/Roboto/roboto-bold-webfont.ttf', fontWeight: 700 },
  ],
});

// Define styles
const styles = StyleSheet.create({
  page: {
    fontFamily: 'Roboto',
    fontSize: 10,
    paddingTop: 30,
    paddingBottom: 60,
    paddingHorizontal: 40,
    backgroundColor: '#FFFFFF',
  },
  sectionTitle: {
    fontSize: 14,
    fontWeight: 700,
    color: '#1F2328',
    marginBottom: 8,
    paddingBottom: 4,
    borderBottom: '1 solid #E5E7EB',
  },
  // ... more styles
});

// Export the main document component
export const DailyReportPDF: React.FC<{ data: DailyReportData }> = ({ data }) => (
  <Document>
    <Page size="LETTER" style={styles.page}>
      <Header data={data} />
      <WeatherSection snapshots={data.weatherSnapshots} />
      <WorkSection work={data.workPerformed} totalCrew={data.totalCrewSize} />
      <PhotosSection photos={data.photos} />
      <MaterialsSection materials={data.materialDeliveries} />
      <Footer preparedBy={data.preparedBy} date={data.finalizationDate} />
      <Text style={styles.pageNumber}
        render={({ pageNumber, totalPages }) => `Page ${pageNumber} of ${totalPages}`}
        fixed
      />
    </Page>
  </Document>
);
```

### Pattern 2: Server-Side PDF Rendering

Generate PDF buffer on the server and upload to S3:

```typescript
// lib/report-finalization/pdf-generation.ts
export async function generateReportPDF(conversationId: string): Promise<string> {
  const ReactPDF = await import('@react-pdf/renderer');
  const React = await import('react');
  const { DailyReportPDF } = await import('../pdf-template');
  const { uploadFile } = await import('../s3');

  // Gather data from database
  const conversation = await prisma.conversation.findUnique({
    where: { id: conversationId },
    include: { Project: true, User: true },
  });

  // Prepare photo URLs (convert S3 paths to signed URLs)
  const photos = (conversation.photos as PhotoEntry[]) || [];
  const photoData = await Promise.all(
    photos.map(async (photo) => {
      const url = await getFileUrl(photo.cloud_storage_path, false);
      return { id: photo.id, url, caption: photo.caption };
    })
  );

  // Build PDF data object
  const pdfData = {
    projectName: conversation.Project?.name || 'Project',
    reportDate: format(new Date(conversation.dailyReportDate), 'MMMM dd, yyyy'),
    photos: photoData.length > 0 ? photoData : undefined,
    preparedBy: conversation.User?.username || 'System',
    finalizationDate: format(new Date(), 'MMMM dd, yyyy h:mm a'),
    // ... other fields
  };

  // Render to buffer
  const pdfBuffer = await ReactPDF.renderToBuffer(
    React.createElement(DailyReportPDF, { data: pdfData }) as React.ReactElement
  );

  // Upload to S3
  const fileName = `daily-report-${conversation.Project?.slug}-${reportDate}.pdf`;
  const cloud_storage_path = await uploadFile(pdfBuffer, fileName, false);

  return cloud_storage_path;
}
```

### Pattern 3: PDF Form Filling with pdf-lib

For filling existing PDF forms (AIA G702/G703, inspection forms):

```typescript
import { PDFDocument, PDFForm, PDFTextField, PDFCheckBox, PDFRadioGroup } from 'pdf-lib';

export async function fillPdfForm(
  pdfBuffer: Buffer,
  data: TemplateData
): Promise<Buffer> {
  const pdfDoc = await PDFDocument.load(pdfBuffer);
  const form: PDFForm = pdfDoc.getForm();
  const fields = form.getFields();

  for (const field of fields) {
    const fieldName = field.getName();
    // Normalize field name for matching
    const normalizedFieldName = fieldName.toLowerCase().replace(/[-\s]/g, '_');

    const dataKey = Object.keys(data).find(
      key => key.toLowerCase() === normalizedFieldName
    );

    if (!dataKey || data[dataKey] === null || data[dataKey] === undefined) continue;

    const value = data[dataKey];

    if (field instanceof PDFTextField) {
      (field as PDFTextField).setText(String(value));
    } else if (field instanceof PDFCheckBox) {
      value ? (field as PDFCheckBox).check() : (field as PDFCheckBox).uncheck();
    } else if (field instanceof PDFRadioGroup) {
      const options = (field as PDFRadioGroup).getOptions();
      const match = options.find(opt => opt.toLowerCase() === String(value).toLowerCase());
      if (match) (field as PDFRadioGroup).select(match);
    }
  }

  const filledPdfBytes = await pdfDoc.save();
  return Buffer.from(filledPdfBytes);
}
```

### Pattern 4: Client-Side PDF Generation

For browser-side PDF generation (room sheets, exports):

```typescript
import { Document, Page, Text, View, StyleSheet, pdf } from '@react-pdf/renderer';

export async function generateRoomSheetPDF(data: RoomSheetData): Promise<Blob> {
  const pdfDoc = (
    <Document>
      <Page size="LETTER" style={styles.page}>
        <Text style={styles.title}>{data.project.name}</Text>
        <Text style={styles.heading}>{roomTitle}</Text>
        {/* ... room details, tables, etc. */}
      </Page>
    </Document>
  );

  const blob = await pdf(pdfDoc).toBlob();
  return blob;
}
```

### Pattern 5: Photo Pagination in PDFs

Split photos into pages of 4, with page break between groups:

```tsx
const PhotosSection: React.FC<{ photos?: Photo[] }> = ({ photos }) => {
  if (!photos || photos.length === 0) return null;

  const photosPerPage = 4;
  const photoPages = [];
  for (let i = 0; i < photos.length; i += photosPerPage) {
    photoPages.push(photos.slice(i, i + photosPerPage));
  }

  return (
    <>
      {photoPages.map((pagePhotos, pageIndex) => (
        <View key={`photo-page-${pageIndex}`} style={styles.section}
          wrap={false} break={pageIndex > 0}>
          <Text style={styles.sectionTitle}>
            Progress Photos {photoPages.length > 1
              ? `(Page ${pageIndex + 1} of ${photoPages.length})` : ''}
          </Text>
          <View style={styles.photoGrid}>
            {pagePhotos.map((photo) => (
              <View key={photo.id} style={styles.photoContainer}>
                <Image src={photo.url} style={styles.photo} />
                <Text style={styles.photoCaption}>{photo.caption}</Text>
              </View>
            ))}
          </View>
        </View>
      ))}
    </>
  );
};
```

### Pattern 6: Table Rendering in PDFs

```tsx
const styles = StyleSheet.create({
  table: { marginTop: 8 },
  tableRow: {
    flexDirection: 'row',
    borderBottom: '1 solid #E5E7EB',
    paddingVertical: 6,
  },
  tableHeader: {
    backgroundColor: '#F3F4F6',
    borderBottom: '1 solid #D1D5DB',
    fontWeight: 500,
  },
  tableCell: {
    flex: 1,
    fontSize: 9,
    color: '#1F2937',
    paddingHorizontal: 4,
  },
});

// Usage:
<View style={styles.table}>
  <View style={[styles.tableRow, styles.tableHeader]}>
    <Text style={[styles.tableCell, { flex: 1.2 }]}>Subcontractor</Text>
    <Text style={[styles.tableCell, { flex: 2 }]}>Material</Text>
    <Text style={[styles.tableCell, { flex: 1 }]}>Quantity</Text>
  </View>
  {materials.map((item, index) => (
    <View key={index} style={styles.tableRow}>
      <Text style={[styles.tableCell, { flex: 1.2 }]}>{item.sub}</Text>
      <Text style={[styles.tableCell, { flex: 2 }]}>{item.material}</Text>
      <Text style={[styles.tableCell, { flex: 1 }]}>{item.quantity}</Text>
    </View>
  ))}
</View>
```

## Data Types

### DailyReportData (PDF input)

```typescript
interface DailyReportData {
  projectName: string;
  projectAddress?: string;
  reportDate: string;
  projectManager?: string;
  superintendent?: string;
  client?: string;
  companyName?: string;
  companyLogo?: string;          // URL to logo image
  weatherSnapshots?: WeatherSnapshot[];
  workPerformed?: WorkEntry[];
  totalCrewSize?: number;
  photos?: Photo[];               // URLs must be pre-signed
  materialDeliveries?: MaterialDelivery[];
  equipment?: Equipment[];
  scheduleUpdates?: ScheduleUpdate[];
  quantityCalculations?: QuantityCalculation[];
  notes?: string;
  preparedBy: string;
  finalizationDate: string;
}
```

## Key Files

| File | Purpose |
|------|---------|
| `lib/pdf-template.tsx` | Daily report PDF component (header, weather, work, photos, tables, footer) |
| `lib/report-finalization/pdf-generation.ts` | Server-side PDF render + S3 upload |
| `lib/template-processor.ts` | PDF form filling with pdf-lib (`fillPdfForm`) |
| `lib/room-pdf-generator.tsx` | Room sheet PDF (finish schedule, MEP, takeoffs) |
| `lib/room-bulk-export.tsx` | Multi-room PDF/DOCX bulk export |
| `lib/project-summary-report.tsx` | Project status summary PDF |
| `app/api/conversations/[id]/generate-daily-report-pdf/route.ts` | API endpoint for PDF generation |

## Anti-Patterns

- **Never use jsPDF** — The project migrated away from jsPDF to `@react-pdf/renderer`. All new PDFs must use React PDF.
- **Never hardcode S3 URLs in PDFs** — Always use `getFileUrl()` to generate signed URLs for images.
- **Don't render PDFs in API routes directly** — Use the finalization pipeline in `lib/report-finalization/`.
- **Don't skip font registration** — Missing fonts cause rendering failures. Always register Roboto.
- **Don't embed large images without size constraints** — Use `objectFit: 'cover'` and fixed dimensions.

## Quick Reference

```typescript
// Server-side render to buffer
const buffer = await ReactPDF.renderToBuffer(
  React.createElement(MyPDF, { data }) as React.ReactElement
);

// Client-side render to blob
const blob = await pdf(<MyPDF data={data} />).toBlob();

// Fill existing PDF form
const filled = await fillPdfForm(templateBuffer, templateData);

// Upload generated PDF to S3
const path = await uploadFile(buffer, 'report.pdf', false);
```
