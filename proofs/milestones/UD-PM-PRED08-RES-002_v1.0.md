# UD-PM-PRED08-RES-002 v1.0 — Energy-accounted, symmetry-equivariant stochastic seed and finite-stock active redistribution

**Kind:** THEOREM / conditional constructive branch. **Proof status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## Premises and sourced input

The **only** source-bound transport contribution is Q162's K4 all-open diffusion `-L b/4`, where `L=4I-J`. Q153 does not specify a predictive nonconservative source; PRED07-BUR-001 introduced the candidate conservative nonlinear redistribution `s_i=gamma*b_i*(b_i-Q/M)`. PRED06-SEL-001 forbids deterministic unique selection at a fully `S4`-invariant state.

**New assumptions (not derived from UD):** `b_i>=0`, `M=sum_i b_i>0`; Euclidean **burden-contrast measure** `V=(1/2)sum_i(b_i-M/4)^2` (not identified with Q165 support energy); nonnegative finite abstract action reserve `R`; cumulative dissipative stock `D>=0`; candidate gain `gamma>0`; reserve scale `R_*>0`; and the declared availability factor `u(R)=R/(R+R_*)` with `u(0)=0`. The model clock and all action units remain uncalibrated.

Between stochastic initialization events declare

\[
\begin{aligned}
\dot b_i&=\frac M4-b_i+u(R)\gamma b_i\left(b_i-\frac QM\right),\quad Q=\sum_i b_i^2,\\
\dot R&=-u(R)\gamma A(b),\quad A(b)=\sum_i b_i^3-\frac{Q^2}{M},\\
\dot D&=\frac14\|B_1^Tb\|^2,\qquad \dot M=0.
\end{aligned}
\]

`R` and `D` are new **normalized quadratic-burden stock accounts**, not joules or the source's historical physical reservoir. The nonlinear term is an additional **conservative redistribution current** because its sum is zero on the mass shell. It is NOT the source law uniquely recovered from Q153.

## Theorem — exact ledger, positivity and conditional instability

1. For nonnegative `b` and `M>0`, `A(b)>=0`; equality holds when all positive `b_i` are equal. Mass `M` and the total normalized ledger `E=V+R+D` are conserved. Nonnegative `b,R,D` remain nonnegative and solutions exist for all nonnegative model times.
2. The evolution is `S4` equivariant. Exactly uniform `b` remains uniform even with sufficient gain; it does **not** deterministically choose a vertex.
3. On the zero-sum tangent subspace at uniform `b=(M/4)*1`, with initial reserve `R_0`, the three contrast eigenvalues are
   `sigma=-1+gamma*M*u(R_0)/4`.
   The uniform state is **linearly unstable** when `gamma*M*u(R_0)>4` and linearly stable to contrast when `<4`. At equality linearization is inconclusive. This is a stability statement on the chosen enlarged dynamical system, not a physical growth prediction.
4. Every strict burden ordering survives at every finite time because
   `(b_i-b_j)'=(b_i-b_j)*[-1+u(R)*gamma*(b_i+b_j-Q/M)]`.

## Proof

Use Cauchy–Schwarz in the form
`(sum b_i^2)^2=(sum b_i^(3/2)*b_i^(1/2))^2 <= (sum b_i^3)*(sum b_i)=M sum b_i^3`;
thus `A>=0`. Both diffusion and the nonlinear redistribution sum to zero. At `b_i=0`, the nonlinear term vanishes while diffusion contributes `M/4>0`; hence the positive simplex is forward invariant. Since `u(0)=0`, the boundary `R=0` is also invariant. `D'` is nonnegative. Direct differentiation gives

\[
\dot V=-\frac14\|B_1^Tb\|^2+u(R)\gamma A(b),
\]

hence `(V+R+D)'=0`. Since the positive simplex with fixed `M` and the resource registers bounded by `E` are compact and the vector field is locally Lipschitz for `R>=0`, the solution extends for all model time. This proves item 1. Every expression is permutation invariant/equivariant, proving item 2. At the uniform state the derivative of `Q/M` in zero-sum directions vanishes and the added source linearizes as `gamma*M/4` times the contrast; multiplying by `u(R_0)` and combining with Q162's `-1` eigenvalue proves item 3. Factor the difference between any two equations to obtain item 4. QED.

## Random initial symmetry-breaking event with an exact cost

**Additional stochastic jump assumption:** Start from exactly uniform `b_i=M/4` and a finite initial `R^- >= epsilon^2`, where `0<epsilon<M/4`. Choose one of the 12 ordered vertex pairs `(u,v)` **uniformly at random**; transfer `epsilon` burden from `v` to `u`:
`b^+=b^-+epsilon*(e_u-e_v)`, `R^+=R^--epsilon^2`, and `D^+=D^-`.

Then `M` remains constant, all `b_i` stay nonnegative, and `V^+-V^-=epsilon^2`; therefore `E=V+R+D` is conserved across the jump. The chosen `u` becomes the unique maximum and `v` the unique minimum, so the conditional outward Q162 current from `u` to `v` is `epsilon/2`, greater than the two other outgoing currents `epsilon/4`. The distribution of this event is exactly `S4` invariant: it picks no preferred vertex **in law**, though each realized event breaks symmetry. This event is a **new seeded noise source and action budget**, not a native prediction of stochasticity, spontaneous birth, hardware noise or physically measured energy.

The comparator can output `(u,v)` when allowed by the still-unsourced native gate law; this does not imply legal cell excision or stable winding. Because a finite reserve will be depleted, a linearly unstable contrast need not persist (see PRED08-ASYM-003).

## Limits / reopening gates

Without `gamma`, `R_*`, a seeding jump, or nonuniform initial data, Q162 alone cannot generate the effect. The counterfactual `R=0` forces `u=0`, restoring passive mixing. Exact uniform data with *deterministic* equivariant evolution remain uniform. A microscopic identification of the reserve, noise statistics, nonlinear current, measurement, clock, and topology-changing cell rule is OPEN_GATED. **Physical promotion: 0.**
