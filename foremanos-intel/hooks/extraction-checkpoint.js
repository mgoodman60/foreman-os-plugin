#!/usr/bin/env node
/**
 * extraction-checkpoint.js
 *
 * Claude Code PreCompact hook (matcher: *)
 * Saves extraction progress before context compaction so that a resumed
 * session can pick up where it left off.
 *
 * Behaviour:
 *   1. Reads stdin JSON (compaction event data).
 *   2. Searches for `AI - Project Brain/project-config.json` on disk.
 *   3. If found, summarises extraction state from `documents_loaded[]`
 *      and writes `.extraction-checkpoint.json` beside it.
 *   4. Passes the original stdin JSON through to stdout (required by hooks).
 *
 * All informational messages go to stderr with a "[Hook]" prefix.
 */

'use strict';

const fs   = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/** Log to stderr so stdout stays clean for the hook pass-through. */
function log(msg) {
  process.stderr.write(`[Hook] extraction-checkpoint: ${msg}\n`);
}

/**
 * Search common locations for project-config.json.
 * Returns the absolute path if found, otherwise null.
 */
function findProjectConfig() {
  const cwd = process.cwd();
  const candidates = [
    path.join(cwd, 'AI - Project Brain', 'project-config.json'),
    path.join(cwd, '..', 'AI - Project Brain', 'project-config.json'),
    path.join(cwd, '..', '..', 'AI - Project Brain', 'project-config.json'),
  ];

  // Also walk up from cwd looking for the marker directory.
  let dir = cwd;
  for (let i = 0; i < 6; i++) {
    const candidate = path.join(dir, 'AI - Project Brain', 'project-config.json');
    if (!candidates.includes(candidate)) {
      candidates.push(candidate);
    }
    const parent = path.dirname(dir);
    if (parent === dir) break; // reached root
    dir = parent;
  }

  for (const candidate of candidates) {
    try {
      fs.accessSync(candidate, fs.constants.R_OK);
      return path.resolve(candidate);
    } catch {
      // not found here, try next
    }
  }

  return null;
}

/**
 * Summarise the extraction state from the documents_loaded array.
 *
 * Status values observed in the wild:
 *   - "extracted"                 -> fully extracted
 *   - "finalized"                -> post-extraction (counts as extracted)
 *   - "current", "received",
 *     "submitted", "executed",
 *     "filed"                    -> loaded but extraction may vary
 *   - "template"                 -> not a real document
 *   - "superseded_by_conformance"-> skipped
 *
 * We classify a document as "extracted or later" when its status is one of
 * the terminal states that imply data was pulled from it.
 */
function summariseExtraction(config) {
  const docs = config.documents_loaded || [];

  // Statuses that mean extraction work has been done on this document.
  const extractedStatuses = new Set([
    'extracted',
    'finalized',
  ]);

  // Statuses that mean the document is present but not yet extracted.
  const pendingStatuses = new Set([
    'current',
    'received',
    'submitted',
    'executed',
    'filed',
  ]);

  // Statuses we intentionally skip (not real extraction targets).
  const skippedStatuses = new Set([
    'template',
    'superseded_by_conformance',
  ]);

  let extracted = 0;
  let pending   = 0;
  let skipped   = 0;
  let unknown   = 0;

  for (const doc of docs) {
    const status = (doc.status || '').toLowerCase().trim();
    if (extractedStatuses.has(status)) {
      extracted++;
    } else if (pendingStatuses.has(status)) {
      pending++;
    } else if (skippedStatuses.has(status)) {
      skipped++;
    } else {
      unknown++;
    }
  }

  // Determine last completed extraction phase from version_history if available.
  let lastPhaseCompleted = null;
  const versions = config.version_history || [];
  for (const entry of versions) {
    const desc = (entry.description || entry.action || entry.details || entry.note || entry.changes || '').toLowerCase();
    const phaseMatch = desc.match(/phase\s*(\d+)/);
    if (phaseMatch) {
      const phaseNum = parseInt(phaseMatch[1], 10);
      if (lastPhaseCompleted === null || phaseNum > lastPhaseCompleted) {
        lastPhaseCompleted = phaseNum;
      }
    }
  }

  return {
    documents_total:        docs.length,
    documents_extracted:    extracted,
    documents_pending:      pending,
    documents_skipped:      skipped,
    documents_unknown:      unknown,
    last_phase_completed:   lastPhaseCompleted,
    files_modified_this_session: [],
  };
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  // Collect all stdin data.
  const chunks = [];
  process.stdin.setEncoding('utf8');

  process.stdin.on('data', (chunk) => {
    chunks.push(chunk);
  });

  process.stdin.on('end', () => {
    const raw = chunks.join('');

    // Parse stdin JSON (best-effort; if it fails we still pass it through).
    let inputJson = null;
    try {
      inputJson = JSON.parse(raw);
    } catch {
      log('Could not parse stdin as JSON — passing through as-is.');
      process.stdout.write(raw);
      return;
    }

    // Find project-config.json.
    const configPath = findProjectConfig();
    if (!configPath) {
      log('No project-config.json found — skipping checkpoint (not an extraction session).');
      process.stdout.write(raw);
      return;
    }

    log(`Found project config at: ${configPath}`);

    // Read and parse project-config.json.
    let config;
    try {
      const configRaw = fs.readFileSync(configPath, 'utf8');
      config = JSON.parse(configRaw);
    } catch (err) {
      log(`Failed to read/parse project-config.json: ${err.message}`);
      process.stdout.write(raw);
      return;
    }

    // Build checkpoint data.
    const extractionState = summariseExtraction(config);
    const checkpoint = {
      checkpoint_date:    new Date().toISOString(),
      extraction_state:   extractionState,
      resume_instructions:
        'Read this checkpoint to resume extraction. Check documents_loaded[] in project-config.json for pending items.',
    };

    // Write checkpoint beside project-config.json.
    const brainDir       = path.dirname(configPath);
    const checkpointPath = path.join(brainDir, '.extraction-checkpoint.json');

    try {
      fs.writeFileSync(checkpointPath, JSON.stringify(checkpoint, null, 2) + '\n', 'utf8');
      log(`Checkpoint written to: ${checkpointPath}`);
      log(
        `State: ${extractionState.documents_extracted} extracted, ` +
        `${extractionState.documents_pending} pending, ` +
        `${extractionState.documents_total} total` +
        (extractionState.last_phase_completed !== null
          ? `, last phase: ${extractionState.last_phase_completed}`
          : '')
      );
    } catch (err) {
      log(`Failed to write checkpoint: ${err.message}`);
    }

    // Always pass through the original stdin JSON to stdout.
    process.stdout.write(raw);
  });
}

main();
