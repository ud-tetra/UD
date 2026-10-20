# New J₁ gap state and complete rectangle through damping4/25

The actual state at exact (ωc,γc)=(921373/204800,4/25)≈(4.498891601562,0.16) has its own continuum upper. Added to the unchanged prior seventeen states, it certifies the complete rectangle

\[
\omega\in[8983/2000,36193/8000]=[4.4915,4.524125],\qquad
\gamma\in[1/10,4/25]=[0.1,0.16].
\]

Uniform continuum-plus-actual-evaluator radius **<0.09983478**, conditional on declared primitive binary64 RN ties-to-even. The state, complete rectangle, depth 24 and 4096-leaf budget were frozen before generation and passed unchanged. The prior complete rectangle is preserved and the full-width upper strip is included. One rectangular guard and one adaptive integer-word tree are used.

![Complete rectangle and new upper strip](COVER.svg)

| Quantity | Verified result |
| --- | --- |
| Uniform total radius | 0.099834778473677444 |
| Leaves / maximum depth | 76 / 12 |
| Active owners / saved states | 16 /18 |
| Accepted represented pairs, analytic count | 112,491,314,264,254,267,283,238,465,317 |
| Newly accepted upper-strip pairs | 13,234,272,266,382,831,206,420,462,499 |
| Certified area | 783/400000 |
| Previous certified area | 261/160000 |
| Area ratio / increase | 6/5 / 20.00% |

Coverage area measures the certified parameter domain, not physical performance or actual-error tightness.

## New state and own flux upper

The meanfree Neumann scalar-wave benchmark keeps F=10(x+y), μ(Ω)=2, gradient/flux metrics, source and mesh unchanged: 18673 P2 degrees of freedom on 12288 tetrahedra. Source comparison permits only the two exact parameter literals to change from PR289's constructor. A sparse solve and exact-residual correction propose four binary64 arrays. Exact arithmetic audits their two-word sum and weighted mean subtraction.

Corrected J≈-4.439238089143684-1.646779241618587i; corrected finite-Galerkin algebraic output budget≈2.78892e-13<10⁻¹⁰. This alone is not continuum precision. The new projected-source RT1/root/patch flux and exact affine-curl correction satisfy divτ=zcΠ1v−F, zero boundary normal trace and exact source/state/payload bindings. Remaining cell-meanfree zc(Π1v−v) receives a rigorous local Poincaré dual lift.

Defect squared≈0.0004911994910373007. Direct actual reported-J continuum radius=0.007453430115456229. The distinct phase-proxy radius=0.003991810821748057 has a different center and is not substituted for the J radius. Flux cross identities use projected mass; output correction uses full-P2 bilinear mass; residual transport uses full Hermitian mass. Saved flux replay checks exact divergence, normal traces, affine-curl reconstruction and direct full-P2-gradient moments.

## Certificate-family change and endpoint audit

PR290's unresolved depth 18/depth 24 attempts and exact inside-goal witness concern the former seventeen-state formula family. Those records remain unchanged. The new state changes that family: its center model upper is≈0.007453430115, whereas the old seventeen minimum particular-formula lower is≈0.103010945282>0.1. This is not an actual-error lower. The joined evaluator now explicitly accepts PR290's corrected exact represented obstacle input.

Both new center constants are nonbinary, and both quantization errors are included. Nearest binary64 to exact 4/25 lies above the exact upper boundary. The audit asserts the stored damping constant is one word above the greatest accepted damping word, and that the next word is rejected by the guard. The exact represented counterexample from PR290 lies inside the new domain and is accepted. Constants and accepted inputs are distinct objects. Decimal parsing/measurement uncertainty and physical frequency calibration are outside this contract.

## Uniform continuum and actual evaluator audit

For an exact meanfree trial vi, z=−ω²+2iγω and Ji(z)=Ji(zi)−(z−zi)∫vi²dμ, the identity H−Ji=ri(Az⁻¹ri) avoids an exact-Galerkin premise. Cₚ≤1/2 and the valid continuum gap lower λ*=4 give the box upper

\[
U_i(Q)=\sqrt{1+(w_+/(2g_-))^2}
\left(\sqrt{d_i^2}+\sqrt{\nu_i^2}+
\tfrac12D_i(Q)\|v_i\|_{L^2}\right)^2+E_i(Q).
\]

D bounds |z−zi| by endpoint extrema and E bounds actual output arithmetic uniformly. The local lift is a dual existence bound, not an explicit polynomial full-source flux. The theorem premises are unchanged and source-bound; λ*=4 is not equality with λ₁. Constructor checks do not create independent review.

The planner minimizes exact rational upper enclosures over eighteen states with lexicographic ties and accepts only upper≤1/10. It splits the larger squared z-variation score at the midpoint of represented positive binary64 words. Closed proof boxes share cuts while runtime word partitions are consecutive and disjoint. Every source hash, domain/root, split, leaf certificate, uniform maximum and analytic word count is checked. Previous word count plus new full-width strip count equals the new root count exactly; area ratio is 6/5.

Supplemental native/software checks: 10,532 input traces, 168,512 intermediate nodes, 450 internal seams and 9 extension-boundary controls. Uniform floating contribution≤4.15515006e-15. The actual evaluator source/AST, all seven constant quantizations, 16 primitive RN operations, additive 2⁻¹⁰⁷⁵ underflow budget, magnitude <16 overflow exclusion, source/type/domain/nonfinite/ties controls, budget exhaustion and corrupted certificate/split/word/domain/hash/uniform-maximum rejection checks pass.

The arithmetic model excludes FMA/contraction and does not formally verify every platform. No interpolation or continuity claim is added. Finite parameter partition success does not establish finite element accuracy termination or a quantitative mesh rate.

## Next placement and replay

A prospectively frozen 129×9 grid probes γ>4/25 through 17/100, excluding its lower damping row: 1032 points. Its selected raw candidate is exact(4624613/1024000,17/100). Minimum of eighteen particular-formula lower enclosures≈0.192668921879; all-eighteen-above-target flag=True. All 1032 sampled minimum model uppers below target: **False**; maximum≈0.192668921879. This ranks a declared finite grid only; it is not a global optimum, actual-error lower, alternate-certificate no-go or presumed candidate precision. Uniform 17/100 coverage is not claimed.

NEXT_STEP_REASSESSMENT.json records: **Construct an own state/flux upper at exact(4624613/1024000,17/100), then repeat the expanded-region audit.**

`PYTHONDONTWRITEBYTECODE=1 python3 replay.py` composes the candidate state/flux and scalar replay. This capture separately executes `candidate/replay.py` and `replay.py --scalar-only`; REPLAY_RECEIPTS.json records actual commands/log hashes. Saved scalar replay rebuilds and compares the cover, 1032-point placement and audit. Prior 17 state/flux proofs are reused by hash. Manifest/event inventory every new file; old evidence remains byte-identical. Project save/reload and CI/merge receipts are provenance, not independent scientific review.

Ledger v0.39 remains the coefficient provenance baseline, not a derivation of the source/damping. CRL2 remains a proposal, not enacted by citation. Notes Backup and ASTER remain context, not proof. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused. External scalar-wave benchmark only; no native UD action/source/damping/metric, material/horn, GR/QFT or experimental identification.

**A. CURRENT MISSION TRAJECTORY —** Close the former formula-family gap with an actual new state and own upper.

**B. WHAT WAS DONE —** Constructed and audited the new P2/flux state, eighteen-state full rectangle and saved replays.

**C. FINDING —** Complete γ≤4/25 passes; radius<0.09983478; area+20%; previous obstacle input included.

**D. UD GAP IMPACT —** DERIVED / EXACT CONDITIONAL benchmark result; Scientific OPEN; Constructor checked only; Development/no registry entry; physical promotion 0. Independent review,full-band precision,mesh termination and native bridge remain OPEN.

**NEXT —** Construct an own state/flux upper at exact(4624613/1024000,17/100), then repeat the expanded-region audit.
