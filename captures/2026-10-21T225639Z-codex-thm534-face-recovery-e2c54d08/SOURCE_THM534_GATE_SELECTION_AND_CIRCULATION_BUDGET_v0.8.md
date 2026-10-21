# THM-534 v0.8 — Hard-Gate Selection Nonidentifiability and Finite Circulation Budget

**Date:** 2026-10-21 · **Scope:** exact finite packet algebra on the filled unit-metric tetrahedron, normalized Q162 vertex-burden relaxation · **Status:** EXACT conditional results / NO-GO / candidate selectors quarantined · **Lane:** development, no registry promotion · **Physical promotion:** **0**.

**Provenance:** \`UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md\`, Q153/Q155/Q156/Q158/Q161/Q162/Q163/Q167/Q169–Q173; [THM-534 v0.7](THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md); [typed v0.7 ledger](THM534_BURDEN_GATE_CLAIM_LEDGER_DELTA_v0.7.md); older [v0.6](THM534_COVARIANT_SOURCE_CONTINUITY_v0.6.md). Q156 defines hard gate factorization but **does not define the full predicate** from packet state. Historical \`THM-534\` micro-event origin remains SOURCE-BLOCKED.

## Definitions and exact scope

Carrier \(\Delta^3\): four vertices, six oriented edges \(01,02,03,12,13,23\), four faces \(012,013,023,123\), unit simplex metric. Signed incidences \(B_1:\mathbb R^6\to\mathbb R^4\) and \(B_2:\mathbb R^4\to\mathbb R^6\) satisfy \(B_1B_2=0\), \(B_1^\mathsf TB_1+B_2B_2^\mathsf T=4I_6\). Vertex burden \(\rho_n\in\mathbb R_{\ge0}^4\), total \(M=\mathbf1^\mathsf T\rho_n\), and centered \(x_n=\rho_n-(M/4)\mathbf1\). Gates \(H_n=\mathrm{diag}(h_{e,n})\), \(0\le h_{e,n}\le1\), with accepted binary Q156 special case \(h_{e,n}\in\{0,1\}\).

**Source-bound conditional rule (Q162 plus explicit one-event convention from v0.7):**
\[
j_n=-\tfrac14 H_n B_1^\mathsf T\rho_n,\quad
P_n=I_4-\tfrac14 B_1H_n B_1^\mathsf T,\quad
\rho_{n+1}=P_n\rho_n,\quad
F_n=B_2^\mathsf Tj_n.
\]
The single update index is an **uncalibrated event count**, not physical time; \(F_n\in C^2\) is a signed *face circulation cochain*, not the v0.6 nilpotency-defect operator or physical electromagnetic curvature.

**Provisional packet inputs for a selection test:** binary projections \(\chi_v\) (vertex-local closure), \(\beta_v\) (vertex boundary admissibility) and \(\tau_{uv}\) (edge transport integrity). Their binary domains and their meanings are **candidate operational projections** of the previously provisional \((\chi,b,T_\mathrm{int})\) states, **not** a source-recovered unique UD update law. The underlying filled simplicial complex is not deleted when an edge's transport gate is closed.

## THM-534-S23 — Hard-gate factorization does not identify a selector (EXACT / NO-GO)

**Hypotheses:** only Q156's \(h_e=C_{\mathrm{cl},e}^{\mathrm{hard}}T_{\mathrm{int},e}^{\mathrm{hard}}\), the above typed binary inputs, vertex-relabeling \(S_4\) equivariance, and Q162's conditional burden update are imposed. Consider two fully specified **competing candidate selectors**, indexed by edge \(e=\{u,v\}\):
\[
\begin{aligned}
h_e^{\mathrm{local}}&=(\chi_u\chi_v)(\beta_u\beta_v\tau_e),\\
h_e^{\mathrm{cell}}&=\bigl(\prod_{w=0}^{3}\chi_w\bigr)(\beta_u\beta_v\tau_e).
\end{aligned}
\]
Both have the required Q156 factorization, use only their declared inputs, preserve the all-open homogeneous reference and are \(S_4\)-equivariant. **But they disagree.** For \(\chi=(1,1,1,0)\), \(\beta=(1,1,1,1)\), \(\tau_e=1\), edge order \(01,02,03,12,13,23\),
\[
h^{\mathrm{local}}=(1,1,0,1,0,0),\qquad h^{\mathrm{cell}}=(0,0,0,0,0,0).
\]
With the identical \(\rho_0=(1,0,0,0)^\mathsf T\), Q162 gives
\[
\rho_1^{\mathrm{local}}=(\tfrac12,\tfrac14,\tfrac14,0)^\mathsf T,\quad
F_0^{\mathrm{local}}=(0,\tfrac14,\tfrac14,0)^\mathsf T,
\]
whereas \(\rho_1^{\mathrm{cell}}=\rho_0,\ F_0^{\mathrm{cell}}=0\).
This supplies a concrete countermodel to uniqueness. The construction is a **countermodel**, not a proof that the partially open \(\chi\) state is *globally admitted* as a retained filled \(K_4\) packet under the missing closure rule. Source completeness requires an independently derived predicate favoring one of the selectors (or a different one). Q156 alone cannot choose. QED.

## THM-534-S24 — Symmetric-input deterministic gate obstruction (EXACT / NO-GO)

Let a deterministic single-valued gate selector \(\mathcal G:\mathcal X\to\{0,1\}^{E(K_4)}\) commute with vertex relabeling by \(S_4\). If initial full packet state \(X_0\) is fixed by every \(S_4\) permutation, then \(\mathcal G(X_0)\) is a uniform edge mask. If in addition the packet-state update \(\mathcal U:\mathcal X\to\mathcal X\) is deterministic and \(S_4\)-equivariant, every \(X_n\) and every \(H_n\) remains symmetric, so Q162 generates \(F_n=0\) for all n.

**Proof:** \(\mathcal G(gX_0)=g\mathcal G(X_0)\) and \(gX_0=X_0\), hence \(\mathcal G(X_0)\) is fixed by all \(g\). \(S_4\) acts transitively on six unoriented edges, so every fixed binary mask is constant. Apply the argument inductively under equivariant \(\mathcal U\). Uniform \(H_n\) implies \(B_2^\mathsf T H_nB_1^\mathsf T=0\) by \(B_1B_2=0\). QED.

**Scope:** no spontaneous deterministic symmetry breaking from a *perfectly symmetric* state in this single-valued equivariant class. Asymmetric packet inputs, boundary forcing, multivalued/stochastic dynamics, non-equivariant coupling or additional states are not excluded.

## THM-534-S25 — Finite cumulative circulation/no-persistence theorem (EXACT / NO-GO)

For the source-free closed update \(\rho_{n+1}=P_n\rho_n\), with **arbitrarily state- or history-dependent gates** \(0\le H_n\le I\), define \(D_n=\|x_n\|_2^2\). Then
\[
\boxed{\quad
\|F_n\|_2^2\le4\|j_n\|_2^2\le D_n-D_{n+1},\qquad
\sum_{n=0}^{N-1}\|F_n\|_2^2\le D_0-D_N\le D_0.\quad}
\]
In particular, \(\|F_n\|_2\to0\) as \(n\to\infty\).

**Proof:** By Q162 and \(0\le H_n^2\le H_n\),
\[
\|j_n\|^2=\tfrac1{16}x_n^\mathsf TB_1H_n^2B_1^\mathsf Tx_n
\le\tfrac14 x_n^\mathsf T(I-P_n)x_n.
\]
As in S18, \(P_n\) is symmetric with \(0\le P_n\le I\); therefore
\[
D_n-D_{n+1}=x_n^\mathsf T(I-P_n^2)x_n
\ge x_n^\mathsf T(I-P_n)x_n.
\]
The unit-metric filled tetrahedron has \(\|B_2^\mathsf T\|_{\mathrm{op}}=2\), so \(\|F_n\|^2=\|B_2^\mathsf Tj_n\|^2\le4\|j_n\|^2\). Combine and telescope. Summability of nonnegative \(\|F_n\|^2\) implies termwise convergence to zero. QED.

**Critical conclusion:** even gate changes chosen adversarially on every step cannot sustain finite nonzero circulation forever **without a source** within this exact closed, relaxational Q162 model. It is not a no-go for other generators, reversible dynamics, boundary pumping, physical magnetic fields or different metrics.

## THM-534-S26 — Necessary compensating source budget (EXACT CONDITIONAL)

Add a separately declared signed vertex source \(s_n\), constrained by \(\mathbf1^\mathsf Ts_n=0\), to obtain \(\rho_{n+1}=P_n\rho_n+s_n\); the source must also preserve \(\rho_{n+1}\ge0\) in any claimed admitted trajectory. Let \(W_n=2\langle P_nx_n,s_n\rangle+\|s_n\|^2\). Then
\[
D_{n+1}-D_n\le-\|F_n\|^2+W_n,\qquad
\sum_{n=0}^{N-1}\|F_n\|^2
\le D_0-D_N+\sum_{n=0}^{N-1}W_n.
\]
**Proof:** expand \(\|P_nx_n+s_n\|^2\), use S25 and telescope. QED.
A persistently nonzero **mean-square** face circulation therefore requires cumulative source work in this \(D\)-variance account; merely reassigning edge gates cannot provide it.

**Explicit controlled driver (not a native packet source):** hold the local selector of S23 fixed and start from \(\rho_0=(1,0,0,0)\). One Q162 attempt produces \(P\rho_0=(1/2,1/4,1/4,0)\) and \(\|F_0\|^2=1/8\). Supply
\[
s=\rho_0-P\rho_0=(\tfrac12,-\tfrac14,-\tfrac14,0).
\]
Then \(\rho_{n+1}=\rho_0\) for every step; \(D_0=3/4\), \(D(P\rho_0)=1/8\) and \(W=5/8\) pay the precise variance deficit. This is an externally **specified internal-stock redistribution**, not an earned physical pump, source of energy, radiation law or independent proof of persistent physical curvature.

## THM-534-S27 — Vertex receipt does not identify total circulation (EXACT / NO-GO)

On the filled \(\Delta^3\), \(\mathrm{im}B_2=\ker B_1\) has dimension three. Any vertex source \(s\) with \(\mathbf1^\mathsf Ts=0\) admits many signed edge routes \(k\) satisfying \(B_1k=s\). In particular \(k'=k+B_2y\) has the same vertex source but a different face circulation:
\[
B_1k'=B_1k,\qquad B_2^\mathsf Tk'=B_2^\mathsf Tk+B_2^\mathsf TB_2y.
\]
For S26's explicit driver, \(k=-j_B\) cancels *all* total edge/face current, while \(k'=-j_B+B_2e_{012}\) preserves exactly the same vertex burden updates but adds nonzero cyclic face circulation. Thus total vertex stock conservation **does not identify the routed current or physical holonomy**. A separate source-route law and readout are indispensable. QED.

## THM-534-S28 — Fixed nonuniform mask may persist while curvature decays (EXACT CONDITIONAL)

Freeze the candidate local selector of S23 as a *boundary/closure state hold* (not a derived \(\chi,b\) update). The active subgraph is the triangle on vertices 0,1,2 plus isolated vertex 3. The fixed \(P\) has spectrum \(\{1^{[2]},(1/4)^{[2]}\}\), and for the displayed \(\rho_0\),
\[
\boxed{F_n=4^{-n}(0,\tfrac14,\tfrac14,0)^\mathsf T,\qquad \|F_n\|^2=\tfrac1{8\cdot16^n}.}
\]
An indefinitely nonuniform hard mask therefore does **not** imply persistent circulating burden under Q162. Proof: diagonalize the complete active \(K_3\) Laplacian and note that its nonconstant directions contract by \(1/4\) per iteration; the face map is linear. QED.

## Exact/finite checks and governance

**[Reproducibility script](verify_thm534_gate_selection_v0_8.py):** exact signed chain identities and two-selector S23 witness; both candidate selectors tested for all 24 \(S_4\) relabelings; S24 edge transitivity; S28 exact 8-step \(4^{-n}\) check; all 64 binary masks checked via exact eigenvalues for positivity of the *S25 circulation budget matrix* \(I-P_H^2-\mathcal F_H^\mathsf T\mathcal F_H\succeq0\), \(\mathcal F_H=-\tfrac14B_2^\mathsf THB_1^\mathsf T\); exact source/route ambiguity witness; 16 numerical state paths ×256 steps with fixed or randomized masks. Constructor-local PASS. This is **not** non-constructor review, and the numerical mask changes are diagnostic *controls*, not native gate dynamics.

**AUTO_LOCK (scoped mathematics):** S23 nonidentifiability, S24 homogeneous equivariance obstruction, S25 finite cumulative circulation bound/no-persistence, S26 algebraic source budget, S27 route ambiguity, S28 fixed-mask decay, under their declared assumptions.
**AUTO_FREEZE:** assertions that Q156 already supplies a unique state-to-gate predicate; that Q162 source-free relaxation sustains stationary nonzero face circulation; that normalized vertex burden equals physical stress-energy; that \(B_2^\mathsf Tj\) equals covariant nilpotency defects or physical electromagnetic curvature; that the externally supplied source in S26 is automatically admitted by UD; and that this settles historical THM-534 probabilities.
**OPEN_GATED:** primitive \(\chi,\beta,\tau\) domain/update and true closure admissibility of S23's countermodel state; predictive h-state mapping and its support/face transition receipts; endogenous nonzero route/pump with physically calibrated stock, action and units; holonomy conversion and 6-edge observable/renewal dynamics. Physical promotion **0**.

**Next decisive criterion:** before promoting any nonuniform mask, an independent current UD packet rule must admit that exact local state/closure configuration and provide its gate transition history. Before promoting persistent curvature, a compensating source-route/current and reservoir receipt must pass, not merely a one-step mask example.
