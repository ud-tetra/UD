# Adopted six-case design clarification

The owner selected exactly SIX paired cases, not the Cartesian product. This
clarification precedes generation/fitting and overrides only the pairing
ambiguity in PROSPECTIVE_REVIEW.md; its source, rounding and policy analysis
remains unchanged.

| Case | Preparation transform | Paired onehot noise family |
| --- | --- | --- |
| T1 | Signed reverse within parity | Stationary channel0 |
| T2 | Signed permutation, seed219237 | Preparation/time channel cycle |
| T3 | Signed permutation, seed219238 | Block1024, seed219301 |
| T4 | Offset rational pairs R1 | Period2 |
| T5 | Exact composed R1 R0 | Period4 |
| T6 | Exact composed (R1 R0)^T | Fixed spatial channel per preparation, seed219302, period4 signs |

R0 pairs the ordinary even/odd index lists; R1 pairs their one-position-left
rolls. Blocks are [[3,-4],[4,3]]/5. Single unpaired members remain unchanged.
T5/T6 use exact composed denominator25 matrices, then nearest rounding once.

Exact channel/sign expressions, RNG calls, PCG64/runtime version, literal
transform matrices, complete six-case table and all code must be frozen before
first generation. The source/rounding theorem is independent of which allowed
onehot channel/sign is chosen. No ambiguity may remain in the implementation
about those choices or subsequent regeneration order.

All six records are locally prospective deterministic synthetic fixtures. Each
has onequantum2^-48 perturbations relative to its own fresh nominal. There is
no original-baseline ball admission or physical-data claim. PR224 fixed caps
are prospective pass/refuse criteria and must not be enlarged after outcomes.

No actual transform matrices, new records, or fits were executed by this review.
Same-team design review only; physical promotion0. Code-specific review follows
when records.py and driver.py are available.
