# UD bounded subdivision: two-event development gate v0.1

**13 October 2026 UTC · development, no registry entry · physical promotion 0.** Constructor and adversarial self-check: Codex; non-constructor review pending. This is a new, conditional branch from [B1, support-balance trigger and reservoir gate v0.1, §§1–5](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T025426Z-codex-balance-trigger-5795d919/UD_BALANCE_TRIGGER_RESERVOIR_GATE_v0.1.md), and responds to the fixed-stock obstruction in [donor tracking and repeat gate v0.1, §§2–4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T030716Z-codex-donor-repeat-96db4640/UD_DONOR_TRACKING_REPEAT_GATE_v0.1.md). It does not amend their ordinary unnormalized subdivision results.

## 1. Source audit and typed problem

[UD Paper I review draft 1.1.1, §§4, 6.1, 7.4, 8.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) supplies fixed-complex real chain evolution `c'=A_K c`, `A_K=B_K^T−B_K`; geometry-change admission and cross-complex evolution remain open. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165 and Q169–Q173 supplies the micro squared-amplitude support, glued fixed-complex generator, control-volume flow, and face/core stock. Q157–Q160 and Q178 keep recursive/coarse support, open-system source/sink, and renewal semantics open. There is **no sourced replenishment law**, nor a sourced event normalization. The supplied CRL2 subdivision governance proposal v1.0, §§1–4, is not a promotion receipt.

We therefore test the other authorized branch: a **candidate** transfer using ordinary oriented barycentric `S:C(K)→C(sd K)` on a finite oriented 3-complex. `C(K)` and `C(sd K)` are distinct real Euclidean coefficient spaces; `∂` is simplicial boundary. Squared support has dimensionless chain-amplitude units, not energy. Internal flow parameter `s` is not physical time. Use the B1 candidate equality-to-event rule with rearming after each successful transfer only for the explicit two-event test. A residual bank has its own coordinates and is not treated as a simplicial chain.

## 2. EXACT bounded transfer within the scalar subdivision family

B1 §4 proves `∂_{sd}S=S∂_K` and `S_k^TS_k=(k+1)!I` for simplex bases. Suppose the candidate uses one scalar per chain degree, `T_k=a_k S_k`. For each nonzero boundary map, `∂T_k=T_{k-1}∂` forces `a_k=a_{k-1}`. For a connected filled 3-simplex all maps are nonzero, so every `a_k` equals one common `a`. Contractivity for all chains is then equivalent to `|a|≤1/√24`. Choose the maximal positive value:

\[
T_k={S_k\over\sqrt{24}},\qquad
T^TT=\bigoplus_{k=0}^3\frac{(k+1)!}{24}I,
\qquad
D=(I-T^TT)^{1/2}.
\]

The map `J:c↦(Tc,Dc)` into `C(sd K)⊕C(K)` is an isometry, since `J^TJ=I`; the native component obeys `∂Tc=T∂c`. Thus an orthogonal completion with unused blanks exists, and no **new** support is needed: `||Tc||²+||Dc||²=||c||²`. Old residual coordinates from earlier events can pass unchanged. This is an **algebraic** construction, not a UD-sourced physical gate. The residual `D` is a complementary carrier, not a simplicial boundary map or a source of new norm. The positive choice of `a` fixes one convention within this scalar family; a different transfer with different geometry or metric remains possible.

**Boundary and readout tradeoff.** The zero-grade map is also scaled: `T₀ e_v=e_{\{v\}}/√24`. Hence vertex amplitudes and boundary amplitudes relative to an unscaled neighboring complex change. If a contract requires `T₀=S₀` **within this common-scalar chain-map family**, then `a=1`, and top-grade norm expands by 24; contractivity fails. The global batch can match its own scaled boundary, but a fixed external boundary requires an additional calibrated interface. Uniform amplitude attenuation is not implied by the source ledger and cannot be dismissed as a gauge without specifying readout and metric.

## 3. EXACT two-crossing calculation on the prepared K4 sector

For the same `t=e_{0123}`, `f=B₃t/2` and first downward stock crossing `c₁=(t-f)/√2` as B1 §3, the native pre-event support is 1. The normalized transfer gives

\[
E_3(Tc_1)=\frac12,\quad E_2(Tc_1)=\frac18,
\quad N_{1+}=\frac58,\quad R_{1+}=\frac38.
\]

Here `R` denotes squared support in a separate residual carrier. The post-event native q is `3/8>0`, so the proposed latch can be rearmed. In the new fixed-complex generator, `u=St`, `v=Sf` satisfy `||u||²=24`, `||v||²=6`, `A'u=-2v`, `A'v=u/2`. Thus `U=u/√24`, `V=v/√6` obey `A'U=-V`, `A'V=U`; the new native state is `√(1/2)U−√(1/8)V`. Its first downward equality after the event occurs at **exact internal delay** `δ₂=arctan(1/3)`, with

\[
E_3=E_2=\frac{5}{16},\qquad N_{2-}=\frac58.
\]

Apply the **same** bounded transfer on `sd K4→sd² K4`. The Gram identity is local to each simplex and remains valid on any finite 3-complex; no 149-to-thousands incidence matrix is needed for this exact norm step. The second output and cumulative residual stocks are

\[
N_{2+}=\frac{24}{24}\frac{5}{16}+\frac6{24}\frac{5}{16}=\frac{25}{64},
\quad R_{2+}=\frac38+\left(\frac58-\frac{25}{64}\right)=\frac{39}{64},
\quad N_{2+}+R_{2+}=1.
\]

**DERIVED conditional result:** two successive admitted refinements are algebraically funded by transferring some native support to residual carriers. This is *not* replenishment: native support decreases from 1 to `5/8` to `25/64`. The 149-coordinate `sd K4` construction in `verify.py` independently checks integer boundary/Gram relations and the first post-event invariant sector; numerical root search gives `0.32175055439664213`, checking the analytic `arctan(1/3)`.

## 4. Failure modes and scope

1. **No source-derived normalization.** Q165–Q173 define stocks and their fixed-complex flows. They do not select `1/√24`, authorize uniform amplitude attenuation, define residual readout, or supply rearming. The branch remains CANDIDATE / development.
2. **No cross-event dynamical intertwining.** With `A_Kf=2t` and `a=1/√24`, the exact relations give `A_{sd}(Tf)=a u/2`, whereas `T(A_K f)=2a u`; their difference is `-3a u/2`. Hence `A_{sd}T≠TA_K` even on the prepared sector. Each fixed-complex segment has its native skew flow, but the transfer does not make them one source-derived continuous dynamics.
3. **External interface unresolved.** The native boundary identity scales both sides, but a fixed unscaled outside boundary cannot be preserved by this scalar family. A global batch or explicit interface law is required.
4. **Repeatability and time unresolved.** Two exact norm-funded events do not provide a third crossing, a non-Zeno lower spacing bound, a local causal rule, a physical clock, a Lorentzian continuum cone, or an experiment. A finite support ledger alone is insufficient to determine event occurrence.

**Disposition:** **EXACT conditional** scalar-family maximal contraction, chain identity, isometric residual completion, two support ledgers and analytic second crossing. **NUMERICAL** enumerated incidence and root replay. **NO-GO** simultaneous common-scalar chain compatibility, unit vertex amplitude, and contractivity on the filled tetrahedron. **OPEN** a UD-sourced admissibility/normalization law, physical boundary/readout, cross-event dynamics, independently reviewed bridge, and physical correspondence. Physical promotion 0. The `Gap2_FINAL_Finite_Genesis.png` attachment was unavailable and not used.

Run `python3 verify.py` with NumPy and SciPy to regenerate `results.json`. The script builds the first barycentric flag complex, verifies `∂S=S∂` and `S_k^TS_k=(k+1)!I` with integer matrices, and checks the proposed two-event ledger. The algebraic second Gram step is proved above rather than inferred from the finite numerical run.
