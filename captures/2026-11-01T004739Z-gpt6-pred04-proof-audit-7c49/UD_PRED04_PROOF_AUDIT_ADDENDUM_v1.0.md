# Unified Dynamics: PRED-04 Proof Audit Addendum v1.0

**Date:** 2026-10-31 (America/Chicago)  
**Program:** Unified Dynamics mathematical proof lineage  
**Source state:** PR #479 at `b5c8146ae4b956279e6f399553e02cffbc42c7ea`, unmerged; proof-governance PR #473 at `2a19727f15e038f39721088b960cd46b97fd9bc5`, unmerged  
**Proof status:** EXACT_CONDITIONAL / VERIFIED_SCOPED; **review:** DEFERRED; **physical promotion:** 0.

## Proof milestones and decisions

| Proof | Mathematical outcome | Evidence / decision |
|---|---|---|
| `UD-PM-PRED04-TOPO-001` | The stated full K4 star-column excision of a tetrahedralized 3-ball yields `H_1(-;Z)=Z`. Legal topology-preserving face moves alone cannot produce that change. | PROVED_CONDITIONAL; independently enumerated at `N=4,6,8`; the assumed EX rule is not native-derived. |
| `UD-PM-PRED04-WORK-002` | For every once-per-edge update order, `W+ <= Delta +(mu*D/3)||h||²`; on the proposed calibrated `n=2`, `D<=6`, `mu=lambda` branch, `W+<=9/5`. | PROVED_CONDITIONAL; strictly tighter than existing valid `41/5`; no physical energy or uncalibrated bound established. |
| `UD-PM-PRED04-CAUSAL-003` | Immediate deletion/pruning of all tetrahedra at the occupied vertex leaves no outgoing live edge from that vertex. | NO-GO under excision-before-transfer / surviving-K4-only transport. The source implementation instead prepares the full trail before topology change. |

## Reconciliation of earlier constraints

The `41/5` estimate in PR #479 remains true but is nonsharp for its one-edge staging assumptions. Its proof did not exploit face closure to control positive curvature variation by exactly `2/3` of the face-edge square sum. This addendum preserves the old version and supplies a new tighter theorem; it does **not** retroactively rewrite frozen results.

The earlier fixed-three-edge source no-go also remains true under its own local-support and stiffness hypotheses. The new distributed theorem uses a different branch (all-edge updates, temporary curvature, and user-chosen `lambda_N` normalization). The uniform **absolute** model-work bound depends on setting the retained gap to unity. Only a **relative** work-to-gap bound survives without that step.

Topological persistence under PL-equivalent `2<->3` moves does **not** imply energetic persistence, stability under cellular restoration, or a conserved physical current. A retained defect requires an actual native source/recovery rule; pure gauge `Z_2` signs and fully `S4`-symmetric initial data do not select the distinguished defect path on their own.

## Reopening conditions

Native derivation may resume by specifying a source state space, a transfer-before-excision evolution, an edge-preserving control substrate, or a restoration-preventing burden rule. Each is a separate candidate model requiring conservation, coupling, clock/readout and no-go hypothesis checks. An independently selected physical measurement must define units, calibration, uncertainty, baseline and falsifier. **No physical promotion** occurs with this purely mathematical proof release.
