# Unified Dynamics v0.88-preview release candidate

**Status** · Draft milestone notes for [CYCLE-088](https://github.com/ud-tetra/UD/issues/592). **Physical Promotion = 0.**

This candidate records the finite-carrier PB3 and PB5 memory relaxation results and the pending spectral-gap series. All ratio claims use the pinned compressed operators and zero exterior damping. The dimensionless parameter $g$ controls the specified radial dissipation operator on each carrier.

## Baseline on main

[PR #593](https://github.com/ud-tetra/UD/pull/593) records the 43-dimensional PB5 carrier, its 12-dimensional undamped subspace, and the nonzero memory-kernel contributions from the stable sector. [PR #594](https://github.com/ud-tetra/UD/pull/594) records the 27-dimensional PB3 carrier, its eight undamped modes, and exponential decay of its projected memory kernel when $g>0$. Its exact squared initial Frobenius norm is $1251/25$. The PB3 result establishes minimality within the tested cyclic bipyramid family.

## Spectral series awaiting independent review

| PR | Pinned head | Result | Constructor evidence |
| --- | --- | --- | --- |
| [#595](https://github.com/ud-tetra/UD/pull/595) | 09e5eff19a5247998d49bedb4b085c13020c871e | At $g=1$, the PB3 and PB5 gaps and active leading memory pole rates are approximately $0.289753482825$ and $0.182555891568$ respectively. | [CI](https://github.com/ud-tetra/UD/actions/runs/44952381002) · [Review](https://github.com/ud-tetra/UD/pull/595#pullrequestreview-6008326332) |
| [#596](https://github.com/ud-tetra/UD/pull/596) | 0d2c773cdad9a14192712283dee52052d73acd9c | As $g\to0^+$, both gaps scale linearly with $g$. Their ratio tends to $5(10-\sqrt5)/57$. | [CI](https://github.com/ud-tetra/UD/actions/runs/44952742601) · [Review](https://github.com/ud-tetra/UD/pull/596#pullrequestreview-6008364748) |
| [#597](https://github.com/ud-tetra/UD/pull/597) | e4e04bcee1aa2614537bee51194084e05e2157ce | As $g\to\infty$, both gaps scale as $1/g$. Their ratio tends to $(5-\sqrt5)/6$. | [CI](https://github.com/ud-tetra/UD/actions/runs/44953184837) · [Review](https://github.com/ud-tetra/UD/pull/597#pullrequestreview-6008394317) |
| [#598](https://github.com/ud-tetra/UD/pull/598) | 934012136369f3b8c005848062fc0fc6c77236bd | The ratio is nonmonotonic. The term $-\sqrt5/(3g^2)$ in its strong-coupling expansion puts it below its limit for sufficiently large $g$, where its derivative is positive. | [CI](https://github.com/ud-tetra/UD/actions/runs/44953501788) · [Review](https://github.com/ud-tetra/UD/pull/598#pullrequestreview-6008462311) |
| [#599](https://github.com/ud-tetra/UD/pull/599) | 882fee8516456ecc25f1edbfa5269f1fc4784c33 | Shifted Routh–Hurwitz tests and root isolation exclude $0<g\le3/2$ from the global minimizer set. | [CI](https://github.com/ud-tetra/UD/actions/runs/44954317792) · [Review](https://github.com/ud-tetra/UD/pull/599#pullrequestreview-6008488272) |
| [#600](https://github.com/ud-tetra/UD/pull/600) | 8d42b6ea7747d96a3e1a4a95cc18d9d30d57a58b | The strong-coupling exclusion $g\ge4$ gives the joint bracket $3/2<g_*<4$. | [CI](https://github.com/ud-tetra/UD/actions/runs/44954716369) · [Review](https://github.com/ud-tetra/UD/pull/600#pullrequestreview-6008556851) |
| [#601](https://github.com/ud-tetra/UD/pull/601) | 06686070506db8a5adca193f01e2653341e2e952 | Interval-certified branch dominance and derivative signs establish exactly one critical point in the bracket. The outer exclusions make it the unique global minimizer. | [CI](https://github.com/ud-tetra/UD/actions/runs/44956165975) · [Review](https://github.com/ud-tetra/UD/pull/601#pullrequestreview-6008588004) |

The critical coupling is enclosed by

$$
\frac{166059063}{52428800}<g_*<\frac{332118127}{104857600}.
$$

These bounds have width $1/104857600$ and locate the minimizer near $3.16732527$. Evaluating the leading root boxes over this enclosure gives $0.410219<R(g_*)<0.410221$. The Padé stationary point near $3.24353$ remains an estimate from the interpolant.

## Scope and release status

The certified decrease and increase adjoining the minimizer cover the compact verification interval $[3/2,4]$. The outer bounds exclude lower values on the rest of the positive axis. They leave all-coupling monotonicity on the two sides, the global supremum, and a universal strict PB3/PB5 gap ordering open. Equality between the gap and the leading observed memory pole rate carries the coupling scope established in the individual proofs.

GitHub records constructor verification for the seven pinned draft heads. Independent approval and integration remain pending. Record an actual independent review against the head examined, and verify the integrated payloads before treating these candidate results as released.
