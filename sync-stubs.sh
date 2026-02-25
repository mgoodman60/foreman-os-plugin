#!/bin/bash
# sync-stubs.sh — Sync stub SKILL.md files from canonical sources to consumer plugins
# Run from the foreman-os repo root after editing any canonical skill SKILL.md
#
# Stubs are SKILL.md-only copies that let commands in other plugins reference
# skill methodology without requiring the full skill (with all its references/).
# Agents are NEVER copied — cross-plugin agent needs are handled by inlining
# methodology into commands or using soft refs.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
CHANGED=0

sync_stub() {
  local canonical="$1"
  local stub="$2"
  local source_plugin="$3"

  local header="<!-- STUB: Canonical source is ${source_plugin}/skills/$(basename "$(dirname "$canonical")")/SKILL.md. Run sync-stubs.sh to update. Do NOT edit directly. -->"

  # Build expected stub content
  local expected
  expected=$(printf '%s\n' "$header"; cat "$canonical")

  if [ ! -f "$stub" ]; then
    echo "  CREATE: $stub"
    mkdir -p "$(dirname "$stub")"
    printf '%s\n' "$header" > "$stub"
    cat "$canonical" >> "$stub"
    CHANGED=$((CHANGED + 1))
    return
  fi

  local current
  current=$(cat "$stub")

  if [ "$current" != "$expected" ]; then
    echo "  UPDATE: $stub"
    printf '%s\n' "$header" > "$stub"
    cat "$canonical" >> "$stub"
    CHANGED=$((CHANGED + 1))
  fi
}

echo "Syncing skill stubs..."
echo ""

# project-data/SKILL.md: core → intel, field, planning, doccontrol, cost, compliance
echo "project-data/SKILL.md (core → 6 plugins)"
for plugin in foremanos-intel foremanos-field foremanos-planning foremanos-doccontrol foremanos-cost foremanos-compliance; do
  sync_stub \
    "$REPO_ROOT/foremanos-core/skills/project-data/SKILL.md" \
    "$REPO_ROOT/$plugin/skills/project-data/SKILL.md" \
    "foremanos-core"
done

# report-qa/SKILL.md: field → planning
echo "report-qa/SKILL.md (field → planning)"
sync_stub \
  "$REPO_ROOT/foremanos-field/skills/report-qa/SKILL.md" \
  "$REPO_ROOT/foremanos-planning/skills/report-qa/SKILL.md" \
  "foremanos-field"

# document-intelligence/SKILL.md: intel → doccontrol, compliance
echo "document-intelligence/SKILL.md (intel → doccontrol, compliance)"
for plugin in foremanos-doccontrol foremanos-compliance; do
  sync_stub \
    "$REPO_ROOT/foremanos-intel/skills/document-intelligence/SKILL.md" \
    "$REPO_ROOT/$plugin/skills/document-intelligence/SKILL.md" \
    "foremanos-intel"
done

# estimating-intelligence/SKILL.md: intel → cost
echo "estimating-intelligence/SKILL.md (intel → cost)"
sync_stub \
  "$REPO_ROOT/foremanos-intel/skills/estimating-intelligence/SKILL.md" \
  "$REPO_ROOT/foremanos-cost/skills/estimating-intelligence/SKILL.md" \
  "foremanos-intel"

# delay-tracker/SKILL.md: cost → compliance
echo "delay-tracker/SKILL.md (cost → compliance)"
sync_stub \
  "$REPO_ROOT/foremanos-cost/skills/delay-tracker/SKILL.md" \
  "$REPO_ROOT/foremanos-compliance/skills/delay-tracker/SKILL.md" \
  "foremanos-cost"

# quantitative-intelligence/SKILL.md: intel → planning
echo "quantitative-intelligence/SKILL.md (intel → planning)"
sync_stub \
  "$REPO_ROOT/foremanos-intel/skills/quantitative-intelligence/SKILL.md" \
  "$REPO_ROOT/foremanos-planning/skills/quantitative-intelligence/SKILL.md" \
  "foremanos-intel"

# submittal-intelligence/SKILL.md: doccontrol → planning
echo "submittal-intelligence/SKILL.md (doccontrol → planning)"
sync_stub \
  "$REPO_ROOT/foremanos-doccontrol/skills/submittal-intelligence/SKILL.md" \
  "$REPO_ROOT/foremanos-planning/skills/submittal-intelligence/SKILL.md" \
  "foremanos-doccontrol"

echo ""
if [ "$CHANGED" -eq 0 ]; then
  echo "All stubs up to date. No changes needed."
else
  echo "$CHANGED stub(s) updated."
fi
