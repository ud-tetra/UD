# THM-534 v2.4 execution and proof-state receipt
**Date:** 2026-10-22 | **Parent source:** PR #391 head `1444359cc7d4e7603f3de00e270e2ffcd4d34429` | **Branch:** `research/thm534-v24-positive-resource-carrier-20261022` | **State:** constructor PASS_SCOPED; **Physical promotion: 0**.

## Source and claims
- [v2.4 theorem manuscript](THM534_GLOBAL_POSITIVE_RESOURCE_CARRIER_AUDIT_v2.4.md)
- [v2.4 typed claim/dependency delta](THM534_GLOBAL_POSITIVE_RESOURCE_CLAIM_LEDGER_DELTA_v2.4.md)
- [Exact GitHub reproducibility script](verify_thm534_global_resource_v2_4.py)
- [Numerical GitHub reproducibility script](verify_thm534_complex_carrier_v2_4.py)
- Historical [v2.3 proof and candidate interaction](https://github.com/ud-tetra/UD/pull/391).
- P3 NO-GO remains in the original real cotangent carrier; P4–P7 are **new, separate complex symplectic carrier** results. Never silently reuse the original real Q171 support amplitudes as identical complex `psi` objects.

## Local constructor checks — completed
- `/mnt/data/thm534_v24/verify_v24.py`: 6,561 exact mixed gate words, strict nonnegative diagonal dominance, explicit three-parameter cotangent runaway, symmetric double-wake, isolated 3/5/2/5 fractions **PASS**. SHA-256: `2cf9c57631d021708d971e07a761e7fb6fb1db38da99323fd4c9f0c745c68118`.
- `/mnt/data/thm534_v24/verify_v24_numeric.py`: 256 binary complex Hermitian spectra and 250 continuous-profile complex-state derivative controls **PASS**. Smallest tested binary matrix eigenvalue `1.7639320225002098` (floating estimate), max reported derivative/stock residual `7.105427357601002e-15`. SHA-256: `97dfa686731d579e825511a05d36f717a7ae35c0b64c61e2acd7294677fff252`.
- Theorem manuscript SHA-256: `81862d5cd2c98b5717854db7415db8a3c84ec31b4cc28b44c6c749963b1e747c`.
- Ledger delta SHA-256: `d6de23f06dd1da9bdd710281f75f5897c5ec1ca3509add3cba6c55a1394f3dde`.
- The complete local release ZIP (including exact locally executed source, manuscript, proof ledger and manifest) is available in the conversation. The **published GitHub verifiers are shorter standalone adaptations**, not asserted byte-identical to the locally executed scripts. GitHub source readback confirms publication but **does not count as an independent execution**.

## Exact no-go and positive alternative
1. Canonical real dual `(x,y)`, unrestricted `y` and exact `x_dot=A(q)x` force `H=y^TAx+K(x,q,p)` unbounded below for `Ax !=0`, regardless of bounded positive source potential.
2. Changed complex `psi in C^9` gives a *conditional* positive Hermitian carrier energy `H_c=K+psi*(4I+iA(q)+Σ U_e P_e/2)psi >= K+R>=0`. Its support continuity is the **complex Re-bilinear extension**, not the frozen real Q171 current as the same object.
3. Isolated real-prepared contact keeps v2.3 funding `K+R=beta*S/2`; on arrival 3/5 kinetic, 2/5 potential.
4. Symmetric shared-face rest with two equal candidate contacts gives **both accelerations beta/2**; no unique exclusive contact selection.
5. Physical action/energy, native carrier choice, gate reset, source measure, historical THM-534 Markov probabilities and independent empirical evidence remain OPEN.

## Governance
This is target-exposed **mathematical development**, not a preregistered test of a new physical observable. New Hamiltonian lower-bound shift `4||psi||^2` is mathematically sourced to maximum Kminus contact degree and does not create physical positive energy or a reservoir. Constructor-only checks; non-constructor independent adversarial review PENDING. **No registry promotion, Physical Promotion 0.**
