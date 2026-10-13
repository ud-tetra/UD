# UD donor tracking and repeat gate v0.1

**13 October 2026 UTC · development result · physical promotion 0.** Constructor and adversarial self-check: Codex. Independent non-constructor review pending. This is an append-only extension of [B1, support-balance trigger and reservoir gate v0.1, §§1–5](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T025426Z-codex-balance-trigger-5795d919/UD_BALANCE_TRIGGER_RESERVOIR_GATE_v0.1.md), not a change to its one-shot contract.

## 1. Sources, objects, and assumptions

[UD Paper I review draft 1.1.1, §§4, 6.1, 7.4, 8.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) specifies the fixed-complex real chain flow `c'=A_K c`, `A_K=B_K^T−B_K`, but leaves an actual geometry-change admission law open. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165–Q173 separately types core and face-interface support; neither source states that equality of stocks triggers refinement. The supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, §§1, 3–6, is proposal governance. B1 §4 supplies the **candidate** ordinary oriented barycentric subdivision `S` and the conditional isometry with donor map `R`; it proves `S^TS=I+R^TR=⊕(k+1)!I` in the simplex coefficient norm. The admission equality and preparation below are additional modeling choices.

All norms below are squared Euclidean chain amplitudes, dimensionless support, **not** measured energy. `s` is the fixed-complex internal evolution parameter, **not** physical time. The finite source carrier `C(K4)`, donor coordinates, residual bank, and post-event carrier `C(sd K4)` are distinct spaces. The physical embedding, causal implementation, a universal source dynamics, and a Lorentzian metric are not given.

## 2. DERIVED conditional closed tracking on the first prepared orbit

Let `t` be the unit oriented filled tetrahedron, `f=B₃t/2`, and `A_K t=-2f`, `A_K f=2t`. B1 §3 gives `c(s)=cos(2s)t−sin(2s)f`, with its first downward stock-balance crossing `s₁=π/8`. Add orthonormal donor axes `r_t,r_f` and an orthogonal residual sink `w`. The five-dimensional **engineered** initial condition and generator are

\[
v_0=t+\sqrt{23}\,r_t,\quad
v_1=-f-\sqrt5\,r_f+\sqrt{18}\,w,\quad
J={v_1v_0^{\!T}-v_0v_1^{\!T}\over12}.
\]

`v₀·v₁=0`, `||v₀||²=||v₁||²=24`, `J^T=-J`, `Jv₀=2v₁`, `Jv₁=-2v₀`. Hence the unique declared closed solution from `v₀` is `x(s)=cos(2s)v₀+sin(2s)v₁`; its projection to `span(t,f)` is **exactly** the sourced fixed-K orbit. Its donor projection is `R c(s)` on this restricted orbit, while its residual amplitude is `√18 sin(2s)`. At `s₁`, the support ledger is exactly:

| Type | Initial | Immediately before first event | Immediately after first event |
| --- | ---: | ---: | ---: |
| Native chain | 1 | 1 | 15 |
| Prepared donor | 23 | 14 | 0 (transferred) |
| Residual sink | 0 | 9 | 9 |
| Total | 24 | 24 | 24 |

The first event applies B1's orthogonal completion `U` to native+donor+zero blanks, while leaving `w` untouched: `(c,Rc,0,w)↦(Sc,w)`. This maps `C(K4)⊕R¹¹⊕R¹²³⊕R` to `C(sd K4)⊕R`, preserves total squared support and has native boundary `∂Sc=S∂c`. The generic donor map has 11 axes; only the two top/face combinations are occupied on this prepared orbit. The sink coefficient `√18` is forced by norm balance **after choosing** to keep the donor tracking relation throughout this orbit. The initial `√23` donor amplitude is supplied as an initial resource; `J` was constructed for this orbit and is not found in Q165–Q173. This is an existence example of closed tracking conditional on an enriched initial state, **not** autonomous bank generation from a blank state or a UD-derived event law. A norm-preserving preparation from `(t,0,0)` alone remains impossible for nonzero donor requirement.

## 3. EXACT second crossing and fixed-stock obstruction

Use the ordinary subdivided incidence generator `A'=B_{sd K4}^T−B_{sd K4}` with initial post-event chain `Sc(s₁)`. Write `u=St` and `v=Sf`. Enumerating all 149 simplex coordinates of `sd K4`, or using the flag-chain boundary cancellations, gives the integer/rational relations

\[
\|u\|^2=24,\quad \|v\|^2=6,\quad u\cdot v=0,\quad A'u=-2v,\quad A'v=\tfrac12 u.
\]

Thus `U=u/√24`, `V=v/√6` are orthonormal and `A'U=-V`, `A'V=U`. The first output is `Sc(s₁)=√12 U−√3 V`, with grade-3 and grade-2 supports 12 and 3. Under the declared **unmodified** new fixed-complex flow, at internal delay `δ` after the event,

\[
a_3(\delta)=\sqrt{12}\cos\delta-\sqrt3\sin\delta,\qquad
a_2(\delta)=-\sqrt{12}\sin\delta-\sqrt3\cos\delta.
\]

The first downward equality of the new grade stocks occurs **exactly** at `δ₂=arctan(1/3)>0`: `tan δ₂=1/3`, `E₃=E₂=15/2`, `q' < 0`, native support 15. This exact two-dimensional sector is independently replayed by enumerated 149-coordinate incidence and numerical spectral propagation in `verify.py`; the scan bracket `[0.32,0.3225]` and root `0.32175055439664213` check the analytic result.

For a second **hypothetical** full barycentric renewal on this trajectory, B1's exact donor debit formula gives

\[
D_2=5E_2+23E_3=5\cdot\frac{15}{2}+23\cdot\frac{15}{2}=210,
\quad \|S_{sd K4}c\|^2=15+210=225.
\]

The closed first episode leaves only 9 squared support outside the native chain, a shortfall of **201**. The whole closed system has 24. Therefore a second transfer to the *ordinary, unnormalized* barycentric output is **NO-GO with fixed total support 24** under this prepared orbit and admission rule, regardless of how the residual is moved among auxiliary coordinates. With the existing B1 one-shot latch, the second equality is simply a calculated signal and does not request a second event. If a renewed latch is installed, the resource gate must reject that event. Replacing the map, norm, donor source, or event criterion defines a new candidate branch, not a refutation of this obstruction.

## 4. General conditional finite-resource statement

For any finite 3-complex and any native chain at a proposed ordinary barycentric event, let `N=||c||²`, `H=E₂+E₃`, `h=H/N` when `N>0`. B1's Gram identity implies

\[
D=E_1+5E_2+23E_3\ge5H,\qquad N_{next}=N+D\ge N(1+5h).
\]

If a closed sequence has finite conserved total support `T`, starts with `N₀>0`, and every admitted event satisfies **an independently assumed** uniform bound `h≥ε>0`, then after `m` events `N_m≥N₀(1+5ε)^m≤T`; consequently `m≤floor(log(T/N₀)/log(1+5ε))`. This is an exact conditional finite-count theorem. A repeated sequence with fixed `T` can evade this bound only if its high-grade fractions lack that positive lower bound, or if the map/norm/closedness assumptions change. On the specific two-sector balance crossings here, `E₁=E₀=0` and `E₂=E₃=N/2`, so `D=14N` and a successful full transfer would multiply native support by 15. `T/N₀=24` permits the first such event but not the second.

These are support and event-count statements. A positive first-to-second delay does **not** prove a uniform positive delay across changing complexes. Finite event count precludes infinitely many successful transfers only under its hypotheses; otherwise possible Zeno accumulation remains **OPEN**. The B1 one-shot latch makes its own one-event execution nonaccumulating by construction.

## 5. Disposition and reproducibility

**EXACT / conditional:** joint skew rotation and total-stock ledger on the prepared two-mode orbit; post-event invariant two-mode sector; second crossing `arctan(1/3)`; debit 210 and deficit 201; finite-count inequality under its stated `ε` bound. **NUMERICAL:** enumerated flag-complex replay and spectral root as independent implementation checks of that case. **CANDIDATE:** stock-balance admission, enriched donor/sink rotor, and a possible rearming policy. **NO-GO:** second ordinary full barycentric transfer with the fixed closed total 24, and free bank preparation from only native support 1. **OPEN:** UD-sourced donor production and tracking for general states, physical or local implementation, a repeatable funded admission protocol, no-Zeno theorem under changing geometry, Lorentzian continuum cone and experiment. Physical promotion 0. The missing attachment `Gap2_FINAL_Finite_Genesis.png` was unavailable and was not used.

Run `python3 verify.py` (NumPy and SciPy) to regenerate `results.json`. The incidence/flag matrices and sample state are built in code, with exact integer relation checks before numerical propagation. The source-facing Gram proof and assumptions are in B1 §4. No external physical data or calibrated time map is used.
