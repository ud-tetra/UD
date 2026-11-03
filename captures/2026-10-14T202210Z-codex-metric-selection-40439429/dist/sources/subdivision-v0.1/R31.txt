# UD support-balance trigger and reservoir transfer gate v0.1

**13 October 2026 UTC · development, no registry entry · physical promotion 0.** Constructor and adversarial self-review: Codex. No independent non-constructor review. This extends the [barycentric renewal candidate R1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T022858Z-codex-subdivision-candidate-d14acda4/UD_BARYCENTRIC_RENEWAL_CANDIDATE_v0.1.md) with one genuinely **pre-event computable** signal and an exactly typed support reservoir. It does not promote that signal to a UD law.

## 1. Source and type declaration

[UD Paper I, review draft 1.1.1, §§4, 6.1, 7.4, 8.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) gives fixed-complex real chain flow `c'(s)=A_K c(s)`, `A_K=B_K^T−B_K`, and expressly separates admission/receipt selection from its algebra. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165–Q173 defines the unit micro support and separately typed face-interface and cell-core stocks. Q171 gives `S_τ^core=c_{3,τ}²`; Q172 gives `S_f^iface=c_{2,f}²`, with exchange fluxes. **Neither source says equal stocks cause subdivision.** Q25–Q26 still leave a native state-dependent weight/route source open. The supplied CRL2 subdivision governance v1.0, §§1, 3–6, is a proposal and does not make constructor checks independent review.

This report uses **dimensionless squared chain amplitude** as its support unit, not energy or joules. The finite carrier `C(K)` and donor/blank coordinates are separate spaces. The post-renewal carrier `C(sd K)` is a different space. The update parameter `s` is internal, not physical time. A stored classical latch is another distinct object and its physical implementation is open.

## 2. CANDIDATE B1: one armed crossing, conditional renewal

For a supplied finite oriented 3-complex `K` with initial `c(0)` and closed fixed-K flow, define the **source-observable combination**

\[
E_3(c)=\sum_{\tau\in K_3}c_{3,\tau}^2,\quad E_2(c)=\sum_{f\in K_2}c_{2,f}^2,\quad q(c)=E_3-E_2.
\]

These stocks and `q` are invariant under signed simplex relabelings; threshold zero follows from equality of declared stocks. **The use of that equality as a decision is newly proposed**, not derived from Q171–Q172. Start `ARMED` with `q(c(0))>0`. The candidate event is the first isolated positive-to-negative crossing at `s_*>0` with `q(c(s_*))=0` and `dq/ds(s_*)<0`. If no such crossing exists, `HOLD`; if `q` is identically zero or the root is tangent/degenerate, `DEGENERATE_HOLD`. Detect using only the old-complex trajectory and past sign, before any post-event state. If the typed bank below is unready at that first crossing, mark `FAILED_RESOURCE` and disarm; a fresh episode would need its own preparation. If ready, apply a **global batch** `K→sd K` with boundary subdivision, use the declared unitary transfer, mark `SPENT`, and resume `c'=A_{sd K}c` from the output. There is no unprovided second renewal in this one-shot contract. Geometric cell shapes and boundary chart are supplied, as in R1.

This resolves an *operational decision syntax* on a prepared finite input. It is not a local causal rule (one global stock gates an entire mesh), a source-authored admission theorem, a repeatable infinite refinement generator, or a physical clock.

## 3. EXACT witness for a native fixed-K signal

On one filled `K4`, let `t=e_{0123}` be the unit top chain, `B_3t` its signed four-face boundary and `f=B_3t/2`. Then `||f||=1`, `B_2 f=0`, `A t=-2f`, `A f=2t`. For the declared initial condition `c(0)=t`, the exact closed trajectory is

\[
c(s)=\cos(2s)t-\sin(2s)f,\qquad q(s)=\cos^2(2s)-\sin^2(2s)=\cos(4s).
\]

The first transverse downward crossing occurs at `s_*=π/8`; `q'(s_*)=-4`, `E_3=E_2=1/2`, and native micro support `||c||²=1` throughout. These are exact mathematical event-time facts for the **candidate observable and prepared state**. They do not show a real geometry change, nor that equality is physically privileged. A stationary/zero-contrast state gives a countercase with no admitted renewal. Without the proposed decision line, both “no event” and “refine at crossing” are compatible with the same native `c(s)`.

## 4. EXACT typed support-bank completion, conditional on preparation

Let `S=⊕_{k=0}^3 S_k:C(K)→C(sd K)` be the ordinary oriented barycentric chain subdivision map from R1; `∂S=S∂`. In unit simplex bases, supports of distinct source basis elements have disjoint same-grade descendant coordinates. Hence

\[
S^TS=M=\bigoplus_{k=0}^3 (k+1)! I_{f_k},\qquad
M-I=\bigoplus_{k=0}^3[(k+1)!-1]I_{f_k}.
\]

The required support debit for output `S c` is **exactly** `D(c)=c^T(M-I)c=||c_1||²+5||c_2||²+23||c_3||²`. It is positive for nonzero higher-grade content. Define a distinct donor bank `R_K=R^{f_1+f_2+f_3}` and the typed linear preparation `R:C(K)→R_K` that maps `c_k` to `√((k+1)!-1)c_k` for `k=1,2,3` and omits `k=0`. Thus `R^TR=M-I` and `||Rc||²=D(c)`.

For the filled tetrahedron `f=(4,6,4,1)`, the old carrier dimension is 15 and the donor dimension is 11. The subdivided carrier has `f'=(15,50,60,24)`, dimension 149. Take a separate 123-dimensional blank bank initially zero, so the **complete** pre-event Euclidean carrier `H_pre=C(K)⊕R^{11}⊕R^{123}` and post-event `H_post=C(sd K)` have equal dimension 149. On the restricted prepared inputs `Jc=(c,Rc,0)`, define the target `Sc`. Since

\[
J^TJ=I+R^TR=M=S^TS,
\]

the map `Jc↦Sc` is an isometry of the prepared 15-dimensional subspace and extends to some orthogonal `U:H_pre→H_post` by completing orthonormal bases. It also has an explicit block construction: for each original `k`-simplex set `m=(k+1)!`, group its old coordinate, one donor coordinate when `m>1`, and `m-2` local blanks; a Householder reflection (identity if the vectors coincide) sends `(1,√(m-1),0,…,0)c_σ` to the `m` signed child coordinates, after orientation signs. The remaining 85 blanks map to the 85 unused target coordinates. The 38 local plus 85 remaining blanks give the stated 123. The existence is **exact**; `verify.py` checks the finite Householder blocks numerically to `10^{-12}`. The extension is nonunique and no Hamiltonian, gate sequence or physical preparation is supplied. Boundary compatibility is the chain identity `∂Sc=S∂c` for the *native target component*, not an assertion that donors carry a simplicial boundary. `149` output coordinates include `64` possible standard-subdivision descendants of source basis simplices; the other `85` coordinates are zero for `Sc`. The 123 pre-event blank coordinates are not a claimed minimal physical bank.

At the prepared crossing in §3, `D(c(s_*))=23/2+5/2=14`. The pre-event complete norm is `||c||²+||Rc||²=1+14=15` and the post-event native chain norm is `||Sc||²=15`. **Exact transfer condition:** a source state of native norm 1 needs a prepared donor carrying squared support 14 at this crossing for this output. It is incorrect to report a free 1→15 increase or to identify squared support with measured energy.

**Conditional minimum:** If a *linear* donor map must complete this Gram identity for **every** `c∈C(K4)`, `rank(R^TR)=6+4+1=11`; any such donor carrier has dimension at least 11. The bank above attains that rank. This rank bound does not apply to a nonlinear/event-surface-only transfer, nor does it say 11 donor particles or 11 units of energy.

## 5. Adversarial review of preparation and dynamics

1. **No free bank preparation.** A blank-bank orthogonal operation on `(c,0)` cannot produce `(c,Rc)` for nonzero higher-grade `c`, since the latter has larger norm. An independent resource must carry the debit, plus a state-dependent correlation or a prepared-state restriction. The donor state is a *new input*, not a derivation from `B_K`.
2. **Passive tracking fails.** On the §3 orbit, if a bank were continuously constrained to `r(s)=R c(s)`, its joint norm would be `||c||²+||Rc||²=24 cos²(2s)+6 sin²(2s)`, varying from `24` at `s=0` to `15` at the first crossing. A closed orthogonal pre-event evolution cannot follow that constrained joint path without further resource channels. A donor prepared only at the event needs a source process and timing. Neither is given.
3. **The trigger is not the law.** Equality of cell and face support follows from this orbit, but treating it as a renewal command is a constitutive choice. Initial states can have no crossing, and repeated post-renewal trigger times or accumulation have not been bounded. The one-shot `SPENT` latch prevents that unanswered iterative problem from being hidden.
4. **Lorentzian limit not advanced.** Barycentric refinement still has unbounded degree at old vertices, and its graded sector/mass-normalized continuum symbol has not been derived. The Freudenthal `C=2I+2J` coefficient from a separately supplied family cannot be imported here.

**Disposition:** **EXACT conditional** pre-event crossing time, transfer Gram identity, norm debit and orthogonal completion. **CANDIDATE** equality-to-renewal decision and donor preparation. **NO-GO** autonomous refinement or free support creation from the current native fixed-complex flow. **OPEN** non-constructor review, prepared resource production, local/batch causality, repeatable renewal, a common wave cone, physical clock and GR correspondence. The candidate remains development only; physical promotion 0. The attachment `Gap2_FINAL_Finite_Genesis.png` was unavailable and is not used.
