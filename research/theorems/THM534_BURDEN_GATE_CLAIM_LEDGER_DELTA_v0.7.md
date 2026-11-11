# THM-534 v0.7 claim/dependency delta — native gated burden-current bridge

**Date:** 2026-10-21 | **Predecessor:** THM534_COVARIANT_SOURCE_CLAIM_LEDGER_DELTA_v0.6.1.md | **External source:** UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md, rows Q153,Q155,Q156,Q158,Q162,Q163,Q169–Q173 | **Lane:** development / no registry promotion | **Physical promotion:** 0.

**New primary theorem manuscript:** [THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md](THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md). **Verifier:** [verify_thm534_burden_gate_curvature_v0_7.py](verify_thm534_burden_gate_curvature_v0_7.py). Original THM-534 transition probabilities remain SOURCE-BLOCKED.

| Claim | Result | Proof bin | Assumptions | Excluded promotion | Next gate |
|---|---|---|---|---|---|
| S18 | ρ'=ρ−(1/4)B1 H B1ᵀρ is nonnegative, mass-sum preserving and variance nonexpanding | EXACT CONDITIONAL | filled K4, 0≤h_e≤1, vertex stock ρ≥0, Q162 current, explicitly chosen one-step update | physical time, energy and open-system mass current | actual hard-gate selection and physical clock/stock mapping |
| S19 | 1ᵀB1j=0; B3ᵀB2ᵀj=0; 4‖j‖²=‖B1j‖²+‖B2ᵀj‖² | EXACT | standard signed Δ³ boundary, unit metric | energy transfer, physical curvature, new particles | optional new physical action or observable bridge |
| S20 | operator B2ᵀ H B1ᵀ identically zero iff all 6 edge conductances equal; binary flat masks exactly all-off/all-on | EXACT / NO-GO | Q162 gradient-only current, tetrahedron's four triangles | no nonflat curvature universally; only this model | source-select nonuniform H from packet states |
| S21 | explicit masked nonzero Fface=(-1/4,-1/4,0,0) with conserved ρ total and exact Hodge receipt | EXACT CONDITIONAL | mask h01=0, others1; ρ=(1,0,0,0); gate provenance OPEN | mask physically admitted or experimentally realized | identify source/boundary event producing this hard-gate configuration |
| S22 | conservation of ρ does not identify phase normalization κ for u_e=e^{iκj_e} | EXACT / NO-GO | arbitrary permitted real κ with no independent angular unit or constitutive law | identified U1 connection, Born probabilities, THM-534 weights | derive phase-action map and held-out readout |

**Source-stratum separation:** Q162's normalized relaxational current \(j_B=-(1/4)H B_1^\mathsf Tρ\) is distinct from Q163's alternative reversible/protected mixing normalization; they are **not** one proven physical event-time law. Hodge–Dirac 15D chain-state squared-amplitude conservation (v0.6) is also **not** the same carrier as the new 4D vertex burden conservation (v0.7).

**Typed curvature distinction:** v0.6 \(F_\downarrow=B_1N \in Hom(C_2,C_0)\), \(F_\uparrow=NB_3\in Hom(C_3,C_1)\) are separate covariant nilpotency-defect operators. v0.7 \(F_{\rm face}=B_2^\mathsf T j_B\in C^2\) is exact abelian face circulation. Their numerical values cannot be interchanged; no equality, conversion coefficient or dynamical promotion is established.

**Evidence:** Exact SymPy enumerator checked 64 gate masks × 4 basis burdens, positivity, stochasticity, rank distribution (0:2,1:12,2:38,3:12), 6 edge orientation flips, source-free null controls, exact 1/2=3/8+1/8 norm split and nonzero witness. Constructor run PASS; independent/non-constructor replay PENDING. No experimental data, no target-blind physical evaluation, no physical promotion.

**Reopening condition:** derive \(h_e=C_{cl,e}^{hard}T_{int,e}^{hard}\) predictively from actual UD packet state \((ρ,θ,χ,σ,b)\) and boundary contacts, obtain a nonuniform admissible state; independently derive phase/holonomy normalization and actual physical burden/energy measurement map. Keep all no-go branches frozen under their stated assumptions.
