# UD O09 harmonic admission and triangulation-covariance gate v0.1

**STATUS:** EXACT / CONDITIONAL / NO-GO as specified in `TECHNICAL_NOTE.md`. **Physical promotion: 0.** Scientific source date 2026-10-31.

Two authorized workloads were completed:

1. Harmonic zero-mode action: the topology determines a period-normalized flat U(1) phase on each 24-tetrahedron solid-torus triangulation, but current O09 does not determine its canonical momentum, local link source or normalization. A family of valid *new, unselected* cotangent actions shows this non-identifiability.
2. Triangulation and step: the naive one-edge harmonic-projection transfer gives unequal final phases; directly integrating a nonclosed burden flux also fails homologous-loop independence. An exact geometrically bounded lazy update `M=I-L0/(2 dmax)` is stable and conservative on both, but the same coarse readout differs. Numerical stability does not imply covariant dynamics.

Main figures: squared-norm ratio `358250301381/358493424791`; metric-pump phase difference `-2934811507/1711383481427` in declared dimensionless test convention; stable step `1/18` for both 9-degree graphs; four-sector readout `(2/3,2/9,0,1/9)` versus `(2/3,1/9,0,2/9)`. **These are not measured physical effects.**

Run:

```bash
python exact_models.py
python loop_source_gate.py
python action_extension.py
python independent_numeric.py
```

The four scripts use SymPy and NumPy and write four reproducibility receipts. Full source history and theorem scopes are in `TECHNICAL_NOTE.md`; the `CLAIM_DEPENDENCY_LEDGER.csv` separates exact, candidate, and open work. The PDF is a concise proof supplement. No past artifact is overwritten. The GitHub publication is a separate draft PR with its own append-only manifest/event; local package is the full downloadable release.
