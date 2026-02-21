---
description: Review submittals against spec requirements
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [submittal ID, or upload a submittal PDF]
---

## Overview
Cross-reference a submittal against spec requirements to generate compliance comments and approval recommendations. This command validates that submitted products, materials, and specifications meet the project requirements.

**Skills Referenced:**
- `${CLAUDE_PLUGIN_ROOT}/skills/submittal-intelligence/SKILL.md` - Submittal review methodology
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` - Project intelligence and requirements
- `${CLAUDE_PLUGIN_ROOT}/skills/document-intelligence/SKILL.md` - Document extraction and analysis

## Execution Steps

### 1. Identify the Submittal
- Check `$ARGUMENTS` for submittal ID (e.g., "SUB-001", "HVAC-02")
- If no ID found, accept PDF file upload
- If both: validate ID exists in `submittal-log.json` (submittal_log array) before processing

### 2. Extract Product Specifications (if new upload)
- Use document-intelligence skill to extract from PDF:
  - Product name and manufacturer
  - Model number and specification data
  - Performance ratings and certifications
  - Dimensions, materials, finishes
  - Installation requirements
  - Warranty and maintenance info

### 3. Determine Spec Section
- Query `submittal-log.json` (submittal_log array) for the spec section associated with the submittal ID
- If not found and PDF uploaded: ask user which spec section (e.g., "06 1000 Rough Carpentry", "08 7100 Hardware")
- Validate against project spec_sections in `specs-quality.json` (spec_sections)

### 4. Load Spec Requirements
From `specs-quality.json` (spec_sections), retrieve all spec requirements for the identified section:
- Material/product specifications
- Performance standards
- Testing and certification requirements
- Installation and quality standards
- Finish and appearance requirements
- Code compliance requirements

### 5. Build Compliance Matrix
Create a structured comparison:

| Spec Requirement | Required Value | Submitted Value | Compliance Status | Notes |
|---|---|---|---|---|
| [Spec item] | [Required] | [Submitted] | Compliant / Non-Compliant / Partial / Unable to Verify | [Details] |

For each requirement:
- Extract the requirement statement from spec
- Extract submitted value from submittal
- Determine status:
  - **Compliant**: Submitted meets or exceeds requirement
  - **Non-Compliant**: Submitted fails to meet requirement
  - **Partially Compliant**: Meets some but not all aspects
  - **Unable to Verify**: Insufficient data to determine compliance

### 6. Generate Overall Recommendation
Based on compliance matrix, assign one of:
- **Approved**: All requirements met, no exceptions
- **Approved as Noted**: Meets requirements with minor clarifications or acceptable deviations
- **Revise and Resubmit**: Specific non-compliances must be corrected
- **Rejected**: Critical non-compliances make submittal unacceptable

### 7. Draft Professional Review Comments
Write comprehensive comments organized by:
- **Overall Assessment**: Summary statement of recommendation
- **Compliant Items**: Acknowledgment of items meeting spec
- **Items Requiring Clarification**: Specific questions or requests for more data
- **Non-Compliant Items**: Specific deviations and why they matter
- **Required Actions**: What must be done to gain approval
- **Suggested Alternatives**: If recommending rejection, offer acceptable options

Use professional, constructive language suitable for owner/architect review.

### 8. Present to User for Review
Display:
- Submittal identification (ID, date, contractor)
- Compliance matrix (visual table)
- Overall recommendation (highlighted)
- Review comments
- Option buttons:
  - **Approve**: Mark as approved in submittal_log
  - **Edit Comments**: Refine review language
  - **Request Revision**: Generate RFI or mark for resubmittal
  - **Export PDF**: Create formatted review document

### 9. Update Submittal Log
Once approved or action taken, update `submittal-log.json` (submittal_log array) entry with:
- Review date and reviewer
- Compliance matrix data
- Recommendation and status
- Comments/observations

### 10. Export Option
- Generate formatted PDF: `{PROJECT_CODE}_Submittal_Review_{submittal_id}_{date}.pdf`
- Include: submittal details, compliance matrix, comments, approval stamp
- Ready for distribution to contractor/architect

### 11. Save & Log
1. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | submittal-review | [action] | [submittal ID, recommendation]
   ```
2. If project data changed significantly, regenerate `CLAUDE.md` to reflect the latest project state
