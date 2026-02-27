#!/usr/bin/env node
"use strict";

/**
 * counter-reconciler.js
 *
 * Claude Code PostToolUse hook (matcher: Write)
 * Validates that counter fields in Project Brain JSON files match actual array lengths.
 *
 * - Reads hook JSON from stdin
 * - Checks if a Project Brain JSON file was written
 * - If so, validates counter fields against computed values
 * - Always passes input JSON through to stdout unchanged
 * - Emits warnings to stderr with [Hook] prefix on mismatches
 */

const path = require("path");

// Counter validation rules keyed by filename
const COUNTER_RULES = {
  "project-config.json": [
    {
      counterPath: ["documents_loaded_count"],
      arrayPath: ["documents_loaded"],
      mode: "length",
      label: "documents_loaded_count",
    },
  ],
  "schedule.json": [
    {
      counterPath: ["summary", "total_activities"],
      arrayPath: ["activities"],
      mode: "length",
      label: "summary.total_activities",
    },
  ],
  "submittal-log.json": [
    {
      counterPath: ["summary", "total_submittals"],
      arrayPath: ["submittals"],
      mode: "length",
      label: "summary.total_submittals",
    },
  ],
  "rfi-log.json": [
    {
      counterPath: ["summary", "total_rfis"],
      arrayPath: ["rfis"],
      mode: "length",
      label: "summary.total_rfis",
    },
  ],
  "change-order-log.json": [
    {
      counterPath: ["summary", "total_change_orders"],
      arrayPath: ["change_orders"],
      mode: "length",
      label: "summary.total_change_orders",
    },
  ],
  "procurement-log.json": [
    {
      counterPath: ["summary", "total_items"],
      arrayPath: ["items"],
      mode: "length",
      label: "summary.total_items",
    },
  ],
  "inspection-log.json": [
    {
      counterPath: ["summary", "total_inspections"],
      arrayPath: ["inspections"],
      mode: "length",
      label: "summary.total_inspections",
    },
  ],
  "cost-data.json": [
    {
      counterPath: ["summary", "subtotal_direct"],
      arrayPath: ["budget_by_division"],
      mode: "sum",
      sumField: "total",
      label: "summary.subtotal_direct",
    },
  ],
};

/**
 * Safely traverse a nested object by an array of keys.
 * Returns undefined if any segment is missing.
 */
function getNestedValue(obj, keys) {
  let current = obj;
  for (const key of keys) {
    if (current == null || typeof current !== "object") {
      return undefined;
    }
    current = current[key];
  }
  return current;
}

/**
 * Run counter validations for a given filename against parsed JSON content.
 * Emits warnings to stderr for each mismatch found.
 */
function validateCounters(filename, data) {
  const rules = COUNTER_RULES[filename];
  if (!rules) return;

  for (const rule of rules) {
    const storedValue = getNestedValue(data, rule.counterPath);

    // If the counter field doesn't exist in the data, skip silently
    if (storedValue === undefined) continue;

    let computedValue;

    if (rule.mode === "length") {
      const arr = getNestedValue(data, rule.arrayPath);
      if (!Array.isArray(arr)) continue;
      computedValue = arr.length;
    } else if (rule.mode === "sum") {
      const arr = getNestedValue(data, rule.arrayPath);
      if (!Array.isArray(arr)) continue;
      computedValue = 0;
      for (const item of arr) {
        const val = item != null ? item[rule.sumField] : undefined;
        if (typeof val === "number" && !isNaN(val)) {
          computedValue += val;
        }
      }
      // Round to avoid floating-point drift (2 decimal places for currency)
      computedValue = Math.round(computedValue * 100) / 100;
    }

    if (computedValue === undefined) continue;

    // Compare: for sums use a small tolerance, for lengths use strict equality
    let mismatch = false;
    if (rule.mode === "sum") {
      mismatch = Math.abs(storedValue - computedValue) > 0.01;
    } else {
      mismatch = storedValue !== computedValue;
    }

    if (mismatch) {
      const unit = rule.mode === "sum" ? "" : " items";
      console.error(
        `[Hook] Counter mismatch in ${filename}: ${rule.label} is ${storedValue} but array has ${computedValue}${unit}`
      );
    }
  }
}

function main() {
  let raw = "";
  process.stdin.setEncoding("utf8");

  process.stdin.on("data", (chunk) => {
    raw += chunk;
  });

  process.stdin.on("end", () => {
    // Always pass through the original input unchanged
    process.stdout.write(raw);

    let hookData;
    try {
      hookData = JSON.parse(raw);
    } catch {
      // Not valid JSON — nothing to check, just pass through
      return;
    }

    // Check if this is a Write to a Project Brain file
    const filePath = hookData?.tool_input?.file_path;
    if (!filePath || !filePath.includes("AI - Project Brain/")) {
      return;
    }

    // Must be a .json file
    if (!filePath.endsWith(".json")) {
      return;
    }

    const filename = path.basename(filePath);

    // Only check files we have rules for
    if (!COUNTER_RULES[filename]) {
      return;
    }

    // Parse the written content
    const content = hookData?.tool_input?.content;
    if (typeof content !== "string") {
      return;
    }

    let data;
    try {
      data = JSON.parse(content);
    } catch {
      console.error(
        `[Hook] Could not parse JSON content for counter check in ${filename}`
      );
      return;
    }

    validateCounters(filename, data);
  });
}

main();
