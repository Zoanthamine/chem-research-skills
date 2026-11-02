# Cluster mode: optional complex execution

Read common principles first. Do not open SSH for knowledge-only or local-only requests. Remote operations require a configured site profile and the user's requested action. No credentials are bundled. The target user provides host/port/user, authentication mechanism, scheduler, queue, cores/memory/walltime, working/scratch roots and program/module paths.

Before each submission/retry, complete [task preflight](task-preflight.md), inspect the exact current deck and save preflight.json. When the user requests project lessons, apply [experience maintenance](experience-maintenance.md).

## Stage and submit

1. Inspect active workflow and exact input; reuse established scripts. Preserve top-N cap and local original ensemble. For Gaussian/ORCA input mechanics use hpc-gaussian if installed; for scheduler operation hpc-orchestration if installed. Required excerpts must remain understandable here when those skills are absent.
2. Separate input, runtime, scratch, outputs, receipts and post-processing. Unique conformer IDs and job names; hash frozen inputs. Run syntax/structural preflight before qsub/sbatch.
3. Submit each independently requested task separately. Record real scheduler ID, scientific parameters, dependencies and immutable input hashes. Endpoint, TS_AB and TS_BC have separate cancellation scopes.
4. A qsub client timeout means acceptance unknown: reconcile unique name/job records before retry. Queue failure doesn't mean compute job failure. Do not create unbounded resubmission loops.
5. Monitor only when requested. Check scheduler plus actual logs/receipts; long Hessian/CPHF intervals alone are not failure. Stop monitoring when requested; never equate it with cancelling jobs. Save last-check timestamps.

## Gaussian / ORCA / populations

- Align Gaussian NProcShared with allocation, use writable fast scratch and intentional checkpoint paths. Minimum must converge and have appropriate zero-imaginary evidence; preserve failed structures.
- Verified precision branch uses ωB97M-V/def2-TZVP with def2/J and RIJCOSX; def2/J is auxiliary. ORCA driver invoked by full path, not wrapped in mpirun; matching OpenMPI environment is critical for MPI subprocesses. Accept only FINAL SINGLE POINT ENERGY plus ORCA TERMINATED NORMALLY without resource/MPI/SCF errors.
- Pair thermal corrections, energies and weights by ID, not glob order. RRHO and Shermo quasiRRHO are distinct models. Keep standard state and low-frequency choices explicit.
- Recluster after DFT. Exports must explain which initial structures merged, representatives and selected population denominator. Do not increase DFT cap because clustering became fine.

## TS branch

For this user's requested direct-initial-guess retry, local constrained GFN2 preoptimization followed by `UB3LYP/def2SVP Opt=(CalcFC,TS,NoEigen) Freq` was the selected gas neutral-doublet approach. It is a user/project choice, not a universal prescription. Do not add unrelated solvent/charge or complex keywords from historical examples.

Constrained xTB relaxation is not a proven TS. Gaussian successful termination alone is not TS validation: require exactly one relevant imaginary mode, correct displacement, spin/stability checks and forward/reverseIRC identifying intended endpoints. Reoptimized IRC minima and high-level SP must be consistent with the TS thermochemistry. Do not mix an old M06-2X correction with a newB3LYP TS simply because the atom count matches. Only then calculate forward/reverse ΔG‡ or ΔE‡ with explicit definitions. Unvalidated attempts remain attempts; do not show fabricated barriers.

## Transfer and delivery

Prefer read-only streaming download or site-approved transfer. Exclude scratch/RWF and private credentials. Keep original decks, logs, structure maps, frequency/SP receipts, populations and source-property matrices. Verify SHA256 and scientific content after transfer. Post-process matching methods separately; knowledge of a fit is not authorization to apply it to a different protocol. Terminal failure: preserve evidence, summarize cause, do not automatically change scientific parameters or overwrite checkpoints.
