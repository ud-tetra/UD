# Explicit quartic trapping at the critical endpoint — EQT v0.1

Development, no registry entry. DERIVED CONDITIONAL under the unchanged UD action. Independent review pending; physical promotion 0.

For epsilon=kappa/(rN)-k_star=0, a,N>0 and any finite rank, the original critical gauge/species-phase orbit satisfies

    H-H_star >= (N/1600) d_g^4, for d_g <= R_star.

Set alpha=min(a/2,N/100), D=279N/(4alpha),
E=N(2177D^2+800D/3+19/6)+1280000N^2/(9alpha), and
R_star=min(alpha/(10000N),N/(400E)). For every target 0<eta<=R_star, the boundary energy is B_eta=N eta^4/1600 and the sufficient initial radius is delta_eta=eta^2 sqrt(N/(1600J)), J=max(a,25N). Initial data in that ball have at most half the barrier energy and remain within eta for all real time. Distance<eta and energy excess<B_eta also suffice. The full fixed-norm manifold is covered, so its invariant zero-Gauss subset inherits the result.

At a=N=1, R_star=9/381342574261400≈2.36008e-14, B_R≈1.93905e-58 and delta_R≈2.78500e-30. These are conservative sufficient bounds in the declared mathematical normalization, not experimental tolerances or estimates of the actual basin size.

## Proof and replay

The eight-page manuscript gives the full analytic argument. Two new Arb congruences prove a scalar fast-Hessian floor of 1/50 and critical-map squared norm below 50. The frozen directed-integer critical quartic certificate is replayed (11<A4<12,12<B4<13). Intrinsic normal-coordinate quartic relaxation, global fourth/fifth geodesic derivative bounds and explicit error absorption give the result. No unspecified slice-chart radius is assumed. General-parameter absorption is proved analytically; four exact budget examples are supplementary checks.

- Python 3 + NumPy, SymPy, python-flint 0.9.0: `python3 certify_endpoint.py` writes ENDPOINT_QUARTIC_CERTIFICATE_v0.1.json.
- Standard-library calculator: `python3 endpoint_budget.py --a 1 --N 1`. Optional `--eta` is an exact positive rational target no greater than R_star. The initial-radius square and a rational square-root enclosure are returned exactly; decimal fields are diagnostics.
- ENDPOINT_REQUIREMENTS_v0.1.json states the mathematical preparation contract and physical translation gates.
- PROVENANCE_v0.1.json records five unchanged copied inputs and attached governance/ledger hashes. The exact kernel and higher-rank block identities remain frozen conditional dependencies, not new independent review.

The declared metric uses unnormalized Frobenius links/electric fields and unit matter spheres after dividing both species by sqrt(N). The residual stabilizer constraint is retained. All finite ranks share these constants; no infinite-rank phase space is constructed. No simulation or experimental data enter this proof. No sharp basin, attraction, endpoint model-error budget or physical realization is established.

This closes the quantitative quartic-endpoint modulus slot in G14/G15, preserving those results and their positive-offset scope. A useful next mathematical step is sharper local remainder control on the fast-relaxation graph. Experimental requirements require a sourced realization and calibrated detector/state/energy/clock maps. The coefficient ledger and action are unchanged.
