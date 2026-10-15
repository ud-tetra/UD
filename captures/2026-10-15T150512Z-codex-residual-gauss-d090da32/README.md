# Residual Gauss cone theorem v0.1

Eight-page conditional theorem for the frozen finite unitary Hasse-link action. Read the PDF or TeX for definitions, proofs and the distinction between an exact constraint germ and quadratic dynamics.

## Replay

Dependencies: Python3, SymPy, NumPy, SciPy. Run `python3 verify_residual_reduction.py`. It writes RESIDUAL_EXACT_VERIFICATION_v0.1.json (70 checks) and the separately typed numerical receipt. Frozen graph/color helpers are copied unchanged and hashed in provenance. The verifier does not integrate a new nonlinear trajectory or produce an exact numerical Gauss lift. Its full rank-three preparation solves constraints through second order; remaining error is cubic. The exact local constraint lift is an existence result from the Hamiltonian local normal form.

## Result and limits

Residual moment zero and quotient by U(r-1) are required after the linear reduction. The rank-two color quotient has a 110-real-dimensional open stratum; it is a topological matrix-cone model, not an assertion about the ordinary analytic smooth structure at its vertex. The all-rank principal dimension is26r^2+60r-2. Trace-balanced color data admit one-matrix vacuum completion with a quadratic energy estimate. Oscillator orientation has no assigned physical interpretation.

The general local reduction theorem is imported explicitly from Sjamaar and Lerman, Annals of Mathematics134 (1991),375-422, Theorem5.1 and Remark5.10, doi:10.2307/2944350. The model-specific representation, moment map, completion and counts are derived here. No source paper is redistributed.

The release ZIP contains the proof, replay and prepublication receipts. The immutable repository capture additionally holds site release, validation and complete source-patch receipts. No earlier artifact is overwritten. Development lane; action and registry unchanged; independent review pending; physical promotion0.
