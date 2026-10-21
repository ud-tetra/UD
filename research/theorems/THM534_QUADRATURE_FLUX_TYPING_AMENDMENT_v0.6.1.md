# THM-534 Covariant Source Audit — Typed Quadrature/Flux Amendment v0.6.1

**Date:** 2026-10-21 · **State:** EXACT algebraic correction / CANDIDATE source map unchanged · **Versioned predecessor:** [v0.6](THM534_COVARIANT_SOURCE_CONTINUITY_v0.6.md). **Physical promotion:** 0. **Development lane; non-constructor review pending.**

## Reason for amendment
The first v0.6 proof correctly distinguishes full-chain *amplitude norm continuity* from physical retained burden. However the wording **"endogenous oriented phase-current"** for
\[
j^{(\mathrm{quad})}_{ef}:=2\operatorname{Im}(\bar\psi_e(B_2)_{ef}\psi_f)
\]
could incorrectly suggest it is the very same antisymmetric continuity **flux** as the Cayley proof. It is **not**. Reclassify this variable as a **phase-sensitive quadrature source candidate**:
\[
q^{(\mathrm{quad})}_{ef}:=2\operatorname{Im}(\bar\psi_e(B_2)_{ef}\psi_f).
\]
The local transport flux under a skew generator \(A\) is
\[
J^{n+1/2}_{a\leftarrow b}
=2h\,\operatorname{Re}(\overline{\psi^{n+1/2}_a}A_{ab}\psi^{n+1/2}_b),
\]
which is a distinct, time-midpoint, typed edge in the full 15-state amplitude graph. The two expressions are real/imaginary components of a complex coherence on potentially different time slices; equal numerical values would not make them equal objects.

## THM-534-S14 — Quadrature/flux independence (EXACT / NO-GO)

Fix any signed incidence \(r=(B_2)_{ef}\in\{\pm1\}\). Let initial amplitudes
\[
\psi_e=1/\sqrt2,\qquad \psi_f=i r/\sqrt2.
\]
Then \(q^{(\mathrm{quad})}_{ef}=1\), whereas the equal-time norm-flow bilinear
\[
j^{(\mathrm{norm})}_{ef}:=2\operatorname{Re}(\bar\psi_e r\psi_f)
\]
vanishes. Conversely take \(\psi_e=1/\sqrt2\), \(\psi_f=r/\sqrt2\), giving \(q^{(\mathrm{quad})}_{ef}=0\) and \(j^{(\mathrm{norm})}_{ef}=1\). The independent counterexamples prove that the source quadrature is **not** an already-receipted conserved burden or amplitude flux.

This does not weaken the separate **exact** Cayley continuity proof: it supplies an antisymmetric flux for any skew \(A_{z_n}\), including when \(z_n\) is selected by the candidate phase-quadrature rule.

## THM-534-S15 — Amplitude-magnitude-only source obstruction (EXACT / NO-GO)

Let a proposed source \(F\) depend only on \(\{|\psi_a|^2\}\) (and on other variables unchanged under \(\psi\mapsto\bar\psi\)), but suppose it claims to identify the **signed** quadrature \(q^{(\mathrm{quad})}_{ef}\) for every state. Complex conjugation preserves all its inputs and reverses \(q^{(\mathrm{quad})}_{ef}\). The preceding witness has \(q=\pm1\) under conjugate inputs with equal magnitudes. Thus no such \(F\) exists. QED.

**Scope:** amplitude magnitudes alone do not fix oriented phase quadrature. This does not prohibit a separately sourced orientation, boundary phase, signed packet current, handedness register, or non-even coupling to scalar burden; adding such information is a new branch requiring independent sourcing.

## Candidate response law (same mathematics, repaired nomenclature)

The v0.6 conditional constitutive response is now written
\[
z_*(q^{(\mathrm{quad})})=
\frac{3+i q^{(\mathrm{quad})}}{\sqrt{9+(q^{(\mathrm{quad})})^2}}.
\]
The curvature receipts \(\|B_1N_z\|_F^2\) and \(\|N_zB_3\|_F^2\), variational functional \(3(1-\cos\phi)-q^{(\mathrm{quad})}\sin\phi\), and total-norm Cayley identities remain unchanged mathematically. The **sine source coupling, choice of marked seam and map from UD packet variables are still CANDIDATE/OPEN**, not exact primitive derivations.

### No-go/claim audit
- **EXACT:** nonzero signed quadrature can conditionally select non-flat curvature under the **postulated** source functional.
- **EXACT:** Cayley update conserves \(\sum_a|\psi_a|^2\) and its local flux receipts.
- **NO-GO:** magnitude-only data cannot determine the orientation sign of \(q^{(\mathrm{quad})}\).
- **NO-GO:** \(q^{(\mathrm{quad})}\neq J^{(\mathrm{norm})}\) as mathematical observables; neither is proved to equal physical packet burden flux.
- **OPEN:** dynamical generation of packet signed source, boundary selection, source/covariant Bianchi receipt, physical conserved burden \(\rho\), and measurement/THM-534 transition law.
- **AUTO_FREEZE:** references to \(q^{(\mathrm{quad})}\) as an already-conserved chain flux or direct physical current.

## Reproduction
[Exact independent counterexample test](verify_thm534_quadrature_flux_typing_v0_6_1.py); constructor execution PASS on 2026-10-21 with three exact independent controls. Results preserved append-only. Physical promotion 0.


## THM-534-S16 — Compatibility of the two covariant closure defects (EXACT)

For any independently specified linear coupling \(N:C_2\to C_1\) with **fixed** original simplicial \(B_1:C_1\to C_0\) and \(B_3:C_3\to C_2\), define the typed nilpotency defects
\[
F_\downarrow=B_1N:C_2\to C_0,\qquad F_\uparrow=NB_3:C_3\to C_1.
\]
Then the following source/curvature *square-compatibility identity* holds:
\[
\boxed{B_1F_\uparrow=F_\downarrow B_3:C_3\to C_0.}
\]
**Proof:** Both sides are \(B_1NB_3\) by associativity; no assumption that \(B_1N=0\) or \(NB_3=0\) is required. For a single marked incidence \(N_z=B_2+(z-1)q|e\rangle\langle f|\), both sides are explicitly \((z-1)q(B_3)_f B_1|e\rangle\), nonzero for \(z\ne1\). QED.

**Typing:** This is a *commuting defect square*, not a proof of a covariant Bianchi identity, dynamic curvature propagation, divergence-free physical stress-energy or conserved packet burden. It prevents treating the lower and upper nilpotency defects as unrelated bookkeeping entries, but its equality alone cannot select \(z\), construct a current, or derive \(T\).

**Independent constructor check:** \(B_1(N_zB_3)=(B_1N_z)B_3\) verified symbolically in the v0.6 exact script (additional control), and independently follows from matrix associativity. Physical promotion 0.
