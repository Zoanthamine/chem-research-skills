# Local runtime, selected only for local mode

## Capability selection

Choose only needed components: structure handling (RDKit/Open Babel), inexpensive optimization/sampling (xTB; CREST optional and platform-dependent), Gaussian geometry/NMR/J (separately licensed), pure Python post-processing. An available organic chemistry MCP/plugin may handle structure operations if its actual tool schema supports them; the xTB executable is a backend, not proof that a named plugin is installed.

On Huangjt's installation read `$CODEX_HOME/tools/science/INTEGRATION.md` and environments.json; run through tools/science/science.ps1 science. Else use the user's configured environment and explicit executable paths or PATH. Do not install packages just to answer knowledge questions.

`scripts/backend_inventory.py --config assets/local-profile.example.json` inspects path availability only. Pass an edited profile with actual paths; it never launches programs, loads Gaussian, contacts SSH or changes the environment. Runtime/license compatibility still needs a small relevant validation before a production run. Avoid unrelated environment inventories.

## Configure and reuse tools on demand

The user requests that software actually needed in local tasks can be configured and retained for later reuse. Support Gaussian geometry/NMR/J; GROMACS molecular dynamics and simulated annealing; xTB GFN-FF/GFN1/GFN2; optional CREST/Molclus, ORCA, RDKit/Open Babel, VMD, Shermo and Multiwfn as the task requires. GROMACS is the G-starting MD/annealing software referred to in this project. Identify the sampler from actual execution records rather than guessing from filenames.

First inspect the active runtime registry and existing installation; reuse it before installing anything. Configure executable/version, required environment, scratch, resource defaults and meaningful smoke-test evidence for the selected tool. Installation, binary presence, connector availability, runtime validation and a proprietary license are separate statuses. Never bundle Gaussian/other licensed binaries or private site data into the shared skill. Do not download all tools simply because they are listed. If missing software truly requires installation, perform only the task-authorized setup within applicable permissions and approved distribution/license constraints; report the specific blocker otherwise.

The registry remains the single source of live machine paths; do not duplicate machine-specific executable paths across portable reference files. Use [task preflight](task-preflight.md) for each launch and [experience maintenance](experience-maintenance.md) to retain verified setup/protocol changes.

## Execution contract

- Explicit input graph, charge, multiplicity/unpaired electrons, output directory, resource budget, selected stages and stage stop conditions.
- Local xTB used 2 threads in the verified project; this is a resource choice, not a universal optimum. Gaussian used ~80% logical cores and conservative free memory (example 13/16 threads, 7–11GB), jobs serially. Reinspect current load before assigning resources.
- Use per-stage working directories and scratch, durable background launch, logs/receipt hashes and PID/process-tree identity. On Windows background helpers use hidden windows. Never stop all Gaussian processes by name to cancel one project.
- Read-only/knowledge work does not require expensive sampling. Changing selection, solvent, multiplicity or method requires explicit tracking in the manifest.
- Stop local runner and its identified descendants to prevent automatic next stages. Record cancellation and preserve complete stages. Never let a later monitor restart a user-cancelled pipeline.

Minimal profile fields: xtb executable, Gaussian executable, Python interpreter, outputs root, xTB thread count, Gaussian cores/memory, optional chemistry connector name. No SSH credentials in a local profile.
