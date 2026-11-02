# Mandatory before local launch or cluster submission

Apply for each newly launched/submitted computational-chemistry job, including a retry or a modified deck. Reuse still-current evidence; inspect the actual input bytes and active state each time. This is an operational check, not a demand for repeated user approval. An authorized unchanged plan can proceed after checks pass.

## Shared checks

1. Read this skill and only the selected knowledge/local/cluster topic. Match the user's latest instruction to the actual job, requested stage, cost cap, cancelled/deferred tasks and selected execution site. Do not widen the requested task merely to match a template.
2. Validate structure graph, stereochemistry, atom map, hydrogens, charge/multiplicity; record radical identity. Check substrate/endpoint/TS identity, not filenames alone.
3. Read the finished input: method/basis, task keywords, solvent, temperature/standard state where applicable, frequency requested or omitted, checkpoint/scratch, exact basis blocks and required blank lines. For NMR/J check calibration scope, FC variant and CH2 environment mapping. Do not substitute SMD/PCM coefficients or average Bally/DU4.
4. Check CPU/memory/walltime, current resource availability, explicit conformer cap and count of jobs. Compare prepared configuration against the existing verified workflow and latest user instruction. Verify upstream stages/receipt hashes; do not run a property on an invalid or wrong structure.
5. Check whether a matching job is running/queued/completed, whether a prior submission has unknown acceptance, and whether a parent automation could duplicate it. Reconcile before retrying. A cancelled task requires a new user request before restart.
6. Write a compact project `preflight.json` (or extend the existing manifest) with timestamp, selected mode, input hashes, actual parameters, check outcomes, unresolved issues and launch decision. No credentials. Check only relevant items; mark others not applicable with a reason. Changed files invalidate their earlier check.
7. Launch only when relevant checks pass, then record PID/process identity or actual scheduler job ID. If a material choice remains ambiguous, explain the concrete issue and clarify; routine reversible corrections within authorization do not require a new approval loop.

## Local additions

Inspect configured executable/profile and version/runtime compatibility for the selected tools only. Use already-installed Gaussian, GROMACS, xTB, ORCA, CREST/Molclus, RDKit/Open Babel, VMD, Shermo or Multiwfn where needed; these are capabilities, not mandatory dependencies. Check existing load, threading/MPI/GPU compatibility if relevant, writable scratch and intended output directory. Preserve process-tree ownership for cancellation. Run syntax/deck checks and a small relevant smoke test only when the backend/configuration is new or changed; do not repeat costly tests for every molecule.

## Cluster additions

Check configured site/scheduler, actual queue/resource directives, program/module/MPI environment, scratch permissions, frozen input/script hashes and dependencies. Use syntax checks and available ShellCheck. SSH success alone does not establish scheduler health. qsub timeout/transport interruption is unknown acceptance until reconciled, not a reason for blind resubmission.

## Knowledge-only exclusion

Knowledge-only explanations, review and “沉淀” do not trigger executable inventory, licensed program launch, SSH or a full production preflight. Save factual guidance without starting or resuming jobs.
