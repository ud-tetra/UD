# UD native-flow projection boundary v0.1

**11 October 2026 UTC · development — no registry entry · physical promotion 0.**

## Source question and types

The selected task asks for a pre-event local transport or closure update, and an independent same-carrier K4/`Theta` target. The source object here is the **global chain evolution**, not an already defined edge transport. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, Q169, locks a skew global Hodge–Dirac operator on uniquely owned cochains, while Q156/Q167/Q173 use **given** hard masks. The exact K4 incidence and a fixed-`U_e=I` null are frozen in [`UD primitive-update audit and static K4 null v0.1`](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T164734Z-codex-native-static-null-b71cb9e8), §§1–3. The 21 August `UD_EDGE_CLOSURE_AND_TRANSPORT_INTEGRITY_HARD_GATE_DERIVATION_v0.1.md`, §§II–IV (Library `libfile_e9d5b0d7a4bc81918822ae403d527626`) defines a context-dependent lawful local transport predicate, not a projection of the chain evolution. The 30 August `UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md`, §6.2 (Library `libfile_8b9461fba6248191bb6d58dcf977a977`) specializes its transport gate to exact isometry `T_e=1[I-U_e^*U_e=0]` for a contractive sector. The proposed bridge `U_e=P_eO(s)P_e` below is **new and deliberately adversarial**; the cited sources do not identify these two typed operators.

## Exact native calculation

Take the oriented filled tetrahedron `Delta^3`, Euclidean real chain register `C=C_0⊕C_1⊕C_2⊕C_3` of dimensions `4+6+4+1=15`, vertex order 0–3 and simplex orientations increasing. Let `B_k:C_k→C_{k-1}` be its exact incidence maps and

\[
A=\begin{pmatrix}
0&-B_1&0&0\\
B_1^T&0&-B_2&0\\
0&B_2^T&0&-B_3\\
0&0&B_3^T&0
\end{pmatrix},\qquad O(s)=e^{sA}.
\]

`A:C→C` is skew adjoint, `s` is a **dimensionless native parameter**, and `O(s)` is orthogonal. Initial data for the diagnostic are any canonical unit edge basis vector `e∈C_1`; no boundary change, defect source, loss, or physical clock is posited. Direct incidence gives

\[
B_1^TB_1+B_2B_2^T=4I_6,\qquad B_1B_2=B_2B_3=0,
\qquad A^2e=-4e.
\]

Thus the trajectory on the two-dimensional invariant plane `span(e,Ae)` is exactly

\[
O(s)e=\cos(2s)e+\tfrac12\sin(2s)Ae.
\]

Declare the **candidate projection bridge** `V_e=span(e)` with orthogonal projection `P_e` and `U_e^{proj}(s)=P_eO(s)P_e|_{V_e}:V_e→V_e`. Since `Ae⊥e`,

\[
\boxed{U_e^{proj}(s)=\cos(2s)I_{V_e}},\qquad
\boxed{Q_e^{proj}(s)=I-(U_e^{proj})^*U_e^{proj}=\sin^2(2s)I_{V_e}}.
\]

For each of the six edges, at native `s=0,\pi/4,\pi/2` the projected scalar is respectively `1,0,-1`, and its exact-isometry hard gate is `1,0,1`. This is a **mathematical projection sequence**, not six observed UD mask switches. The underlying full flow is lawful throughout, and `U_e^{proj}=-I` at `\pi/2` is again an isometry. No fitted threshold or physical unit enters.

## Why a local contractive step misses the return

For a chosen step `h=\pi/4`, `O_h=O(h)` is orthogonal and `O_h^2=O(2h)`, but compression does not preserve composition:

\[
P_eO_h^2P_e
=(P_eO_hP_e)^2+P_eO_h(I-P_e)O_hP_e
=-I_{V_e},\qquad (P_eO_hP_e)^2=0.
\]

The `-I` term returns through the complement. Equivalently, for `x_n=P_e\psi_n`, `y_n=(I-P_e)\psi_n`, native source flow entails the **exact augmented-state recurrence**

\[
x_{n+1}=P_eO_hP_ex_n+P_eO_h(I-P_e)y_n,\quad
y_{n+1}=(I-P_e)O_hP_ex_n+(I-P_e)O_h(I-P_e)y_n.
\]

This predicts the projected amplitude from a specified full pre-event chain state and interval. It is **not** a closure receipt or a justified map on the source's internal edge transport fiber. The previous [conditional contractive update boundary v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T225355Z-codex-transport-boundary-6666de3f) assumes `U_{n+1}=R_nK_nU_n`; from `U_h=0`, no such composition can give `U_{2h}=-I`. Its one-way theorem remains exact under its own assumptions. This counterexample shows why the native projection cannot be inserted into that one-step class without environmental memory or a separate reset.

## Frozen-null test and decision

The prior exact [fixed-structure K4 null v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T164734Z-codex-native-static-null-b71cb9e8) allows the same native cochain operator to evolve while primitive closure receipts and six declared internal edge maps `U_e=I` remain fixed. The compression identification would instead label each edge integrity failure at `s=\pi/4`. Those are different **model completions**: a change of global chain amplitude is not by itself a failure of the typed internal transport map. Therefore **NO-GO, scoped:** `P_eO(s)P_e` cannot be asserted as a *universal* source-derived local transport law consistent with that allowed fixed-map completion. This does not forbid a new context-specific bridge with an explicit internal fiber, metric, connection, and structural change mechanism. It also says nothing about pair-level `Theta` events. Exact recurrence times here reflect the finite native operator spectrum, not physical recurrence.

`verify.py` independently constructs all oriented boundary maps from simplex lists; it checks `B_1B_2=B_2B_3=0`, edge Laplacian `4I_6`, `A^3=-4A`, two exact polynomial evaluations of `e^{sA}`, orthogonality and composition on the full 15-space, the six compressed edges, and agreement with the prior frozen null's `B_1,B_2`. It uses rational arithmetic for the exact endpoint operators. The general formula follows algebraically, not from enumerating six edges alone.

## Independent target intake

The frozen `UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.1.md` (30 August, Library `libfile_30fb9c2688f08191acb9119bfdb6a2f4`, Event boundary through Scoring) and the [OP03 intake v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T165944Z-codex-op03-intake-ed488bce) require ordered pre-event cochains/transport, a predictor freeze before endpoint exposure, an independent producer and sealed post-event `Theta` receipts. Current GitHub `main` at `f2fc124c2bdf6db1fb1700ace2acd1f7634190d9` adds no such producer; a repository filename search found no `pre_event.jsonl` or `outcomes.jsonl`. A fresh Library listing after 10 October 18:25 UTC yielded this project's previous release and MQM files; targeted queries found no new qualifying history. The known generated history remains ineligible because it used the selector to label its endpoints, as recorded in [eligibility audit v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T165456Z-codex-event-eligibility-d4d33a75). The supplied older `Gap2_FINAL_STATUS.md` and placeholder ZIP do not contain K4/`Theta` event receipts. `Gap2_FINAL_Finite_Genesis.png` failed to materialize and was **not inspected**.

**NO_DATA / NOT_RUN:** no independent same-carrier history is available for scoring. This is an acquisition status, not a negative empirical finding. Reopening requires a versioned independent producer with code hash, complete consecutive eligible and null windows, raw ordered pre-event cochains and structural receipts, frozen eligibility, and sealed independently generated endpoint `Theta` labels; then run the existing OP03 intake unchanged.

## Disposition

**EXACT conditional:** edge Laplacian and projected return with noncomposition. **NO-GO, scoped:** naive global-flow compression as a universal internal edge transport law. **OPEN:** constitutive, typed map from native packet state/connection to the internal edge fiber and primitive closure update; independent OP03 target. No autonomous dynamics or physical correspondence promoted. The supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, §§1–4, is a governance proposal; non-constructor review remains pending. Physical promotion 0.
