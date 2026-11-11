# Unified Dynamics review candidate 0.4

Read `UD_Theory_Narrative_Manuscript_v0.4.pdf` or the editable Markdown. Read `UD_Publication_Readiness_v0.4.md` for remaining submission work. The four companion papers are in `sources/`; their detailed inherited arguments remain part of the review record.

## Replay

Extract the package into a disposable directory. Use Python with SymPy, NumPy and SciPy; recorded constructor versions are in `ENVIRONMENT.json`. Run:

```bash
python3 replay/verify_first_package.py
python3 verify_review_checks.py
```

The script regenerates `replay/results.json` and the exact matrix certificates beside it. It checks skewness, boundary composition, carrier dimensions, boundary-face counts, symbolic spectra, rational LDL norm ceilings, the two-cell augmented separation, interface orthogonality and defect ranks, and 24,576 conditional fixed-gate closure cases. This is deliberate replay, not an instruction to run every imported source script.

Exact matrix and polynomial outputs are distinct from numerical norms, Gaussian evaluations and finite-grid diagnostics. The latter have no interval certificate. The historical `verification_stdout.txt` is retained; `verification_stdout_v0.4.txt` records this candidate's run. All generators, noise laws, preparations and comparison scales remain model assumptions.

`SHA256SUMS.json` inventories the distributed files, excluding itself. Sources were recovered from first-package commit `f274108856caecd2504f28a6729a91ce93846893` and the existing manuscript 0.3. The first-package source register records prior reconciliation against base `4b9c1f7ba03f76324b792f389517161d2bc47e05`.

This candidate has constructor checks, not independent review or submission acceptance. Do not treat a successful replay as physical validation.

The additional review checks assert both expected degree-47 characteristic polynomials, the star collective block and its three-dimensional frequency-2 sector, and covariance transport of a discrimination score. A fresh environment replay remains outstanding.
