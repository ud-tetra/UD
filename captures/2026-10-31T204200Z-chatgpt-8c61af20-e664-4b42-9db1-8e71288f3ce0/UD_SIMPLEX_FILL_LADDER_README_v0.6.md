# UD Point-to-Tetrahedron Filling Ladder v0.6

**Artifact lane:** development; **physical promotion:** 0.

This self-contained research package verifies a mathematics-only simplex filling ladder:

- `UD_SIMPLEX_FILL_LADDER_AND_VOLUME_CLOSURE_AUDIT_v0.6.md`: proofs, assumptions, source strata, caveats, proposed source-dependent UD gate.
- `UD_SIMPLEX_FILL_LADDER_VERIFY_v0.6.py`: exact SymPy test program.
- `UD_SIMPLEX_FILL_LADDER_RESULTS_v0.6.json`: machine-readable test outputs.
- `UD_SIMPLEX_FILL_LADDER_RUN_v0.6.txt`: captured run log.
- `UD_SIMPLEX_FILL_LADDER_MANIFEST_v0.6.json`: file hashes and source provenance.

Reproduce with Python 3.11+ and SymPy:

```bash
python3 UD_SIMPLEX_FILL_LADDER_VERIFY_v0.6.py
```

Scope: exact combinatorial fill counts, homology, cone construction, facet-to-volume relation, regular-simplex incenter factor (d+1)/d, boundary flux, source-typed energy additivity and controls. Does **not** derive native UD spontaneous simplex birth, energy extraction, physical time, Lorentzian signature, or fractal scaling.

The frozen coefficient ledger v0.39 remains unchanged. The equal numbers `4/3` (face-to-volume factor and existing frame coefficient) do not establish operator identity without a typed bridge. Independent peer review and physical correspondence tests are pending.
