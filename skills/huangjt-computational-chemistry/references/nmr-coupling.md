# NMR and two distinct J protocols

Use in knowledge, local or cluster mode; this page alone does not launch a backend.

## Chemical shifts

The verified low-cost local branch used gas B3LYP/6-31G(d) optimization without frequency, then GIAO B3LYP/6-31G(d), SMD chloroform, G09Defaults. Historical project conversion: δH=(32.2109−σ)/1.0157 and δC=(188.4418−σ)/0.9449. Reuse only after checking original calibration applicability including geometry, shielding convention, solvent and nucleus. These coefficients are not universal defaults or a validated calibration for arbitrary molecules.

The separate cluster branch used IEFPCM chloroform/G09Defaults: 01 B3LYP/6-31G(d), 02 mPW1PW91/6-311+G(d,p), 03 wB97XD/6-31G(d). 01/02 used each method's own configured TMS σTMS−σ reference; this is not the above SMD fit. Without a matched03 reference/scaling, retain σ and mark δ missing. Never silently copy coefficients across methods or solvents. Preserve coefficient source/version with the result; verify literature if choosing a new protocol.

## General H–H: Bally–Rablen

DOI: https://doi.org/10.1021/jo200513q (2011). This installed variant is the hydrogen-only u+1s prescription: gas B3LYP/6-31G(d) geometry; B3LYP/Gen FCOnly, 6D, ReadAtoms, Int=NoBasisTransform, G09Defaults, with verified input flags SCF=XQC/NoSymm in this project. C/O6-31G(d,p); H four uncontracted valence-s exponents + tight s + p. Exact basis block: `assets/basis/Bally-H-uplus1s.gbs`.

**J=0.9155×FC**, signed, no intercept. Do not substitute0.9117 belonging to a different whole-basis/IOp implementation. Export all H–H pairs if requested, with bond distance to distinguish geminal/vicinal/long-range. This is FC empirical prediction, not the full Ramsey sum.

## CH2 geminal ²JHH: DU4

DOI: https://doi.org/10.1021/jo501781b (2014), author SI S4 checked in the source project. Exact basis block: `assets/basis/DU4-CHO.gbs`: C4-31G, O6-31G, H8s1p. Use the prescribed gas B3LYP/6-31G(d) geometry and verified B3LYP FC settings. This skill's implementation covers C/H/O and geminal CH2; other elements or other couplings require method review.

|CH2 environment code|Signed formula / Hz|
|---|---|
|sp3_general|1.240 FC +0.57|
|sp3_alpha_pi|1.072 FC −1.66|
|small_ring|1.249 FC +1.05|
|sp2|1.337 FC +0.52|

CH2–O is not CH2–Cπ merely because the O is conjugated. Ring and π-adjacency need graph/chemical review; a CH2 with two adjacentπcenters is explicitly extrapolative in this project, not a validated new fit class. Do not apply this geminal routing to ¹JCH or general vicinal³JHH. Record classification and source mapping per pair.

## Input and result gates

- Actual basis must end `****\n\natoms=H\n\n`; the blank line before ReadAtoms is essential.
- C27H34O7 example had782 Bally /680 DU4 basis functions; these totals are molecule-specific, not universal. Compare to the expected count from the actual deck.
- Normal termination, intended method/basis, all H indices and exact pair counts, raw FC matrix, finite values and original file hashes. For34H expect34×33/2=561 unordered pairs. SomeReadAtoms inputs request a subset: declare the subset instead of assuming full matrices.
- Identify each CH2 carbon and both explicit attached H from the molecular graph; Gaussian one-based IDs, same atom map as geometry and shift table. Do not carry atom-number assignments between different molecules.
- Separate CSVs for raw/marked/weighted Bally and DU4, preserve signed values. For each method `J_weighted=Σ wi J_i` with explicit selected IDs and normalized weights. Never average methods or silently insert missing conformers. Keep source ensemble coverage, gas/solution weighting conditions and extrapolation flags.
- Single-conformer tables contain no invented weights; keep separate filenames from final ensemble tables. Gas FC fits do not explicitly model CDCl3/MeCN effects.

## Assets and cheap processing

Use `scripts/coupling_postprocess.py` with explicit method selection and CSV schema in postprocess-cli.md. It performs no quantum calculation, no chemical environment inference and no source fitting. It rejects missing pairs/weights, duplicated unordered pairs, ambiguous environment codes and nonfinite numbers. Outputs raw+scaled and optionally weighted tables. The basis assets contain C/H/O only, and cannot supply an unsupported element's basis.
