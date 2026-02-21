# Lookahead Template Reference

This reference guide covers the HTML structure, styling, layout, and responsive design patterns for the Look-Ahead Planner skill's output documents.

---

## 1. Overall HTML Structure

The lookahead document is a self-contained, single-file HTML5 document with embedded CSS and JavaScript. No external file dependencies except for Chart.js via CDN.

### Document Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Construction Lookahead Schedule">
    <title>Lookahead Schedule - {PROJECT_CODE} - {DATE}</title>
    
    <!-- Chart.js for visualizations -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    
    <!-- Embedded CSS -->
    <style>
        /* See section 2: CSS Styles */
    </style>
</head>
<body>
    <!-- Content sections (see sections 3-8 below) -->
    
    <!-- Embedded JavaScript -->
    <script>
        // See section 9: JavaScript Functions
    </script>
</body>
</html>
```

---

## 2. CSS Styling & Color Palette

### Core Color Palette

The lookahead uses the daily-report identity colors:

```css
:root {
    /* Primary Colors */
    --navy: #1B2A4A;           /* Dark backgrounds, header, critical elements */
    --blue-accent: #2E5EAA;    /* Links, hover states, near-critical */
    --light-blue: #EDF2F9;     /* Background tints, alternating rows */
    
    /* Status Colors */
    --critical-red: #DC3545;   /* Critical path, blockers, urgent alerts */
    --at-risk-amber: #FFC107;  /* Near-critical, at-risk items */
    --on-track-green: #28A745; /* On-schedule activities */
    --blocked-gray: #6C757D;   /* Weather-blocked, suspended activities */
    
    /* Neutral Colors */
    --white: #FFFFFF;
    --light-gray: #F8F9FA;
    --medium-gray: #D3D3D3;
    --dark-gray: #333333;
    
    /* Semantic Colors */
    --success: #28A745;
    --warning: #FFC107;
    --danger: #DC3545;
    --info: #17A2B8;
}
```

### Full CSS Stylesheet

```css
/* ============ GLOBAL STYLES ============ */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    font-size: 14px;
    line-height: 1.6;
    color: var(--dark-gray);
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background-color: var(--light-gray);
    padding: 20px;
}

/* ============ HEADER ============ */

.header {
    background: linear-gradient(135deg, var(--navy) 0%, var(--blue-accent) 100%);
    color: white;
    padding: 30px;
    border-radius: 8px;
    margin-bottom: 30px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header h1 {
    font-size: 32px;
    margin-bottom: 8px;
    font-weight: 700;
}

.header .project-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    font-size: 13px;
    opacity: 0.95;
    margin-top: 12px;
}

.header .meta-item {
    display: flex;
    flex-direction: column;
}

.header .meta-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    opacity: 0.8;
    margin-bottom: 2px;
}

.header .meta-value {
    font-size: 14px;
    font-weight: 600;
}

/* ============ ALERTS & BLOCKERS ============ */

.alerts-container {
    margin-bottom: 30px;
}

.alert {
    padding: 16px;
    border-radius: 6px;
    margin-bottom: 12px;
    display: flex;
    gap: 12px;
    border-left: 4px solid;
}

.alert.blocker {
    background-color: #FADBD8;
    border-left-color: var(--critical-red);
    color: #78281F;
}

.alert.warning {
    background-color: #FEF5E7;
    border-left-color: var(--at-risk-amber);
    color: #7D6608;
}

.alert.info {
    background-color: #D6EAF8;
    border-left-color: var(--blue-accent);
    color: #1B4965;
}

.alert-icon {
    font-size: 20px;
    flex-shrink: 0;
}

.alert-content {
    flex: 1;
}

.alert-title {
    font-weight: 600;
    margin-bottom: 4px;
}

.alert-message {
    font-size: 13px;
    line-height: 1.5;
}

/* ============ WEATHER FORECAST STRIP ============ */

.weather-strip {
    background-color: var(--light-blue);
    border: 1px solid #C8D8E8;
    border-radius: 6px;
    padding: 16px;
    margin-bottom: 20px;
}

.weather-strip h3 {
    color: var(--navy);
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 12px;
}

.weather-forecast {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
    gap: 12px;
}

.weather-day {
    background-color: white;
    border: 1px solid #D3D3D3;
    border-radius: 4px;
    padding: 8px;
    text-align: center;
    font-size: 12px;
}

.weather-day-name {
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 4px;
}

.weather-icon {
    font-size: 24px;
    margin: 4px 0;
}

.weather-temp {
    color: var(--blue-accent);
    font-weight: 600;
    font-size: 13px;
}

.weather-precip {
    color: #666;
    font-size: 11px;
    margin-top: 4px;
}

/* ============ WEEK HEADER ============ */

.week-section {
    margin-bottom: 40px;
}

.week-header {
    background-color: var(--navy);
    color: white;
    padding: 12px 16px;
    border-radius: 6px 6px 0 0;
    font-size: 16px;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.week-header-info {
    display: flex;
    gap: 20px;
}

.week-range {
    font-size: 14px;
}

.week-stats {
    font-size: 12px;
    opacity: 0.9;
    display: flex;
    gap: 12px;
}

.week-stat {
    display: flex;
    align-items: center;
    gap: 4px;
}

.stat-icon {
    width: 12px;
    height: 12px;
    border-radius: 2px;
}

/* ============ DAILY ROWS TABLE ============ */

.days-table {
    width: 100%;
    border-collapse: collapse;
    background-color: white;
    border-radius: 0 0 6px 6px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    margin-bottom: 20px;
}

.days-table thead {
    background-color: #F5F5F5;
    border-bottom: 2px solid #D3D3D3;
}

.days-table th {
    padding: 12px 12px;
    text-align: left;
    font-weight: 600;
    font-size: 12px;
    color: var(--navy);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.days-table tbody tr {
    border-bottom: 1px solid #E8E8E8;
}

.days-table tbody tr:hover {
    background-color: var(--light-blue);
}

.days-table td {
    padding: 12px;
    font-size: 13px;
    vertical-align: top;
}

/* ============ ACTIVITY CELLS ============ */

.activity-item {
    background-color: white;
    border-left: 4px solid;
    padding: 8px 10px;
    margin-bottom: 6px;
    border-radius: 3px;
    font-size: 13px;
    line-height: 1.4;
}

.activity-item.critical {
    border-left-color: var(--critical-red);
    background-color: #FEF5F5;
}

.activity-item.near-critical {
    border-left-color: var(--at-risk-amber);
    background-color: #FFFBF0;
}

.activity-item.on-track {
    border-left-color: var(--on-track-green);
    background-color: #F5FFF7;
}

.activity-item.blocked {
    border-left-color: var(--blocked-gray);
    background-color: #F9F9F9;
    opacity: 0.7;
    text-decoration: line-through;
}

.activity-name {
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 3px;
}

.activity-meta {
    font-size: 12px;
    color: #666;
}

.activity-progress {
    font-size: 11px;
    color: var(--blue-accent);
    margin-top: 3px;
}

/* ============ MILESTONE MARKERS ============ */

.milestone-marker {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 8px;
    background-color: white;
    border: 2px solid;
    border-radius: 3px;
    font-size: 12px;
    font-weight: 600;
    margin: 4px 0;
}

.milestone-marker.major {
    border-color: var(--critical-red);
    color: var(--critical-red);
}

.milestone-marker.minor {
    border-color: var(--blue-accent);
    color: var(--blue-accent);
}

.milestone-marker::before {
    content: "🚩";
    font-size: 14px;
}

/* ============ MATERIAL DELIVERY HIGHLIGHTS ============ */

.material-delivery {
    background-color: #E8F4F8;
    border: 2px solid var(--blue-accent);
    padding: 8px 10px;
    border-radius: 3px;
    font-size: 12px;
    margin-bottom: 6px;
}

.material-delivery.pending {
    background-color: #FEF5E7;
    border-color: var(--at-risk-amber);
    font-weight: 500;
}

.material-delivery.confirmed {
    background-color: #F5FFF7;
    border-color: var(--on-track-green);
}

.material-name {
    font-weight: 600;
    color: var(--navy);
}

.material-supplier {
    font-size: 11px;
    color: #666;
    margin-top: 2px;
}

/* ============ SUBCONTRACTOR & CREW ============ */

.sub-info {
    font-size: 12px;
    line-height: 1.5;
}

.sub-name {
    font-weight: 600;
    color: var(--navy);
}

.crew-badge {
    display: inline-block;
    background-color: var(--light-blue);
    color: var(--navy);
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 11px;
    font-weight: 600;
    margin-left: 4px;
}

/* ============ NOTES & WARNINGS ============ */

.notes-cell {
    font-size: 12px;
    color: #666;
}

.warning-text {
    color: var(--critical-red);
    font-weight: 600;
    margin: 4px 0;
}

/* ============ LEGEND ============ */

.legend {
    background-color: var(--light-blue);
    border: 1px solid #C8D8E8;
    border-radius: 6px;
    padding: 16px;
    margin-top: 40px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 13px;
}

.legend-color {
    width: 20px;
    height: 20px;
    border-radius: 3px;
    border: 2px solid #999;
}

.legend-color.critical {
    background-color: var(--critical-red);
}

.legend-color.near-critical {
    background-color: var(--at-risk-amber);
}

.legend-color.on-track {
    background-color: var(--on-track-green);
}

.legend-color.blocked {
    background-color: var(--blocked-gray);
}

/* ============ FOOTER ============ */

.footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #D3D3D3;
    text-align: center;
    font-size: 12px;
    color: #999;
}

.footer-info {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 12px;
    flex-wrap: wrap;
}

/* ============ RESPONSIVE DESIGN ============ */

@media (max-width: 1024px) {
    body {
        padding: 16px;
    }
    
    .header {
        padding: 20px;
    }
    
    .header h1 {
        font-size: 24px;
    }
    
    .header .project-meta {
        gap: 16px;
    }
    
    .weather-forecast {
        grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
    }
    
    .days-table td {
        padding: 10px;
        font-size: 12px;
    }
    
    .legend {
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    }
}

@media (max-width: 768px) {
    body {
        padding: 12px;
        font-size: 12px;
    }
    
    .header {
        padding: 16px;
    }
    
    .header h1 {
        font-size: 20px;
    }
    
    .header .project-meta {
        gap: 12px;
        flex-direction: column;
    }
    
    .header .meta-item {
        flex-direction: row;
        gap: 8px;
    }
    
    .weather-forecast {
        grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
    }
    
    .weather-day {
        padding: 6px;
        font-size: 11px;
    }
    
    .days-table {
        font-size: 11px;
    }
    
    .days-table th,
    .days-table td {
        padding: 8px;
    }
    
    .activity-item {
        padding: 6px 8px;
        margin-bottom: 4px;
        font-size: 12px;
    }
    
    .activity-name {
        margin-bottom: 2px;
    }
    
    .activity-meta {
        font-size: 11px;
    }
    
    .week-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }
    
    .week-stats {
        width: 100%;
        flex-wrap: wrap;
    }
    
    .legend {
        grid-template-columns: 1fr;
    }
    
    /* Stack table columns on very small screens */
    .days-table thead {
        display: none;
    }
    
    .days-table tbody tr {
        display: block;
        margin-bottom: 16px;
        border: 1px solid #D3D3D3;
        border-radius: 4px;
    }
    
    .days-table td {
        display: block;
        text-align: right;
        padding-left: 50%;
        position: relative;
    }
    
    .days-table td::before {
        content: attr(data-label);
        position: absolute;
        left: 10px;
        font-weight: 600;
        color: var(--navy);
    }
}

/* ============ PRINT STYLES ============ */

@media print {
    body {
        background-color: white;
        padding: 0;
    }
    
    .header {
        page-break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ddd;
    }
    
    .week-section {
        page-break-inside: avoid;
    }
    
    .days-table {
        page-break-inside: avoid;
    }
    
    .activity-item.blocked {
        opacity: 1;
        text-decoration: none;
        color: #999;
    }
}
```

---

## 3. Header Section

The header contains the project title, metadata, and document info.

```html
<header class="header">
    <h1>Lookahead Schedule</h1>
    <div class="project-meta">
        <div class="meta-item">
            <span class="meta-label">Project</span>
            <span class="meta-value">GC001 - Main Building Construction</span>
        </div>
        <div class="meta-item">
            <span class="meta-label">Period</span>
            <span class="meta-value">Feb 16 – Mar 8, 2025 (3 weeks)</span>
        </div>
        <div class="meta-item">
            <span class="meta-label">Generated</span>
            <span class="meta-value">Feb 16, 2025 at 09:30 AM</span>
        </div>
        <div class="meta-item">
            <span class="meta-label">Forecast</span>
            <span class="meta-value">3-Week Weather Forecast Included</span>
        </div>
    </div>
</header>
```

---

## 4. Alerts & Blockers Section

Critical blockers and warnings are displayed prominently at the top.

```html
<section class="alerts-container" id="alerts">
    <!-- Example Blocker Alert -->
    <div class="alert blocker">
        <div class="alert-icon">🚨</div>
        <div class="alert-content">
            <div class="alert-title">BLOCKER: RFI-025 Response Due</div>
            <div class="alert-message">
                RFI-025 response is due Feb 24. This RFI blocks the Concrete Pour activity 
                scheduled to start Feb 22. Coordinate with engineer immediately.
            </div>
        </div>
    </div>
    
    <!-- Example Warning Alert -->
    <div class="alert warning">
        <div class="alert-icon">⚠️</div>
        <div class="alert-content">
            <div class="alert-title">At-Risk Material Delivery</div>
            <div class="alert-message">
                Ready-mix concrete delivery promised for Feb 22, but only 2 days before 
                Concrete Pour activity starts. Monitor supplier closely.
            </div>
        </div>
    </div>
    
    <!-- Example Info Alert -->
    <div class="alert info">
        <div class="alert-icon">ℹ️</div>
        <div class="alert-content">
            <div class="alert-title">Weather Watch</div>
            <div class="alert-message">
                Excavation is weather-sensitive. Forecast shows 40% rain probability Feb 20–21. 
                Activities may shift.
            </div>
        </div>
    </div>
</section>
```

---

## 5. Weather Forecast Strip

The weather strip shows the 3-week forecast at the top of each week.

```html
<div class="weather-strip">
    <h3>☀️ 3-Week Weather Forecast (Springfield, IL)</h3>
    <div class="weather-forecast">
        <div class="weather-day">
            <div class="weather-day-name">Sun, Feb 16</div>
            <div class="weather-icon">🌤️</div>
            <div class="weather-temp">42–58°F</div>
            <div class="weather-precip">10% rain</div>
        </div>
        <div class="weather-day">
            <div class="weather-day-name">Mon, Feb 17</div>
            <div class="weather-icon">☁️</div>
            <div class="weather-temp">40–55°F</div>
            <div class="weather-precip">20% rain</div>
        </div>
        <!-- More days ... -->
    </div>
</div>
```

---

## 6. Week Section & Daily Table

Each week is a self-contained section with a week header and daily breakdown table.

### Week Header

```html
<section class="week-section">
    <div class="week-header">
        <div class="week-header-info">
            <div class="week-range">
                Week 1: Feb 16–22, 2025
            </div>
            <div class="week-stats">
                <div class="week-stat">
                    <span class="stat-icon" style="background-color: var(--critical-red);"></span>
                    <span>3 Critical</span>
                </div>
                <div class="week-stat">
                    <span class="stat-icon" style="background-color: var(--at-risk-amber);"></span>
                    <span>2 At-Risk</span>
                </div>
                <div class="week-stat">
                    <span class="stat-icon" style="background-color: var(--on-track-green);"></span>
                    <span>5 On-Track</span>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Daily Table -->
    <table class="days-table">
        <thead>
            <tr>
                <th>Date</th>
                <th>Day</th>
                <th>Activities</th>
                <th>Subcontractor</th>
                <th>Headcount</th>
                <th>Materials / Deliveries</th>
                <th>Notes</th>
            </tr>
        </thead>
        <tbody>
            <!-- Daily rows (see section 7 below) -->
        </tbody>
    </table>
</section>
```

---

## 7. Daily Table Rows

Each row represents one calendar day with all scheduled work.

### Standard Daily Row

```html
<tr>
    <td>Feb 17</td>
    <td>Monday</td>
    <td>
        <div class="activity-item critical">
            <div class="activity-name">Excavation & Grade Beam</div>
            <div class="activity-meta">
                Day 2 of 14 (12 days remaining)
            </div>
        </div>
        <div class="activity-item on-track">
            <div class="activity-name">Temporary Power Installation</div>
            <div class="activity-meta">
                Day 1 of 3
            </div>
        </div>
    </td>
    <td>
        <div class="sub-info">
            <div class="sub-name">ABC Excavation</div>
            <span class="crew-badge">6 crew</span>
        </div>
        <div class="sub-info" style="margin-top: 8px;">
            <div class="sub-name">Site Power Co.</div>
            <span class="crew-badge">3 crew</span>
        </div>
    </td>
    <td>
        <span class="crew-badge">9 total</span>
    </td>
    <td>
        <div class="material-delivery pending">
            <div class="material-name">🚚 Temporary Generator</div>
            <div class="material-supplier">Pending from United Rentals</div>
        </div>
    </td>
    <td>
        <div class="notes-cell">
            Weather: 42–55°F, 20% rain. Excavation proceeding as scheduled.
        </div>
    </td>
</tr>
```

### Milestone Day Row

```html
<tr>
    <td>Feb 21</td>
    <td>Friday</td>
    <td>
        <div class="milestone-marker major">
            Excavation Complete
        </div>
        <div class="activity-item critical">
            <div class="activity-name">Formwork Setup for Grade Beam</div>
            <div class="activity-meta">Day 1 of 5</div>
        </div>
    </td>
    <td>
        <div class="sub-info">
            <div class="sub-name">XYZ Concrete</div>
            <span class="crew-badge">4 crew</span>
        </div>
    </td>
    <td>
        <span class="crew-badge">4 total</span>
    </td>
    <td>
        <!-- No material deliveries this day -->
    </td>
    <td>
        <div class="notes-cell">
            🎯 <strong>Milestone achieved:</strong> Excavation complete on schedule.
        </div>
    </td>
</tr>
```

### Weather-Blocked Day Row

```html
<tr>
    <td>Feb 20</td>
    <td>Thursday</td>
    <td>
        <div class="activity-item blocked">
            <div class="activity-name">Concrete Pour (WEATHER-BLOCKED)</div>
            <div class="activity-meta">Rescheduled due to rain forecast</div>
        </div>
    </td>
    <td>
        <div class="sub-info">
            <div class="sub-name">XYZ Concrete</div>
        </div>
    </td>
    <td>
        <!-- N/A when blocked -->
    </td>
    <td>
        <!-- N/A when blocked -->
    </td>
    <td>
        <div class="notes-cell">
            <div class="warning-text">⚠️ Concrete pour rescheduled. Forecast: Heavy rain (1.2 inches), 40–45°F. 
            Activity moved to Feb 23 (pending supplier confirmation).</div>
        </div>
    </td>
</tr>
```

---

## 8. Legend & Footer

### Legend Section

```html
<section class="legend">
    <div class="legend-item">
        <div class="legend-color critical"></div>
        <span><strong>Critical Path:</strong> Zero float, delays impact project end date</span>
    </div>
    <div class="legend-item">
        <div class="legend-color near-critical"></div>
        <span><strong>Near-Critical:</strong> 1–5 days float, monitor closely</span>
    </div>
    <div class="legend-item">
        <div class="legend-color on-track"></div>
        <span><strong>On-Track:</strong> 6+ days float, schedule slack available</span>
    </div>
    <div class="legend-item">
        <div class="legend-color blocked"></div>
        <span><strong>Blocked:</strong> Weather, material delay, or RFI blocking work</span>
    </div>
</section>
```

### Footer Section

```html
<footer class="footer">
    <div class="footer-info">
        <span>Generated: Feb 16, 2025 at 09:30 AM</span>
        <span>|</span>
        <span>Project: GC001</span>
        <span>|</span>
        <span>3-Week Lookahead Schedule</span>
    </div>
    <div style="font-size: 11px; color: #ccc;">
        This document is self-contained and can be saved, printed, or emailed. 
        Data is current as of generation date.
    </div>
</footer>
```

---

## 9. JavaScript Functions

### Dynamic Interactivity

The lookahead includes JavaScript for interactive features:

```javascript
// ============ INITIALIZATION ============

document.addEventListener('DOMContentLoaded', function() {
    initializeTooltips();
    initializeExpandCollapse();
    initializeSearch();
    initializePrint();
});

// ============ TOOLTIPS ============

function initializeTooltips() {
    // Add hover tooltips to activity items, material deliveries, etc.
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(event) {
    const tooltip = event.target.getAttribute('data-tooltip');
    const tooltipEl = document.createElement('div');
    tooltipEl.className = 'tooltip';
    tooltipEl.textContent = tooltip;
    tooltipEl.style.position = 'absolute';
    tooltipEl.style.background = 'rgba(0, 0, 0, 0.8)';
    tooltipEl.style.color = 'white';
    tooltipEl.style.padding = '6px 10px';
    tooltipEl.style.borderRadius = '3px';
    tooltipEl.style.fontSize = '12px';
    tooltipEl.style.zIndex = '1000';
    
    document.body.appendChild(tooltipEl);
    
    const rect = event.target.getBoundingClientRect();
    tooltipEl.style.top = (rect.top - tooltipEl.offsetHeight - 10) + 'px';
    tooltipEl.style.left = rect.left + 'px';
    
    event.target._tooltip = tooltipEl;
}

function hideTooltip(event) {
    if (event.target._tooltip) {
        event.target._tooltip.remove();
        delete event.target._tooltip;
    }
}

// ============ EXPAND/COLLAPSE ============

function initializeExpandCollapse() {
    const collapsibleHeaders = document.querySelectorAll('.week-header');
    
    collapsibleHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const section = this.closest('.week-section');
            const table = section.querySelector('.days-table');
            table.style.display = table.style.display === 'none' ? 'table' : 'none';
            this.classList.toggle('collapsed');
        });
    });
}

// ============ SEARCH / FILTER ============

function initializeSearch() {
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = 'Search activities, subs, materials...';
    searchInput.style.width = '100%';
    searchInput.style.padding = '10px';
    searchInput.style.marginBottom = '20px';
    searchInput.style.border = '1px solid #D3D3D3';
    searchInput.style.borderRadius = '4px';
    searchInput.style.fontSize = '14px';
    
    const alertsContainer = document.querySelector('.alerts-container');
    alertsContainer.parentElement.insertBefore(searchInput, alertsContainer);
    
    searchInput.addEventListener('input', function() {
        filterLookahead(this.value.toLowerCase());
    });
}

function filterLookahead(searchTerm) {
    const activityItems = document.querySelectorAll('.activity-item');
    const rows = document.querySelectorAll('.days-table tbody tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchTerm) ? '' : 'none';
    });
}

// ============ PRINT FUNCTIONALITY ============

function initializePrint() {
    const printButton = document.createElement('button');
    printButton.textContent = 'Print / Save as PDF';
    printButton.style.padding = '10px 16px';
    printButton.style.background = 'var(--blue-accent)';
    printButton.style.color = 'white';
    printButton.style.border = 'none';
    printButton.style.borderRadius = '4px';
    printButton.style.cursor = 'pointer';
    printButton.style.fontSize = '14px';
    printButton.style.fontWeight = '600';
    printButton.style.marginBottom = '20px';
    
    const header = document.querySelector('.header');
    header.parentElement.insertBefore(printButton, header.nextSibling);
    
    printButton.addEventListener('click', function() {
        window.print();
    });
}

// ============ STATISTICS CALCULATION ============

function calculateWeekStatistics(weekElement) {
    const activities = weekElement.querySelectorAll('.activity-item');
    let critical = 0, nearCritical = 0, onTrack = 0, blocked = 0;
    
    activities.forEach(activity => {
        if (activity.classList.contains('critical')) critical++;
        else if (activity.classList.contains('near-critical')) nearCritical++;
        else if (activity.classList.contains('on-track')) onTrack++;
        else if (activity.classList.contains('blocked')) blocked++;
    });
    
    return { critical, nearCritical, onTrack, blocked };
}

// ============ EXPORT CAPABILITIES ============

function exportToCSV() {
    // Generate CSV export of daily schedule
    let csv = 'Date,Day,Activities,Subcontractor,Headcount,Materials,Notes\n';
    
    const rows = document.querySelectorAll('.days-table tbody tr');
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        const rowData = Array.from(cells).map(cell => 
            '"' + cell.textContent.replace(/"/g, '""') + '"'
        ).join(',');
        csv += rowData + '\n';
    });
    
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'lookahead_schedule.csv';
    a.click();
}
```

---

## 10. Responsive Design Notes

### Desktop (1200px+)
- Full 7-column table with all details visible
- Side-by-side weather forecast and activity list
- Fixed header with sticky navigation

### Tablet (768px–1023px)
- Compact font sizes
- Table columns retain structure but tighter padding
- Weather forecast in 3-column grid
- Touch-friendly buttons and interactive elements

### Mobile (< 768px)
- Table converts to vertical card layout (one day per "card")
- Stack columns vertically with data labels
- Full-width material delivery highlights
- Collapsible week sections to save vertical space
- Single-column legend
- Touch-optimized button sizes

### Print
- A4/Letter page breaks between weeks
- Hide non-essential UI elements (search, buttons)
- Optimize colors for B&W printing
- Preserve hierarchy and activity color coding

---

## 11. Data Embedding

All data is embedded as a JSON object in a `<script>` tag for offline use:

```html
<script type="application/json" id="lookahead-data">
{
    "metadata": {
        "project_code": "GC001",
        "project_name": "Main Building Construction",
        "generated_date": "2025-02-16T09:30:00Z",
        "lookahead_weeks": 3,
        "window_start": "2025-02-16",
        "window_end": "2025-03-08"
    },
    "alerts": [
        {
            "type": "blocker",
            "id": "RFI-025",
            "title": "RFI Response Due",
            "message": "RFI-025 response due Feb 24, blocks Concrete Pour",
            "severity": "critical"
        }
    ],
    "weeks": [
        {
            "week_number": 1,
            "start_date": "2025-02-16",
            "end_date": "2025-02-22",
            "days": [
                {
                    "date": "2025-02-17",
                    "day_of_week": "Monday",
                    "activities": [...],
                    "materials": [...],
                    "weather": {...}
                }
            ]
        }
    ]
}
</script>

<script>
// Parse and use embedded data
const lookaheadData = JSON.parse(document.getElementById('lookahead-data').textContent);
console.log('Lookahead for:', lookaheadData.metadata.project_name);
</script>
```

---

## 12. Chart.js Visualization Example

For projects with extended lookaheads (4+ weeks), a resource utilization chart is included:

```html
<div style="max-width: 800px; margin: 40px auto;">
    <h3 style="color: var(--navy); margin-bottom: 20px;">Crew Utilization Forecast</h3>
    <canvas id="crewChart"></canvas>
</div>

<script>
const ctx = document.getElementById('crewChart').getContext('2d');
const crewChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Feb 16', 'Feb 17', 'Feb 18', 'Feb 19', 'Feb 20', 'Feb 21', 'Feb 22'],
        datasets: [
            {
                label: 'ABC Excavation',
                data: [6, 6, 6, 6, 0, 4, 4],
                backgroundColor: '#2E5EAA'
            },
            {
                label: 'XYZ Concrete',
                data: [0, 0, 0, 0, 5, 5, 5],
                backgroundColor: '#FFC107'
            },
            {
                label: 'Site Power Co.',
                data: [3, 3, 0, 0, 0, 0, 0],
                backgroundColor: '#28A745'
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top'
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Crew Count'
                }
            }
        }
    }
});
</script>
```

---

## Summary: Template Checklist

- [x] Self-contained HTML5 with embedded CSS and JS
- [x] Navy/Blue color palette consistent with daily report
- [x] Header with project metadata
- [x] Alert/blocker banner section
- [x] Weather forecast strip
- [x] Week-by-week sections with headers
- [x] Daily table with 7 columns (Date, Day, Activities, Sub, Headcount, Materials, Notes)
- [x] Color-coded activity items (Red/Amber/Green/Gray)
- [x] Milestone markers with flags
- [x] Material delivery highlights
- [x] Subcontractor and crew info
- [x] Legend explaining color codes
- [x] Footer with metadata
- [x] Responsive design (mobile, tablet, desktop)
- [x] Print-friendly styles
- [x] JavaScript interactivity (tooltips, expand/collapse, search)
- [x] Embedded data for offline use
- [x] Chart.js for visualizations (optional)
- [x] No external file dependencies (except CDN)

