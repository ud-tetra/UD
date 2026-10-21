# J1 unchanged-bank rectangle through 17/50

**PASS — the complete proposed rectangle is certified using the existing 35-state bank.** DERIVED / EXACT CONDITIONAL external scalar-wave benchmark; Scientific OPEN; constructor checked; independent review pending. Development — no registry entry; physical promotion 0.

## Frozen scope and result

The prior PR331 finite-grid scout motivated this attempt, without certifying it. Before execution, AUDIT_FREEZE.json fixes the full goal, target and finite budget:

| Quantity | Exact scope |
|---|---|
| Frequency | [8983/2000,36193/8000] |
| Damping | [1/10,17/50] |
| Target total radius | 1/10 |
| Maximum depth / leaves | 30 / 4096 |
| Saved states | 35, unchanged |

The new complete cover has **129 cells**, maximum depth **11**, and uniform continuum-plus-floating radius **0.09995045691185293<1/10**. Its 33 active owners are selected from the unchanged 35 saved states. The domain includes the entire previous rectangle through33/100 plus a new full-width upper strip. Exact area ratio is **24/23**, an increase of 1/23 (approximately4.34783%). Exact accepted represented-input pair count is **291153989860422837528517086093**, with **6617136133191433969452461620** newly accepted pairs.

No new state or flux coefficients were generated, and no state/flux solver was rerun. BANK.json and the kernel, planner, evaluator and rounding sources are byte-identical to PR331. Prior state/flux results and replay receipts are reused by hash. The new work is the complete rectangular cover, actual estimator audit and saved scalar replay, not another own-state construction.

## Continuum and floating certificate

The inherited meanfree Neumann benchmark keeps C_P<=1/2 and continuum eigenvalue lower bound lambda_*=4; this is not equality with the first eigenvalue or the old discrete gap. For each state c and exact rational proof box Q, the envelope is
\[
r_Q=\kappa_Q\left(\sqrt{d_c^2}+\sqrt{\nu_c^2}+\tfrac12 D_{z,Q}\sqrt{m_c}\right)^2+E_Q.
\]
Own flux defects, local cell-meanfree residual lifts and full Hermitian masses enter transport; the full bilinear masses enter the corrected-output estimator. Exact decoded saved words have exact mean removal; no exact-Galerkin assumption is imposed on floating coefficients. Primitive binary64 round-to-nearest arithmetic is audited using the unchanged16-operation expression, exact rational square-root enclosures, outward error grid, quantized constants, underflow allowance and bounded magnitudes. Proof boxes share cuts, while accepted word partitions are disjoint and exhaust the guard. The continuum enclosure covers every proof box; the floating addition applies to represented inputs in its word partition.

**Upper boundary repair:** 17/50 is not representable. Its nearest binary64 value `0x1.5c28f5c28f5c3p-2` exceeds the exact guard by `11/450359962737049600` and is the first excluded word. The last accepted value is `0x1.5c28f5c28f5c2p-2`, whose signed offset is `-7/225179981368524800`. The actual evaluator rejects the nearest rounded guard value; clients must use a represented input inside the exact guard. This is checked separately from unrelated saved state-center constants.

![Complete proof boxes](COVER_REGION.png)

## Executed verification

The constructor audit checks source hashes, all35 bank definitions, source parameters, full state masses, exact node/leaf/word/pair identities, uniform bounds and source-code identity. It exercises **17920** native traces, **286720** operation comparisons, **768** internal seam controls, and **9** previous/new-strip boundary controls. Tampered tree, certificate, radius, domain and hash records are rejected. Budget exhaustion, outside words, nonfinite/wrong-type inputs, the rounded upper guard, and normal/subnormal ties-to-even controls are exercised. The saved scalar replay must reproduce COVER.json, PLACEMENT_RESULTS.json and AUDIT_RESULTS.json; its actual exit and log hash are in REPLAY_RECEIPTS.json. These are scoped constructor checks under the declared primitive arithmetic model, not non-constructor review or an all-platform formal proof.

## Next gate and provenance

The prospectively frozen129-by-8 scout over damping(17/50,7/20] executes all1032 probes. It selects exact **(36193/8000,7/20)**, with minimum particular-formula lower approximately **0.1191105230781425**. All35 particular formulas exceed1/10 there: **True**. This lower enclosure concerns those declared upper-bound formulas, not the unknown actual approximation error. It does not rule out alternate certificates or identify a continuous optimum. It does justify constructing another own state before attempting that future full rectangle; no candidate precision is presumed.

Next action: **Construct own state/flux at exact(36193/8000,7/20),then audit a prospectively frozen full rectangle through7/20.**

Preparation base is `6544adf6a5649f50718cd823c85abc73553bd93e`, including concurrent PR329/330's action-scale recovery and identifiability work. That separate track is preserved and is not a mathematical dependency of this scalar-wave result. The supplied provenance ledger's identical bytes remain context; its coefficients do not derive this source or damping. The supplied CRL-2 amendment remains a proposal, not enacted by citation. No native UD constitutive/metric/clock bridge, physical material or horn identification, empirical calibration, full audit-band closure, or quantitative mesh-termination theorem is inferred. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused.

**A. CURRENT MISSION TRAJECTORY —** Extend certified parameter coverage using the frozen bank when possible.

**B. WHAT WAS DONE —** Full17/50 rectangle, actual evaluator audit and saved scalar replay; no new state/flux generation.

**C. FINDING —** PASS; radius 0.09995045691185293,129 cells,area ratio24/23 relative to PR331.

**D. UD GAP IMPACT —** DERIVED / EXACT CONDITIONAL benchmark; Scientific OPEN, independent review pending, Development/no registry,physical promotion0.

**NEXT —** Construct own state/flux at exact(36193/8000,7/20),then audit a prospectively frozen full rectangle through7/20.
