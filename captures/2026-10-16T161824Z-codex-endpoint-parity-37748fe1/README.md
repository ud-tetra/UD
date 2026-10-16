# Parity-sharpened endpoint trapping — PET v0.1

Development, no registry entry. DERIVED CONDITIONAL under the unchanged frozen action. Independent review pending; physical promotion 0.

An exact energy-preserving isometric reflection reverses all three critical kernel directions and fixes their leading fast-relaxation correction. Three intrinsic jet cancellations permit sixth-order remainder control. The same energy coercivity H-H_star >= (N/1600)d_g^4 now holds on a sufficient radius at least 50,000 times the earlier EQT radius, for every a,N>0 and each finite rank at epsilon=0.

Define alpha=min(a/2,N/100), D=279N/(4alpha), J=max(a,25N), C3=279N, C4=1600N, C5=10000N, and

    S6 = 9*C3^2*D^2/(2*alpha) + C3*D^3/6 + C4^2/(18*alpha)
         + 5*C4*D^2 + 2*C5*D/15 + 8*C5^2/(9*alpha) + 264*N.
    R_p = min(alpha/(500000*N), sqrt(N/(400*S6))).

For every target eta<=R_p, B_eta=N eta^4/1600 is a boundary barrier and delta_eta=eta^2 sqrt(N/(1600J)) is a sufficient initial radius. Initial distance below eta with energy excess below B_eta also suffices. The full fixed-norm manifold is covered; its invariant zero-Gauss subset inherits trapping. The residual stabilizer is retained.

At a=N=1, the calculator returns the exact rational radius 1/829538022 <= R_p, approximately 1.20549e-9, a gain of 51,078.3 over EQT. At this target B≈1.31988e-39 and delta≈7.26603e-21. These are conservative mathematical bounds in the same unnormalized Frobenius/unit-matter-sphere metric, not physical tolerances or actual basin estimates.

## Replay

- Python 3 + SymPy: `python3 certify_parity.py` checks 22 exact conditions, including positive-coefficient comparison polynomials for the complete parameter range, plus four exact rational budget examples. The generic tensor estimates and exact reflection are proved analytically in the seven-page manuscript.
- Standard-library calculator: `python3 parity_budget.py --a 1 --N 1`. Optional `--eta` is an exact rational target within the returned inward-rounded rational radius. Exact barrier, initial-radius square and rational square-root brackets are included. Decimal fields are diagnostics.
- NumPy + SciPy + python-flint 0.9.0: `python3 check_parity_matrices.py` checks four NUMERICAL synthetic full-matrix states, at ranks 1,2,3,5. No empirical samples or Gauss-projected trajectories are used.

The frozen EQT certificate and geometry helper are copied unchanged and hash-bound. Their Arb matrix bounds, kernel identity, scalar quartic and higher-rank identities remain conditional dependencies; this extension does not count them as new independent review. The artifact is an additive improvement to the sufficient endpoint radius; the earlier theorem remains valid and unchanged.

## Remaining obligations

No sharp basin, attraction, infinite-rank flow, endpoint forcing/model-error budget or laboratory realization is established. Further improvement may come from actual directional tensor coefficients on the fast-relaxation graph. Experiment-facing requirements still need calibrated state, energy, clock and detector maps. The coefficient ledger and action are unchanged. No physical coupling unification, proton decay or monopole/neutrino signal is claimed.
