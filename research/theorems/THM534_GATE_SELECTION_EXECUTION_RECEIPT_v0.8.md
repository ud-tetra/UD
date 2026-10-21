# THM-534 v0.8 constructor execution, negative-controls and proof-repair receipt

**Date:** 2026-10-21 | **Result:** PASS_SCOPED for exact S23–S28 finite mathematics, target-exposed development | **Physical promotion:** 0 | **Review:** constructor only; non-constructor independent replay PENDING.

**Primary theorem:** [THM534_GATE_SELECTION_AND_CIRCULATION_BUDGET_v0.8.md](THM534_GATE_SELECTION_AND_CIRCULATION_BUDGET_v0.8.md)  
**Ledger:** [THM534_GATE_SELECTION_CLAIM_LEDGER_DELTA_v0.8.md](THM534_GATE_SELECTION_CLAIM_LEDGER_DELTA_v0.8.md)  
**GitHub verifier:** [verify_thm534_gate_selection_v0_8.py](verify_thm534_gate_selection_v0_8.py). The local executed source is a longer version with matching primary checks, but its bytes differ from this compact GitHub adaptation. Repository readback verifies publication, *not an independent computational replay*.

## Frozen constructor outputs (locally executed script)
- Two competing S4-equivariant Boolean selectors: local mask (1,1,0,1,0,0), complete-cell mask (0,0,0,0,0,0), same χ=(1,1,1,0), β=(1,1,1,1), τ=all-one.
- Identical vertex burden (1,0,0,0): local \(\rho'=(1/2,1/4,1/4,0)\) and \(F=(0,1/4,1/4,0)\); complete-cell unchanged, zero \(F\).
- All 24 vertex relabelings were checked for both selector candidates. Symmetric-input S4 action transitive over six edges.
- **All 64 binary masks:** \(W=I-P_H^\mathsf TP_H-\mathcal F_H^\mathsf T\mathcal F_H\succeq0\) checked by exact rational eigenvalues; \(\mathcal F_H=-B_2^\mathsf THB_1^\mathsf T/4\). Matrix rank distribution: 0:1, 1:6, 2:19, 3:38 (this is the **budget matrix** rank, not v0.7 face-circulation operator rank).
- Exact fixed-mask demonstration: \(P\) eigenvalues {1×2, (1/4)×2}; \(F_n=4^{-n}F_0\) checked through n=7. Nonuniform mask may remain fixed, but circulating current tends to zero.
- Exact replenishment vector \(s=(1/2,-1/4,-1/4,0)\) returns \(\rho\) to its original value on each driven step. Variance \(D_0=3/4\), post-relaxation \(D'=1/8\), compensating source \(W=5/8\), \(||F_0||^2=1/8\).
- Exact route ambiguity: \(k=-j_B\) and \(k'=-j_B+B_2e_{012}\) both realize the same vertex source \(B_1 k=s\), but total face circulation differs.
- **NUMERICAL:** 16 paths ×256 updates = 4,096 source-control steps with fixed candidate or seeded random gate masks (seed 534080); 361 samples had \(\|F\|>10^{-12}\). Maximum stock drift 2.220446049250313e-16, max circulation budget overshoot 0.0, max last-64-step face magnitude 1.962615573354719e-17.
- **Local executed script SHA-256:** 62cd163c331c68928c213f61cab4340edf66923be931e44d382bbfe7b242d247.
- **Local console receipt SHA-256:** 2ba4095f746632c3a26bba6cf479e65eb4b6a0eacdbf5b728f419cfa31e997ce.

## First-pass self-review correction (append-only)
A preliminary extra assertion required that the **unweighted sum** of the four signed face-circulation coordinates vanish. The exact S23 local-gate witness falsified that assertion: \(F=(0,1/4,1/4,0)\), whose ordinary component sum equals 1/2. That assertion was **not a valid topological closure identity** and was removed *before* the successful release run.

**Correct law:** \(B_3^\mathsf TF=0\), i.e. the *oriented* tetrahedral 3-chain boundary pairing vanishes; here the two nonzero face components carry opposite orientation signs under \(B_3\), so the exact closure passes. This correction was found during construction, not independent adversarial review; it does not change the v0.7 or S25 topology statement.

## Strict interpretation
- The S23 selectors and frozen χ/b/τ are **constructed countermodels**, not derived UD gate dynamics. Whether χ=(1,1,1,0) is a valid retained cell is specifically OPEN.
- S25 is an \(\ell^2\) summability statement and forces \(\|F_n\|\to0\); it **does not** say \(F_n\) becomes exactly zero after finitely many steps. The explicit S28 counterexample retains nonzero \(F_n\) at every finite step while decaying as \(4^{-n}\).
- S26's compensating source is a **signed zero-sum redistribution in the vertex burden model**, not a proved endogenous pump or physical energy source.
- S27 proves that the vertex source alone leaves an edge cycle-current ambiguity, which must be fixed before claiming physical holonomy.
- The six-edge historical THM-534 transition weights, action normalization, physical burden/current law and empirical bridge remain SOURCE-BLOCKED/OPEN.

**Reopening gates:** derive a genuine packet closure/boundary/transport integrity update; independent nonconstructor proof review; source-complete reservoir and route-selection law; preregister a genuinely new held-out physical observable before outcome exposure. Physical promotion 0.
