# Certified J₁ central damping0.15 state and complete local parameter rectangle

The actual saved state at exact (ωc,γc)=(577/128,3/20)=(4.5078125,0.15) has its own continuum upper certificate. Added to the prior sixteen states, it certifies the complete rectangle

\[
\omega\in[8983/2000,36193/8000]=[4.4915,4.524125],
\qquad\gamma\in[1/10,3/20]=[0.1,0.15].
\]

Uniform continuum-plus-actual-evaluator radius **<0.09981147**, conditional on declared primitive binary64 RN ties-to-even. The entire PR287 three-component union is preserved. Its formerly rejected upper central region is now included. Runtime evaluation uses one rectangular guard and one tree, with no component switch.

![Complete rectangle and former central gap](COVER.svg)

| Quantity | Verified result |
| --- | --- |
| Uniform total radius | 0.099811468598953651 |
| Leaves / maximum depth | 65 / 8 |
| Active owners in seventeen-state bank | 15 |
| Accepted represented pairs, analytic count | 99,257,041,997,871,436,076,818,002,818 |
| Newly accepted former-gap pairs | 1,323,427,226,638,322,822,687,511,288 |
| Certified area | 261/160000 |
| Previous union area | 12789/8000000 |
| Area ratio / increase | 50/49 / 2.04% |

Coverage area measures the certified parameter domain, not physical performance or error tightness.

## Actual state and own continuum upper

The declared source F=10(x+y), meanfree Neumann space, normalized μ(Ω)=2, gradient metric and flux metric remain unchanged. The conforming P2 mesh has 12,288 tetrahedra and 18,673 degrees of freedom. Exact source comparison permits only the frequency literal to change relative to PR287's constructor. Sparse factorization plus one exact-residual correction proposes four binary64 arrays; exact arithmetic audits their two-word sum and weighted mean subtraction.

Corrected J≈-4.431149462437416-1.512810282621893i. Its corrected finite-Galerkin algebraic output budget is 2.35457e-13, below 10⁻¹⁰. This alone is not continuum certification. The new projected-source RT1/root/patch flux with exact affine-curl correction satisfies divτ=zcΠ1v−F and zero boundary normal trace. The remaining cell-meanfree source zc(Π1v−v) receives a rigorous local Poincaré dual lift.

Exact defect squared≈0.0004804075875103615. Direct actual reported-J continuum radius=0.007790787293186475. The separate phase-proxy radius=0.00417349099367713 has a different center and is not substituted for the J radius. Saved flux replay checks exact divergence, normal traces, affine-curl corrections and direct full-P2-gradient moments. Flux cross identities use projected mass; output correction uses full-P2 bilinear mass; residual transport uses the Hermitian mass. Source/state/parameter/payload bindings pass.

Frequency 577/128 is exactly binary64, so its center-constant quantization error is zero. Damping 3/20 is nonbinary and its center error remains explicitly included. The audit asserts both facts. Inputs denote exact represented values. Measurement uncertainty, decimal parsing uncertainty and physical time/frequency calibration are outside this contract.

## Continuum and actual evaluator proof

For any exact meanfree trial vᵢ, with z=−ω²+2iγω, define Jᵢ(z)=Jᵢ(zᵢ)−(z−zᵢ)∫vᵢ²dμ and residual rᵢ. The identity H−Jᵢ=rᵢ(Az⁻¹rᵢ) avoids an exact-Galerkin premise. Convex-domain Cₚ≤1/2 and rotated coercivity give the sufficient box upper

\[
U_i(Q)=\sqrt{1+(w_+/(2g_-))^2}
\left(\sqrt{d_i^2}+\sqrt{\nu_i^2}+
\tfrac12D_i(Q)\|v_i\|_{L^2}\right)^2+E_i(Q).
\]

D encloses |z−zᵢ| using endpoint extrema; E bounds the actual evaluator uniformly. The local lift is a dual existence bound, not an explicit full-source polynomial flux. The continuum spectral gap λ*=4 is a lower bound, not equality with λ₁. Earlier continuum/flux premises remain source-bound and conditional; citation does not create independent review.

The deterministic planner minimizes rational upper bounds over seventeen states with lexicographic ties. It accepts only upper≤1/10; otherwise it splits the larger variation score at the midpoint of represented positive binary64 words. Closed proof boxes share cuts; runtime word boxes form disjoint consecutive partitions. Frozen limits are depth 18 and 4096 leaves. Exhaustion means unresolved. Finite parameter partition termination does not imply finite element accuracy termination.

Every root/domain/source hash, split, leaf certificate, uniform-radius maximum and analytic word count is checked. All three former component domains are subsets of the new rectangle. Their disjoint word counts plus the formerly rejected central word rectangle equal the new root count exactly. Six specific former-gap controls confirm runtime acceptance immediately inside the former gap boundaries and at the binary-exact central frequency. All 384 internal-seam controls pass.

Supplemental 9,011 native/software traces compare 144,176 intermediate nodes and the exact closed output identity. Uniform floating contribution≤4.15317103e-15. Uniform-radius tampering, corrupted certificates/splits/words/domain/hashes, budget exhaustion, AST/source, type/domain/nonfinite and software ties-to-even controls pass. Active owners: adaptive_central, adaptive_left, adaptive_right, central_15, central_high, damping_left, damping_right, edge_15, edge_damping, opposite_edge, right_edge_15, shifted_neighbor, shifted_original, wider_left, wider_right.

The evaluator proof includes seven constant quantization budgets (including zero errors where exact), sixteen primitive RN operations, additive 2⁻¹⁰⁷⁵ underflow and magnitude <16 overflow exclusion. No interpolation or continuity claim is added. These constructor checks do not formally verify every platform or FMA/contraction mode.

## Prospective freeze, next placement and reproduction

The selected state and full-rectangle goal were frozen before generation and passed unchanged. A frozen 9×9 grid probes above γ=3/20 through 4/25, excluding its lower damping row. Its 72 probes recommend next **(ω,γ)=(143989/32000,4/25)≈(4.499656250,0.160000000)**. The minimum of seventeen downward-enclosed particular transported-upper formulas is≈0.097545988; all-seventeen-above-target flag: **False**. This ranks only a finite declared grid with fixed norm budgets. It is not an actual-error lower, global optimum, alternate-certificate no-go or assumed new-state precision. The candidate remains outside the accepted rectangle.

All 72 saved minimum_model_upper values are below the target, with their maximum≈0.097545987959. NEXT_STEP_REASSESSMENT.json records the decision to attempt a uniform cover through γ=4/25 using the existing seventeen-state bank before constructing another state. This finite-grid result does not certify γ=4/25; the current runtime guard and uniform certificate still stop at γ=3/20.

`PYTHONDONTWRITEBYTECODE=1 python3 replay.py` composes candidate state/flux and scalar replay. This capture separately executed `candidate/replay.py` and `replay.py --scalar-only`; REPLAY_RECEIPTS.json records actual commands/log hashes. Scalar replay rebuilds and compares the complete cover, placement and audit results. Earlier states/proofs are reused by hash. Manifest/event inventory every new file; previous capture bytes remain unchanged. GitHub/CI/merge receipts are posted after completion.

Concurrent PR288 is preserved without importing its full-spectrum accuracy claims into this benchmark proof. Ledger v0.39 remains the coefficient provenance baseline, not a derivation of the benchmark source/damping. CRL2 remains a proposal, not enacted by citation. The Notes Backup and ASTER context were inspected previously and are not benchmark proof sources. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused.

Classification **DERIVED / EXACT CONDITIONAL** for state/rectangle; **CANDIDATE** for next placement. Constructor checked; independent review absent; Scientific overall **OPEN**; Development—no registry entry; **physical promotion=0**. The declared local parameter gap is conditionally closed; full-band precision, quantitative finite mesh termination, native UD action/source/damping/metric derivation and experimental identification remain OPEN. External scalar-wave benchmark only; no material/horn or GR/QFT identification.

**A. CURRENT MISSION TRAJECTORY —** Close the local upper central gap with an actual central state and own upper.

**B. WHAT WAS DONE —** Constructed and audited the P2/flux state, seventeen-state complete evaluator and saved replays.

**C. FINDING —** Complete ω[4.4915,4.524125]×γ[0.1,0.15] passes; radius<0.09981147; former gap included; area+2.04%.

**D. UD GAP IMPACT —** Local gap closed conditionally. Independent review, full-band precision, finite mesh termination and native bridge remain OPEN. Physical promotion 0.

**NEXT —** Audit the complete γ≤4/25 region using the existing seventeen-state bank before adding states.
