#!/usr/bin/env node
"use strict";

/**
 * project-brain-validator.js
 *
 * Claude Code PreToolUse hook (matcher: Write|Edit)
 * Validates writes to the AI - Project Brain/ directory.
 *
 * - Checks JSON validity on Write operations
 * - Validates canonical top-level array keys per file
 * - Warns on empty overwrites ({} or [])
 * - Never blocks — always passes input through to stdout
 * - Warnings go to stderr with [Hook] prefix
 */

const CANONICAL_KEYS = {
  "schedule.json": "activities",
  "delay-log.json": "delay_events",
  "submittal-log.json": "submittals",
  "rfi-log.json": "rfis",
  "change-order-log.json": "change_orders",
  "inspection-log.json": "inspections",
  "procurement-log.json": "items",
  "action-items.json": "items",
  "safety-log.json": "safety_entries",
  "labor-tracking.json": "labor_entries",
  "quality-data.json": "quality_records",
  "drawing-log.json": "drawings",
  "meeting-log.json": "meetings",
  "environmental-log.json": "entries",
};

function warn(msg) {
  process.stderr.write(`[Hook] project-brain-validator: ${msg}\n`);
}

function isProjectBrainPath(filePath) {
  return (
    filePath.includes("AI - Project Brain/") ||
    filePath.includes("AI - Project Brain\\") ||
    filePath.includes("AI%20-%20Project%20Brain/") ||
    filePath.includes("AI%20-%20Project%20Brain\\")
  );
}

function getFileName(filePath) {
  const normalized = filePath.replace(/\\/g, "/");
  const parts = normalized.split("/");
  return parts[parts.length - 1];
}

function validateWrite(toolInput) {
  const filePath = toolInput.file_path || "";
  const content = toolInput.content;

  if (!isProjectBrainPath(filePath)) {
    return;
  }

  const fileName = getFileName(filePath);

  if (!fileName.endsWith(".json")) {
    return;
  }

  // Rule 1: Valid JSON
  let parsed;
  try {
    parsed = JSON.parse(content);
  } catch (e) {
    warn(`Invalid JSON in ${fileName}: ${e.message}`);
    return;
  }

  // Rule 3: No empty overwrites
  if (typeof parsed === "object" && parsed !== null) {
    if (Array.isArray(parsed) && parsed.length === 0) {
      warn(
        `Writing empty array [] to ${fileName} — possible accidental data loss`
      );
    } else if (!Array.isArray(parsed) && Object.keys(parsed).length === 0) {
      warn(
        `Writing empty object {} to ${fileName} — possible accidental data loss`
      );
    }
  }

  // Rule 2: Canonical top-level keys
  const expectedKey = CANONICAL_KEYS[fileName];
  if (expectedKey && typeof parsed === "object" && parsed !== null && !Array.isArray(parsed)) {
    const topKeys = Object.keys(parsed);
    if (topKeys.length > 0 && !topKeys.includes(expectedKey)) {
      // Check if any key looks like a misnamed array
      const arrayKeys = topKeys.filter((k) => Array.isArray(parsed[k]));
      if (arrayKeys.length > 0) {
        warn(
          `${fileName}: expected canonical key "${expectedKey}" but found array key(s): ${arrayKeys.map((k) => `"${k}"`).join(", ")}`
        );
      }
    }
  }
}

function validateEdit(toolInput) {
  const filePath = toolInput.file_path || "";

  if (!isProjectBrainPath(filePath)) {
    return;
  }

  const fileName = getFileName(filePath);

  if (!fileName.endsWith(".json")) {
    return;
  }

  // For Edit, we can check if new_string is valid JSON when it looks like a
  // complete JSON replacement, but partial edits are expected. Only warn if
  // the new_string itself appears to be a complete JSON document that is invalid.
  const newString = toolInput.new_string || "";
  const trimmed = newString.trim();

  if (
    (trimmed.startsWith("{") && trimmed.endsWith("}")) ||
    (trimmed.startsWith("[") && trimmed.endsWith("]"))
  ) {
    try {
      const parsed = JSON.parse(trimmed);

      // Check empty replacement
      if (typeof parsed === "object" && parsed !== null) {
        if (Array.isArray(parsed) && parsed.length === 0) {
          warn(
            `Edit replacing with empty array [] in ${fileName} — possible accidental data loss`
          );
        } else if (!Array.isArray(parsed) && Object.keys(parsed).length === 0) {
          warn(
            `Edit replacing with empty object {} in ${fileName} — possible accidental data loss`
          );
        }
      }
    } catch (_) {
      // Partial JSON fragment in an edit is normal — don't warn
    }
  }
}

function main() {
  let inputData = "";

  process.stdin.setEncoding("utf8");

  process.stdin.on("data", (chunk) => {
    inputData += chunk;
  });

  process.stdin.on("end", () => {
    // Always output the original input unchanged
    let hookInput;
    try {
      hookInput = JSON.parse(inputData);
    } catch (_) {
      // Can't parse hook input — pass through as-is
      process.stdout.write(inputData);
      return;
    }

    const toolName = hookInput.tool_name || "";
    const toolInput = hookInput.tool_input || {};

    try {
      if (toolName === "Write") {
        validateWrite(toolInput);
      } else if (toolName === "Edit") {
        validateEdit(toolInput);
      }
    } catch (e) {
      warn(`Unexpected error during validation: ${e.message}`);
    }

    // Pass through unchanged
    process.stdout.write(inputData);
  });
}

main();
