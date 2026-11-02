# Verified failure patterns from the 2026 project

Use when the matching failure appears; these are observations, not reasons to add every workaround to every task.

- Gaussian may say `Optimization completed on the basis of negligible forces.` rather than `Optimization completed.`. Parse flexibly, then inspect stationary point, final forces and normal termination. Reuse a completed valid geometry; no-frequency optimization still lacks frequency evidence.
- ReadAtoms must be separated from Gen basis by a blank line (`****\n\natoms=H\n\n`). Test actual produced input, not just template text.
- Compare normalized text for LF/CRLF logical equality; separately hash actual bytes for receipts. Never compare an LF template hash with a CRLF file hash and call the job corrupt.
- RDKit APIs may fail on Unicode filenames on Windows; use Path.read_text + MolFromMolBlock, file-object suppliers and block-based writes. Preserve atom order/explicit H.
- A cached filename “A completed” once contained originalR/A result. Check internal label, source project, geometry map, method and SP+thermal=G; retrieve actual final endpoint when inconsistent.
- PBS qstat/qsub may be unavailable while existing compute jobs continue. SSH transport and scheduler server health are separate.
- Unknown qsub acceptance: reconcile before retry. A shared filesystem rejectedflock; an atomic mkdir protected the reviewed single submission. Do not remove stale locks before checking their ownership/state.
- Windows shell expansion can consume `$d` intended for a remote shell. Prefer properly quoted argument lists, Python remote code and structured results.
- Long CPHF intervals can be normal; logs advanced roughly every10–20min in this case. Use queue/CPU/scratch/log evidence rather than declaring a hang from one unchanged tail.
- Cancel local pipeline parent and verified descendants to prevent stage continuation; preserve other processes. Stop a monitor through its automation API, not by deleting quantum jobs.

Project provenance and exact historical results remain in the research project, not in this portable skill. No task should automatically resume because this file describes it.
