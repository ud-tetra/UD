# Controller coefficient mismatch and complete fixed-word command error v0.1

**DERIVED / CONDITIONAL. Development — no registry entry.** Constructor checks only; physical promotion0. Target acceleration and canonical/mechanical identities are inherited premises from the hash-pinned v104/v106/v110 records. No archived program is executed and no original result is rewritten.

## 1. The implementation gap and the exact command

The v110 plant is driven by the complete sampled acceleration command

\[
u_\theta(\widehat Q,\widehat v,\widehat D,\widehat v_d)
=\alpha_\theta(\widehat Q,\widehat v)+N_\theta(\widehat Q)(-\widehat D\widehat v_d),
\quad N=M^{-1}.
\]

The v110 error `e_C` was an assumed bound on the entire evaluated command. It did not certify either controller coefficients differing from the modeled target or the arithmetic implementing the command. We now supply one explicit fixed-point implementation whose two errors fit that same allowance.

Let theta be the **actual modeled target parameters**, and bar(theta) the exact logical coefficients programmed into the controller. Both lie in the same inherited convex extended parameter box. The old target/reference offset remains covered by the inherited comparison theorem; it is not the new controller/target offset. Both coefficient sets are constant over the admitted history. Estimated D and damping velocity are logical input data satisfying their old bounds. If their calibration depends on coefficient estimates, that dependence must first fit their separate old calibration error; it is not silently absorbed here.

Use the actual source Q radius and velocity radius (w+1), not an origin-centered ambient unit cube. These are conservative boxes enclosing the admitted sampled coordinates. The source e_Q,e_V, common Q/v historical stamp, old damping stamps, causal locally finite holds, actual launch-centered trajectory enclosure and original latency limits remain in force.

## 2. Positive denominator and executable expression graph

The nine canonical acceleration expressions are copied from v106 `plant_map.acceleration`. The inverse mass uses the v104 block

\[
N_2=\mu G^{-1}+2\gamma^2u_c u_c^T,\quad
G=\begin{pmatrix}2&1\\1&2\end{pmatrix},\quad
u_c=\binom{-Q_7-2Q_8}{2Q_7+Q_8}.
\]

Here gamma denotes the source parameter gamma_chi. The vector u_c is distinct from the parameter nu and the acceleration command. The first seven inverse-mass entries are2. All nine damping products and their final additions are included in the graph. No exact current-state inverse mass is assumed.

For robust interval evaluation, rewrite every occurrence of the source denominator as

\[
d=\mu+2\gamma^2\{3Q_7(2Q_7+Q_8)-3Q_8(-Q_7-2Q_8)\}
=\mu+6\gamma^2\{Q_7^2+Q_8^2+(Q_7+Q_8)^2\}\ge\mu_{\min}>0.
\]

The rewrite and all four entries of N_2 times its supplied inverse are checked with exact sparse rational-function arithmetic. It changes no law or coefficient. The complete arithmetic graph has670 unique nodes and59 rewritten denominator occurrences. AST parsing admits only integer literals, named inputs, unary signs and finite arithmetic; imported Python programs are not evaluated.

## 3. Coefficient mismatch theorem

For each output i and parameter j, bound the partial derivative of the **whole command** throughout the logical input/parameter box by L_ij. Exact interval automatic differentiation uses the product and quotient rules, with the positive denominator floors. Bounds are rounded upward to dyadic rationals for tractability. Therefore

\[
\|u_{\bar\theta}-u_\theta\|_\infty
\le\max_i\sum_j L_{ij}|\bar\theta_j-\theta_j|.
\]

This is the line-segment mean-value bound, since the parameter box is convex. Write L=max_i sum_j L_ij and impose the sufficient common component bound rho with L*rho<=e_C/2. This uniform bound is in the declared native parameter coordinates, not a dimensionless relative calibration claim. The logical coefficient mismatch is measured before encoding; coefficient and other input quantization are charged separately to the word-error allowance in Section4. Boundary membership is an additional condition: a small error does not license leaving the box. D's row norm remains bounded by kappa+e_D,d; entrywise intervals used in the proof may be larger than that row-norm class, which makes the bound conservative.

## 4. Complete fixed-point arithmetic theorem

Use signed integers n representing n*2^(-p). Input conversion, multiplication and division use exact integer arithmetic followed by nearest rounding with ties to even; addition/subtraction and sign change are exact on the grid. Power2 is one rounded multiplication. Integer literal loading is exact. The certificate pessimistically allows delta=2^(-p-1) even at exact operations and loads.

At every node certify an exact-value magnitude B and an absolute error E<=K*delta. Input/constant nodes use K=1. With all child errors<=1, valid recurrences are

\[
K_{a\pm b}\ge K_a+K_b+1,\qquad
K_{a^2}\ge(2B_a+1)K_a+1,
\]

\[
K_{ab}\ge B_aK_b+B_bK_a+\min(K_a,K_b)+1.
\]

For division with exact |b|>=d0 and K_b*delta<=d0/2,

\[
K_{a/b}\ge 2K_a/d0+2B_aK_b/d0^2+1.
\]

Proof: subtract exact and perturbed products or quotients. The product cross error is at most min(E_a,E_b) under the unit-error bootstrap. The quotient denominator is separated from zero by d0/2. Add at most delta rounding at the operation. Upward dyadic rounding preserves every inequality. **Every node** must satisfy K*delta<=1, and every denominator must satisfy its additional separation test. Thus the induction does not assume a final error bound before proving it.

Choose p so every condition holds and max_output K*delta<=e_C/2. Choose integer magnitude bits I with 2^I>max_node B+1, and stored signed width W=1+I+p. The error bootstrap then bounds every stored value strictly within range. Signed2W+2 temporary bits cover full products and scaled division numerators. Overflow and a zero rounded denominator are refused; saturation/wraparound are not members of this implementation class. The Python reference uses unbounded integers to implement these explicitly bounded operations and checks the bounds; it is a finite-word semantic reference, not a processor or HDL timing certificate.

Combining with Section3 gives

\[
\boxed{\|u_{\rm word}-u_\theta\|_\infty\le L\rho+K_{\rm out}\delta\le e_C.}
\]

Loading Q,v,D and damping velocity, evaluating acceleration, forming every damping dot product, applying inverse mass and summing the command are all charged. No part of this complete arithmetic error is assigned the much looser damping-only tolerance.

## 5. Sufficient layouts under unchanged v110 budgets

Both original damping classes produce these same sufficient layouts; their distinct source inputs remain separately checked. Widths are sufficient for this expression graph and majorant scheme, not optimal requirements.

|Domain|Controller/target component error rho|Off arm p / W|On arm p / W|Largest temporary width|
|---|---:|---:|---:|---:|
|1|2^-249|222 /240|256 /298|598|
|2|2^-227|208 /221|234 /268|538|
|3|2^-231|219 /233|239 /265|532|

The inherited full-command caps are respectively2^-174,2^-165,2^-180. None is enlarged. The preceding precision in each layout fails at least one sufficient arithmetic test. A 32-fractional/64-stored-bit version fails the certificate; this is not evidence that every binary64 implementation or every physical controller fails. IEEE floating-point, alternative evaluation orders, fused operations, lower-precision approximations and sharper bounds require separate versions/proofs.

## 6. Transport into the existing comparison and energy accounting

Replace the former assumed e_C by the derived combined bound above. The old canonical force contribution is still at most beta*e_C; therefore the **same** v110 K0/K1 force envelope, reconstruction, plant-error, external-force and first-exit/comparison inequalities remain sufficient. This is monotone substitution into an inherited theorem, not a new execution of the entire predecessor chain.

All source timing assumptions remain load-bearing. Q and v must correspond to the same historical stamp. Total age at actuation includes sensor transport, arithmetic, scheduling and hold delay and must remain below the original h. The new reference program has not been certified to finish on a device within that h. A fresh numeric word design does not establish real-time feasibility. The old separate damping timestamps and readout timing are not replaced by the command stamp.

The existing external canonical-force reserve b/4 and plant acceleration allowance are unchanged. Physical units remain position ell_*, velocity ell_*/tau_*, acceleration ell_*/tau_*^2 and force E_*/ell_*. No SI scales are chosen. Target virtual Hamiltonian tracking or its controlled dissipation is not actual controller/actuator supply work or total apparatus storage; the physical work ledger remains a separate required return under APP02/APP01.

## 7. Verification and limits

309 exact constructor checks plus60 deterministic rational command witnesses pass. Every one of670 graph nodes is compared to its own rounding enclosure at each witness. Complete word-to-actual-model command error fits the old cap. Controls reject excessive coefficient mismatch, nonpositive/out-of-box mass, excessive logical damping row norm, asynchronous Q/v, stale actuation, enlarged latency reserve, insufficient precision and actual word overflow. The source acceleration formula's prior canonical correctness is an inherited pinned premise, not independently reproved here. Witnesses complement the analytic induction; they do not replace a uniform proof.

APP04 has a bounded fixed-point mathematical return ready for review. Actual numeric-backend choice, independent review, component calibration, computation latency and physical bridge qualification remain open. The source ledger and governance proposal are unchanged. Missing Gap2_FINAL_Finite_Genesis.png is unused. No CRL/registry or physical promotion is made.
