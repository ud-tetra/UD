# THM-534 claim/dependency delta v0.8 — gate selection and dissipation

**Date:** 2026-10-21 | **Source baseline:** UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md, Q153/Q155/Q156/Q158/Q161/Q162/Q163/Q167/Q169–Q173 | **Parent:** [THM-534 v0.7](THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md) | **Lane:** development / no registry promotion | **Physical promotion:** 0.

| Claim | Status | Object/domain and dependencies | Exact finding or limit | Promotion gate |
|---|---|---|---|---|
| S23 | EXACT / NO-GO | binary vertex projection χ, boundary β, edge integrity τ; Q156 factorization and Q162 | two distinct S4-equivariant Boolean selectors yield different H and face circulation from same inputs | select actual closure vs cell-wide semantics from admitted χ,b update |
| S24 | EXACT / NO-GO | deterministic S4-equivariant state update and edge-gate map, homogeneous initial state | no dynamically selected nonuniform H or F_face without symmetry-breaking inputs | derive event/boundary/memory dynamics producing or identifying asymmetry |
| S25 | EXACT / NO-GO | closed Q162 relaxational ρ_{n+1}=P_H ρ_n, arbitrary 0≤H_n≤I | Σ‖F_n‖²≤D0−D_N≤D0; F_n→0; gate switching alone cannot sustain curvature | independent restorative source or different generator |
| S26 | EXACT CONDITIONAL | added zero-sum vertex source s_n; ρ_{n+1}=P_nρ_n+s_n | Σ‖F‖²≤D0−D_N+Σ[2⟨P_nx_n,s_n⟩+‖s_n‖²] | derive source energetics, reservoirs and contact routing |
| S27 | EXACT / NO-GO | vertex source s=B1k, complete Δ³ | k→k+B2y preserves source while changing total face circulation | derive route selection, holonomy map and independent readout |
| S28 | EXACT CONDITIONAL | frozen candidate local mask (1,1,0,1,0,0), ρ0=e0 | P has eigenvalues 1×2 and 1/4×2; F_n=4^{-n}F0 with ‖F0‖²=1/8 | derive admissibility and dynamic origin of constant χ/β/τ |

**Source conflict/disambiguation:** The historical ledger Q156 specifies only h_e=C_cl,e^hard T_int,e^hard, and Q162 specifies the relaxational *current* conditional on h_e. Neither gives a unique state-to-gate predicate nor a χ/β/τ evolution rule. The competing local/cell selectors are explicit falsification witnesses, not competing accepted UD canons. Historical Q163 protected/reversible mixing does **not** inherit S25's dissipative bound without checking its separate generator and carrier.

**Source-free versus externally restored currents:** S25 is a closed, source-free current result. S26 demonstrates a possible zero-total-stock replenishment route, but source vector s does not uniquely select its edge path; S27 exhibits null-route/cycle ambiguity. A cyclic vertex burden source is **not** thereby a native physical energy source or empirical magnetic field.

**Separate typed objects:** \(\rho\in C_0\) is the normalized vertex burden model, \(\psi\in\bigoplus C_k^\mathbb C\) from v0.6 is a complex 15D amplitude state, \(j\in C_1\) is burden redistribution, \(F_\mathrm{face}=B_2^\mathsf T j\in C^2\) is a face circulation. The older v0.6 covariant \(F_\downarrow=B_1N\) and \(F_\uparrow=NB_3\) are operators, not the same F. No physical metric, calibrated time, energy or Born map is identified.

**Evidence:** constructor mathematical proof and exact all-64 PSD mask verification; exact 24-permutation S4 selector tests; exact source/route and fixed-mask witness; 16×256=4096 finite numerical control steps, maximum mass drift 2.22e-16, maximum face-circulation budget overshoot 0, face-current tail maximum 1.96e-17. No non-constructor reviewer, no held-out external result, no claim-promotion. Source law OPEN_GATED.

**Next admissible gate:** independently derive/update χ_v, β_v and τ_e—or whichever actual packet-local typed variables replace these provisional projections—and exhibit a closure-valid nonuniform H. To obtain persistent curvature, also derive a finite source/reservoir budget and determine the extra edge-cycle routing. An externally prescribed mask or replenishment current is not a closure.
