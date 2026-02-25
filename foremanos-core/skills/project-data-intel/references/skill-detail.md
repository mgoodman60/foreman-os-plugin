# project-data-intel — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the project-data-intel skill.



## 5. Data Sources Reference Table

| # | JSON File | Dashboard Sections | Update Frequency | Size (typical) |
|---|-----------|-------------------|------------------|----------------|
| 1 | config.json | Dashboard, Header | 1x per setup | <5 KB |
| 2 | spatial.json | Grid Lines, Building Areas, Room Browser, Spatial Correlation | Geometry change | 20–50 KB |
| 3 | specs.json | PEMB/Structure, CFS, Concrete Mix Designs, MEP, Finishes, Doors & Hardware | Plan revision | 80–200 KB |
| 4 | schedule.json | Schedule & Critical Path, Procurement Gantt, Look-Ahead | Weekly update | 30–100 KB |
| 5 | directory.json | Project Directory (all contacts) | On-demand | 15–30 KB |
| 6 | submittals.json | Submittals Pipeline, Alerts | Daily update | 25–60 KB |
| 7 | procurement.json | Subcontracts & POs, Material Tracker, Procurement Alerts | Daily update | 40–120 KB |
| 8 | inspections.json | Hold Points, Test Results, Photo Log | Daily update | 50–150 KB |
| 9 | daily-reports.json | Daily Report Log (referenced, not embedded) | Daily | 100–500 KB |
| 10 | rfis.json | RFIs Pipeline, Trend Analysis | On-demand | 20–80 KB |
| 11 | meetings.json | Meeting Log, Decisions, Action Items | Weekly | 15–50 KB |
| 12 | change-orders.json | Change Orders, Cost Impact Analysis | On-demand | 10–40 KB |
| 13 | delays.json | Delays Log, Impact Analysis, Mitigation Tracking | On-demand | 15–50 KB |
| 14 | pay-apps.json | Pay Applications, Financials Summary, Waterfall Chart | Monthly | 20–80 KB |
| 15 | punch-list.json | Punch List, Phase-Based Closeout | On-demand | 30–100 KB |
| 16 | visual-context.json | Photo Gallery, Site Progress Timeline | Optional, on-demand | 50–200 KB |
| 17 | rendering-log.json | Renderings Gallery, AI Prompt History | Optional, on-demand | 20–100 KB |

**Total typical data.js size**: 400–2,000 KB (project-dependent)

---



## 7. Complete Sidebar Navigation

The sidebar is **dynamically rendered** based on data completeness. Sections with no data auto-hide.

### OVERVIEW (Always visible)
- **Dashboard** (role-based summary)
- **Alerts** (procurement, submittals, hold points)
- **Data Completeness** (% of sections populated)
- **Revision Tracker** (ASI/plan revision history)

### BUILDING DATA
- **Grid Lines** (X/Y reference grids)
- **Building Areas** (footprint, zones, by-type breakdown)
- **Room Browser** (fact sheets per room with cross-references)
- **Doors & Hardware** (schedule, hardware groups, supplier)
- **PEMB/Structure** (supplier, dimensions, frame data, reactions)
- **MEP Systems** (HVAC, Plumbing, Electrical, Fire, Specialty)
- **Site & Civil** (site plan, utilities, stormwater, pavement, geotech)

### QUANTITIES & COST
- **Material Takeoff** (room-by-room quantities)
- **Materials Dashboard** (inventory, consumption rate)
- **Bidding Analysis** (bid vs. quote vs. contract)
- **Material Calculator** (linear feet, square feet, count estimator)

### FINANCIALS
- **Financials Summary** (contract value, % complete, cost to date)
- **Subcontracts & POs** (all contracts, amounts, status)
- **Change Orders** (log, cost impact, trend)
- **Pay Applications** (history, retainage, earned value)

### SPECIFICATIONS
- **Spec Sections** (by CSI division, linked to details)
- **Concrete Mix Designs** (all mixes, testing schedule)
- **Field Tolerances** (by system: structure, MEP, finishes)
- **Weather Thresholds** (temp, wind, precipitation limits by phase)
- **Hold Points** (HP-001 through HP-007+, trigger/responsible/status)

### PROJECT CONTROLS
- **Schedule & Critical Path** (baseline Gantt, float analysis, CCP)
- **Procurement Gantt** (supplier timeline, material delivery window)
- **Submittals Pipeline** (all items, days in review, approvals pending)
- **RFIs** (log, trend, resolution time)
- **Permit Compliance** (permits, inspections required, status)

### DOCUMENTS
- **Sheet Index** (plan set index, revision level, uploaded date)
- **Plan Overlay Viewer** (Fabric.js-based grid/plan annotation)
- **ASI / Revision Log** (all ASIs, changes, impact)

### SPATIAL
- **Spatial Correlation** (D3 graph: rooms ↔ doors ↔ MEP ↔ finishes)
- **Progress Tracking** (% by phase, by trade, by location)

### TOOLS
- **Renderings Gallery** (AI-generated site images, progress mockups)
- **AI Chatbot** (ask questions, get context-aware answers)
- **Export/Print** (PDF, CSV, Excel, JSON)

### LOGS
- **Daily Report Log** (7+ existing reports, search, filter by date/superintendent)
- **Delays Log** (all delays, cause, impact, mitigation status)
- **Punch List** (by phase, by trade, by location, status tracker)
- **Meeting Notes** (decisions, action items, attendees)
- **Geotechnical** (bearing, settlement, testing results, compaction log)
- **SWPPP** (weekly inspections, rainfall events, corrective actions)

---



## 9. Role-Based Views

The dashboard adapts its **overview, sidebar order, and default alerts** based on the logged-in role. Role is selected in the header and persisted in localStorage.

### Superintendent View (Field-Focused)
**Dashboard overview**: Current phase, weather (today + 3-day forecast), today's hold points, crew on-site, active trades, active safety alerts.
**Sidebar priority order**:
1. Dashboard
2. Alerts
3. Schedule & Critical Path
4. Room Browser (current phase rooms)
5. Hold Points
6. Weather Thresholds
7. Daily Report Log
8. Inspections / Test Results
9. PEMB/Structure (if relevant phase)
10. MEP Systems (if rough-in phase)

**Key actions**: Log daily report, mark hold points complete, photo upload, weather override.

### Project Manager (Controls-Focused)
**Dashboard overview**: Budget status (contract vs. spent), submittals pending, RFIs open, change order log, next 3 milestones.
**Sidebar priority order**:
1. Dashboard
2. Alerts
3. Submittals Pipeline
4. Schedule & Critical Path
5. Procurement Gantt
6. Financials Summary
7. Change Orders
8. Pay Applications
9. RFIs
10. Material Tracker

**Key actions**: Approve submittals, process RFIs, log change orders, generate pay apps.

### Owner / Executive View
**Dashboard overview**: Percent complete (%) with photo gallery, project budget remaining, key milestones (planned vs. actual), cost-to-date summary.
**Sidebar priority order**:
1. Dashboard
2. Progress Tracking
3. Financials Summary
4. Schedule & Critical Path (milestones only)
5. Photo Gallery / Renderings
6. Punch List (closeout tracking)
7. Meeting Notes

**Key actions**: View progress photos, approve final payment, download project summary.

### Architect / Engineer View
**Dashboard overview**: Submittals awaiting review, RFIs to address, change order log (cost/schedule impact), drawing revisions (ASI log).
**Sidebar priority order**:
1. Dashboard
2. Alerts
3. RFIs
4. Submittals Pipeline
5. ASI / Revision Log
6. Spec Sections
7. Hold Points
8. Field Tolerances
9. Change Orders
10. Permit Compliance

**Key actions**: Review submittals, respond to RFIs, issue ASIs, approve hold point release.

---



## 10. AI Chatbot Integration

### Chatbot Component (Sidebar Widget)
Located in a collapsible panel at bottom of sidebar. Always accessible.

### Architecture
```javascript
const chatbotConfig = {
  model: 'claude-3-5-sonnet-20241022',
  maxTokens: 1024,
  systemPrompt: `
    You are the AI assistant for ${PROJECT_DATA.config.projectName}
    (${PROJECT_DATA.config.projectCode}), a ${PROJECT_DATA.config.buildingType} project
    in ${PROJECT_DATA.config.address}. You have access to comprehensive project data:
    - Building specifications and systems
    - Schedule and critical path
    - Submittals, RFIs, and change orders
    - Daily reports and field notes
    - Financial summaries and pay applications
    - Hold points and inspections
    - Permit and compliance status

    Answer questions accurately and concisely using the data context.
    Reference specific details (drawing numbers, specification sections,
    contract values, dates) when relevant. Always be factual; if data is
    missing or unclear, say so.
  `,
  contextInjection: {
    projectSummary: JSON.stringify(PROJECT_DATA.config),
    recentActivity: last7DailyReports,
    alertsSummary: currentAlerts,
    scheduleSnapshot: nextMilestonesAndCriticalPath,
    financialSnapshot: currentBudgetStatus
  }
};
```

### User Experience
1. **Suggested questions** (initially displayed):
   - "What is the critical path?"
   - "Show me overdue submittals"
   - "What's the weather forecast?"
   - "How much budget is remaining?"
   - "What are today's hold points?"
   - "What's the permit status?"

2. **Message history**: Scrollable list of user questions + AI responses, persisted in localStorage

3. **Features**:
   - Copy-to-clipboard button on each response
   - Export chat transcript to text file
   - Clear history button
   - Suggested follow-up questions auto-generated by AI

### API Call Pattern
```javascript
async function sendMessage(userMessage) {
  const messages = [
    { role: 'user', content: userMessage }
  ];

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': API_KEYS.anthropic,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
      'anthropic-dangerous-direct-browser-access': 'true'
    },
    body: JSON.stringify({
      model: chatbotConfig.model,
      max_tokens: chatbotConfig.maxTokens,
      system: chatbotConfig.systemPrompt,
      messages: messages
    })
  });

  const data = await response.json();
  return data.content[0].text;
}
```

### Offline Fallback
If API unavailable or key missing, chatbot switches to **keyword search engine**:
```javascript
function keywordSearch(query) {
  // Search PROJECT_DATA for matching sections
  const results = [];
  const keywords = query.toLowerCase().split(' ');

  // Search across all major sections
  for (const [section, data] of Object.entries(PROJECT_DATA)) {
    const serialized = JSON.stringify(data).toLowerCase();
    const matches = keywords.filter(kw => serialized.includes(kw)).length;
    if (matches > 0) {
      results.push({ section, matches, preview: extractPreview(data, keywords) });
    }
  }

  return results.sort((a, b) => b.matches - a.matches);
}
```

---



## 11. Color Palette & Styling

Consistent with Foreman OS v2.1 design system:

### Primary Colors
- **Navy** (#1B2A4A): Headers, sidebar, primary buttons
- **Blue** (#2E5EAA): Links, accents, hover states
- **Light Gray** (#F5F7FA): Background, card backgrounds
- **White** (#FFFFFF): Text on colored backgrounds

### Status Colors
- **Green** (#27AE60): Complete, approved, passed
- **Yellow/Amber** (#F39C12): In Progress, under review, caution
- **Red** (#E74C3C): Overdue, rejected, failed, critical
- **Gray** (#95A5A6): Pending, deferred, inactive

### Charts
- **S-curve / Earned Value**: Blue line (planned), Green line (actual)
- **Waterfall**: Green bars (positive), Red bars (negative), Gray connectors
- **Gantt bars**: Blue (standard), Red (critical path), Light gray (slack/float)

---



## 12. API Key Discovery & Injection

The `/data` command discovers API keys from multiple sources and injects them into `data.js`.

### Discovery Order (first match wins)
1. **Environment variables** (most secure):
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   export GEMINI_API_KEY="AIza..."
   export FLUX2_API_KEY="..."
   ```

2. **.env file** (project root):
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   GEMINI_API_KEY=AIza...
   FLUX2_API_KEY=...
   ```

3. **project-config.json** (project root or AI folder):
   ```json
   {
     "api_keys": {
       "anthropic": "sk-ant-...",
       "gemini": "AIza...",
       "flux2": "..."
     }
   }
   ```

### Security Notes
- **Keys NEVER written to disk** during browser operations
- Keys injected into `data.js` during **server-side generation only** (Foreman OS backend)
- Browser receives `data.js` with keys already embedded (read-only)
- Dashboard uses keys for **read-only API operations** (chatbot, rendering requests)
- Keys in localStorage only if user opts to "save" (not recommended for production)

### Fallback Behavior
If no keys discovered:
- Chatbot operates in **keyword search mode** (offline)
- Rendering gallery displays empty state with "Request API key" prompt
- All other dashboard functionality unaffected

---



## 13. Output & File Generation

### File Naming Convention
```
Project Code: MOSC-825021
Project Name: Morehead One Senior Care

Output Files (in "AI - Project Brain/" folder):
├── MOSC-825021_Data_Intel.html    ← Static template (generated once, ~10 KB)
├── MOSC-825021_data.js             ← Dynamic data payload (regenerated per run, 400–2,000 KB)
└── logs/
    └── data-intel-generation.log   ← Audit trail (append-only)
```

### First-Run Initialization
```bash
/data
# or
/data --init
```
1. Check if `{PROJECT_CODE}_Data_Intel.html` exists
2. If NO: Copy template from plugin → create file
3. Generate `{PROJECT_CODE}_data.js` from source JSON files
4. Log: "Dashboard created: {filename}, {size} KB, {section_count} sections"
5. Browser: Render dashboard, prompt user to save API keys (optional)

### Subsequent Runs
```bash
/data
# or
/data --refresh
```
1. Load existing `{PROJECT_CODE}_Data_Intel.html` (no changes)
2. Check `{PROJECT_CODE}_data.js` manifest
3. Compute MD5 hashes of source files
4. Selective regeneration (only changed sections)
5. Update `{PROJECT_CODE}_data.js`
6. Log: "Updated: {N} sections, {size_delta} KB"

### Log Format (data-intel-generation.log)
```
[2026-02-19T14:30:00Z] INIT: Template copied
[2026-02-19T14:30:05Z] Generating data.js...
[2026-02-19T14:30:06Z] ✓ config.json (1 rows)
[2026-02-19T14:30:06Z] ✓ spatial.json (42 rows)
[2026-02-19T14:30:07Z] ✓ specs.json (156 rows)
...
[2026-02-19T14:30:15Z] SUCCESS: data.js generated, 18 sections, 850 KB
[2026-02-19T14:30:16Z] ✓ API keys injected (3 keys)
[2026-02-19T14:30:16Z] ✓ Manifest updated

[2026-02-20T09:15:00Z] REFRESH: Checking for updates...
[2026-02-20T09:15:01Z] ✓ config.json: NO CHANGES
[2026-02-20T09:15:02Z] ✓ spatial.json: NO CHANGES
[2026-02-20T09:15:03Z] ✓ schedule.json: UPDATED (critical path changed)
[2026-02-20T09:15:04Z] ✓ daily-reports.json: NEW (2026-02-20 report added)
[2026-02-20T09:15:05Z] SUCCESS: data.js updated, 2 sections, +12 KB
```

---



## 14. Universal Template Rules (Design Principles)

The static HTML template is **designed to work for ANY construction project type**. The following 12 rules ensure universal applicability:

### 1. No Hardcoded Data
- No project-specific text, numbers, or IDs embedded in HTML
- All data sourced from `PROJECT_DATA` object (injected via `data.js`)
- Template agnostic to building type, location, stakeholders

### 2. Conditional Section Rendering
- Sections auto-hide if their data is empty/null
- Example: If `specs.mep.plumbing` is empty, "Plumbing" tab hidden
- Sidebar updates to reflect only populated sections
- Reduces visual clutter for smaller projects

### 3. Flexible Data Structures
- Rooms: Supports 1–500+ rooms (scaled grid, pagination)
- Doors: Supports 1–1,000+ openings (tabbed interface, search/filter)
- MEP equipment: Nested arrays (HVAC, plumbing, electrical, specialty)
- Submittals: Supports 1–1,000+ items (pipeline view, status filters)

### 4. Graceful Null Handling
- All displayed values wrapped in null checks: `item?.name || 'N/A'`
- Missing data displays "Not specified" or "—" (en-dash)
- Charts skip null data points gracefully
- Tables show empty cells without breaking layout

### 5. Building Type Agnostic
- Accommodates: Office, Healthcare, Senior Care, Industrial, Education, Hospitality, Multi-Family, Mixed-Use, Renovation, etc.
- Room types: Bedroom, Office, Lab, Classroom, Lobby, Warehouse, Kitchen, etc. (custom)
- MEP systems scale: 1 AHU (small project) to 50+ (large project)
- Financials support: Single trade to 30+ subcontractors

### 6. Scalable Room & Door Counts
- UI supports 1 to 1,000+ rooms/doors via:
  - Tabbed interface (100 items per tab)
  - Search/filter functionality
  - Pagination (25 items per page)
  - Sortable columns
- No hardcoded array length assumptions

### 7. Multi-Story Support
- `spatial.floorPlans` array: Floor 1, Floor 2, Floor 3+
- Room list includes "Floor" attribute for filtering
- Exploded floor plans can be toggled on/off in Plan Overlay Viewer
- Schedule shows floor-by-floor milestones (if tracked)

### 8. Rendering Prompts Adapt to Building Type
- Senior Care: "Patient rooms with handrails and grab bars installed"
- Office: "Open floor plan with workstations, natural light"
- Warehouse: "Clear span structure with overhead doors"
- Healthcare: "Clean rooms with HVAC terminal units visible"
**AI rendering system inspects `building_type` → adjusts prompt template**

### 9. Visual Context Optional
- If no site photos uploaded: Photo Gallery shows "No photos available" + upload prompt
- If no rendering requests: Renderings Gallery shows empty state + "Request rendering" button
- If no as-built markups: Plan Overlay Viewer operates without annotations
- Core dashboard functional without visual data

### 10. API Keys Optional
- If no Anthropic key: Chatbot shows "Offline mode" + keyword search fallback
- If no Gemini key: Gemini-specific features disabled (no impact)
- If no Flux2 key: Rendering feature shows "API key required" + setup prompt
- No hard dependency on any API

### 11. No Folder Structure Assumptions
- Template works whether files are in:
  - `AI - Project Brain/` (Foreman OS structure)
  - `project/dashboard/` (flat structure)
  - `s3://bucket/project/` (cloud storage)
  - Any relative or absolute path
- All paths in `data.js` are relative to HTML location or CDN URLs
- Image/asset URLs resolved dynamically

### 12. Safety Section Deliberately Excluded
- Dashboard does NOT include a "Safety" tab or safety-specific data sections
- Safety is a critical operational system, managed separately via `/safety` command
- Rationale: Safety policies, OSHA compliance, incident reports require stricter access controls than general project data
- If user needs safety context in dashboard, direct to `/safety` command for proper authorization flow

---



## 15. HTML Template Reference

The complete, static HTML template is located at:
```
{foreman-os-plugin-root}/references/data-intel-template.html
```

### Template Characteristics
- **Size**: ~10,000+ lines of HTML, CSS, JavaScript
- **Content**: Empty skeleton with named `<div>` containers for each of 40+ sections
- **CSS**: Embedded `<style>` tag with Foreman OS design system (colors, typography, spacing)
- **JavaScript**: Modular functions for each section's rendering logic
- **Dependencies**: Chart.js, Fabric.js, D3.js, DOMPurify (all via CDN)
- **No build step required**: Self-contained, copy-paste ready

### Template Structure (conceptual)
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{projectName} — Data Intelligence Dashboard</title>
  <style>
    /* Foreman OS design system (colors, typography, spacing) */
  </style>
</head>
<body>
  <div id="app">
    <!-- Header: Project title, role selector, search, export -->
    <header id="header"></header>

    <!-- Sidebar: Dynamic navigation -->
    <nav id="sidebar">
      <!-- Groups auto-populated from section visibility -->
    </nav>

    <!-- Main content area -->
    <main id="main-content">
      <!-- 40+ section containers -->
      <div id="section-dashboard"></div>
      <div id="section-alerts"></div>
      <div id="section-grid-lines"></div>
      <div id="section-room-browser"></div>
      <!-- ... -->
    </main>

    <!-- Chatbot widget (sidebar bottom) -->
    <div id="chatbot-panel"></div>
  </div>

  <!-- CDN libraries -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/fabric@5.3.0/dist/fabric.min.js"></script>
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.6/dist/purify.min.js"></script>

  <!-- Data injection (data.js) -->
  <script src="{projectCode}_data.js"></script>

  <!-- Rendering logic (embedded in template) -->
  <script>
    // Initialize dashboard with PROJECT_DATA
    initializeDashboard();

    // Render each section based on data availability
    renderOverviewDashboard();
    renderAlerts();
    renderGridLines();
    // ... 37 more render functions
  </script>
</body>
</html>
```

### Key Functions (Template Responsibilities)
- `initializeDashboard()`: Set up role selector, load localStorage prefs, inject API keys
- `renderSection(sectionName)`: Dynamically render a section by name
- `populateSidebar()`: Build navigation based on data completeness
- `updateCharts()`: Refresh all Chart.js instances with latest data
- `openChatbot()`: Show/hide chatbot widget, initialize message history
- `exportData(format)`: Trigger PDF/CSV/Excel/JSON export
- `searchDashboard(query)`: Full-text search across all sections

---



## 16. Deployment Checklist

### Pre-Deployment
- [ ] Verify all 17 JSON source files generated and validated
- [ ] Test MD5 hash computation (compare old vs. new)
- [ ] Confirm API keys discovered and injected (if available)
- [ ] Validate HTML template copied to project folder (first run only)
- [ ] Test role selector in header (superintendent, PM, owner, architect)
- [ ] Verify sidebar sections conditionally render/hide based on data

### Data Validation
- [ ] config.json: All required fields present (projectCode, name, address, buildingType, dates)
- [ ] spatial.json: Grid lines defined, rooms populated, floor plans listed
- [ ] specs.json: Building systems present (PEMB, CFS, MEP, finishes, doors)
- [ ] schedule.json: Critical path defined, milestones listed, no orphaned tasks
- [ ] procurement.json: POs logged, suppliers linked, material tracking started
- [ ] submittals.json: All Schiller, Wells, MMI items listed with status
- [ ] inspections.json: Hold points populated, test results linked

### Browser Compatibility
- [ ] Chrome/Edge 120+ (primary target)
- [ ] Firefox 121+
- [ ] Safari 17+
- [ ] Mobile Safari (iPad): Responsive layout tested

### Performance Baseline
- [ ] Page load: < 3 seconds (data.js embedded)
- [ ] Section render: < 500 ms per section
- [ ] Chart update: < 1 second
- [ ] Search response: < 200 ms (1,000 items)
- [ ] File size: data.js < 2 MB (acceptable for browser cache)

---



## 17. Troubleshooting & FAQ

### Q: "Dashboard not loading"
**A**: Check browser console for JavaScript errors. Verify:
1. `{PROJECT_CODE}_data.js` is valid JavaScript syntax
2. `PROJECT_DATA` object is defined and not empty
3. CDN libraries (Chart.js, D3.js) are accessible (check network tab)
4. HTML template file has `.html` extension and is in correct folder

### Q: "Submittals section shows 'No data available'"
**A**: The `submittals.json` file is empty or `DATA_MANIFEST.section_visibility.submittals` is `false`. Regenerate data.js after populating submittals in source files.

### Q: "Chatbot not responding"
**A**: Check if:
1. `ANTHROPIC_API_KEY` is valid in data.js
2. API key has sufficient quota/credit
3. Browser has internet connectivity
4. CORS errors in console? (should not occur with proper headers)

If all checks pass, chatbot falls back to keyword search (offline mode).

### Q: "Why are some sidebar sections hidden?"
**A**: Sections auto-hide if their data is empty/null. To show a section, populate its corresponding JSON source and regenerate `data.js`.

### Q: "Can I customize the dashboard layout?"
**A**: Moderately. Edit the static HTML template:
1. Move sidebar to right (change CSS `flex-direction`)
2. Reorder section containers (change HTML order)
3. Hide/show sections (add `display: none` to CSS)
4. Change colors (update CSS variables)

Do NOT regenerate the template after first deployment—only regenerate `data.js`.

### Q: "How often should I regenerate data.js?"
**A**: As data changes:
- Daily (if daily reports are logged)
- After submittals are updated (usually weekly)
- After schedule changes (usually weekly or on milestone)
- After financial updates (after pay app approval)
- Manual trigger: `/data --refresh`

---



## 18. Development Notes

### Extending the Dashboard
To add a new section:
1. Add corresponding data structure to `PROJECT_DATA` in data.js
2. Add new `<div id="section-{name}"></div>` container in HTML template
3. Add new `render{Name}()` function in template's `<script>` tag
4. Call function in `initializeDashboard()`
5. Add menu item to sidebar (in `populateSidebar()`)
6. Test conditional rendering (if no data, section hides)

### Adding a New Data Source
To ingest a new JSON source (e.g., `permits.json`):
1. Add entry to data.json file structure
2. Add corresponding `permits.json` to source files
3. Update `/data` command to parse permits file
4. Add field to `PROJECT_DATA.permits`
5. Regenerate data.js
6. Create new dashboard section (or add to "Permit Compliance" section)

### Testing
- Unit tests: Validate JSON structure against schema
- Integration: Verify data flows from source → data.js → dashboard
- Visual: Spot-check each role's sidebar order and default alerts
- Performance: Monitor load times with Chrome DevTools

---



## 19. Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-02-19 | Complete rewrite: Template + data injection architecture, 40+ sections, role-based views, AI chatbot, incremental updates |
| 2.1.0 | 2025-12-15 | Added Room Browser, Submittals Pipeline, enhanced MEP visibility |
| 2.0.0 | 2025-10-01 | Initial dashboard rollout, 25 sections, single-file HTML |
| 1.0.0 | 2025-06-01 | Prototype, static PDF reports only |

---



## 20. Support & Contact

For issues or feature requests:
- Check troubleshooting section (§17) first
- Review generation log: `AI - Project Brain/logs/data-intel-generation.log`
- Inspect browser console: Press F12 in Chrome, check "Console" tab
- Contact Foreman OS support with:
  - Project code
  - Error message or unexpected behavior
  - Browser/OS version
  - Generation log excerpt

## 4. Command Interface

### Primary Command
```
/data [section-name] [options]
```

### Execution Flow
1. User invokes `/data` (no args) → Opens dashboard with role-based overview
2. User invokes `/data room-browser` → Dashboard opens, sidebar auto-scrolls to Room Browser
3. User invokes `/data --export pdf` → Exports current view to PDF
4. User invokes `/data --search "anchor bolts"` → Searches all sections, highlights results

### Arguments (optional)
- `section-name`: Jump directly to a specific section (e.g., "submittals", "schedule", "financial")
- `--export [format]`: Export data (pdf, csv, xlsx, json)
- `--search [query]`: Full-text search across all sections
- `--role [superintendent|pm|owner|architect]`: Override default role
- `--offline`: Force keyword search (no API calls)

---



## 6. Technology Stack

### Frontend Framework
- **Single-page application** hosted in static HTML (`data-intel-template.html`)
- No external framework dependency (vanilla JavaScript)
- Modular architecture with named functions for each section

### Charting & Visualization
- **Chart.js 4.4.1** (via CDN): All bar, line, pie, waterfall charts
  - S-curve (Earned Value chart)
  - Waterfall (Change Order impact, Cost breakdown)
  - Gantt-style rendering (Schedule, Procurement timeline)
  - Progress burndown
- **Fabric.js 5.3.0** (via CDN): Plan overlay viewer with markup tools
  - Pin locations
  - Dimension callouts
  - Progress overlay
- **D3.js v7** (via CDN): Spatial correlation graph
  - Node-link diagram for room-to-door-to-MEP relationships
  - Force-directed layout

### API Integration
- **Anthropic API** (optional): Claude 3.5 Sonnet for chatbot & context-aware rendering
- **Gemini API** (optional): Secondary LLM for fallback
- **Flux 2 API** (optional): Image generation for rendering requests
- **Header**: `anthropic-dangerous-direct-browser-access` (browser-side API calls)
- **Fallback**: Keyword search engine (no API needed)

### Data Persistence
- **localStorage**: Role preference, sidebar collapse state, chat history
- **sessionStorage**: Transient UI state
- **IndexedDB**: Optional for full project cache (experimental)

### Security
- **API keys**: Stored in `data.js` (server-side during generation), injected at template load
- **CORS**: API calls use `mode: 'cors'`, requests include appropriate headers
- **XSS Prevention**: All user input sanitized via `DOMPurify` library (included in template)
- **No network persistence**: Data never leaves browser except API calls (read-only)

### Content Delivery
All assets via **public CDN** (jsDelivr, unpkg, or equivalent):
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fabric@5.3.0/dist/fabric.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.6/dist/purify.min.js"></script>
```

---



## 8. Section Specifications (40+ Sections)

### OVERVIEW Group

#### Dashboard (Role-Based Summary)
**Superintendent view**: Current phase, daily items (hold points, inspections, weather), crew count, active trades, alert count.
**PM view**: Budget status, submittals pending, change order log, key dates.
**Owner view**: Photo gallery, milestone progress, cost-to-date, percent complete waterfall.
**Data sources**: config, schedule, procurement, submittals, inspections

#### Alerts Banner
Real-time alerts: **Procurement** (orders overdue, materials not on-site), **Submittals** (>7 days in review), **Hold Points** (not completed), **Weather** (forecast outside thresholds).
**Data source**: submittals, procurement, inspections

#### Data Completeness Meter
Pie chart showing % coverage: Building Data (X%), Financials (Y%), Controls (Z%), Logs (W%). Drill-down to see which sections are populated.
**Data source**: data.js structure introspection

#### Revision Tracker
Timeline of all plan revisions, ASIs, addenda. Shows date, revision level, change summary, impact (cost, schedule). Integrated with ASI log.
**Data source**: asin.json (if available), schedule.json

### BUILDING DATA Group

#### Grid Lines
Interactive grid overlay. Display X-grids (1–8, or as defined), Y-grids (A–H, or as defined). Clickable cells show room assignments. Zoomable SVG or Canvas.
**Data source**: spatial.json (gridLines.x, gridLines.y)

#### Building Areas
By-type breakdown: Bedroom, Common, Support, Restroom, Corridor, Mechanical, Entry. Total area, gross area, net usable area. Table + pie chart.
**Data source**: spatial.json (buildingAreas)

#### Room Browser
Searchable, filterable table of all rooms. Click a room → detailed fact sheet:
- Room ID, Name, Area (SF), Type, Occupancy, Floor, Grid reference
- Finishes: Flooring, Wall, Ceiling, Paint, Acoustical (with color/material links)
- Doors: List all doors in room, hardware schedule, hand/swing
- MEP Equipment: HVAC terminal, plumbing fixtures, electrical outlets/switches, fire alarm
- Casework: Built-ins, cabinetry, special equipment
- Furniture: If furnished (owner responsibility or scope TBD)
- Cross-references: Link to doors section, MEP section, specifier contact
**Data source**: spatial.json (rooms), specs.json (finishes, doors, MEP, casework)

#### Doors & Hardware (3 Sub-Tabs)
**Tab 1 — Door Schedule**: All 52 doors (or as-defined). Columns: Opening #, Type (HM, Wood, Glass), Material, Width × Height, Fire Rating (if any), Hardware Spec, Supplier (Schiller), Delivery Status, Installation Status.
**Tab 2 — Hardware Groups**: Each hardware spec (e.g., "HM-01", "Wood-02"). Components: Hinges, Closer, Handle, Lockset, Kickplate, Astragal. Supplier, lead time, price per set.
**Tab 3 — Supplier Tracking**: Schiller status (contract date, PO, delivery window, submittals pending). Delivery update section for each door type.
**Data source**: specs.json (doors), procurement.json (Schiller PO)

#### PEMB/Structure
Supplier: Nucor. Model: S25R0990A. Dimensions: 75' × 132'-8" × 16' eave. Slope: 1:12. Frames: 6 clear-span rigid, 26'-8" spacing. Max reactions: 23.5 kips vert, 17.9 kips horiz. Anchor bolts: 1-1/4" primary (interior), 3/4" secondary (endwalls), F1554 Gr36. Design loads: 115 mph wind, 15 PSF snow, SDC B. Status: On-site scheduled 3/5/26. Anchor bolt template approval pending.
**Data source**: specs.json (pemb), procurement.json (Nucor contract)

#### MEP Systems (3 Sub-Tabs)
**Tab 1 — HVAC**: Equipment list (ERV-1, AHU-1/2/3, AC-1/2/3, EF-1/2). By room/zone: terminal type, capacity, controls (thermostat/CO2 sensor/occupancy). Ductwork: Galvanized, R-6 insulation. Routing plan reference.
**Tab 2 — Plumbing**: Hot water: Lochinvar 50 gal. Fixtures: 35+ itemized. Supply: Type L copper. DWV: PVC Schedule 40. Routing: Plan reference.
**Tab 3 — Electrical**: Panels A/B/C (208/120V 3-phase). Branch circuits: 120+ LED fixtures, fire alarm, nurse call, access control. Panel schedule (loads, breaker sizes). Riser diagram.
**Data source**: specs.json (mep.hvac, .plumbing, .electrical)

#### Site & Civil
Site plan coordinates, utilities routing, stormwater design (detention pond, swales, outfall), pavement (parking, drive aisles, thickness, finish), geotech summary (bearing 2000 PSF, settlement <1", <0.5" differential), soil conditions, fill removal (3.5'), compaction testing schedule (98% Std Proctor, 8" lifts).
**Data source**: spatial.json (site), specs.json (civil), inspections.json (geotech tests)

### QUANTITIES & COST Group

#### Material Takeoff
Room-by-room material quantities extracted from specs:
- Drywall: LF of walls × height → SF of GWB by type
- Insulation: By cavity, type (mineral wool, spray, etc.)
- Flooring: SF by type (VCT, carpet, concrete)
- Paint: SF of walls, ceiling by color/sheen
- Hardware: Count by room × door count = total sets
- Fixtures: Count by type (lavatories, WCs, sinks, etc.)
**Data source**: specs.json (finishes, doors, MEP), spatial.json (rooms)

#### Materials Dashboard
Inventory tracker: Current on-hand, ordered, received, consumed-to-date, remaining. Consumption rate chart (daily, weekly). Alert if low stock.
**Data source**: procurement.json (material_tracking)

#### Bidding Analysis
Vendor quotes for major items (PEMB, Doors, Concrete, MEP). Columns: Item, Vendor A (price, lead time), Vendor B, Vendor C. Variance analysis. Selections highlighted.
**Data source**: procurement.json (vendor_quotes), schedule.json (lead times)

#### Material Calculator
User-driven estimator: Input room count, door count, fixture count → generates takeoff. Linear feet, square feet, count estimator tools.
**Data source**: specs.json (room types, fixture schedules)

### FINANCIALS Group

#### Financials Summary
**Key metrics**: Total contract value, total completed to date, percent complete (%), earned value, spent, retainage, balance to invoice. Trend lines month-to-date.
**Data source**: procurement.json (po_log), pay-apps.json

#### Subcontracts & POs
Table of all contracts: Contractor/Supplier, Trade, Contract value, PO number, order date, delivery (if applicable), invoiced to date, retainage, balance. Status: Executed, Pending, Closed.
**Data source**: procurement.json (po_log), directory.json (subs)

#### Change Orders
Log of all change orders: CO #, description, cost impact (+/−), schedule impact (days), requested by, approval chain, approval date, status (pending, approved, rejected). Cumulative cost impact chart.
**Data source**: change-orders.json

#### Pay Applications
Payment history: Period, contractor, invoice amount, cost completed (earned value), retainage withheld, approved amount, approval date. Cumulative invoiced chart. Waterfall showing budget vs. actual.
**Data source**: pay-apps.json

### SPECIFICATIONS Group

#### Spec Sections
Organized by CSI Division: 01 (General), 03 (Concrete), 04 (Masonry), 05 (Metals), 06 (Wood), 07 (Thermal/Moisture), 08 (Openings), 09 (Finishes), 10–14 (Specialties), 15–16 (MEP), 17 (Conveying), 18–21 (Facilities). Click each division → summary + key spec products.
**Data source**: specs.json (all)

#### Concrete Mix Designs
All 5 mixes (interior 4000 PSI, exterior 4500 PSI, etc.). For each: Supplier (Wells Concrete), ingredients (cement, sand, aggregates, water reducer, air entrainer), yield, slump range, air content, temperature range, curing instructions, testing schedule (1 set per 50 CY), workability notes.
**Data source**: specs.json (concrete.mixes), submittals.json (Wells Concrete mix design submittal)

#### Field Tolerances
By system: **Structure** (±1/2" in 10', ±1/4" in 40'), **CFS Framing** (±1/4" in 10'), **MEP** (±1/2" ductwork, ±3/8" piping, ±1/8" electrical), **Finishes** (±1/8" on flatness, ±1/16" on door frame reveal). Reference standard (ACI, AISC, ASHRAE, etc.).
**Data source**: specs.json (field_tolerances) or master specs document

#### Weather Thresholds
By phase and operation:
- **Concrete placement**: Min 40F rising, max 90F, no rain during pour, protect 24–48 hr post-pour
- **Earthwork**: No frozen ground, no saturated soils, 24–48 hr post-rain delay
- **PEMB erection**: Wind < 25 mph, no lightning, no active precipitation
- **Roof panels**: Wind < 30 mph, no precip, min 40F for sealant cure
- **CFS/GWB**: Min 50F, max 85F, 24–48 hr post-rain delay
**Data source**: specs.json (weather_thresholds)

#### Hold Points
List of all hold points (HP-001 through HP-007+):
- **HP-001**: Proof-roll subgrade (Terracon) — before fill
- **HP-002**: Footing rebar inspection (Building Official) — before pour
- **HP-003**: Anchor bolt template verification (Super + Nucor) — before PEMB foundation pour
- **HP-004**: Stem wall inspection (Building Official) — before pour
- **HP-005**: SOG pre-pour inspection (Building Official) — vapor barrier + reinforcing
- **HP-006**: Compaction testing (Terracon) — every lift, 98% Std Proctor
- **HP-007**: Anchor bolt survey (Surveyor) — 1 week before steel arrives
Plus SWPPP weekly + after 0.5" rainfall events
**Data source**: inspections.json (hold_points)

### PROJECT CONTROLS Group

#### Schedule & Critical Path
Gantt chart (Chart.js or D3 custom) showing all tasks from baseline schedule. Critical path highlighted in red. Float slacks visible. Filter by trade, phase, or custom. Milestone markers. Current date line. Update progress with weekly input.
**Data source**: schedule.json (baseline, milestones, critical_path)

#### Procurement Gantt
Timeline of all procurement items: Concrete (order, deliver), PEMB (order 12/18, deliver 3/5), Doors (order 1/20, deliver TBD), MEP equipment (order, 8-week lead), etc. Shows order window, supplier lead time, expected delivery.
**Data source**: procurement.json (vendor_quotes, po_log), schedule.json (procurement_gantt)

#### Submittals Pipeline
Status summary pie: % Pending, % In Review, % Approved, % Rejected, % Deferred. Detailed table: Item, Supplier, Days in Review, Status, Approver, Notes. Alert if > 7 days in review. Sort by age, trade, or status.
**Data source**: submittals.json

#### RFIs
Log of all RFIs: ID, date submitted, question, submitted by, assigned to, days open, response received, days to resolve. Trend chart: RFIs opened vs. closed per week. By category (design, constructability, materials, coordination, other).
**Data source**: rfis.json

#### Permit Compliance
List of all permits on file (HBC #2511-005566, MUPB #26, others). For each: Permit #, type, scope, approval date, expiration (if any), correction list (if any), inspection status. Link to inspection log.
**Data source**: inspections.json (third_party)

### DOCUMENTS Group

#### Sheet Index
All drawings in plan set: Drawing #, Title, Revision level, dated, uploaded to system on [date]. Filter by discipline (Arch, Struct, MEP, Civil). Clickable to view (if PDF embedded) or download.
**Data source**: visual-context.json (sheet_index) or document manifest

#### Plan Overlay Viewer
Fabric.js-based tool: Load a floor plan image, overlay grid lines (X/Y), room IDs, door IDs, equipment pins (HVAC, plumbing, electrical). Markup tools: add dimensions, callouts, notes. Save markup. Progress overlay: show % complete per zone.
**Data source**: spatial.json (gridLines, rooms), specs.json (doors, MEP), visual-context.json (site_photos, as_built_markup)

#### ASI / Revision Log
Chronological list of all ASIs/Addenda/Revisions. For each: ASI #, date issued, summary (floor plan revision, spec clarification, etc.), impact (cost +/−, schedule +/− days). Mark as reviewed/incorporated.
**Data source**: ASI JSON (if separate), or notes in schedule.json

### SPATIAL Group

#### Spatial Correlation Graph
D3.js force-directed graph: Nodes for Rooms, Doors, MEP Equipment, Finishes. Edges show relationships:
- Room ↔ Door (doors in room)
- Room ↔ HVAC terminal (supply/return)
- Room ↔ Plumbing fixture (location)
- Room ↔ Electrical outlet (count)
- Room ↔ Casework (items in room)
Hover node → show details. Drag to reposition. Zoom/pan.
**Data source**: spatial.json (rooms), specs.json (doors, MEP, casework)

#### Progress Tracking
By-phase completion chart: Foundation (%), PEMB (%), Rough-in (%), Finishes (%). By-trade: Concrete, Steel, EKD (CFS/GWB), MEP, etc. By-location: By floor, by zone. Trend line (S-curve or actual vs. baseline).
**Data source**: schedule.json (milestones, actual dates), daily-reports.json (work summary)

### TOOLS Group

#### Renderings Gallery
AI-generated images (if available). For each rendering: Prompt used, model (Flux 2), date generated, image preview. Option to regenerate or tweak prompt. Filter by phase (site prep, foundation, PEMB, dry-in, rough-in, finishes).
**Data source**: rendering-log.json

#### AI Chatbot (Sidebar Widget)
**System prompt**: Built from PROJECT_DATA summary: "You are the AI assistant for Morehead One Senior Care (MOSC), a 9,980 SF senior care facility in Morehead, KY. You have access to detailed project data: building specs, schedule, submittals, change orders, hold points, daily reports, etc. Answer questions accurately using data context."

**Features**:
- Chat input + message history (scrollable)
- Suggested questions: "What is the critical path?", "Show me overdue submittals", "What's the permit status?"
- Copy-to-clipboard button for each response
- Search fallback (keyword matching) if API unavailable
- Message export to text

**Data source**: All PROJECT_DATA via context injection

#### Export/Print
Buttons for each format: PDF (current section or full dashboard), CSV (tables), Excel (with charts), JSON (raw data). Browser's print dialog for paper output.
**Data source**: All visible sections, rendered to respective formats

### LOGS Group

#### Daily Report Log
Table of all daily reports (7+ existing, growing). Columns: Date, Superintendent, Crew count, Weather (temp, wind, precip), Work summary, Issues, Safety events. Click to expand summary. Search by date, superintendent, or keyword.
**Data source**: daily-reports.json (reference/summary only; full reports stored separately)

#### Delays Log
All delay events: ID, Event/cause, Trade affected, Duration (days), Impact on critical path (Y/N), Mitigation action, Status (open/closed). Filter by cause category.
**Data source**: delays.json

#### Punch List
Sortable by: Location, Item, Trade, Priority, Status. Columns: ID, Location (room + grid ref), Description, Trade responsible, Priority (critical/high/medium/low), Assigned to, Due date, Status. Progress bar (% closed). Bulk status update.
**Data source**: punch-list.json

#### Meeting Notes
Date, Meeting type (coordination, safety, owner, subcontractor), Attendees, Agenda, Decisions made, Action items (owner + due date). Search by date or attendee. Mark action items as completed.
**Data source**: meetings.json

#### Geotechnical
Summary of all geotech tests: Bearing 2,000 PSF, expected settlement <1" total, <0.5" differential. Compaction testing log: Location, date, % Std Proctor, pass/fail. Fill removal tracking (3.5' existing fill, replace status). Dewatering log (if applicable).
**Data source**: inspections.json (test_results), geotech report (Terracon N3255095)

#### SWPPP
Stormwater Pollution Prevention Plan compliance: Weekly inspection checklist, rainfall event log (>0.5"), corrective actions taken, date completed. Filtration device status, sediment trap, inlet protection. Compliance trending chart.
**Data source**: inspections.json (third_party SWPPP inspections), daily-reports.json (notes)

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


