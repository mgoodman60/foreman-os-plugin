# MCP Tools for Document Extraction

Reference guide for MCP server tools that enhance the 5-phase extraction pipeline. These tools are optional — the pipeline works without them — but they improve quality, speed, and traceability when available.

## PDF Tools MCP

**Server**: `PDF Tools - Analyze, Extract, Fill, Compare`

### Available Tools

| Tool | Use During | Purpose |
|------|-----------|---------|
| `read_pdf_content` | Phase 1 (Index & Classify) | Pre-validate PDF structure: page count, text layer presence, form fields |
| `read_pdf_fields` | Phase 2 (Extract) | Extract form field data from submittal packages without rendering |
| `list_pdfs` | Phase 1 (Index & Classify) | Inventory documents in a directory before classification |
| `validate_pdf` | Phase 2 (Extract) | Check if all required form fields are populated |

### When to Use
- **Before Phase 1**: Run `list_pdfs` on project folders to build document inventory
- **During Phase 1**: Run `read_pdf_content` on each document to classify (faster than full rendering for text-heavy docs like specs and contracts)
- **During Phase 2**: Use `read_pdf_fields` for submittal packages that have form fields (avoids OCR entirely)

### Example Workflow
```
Phase 1: list_pdfs → classify each → build batch plan
Phase 2: For specs/contracts → read_pdf_content (text extraction, no rendering needed)
         For plan sheets → Claude Vision (image analysis required)
         For submittals with forms → read_pdf_fields (direct field extraction)
```

## PDF Display MCP

**Server**: `PDF Display`

### Available Tools

| Tool | Use During | Purpose |
|------|-----------|---------|
| `display_pdf` | Phase 3-4 (Cross-Reference, Remediate) | Interactive PDF viewer for conflict resolution |
| `list_pdfs` | Any phase | List available PDFs for display |

### When to Use
- **Phase 3 exit (PM review gate)**: Display source documents when presenting cross-reference conflicts to PM
- **Phase 4 (Remediate)**: Show original document alongside extracted data for PM verification of financial/schedule/safety conflicts

## Cloudflare D1 (Extraction State Database)

**Server**: Cloudflare MCP

For projects with 100+ documents or multi-session extraction, use D1 to persist extraction state beyond context window limits.

### Schema

```sql
-- Extraction runs
CREATE TABLE extraction_runs (
  run_id TEXT PRIMARY KEY,
  project_code TEXT NOT NULL,
  phase INTEGER NOT NULL,
  started_at TEXT NOT NULL,
  completed_at TEXT,
  status TEXT DEFAULT 'in_progress',
  documents_total INTEGER,
  documents_processed INTEGER DEFAULT 0
);

-- Per-document progress
CREATE TABLE document_progress (
  doc_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES extraction_runs(run_id),
  filename TEXT NOT NULL,
  type TEXT,
  page_count INTEGER,
  phase INTEGER DEFAULT 1,
  status TEXT DEFAULT 'pending',
  confidence REAL,
  last_updated TEXT
);

-- Conflicts for PM review
CREATE TABLE conflicts (
  conflict_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES extraction_runs(run_id),
  file TEXT NOT NULL,
  field TEXT NOT NULL,
  value_a TEXT,
  source_a TEXT,
  value_b TEXT,
  source_b TEXT,
  resolution TEXT,
  resolved_at TEXT
);
```

### Available Tools

| Tool | Use During | Purpose |
|------|-----------|---------|
| `d1_database_create` | Setup | Create extraction state database |
| `d1_database_query` | All phases | Read/write extraction state |

### When to Use
- **Project setup**: Create D1 database for projects with 100+ documents
- **Phase transitions**: Log phase entry/exit with timestamps
- **Multi-session extraction**: Resume from last known state instead of re-scanning
- **Conflict tracking**: Persist conflicts for PM review across sessions

### Setup
```
1. mcp__cloudflare__d1_database_create(name: "{project_code}_extraction")
2. Run CREATE TABLE statements above
3. Insert extraction_run record at pipeline start
4. Update document_progress as each document completes
```

## Cloudflare R2 (Render Archive)

**Server**: Cloudflare MCP

Store rendered PNG pages for debugging and reprocessing.

### Available Tools

| Tool | Use During | Purpose |
|------|-----------|---------|
| `r2_bucket_create` | Setup | Create render archive bucket |

### When to Use
- **Large plan sets (50+ sheets)**: Cache rendered PNGs to avoid re-rendering on re-extraction
- **Debugging**: Preserve the exact image that Claude Vision analyzed for traceability
- **Naming convention**: `{project_code}/{sheet_id}_{dpi}dpi.png`

### Note
R2 upload requires the Cloudflare Workers API — rendered PNGs are typically stored locally during extraction and optionally archived to R2 afterward for long-term storage.

## Playwright MCP (Visual Verification)

**Server**: Playwright

### When to Use
- **Phase 5 (post-normalization)**: If the project has a web dashboard, use Playwright to screenshot the dashboard showing extraction results for visual verification
- **Not used during extraction itself** — Playwright is for web page interaction, not document processing

## Integration Priority

| MCP Server | Priority | Reason |
|-----------|----------|--------|
| PDF Tools | **High** | Directly improves Phase 1 classification speed and Phase 2 form extraction |
| PDF Display | **Medium** | Enhances PM review during Phases 3-4 |
| Cloudflare D1 | **Medium** | Essential for 100+ doc projects; optional for smaller ones |
| Cloudflare R2 | **Low** | Nice-to-have for render caching; local storage usually sufficient |
| Playwright | **Low** | Post-extraction verification only |

## Availability Check

Before using any MCP tool in the pipeline, verify the server is connected:
- If the tool call fails with a connection error, skip and use the fallback approach
- Never block extraction because an MCP server is unavailable
- Log which MCP tools were available for the extraction summary report
