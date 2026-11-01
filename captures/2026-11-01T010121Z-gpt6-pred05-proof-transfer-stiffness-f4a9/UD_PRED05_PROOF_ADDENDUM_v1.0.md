# UD PRED05 — Proof-first local dynamics and stiffness addendum v1.0

**Status:** VERIFIED_SCOPED / EXACT_CONDITIONAL mathematical results; external review deferred; physical promotion 0.

## Mathematics closed under new assumptions

- **Local source evolution:** Given a seeded token and local directed +z port on a Freudenthal tetrahedral ball, *transfer before star excision* is always enabled along the next untouched slab. The token-plus-boundary-reservoir stock is exactly conserved. Full column excision yields first integral homology Z. This establishes a local computation without an externally supplied precomputed trail, **not** an endogenous selector.
- **Topological persistence restriction:** fixed geometry or PL-homeomorphism-preserving post-event moves retain first homology. A *new radial cut* can kill the winding while leaving all original trail marks intact; bare memory veto cannot establish dynamical stability.
- **Rigorous norm growth:** for 3-layer cut grids and unweighted edge counting metric, if h_N is the unit-period harmonic representative and m=N/2, then
  `3/8 H_m <= ||h_N||^2 <= 336 H_m`, where `H_m=sum_{r=1}^m 1/r`.
- **Action gap:** the assumed n=2->3 quadratic retained gap is `Delta_N=(5/2) lambda_N ||h_N||^2`. A constant positive lambda_N causes the gap (and positive injected work under the one-pass bound) to diverge at least logarithmically. A uniformly positive bounded gap forces `lambda_N = Theta(1/log N)`; the prior `lambda_N||h_N||^2=2/5` was an inverse calibration, not a derivation.
- **No coefficient identification from statics:** multiplying the quadratic model action by any positive scalar preserves homology and equilibrium minimizers but changes all action gaps. Without a separately normalized action/source or measured clock, geometry cannot determine lambda_N.

## Required source rule

Recover a native burden/parity seed and oriented port, a lawful supported-cell-removal and recovery generator, and a micro-to-cochain action coefficient map. Determine the appropriate edge metric and renormalization, with independent physical units before claiming energy or time. These dependencies remain OPEN_GATED.

## New proof IDs

`UD-PM-PRED05-EVOL-001`, `UD-PM-PRED05-SCALE-002`, `UD-PM-PRED05-IDENT-003`, `UD-PM-PRED05-PERSIST-004` (all v1.0, source-bound conditional, review deferred, physical promotion 0).
