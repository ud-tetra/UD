# Tetrahedral Native Coordinate Atlas — v0.7 Development Capture

**Finding:** Four nonnegative barycentric vertex weights summing to one represent precisely three independent spatial coordinates; their support sizes encode the point → line → triangle → filled-tetrahedron strata. For the regular unit-circumradius tetrahedron, the metric identity is `ds²=(4/3)Σ(dλ_i)²` under `Σdλ_i=0`. Adjacent nonregular tetrahedra glue through compatible face coordinates, and correctly transformed cell-energy integrals are additive.

**No-go:** Regular equilateral tetrahedra cannot alone face-to-face tile flat Euclidean three-space; the atlas must permit nonregular tetrahedra or derived curvature. The constrained fourth barycentric weight is not physical time and is not the unconstrained channel singlet of v0.5.

**Exact checks:** Run `python UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_VERIFY_v0.7.py` with SymPy installed; expect `EXACT_CHECKS_PASS=121` and an exact JSON results file.

**Claim boundary:** Source-derived Ω0 cell filling, native metric, physical clock and physical energy conservation remain OPEN. No canonical UD coefficient is replaced. Physical promotion = 0. This is a constructor-verified development artifact awaiting non-constructor review.

**Dependencies:** Ledger v0.39 (F01–F05, P01–P09, G05, Q153–Q179); tetrahedral 3+1 and conservative energy audit v0.5; point-to-tetrahedron fill-ladder audit v0.6. These previous artifacts are not overwritten.
