#!/usr/bin/env node
"use strict";

/**
 * data-loss-guard.js
 *
 * Claude Code PreToolUse hook (matcher: Write)
 * Warns before potential data loss in AI - Project Brain/ JSON files.
 *
 * Compares record counts between the existing file on disk and the
 * incoming content. If any top-level array shrinks or disappears,
 * a warning is emitted to stderr. The hook never blocks — it always
 * passes the original stdin JSON through to stdout unchanged.
 */

const fs = require("fs");
const path = require("path");

function warn(msg) {
  process.stderr.write(`[Hook] data-loss-guard: ${msg}\n`);
}

function isProjectBrainJson(filePath) {
  if (!filePath) return false;
  const hasMarker =
    filePath.includes("AI - Project Brain/") ||
    filePath.includes("AI - Project Brain\\") ||
    filePath.includes("AI%20-%20Project%20Brain/") ||
    filePath.includes("AI%20-%20Project%20Brain\\");
  return hasMarker && filePath.endsWith(".json");
}

function getFileName(filePath) {
  const normalized = filePath.replace(/\\/g, "/");
  const parts = normalized.split("/");
  return parts[parts.length - 1];
}

/**
 * Collect all top-level keys whose values are arrays.
 * Returns a Map of key -> array length.
 */
function getArrayKeys(obj) {
  const map = new Map();
  if (typeof obj !== "object" || obj === null || Array.isArray(obj)) {
    return map;
  }
  for (const key of Object.keys(obj)) {
    if (Array.isArray(obj[key])) {
      map.set(key, obj[key].length);
    }
  }
  return map;
}

function checkDataLoss(toolInput) {
  const filePath = toolInput.file_path || "";
  const content = toolInput.content;

  if (!isProjectBrainJson(filePath)) {
    return;
  }

  const fileName = getFileName(filePath);

  // Parse the new content
  let newData;
  try {
    newData = JSON.parse(content);
  } catch (e) {
    warn(`${fileName}: new content is not valid JSON — skipping comparison (${e.message})`);
    return;
  }

  // Read the existing file from disk
  let existingRaw;
  try {
    existingRaw = fs.readFileSync(filePath, "utf8");
  } catch (e) {
    // File does not exist yet (new file) or unreadable — nothing to compare
    return;
  }

  let existingData;
  try {
    existingData = JSON.parse(existingRaw);
  } catch (e) {
    warn(`${fileName}: existing file on disk is not valid JSON — skipping comparison`);
    return;
  }

  // Collect top-level array keys from both versions
  const existingArrays = getArrayKeys(existingData);
  const newArrays = getArrayKeys(newData);

  if (existingArrays.size === 0) {
    // Existing file has no top-level arrays — nothing to guard
    return;
  }

  // Check each existing array key
  for (const [key, oldCount] of existingArrays) {
    if (!newArrays.has(key)) {
      // Key present in old, missing in new
      if (oldCount > 0) {
        warn(
          `Data loss warning: ${fileName} missing key "${key}" that exists in current file (${oldCount} records)`
        );
      }
    } else {
      const newCount = newArrays.get(key);
      if (newCount < oldCount) {
        warn(
          `Data loss warning: ${fileName} ${key} shrinking from ${oldCount} to ${newCount} records`
        );
      }
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
    // Parse hook input
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

    // Only act on Write operations
    if (toolName === "Write") {
      try {
        checkDataLoss(toolInput);
      } catch (e) {
        warn(`Unexpected error: ${e.message}`);
      }
    }

    // Always pass through unchanged
    process.stdout.write(inputData);
  });
}

main();
