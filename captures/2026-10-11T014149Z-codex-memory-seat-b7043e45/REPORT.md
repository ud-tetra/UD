# UD native C1 memory lift and OP03 seat-source boundary v0.1

**11 October 2026 UTC · development addendum · physical promotion 0.**

## Inputs and source versions

The attached `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, Q165/Q169 (local SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) supplies the real Euclidean chain stock and global skew Hodge–Dirac generator on the filled tetrahedron. `UD_RELATIVE_FRAME_FROM_C1_EXECUTION_v0.7.md` (30 August, Library `libfile_197ff0fbc504819185ef21e9e3ed083f`), §§0–5, requires a source-complete oriented (C_1) transfer. `UD_PREEVENT_RELATIVE_FRAME_SOURCE_LAW_v0.1.md` (30 August, `libfile_f5cc9aef39fc819180ce90b67b7ec4b5`), §§2, 4–6, retains an observed/co-moving quotient as a conditional frame source. `UD_OPEN_SYSTEM_HAMMING_BUDGET_RECEIPT_INDEX_LAW_v0.2 (1).md` (30 August, `libfile_8ea519b7af8881918c2d009ce74fe8d8`), §§1, 3–8, supplies the conditional receipt index and endpoint optimizer. The [prior scope amendment](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-11T013224Z-codex-receipt-eligibility-901e806e) recorded its no-op and seat-address counterexamples. This release derives a native memory lift and checks a candidate guard without changing the frozen source.

## Exact 12-dimensional native memory lift

Set (q=c_1\in C_1(K_4)=\mathbb R^6) and (p=\dot c_1=B_1^Tc_0-B_2c_2\in C_1). The source generator uses (\dot c_0=-B_1c_1), (\dot c_2=B_2^Tc_1-B_3c_3), with (B_2B_3=0). On the filled tetrahedron, (B_1^TB_1+B_2B_2^T=4I_6). Hence

\[
\dot q=p,\qquad \dot p=-4q,\qquad
M(s)=\begin{pmatrix}\cos(2s)I_6&\tfrac12\sin(2s)I_6\\-2\sin(2s)I_6&\cos(2s)I_6\end{pmatrix}.
\]

Initial conditions (q(0),p(0)) are independent: (p\) is realized by (c_0=B_1p/4,\ c_2=-B_2^Tp/4\), with (c_1=q,c_3=0). This canonical minimum-norm lift (L:C_1\oplus C_1\to C_0\oplus C_1\oplus C_2\oplus C_3) has (A L=L\begin{psmallmatrix}0&I\\-4I&0\end{psmallmatrix}\), and (L^TL=\operatorname{diag}(I_6,I_6/4)\). The induced positive stock (\lVert q\rVert^2+\lVert p\rVert^2/4\) is conserved. The map is an exact 12-dimensional invariant subspace of the 15-dimensional source generator. This does not contradict the prior result that **no nonzero invariant subspace lies entirely inside the six-dimensional (C_1)**.

**EXACT minimality, specified class:** for a linear time-homogeneous first-order realization representing every native (q) trajectory with (q) as readout, the initial jet ((q(0),\dot q(0))\) ranges freely over (\mathbb R^{12}). A realization state must distinguish all these jets, so its linear state dimension is at least 12. (L) attains the bound. This is a minimal realization of the native (C_1) readout under these assumptions, not a primitive packet transport law.

At (s=\pi/4), (M=\begin{psmallmatrix}0&I_6/2\\-2I_6&0\end{psmallmatrix}\), (M^2=-I_{12}), and (M^{-1}=-M). The (q\to q) block vanishes, but (q\to p) carries (-2I_6). The singularity of a (q)-only compression is therefore **not** a singularity of the native memory lift. `memory_lift.py` independently verifies the chain incidence, 15-by-12 intertwiner, positive metric, exact quarter-step inverse and all 24 (S_4) equivariance cases using rational arithmetic.

**CANDIDATE bridge, conditional:** let (R_W(r)=\operatorname{diag}(\rho_1(r),\rho_1(r))\). If a separately sourced observed operator satisfies (T_W^{obs}=R_W(r)M(s)) and its co-moving companion is (D_W^{cf}=M(s)) on the same frozen history, then (T_W^{obs}(D_W^{cf})^{-1}=R_W(r)), including at the (q)-only quarter-step singularity. All 24 exact conditional fixtures pass. The native (A) supplies (M), **not** a nonidentity (r) or the assumed observed/co-moving factorization. Reusing the v0.7 six-dimensional boundary extractor on the 12-dimensional operator requires an explicitly defined bridge; equal edge dimensions do not identify the carriers. Frame-source and switch-source claims remain **OPEN_GATED**.

## Independent finite guard reproduction

`guard_replay.py` reimplements the v0.2 shell optimizer and candidate v0.2.1 coordinate-seat guard using three-bit masks, independently of the earlier matrix verifier. It enumerates all (8\) pre-event Θ states, (8\) frozen coordinate output-seat sets, (8\) pair-integrity masks, and (3^3=27\) exact burden-score vectors: (8^3\cdot3^3=13{,}824\) algebraic combinations. It checks six (S_3) relabelings per combination, (82{,}944\) exact covariance checks.

| Candidate guard classification | Cases |
|---|---:|
| Required open seat fails integrity | 7,992 |
| Admissible no change, (a=000) | 729 |
| Θ switch, (a\ne000) | 5,103 |
| Of switches, zero index (\mu=0) | 972 |

These counts include repeated exact score vectors and are **not** event frequencies. An independent counting check gives 27 integrity-admitted seat/mask combinations: (27\cdot8\cdot27=5{,}832\), partitioned into (729+5{,}103\). There are (3^3=27) no-change seat/mask combinations, each replicated over 27 score vectors, hence 729. The original v0.2 shell-only optimizer has 912 unique endpoints inconsistent with the coordinate-complete output seat among the cases where the candidate seat guard is integrity-admissible. They are source-compatibility diagnostics, not measured errors.

**EXACT coordinate-seat theorem.** If the frozen viable output obligation space is exactly (\mathcal L^+=\operatorname{span}\{e_p:p\in S^+\}\), any coordinate endpoint satisfying (\operatorname{span}\{e_p:\theta_p^+=0\}=\mathcal L^+\) is uniquely (\theta_p^+=0\iff p\in S^+\). The burden objective is then a diagnostic; it cannot choose a different address. The event toggle (a=\bar\theta^-\oplus\theta^+\) vanishes exactly when the old and new open-seat sets agree. Equal seat counts only imply (\mu=0\); they permit genuine swaps.

**EXACT equivariant no-go for all untyped non-coordinate lines.** The line (\operatorname{span}(e_A+e_B+e_C)\subset\mathbb Q^3\) is fixed by every (S_3) pair relabeling, while no one-seat subset is fixed by every (S_3\) permutation. Therefore there is no deterministic (S_3)-equivariant rank-preserving selector from **all** one-dimensional subspaces to one-seat subsets. A non-coordinate lineage needs a frozen typed seat map or a hold; arbitrary projection or tie breaking would change the source claim.

## Frozen candidate protocol and independent evidence

`PROTOCOL_v0.2.1_CANDIDATE.md` freezes the pre-target null/seat guard, event labels, score fields and rollback conditions. It is a **candidate protocol** appended beside the frozen v0.2 protocol (`UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.2_RECEIPT_INDEX.md`, 4 September, Library `libfile_e56ff2964c8881918c6564d57e9a6a17`), not its replacement. The 14 September authenticated source gate (`UD_OP03_AUTHENTICATED_HELD_OUT_REPLAY_SOURCE_GATE_v0.2.md`, `libfile_32f759d285608191a746627e198f7be7`, §§0–5) reports no independent target corpus; [prior acquisition status](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-11T013224Z-codex-receipt-eligibility-901e806e) remains `NO_DATA`. No endpoint was opened, no independent score was run and no candidate guard was promoted as a predictive law. A future independent producer must supply the lineage-to-seat assignments and source-labelled observed/co-moving (W) transfers, if the memory route is used, before target disclosure.

## Disposition

**EXACT:** native 12D minimum linear realization, its conserved metric and invertible quarter-step; finite coordinate-seat guard census and (S_3) covariance; non-coordinate rank-one equivariant selector no-go. **CANDIDATE:** use the memory transfer as a co-moving control only when an observed counterpart is sourced, and use the v0.2.1 seat/no-op guard in a future frozen cohort. **OPEN:** actual exposure-frame mechanism, sourced lineage-to-seat assignments outside coordinate-complete cases, independent sealed OP03 history, physical bridge. Physical promotion 0; non-constructor review pending.
