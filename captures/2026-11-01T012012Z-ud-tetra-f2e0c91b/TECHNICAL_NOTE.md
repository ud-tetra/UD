# Unified Dynamics — O09 harmonic admission and triangulation-covariance gate v0.1

**Source date:** 2026-10-31 (America/Chicago).  **Research lane:** DEVELOPMENT / NO REGISTRY ENTRY.  **Physical promotion:** **0**.  **Claim types:** EXACT (scoped homology, loop periods, source-representative obstruction, event-step bounds); DERIVED / CONDITIONAL (candidate cotangent action and work bank); NUMERICAL (independent eigenvalue diagnostics); NO-GO (source-identifiability and naive transfer covariance); OPEN (source-selected O09 zero-mode dynamics, physical readout).  All results are constructor-checked only; non-constructor review pending.

## 1. Question and source hierarchy

Previous exact work produced a 24-tetrahedron, face-connected triangulated solid torus with one harmonic edge mode. Two triangulations have the same first Betti number but different harmonic squared norms in their separately declared *unit oriented-simplex Euclidean* metrics. A previous **postulated** transfer `x' = Ax + P_H j_B` generated a lasting harmonic amplitude after a transient Q162 burden source, but did not derive this transfer from O09.

**Current source record**: recovered UD coefficient ledger `library_LEDGER_v0.85.json` (retrieved from the public UD ledger recovery on 2026-10-31; its inherited scientific revision field says `v0.43`). Its **O09** is the temporally additive history-to-Hodge map

\[
\mathcal I_{\rm lift}=\frac12\sum_{\omega>0} a_{\omega}\,\Delta\widetilde\phi_{\omega},
\qquad \mathcal I_{\rm closed}=\pi\sum_{\omega>0}n_{\omega}a_{\omega}.
\]

O09 is `NOT_A_COEFFICIENT`, and *as written* only sums over positive frequencies. It does not specify a local edge-phase Hamiltonian, zero-frequency canonical variables, photon readout or source-to-harmonic coupling. **G05** (previously proposed universal loop-action scalar) remains `AUTO_FREEZE` as a current mainline universal coefficient. **Q140** supplies the exact mathematical holonomy cost, not a physical gauge coupling. **Q153** is a continuity/source-receipt grammar with constitutive burden-current components still open; **Q162** admits a scoped relaxation model `j_B=-(1/4)D_h B_1^T b`, not an O09 phase-current source.

Sources and associated earlier draft PRs: `https://unified-dynamics-public.ben-w-mayes.chatgpt.site/evidence/ledger-recovery/`; previous conserved-source gate `https://github.com/ud-tetra/UD/pull/478`; previous glued-harmonic theorem `https://github.com/ud-tetra/UD/pull/486`. The historical uploaded v0.39 ledger is not silently declared current over the recovered v0.85 content.

The two authorized tasks were: **(1)** derive or rule out a normalized O09 zero-mode action/source with work accounting; **(2)** test triangulation covariance and event-step stability on both face-connected 24-tetrahedron tori. No astronomical or laboratory target was used to construct or choose parameters.

## 2. Mathematical objects and geometric normalization

Let \(K_A,K_B\) be the two simplicial complexes obtained from a four-sector triangulated annulus multiplied by an interval, with the annulus quadrilateral diagonals flipped between the two versions. Each consists of 24 unique tetrahedra, with chain dimensions

\[
(f_0,f_1,f_2,f_3)=(16,56,64,24),\quad
(r_1,r_2,r_3)=(15,40,24),\quad
(\beta_0,\beta_1,\beta_2,\beta_3)=(1,1,0,0).
\]

Write \(B_k:C_k(K;\mathbb Q)\to C_{k-1}(K;\mathbb Q)\) for increasing-vertex oriented incidence; \(B_{k-1}B_k=0\). On real edge cochains with the **chosen unit metric**, the harmonic space is

\[
\mathcal H^1(K)=\ker B_1\cap\ker B_2^{\mathsf T},\qquad\dim \mathcal H^1=1.
\]

Define a specific oriented reference one-cycle \(\gamma_0=(0,1,2,3,0)\). Let \(c_K\) be the integer closed edge cochain that counts signed steps between adjacent residue classes \(v\bmod4\), with \(B_2^{\mathsf T}c_K=0\) and \(\langle\gamma_0,c_K\rangle=4\). The unique unit-metric harmonic representative \(h_K=c_K-B_1^{\mathsf T}v_K\) is obtained by solving \(B_1 B_1^{\mathsf T}v_K=B_1c_K\) with one vertex potential fixed. It obeys

\[
B_1h_K=0,\quad B_2^{\mathsf T}h_K=0,\quad \langle\gamma_0,h_K\rangle=4.
\]

**Theorem H1 (EXACT, fixed generator and orientation).** The *period-normalized* harmonic cochain \(\omega_K=h_K/4\) obeys \(\langle\gamma_0,\omega_K\rangle=1\). For any flat phase \(\alpha_K=\theta\omega_K\), each triangular holonomy vanishes, while its noncontractible Wilson-loop value is exactly \(W_\gamma=e^{i\theta}\). The same number is obtained on both triangulations under the declared comparison of the fundamental loop. This is an isomorphism of their one-dimensional topological phase coordinates, **not** a selected local edge-by-edge transport operator or physical electron/photon observable.

**Counterexample to metric-independent amplitude.** The unit-simplex squared norms are

\[
\|h_A\|^2=\frac{7971126}{278293},\qquad
\|h_B\|^2=\frac{2576374}{89887},
\]

so the squared norms of \(\omega_K\) differ by the same exact ratio

\[
\frac{\|\omega_A\|^2}{\|\omega_B\|^2}=
\frac{358250301381}{358493424791}\ne1.
\]

The difference is approximately \(-0.067818\%\) relative to the second norm. **It is not evidence of a physical fine-structure, lepton, cosmology or instrument-correction mechanism.** It is a controlled difference between *two metric conventions on different triangulations*. Geometry preserves the period but does not force a metric-dependent energy or oscillator frequency to match.

## 3. What action can be admitted from O09?

**Theorem H2 (NO-GO, source identifiability).** The source-defined O09 functional has summation index \(\omega>0\), so does not contain the harmonic \(\omega=0\) degree of freedom or an associated source/kinetic term *as written*. Neither the exact topological period nor Q153 continuity selects an extra zero-mode Hamiltonian or its numerical action scale. To prove underdetermination construct two different, internally consistent extensions of the *same* positive-frequency O09 part, one with no harmonic topological term and another with a freely parameterized canonical pair. The original O09 data are unchanged by the extension.

A **CANDIDATE** (additional, not O09-derived) canonical lift uses a compact angle \(\theta_n\in S^1\) with a consistently chosen local lift on each history increment, conjugate momentum \(p_n\in\mathbb R\), a dimensionless internal step \(h>0\), a freely chosen positive inertia \(I\), a source amplitude \(J_n\), and an externally given phase reference \(\chi\):

\[
S_{\rm top}=\sum_n\left[p_n(\theta_{n+1}-\theta_n)-h\left(\frac{p_n^2}{2I}-J_n\cos(\theta_n-\chi)\right)\right].
\]

The exact discrete first variations give

\[
\theta_{n+1}-\theta_n=h\frac{p_n}{I},\qquad
p_n-p_{n-1}=-hJ_n\sin(\theta_n-\chi).
\]

Here \(I\), \(J_n\), \(\chi\) and the action/physical time units are *not* derived by O09. Even if \(J_n=0\), choosing two different \(I\) values gives different phase drift for the same \(p\), while leaving all O09 positive-mode data untouched. No automatic physical clock follows. The angular local lift and winding-sector bookkeeping are part of this extra canonical contract.

For the continuum-parameter Hamiltonian \(H=p^2/(2I)-J(s)\cos(\theta-\chi)\), the canonical equations give the exact work identity

\[
\frac{dH}{ds}=-\dot J(s)\cos(\theta-\chi).
\]

A donor stock can close the mathematical balance if \(\dot E_D=+\dot J\cos(\theta-\chi)\). It is nonnegative **only if** its starting stock and the total variation of \(J\) fund it (sufficient condition \(E_D(0)\ge\int|\dot J|\,ds\)). The donor is **newly supplied**, not extracted from the native O09 action.

**Typed map conclusion:** The period normalization uniquely coordinates the *topological flat phase* on each chosen homology generator. It does not uniquely normalize its canonical momentum, kinetic form, burden-to-phase coupling, work donor or physical measurement scale.

## 4. Failure of the earlier unselected projected-pump under triangulation changes

In the earlier *conditional* one-edge hard-gate example, one prescribed burden impulse was

\[
j_B(s)=-\tfrac14 e^{-s/2}e_{01},
\qquad F_K(s)=g P_{\mathcal H,K}j_B(s),
\]

where \(g\) is an **undetermined** transfer coefficient and \(P_{\mathcal H,K}=h_Kh_K^{\mathsf T}/\|h_K\|^2\). An initially empty protected mode acquires \(\alpha_K(\infty)=a_Kh_K\) with

\[
a_K(\infty)=-\frac{g(h_K)_{01}}{2\|h_K\|^2},\qquad
\theta_K(\infty)=-\frac{2g(h_K)_{01}}{\|h_K\|^2}.
\]

With \(g=1\) as a **test convention, not a fitted native law**:

\[
\theta_A=-\frac{104806}{1328521},\quad
\theta_B=-\frac{99415}{1288187},\quad
\theta_A-\theta_B=-\frac{2934811507}{1711383481427}\ne0.
\]

**Theorem H3 (NO-GO under this transfer rule).** Fixing the same one-edge impulse, same unit transfer coefficient and same unit simplex metric on each triangulation fails to produce identical final *global loop phase*. This is a counterexample to universal triangulation covariance of that supplied metric-projection pump. No statement about measured photons follows. One may declare additional metric/coupling transport, but must prove its source and invariance before adopting it.

## 5. A failed tempting repair: directly integrate the source around a loop

Define three homologous cycles \(\gamma_0=(0,1,2,3,0)\), \(\gamma_8=(8,9,10,11,8)\), and \(\gamma_4=(4,5,6,7,4)\) in each triangulation. Exact boundary solves verify \([\gamma_0]=[\gamma_8]=[\gamma_4]\in H_1(K;\mathbb Q)\). The flat cocycle has \(\oint_\gamma c_K=4\) for all three. But the bare Q162 single-edge impulse cochain \(j=-e_{01}/4\) has \(B_2^{\mathsf T}j\ne0\), and thus

\[
\left(\oint_{\gamma_0}j,\oint_{\gamma_8}j,\oint_{\gamma_4}j\right)=(-1/4,0,0).
\]

**Theorem H4 (NO-GO for unsourced loop evaluation).** A nonclosed source 1-cochain does not in general define a homology-class functional. The loop integral depends on the representative, even when the loops are homologous. Therefore the alternative *candidate* driving law \(\dot\theta=g\oint_\gamma j_B\) is not topologically canonical without selecting an exact loop representative or adding a source rule producing an appropriately closed/cohomologically transported source.

For a deliberately fixed \(\gamma_0\), this extra drive can be integrated exactly: \(\theta(s)=-g(1-e^{-s/2})/2\), independent of A or B **on that named-loop fixture only**. With a further *chosen* global quadratic store \(E_\theta=\theta^2/2\), burden release \(\Delta E_B=(1-e^{-s})/4\) and bank \(E_D=\Delta E_B-E_\theta\), the bank is nonnegative for \(g^2\le2\). At chosen \(g=1\) the late-time receipt is \(E_\theta=E_D=1/8\). This is an existence control, neither a source-derived coupling nor a homology-independent current nor a physical energy conversion.

## 6. Stable discrete event-step test on both carriers

Q162 supplies a relaxational **continuous** law on the K4 normalization, \(\dot b=-\frac14L_0 b\), with \(L_0=B_1B_1^{\mathsf T}\). The prior blanket **discrete** step \(b_{n+1}=(I-L_0/4)b_n\) was unstable on both solid-torus graphs because a degree-nine vertex implies \(\lambda_{\max}(L_0)\ge9\) and hence an eigenvalue at most \(-5/4\).

For any simple finite graph with maximum vertex degree \(d_{\max}>0\), the algebraic spectral bound \(0\le\lambda(L_0)\le2d_{\max}\) gives an explicitly **stable numerical substep**, not a physical clock:

\[
M=I-\frac{L_0}{2d_{\max}},\qquad 0\le\operatorname{spec}(M)\le1.
\]

It is entrywise nonnegative, symmetric and doubly stochastic, conserving \(\sum_i b_i\) and contracting unweighted Euclidean burden contrast. Relative to Q162's chosen rate \(1/4\), this corresponds to an internal Euler substep \(\Delta s=2/d_{\max}\). Both tested graphs have \(d_{\max}=9\), so \(M=I-L_0/18\) and \(\Delta s=2/9\). This is one **sufficient** stability choice; source-selected event duration and metric remain OPEN.

**Theorem H5 (EXACT stable but not covariant).** Both A and B have positive nonoscillatory spectra for their respective \(M\), and preserve total burden, but one step from the same labeled vertex stock \(b_0=e_0\) gives *different* coarse four-sector sums when vertices are grouped by \(v\bmod4\):

\[
C M_A e_0=(2/3,\;2/9,\;0,\;1/9),\qquad
C M_B e_0=(2/3,\;1/9,\;0,\;2/9).
\]

The chosen coarse bin map \(C\) is an explicit **test readout**, not a native UD macroscopic observer. Stability is not triangulation covariance. Any physical comparison requires a selected cross-triangulation transfer and compatible metric/observer contract. An implementation can satisfy mathematical continuity, geometry and nonnegative event stocks without being physically equivalent to a different discretization.

## 7. Decisions, review gates, and correspondence limits

| ID | Claim | Status | Admission boundary |
|---|---|---|---|
| H1 | Flat loop period and Wilson phase identical on A/B | EXACT on named loop | No physical photon phase |
| H2 | O09 does not identify harmonic-sector inertia, source or coupling | NO-GO for unique derivation from current source | A new source-level extension could reopen |
| H3 | Metric-projection one-edge pump fails equal-loop-phase test | NO-GO for this selected convention | A native metric/intertwiner or coupling transport is needed |
| H4 | Bare loop integral of nonclosed Q162 flux depends on homologous loop representative | NO-GO for topological source identity | Need closed source or admissible cohomology-history map |
| H5 | Degree-bounded event substep is stable but produces different coarse outcomes | EXACT / CONDITIONAL | The step is a chosen numerical integrator, not a physical time law |
| H6 | Canonical cotangent and donor Hamiltonian extensions are mathematically consistent | DERIVED / CANDIDATE | Inertia, action units, donor and source normalization OPEN |

**Decision:** AUTO_LOCK only the scoped algebraic/combinatorial statements after constructor verification; no registry theorem promotion without non-constructor review. AUTO_FREEZE as native any assertion that Q162 alone loads \(H^1\), that the previous unit-coefficient harmonic projection is triangulation-covariant, or that a named-loop integral of nonclosed j is a canonical homology source. Retain all narrower valid results.

**What would reopen the bridge:** A source-level O09-to-zero-mode extension with explicit carrier map, normalized kinetic form, admissible closed or transported source cochain, donor/work accounting, and proof that the chosen observable commutes with history transfer on A and B. Then impose independent readout and uncertainty protocols and preregister the eventual physical experiment. No physical promotion until the specific bridge passes.

## 8. Verification instructions

Fresh from-scratch reproducible programs:

```bash
python exact_models.py
python loop_source_gate.py
python action_extension.py
python independent_numeric.py
```

- `exact_models.py`: two rational incidence/Hodge computations, exact loop phases, conditional pump and unit-metric obstruction, 1/18 updates and four-sector reports; writes `EXACT_RECEIPT.json`.
- `loop_source_gate.py`: exact three-loop homologous boundary witnesses and nonclosed flux counterexample; writes `LOOP_SOURCE_RECEIPT.json`.
- `action_extension.py`: symbolic discrete Euler equations, alternative inertia and compact Hamiltonian donor identity, named-loop conditional work bank; writes `ACTION_RECEIPT.json`.
- `independent_numeric.py`: independently constructs both complexes, verifies modular ranks over primes 2,101,1009, floating harmonic/nullity and stable update, writes `INDEPENDENT_RECEIPT.json`. Its floating calculation is corroboration, not exact proof.

**No source target exposure**: No lab constants, measured cosmological redshift, fine-structure value, lepton ratios or instrument residual were used to select the carrier, current, coefficient, step or acceptance rule.
