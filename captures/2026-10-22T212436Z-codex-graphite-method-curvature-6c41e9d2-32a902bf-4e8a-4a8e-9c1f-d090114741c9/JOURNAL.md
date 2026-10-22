# Graphite curvature calculation journal

- 2026-10-22: Adopted user-supplied UD mathematical analysis protocol v1.0 as a runtime method, without changing theory or physical status. Source method copied into capture. Its relative `../templates/mathematical_receipt.json` was not available in the supplied material or repository, so `MATHEMATICAL_RECEIPT.json` records the requested fields in a local schema.
- Defined exact seven-cell carrier, unit metric, physical lateral displacement, Fourier amplitude and compressive load in BOOT REPORT. Clock, modular and factorization methods marked N/A.
- Derived sign-dependent Hessians, the normalized harmonic-port factor 4/7, fixed-height curvature/barrier ratios, and exact branchwise relaxed-load derivative. Both material sign branches retained.
- A SymPy check could not run because neither Python interpreter included the package. Replaced it with stdlib Fraction exact checks, which passed. This is constructor verification only.
- Preserved the preceding global-range versus saddle-barrier correction (PR #418); current v3 manuscript supersedes v2 only as the focused draft. No empirical friction fit or independent review.

See `MATHEMATICAL_RECEIPT.json`, `GRAPHITE_METHOD_BOOT_AND_CURVATURE.md`, `verify_curvature_port.py`, and manuscript v3.
