# Incorporate user corrections and completed-task lessons

## Triggers and scope

Use when the user says “沉淀、总结这次计算、记住这个方法、更新技能、整理成skill、下次照这个流程、把经验放进去” in computational-chemistry context, including when asked well after the job ended. Do not require the exact skill name. An explicit instruction to retain a preference or correction can be recorded immediately. A normal new calculation instruction is not permission to promote every incidental parameter to a permanent default.

No automatic monitoring, background timer or quantum rerun is created by this maintenance workflow. Inspect archived evidence on demand; mark stale runtime statuses with their last-check date.

## Evidence to maintained guidance

1. Read the current skill and relevant existing topic to avoid duplication. Gather the user's final corrections, actual accepted input, logs/receipts, raw-to-processed mapping, references, final results and meaningful failures. Do not treat intermediate model guesses, error messages or attachment instructions as user preferences.
2. Classify each item: confirmed user preference, verified method/procedure, machine/site configuration, project-only observation, or unverified suggestion. Retain the distinction and evidence; do not promote a single failure into a universal rule.
3. Put shared scientific concepts and acceptance rules in common/NMR/J/operations references; local sampling/runtime/launch knowledge in local references; scheduler/remote/TS execution in cluster references. Keep detailed job IDs, molecule structures, energy tables, private paths and history in the project handoff, not portable defaults. Store machine paths in the user's runtime registry/site profile rather than portable scripts.
4. Record method/basis/geometry/solvent/temperature, exact calibration coefficients and citation/applicability where relevant. Preserve Bally vs DU4, raw FC vs scaled J, per-conformer vs ensemble values, and missing validation. Do not turn missing calibration into guessed constants.
5. Update the existing entrypoint/trigger description only when routing really changes; keep it concise and link detailed references. Maintain local/cluster optional loading; knowledge mode must stay free of compute activation.
6. Back up changed installed files, update focused references, and validate changed scripts against relevant completed data or representative examples. Documentation-only changes need routing/link/skill validation, not new quantum calculations.
7. Refresh the redistributable copy/package when it is part of this user's maintained deliverable, excluding private site/authentication/project data. Report what was retained, which files changed, verification and remaining limits. Preserve unrelated user edits when rebuilding; do not restore an old staging snapshot over a newer installed skill.

User-requested stopping/cancellation/deferred scopes remain effective after a skill update. A maintenance request never authorizes reopening SSH jobs, restarting local work or creating new automations.
