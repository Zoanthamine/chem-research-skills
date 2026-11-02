# Local xTB conformer workflow

## Verified project recipe and scope

This project used GFN-FF annealing, GFN1 normal optimization, then GFN2 tight refinement and deduplication. It is a practical local alternative to the existing GROMACS/CREST chain; it is not equivalent to CREST iMTD-GC, metadynamics, GAFF/RESP MD or an exhaustive global search.

1. Read validated MOL/SDF and preserve atom order/stereochemistry. Convert to XYZ only after recording graph and atom map. Check nonbonded clashes before GFN-FF topology assignment. One input required UFF clash removal; verify graph/stereo after repair and preserve the failed trajectory.
2. GFN-FF initial tight optimization, graph/stereo audit before long MD.
3. Example proven sampling: one continuous 600ps trajectory, three heat/cool cycles, natural H masses, no SHAKE, time step0.5fs, native xTB Berendsen NVT, output every0.1ps. Each 200ps cycle heats100→2000K over30ps, holds to80ps, cools to100K by200ps. Temperature implemented as short constant-target segments with continuous coordinate AND velocity restart, not fresh MD each segment. Record actual schedule approximation, restart hashes and seeds/version where available. Native Windows SHAKE restart had crashed and was not used in the accepted recipe.
4. High-temperature sampling is a candidate-generation strategy, not 298K equilibrium population. Filter every extracted geometry for connectivity/stereo; if decomposition or epimerization dominates, diagnose rather than silently replacing the chemistry. Other molecules may need lower temperatures or different sampling.
5. Select up to300 valid frames across the complete trajectory for low-cost refinement in this example; retain cycle/time provenance. GFN1 optimize normal, cluster, GFN2 optimize tight and cluster again. Historical fine thresholds Edis0.2/Gdis0.20 then0.10 are tied to the specific clustering program and its units; confirm those units and implementation before reuse.
6. Rank each method separately; export complete validated conformer pool plus top6 PDB/SDF/XYZ and energy table. Keep originalIDs, GFN2 energy, relative kcal/mol, origin frames, converged flag and rejection reasons.
7. Diagnose repeated low-basin discovery by cycle and compare independent starts/seeds when resources allow. Three cycles in one continuous trajectory are not independent seed replicates. Report “lowest found”.

## xTB command fragments

After validating binary/version and explicit metadata, a neutral closed-shell example is `xtb start.xyz --gfnff --chrg 0 --opt tight`; GFN2 refinement uses `xtb conformer.xyz --gfn 2 --chrg 0 --uhf 0 --opt tight`. For a neutral doublet use `--chrg 0 --uhf 1`. Validate the actual version's CLI first; these examples do not select a generic molecule's charge for you.

MD control concept for the tested backend:

```text
$md
 temp=<segment_target_K>
 time=<segment_length_ps>
 dump=100
 step=0.5
 hmass=0
 shake=0
 nvt=true
 restart=<false_first_segment_true_afterwards>
$end
```

Reconstruct restart coordinates using the backend's documented units; the tested mdrestart positions were bohr. Keep velocities and check atom counts/order. Do not use this placeholder as a finished executable input.

## Higher-cost branch

Keep the user cap (project default6) for Gaussian optimization/frequency and ORCA SP. Recluster after DFT. Only derive Gibbs populations when appropriate thermochemical evidence exists; xTB electronic-energy Boltzmann estimates are not reliable experimental conformer fractions by declaration.
