# Portable post-processing, no quantum backend

Requires Python3 standard library only. Run only when file processing is requested; knowledge mode can explain the schemas without executing. CLI uses a new output directory and refuses overwrite, never contacts cluster or xTB.

Raw CSV columns: `conformer,H_a,H_b,FC_raw_Hz`; unordered integer H pair IDs are one-based; exactly one row per pair per conformer. All conformers must contain the same pair set for that method. A separate raw CSV per method is required.

DU4 map CSV columns: `H_a,H_b,carbon_atom,environment,extrapolative`. Environment one of sp3_general, sp3_alpha_pi, small_ring, sp2. `extrapolative` is true or false and is preserved; validate molecular CH2 connectivity before invoking. Classification is explicit, not inferred by the script. Only mappedCH2 pairs are exported forDU4.

Optional weights JSON: `{"c0003":0.8619687299811625,"c0005":0.13803127001883744}` (example only). IDs must equal input IDs and weights must sum to1, be nonnegative and finite. The CLI does not select or renormalize weights implicitly. Omit weights for per-conformer outputs only. Preserve ensemble coverage separately.

```text
python scripts/coupling_postprocess.py --method bally --raw raw-bally.csv --out new-bally-results
python scripts/coupling_postprocess.py --method du4 --raw raw-du4.csv --map reviewed-ch2.csv --weights selected-weights.json --out new-du4-results
```

Outputs `per-conformer.csv`, optional `weighted.csv`, `provenance.json`. Method-specific column names prevent accidental merging; signedJ is primary, absoluteJ is separate. This tool does not establish that Gaussian used the published basis/geometry: validate logs, input hashes, atom maps and basis conventions first. Basis assets and metadata alone are not scientific validation of an arbitrary new molecule.
