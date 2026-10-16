# Explicit nonlinear perturbation radius and energy barrier — NEB v0.1

Development, no registry entry. DERIVED CONDITIONAL under the unchanged finite UD action. Independent review pending; physical promotion 0.

For any one of the six balanced embeddings, every finite rank r>=1, a,N>0 and 0<epsilon<=10^-5 (epsilon=kappa/(r*N)-k_star), define:

    m=min(a,N*epsilon)/2
    J=max(a,25*N)
    R=3*m/(62*N)
    B=m*R^2/2
    delta=R*sqrt(m/(2*J))

An initial distance <=delta from the chosen gauge/species-phase orbit implies initial energy excess <=B/2 and distance <R for all time. Alternatively distance <R and energy excess <B suffice. For any target 0<eta<=R, use B_eta=m*eta^2/2 and delta_eta=eta*sqrt(m/(2*J)). These are local sufficient guarantees, not maximal basins or attraction claims.

## Metric and energy reference

Use the product of unnormalized Frobenius bi-invariant link metrics, Frobenius Euclidean electric metrics, and real round metrics on the unit matter spheres q=psi/sqrt(N), w=bar(chi)/sqrt(N). Distance is minimized over the compact node gauge and independent species-phase orbit. This is not a componentwise or physically calibrated perturbation budget. Energy is measured relative to the exact equilibrium H_star=2*N*(mu+lambda)+N*(k_star+epsilon)*sum_d(1+cos(phi_d)).

## Reproduction

With Python 3, NumPy and python-flint 0.9.0, run `python3 certify_energy_barrier.py`. Its 211 checks include 19 geometry/margin checks and three checks per each of 64 nested interval cells. It certifies the scalar phase Schur floor C_phase>2*epsilon*I throughout the interval. The manuscript proves the conversion to full orbit-normal quadratic coefficient m and global geodesic derivative bounds J and 62*N.

With SciPy additionally installed, run `python3 check_geodesic_bounds.py`. Six deterministic synthetic fixtures cover ranks 2,3,5 and two offsets. These are NUMERICAL diagnostics, not empirical data or proof over an interval.

For a usable exact budget, run `python3 barrier_budget.py --a 1 --N 1 --epsilon 1/100000`. This uses only the Python standard library and returns exact R, energy barrier and delta^2, plus an integer-certified square-root bracket and a safe rational initial-radius budget. Optional `--target` selects a target <=R.

## Dependencies and limits

Five inherited modules/input/certificate files are copied unchanged; hashes and source captures are in PROVENANCE_v0.1.json. The prior full stationary and full-rank proofs remain explicit dependencies, available through the append-only captures and public packages G12 and G13.

The quadratic radius excludes epsilon=0; that quartically stable endpoint requires a separate quantitative modulus. The interval and radii are sufficient, not sharp. Formulas are uniform over finite ranks in the declared metric; no infinite-rank dynamics is constructed. The residual stabilizer and moment-map condition remain. No physical coupling identification, laboratory tolerance, experimental evidence or registry promotion follows.
