# UD-PM-PRED08-ASYM-003 v1.0 — Finite reserve cannot sustain permanent K4 burden contrast

**Kind:** NO-GO / exact asymptotic dynamical theorem. **Proof status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## Theorem and typed assumptions

Assume exactly the autonomous continuous-time finite-stock K4 model of PRED08-RES-002: nonnegative burden `b` with constant `M>0`, all Q162 contacts open, candidate active redistribution, nonnegative reserve `R` and dissipated stock `D`, and `E=V+R+D<infinity` conserved. The declared Euclidean burden contrast is `V=(1/2)||b-(M/4)*1||^2`.

Then **every** global trajectory satisfies

\[
\int_0^\infty V(t)\,dt\le \frac{E(0)}{2},\qquad
\lim_{t\to\infty}V(t)=0.
\]

For every contrast threshold `delta>0`, the total amount of **model time** spent in the set `{t: max_i b_i(t)-min_j b_j(t) >= delta}` is bounded by `2 E(0)/delta^2`. Thus this closed finite-reserve system cannot maintain a strictly nonzero burden-separation threshold forever. No physical-time interpretation is established.

## Proof

On the complete four-vertex K4, `L=4I-J` and
`D'=1/4*b^T L b=sum_i(b_i-M/4)^2=2V`.
The resource ledger is conserved and `V,R,D>=0`, so `D(t)<=E(0)` and
`2 int_0^T V(t)dt=D(T)-D(0)<=E(0)` for every `T`; taking `T` to infinity proves the integral bound.

The b/R/D trajectory is confined to a compact invariant subset (`b>=0`, sum b=M, R>=0, V+R+D=E(0)`). Its vector field is smooth/Lipschitz on this set (since `R_*>0`), hence `V'` is uniformly bounded, making `V` uniformly continuous. A nonnegative uniformly continuous function with finite integral must tend to zero (the elementary Barbalat argument: otherwise infinitely many disjoint intervals of uniformly positive area would force divergent integral). This proves asymptotic decay.

For all `i,j`, by Cauchy–Schwarz
`(b_i-b_j)^2 <=2[(b_i-M/4)^2+(b_j-M/4)^2]<=4V`.
If any pair differs by at least `delta`, then `V>=delta^2/4`. On the set of such times `T_delta`,
`int_0^infty 2 V >= |T_delta| *delta^2/2`.
Together with `int 2V<=E(0)` this proves `|T_delta|<=2E(0)/delta^2`. QED.

## Counterexamples and scope

This theorem is **not** a no-go for permanent topological memory, permanent charge under an independent protected sector, or a source with replenishment. It assumes a fixed K4 graph, open passive Q162 contacts, a finite initial reserve, nonnegative dissipated stock, and the declared normalized ledger. A maintained external reservoir, a different transport law, topology-changing occupancy or a nondissipative invariant can evade it without contradicting this result.

A synthetic control with `M=4`, `gamma=2`, `R_*=1`, initial `b=(11/10,9/10,1,1)` and post-jump `R=199/100`, gives initial growth of the 0-to-1 separation, then eventual decay as the reserve is spent. This numerical example is not needed for the theorem and supplies **no** physical persistence evidence.

**OPEN_GATED:** Native source of reserve, physical action units, true packet defect persistence, cell occupancy, SI clock and independent review. Physical promotion 0.
