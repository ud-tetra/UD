# Independent review of the finite Chebyshev decoder

PASS for the decoder theorem, its conditional full-space arithmetic bound, and the disclosed small-operator reference checks. The actual weighted600-cell forward/adjoint actions and full problem execution remain HOLD.

The frozen PR307 map, metric, weights and sampling are unchanged. Its rank1999/kernel641, norm at most1 and positive singular lower s=61/27648 are inherited and pinned. The new exact linear decoder has

\[
\|B_{8192}F-P\|<2^{-51},\quad \|B_{8192}\|<512.
\]

Under the declared absolute action and aggregate whole-update arithmetic contracts, the computed output also satisfies

\[
\|\widehat x_{8192}-B_{8192}y\|<11\,2^{-46}<2^{-42}.
\]

These are not measured acquisition or actual floating-estimator claims.

## Polynomial, recurrence and hidden directions

The normalized Chebyshev residual is correct. Its value at zero is1, so the apparent quotient(1-p_N(lambda))/lambda is a polynomial. This gives the correct full-state operator BF-P and avoids the earlier arbitrary-trial-frame right-inverse problem. Exact F-transpose data seeds the nominal observable subspace; polynomial functional calculus preserves it. No explicit observable projector is required by the recurrence.

The recurrence initialization and indices are correct: x0=0, x1=g/c, rho_k=T_k(sigma)/T_{k+1}(sigma), and the momentum/residual update returns B_k y at index k. Exact integer arithmetic independently confirms27587^8192*2^52<27709^8192. There is no floating-logarithm inference in the bias bound.

The quotient polynomial's value at zero is nonzero: N*U_{N-1}(sigma)/(d*T_N(sigma)). Thus a hidden component of a delivered adjoint seed or a computational error can survive and grow. Ideal hidden annihilation is not a license to ignore finite-arithmetic hidden errors.

For an error inserted into iterate j, including j=1 and j=N, the exact response operator is

\[
[T_j(\sigma)/T_N(\sigma)]U_{N-j}(Z).
\]

On the complete A spectrum, Z lies in[-1,sigma], not merely[-1,1]. The hyperbolic bound is

\[
G=(1+s)^2/(2s)=767788681/3373056<256.
\]

This proves the full-space accumulated error bound, including coherent hidden errors. The final-step factor is1; initialization is included. Exact zero x0 is an explicit premise and is enforced by the interface.

## Oracle, arithmetic and memory obligations

The11u local budget correctly counts two delivered-action errors and one aggregate complete-update arithmetic/coefficient error, u=2^-67. It is not a per-primitive rounding assumption. Initialization has defect at most3u, later updates at most11u, and counting8192 terms is conservative.

For normalized data norm at most2, all ideal intermediate iterates have norm at most4/s. Adding the accumulated error keeps the actual iterates below2048. The sufficient factored contract—forward absolute error at most2^-68 on state ball2048 and adjoint absolute error at most2^-68 on data ball2049—therefore closes the normal-action budget at most2^-67. A unit-vector-only absolute guarantee would not suffice.

The executable reference validates entire coordinate expressions against Arb192 coefficient enclosures and current dyadic96-bit states. A complete-coordinate defect below2^-80 yields a vector defect below2^-67 for n at most2640. This includes coefficient generation, cancellation and all rounding. The module correctly distinguishes these arithmetic checks from the mathematical truth of an opaque action callback.

The recurrence uses three iterate vectors, the fixed adjoint seed and current action results, in addition to input/oracle storage. It requires one adjoint seed and8191 normal actions; composition via F and F-transpose entails16383 observation actions. Its working-state bound does not certify the storage, cost or performance of an as-yet-unvalidated actual action backend. No actual600-cell runtime is established.

## Independent exact and reference checks

No producer decoder or reference driver was imported or executed by this reviewer. Independent evidence includes:

| Check | Coverage | Result |
|---|---:|---|
| Exact scalar polynomial/iterate and Green insertion controls | 176 identities on0,a,c,1 | PASS |
| Exact degree8192 decay inequality | Integer powers and hashes | PASS |
| Gain, Green, local/global and domain constants | Rational comparisons | PASS |
| Independent diagonal rank-deficient proxy | Two full8192-step cases | PASS |
| Diagonal-proxy whole-coordinate defects | 49,152 checks | Below2^-80 |
| Disclosed rotated rational proxy, independent regrouped update | Three full8192-step cases | PASS |
| Rotated-proxy whole-coordinate defects | 98,304 checks | Below2^-80 |
| Rotated-proxy normal-action error audit | 24,573 calls | Within declared budget |

The independent rotated replay reconstructs the actual encoded dyadic input, exact adjoint/normal actions and minimum-norm target. Final dyadic states and all recorded seed/action/final error norms and hidden components match the producer evidence exactly. This replay uses an algebraically regrouped Chebyshev update. Coherent hidden injections produce nonzero hidden computed components while remaining within the full-space bound.

The weak-unit-data reference has a minimum-norm state amplitude near453. It validates the generic data-ball2 decoder, not the separate C28 illustrative preparation cap X<=1. Bad callback delivery is rejected by the external exact proxy action audit; the generic module alone does not certify callback truth. Wide arithmetic balls are rejected internally. Small reference executions and exact operator theorems do not constitute actual600-cell action validation.

## Conditional profile and final binding

Substituting the earlier declared C28 input envelope gives a new composed conditional upper of approximately4.907185768843192e-13, below2^-40. This uses the newly derived ideal decoder defect and gain and the conditional implementation bound. Every physical/input premise and actual action implementation remains unsupported/HOLD. The target is observable-chain Euclidean error, not a six-ratio or Hankel-family parameter target. Hidden state components are not reconstructed.

FINAL_BINDING.json pins the final decoder, certificate checker, reference driver and theorem, the inherited source receipts, all scalar consequences and five byte-identical replay files. The reference interface extension adds normalized-data/adjoint dispatch and checks without changing the recurrence or mathematical budgets. Prefinal clarifications count the fixed seed in storage and distinguish the weak proxy's amplitude; no mathematical retraction is required.

This is same-team development review, not blinded validation or external promotion authority. Correct integer/Arb primitives, the stated inherited model facts, stable intended inputs and future absolute action contracts remain assumptions. No all-input/backend guarantee, physical correspondence, acquisition admission or actual floating-estimator conformance is supplied.

Development — no registry entry. Mathematical decoder/reference PASS; actual weighted actions, full execution and input evidence HOLD. External review PENDING. Physical Promotion=0.
