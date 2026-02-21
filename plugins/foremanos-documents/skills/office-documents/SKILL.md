---
name: office-documents
description: ForemanOS Office document patterns. Use when generating DOCX with docxtemplater, XLSX with xlsx-populate, or processing document templates.
---

# Office Document Generation for ForemanOS

## When to Use This Skill
- Creating DOCX documents from templates (daily reports, room sheets)
- Processing XLSX spreadsheets with template variables
- Building DOCX files from scratch with PizZip
- Working with the template processor pipeline

## Core Patterns

### Pattern 1: DOCX Template Processing with Docxtemplater

Fill DOCX templates with data using `{{variable}}` placeholders:

```typescript
import Docxtemplater from 'docxtemplater';
import PizZip from 'pizzip';

export async function processDocxTemplate(
  templateBuffer: Buffer,
  data: TemplateData
): Promise<Buffer> {
  // Load the template
  const zip = new PizZip(templateBuffer);
  const doc = new Docxtemplater(zip, {
    paragraphLoop: true,
    linebreaks: true,
    nullGetter: () => '',  // Return empty string for null/undefined values
  });

  // Set the template data
  doc.setData(data);

  // Render the document
  doc.render();

  // Generate the output
  const output = doc.getZip().generate({
    type: 'nodebuffer',
    compression: 'DEFLATE',
  });

  return output;
}
```

### Pattern 2: XLSX Template Processing with xlsx-populate

Fill XLSX spreadsheets by replacing `{{variable}}` patterns in cells:

```typescript
export async function processXlsxTemplate(
  templateBuffer: Buffer,
  data: TemplateData
): Promise<Buffer> {
  const XlsxPopulate = require('xlsx-populate');

  // Load the workbook
  const workbook = await XlsxPopulate.fromDataAsync(templateBuffer);

  // Replace variables in all sheets
  workbook.sheets().forEach((sheet: any) => {
    sheet.usedRange().forEach((cell: any) => {
      const value = cell.value();
      if (typeof value === 'string') {
        let newValue = value;
        Object.keys(data).forEach(key => {
          const regex = new RegExp(`{{\\s*${key}\\s*}}`, 'g');
          newValue = newValue.replace(regex, String(data[key] || ''));
        });
        if (newValue !== value) {
          cell.value(newValue);
        }
      }
    });
  });

  const output = await workbook.outputAsync();
  return output;
}
```

### Pattern 3: Building DOCX from Scratch with PizZip

For programmatic DOCX creation without a template (room sheets, exports):

```typescript
import PizZip from 'pizzip';

export async function generateDocx(data: RoomSheetData): Promise<Blob> {
  const zip = new PizZip();

  // [Content_Types].xml
  zip.file('[Content_Types].xml', `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>`);

  // _rels/.rels
  zip.file('_rels/.rels', `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
    Target="word/document.xml"/>
</Relationships>`);

  // word/_rels/document.xml.rels
  zip.file('word/_rels/document.xml.rels', `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
    Target="styles.xml"/>
</Relationships>`);

  // word/styles.xml (with ForemanOS brand color #F97316)
  zip.file('word/styles.xml', stylesXml);

  // word/document.xml (generated from data)
  zip.file('word/document.xml', generateDocumentXml(data));

  return zip.generate({
    type: 'blob',
    mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  });
}
```

### Pattern 4: XML Table Generation for DOCX

Helper for creating Word tables in raw XML:

```typescript
function escapeXml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function createTable(headers: string[], rows: string[][]): string {
  const colCount = headers.length;
  const colWidth = Math.floor(9000 / colCount);

  let xml = '<w:tbl>';
  xml += '<w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="5000" w:type="pct"/></w:tblPr>';

  // Grid columns
  xml += '<w:tblGrid>';
  for (let i = 0; i < colCount; i++) {
    xml += `<w:gridCol w:w="${colWidth}"/>`;
  }
  xml += '</w:tblGrid>';

  // Header row (gray background)
  xml += '<w:tr>';
  headers.forEach(h => {
    xml += `<w:tc><w:tcPr><w:shd w:val="clear" w:fill="F0F0F0"/></w:tcPr>`;
    xml += `<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>${escapeXml(h)}</w:t></w:r></w:p></w:tc>`;
  });
  xml += '</w:tr>';

  // Data rows
  rows.forEach(row => {
    xml += '<w:tr>';
    row.forEach(cell => {
      xml += `<w:tc><w:p><w:r><w:t>${escapeXml(cell || '-')}</w:t></w:r></w:p></w:tc>`;
    });
    xml += '</w:tr>';
  });

  xml += '</w:tbl>';
  return xml;
}
```

### Pattern 5: Template Processing Pipeline

The unified template processor handles DOCX, XLSX, and PDF:

```typescript
// lib/template-processor.ts
export async function processTemplateById(
  templateId: string,
  data: TemplateData
): Promise<{ buffer: Buffer; filename: string; contentType: string }> {
  // Get template from database
  const template = await prisma.documentTemplate.findUnique({
    where: { id: templateId },
  });

  // Download template from S3
  const templateUrl = await getFileUrl(template.cloud_storage_path, template.isPublic);
  const response = await fetch(templateUrl);
  const templateBuffer = Buffer.from(await response.arrayBuffer());

  // Process based on file format
  switch (template.fileFormat.toLowerCase()) {
    case 'docx':
      return {
        buffer: await processDocxTemplate(templateBuffer, data),
        filename: `${template.name}_${timestamp}.docx`,
        contentType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      };
    case 'xlsx':
      return {
        buffer: await processXlsxTemplate(templateBuffer, data),
        filename: `${template.name}_${timestamp}.xlsx`,
        contentType: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      };
    case 'pdf':
      return {
        buffer: await fillPdfForm(templateBuffer, data),
        filename: `${template.name}_${timestamp}.pdf`,
        contentType: 'application/pdf',
      };
  }
}
```

### Pattern 6: Template Data Extraction

Extract data from daily report conversations for template filling:

```typescript
export async function extractDailyReportData(
  conversationId: string
): Promise<TemplateData> {
  const conversation = await prisma.conversation.findUnique({
    where: { id: conversationId },
  });

  const project = conversation.projectId
    ? await prisma.project.findUnique({
        where: { id: conversation.projectId },
        include: { User_Project_ownerIdToUser: { select: { username: true } } },
      })
    : null;

  // Extract from JSON fields
  const reportData = (conversation.reportData as ReportData) || {};
  const weatherSnapshots = (conversation.weatherSnapshots as WeatherSnapshot[]) || [];
  const photos = (conversation.photos as PhotoEntry[]) || [];

  return {
    project_name: project?.name || 'Unknown Project',
    report_date: new Date(conversation.dailyReportDate).toLocaleDateString(),
    crew_size: reportData.crewSize || 0,
    weather_condition: weatherSnapshots[weatherSnapshots.length - 1]?.condition || '',
    photo_count: photos.length,
    // ... more fields
  };
}
```

## TemplateData Interface

```typescript
export interface TemplateData {
  project_name?: string;
  project_address?: string;
  report_date?: string;
  report_title?: string;
  weather_condition?: string;
  weather_temperature?: string;
  crew_size?: number;
  hours_worked?: number;
  tasks_completed?: string;
  work_description?: string;
  percent_complete?: number;
  materials_delivered?: string;
  equipment_used?: string;
  safety_incidents?: number;
  photo_count?: number;
  additional_notes?: string;
  [key: string]: any;  // Extensible
}
```

## Key Files

| File | Purpose |
|------|---------|
| `lib/template-processor.ts` | Unified template processor (DOCX, XLSX, PDF form filling) |
| `lib/room-docx-generator.ts` | Room sheet DOCX with PizZip (tables, styles, XML) |
| `lib/room-bulk-export.tsx` | Multi-room PDF/DOCX bulk export |
| `lib/project-summary-report.tsx` | Project summary report (PDF/DOCX) |
| `lib/report-finalization/orchestrator.ts` | Report finalization pipeline |
| `lib/types/report-data.ts` | Type definitions for report data fields |

## Anti-Patterns

- **Never use `new Document()` from docx library** — ForemanOS uses `docxtemplater` + `PizZip`, not the `docx` npm package.
- **Don't forget `nullGetter: () => ''`** in Docxtemplater — Without this, undefined template vars throw errors.
- **Don't use `compression: 'STORE'`** — Always use `compression: 'DEFLATE'` for smaller output files.
- **Don't forget to escape XML** — Raw data in DOCX XML must be escaped with `escapeXml()`.
- **Don't use `xlsx` (SheetJS) library** — ForemanOS uses `xlsx-populate` for XLSX processing.

## Quick Reference

```typescript
// DOCX from template
const output = await processDocxTemplate(templateBuffer, data);

// XLSX from template
const output = await processXlsxTemplate(templateBuffer, data);

// DOCX from scratch
const blob = await generateRoomSheetDOCX(roomData);

// Process any template by ID
const { buffer, filename, contentType } = await processTemplateById(templateId, data);

// Extract report data for templates
const data = await extractDailyReportData(conversationId);
```
