# Replay source staging

Call the frozen `replay_all.py` entrypoint for full raw/projection, saved-factor
and five exact logical-control verification. It invokes no estimator, SVD or
auxiliary alignment proposer. Imports define those functions but never call
them. Exact saved-output proof uses the existing frozen coefficients.

The producer directory must be staged as
`STAGE/directional-admission-work-20261019`, preserving its files and bytes.
All relative `source_files` in its PROTOCOL_FREEZE.json resolve from STAGE.
Stage the two old U0 archives and external baseline exactly as the five-row
PR237 COUNTEREXAMPLE_SOURCE_INDEX.json specifies. Its reverse-anchor SVD/RUN
files may also be staged but are unused by this directional script. In addition
stage the following FOUR SMALL files from PR237's captured counterexample
subtree into `STAGE/strict-family-review-20261019/`:

- PROTOCOL_FREEZE.json
- SPATIAL_SELECTION.json
- COUNTEREXAMPLE_RESULT.json
- estimator.py

Their exact SHA values are already in this producer's PROTOCOL_FREEZE.json
source_files. No old15MB estimator factors need duplication. The current
directional saved factors may be hardlinked read-only when staging; control
mutations first unlink their isolated destination. Never modify a shared inode.

The caller provides the original150,321,232-byte synthetic nominal baseline
with SHA25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59.
It is not an instrument recording and is not replaced by invented bytes. It
must also be accessible under the frozen relative baseline source path, e.g.
through a stage-local symlink to that verified external file.

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python STAGE/directional-admission-work-20261019/replay_all.py --baseline /absolute/path/to/pinned-baseline.i64le --out /absolute/path/to/new-replay-output
```

All four complete records are reconstructed in anonymous RAM files and checked
against their prefit hashes, vector norms and exact integer projection hashes.
No persistent raw files or full Hankel matrix are written. The full exact
saved-factor table must match the original certificate with no tolerance. One
post-known-outcome alignment hash corruption must reject; the five fixed
logical controls must exactly match their original receipt.

`--controls-only` runs only the five small logical controls and explicitly emits
a controls-only status; it is not a full replay. Source constants and finite
counterexample outcomes were known before this wrapper freeze. All physical
verdicts and external-review status remain unchanged.
