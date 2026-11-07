# NMR and two distinct J protocols

Use in knowledge, local or cluster mode; this page alone does not launch a backend.

## Chemical shifts

The verified low-cost local branch used gas B3LYP/6-31G(d) optimization without frequency, then GIAO B3LYP/6-31G(d), SMD chloroform, G09Defaults. Historical project conversion: δH=(32.2109−σ)/1.0157 and δC=(188.4418−σ)/0.9449. Reuse only after checking original calibration applicability including geometry, shielding convention, solvent and nucleus. These coefficients are not universal defaults or a validated calibration for arbitrary molecules.

The separate cluster branch used IEFPCM chloroform/G09Defaults: 01 B3LYP/6-31G(d), 02 mPW1PW91/6-311+G(d,p), 03 wB97XD/6-31G(d). 01/02 used each method's own configured TMS σTMS−σ reference; this is not the above SMD fit. Without a matched03 reference/scaling, retain σ and mark δ missing. Never silently copy coefficients across methods or solvents. Preserve coefficient source/version with the result; verify literature if choosing a new protocol.

## General H–H: Bally–Rablen

DOI: https://doi.org/10.1021/jo200513q (2011). Hydrogen-only u+1s prescription: gas B3LYP/6-31G(d) geometry; B3LYP/Gen FCOnly, ReadAtoms, Int=NoBasisTransform, G09Defaults. Exact basis block: `assets/basis/Bally-H-uplus1s.gbs`.

The published prescription (SI Table S4a code `H F H D N`) is: mixed (u+1s) basis on H only, Fermi contact only, `ReadAtoms/H`, **default SCF convergence and grid**, `integral=nobasistransform`. Do not add `SCF=XQC`, `NoSymm`, `scf=conver=10` or `grid=ultrafine` "for safety": none is part of the protocol, and the SI reports their effect on results as 0.00 Hz while costing time. `ReadAtoms/H` only limits which FC elements are computed; values match an all-atom run to 0.00–0.01 Hz, so printing the full matrix is acceptable when a shared parser needs it.

The u+1s hydrogen block is **eight s primitives + one p**, taken from the author's `mk_input_file`: four decontracted 6-31G s (18.7311, 2.8254, 0.6401, 0.1613), four added tight s (56.1934, 168.580, 505.741, 1517.222), p = 1.1. A trimmed 5s1p copy circulates in some setups; results from it are not comparable with 8s1p results. Non-hydrogen elements take the author-script default 6-31G(d,p) for every element present.

**J=0.9155×FC**, signed, no intercept. Do not substitute 0.9117 belonging to a different whole-basis/IOp implementation. Export all H–H pairs if requested, with bond distance to distinguish geminal/vicinal/long-range. This is FC empirical prediction, not the full Ramsey sum.

## CH2 geminal ²JHH: DU4

DOI: https://doi.org/10.1021/jo501781b (2014), author SI S2–S4. Exact basis block: `assets/basis/DU4-CHO.gbs`. Gas B3LYP/6-31G(d) geometry, FC only, `int=nobasistransform`.

The basis is assigned **per element** in the SI: C 4-31G; N/O/F/Li/Be/B 6-31G; Si/S/P/Cl/As/Se/Br/I **3-21G\***; H the optimised 8s1p block. Do not substitute 4-31G for Si, and do not assume "same as carbon" for other elements. Elements outside this list need method review.

The geminal class is a **chemical judgement**, not something a workflow should pick silently: compute FC, export raw per-conformer values plus a worksheet showing what each of the four formulas would give, then let post-processing choose and record the class, the resulting J and a one-line rationale. Frequent misclassifications: CH2–O is *not* CH2–Cπ; "small ring" means three- or four-membered only (a five-membered ring stays `sp3_general`); a CH2 adjacent to two π centres is outside the fitted set and must be flagged extrapolative; an acetal-type O–CH2–O has no dedicated class.

|CH2 environment code|Signed formula / Hz|
|---|---|
|sp3_general|1.240 FC +0.57|
|sp3_alpha_pi|1.072 FC −1.66|
|small_ring|1.249 FC +1.05|
|sp2|1.337 FC +0.52|

CH2–O is not CH2–Cπ merely because the O is conjugated. Ring and π-adjacency need graph/chemical review; a CH2 with two adjacentπcenters is explicitly extrapolative in this project, not a validated new fit class. Do not apply this geminal routing to ¹JCH or general vicinal³JHH. Record classification and source mapping per pair.

## Input and result gates

- Actual basis must end `****\n\natoms=H\n\n`; the blank line before ReadAtoms is essential.
- Basis-function totals are molecule-specific acceptance values, not universal constants. Count from the actual deck under the exact basis asset version, and label the asset version (8s1p vs a trimmed copy) on every J table; results from different basis versions are not comparable and must not be merged.
- Normal termination, intended method/basis, all H indices and exact pair counts, raw FC matrix, finite values and original file hashes. For N hydrogens expect N(N−1)/2 unordered pairs, so drop self-pairs before counting; the FC matrix diagonal is the magnetogyric-ratio term (order 1e11), not a coupling. Some ReadAtoms inputs request a subset: declare the subset instead of assuming full matrices.
- Identify each CH2 carbon and both explicit attached H from the molecular graph; Gaussian one-based IDs, same atom map as geometry and shift table. Do not carry atom-number assignments between different molecules.
- Separate CSVs for raw/marked/weighted Bally and DU4, preserve signed values. For each method `J_weighted=Σ wi J_i` with explicit selected IDs and normalized weights. Never average methods or silently insert missing conformers. Keep source ensemble coverage, gas/solution weighting conditions and extrapolation flags.
- Single-conformer tables contain no invented weights; keep separate filenames from final ensemble tables. Gas FC fits do not explicitly model CDCl3/MeCN effects.

## Assets and cheap processing

Use `scripts/coupling_postprocess.py` with explicit method selection and CSV schema in postprocess-cli.md. It performs no quantum calculation, no chemical environment inference and no source fitting. It rejects missing pairs/weights, duplicated unordered pairs, ambiguous environment codes and nonfinite numbers. Outputs raw+scaled and optionally weighted tables. The basis assets contain C/H/O only, and cannot supply an unsupported element's basis.
