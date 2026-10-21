# New J₁ interior state and complete rectangle through damping 1/4

The new exact state (ωc,γc)=(1269899393868235009/281474976710656000,1/4)≈(4.5115889472961435,0.25), with its own flux upper, joins the unchanged previous 28 states. The complete rectangle ω∈[8983/2000,36193/8000]=[4.4915,4.524125],γ∈[1/10,1/4]=[0.1,0.25] passes with **uniform continuum-plus-actual-evaluator radius <0.09965137**, conditional on declared primitive binary64 RN ties-to-even. The center, full goal, depth 30 and 4096-leaf budget were frozen before generation and passed unchanged.

![Complete certified region](COVER.svg)

| Quantity | Constructor-verified result |
| --- | --- |
| Uniform total radius | 0.099651367742709676 |
| Leaves / maximum depth | 129 / 11 |
| Active / saved states | 27 / 29 |
| Accepted represented pairs | 231599764661700005268413852995 |
| Newly accepted upper-strip pairs | 13234272266382867938904923240 |
| Area ratio / increase | 15/14 / 7.14286% |

## State and own upper

The unchanged meanfree Neumann scalar-wave benchmark uses F=10(x+y),μ(Ω)=2, and 18,673 nodal P2 coefficients with one exact mean constraint on 12,288 tetrahedra. Relative to `captures/2026-10-21T005546Z-codex-j1-left-25-88b09d86`, only the exact frequency literal changes; damping remains 1/4. Flux, curl and candidate replay constructors remain byte-identical. Exact decoding, weighted mean subtraction and residual correction audit the proposed two-word state; the continuum certificate does not assume an exact Galerkin solve.

Corrected J≈-3.719934462412676-2.100744116607757i. Finite-Galerkin algebraic output budget≈1.48364e-13; this alone is not continuum precision. Own defect squared≈0.0004005268758598898. Direct actual reported-J continuum radius=0.003917186979208949. The distinct phase-proxy radius=0.002099111052179269 has a different center and is not substituted for J precision.

The projected-source RT1/root/patch flux plus exact affine-curl correction obeys divτ=zcΠ1v−F and zero boundary normal trace. The cell-meanfree remainder zc(Π1v−v) receives a local Poincaré dual lift. This is a dual existence bound, not an explicit polynomial full-source flux. Saved replay checks direct divergence, normal traces, affine correction and full-P2-gradient moments. Full Hermitian mass controls residual transport; full bilinear mass controls output correction; projected mass appears only in flux cross identities.

## Join and rounded boundaries

At the new rational center, the previous 28 particular transported formulas have minimum lower enclosure≈0.114108787614>0.1. New-state model upper≈0.003917186979. The exact represented input `['0x1.20bddf916872cp+2', '0x1.0000000000000p-2']`, inside the goal, has previous-family minimum formula lower≈0.114108787614>0.1 and is now accepted with owner central_25. This is a change in certificate family, not an actual-error lower, a global optimum or exclusion of alternative flux/dual certificates.

One rectangular runtime guard and adaptive integer-word tree preserve the previous full γ≤6/25 domain and add the full-width upper strip. Previous count plus novel-strip count equals the new root count exactly. Area ratio=15/14; area measures certified parameter coverage, not physical performance or certificate tightness.

The exact frequency center is interior to the guard. Its nearest binary64 constant lies below the rational center and is neither frequency guard endpoint. Its stored-minus-rational error is -9/281474976710656000. Damping 1/4 is exactly binary64, equals the upper guard, and is its last accepted word; its quantization error is exactly 0. The words outside the frequency domain and following damping word are rejected; the interior center word is accepted. The frozen hex words and exact errors are checked. All constant quantization errors enter arithmetic propagation, including the zero damping error. Rational state centers, stored constants and exact represented inputs remain distinct; measurement/decimal-parsing uncertainty and physical calibration are outside this contract.

The placement/bank source is `captures/2026-10-21T005546Z-codex-j1-left-25-88b09d86`, using `LOCAL_SCOUT_RESULTS.json`. The state constructor source is separately bound to `captures/2026-10-21T005546Z-codex-j1-left-25-88b09d86`. The placement/bank parent retains the failed full 1/4 goal at the same frozen budget. The last complete uniform reference is separately bound to `captures/2026-10-21T000423Z-codex-j1-bank-24-11c33657`. This capture adds the new state without changing that goal or budget. The selected source point was at a finite local-grid endpoint, not an optimum. All previous 28 bank entries remain exactly equal. Scout metadata derives its formula count from the actual bank and checks every row's count, state keys and threshold flag. No mathematical formula or threshold changes. No new frozen mathematical retraction is made; the full-session retraction ratio is not computed without a complete claim inventory.

## Uniform and actual arithmetic audit

For exact meanfree trial vi, Ji(z)=Ji(zi)−(z−zi)∫vi² and H−Ji=ri(Az⁻¹ri). Cₚ≤1/2 and λ*=4, a valid continuum lower bound rather than equality with λ₁, yield

\[
U_i(Q)=\sqrt{1+(w_+/(2g_-))^2}
\left(\sqrt{d_i^2}+\sqrt{\nu_i^2}+\tfrac12D_i(Q)\|v_i\|_{L^2}\right)^2+E_i(Q).
\]

Every source dependency, root, split, leaf bound, uniform maximum and analytic count is checked. Owners minimize certified rational upper with lexicographic ties. Closed proof boxes share cuts; runtime word partitions are disjoint and consecutive. Frozen budget exhaustion remains UNRESOLVED. Successful finite parameter partitioning does not prove FEM accuracy termination or an a priori mesh rate.

Supplemental native/software controls: 17877 input traces,286032 intermediate nodes,768 internal seams, and 9 extension controls. Uniform floating radius≤4.77284711e-15. Source/AST, seven constant errors,16 primitive RN operations, additive 2⁻¹⁰⁷⁵ underflow, magnitude<16 overflow exclusion, ties, type/nonfinite/domain rejection, and corrupted certificate/split/word/domain/hash/uniform-radius checks pass. FMA/contraction is excluded; these checks are not an all-platform formal proof. No interpolation or continuity claim is added.

## Next action and replay

The prospectively frozen 129-frequency×8-positive-damping-row scout contains 1,032 points above 1/4 through 13/50, with 29 formulas per point. Raw next candidate=(36193/8000,13/50); sampled minimum formula lower≈0.075175513584. All sampled minimum model uppers below target:True; maximum≈0.075175513584. This remains diagnostic only. No uniform 13/50 cover, actual-error lower, global optimum or presumed candidate precision is claimed.

**Next:** Audit the complete region through γ=13/50 with the existing 29-state bank; if unresolved, inspect a prospectively frozen local scout before choosing a new state.

The standard root replay wrapper composes candidate state/flux and scalar-only replay. Actual saved executions run the components separately; REPLAY_RECEIPTS.json binds commands and log hashes. Prior 28 state/flux records are reused by hash. Manifest/event inventory every new artifact; old captures are unchanged. Figure inspected; native Project saved and reloaded. CI checks capture integrity and rejection controls, not independent scientific review.

Ledger v0.39 is coefficient provenance, not a source/damping derivation. CRL2 remains a proposal. Notes Backup and ASTER remain context, not proof. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused. External scalar-wave benchmark only; no native UD action/source/damping/metric, material/horn, GR/QFT or experimental identification.

**A. CURRENT MISSION TRAJECTORY —** Extend certified continuum coverage with an interior state and own upper.

**B. WHAT WAS DONE —** Constructed and replayed the new P2/flux state and complete 29-state rectangle.

**C. FINDING —** Complete γ≤1/4 passes; uniform radius<0.09965137; certified area+7.14286%.

**D. UD GAP IMPACT —** DERIVED / EXACT CONDITIONAL benchmark; Scientific OPEN; Constructor checked only; independent_review:false; Development/no registry; physical promotion 0. Independent review, full-band precision, FEM termination and native UD bridge remain OPEN.

**NEXT —** Audit the complete region through γ=13/50 with the existing 29-state bank; if unresolved, inspect a prospectively frozen local scout before choosing a new state.
