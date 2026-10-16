# Full-rank finite-offset stability — FRC v0.1

Development, no registry entry. DERIVED CONDITIONAL mathematics under the unchanged finite UD action. Independent review pending; physical promotion 0.

The seven-page theorem closes the full-rank stability slot left open by FOC v0.1. For every fixed finite r>=2 and a,N>0, the six balanced phase-branch embeddings are nonlinearly orbitally stable on 0<epsilon<=10^-5, where epsilon=kappa/(r*N)-k_star. The twelve and eight saddle embeddings retain their scalar instabilities. The critical endpoint inherits the prior positive quartic theorem.

In the matter-aligned gauge P=0, each unused color has quadratic energy at least

    a||e||^2 + (17/10)||Q||^2 + (N/16)||beta||^2.

The link margin before rounding is 2599*N/40000. The finite-offset magnetic contribution is bounded in absolute value by 3*N/200 times ||beta||^2. Gauss-reduced color squared frequencies exceed a*N/16; unused vacuum cycle squared frequencies exceed 3*a*N/32. Frequency lists are on the linear symplectic slice before the residual global U(r-1) moment-map condition and quotient.

## Reproduction

Use Python 3, NumPy, and python-flint 0.9.0. Run `python3 verify_rank_extension.py` for the 28 exact/192-bit interval checks. This replays the three inherited global solution tubes and proves the rational margins. The prior scalar existence, index and soft-frequency results remain explicit dependencies; its 1,536 child boxes and 2,048 spectral cuts are not new checks here.

With SciPy additionally installed, run `python3 check_matrix_hessian.py` for four deterministic NUMERICAL full-matrix fixtures. Their maximum quadratic-coefficient discrepancy is below 8e-8. These fixtures are synthetic diagnostics, not interval proofs or empirical observations.

The source modules geometry.py and scaled_model.py and the two inherited certificate JSON files are byte-for-byte copies from FOC v0.1. PROVENANCE_v0.1.json records hashes and exact source capture. The prior release is available at https://unified-dynamics-public.ben-w-mayes.chatgpt.site/papers/#finite-offset-v01 .

## Scope

The interval is sufficient, not maximal. Nonlinear stability is local and does not include an explicit displacement/energy radius, attraction or a global basin. No uniform nonlinear neighborhood as epsilon tends to zero or rank tends to infinity is asserted. The final quotient need not be smooth. There is no exhaustive higher-rank equilibrium classification, exact finite-offset color spectrum, experimental analysis or physical correspondence. Next: an explicit nonlinear energy barrier and perturbation radius with parameter dependence.
