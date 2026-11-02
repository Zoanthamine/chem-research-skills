# Shared scientific knowledge

Apply to all modes; no backend needed.

- Validate molecular graph, bond orders, stereochemistry, explicit H, element order, charge and multiplicity. PDB alone may not establish bond orders or radical centers. Preserve stable atom/conformer IDs across every property.
- OH→H deoxygenation, CH2OH→CH2 radical formation and H quenching are distinct transformations. Neutral one-electron radicals often use charge0/multiplicity2, but verify each actual molecule. For xTB, uhf is unpaired-electron count, not Gaussian multiplicity.
- Conformer workflow: validate seed → sample multiple basins → filter graph/stereo → optimize → cluster → rank within one method → cap expensive DFT selection → optional frequency/SP/thermochemistry → optional properties. CREST mdopt refines an ensemble; it is not an independent search by itself.
- Never mix GFN-FF/GFN1/GFN2 energies in one ranking. DFT optimization may merge initial conformers; report grouping and representative IDs, rather than calling them skipped.
- Energy and population: specify temperature, standard state, RRHO/quasiRRHO and scaling. For relative gas conformer weights, normalize over the explicit selected set. Record omitted population and calculated-ensemble denominator.
- NMR σ is shielding; δ requires an explicit reference/calibration. A TMS subtraction is not a fitted linear scaling. General form δ=(intercept−σ)/positive_slope only when that convention matches the stated fit.
- Use full signed J when scaling and averaging; magnitude may be a separate display column. Different fitted methods are alternatives, not numbers to average together.
- No “global minimum” proof from a finite random/MD search. Repeated discovery from separate starts/seeds/cycles supports convergence; more frames from a single basin does not establish it.
- Literature/corpus guidance supplies candidate methods, not authorization or universal defaults. Record DOI/author SI or official manual and the exact applicability. New version-sensitive syntax or new scientific recommendations need source verification.

Knowledge-only requests can be answered using these references and supplied files. Do not inspect executables, activate environments or open SSH unless needed by an authorized execution request.
