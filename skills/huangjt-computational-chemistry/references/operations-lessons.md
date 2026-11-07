# Verified failure patterns from the 2026 project

Use when the matching failure appears; these are observations, not reasons to add every workaround to every task.

- Gaussian may say `Optimization completed on the basis of negligible forces.` rather than `Optimization completed.`. Parse flexibly, then inspect stationary point, final forces and normal termination. Reuse a completed valid geometry; no-frequency optimization still lacks frequency evidence.
- ReadAtoms must be separated from Gen basis by a blank line (`****\n\natoms=H\n\n`). Test actual produced input, not just template text.
- Compare normalized text for LF/CRLF logical equality; separately hash actual bytes for receipts. Never compare an LF template hash with a CRLF file hash and call the job corrupt.
- RDKit APIs may fail on Unicode filenames on Windows; use Path.read_text + MolFromMolBlock, file-object suppliers and block-based writes. Preserve atom order/explicit H.
- A cached file whose name said "A completed" once contained the original endpoint result. Check the internal label, source project, geometry map, method and SP+thermal=G; retrieve the actual final endpoint when they are inconsistent.
- PBS qstat/qsub may be unavailable while existing compute jobs continue. SSH transport and scheduler server health are separate.
- Unknown qsub acceptance: reconcile before retry. A shared filesystem rejected `flock`; an atomic mkdir protected the reviewed single submission. Do not remove stale locks before checking their ownership/state.
- Windows shell expansion can consume `$d` intended for a remote shell. Prefer properly quoted argument lists, Python remote code and structured results.
- Long CPHF intervals can be normal; logs advanced roughly every 10–20 min in this case. Use queue/CPU/scratch/log evidence rather than declaring a hang from one unchanged tail.
- Cancel local pipeline parent and verified descendants to prevent stage continuation; preserve other processes. Stop a monitor through its automation API, not by deleting quantum jobs.
- Windows-generated scripts piped into `bash -s` fail on BOM/CRLF, surfacing as `bash: -c: line 1: syntax error`, `$'\r': command not found` or `cd: command not found`; strip both remotely (`tr -d '\r' | sed '1s/^\xEF\xBB\xBF//'`) and run `bash -n` before submitting.
- A Torque qsub may accept `-l nodes=1:ppn=1:gpus=1` while the site has no gres; acceptance is not a reservation and the job may share a node. Verify the card inside the job before launching production work.
- `GAUSS_EXEDIR` is a colon-separated list of directories, not a single path: `"${GAUSS_EXEDIR}/g16"` expands to `dir1:dir2/g16` and the job dies instantly with "No such file or directory". Use the absolute g16 path from the site profile, or source `g16.profile` and call `g16`.
- A pipeline Python older than 3.10 has no `Path.write_text(newline=...)`; it raises `TypeError` only at write time, after the expensive part of a patch has run. Use `open(path, "w", encoding="utf-8", newline="\n")`, and run the patch script once against the actual interpreter before trusting it.
- PowerShell 5.1 corrupts UTF-8 text with non-ASCII characters on a read-modify-write round trip: `Get-Content -Raw` decodes as ANSI and `Set-Content -Encoding utf8` adds a BOM, so non-ASCII path literals become mojibake and remote commands fail with "No such file". Use `[IO.File]::ReadAllText(p,[Text.Encoding]::UTF8)` and `[IO.File]::WriteAllText(p,t,New-Object Text.UTF8Encoding($false))`, or edit with Python.
- Cross-platform archive/transfer of non-ASCII filenames is unreliable: bsdtar on Windows mangles them on extract, and scp with such a path can hang. Copy to ASCII names remotely, stream with `tar | base64` over ssh, extract, then rename locally.
- An HTTP 403 with a body like "Just a moment..." is a Cloudflare bot challenge, not an authentication or subscription error. Check first whether the paper or SI is already on local disk (`*.pdf`) and parse it with pypdf; otherwise ask the user for the publisher PDF. Do not attempt to evade the challenge.
- Before claiming a queue is "busy", count free cores per node rather than queue length: a pool of nodes each carrying tens of cores at near-full load cannot place a wide job at all, while other visibly idle nodes may belong to a different group's queue and be unreachable.
- The Gaussian FC-coupling table prints its **diagonal** as a huge constant (order 1e11 for the K and J tables) because it is the magnetogyric-ratio term, not a coupling. A parser that keeps self-pairs reports N(N+1)/2 pairs instead of N(N−1)/2 and a nonsense coupling value. Always drop self-pairs before counting or averaging, and sanity-check the pair count.

Project provenance and exact historical results remain in the research project, not in this portable skill. No task should automatically resume because this file describes it.
