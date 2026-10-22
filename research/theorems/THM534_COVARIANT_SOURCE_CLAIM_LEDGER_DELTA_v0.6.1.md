# THM-534 claim/dependency ledger delta — covariant-source programme v0.6.1

**Date:** 2026-10-21 | **Parent ledger:** UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39 (read-only historical baseline) | **Repository:** ud-tetra/UD | **Lane:** Development, no registry entry | **CRL gate:** constructor checked only; non-constructor adversarial review PENDING | **Physical promotion:** 0.

This is an **append-only claim/dependency amendment**. It does not overwrite any v0.39 coefficient record, historical THM-534 assertion or prior frozen negative result. The original THM-534 microscopic event law and probability selection remain SOURCE-BLOCKED.

| New claim | Object / conclusion | Proof scope | Classification | Dependencies | Reopening gate |
|---|---|---|---|---|---|
| S10a | \(F_\downarrow=B_1N_z,\ F_\uparrow=N_zB_3\); norms \(2|z-1|^2,\ |z-1|^2\) | filled \(\Delta^3\), one marked incidence, unit simplicial metric | EXACT CONDITIONAL | v0.5 S5–S7, signed \(B_k\) | none inside declared carrier |
| S10b | minimizer \(z=(3+ij)/\sqrt{9+j^2}\) | **postulated** \(U-j\sin\phi\), signed dimensionless \(j\) | EXACT CONDITIONAL / CANDIDATE source | S10a; *not* frozen UD action | derive source coupling/normalization from actual primitive |
| S11 | Cayley full-chain unitary update and antisymmetric local squared-amplitude flux | skew \(15\times15\) \(A_{z_n}\), finite real step | EXACT CONDITIONAL | typed \(N_z\), unit chain metric | separately derive physical packet burden/source ledger |
| S12 | \(q_n=2\operatorname{Im}(\bar\psi_e q\psi_f)\) produces nonzero \(z_n\) for complex state, while real-state sector remains flat | marked seam, proposed phase quadrature, selected response functional | CANDIDATE / finite NUMERICAL | S10/S11 | native marked-incidence and phase/burden law |
| S14 | phase quadrature is not same as norm-conservation current | exact two-component witnesses | EXACT / NO-GO | distinct real/imag observables | none; do not conflate again |
| S15 | magnitude-only source cannot select sign of phase quadrature | phase conjugation symmetry, no extra orientation input | EXACT / NO-GO | amplitude-magnitude-only assumptions | add independently sourced orientation/boundary register |
| S16 | defect square \(B_1F_\uparrow=F_\downarrow B_3\) | any compatible typed matrices | EXACT CONDITIONAL | associativity of \(B_1NB_3\) | physical Bianchi/source law separate |
| S17 | \(|q_n|\le\|\psi_n\|^2=M\); if \(M=1\), \(|\arg z|\le\arctan(1/3)\) | candidate quadrature, unit norm, chosen response function | EXACT CONDITIONAL | S10/S11/S14; AM–GM | packet action and physical normalization still open |

## Explicit distinctions
- \(N_z:C_2\to C_1\) is a *covariant candidate coupling*; original \(B_2\) remains nilpotent with adjacent topological \(B_1,B_3\).
- \(F_\downarrow\in \mathrm{Hom}(C_2,C_0)\) and \(F_\uparrow\in\mathrm{Hom}(C_3,C_1)\) are **nilpotency-defect receipts**, not independent physical curvature tensors or energies.
- \(U(z)=\frac12(\|F_\downarrow\|_F^2+\|F_\uparrow\|_F^2)\) is a **structural norm diagnostic**; \(-j\sin\phi\) is an unproved constitutive coupling.
- \(\|\psi\|^2\) is a conserved finite-dimensional *amplitude content*. It is neither an independently established UD packet burden \(\rho\) nor a Born probability.
- \(q^\mathrm{quad}\) is the imaginary phase quadrature. The conserved-amplitude flux is a real-part midpoint bilinear \(J_{a\leftarrow b}\). The two are not interchangeable.
- Scalar burden magnitude alone cannot select the sign of \(q^\mathrm{quad}\) without an oriented input. A nonzero source/curvature *model* therefore exists, but physical source selection remains OPEN.

## Verification and exposure
- [v0.6 exact source/Cayley verification](verify_thm534_covariant_source_v0_6.py): exact SymPy phase minimizer, rational \(j=4\) receipts \(8/5+4/5\), full Cayley unitarity, all 15 local flux identities, S16 defect compatibility.
- [v0.6 endogenous feedback check](verify_thm534_endogenous_phase_v0_6.py): 30 numerical time steps, max local residual \(6.11\cdot10^{-16}\), ten-step real flat control.
- [v0.6.1 typing counterexamples](verify_thm534_quadrature_flux_typing_v0_6_1.py): 3 exact counterexample gates.
- [v0.6.1 stress check](verify_thm534_source_norm_bound_v0_6_1.py): 70 × 15 finite runs, 3 step sizes, \(\|\psi\|^2\) and local flux residual checks. Analytic bound independently proven, not inferred from finite samples.

Historical THM-534 transport weights were seen before the present choice of candidate source functional. **Confirmatory, target-blind status: NOT EARNED.** Independent non-constructor adversarial replay absent. Other paths remain viable: a separately sourced signed packet current, boundary event, new metric, nontrivial transport carrier, or explicit open-system burden exchange. Do not promote numerical agreement, invariant norm, or a current definition to a physical theory.
