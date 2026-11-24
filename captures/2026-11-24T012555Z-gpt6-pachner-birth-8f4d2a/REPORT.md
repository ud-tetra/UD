# 1→4 Pachner vertex-birth and all-grade Whitney recurrence — cross-repository audit v0.1

**Captured: 2026-11-24 UTC. Status: EXACT/CONDITIONAL; NO-GO_SCOPED; OPEN_CONSTITUTIVE_SOURCE. Physical Promotion = 0.**

## Direct source pins
- UD accepted baseline `2e47d8718742cdd56ed81c41941b1cc3d42ad74b`, ledger v0.85 Git blob `93e2ca31eba625989087275a71c4857848e321c6`, rows Q165 (unit simplex quadratic support), Q169 (fixed-complex skew generator), Q177–Q179 (post-complex equal-top-star ownership), Q200/Q210 (lineage/constitutive nonidentifiability).
- UD-Physics accepted baseline `ea93a86305925aced4ad9aa43b8bc7979f5b0f15`, `experiments/four-cell-tetrahedron/README.md` v1.0, `experiments/pachner-boundary-observability/README.md` v0.1, `experiments/pachner-state-transport/README.md` v0.1.
- Independent development [UD-Physics draft PR #476](https://github.com/ud-tetra/UD-Physics/pull/476) at `bd78ee5723f84c02dfe2e0c5d8d965ff68c8113f`. Source of the present new scoped calculation: [UD-Physics draft PR #477](https://github.com/ud-tetra/UD-Physics/pull/477) at `f82620113a532ce88eb2408c2cab53e0efd410a2`. Both drafts are not mainline canon.
- Locally executed exact SymPy scratch package: `UD_PACHNER_VERTEX_BIRTH_WHITNEY_RECURSION_v0.1.zip`; SHA-256 `386873e43b7d042bf8c746520fffbd5fddc6f97cf794f0b50073775d6c56ecc1`. ZIP includes complete Python sources, reports and replay outputs. This GitHub report is a separate textual audit, not byte-identical to the ZIP.

## Precisely typed result
A single filled K4 cell admits an interior 1→4 Pachner/stellar subdivision, without another tetra or two-carrier gluing. With the regular tetra coordinates of prior pinned research and a central new vertex, f-vector `(4,6,4,1)→(5,10,10,4)`, old/new total real cochain dimensions 15→29; fixed oriented exterior shell; four daughter tetra each Euclidean volume 2/3.

Distinguish integral **chain** transfer `T:C_*(K)→C_*(K')` from barycentric Whitney **cochain** prolongation `P:C^*(K)→C^*(K')`:
- `∂'T=T∂`, but `T3ᵀT3=4`, so inherited Q165 unit simplex stock is **not** isometric on the top chain.
- `d'P=P d`, and `P_kᵀ M'_k P_k=M_k` for **all four k=0,1,2,3**, where `M_k` is assembled from exact Euclidean Whitney finite-element k-form integrals, `M_k,ij=∫<w_i,w_j>dV`. This is exact same-domain *cochain* isometry under a different, geometrically selected mass metric, not a retroactive correction to Q165.
- The 29D new cochain space includes 14 additional independent coordinates; the prolongation embeds old 15D without initializing independent amplitudes in those complement modes.
- Offcenter interior placement `(1/2,1/4,1/8)`, barycentric `(15,9,5,3)/32`, retains all-grade exact Whitney mass isometry.

Define the **conditional metric-skew** cochain generator `A_M=d−M⁻¹ dᵀ M`, not the locked Q169 *unit-metric* generator `A_unit=d−dᵀ`. Exact symbolic checks:
- Centroid 15→29: `A'_M P=P A_M` (**rank 0**), whereas `A'_unit P−P A_unit` has **rank 7** and squared Frobenius norm **15/4**.
- Offcenter 15→29: all-grade Whitney isometry holds, but `A'_M P−P A_M` has **rank 4**.
- Repeat centroid 1→4 in every first-generation tetra: level 2 f-vector `(9,26,34,16)`, dimension 85. Again all-grade Whitney mass isometry and cochain map pass, yet the Whitney-generator residual has **rank 13** (306 nonzero entries in its mass-premultiplied form). Thus initial centroid metric intertwining is NOT generally persistent under recursion.

The direct-sum Whitney metric combines forms of different geometric scaling `L^(3−2k)`; treating their sum as physically measured energy requires a separate unit/normalization map. The exact calculations use dimensionless reference coordinates; no physical energy or clock inferred.

## Claim control and boundary
**EXACT/CONDITIONAL:** An alternate single-carrier geometric recurrence and all-grade same-domain Whitney field conservation exist. This branch avoids two-carrier matching and overlap-quotient obstructions by changing the typed operation; it does not repeal those no-go results.
**NO-GO_SCOPED:** The original unit-chain metric still inflates the top chain under the integral subdivision; and one exact symmetric post-event generator intertwiner does not prove recursive dynamical self-similarity.
**OPEN:** What native pre-event state authorizes vertex birth, born-mode preparation, dynamic boundary/readout, physical time, choice between unit and Whitney metrics, and physical correspondence. No status is promoted in the accepted ledger.

## Verification
Source manuscript and report sections were read through GitHub at explicit revisions. Local tests `verify.py`, `whitney_allgrades.py`, `weighted_generator.py`, `weighted_noncentroid.py`, `level2.py` passed exact SymPy; the level-two script was corrected from accidental Python floating division to exact `Rational` before this release. GitHub CI, native repository verify script and independent non-constructor review NOT_RUN. This is a cross-repository **audit note** for review, not an accepted theorem release.

**Next decision:** derive the actual source-bound vertex-birth gate, initial complement states and a recurrence-compatible post-event generator; preregister physical correspondence separately. Physical Promotion = 0.
