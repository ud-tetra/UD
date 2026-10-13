# UD native spatial-refinement source gate v0.1

**13 October 2026 UTC · development, no registry entry · physical promotion 0.** Constructor: Codex; independent review pending. This audit tests the next dependency of [spatial-symbol calculation v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T020255Z-codex-spatial-symbol-753fe949/UD_SPATIAL_REFINEMENT_SYMBOL_v0.1.md): whether current UD sources actually select a three-dimensional, increasingly fine family of tetrahedral complexes and its continuum clock/chart. It makes a scoped source determination, not a proof that *no possible future* UD rule can do so.

## 1. Source-bound objects and provenance

| Source and section | Defined object | What is still needed |
|---|---|---|
| [Paper I, review draft v1.1.1, §§1, 4, 6.1, 6.5, 7.4, 8.4, 9](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) | Supplied finite oriented 3-complex `K`, unique-simplex chain space, unit Euclidean pairing, `A_K=B_K^T−B_K`; an oriented 2-to-3 boundary identity and obstructions to canonical linear jumps | A rule selecting which `K`, when to move, a jump map for state, and a chart/refinement scale |
| [Paper IV, review draft v0.1, §§1, 8–9](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_IV_REVIEW_DRAFT_v0.1.md) | Conditional prepared controllers, capture and finite bank renewal on supplied carriers | No bulk-spatial refinement selector or physical clock |
| Supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q25–Q26, Q101, Q169–Q170 | Native global skew generator on *given* unique-simplex complex; edge-weight and routing primitive remain open | Source law for weights, move, state transfer, effective spacetime metric |
| Supplied `artifact_dependency_map.md`, §§2–5; `Gap2_FINAL_STATUS.md`, §§1, 3, 5 | A proposed dependency spine; a report of 80×80 grid simulations and qualitative cluster development | Grid is supplied, not a three-dimensional tetrahedral refinement limit or a proven physical bridge |
| Supplied `Unified Dynamics (Distinction Theory) v2.2_ Master Manuscript.pdf`, §§2–4 | Historical hierarchy calling the tetrahedron the first volumetric closure and icosahedron a shell | No specific lawful subdivision geometry, transition map, or mesh continuum theorem |
| Supplied `distinction_dynamics_manuscript.pdf`, 11 March 2026, §§3, 5 eq. (10), 11 eq. (30), SHA-256 `909ac4bfbb07ab815d15463648278877a7452989797589bf630564a0afa9f1ef` | Historical candidate packet lattice, coframe metric and later FLRW ansatz | See exact sign conflict below; no source of refinement |
| Supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, §§1, 4–6 | Proposed status ladder and development lane | Constructor audit cannot promote a physical bridge or registry status |

The archived `DistinctionDynamics_Full_Repository_v1.zip` contains 55 very short placeholder files (4,892 total uncompressed bytes); sampled `packet_modulation_layer.md`, `packet_field_equation.md`, `carrier_definition.md` and the other local reconstruction pages are placeholders. They do not encode a recoverable refinement rule. An inaccessible image `Gap2_FINAL_Finite_Genesis.png` was not inspected; re-upload it if it contains a rule.

## 2. EXACT source-bounded obstruction and finite replay

Fix any supplied finite 3-complex `K`, signed boundary `B_K` and real graded state `c∈C_•(K)`. The only native flow claimed here is

\[
\dot c=A_Kc,\quad A_K=B_K^T-B_K,\quad K(s)=K_0\ \text{for the duration of this declared flow}.
\]

`A_K` acts **within** `C_•(K)`; it has neither a codomain of complexes nor a state-transfer map from `C_•(K)` to `C_•(K')`. It cannot by itself change the number of vertices, generate a mesh scale `a_n→0`, or order candidate local moves. This is a type obstruction under the fixed-complex premises, not a universal no-go on enriched UD dynamics.

Paper I's exact 2-to-3 identity has common exterior boundary but source/target top-chain squared norms `2` and `3` under its unit Euclidean chain pairings (§6.5). Thus boundary equality does not supply a norm-preserving boundary-fixing chain jump. A 2-to-3 bistellar move also retains the same five vertices; iterating only that move is not a vertex-refining rule. Paper I explicitly leaves admission and jump data as supplied contracts, and its §8.4 symmetry example forbids a deterministic covariant selector that exclusively picks one of two automorphism-exchanged eligible contacts while always making progress. Nothing in these statements creates the Freudenthal family of the previous report.

**EXACT fixed-complex replay:** for one filled tetrahedron `K4`, `L_0=B_1B_1^T=4I_4-J_4`; its spectrum is `0,4,4,4`. Vertex amplitudes satisfy `u_{ss}+L_0u=0`, with a finite set of spatial modes and no scale parameter. `verify.py` constructs the signed incidence and confirms `B²=0`, the spectrum and the boundary/norm witness with integer arithmetic. **NO-GO, scoped:** that fixed source law cannot by itself yield a three-spatial-dimensional continuum principal symbol. The positive definite coefficient `C=2I+2J` in the prior Freudenthal example is consequently **conditional on externally supplied geometry and the chosen scale**; it is not a UD-selected tensor.

## 3. Historical coframe sign conflict (versioned scope finding)

The 11 March 2026 `distinction_dynamics_manuscript.pdf`, §5 eq. (10), proposes `g_{μν}=e_μ^a e_ν^b δ_{ab}`; its §11 eq. (30) writes a line element with negative time square and positive spatial squares. For any **real** coframe matrix `E` and positive Euclidean `δ=I`, the former is `g=EE^T` and, for every real covector `v`, `v^Tgv=||E^Tv||²≥0`. If `E` is nonsingular, inertia is four positive; if singular, at least one zero. It **cannot** have one negative eigenvalue. The later FLRW signature cannot follow from eq. (10) on the same real carrier, independent of mesh refinement. This is a conflict in a historical candidate, not a defect in Paper I's finite chain theorem.

**AUTO_FREEZE for reuse as a derived Lorentzian metric:** Do not reuse the historical eq. (10) as having derived eq. (30). A versioned amendment must either add a source-derived hyperbolic propagation co-metric on a separately typed carrier, or give an indefinite internal form with its dynamical sign-selection and clock justification; changing `δ` to `η` by decree would reintroduce the target. Such an amendment must retain both old equations and state explicitly which interpretation is superseded. No source is silently rewritten here.

## 4. Minimal missing selector contract and decision test

A future proposal needs `R:(K,c,m)→(K',c',m')`, where `m` is declared local memory, plus a legal-move set, state jump/initialization map, event timing and tie/batch rule. It must be invariant under relabeling, prescribe boundary handling, and prove when/why repeated updates yield nondegenerate 3D meshes with `a_n→0`, bounded degree/shape and a stable or state-dependent second-moment tensor. A physical chart or length may not be reverse engineered from the desired light cone. Then recompute `B_{K_n}`, controlled rescaled dispersion and every relevant sector's principal symbol on target-blind selected trajectories; a positive-definite 3D spatial tensor on an open state domain and a shared causal cone would pass the mathematical signature gate. Null outcomes, degeneration, anisotropy, differing cones or no refinement reject their respective stronger claims.

**Decision:** No accepted current source rule found that selects a bulk-refining `K_n`; source retrieval plus type checking closes only the *status question*. Lorentzian mathematical emergence from current UD remains **OPEN_GATED**, while a fixed-complex-only derivation is **NO-GO** under its exact premises. Physical promotion 0; independent review pending.
