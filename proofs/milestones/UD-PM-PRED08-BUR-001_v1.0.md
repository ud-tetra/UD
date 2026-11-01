# UD-PM-PRED08-BUR-001 v1.0 — Passive Q162 transport cannot amplify burden contrast

**Kind:** NO-GO / dissipation theorem. **Proof status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## Typed source and hypotheses

* Source: UD coefficient provenance ledger v0.39 (2026-08-22), Q153/Q158 (continuity and constitutive source still open), Q156 (typed hard contact), Q162 (relaxational mixing `j_e=-(1/4)h_e(B_1^T b)_e`); source-bound `UD_Native_Gate_Trigger_and_Recovery_v0.1.md` (2026-10-15, §§1–2) and PRED06-SEL-001 (PR #490). All earlier scientific statuses retain their original scope.
* Mathematical carrier: connected undirected graph with a fixed oriented incidence matrix `B_1: R^E -> R^V`, real vertex burden vector `b`, model time `t`, and symmetric nonnegative diagonal mobility/contact matrix `H(t,b)`. This proof does **not** identify burden units with Q165 support energy.
* **Hypotheses:** No nonconservative burden source (`s_B=0`); no topology-changing cell update; `j=-(1/4)H B_1^T b` (or, more generally, any nonnegative mobility prefactor); `b' = B_1 j`; all states differentiable on the declared interval. No physical clock is assumed. Time-dependent masks are permitted as long as their entries remain nonnegative.

## Theorem and proof

Set `M=1^T b`, `bar b=M/|V|` and `V(b)=(1/2)||b-bar b*1||^2`. Since `1^T B_1=0`, `M` is conserved. Thus

\[
\frac{dV}{dt}=(b-\bar b\mathbf 1)^TB_1j=b^TB_1j
=-\frac14(B_1^Tb)^TH(B_1^Tb)\le0.
\]

At a uniform state `b=b_0*1`, `B_1^T b=0`, so `b'=0`, independently of the time-dependent nonnegative hard gate masks. Under locally well-posed evolution, the uniform trajectory remains uniform. In particular, **the sourced passive Q162 law alone cannot create or amplify a nonuniform burden state from an exactly uniform one**. QED.

The same argument works for any **passive** current `j=-K(t,b)B_1^T b` whose symmetric part is positive semidefinite, not merely diagonal Q162 gates. This extension is a mathematical hypothesis about the current class, not an import of a new UD source.

## Scope and counterexamples

The theorem does not prohibit a new constitutive source, an active negative-mobility edge term, external/nonuniform boundary flux, a stochastic symmetry-breaking event, or modified topology. Such branches change the hypotheses. A nonuniform gate mask cannot generate contrast from a perfectly uniform burden by passive gradient transport alone. It can influence which pre-existing contrasts relax.

On K4 with all gates open, `B_1B_1^T=4I-J`. Hence `b'=bar b*1-b`, so every contrast decays exactly as `exp(-t)` and the variance as `exp(-2t)`. These are uncalibrated model-time rates.

**Verification:** independent rational finite sweeps of 624 positive burden vectors against all 64 binary K4 masks (39,936 nonnegative quadratic-form checks), plus a separate symbolic incidence identity. Finite sweeps corroborate, rather than replace, the displayed general proof. **Review:** DEFERRED. **Physical promotion:** 0.
