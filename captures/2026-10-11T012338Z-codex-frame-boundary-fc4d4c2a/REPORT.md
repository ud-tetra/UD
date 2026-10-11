# UD pre-event C1 frame boundary and independent-intake status v0.1

**11 October 2026 UTC · development addendum · physical promotion 0.**

## Source reconciliation and scope

The existing source-defined frame boundary is `UD_RELATIVE_FRAME_FROM_C1_EXECUTION_v0.7.md` (30 August 2026, Library `libfile_197ff0fbc504819185ef21e9e3ed083f`), §§0–5, 7–10. The later `UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md` (30 August, `libfile_8b9461fba6248191bb6d58dcf977a977`), §7.R6, prefers this boundary-covariance extractor and retains `UD_PREEVENT_RELATIVE_FRAME_SOURCE_LAW_v0.1.md` (30 August, `libfile_f5cc9aef39fc819180ce90b67b7ec4b5`), §§2, 4–6, as a conditional co-moving polar alternative. The earlier recommendation to *define* a frame boundary was therefore overbroad. This report **scope-amends** it: a finite frame extractor exists; a source-complete native producer and a structural event trigger remain open.

These sources do not license identifying the chain-edge compression, internal link maps, relative frame, or affine Θ transport merely because each has six edge addresses or a common numerical value. The previous [native projection audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-11T010749Z-codex-native-projection-c9c95ae7), [fixed-structure K4 null](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T164734Z-codex-native-static-null-b71cb9e8), and [connected seam audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-11T011622Z-codex-connected-seam-84c4d102) remain valid in their declared carriers. The attached ledger `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, Q169, records the native Hodge–Dirac carrier; its local copy SHA-256 is `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`.

## Typed rule and continuity obstruction

Let (C_1(K_4)=\mathbb Q^6) with oriented basis (01,02,03,12,13,23), Euclidean support metric and incidence (B_1:C_1\to C_0(K_4)=\mathbb Q^4). A **source-complete** pre-event transfer (T:C_1^{src}\to C_1^{tgt}), not a single transported vector, is required. With consistent source/target orientations and (J_4=\mathbf1\mathbf1^T), the v0.7 mainline decoder is

\[
\widehat P_0(T)=\tfrac14(B_{1,tgt}TB_{1,src}^{T}+J_4),\quad
F(T)=\mathbf1[\widehat P_0(T)\in\operatorname{Perm}(4)\ \wedge\ B_{1,tgt}T=\widehat P_0(T)B_{1,src}].
\]

On (F=1), the unique (r\in S_4) has vertex action (P_0(r)=\widehat P_0). It is a **frame receipt**, not a positive occurrence decision. The residual (K=\rho_1(r)^{-1}T) satisfies (B_1K=B_1). If the exact gate fails, the v0.7 result is `NO_EXACT_DISCRETE_RELATIVE_FRAME_RECEIPT`, not a nearest frame or a declared event.

**EXACT, connected-path theorem.** Let (T:[a,b]\to\mathbb R^{6\times6}) be continuous with fixed labeled source/target (B_1). If (F(T(s))=1) for every (s\in[a,b]), then (r(s)) is constant. Indeed (\widehat P_0(T(s))) is continuous, while its image lies in the finite discrete set (\operatorname{Perm}(4)); a continuous image of an interval is connected. A frame change along a continuous path must therefore cross a failed exact gate (or leave the fixed-carrier assumptions); a discontinuous sourced update is another branch. A gate failure is **not** sufficient for a Θ switch. The same argument applies to a continuous nonsingular co-moving residual whose polar factor remains in the finite (\rho_1(S_4)) grammar throughout.

## Exact fixed-K4 null replay

`verify.py` builds oriented (B_1,B_2,B_3) for the filled tetrahedron, the 15-dimensional real skew Hodge–Dirac generator (A), and checks (B_1B_2=B_2B_3=0), (B_1^TB_1+B_2B_2^T=4I_6), (A^3=-4A). On the declared **diagnostic choice** that the observed chain transfer is the global flow compressed to (C_1),

\[
T_{chain}(s)=P_1e^{sA}\iota_1=\cos(2s)I_6.
\]

This diagnostic is not an identification with the six distinct primitive local edge transports, which remain (U_e=I) in the frozen static null. The time parameter (s) is internal evolution parameter, not calibrated physical time. Exact polynomial flow values at (0,\pi/4,\pi/2) give the following comparison:

| Internal (s) | Chain compression (T_{chain}) | v0.7 boundary gate on that diagnostic | v0.1 polar alternative if (T^{obs}=D^{cf}=T_{chain}) |
|---|---|---|---|
| (0) | (I_6) | identity `FRAME_PASS` | residual (I_6), identity pass |
| (\pi/4) | (0_6) | `HOLD`: (\widehat P_0=J_4/4), not a permutation | singular (D^{cf}=0), `HOLD`; zero paired output alone admits all 24 frames |
| (\pi/2) | (-I_6) | `HOLD`: (\widehat P_0=-I_4+J_4/2), not a permutation | residual ((-I_6)(-I_6)^{-1}=I_6), identity pass |

At the half step the raw polar factor (-I_6) is outside (\rho_1(S_4)), although the co-moving residual is identity. This is precisely the v0.1 §2.1 warning against treating raw intrinsic motion as a frame. The two protocols are **conditional on different admissible input receipts**: v0.7 requires a boundary-covariant pre-event transport with boundary-silent intrinsic residual, whereas v0.1 requires an explicitly sourced observed/co-moving pair and nonsingular null, or a singleton paired-history certificate. The global Hodge–Dirac compression by itself satisfies neither universal bridge into primitive local (U_e) nor automatic v0.7 frame grammar at the two later instants. The half-step discrepancy is a source-definition dependency, not a reason to choose the passing route after seeing an endpoint.

The exact verifier independently enumerates all 24 signed edge-frame matrices, checks orthogonality, chain covariance and mainline extraction, and checks 576 two-sided input/output relabeling examples. It reconstructs the two exact native flow steps, and checks the three table rows and absence of (-I_6\) from (\rho_1(S_4)). This is a reproducible algebraic diagnostic, not an observed event history. There are **zero positive event examples** and **zero independently scored OP03 histories** in this release.

## Independent producer and sealed endpoints: acquisition workload

The frozen `UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.1.md` (30 August, `libfile_30fb9c2688f08191acb9119bfdb6a2f4`), §§Event boundary–Rollback, requires source-labelled pre-event transfer, signed pair support, burden histories, integrity and locality, predictor hash and freeze chronology, then separately sealed endpoint frame/Θ and exclusions. The [existing two-stage intake](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T165944Z-codex-op03-intake-ed488bce) remains unchanged. `UD_OP03_JOINT_REPLAY_EXECUTION_v0.9.md` (4 September, `libfile_de1a3ebc085c8191a78c966bd723cd7a`), §§1, 4–9, explicitly describes its 780 cases as synthetic controls: its frame replay is algebraic and its polarity alternatives disagree, so it is not an independent target. The [prior eligibility audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T165456Z-codex-event-eligibility-d4d33a75) likewise rejects candidate-generated labels as held-out evidence.

Targeted current Library searches for independent pre-event event corpus and sealed K4/Θ endpoint surfaced protocols and synthetic controls, with no qualified producer. A GitHub code-search invocation rejected its arguments; prior repo search is documented in the connected seam audit. This is `NO_QUALIFYING_SOURCE_FOUND_IN_INSPECTED_MATERIAL`, not proof that no corpus exists. `ACQUISITION_STATUS.json` fixes the missing fields and `NO_DATA / NOT_RUN` disposition. No target was exposed, no predictor was retuned, and no OP03 score was run.

## Disposition

**EXACT:** v0.7 source frame gate and the stated connected-path consequence; finite verifier passes its declared diagnostic. **DERIVED, conditional:** the different outcomes of the mainline and co-moving routes on the explicit native null completion. **NO-GO, scoped:** singularity/grammar failure alone as a positive structural Θ switch, and raw chain compression as an unsourced universal primitive local transport. **OPEN_GATED:** specify the native source-complete (C_1) transfer or paired history, a constitutive event eligibility/trigger and any bridge to local edge maps; then obtain an independently produced, pre-frozen OP03 corpus. The v0.1 polar route is retained as a conditional alternative, not silently promoted over v0.7. No autonomous event law or physical correspondence is promoted; physical promotion remains 0.
