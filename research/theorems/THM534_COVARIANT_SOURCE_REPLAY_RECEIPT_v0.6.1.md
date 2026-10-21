# THM-534 v0.6.1 constructor replay receipt — 2026-10-21

**Status:** PASS_SCOPED, constructor-only; independent non-constructor review PENDING; **development/no registry promotion**, **physical promotion 0**.

**Source:** [v0.6 source/continuity theorem](THM534_COVARIANT_SOURCE_CONTINUITY_v0.6.md); [v0.6.1 typed amendment, S14–S17](THM534_QUADRATURE_FLUX_TYPING_AMENDMENT_v0.6.1.md); [typed claim-ledger delta](THM534_COVARIANT_SOURCE_CLAIM_LEDGER_DELTA_v0.6.1.md).

## Reproduction
Four locally executed scripts were run sequentially on the development container. The corresponding GitHub verifier files are published compact adaptations; their bytes are **not asserted equal to the locally executed sources**. GitHub scripts were read back using repository file API. Readback does not constitute a second computational run.

| Local executed script | SHA-256 (local executed bytes) | Result |
|---|---|---|
| verify_thm534_covariant_source_v0_6.py | 4e27101df06e806b2eb47c7ebddfd6811beb9de81be9fd1430e48fa1a6fe380b | PASS: signed boundaries, exact source minimizer, j=4 8/5 + 4/5 receipt, 15 local Cayley flux checks, S16 compatibility |
| verify_thm534_endogenous_phase_v0_6.py | b299d171a1a437bd52f3b156c7a6c3cfc691b8714e7ff260e9261d15732d9776 | PASS: 30 update checks, max flux residual 6.106226635438361e-16; 10-step real-flat control |
| verify_thm534_quadrature_flux_typing_v0_6_1.py | f84a614cfccf87ec3e82493647795c4452ac6e0559835fcccbd1fefb7620b429 | PASS: three exact counterexamples showing imaginary quadrature != real conserved norm-flow and moduli cannot determine source sign |
| verify_thm534_source_norm_bound_v0_6_1.py | 18eb5ce8de8a360adbbb7afa1a03647ad13530cfaceca2fe326ecba916372ca4 | PASS: 70 states × 15 updates, h=0.03/0.2/0.7; max norm drift 1.9984014443252818e-15, max local flux residual 3.3393426912553537e-16 |

**Replay bundle:** \`THM534_COVARIANT_SOURCE_v0.6.1_REPLAY.zip\` is a local generated conversation artifact containing exact executed local scripts and MANIFEST.json (not uploaded into the UD Git repository). The GitHub branch contains the standalone manuscript and separately captured replayable scripts.

## Scope: what was and was not verified
- **Exact within assumptions:** S10 conditional nonflat source receipt; S11 chain-amplitude norm continuity and local antisymmetric flux; S14 quadrature/flux separation; S15 modulus-only source no-go; S16 defect-square compatibility; S17 source/curvature norm bounds.
- **Candidate only:** sine source functional \(U-j\sin\phi\), marked edge–face event, and endogenous phase-quadrature selection rule.
- **Not derived:** native UD packet-burden/current conservation from \((\rho,\theta,\chi,\sigma,b)\), physical action/energy or proper time, Born or six-edge Markov readout, microscopic THM-534 transition weights, physical U(1) coupling.
- **Original source gap:** historical THM-534 microscopic derivation remains unrecovered; v0.5 no-go for pure source-free seam chain closure is preserved.
- **Review:** no independent proof replay, no blinded preregistration (historical target already exposed), no CRL/physics promotion.

**Next gate:** derive from admitted packet constitutive dynamics an oriented source law and reciprocal burden/reservoir receipt, including metric and seam-site selection; compare with independent controls and obtain non-constructor review. No structural algebra alone can identify physical stress-energy.
