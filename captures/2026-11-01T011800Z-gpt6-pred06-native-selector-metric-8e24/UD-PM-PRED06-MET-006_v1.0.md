# UD-PM-PRED06-MET-006 v1.0 — Uniformly elliptic cochain metrics retain logarithmic stiffness obstruction

**Kind:** THEOREM plus normalization NO-GO. **Status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0.

## Source and mathematical objects

**Dependency:** UD-PM-PRED05-SCALE-002_v1.0, open stacked PR #487, gives for the specific fully excised three-layer Freudenthal complex at even \(N=2m\ge4\) with unweighted real 1-cochain norm
\[
\frac38 H_m\le P_N(I)\le336H_m,\qquad H_m=\sum_{r=1}^{m}\frac1r.
\]
Here \(P_N(I)\) is the minimum squared norm of a closed real 1-cochain with period one around the excised column. This PRED05 source theorem is independently scoped, not an accepted physical relation. Ledger v0.39 Q169 specifies a unit-simplex support metric for the skew Hodge–Dirac generator; G05 leaves master action weighting open, and Q13/O03 have different coefficient types.

For each \(N\), let \(G_N\) be a symmetric positive definite matrix on oriented real 1-cochains such that constants \(0<c\le C<\infty\), independent of \(N\), satisfy \(cI\preceq G_N\preceq CI\) in positive-semidefinite ordering. This is *uniform ellipticity* relative to the unweighted source metric. Define \(\mathcal Z_N=\{a\in C^1(K_N;\mathbb R):d_1 a=0,\oint_\gamma a=1\}\), and \(P_N(G)=\min_{a\in\mathcal Z_N}a^{\mathsf T}G_Na\).

## Theorem: log growth is robust to bounded local metric weights

For every even \(N=2m\ge4\),
\[
\boxed{\frac{3c}{8}H_m\le P_N(G)\le336C H_m.}
\]
If the assumed quadratic sector action is \(S_N(n)=\frac{\kappa_N}{2}n^2P_N(G)\) and \(\kappa_N>0\), then \(\Delta_N=S_N(3)-S_N(2)=\frac52\kappa_NP_N(G)\). A fixed \(\kappa_N=\kappa_0>0\) gives a divergent gap. If a family satisfies \(0<\delta_-\le\Delta_N\le\delta_+<\infty\) for all refinements, then necessarily
\[
\boxed{\frac{\delta_-}{840 C H_m}\le\kappa_N\le\frac{16\delta_+}{15 c H_m},}
\]
so \(\kappa_N=\Theta(1/\log N)\). The same asymptotic bound is sufficient up to positive constants under these metric inequalities.

**Proof.** For every \(a\in\mathcal Z_N\), \(c\|a\|^2\le a^TG_Na\le C\|a\|^2\). Taking minima yields \(P_N(G)\ge cP_N(I)\); evaluating the weighted action on the unweighted minimizer yields \(P_N(G)\le CP_N(I)\). Apply the inherited PRED05 two-sided bounds. Multiplying by \(5\kappa_N/2\), and using \(\delta_-\le\Delta_N\le\delta_+\), yields the displayed coefficient inequalities. Since \(H_m\to\infty\) with \(H_m\sim\log m\), fixed positive \(\kappa_0\) forces divergence. QED.

## Scale-split nonidentifiability (exact)

Even if the entire quadratic action \(\frac{\kappa_N}{2}a^TG_Na\) were known as a function of \(a\), the pair \((\kappa_N,G_N)\) cannot be uniquely separated without an external normalization convention: for every \(t>0\), the replacement
\[
(\kappa_N,G_N)\mapsto(\kappa_N/t,tG_N)
\]
leaves the action **identical on every cochain**. The identifiable quadratic operator is the product \(\kappa_N G_N\), not its two factors. This argument does not assert equivalence of additional dynamics that independently specify the metric or clock. It sharpens the earlier static-action nonidentifiability proof PRED05-IDENT-003.

## Exact witness, limits and remaining native action gate

On an independent triangulated annulus, \(P_I=5/8\). An **illustrative**, face-incidence-count metric with diagonal entries 1 or 2 has \(P_G=3/4\); both preserve the winding topology, but yield different sector amplitudes. This is a legitimate combinatorial metric example, **not** evidence that native UD uniquely selects face-incidence weighting.

A metric whose eigenvalues decay with refinement, e.g. \(G_N=I/H_m\), violates uniform ellipticity and can absorb the scaling with a fixed \(\kappa_N\). A changing defect radius, scale-dependent topological carrier, nonquadratic action, or additional native source/loop terms similarly defines a different branch and does not refute this scoped theorem. No physical SI scale, unique micro-to-cochain metric, or value of \(\kappa_N\) follows from G05 or Q169 in the currently inspected sources. The demonstrated constraint is a necessary conditional refinement law, not an observed renormalization-group equation. Physical promotion 0.
