# UD-PM-PRED04-WORK-002 v1.0 — Sharper uniformly bounded distributed-source theorem

**Proof kind:** THEOREM + scoped normalization audit  
**Evidence:** EXACT_CONDITIONAL, independently rederived; numerical source replay is auxiliary  
**Review:** DEFERRED  
**Physical promotion:** 0  
**Source audited:** UD PR #479 at `b5c8146ae4b956279e6f399553e02cffbc42c7ea`, `docs/UD_PRED01_LOCAL_DEFECT_SELECTION_AND_BOUNDED_SOURCE_v0.4.md`, §4 (blob `abefbc821bd7897e9c469b2ff12bd7cccab56c99`). The antecedent bound `41/5` is correct but non-sharp in the declared update class.

## A. Typed mathematical model

Let `K` be a **finite oriented triangular 2-skeleton**, with real edge cochains `C¹(K;R)` and oriented face coboundary `d:C¹→C²`, under the counting inner product on edges and faces. Let `h≠0` be any **closed real 1-cochain**, `d h=0`. Write `D` for the maximum number of triangular faces incident to a single edge. Choose `λ>0`, `μ≥0` and a nonnegative integer `n`.

Define the *assumed native model action* on any edge cochain `a` by

\[
\mathcal A(a)=\frac{\lambda}{2}\sum_{e}a_e^2+\frac{\mu}{2}\sum_f(da)_f^2.
\]

Start at `a_0=n h` and finish at `a_m=(n+1)h`. Choose **any** ordering of the edges and update each edge exactly once, from `n h_e` to `(n+1)h_e` by addition of `h_e`. Zero-valued edges may be included. Intermediate cochains may be nonclosed. Define total positive increment

\[
W^+=\sum_{t=0}^{m-1}\max\{\mathcal A(a_{t+1})-\mathcal A(a_t),0\}.
\]

This is dimensionless or in chosen **native action units**; it is not automatically physical work, energy, time or power. `λ`, `μ`, `h` and the source update path are independently specified assumptions, not native UD-derived constitutive data.

## B. Theorem — improved exact work bound

Let `Δ = A((n+1)h)-A(nh) = λ(2n+1)||h||²/2 > 0`. Under A,

\[
\boxed{W^+\le \Delta+\frac{\mu D}{3}\|h\|^2},\qquad
\boxed{\frac{W^+}{\Delta}\le 1+\frac{2\mu D}{3\lambda(2n+1)}}.
\]

On the specific Freudenthal tetrahedralized square-grid family in PR #479, `D≤6` exactly. For its `n=2`, `μ=λ` assumption, the multiplicative bound becomes

\[
\boxed{W^+\le\frac95\,\Delta}.
\]

With the **chosen inverse normalization** `λ_N||h_N||²=2/5` (and so `Δ_N=1`), this gives the uniform **absolute model-action bound**

\[
\boxed{W_N^+\le\frac95}.
\]

This improves the earlier valid `41/5` bound under the *same* assumptions. It is not a statement that uncalibrated native physical energy is bounded.

## C. Exact proof

At each edge update, `a_e` changes from `n h_e` to `(n+1)h_e`; since `n≥0`, the positive change in the norm part is exactly `λ(2n+1)h_e²/2`. Summing gives `Δ`. Decompose each total action increment into this nonnegative norm contribution plus the changes in each face's curvature energy. Since the positive-part map is subadditive, total positive work is at most `Δ` plus the sum of positive variations of the individual face curvature energies.

Fix a triangular face `f` with its three oriented contributions `(x,y,z)` from `h`; closedness is precisely `x+y+z=0`. Regardless of global edge ordering, the local face has three updates. Its curvature values visit `0`, then (up to sign) `x`, then (up to sign) `z`, then `0`. Therefore its *squared* curvature sequence is `0,x²,z²,0`, and its total **positive** variation is exactly `max{x²,z²}`.

Because `x=-(y+z)`, Cauchy–Schwarz gives `x²≤2(y²+z²)`. Hence `3x²≤2(x²+y²+z²)`; the same bound holds for `z²`, so

\[
\max(x^2,z^2)\le\frac23(x^2+y^2+z^2).
\]

Thus total positive curvature variation is at most

\[
\frac{\mu}{2}\sum_f\max(x_f^2,z_f^2)
\le\frac{\mu}{3}\sum_f\sum_{e\subset\partial f}h_e^2
\le\frac{\mu D}{3}\|h\|^2.
\]

Add `Δ` and divide by the positive endpoint gap to obtain the theorem. ∎

**Sharpness of the FACE constant:** `(x,y,z)=(1,-1/2,-1/2)` has zero sum, positive variation `1`, and total squares `3/2`, saturating the ratio `2/3`. This does **not** claim the *global* bound `9/5` is sharp on UD triangulations.

### Exact incidence lemma for the Freudenthal family

Any edge in an infinite regular Freudenthal cubical tetrahedralization joins comparable grid vertices `u≤v`, where `v-u` has `k` nonzero binary components, `k∈{1,2,3}`. A third vertex completing a monotone triangular face must be below `u`, strictly between `u,v`, or above `v`. These cases have respectively `2^(3-k)-1`, `2^k-2`, and `2^(3-k)-1` choices. Every such ordered triple occurs in a Freudenthal tetrahedron. Thus the exact local face incidence is

\[
d(k)=2(2^{3-k}-1)+(2^k-2)=2^{4-k}+2^k-4,
\quad(d(1),d(2),d(3))=(6,4,6).
\]

Finite-boundary clipping and K4-star excision only **remove** triangles. Consequently `D≤6` uniformly in the grid resolution; this is a combinatorial proof, not an extrapolation from three simulated grids.

## D. Scope, counterexamples and normalization audit

1. **Prior fixed-three-edge no-go remains valid.** The antecedent v0.3 used a fixed limited support and more restrictive intermediates. This theorem uses all nonzero edges of `h` with one-edge staging and permits temporary nonzero curvature. Changed hypotheses define a new branch; they do not contradict the old no-go.
2. **The absolute uniform bound depends on calibration:** without `λ_N||h_N||²=2/5`, only the *relative* inequality `W_N^+/Δ_N≤9/5` follows when `μ_N=λ_N`. A constant `λ` does not imply `Δ_N` is constant; asymptotic behavior of `||h_N||` is not proved here.
3. **Order freedom versus update-count freedom:** the proof works for any one-pass edge ordering but not for arbitrary extra cycles. Repeatedly toggling one nonzero edge back and forth adds nonzero positive work without changing the final state, producing arbitrarily large `W+` at fixed `Δ`. Hence the one-update-per-edge assumption is essential.
4. **Nonclosed endpoint, negative n, unbounded incidence, or `μ_N/λ_N`:** the derivation must be reconsidered. If `h=0`, the positive retained gap and ratio normalization are undefined.
5. **Physical claim remains open:** `S` is an assumed positive quadratic action, `λ_N` an inverse calibration, the local order a chosen source mechanism, and event count not duration. No SI energy, measured work, endogenous K4 trigger, source/sink coupling or empirical readout is established.

## E. Independent verification

`independent_topology_work_audit.py` uses exact Python `Fraction` and tests **1,008** closed-face rational/order configurations and **1,728** additional exact action/update sequences; it verifies the sharp `2/3` face coefficient and the full general inequality. A separate local combinatorial count checks the seven Freudenthal edge types. A replay of the antecedent PR #479 implementation at `N=4,6,8` returned `W+ ≈ 1.00009961, 1.00082468, 1.00138162`, all below `9/5`, but these numerical examples are corroboration, not proof.

**Proof status:** `VERIFIED_SCOPED / EXACT_CONDITIONAL`. **Independent non-constructor review:** DEFERRED. **Physical promotion:** 0. **Next gate:** derive the distributed support and resolution dependence of `λ_N` from the admitted native UD action, or produce a source-independent observable that distinguishes this rule from competing mechanisms.
