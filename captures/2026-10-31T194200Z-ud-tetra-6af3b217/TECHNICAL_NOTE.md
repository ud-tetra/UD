---
title: "Unified Dynamics: O09 Burden-to-Phase Source Identifiability Gate"
subtitle: "Cut/cycle projection, fixed and switching-gate no-go, and discrete event receipts"
author: "UD development analysis — constructor-side review only"
date: "31 October 2026 · v0.1"
lang: en-US
---

**RESULT.** `NO-GO` for deriving a nonzero, normalized, persistent phase-current coupling **solely** from the currently recovered O09 history action plus source-continuity and Q162 relaxational burden-mixing laws. A unique **metric-relative cycle projection** of the admitted burden flux can be calculated, but adoption as a phase source is **OPEN_GATED**. Under declared source-free continuous or discrete burden updates, its long-time mean-square circulation is zero, even with gate switching. A lower-order K4 cubic source shape remains valid **conditionally** but is not dynamically selected. **Physical promotion: 0.**

## 1. Sources, version precedence, and typed boundary

**S1 — current recovered ledger.** `library_LEDGER_v0.85.json`, recovered 21 October 2026 (filename version v0.85; inherited scientific revision v0.43); immutable portal: <https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json>. Its rows relevant here are:

- **O09** `I_loop->Hodge`: the current lifted Hodge loop-history action map,
  \(\mathcal I_{\rm lift}=\frac12\sum_{\omega>0}a_\omega\,\Delta\widetilde\phi_\omega\), with closed history \(\pi\sum n_\omega a_\omega\). **No** local link-phase Hamiltonian, burden-to-modal amplitude source, or edge-phase intertwiner is supplied. Physical action units downstream via G06 remain open.
- **G05:** historical universal scalar loop coefficient **retired from mainline**, with restricted reuse contingent on a new sufficiency theorem. It cannot normalize a new phase-current interaction by historical symbol reuse.
- **Q140:** \(\delta_U(U)=1-\operatorname{ReTr}(U)/d\) is a dimensionless loop mismatch statistic, **not** a current, rate or action coefficient.
- **Q153–Q155:** incidence burden continuity, regional in/out/source/sink balance, and gross redistribution receipts are structural. They do not select an arbitrary solenoidal edge flux.
- **Q156:** hard gate \(h_e=C_{\rm cl}^{\rm hard}T_{\rm int}^{\rm hard}\); smooth conductance law is open.
- **Q162:** scoped *relaxational* burden mixing, \(j_{B,e}^{\rm mix}=-\frac14h_e(B^{\mathsf T}b)_e\), and its next gate is protected-mode projection and physical clock.
- **Q163:** a separately normalized relaxation model with decay \(4/3\) per its own internal parameter. **Do not** substitute that rate into the Q162 calculation.

**S2 — archived source.** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, 22 August 2026, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`. Its earlier G05 status is retained for provenance, but not preferred over the recovered v0.85 repair. S1 and S2 agree on the Q162 scoped formula.

**S3 — previous scoped theorem.** `UD_O09_CUBIC_CURRENT_GATE_v0.1`, 31 October 2026, SHA-256 of prior ZIP `7def5fd8a7e9fee1addf09f8ee9bf74a3af946f98df85823485cbefc808c4ce7`, corresponding draft [PR #472](https://github.com/ud-tetra/UD/pull/472). It proves the first nonzero fully \(S_4\)-equivariant polynomial map from *one scalar vertex field* to an oriented K4 edge cycle appears at degree three, with \(J_{\rm cub}(b)=B_2t(b)\). This remains a theorem about eligible **shape**, not physical activation or magnitude.

**Typing.** The present test supplies an identification of Q162's scalar burden sites with the four vertices \(b\in C_0(\Delta^3;\mathbb R)\). Edge flux \(j_B\in C_1\), phase \(\alpha\in C^1(\Delta^3;\mathbb R/2\pi\mathbb Z)\), co-closed edge-cycle \(Z\subset C_1\), and O09 modal phases \(\widetilde\phi_\omega\) remain **different objects**. No map between \(j_B\) and a variation of \(\alpha\) is imported. All rates below use a dimensionless internal evolution parameter or counted event index, not SI seconds.

## 2. Exact K4 Hodge decomposition

With ascending edge orientation \(01,02,03,12,13,23\), let \(B_1:C_1\to C_0\) be the ordinary incidence and \(B_2:C_2\to C_1\) the face incidence. Standard boundary closure gives \(B_1B_2=0\). For the connected tetrahedral graph,

\[
 B_1B_1^{\mathsf T}=4I_4-\mathbf1_4\mathbf1_4^{\mathsf T},\qquad
 P_Z=I_6-\frac14B_1^{\mathsf T}B_1=\frac14B_2B_2^{\mathsf T}.
\]

**Theorem A (EXACT).** \(P_Z\) is the Euclidean orthogonal projector onto \(Z=\ker B_1=\operatorname{im}B_2\), \(\dim Z=3\). For any edge vector \(j\), \(P_Zj\) is the unique \(z\in Z\) minimizing \(\|z-j\|^2\). Proof: \(P_Z^2=P_Z=P_Z^{\mathsf T}\), \(B_1P_Z=0\), and \((I-P_Z)j\perp Z\). This is a **metric-relative least-squares theorem**, not selection of a physical phase coupling.

Insert the declared Q162 burden-flux law, with \(0\le h_e\le1\) on a fixed K4:

\[
 j_B=-\frac14D_hB_1^{\mathsf T}b,\quad D_h=\operatorname{diag}(h),\quad
 J_Z^{\rm proj}:=P_Zj_B=-\frac14P_ZD_hB_1^{\mathsf T}b. \tag{1}
\]

**Theorem B (EXACT / CONDITIONAL).** If all six gates have the same scalar value \(h_e=c\), then \(J_Z^{\rm proj}=0\). In particular, all-open Q162 transport is pure gradient and cannot supply a nonzero edge-cycle source. The coefficient \(1/4\) in (1) remains a *relaxational flux normalization*: it is **not** an action unit, photon interaction, Wilson face-stiffness coefficient or O09 coupling.

A direct link-phase source \(-\alpha^{\mathsf T}j_B\) would also fail infinitesimal gauge invariance in general: under \(\alpha\mapsto\alpha+B_1^{\mathsf T}\chi\), its variation is \(-\chi^{\mathsf T}B_1j_B\), typically nonzero. Projecting onto \(Z\) removes this infinitesimal gauge obstruction, **but** a linear link-angle interaction is not globally periodic on a compact \(U(1)\) carrier. A truly compact gauge-invariant action needs a separate periodic construction and its own normalization.

## 3. Identifiability no-go for the O09 source

**Theorem C (NO-GO / sources S1–S2 as written).** O09 plus the burden continuity identity alone does not determine a unique local phase current, its amplitude or its temporal persistence.

**Proof 1 (missing typed derivative).** O09 specifies the modal history 1-form in variables \(a_\omega,\widetilde\phi_\omega\); it provides neither \(\alpha=T(\widetilde\phi)\) nor \(a=a(b,\alpha)\) nor a source-selected Hamiltonian. Consequently \(\delta\mathcal I_{\rm O09}/\delta\alpha\) is not a defined source-native object. As an *added* independent-variable discrete variational interpretation, \(S_{09}=\frac12\sum_{n,\omega}a_{n\omega}(\phi_{n+1,\omega}-\phi_{n\omega})\) gives only \(a_n-a_{n-1}=0\) and \(\phi_{n+1}-\phi_n=0\) when both variables vary freely in the interior. Appending a Hamiltonian \(H\) changes both equations; O09 alone does not select \(H\).

**Proof 2 (continuity-null directions).** For the general Q153 continuity equation \(\dot b=B_1j+s_B\), any \(z\in\ker B_1\) obeys \(B_1(j+z)=B_1j\). In particular \(j^{(\lambda)}=j_B^{\rm mix}+\lambda J_{\rm cub}(b)\) yields the same vertex burden history for every \(\lambda\). This is a family of possible **additional protected flux lanes**: it does **not** reclassify Q162's specifically normalized relaxation current as arbitrary. Q155's gross-current receipt can measure distinctions between these choices after a choice is made, but supplies no constitutive selection rule or measured target value. Hence continuity by itself cannot determine \(\lambda\).

**Proof 3 (explicit action countermodels).** The same canonical O09 1-form can be completed by Hamiltonians \(H_0\) and \(H_\lambda=H_0-\lambda\sum_f t_f(b)\sin\Phi_f\) with \(\Phi=B_2^{\mathsf T}\alpha\), without changing the O09 1-form. The two give different gauge-conserving phase force laws for generic \(b\), while the burden continuity identity can be maintained with separately declared transport. These are **CANDIDATE completions**, not mainline equations; their existence demonstrates that O09 does not determine \(\lambda\) without additional source information. The earlier scalar G05 is retired and cannot fill the gap.

## 4. Exact 64-hard-gate current audit

Take the explicitly declared fixture \(b=(0,1,2,3)^{\mathsf T}\); the old theorem gives \(J_{\rm cub}=(8,4,-12,4,4,8)^{\mathsf T}\). Enumerate all \(2^6=64\) binary hard gates in edge order \((01,02,03,12,13,23)\). Exact rational calculations give:

| Gate-sweep result | Count |
|:--|--:|
| Fixed hard-gate masks | 64 |
| Connected transport graphs | 38 |
| Disconnected transport graphs | 26 |
| Masks with \(P_Zj_B\ne0\) initially | 62 |
| Masks with \(P_Zj_B=0\) initially | 2 (all-off and all-on) |
| Nonzero projected currents collinear with \(J_{\rm cub}\) at this fixture | 0 |
| Rank of the span of all nonzero projected currents | 3 |
| Masks with nonzero current at source-free fixed-gate equilibrium | 0 |

**NUMERICAL (exact finite enumeration).** These are reproducible scoped enumerations, **not** a theorem excluding every gate/burden pattern. They show that hard-gate asymmetry allows temporary circulation, but does not pick a universal direction or the earlier cubic generator at this fixture. The gated edge field is an additional carrier, so an input involving \(h\) does not violate the prior single-vertex-scalar cubic-minimum theorem.

The full 64-mask Laplacian spectra have smallest positive eigenvalue \(2-\sqrt2\) among nonempty masks, with normalized continuous relaxation rate \((2-\sqrt2)/4\); no physical time unit follows.

## 5. Source-free persistence theorem: normalized continuous branch

**Additional declared evolution rule**, not a physical clock: in a dimensionless parameter \(s\), take \(\dot b=B_1j_B\), with piecewise measurable \(h_e(s)\in[0,1]\), no \(s_B\), and \(j_B\) as in (1). The mean \(\bar b=\frac14\mathbf1^{\mathsf T}b\) is conserved. Define contrast stock \(E_B=\frac12\|b-\bar b\mathbf1\|^2\). Then

\[
 \frac{dE_B}{ds}=-\frac14\sum_eh_e(\Delta b_e)^2,\qquad
 -\frac{dE_B}{ds}-4\|j_B\|^2=\frac14\sum_eh_e(1-h_e)(\Delta b_e)^2\ge0.
\]

**Theorem D (EXACT / CONDITIONAL).** Since \(P_Z\) is an orthogonal projector,

\[
 \boxed{\int_0^T\|P_Zj_B(s)\|^2\,ds\le\frac{E_B(0)}4.} \tag{2}
\]

The long-time average squared projected current is therefore at most \(E_B(0)/(4T)\), which tends to zero. This excludes **sustained nonzero mean-square circulation** under the specified source-free relaxational update even with switching gates. It does **not** prove pointwise vanishing for arbitrary infinitely switching gate functions, nor exclude external source, a separate conserved circulation mode, nondissipative action or a changed state space.

For constant full-open gates \(D_h=I_6\), \(b_\perp(s)=e^{-s}b_\perp(0)\). The cubic form is shift invariant and degree three, hence \(J_{\rm cub}(s)=e^{-3s}J_{\rm cub}(0)\). This rate belongs only to this continuous update.

## 6. Source-free persistence theorem: discrete event branch

A **separate** completion of Q153's difference-form source law is

\[
 b_{n+1}=b_n+B_1j_{B,n},\qquad
 j_{B,n}=-\frac14D_{h,n}B_1^{\mathsf T}b_n.
\]

Let \(L_{h,n}=B_1D_{h,n}B_1^{\mathsf T}\). As \(0\preceq D_{h,n}\preceq I_6\),
\(0\preceq L_{h,n}\preceq B_1B_1^{\mathsf T}=4P_\perp\). Thus every update matrix \(M_{h,n}=I_4-L_{h,n}/4\) is positive semidefinite and nonexpansive on the burden-contrast space. Its energy decrement is exactly

\[
 E_{B,n}-E_{B,n+1}=\frac1{32}b_n^{\mathsf T}(8L_{h,n}-L_{h,n}^2)b_n
 \ge 2\|j_{B,n}\|^2\ge2\|P_Zj_{B,n}\|^2.
\]

**Theorem E (EXACT / CONDITIONAL).** For any gate-switching sequence \(0\le h_{e,n}\le1\) without other source,

\[
 \boxed{\sum_{n=0}^{N-1}\|P_Zj_{B,n}\|^2\le\frac{E_{B,0}}2.} \tag{3}
\]

Therefore the asymptotic time-averaged squared projected current also vanishes on this discrete-event branch. For all-open gates, \(M_h=\mathbf1\mathbf1^{\mathsf T}/4\), so *one discrete event* sends every vertex burden to its mean; the cubic current shape becomes zero afterward. This must **not** be conflated with the continuous exponential branch above. The update index is not physical duration.

## 7. Remaining constructive interface and no-free-scalar ruling

The only directly calculable normalized link-current *shape* from the existing Q162 flux plus unit K4 metric is \(J_Z^{\rm proj}=P_Zj_B\), unique under the explicitly chosen Euclidean least-squares principle. It is not intrinsically a compact phase interaction, and its dissipation prevents source-free persistence.

One may formally manufacture the earlier cubic current via a **new** quadratic soft-gate family \(h_{ij}(b)=c-4b_ib_j\): then \(P_Z[-\frac14D_hB_1^{\mathsf T}b]=J_{\rm cub}(b)/4\). This is an exact algebraic countermodel only; it is **not** supplied by Q156 hard gating, and it need not satisfy \(0\le h\le1\) for general \(b\). Neither its normalization nor its sign is selected by O09. No hidden universal factor has been derived.

**NO-GO DECISION:** The combined current source register (O09, Q153–Q156, Q162, Q140) does not uniquely derive a nonzero normalized, persistent burden-to-phase coupling. The allowed exact geometric projection and cubic source-shape theorem are retained. Earlier physical or electromagnetic dressing identifications stay frozen. Source-selected phase kinetic term/Hamiltonian, O09-to-link intertwiner, protected or driven burden-current source, donor/work receipt, clock/lapse, photon-compatible carrier and instrument calibration remain **OPEN_GATED**.

**Reopening condition.** Present a versioned current UD primitive/action interface specifying (i) accepted burden state and its scalar-vs-vector carrier, (ii) an equivariant, local modal-to-link phase map, (iii) a source-selected periodic coupling or variation with correct units, (iv) accounted donor and sink currents, (v) a reproducible nonzero stationary solution stable under source-free or funded dynamics, and (vi) a target-blind optical readout with null controls. The phase coupling must survive independent non-constructor review before any physical identification.

## 8. Reproduction and governance

Five standalone Python/SymPy checks constitute the local constructor verification set:

1. `check_generated.py`: generated incidence, \(P_Z\), cubic fixture, all 64 initial hard masks, continuous exact unit-gate decay, and cubic soft-gate identity.
2. `check_independent.py`: separate hard-coded boundary, O09 first variation, direct gauge variation, 64-mask cycle-span rank, and Hamiltonian-completion countermodels.
3. `check_relaxation_all_gates.py`: all 64 fixed binary Laplacian nullspaces and spectra, exact \(2-\sqrt2\) smallest positive eigenvalue.
4. `check_switching_energy_bound.py`: exact polynomial proof receipt for arbitrary \(h(s)\in[0,1]\), plus source-free cubic counterexample.
5. `check_discrete_source_update.py`: every binary-gate discrete update spectrum, exact contraction inequality and finite gate-switch sequence.

Each script produces a machine-readable receipt (except the fourth, which prints its identity); all outputs are developmental, not independent review or physical evidence. The complete release includes a source hash manifest and a separately maintained claim/dependency ledger. No previous source is overwritten; nothing here updates the public site or promotes a physical bridge.
