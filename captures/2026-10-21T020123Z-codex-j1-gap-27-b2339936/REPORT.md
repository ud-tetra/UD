# New J₁ interior-frequency boundary state and complete rectangle through damping 27/100

The new exact state (ωc,γc)=(1264331734346891259/281474976710656000,27/100)=(4.491808647155762,0.27), with its own flux upper, joins the unchanged previous 30 states. The complete rectangle ω∈[8983/2000,36193/8000]=[4.4915,4.524125],γ∈[1/10,27/100]=[0.1,0.27] passes with **uniform continuum-plus-actual-evaluator radius <0.09977165**, conditional on declared primitive binary64 RN ties-to-even. The center, full goal, depth 30 and 4096-leaf budget were frozen before generation and passed unchanged.

![Complete certified region](COVER.svg)

| Quantity | Constructor-verified result |
| --- | --- |
| Uniform total radius | 0.099771647812212233 |
| Leaves / maximum depth | 108 / 10 |
| Active / saved states | 29 / 31 |
| Accepted represented pairs | 244834036928082836474834315494 |
| Newly accepted upper-strip pairs | 6617136133191433969452461620 |
| Area ratio / increase | 17/16 / 6.25% |

## State and own upper

The unchanged meanfree Neumann scalar-wave benchmark uses F=10(x+y),μ(Ω)=2, and 18,673 nodal P2 coefficients with one exact mean constraint on 12,288 tetrahedra. Relative to `captures/2026-10-21T014039Z-codex-j1-corner-27-41506396`, only the exact frequency literal changes. Flux, curl and candidate replay constructors remain byte-identical. Exact decoding, weighted mean subtraction and residual correction audit the proposed two-word state; the continuum certificate does not assume an exact Galerkin solve.

Corrected J≈-3.657936469734903-2.324776818437068i. Finite-Galerkin algebraic output budget≈1.45811e-13; this alone is not continuum precision. Own defect squared≈0.0004121849910942985. Direct actual reported-J continuum radius=0.00371801306347723. The distinct phase-proxy radius=0.001991358192547468 has a different center and is not substituted for J precision.

The projected-source RT1/root/patch flux plus exact affine-curl correction obeys divτ=zcΠ1v−F and zero boundary normal trace. The cell-meanfree remainder zc(Π1v−v) receives a local Poincaré dual lift. This is a dual existence bound, not an explicit polynomial full-source flux. Saved replay checks direct divergence, normal traces, affine correction and full-P2-gradient moments. Full Hermitian mass controls residual transport; full bilinear mass controls output correction; projected mass appears only in flux cross identities.

## Join and rounded boundaries

At the new rational center, the previous 30 particular transported formulas have minimum lower enclosure≈0.104094226541>0.1. New-state model upper≈0.003718013063. The exact represented input `['0x1.1f79caf9db22dp+2', '0x1.147ae147ae147p-2']`, inside the goal, has previous-family minimum formula lower≈0.104094226541>0.1 and is now accepted with owner gap_27. This is a change in certificate family, not an actual-error lower, a global optimum or exclusion of alternative flux/dual certificates.

One rectangular runtime guard and adaptive integer-word tree preserve the previous full γ≤13/50 domain and add the full-width upper strip. Previous count plus novel-strip count equals the new root count exactly. Area ratio=17/16; area measures certified parameter coverage, not physical performance or certificate tightness.

Both center constants are nonbinary. Nearest frequency lies below the exact interior center and is distinct from either frequency guard endpoint. Nearest damping lies above the exact upper damping guard, one word beyond the last accepted damping input, and the rounded center word is rejected as runtime input. Stored-minus-rational errors are δω=-9/281474976710656000 and δγ=1/56294995342131200. The frozen hex words and exact errors are checked; both errors enter arithmetic propagation. Rational state centers, stored constants and exact represented inputs remain distinct. Measurement/decimal-parsing uncertainty and physical calibration are outside this contract.

The placement/bank source is `captures/2026-10-21T014039Z-codex-j1-corner-27-41506396`, using `LOCAL_SCOUT_RESULTS.json`; the last complete uniform source is separately bound to `captures/2026-10-21T012822Z-codex-j1-bank-26-5b4bbc69`. The state constructor source is separately bound to `captures/2026-10-21T014039Z-codex-j1-corner-27-41506396`. The parent full-goal attempt was unresolved at the same frozen budget; this new state changes the certificate bank while preserving that target and budget. The source scout score was evaluated at represented inputs, not the exact rational candidate center. All previous 30 bank entries remain exactly equal. Scout metadata derives its formula count from the actual bank and checks every row's count, state keys and threshold flag. No mathematical formula or threshold changes. No new frozen mathematical retraction is made; the full-session retraction ratio is not computed without a complete claim inventory.

## Uniform and actual arithmetic audit

For exact meanfree trial vi, Ji(z)=Ji(zi)−(z−zi)∫vi² and H−Ji=ri(Az⁻¹ri). Cₚ≤1/2 and λ*=4, a valid continuum lower bound rather than equality with λ₁, yield

\[
U_i(Q)=\sqrt{1+(w_+/(2g_-))^2}
\left(\sqrt{d_i^2}+\sqrt{\nu_i^2}+\tfrac12D_i(Q)\|v_i\|_{L^2}\right)^2+E_i(Q).
\]

Every source dependency, root, split, leaf bound, uniform maximum and analytic count is checked. Owners minimize certified rational upper with lexicographic ties. Closed proof boxes share cuts; runtime word partitions are disjoint and consecutive. Frozen budget exhaustion remains UNRESOLVED. Successful finite parameter partitioning does not prove FEM accuracy termination or an a priori mesh rate.

Supplemental native/software controls: 15010 input traces,240160 intermediate nodes,642 internal seams, and 9 extension controls. Uniform floating radius≤4.75888226e-15. Source/AST, seven constant errors,16 primitive RN operations, additive 2⁻¹⁰⁷⁵ underflow, magnitude<16 overflow exclusion, ties, type/nonfinite/domain rejection, and corrupted certificate/split/word/domain/hash/uniform-radius checks pass. FMA/contraction is excluded; these checks are not an all-platform formal proof. No interpolation or continuity claim is added.

## Next action and replay

The prospectively frozen 129-frequency×8-positive-damping-row scout contains 1,032 points above 27/100 through 7/25, with 31 formulas per point. Raw next candidate=(922939/204800,7/25); sampled minimum formula lower≈0.084002432845. All sampled minimum model uppers below target:True; maximum≈0.084002432845. This remains diagnostic only. No uniform 7/25 cover, actual-error lower, global optimum or presumed candidate precision is claimed.

**Next:** Audit the complete region through γ=7/25 with the existing 31-state bank; if unresolved, inspect a prospectively frozen local scout before choosing a new state.

The standard root replay wrapper composes candidate state/flux and scalar-only replay. Actual saved executions run the components separately; REPLAY_RECEIPTS.json binds commands and log hashes. Prior 30 state/flux records are reused by hash. Manifest/event inventory every new artifact; old captures are unchanged. Figure inspected; native Project saved and reloaded. CI checks capture integrity and rejection controls, not independent scientific review.

Ledger v0.39 is coefficient provenance, not a source/damping derivation. CRL2 remains a proposal. Notes Backup and ASTER remain context, not proof. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused. External scalar-wave benchmark only; no native UD action/source/damping/metric, material/horn, GR/QFT or experimental identification.

**A. CURRENT MISSION TRAJECTORY —** Extend certified continuum coverage with a boundary state and own upper.

**B. WHAT WAS DONE —** Constructed and replayed the new P2/flux state and complete 31-state rectangle.

**C. FINDING —** Complete γ≤27/100 passes; uniform radius<0.09977165; certified area+6.25%.

**D. UD GAP IMPACT —** DERIVED / EXACT CONDITIONAL benchmark; Scientific OPEN; Constructor checked only; independent_review:false; Development/no registry; physical promotion 0. Independent review, full-band precision, FEM termination and native UD bridge remain OPEN.

**NEXT —** Audit the complete region through γ=7/25 with the existing 31-state bank; if unresolved, inspect a prospectively frozen local scout before choosing a new state.
