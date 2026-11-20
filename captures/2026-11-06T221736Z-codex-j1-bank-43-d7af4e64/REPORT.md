# J1 scalar-wave benchmark: certified rectangle through 43/100

**DERIVED / CONDITIONAL — PASS.** The full rectangle `omega ∈ [8983/2000, 36193/8000]`, `gamma ∈ [1/10, 43/100]` is certified at target radius `1/10` using the unchanged 40-state bank. The proof covers the exact rational domain; the floating allowance applies to represented binary64 inputs under the declared round-to-nearest arithmetic model.

| Item | Result |
|---|---:|
| Certified cells | 123 |
| Maximum depth / frozen limit | 11 / 30 |
| Active owners / saved states | 38 / 40 |
| Uniform total radius (outward decimal bound) | <0.099700362 |
| Area ratio relative to PR #362 | 33/32 |
| Accepted binary64 input pairs | 350708215059145706521104779932 |
| New upper-strip pairs | 6617136133191433969452461620 |

## Scope, method and replay

The domain, target, bank digest, depth/leaf budget (30/4096) and next scout were fixed in [AUDIT_FREEZE.json](AUDIT_FREEZE.json) before computation. The [contract](CONTRACT.json) binds the original state/flux results and their dependent artifacts by SHA-256. No state/flux coefficients or solvers were rerun. The frozen basis is [PR #362](https://github.com/ud-tetra/UD/pull/362), report sections “Continuum and floating certificate” and “Executed verification,” and its exact source dependencies. The current repository base was `a78193d420f3bac957be081aed0525fbc1457825`; the recovered checkout preserves intervening tracks.

The checker recomputes the box certificates, verifies disjoint and exhaustive input word ranges, and checks the actual scalar evaluator. It exercised 17139 native traces, 274224 primitive comparisons, 732 seams and 9 extension controls. Malformed proof data, budget exhaustion, outside-domain inputs, invalid types and nonfinite inputs were checked. The accepted upper damping word is `0x1.b851eb851eb85p-2`, with exact offset `-3/450359962737049600`; the evaluator rejects the next word above the guard.

Run `PYTHONDONTWRITEBYTECODE=1 python3 replay.py` in this capture within the repository. The [saved replay](REPLAY.log) exited 0 and reproduced the cover, placement and audit records.

## Next decision

The 1,032-point scout over `gamma ∈ (43/100, 11/25]` selected `(4611563/1024000, 11/25)`. The exact minimum lower enclosure of the 40 declared transport formulas exceeds `1/10` at that point (approximately 0.1067054608). This establishes a limitation of those formulas at the selected point. Actual error, other certificate constructions and continuous coverage beyond `43/100` remain open.

Freeze a new own state and flux at exact (4611563/1024000, 11/25), then audit the full rectangle through 11/25.

## Governance and publication

Constructor checks passed. Scientific status OPEN; independent review pending; physical promotion 0. Full-band closure, general mesh termination and native UD correspondence remain OPEN. The supplied v0.39 provenance ledger and CRL2 proposal match the prior contextual hashes and supply no benchmark coefficients. Gap2_FINAL_Finite_Genesis.png was unavailable and unused. The Project field could not be edited in the signed-out browser; see [PROJECT_RECEIPT.json](PROJECT_RECEIPT.json).
