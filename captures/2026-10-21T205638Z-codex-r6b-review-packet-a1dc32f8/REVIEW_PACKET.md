# R6b independent-review packet

**READY FOR REVIEW; REVIEW NOT PERFORMED.** Development — no registry entry. Constructor: Codex. Reviewers: none. Physical promotion: 0. The packet consolidates existing claims and reproduces their checks; it adds no physical identification or empirical evidence.

## Review objective

Determine whether the clean rational L=4 R6b reductions, component-conditional diagnostic, and stored-replay eigenvalue error budget follow from the pinned source equations and evidence. Review the mathematical implications as well as the programs. Constructor reproduction and passing CI alone are insufficient.

The six source PRs are drafts and unmerged at the recorded observation. Their exact commits are pinned below; review does not depend on their merge order or moving branch names. EVIDENCE_INDEX.json records each upstream manifest and all 44 inventoried file hashes. Three source files are separately pinned and checked. UPSTREAM_STATUS.json is a historical snapshot, not a live status claim.

| Evidence | Pinned commit | Primary role |
|---|---|---|
| [PR350](https://github.com/ud-tetra/UD/pull/350) | b6837b5c00a0235344c642b2cdfa9fb07914535a | Exact Theta spectrum and conditional diagnostic |
| [PR352](https://github.com/ud-tetra/UD/pull/352) | 524f180d3f903267925d48599add52acb9301d6b | Frozen development settings and serialized numerical replay |
| [PR354](https://github.com/ud-tetra/UD/pull/354) | 4afee8f58a24d398dc7f77c0355279c05ccd62e6 | Three depth1 two-coordinate reductions |
| [PR355](https://github.com/ud-tetra/UD/pull/355) | dd865ff16d102c6aa2a2e8ad2e08dcda17eaa85a | Varying-depth 32-coordinate reduction and profile bound |
| [PR356](https://github.com/ud-tetra/UD/pull/356) | 58fdeeb4858ae65aeb5c7edfc0f2030697910664 | Six-coordinate ground sector, root and channel-weight intervals |
| [PR358](https://github.com/ud-tetra/UD/pull/358) | 98d084191b2c6471b1e73aae2985abefc8bc80ff | Exact assembly-versus-solver eigenvalue error budget |

## Claims submitted for review

The identifiers below are packet-local review IDs, not new registry entries. CLAIMS.json maps each to its dependencies and evidence.

| ID | Claim and boundary | Evidence to examine |
|---|---|---|
| C01 | L=4 implementation has four disconnected 64-site Theta modules; its docstring's global-connectivity intent is not achieved | PR350 source reading and projector checks |
| C02 | Theta64 eigenvalues 0, 64 eta^6, 16 eta^4+48 eta^6, 12 eta^4+48 eta^6 have ranks 1,3,12,48 | PR350 exact reconstruction |
| C03 | Conditional within-component F separates component occupancy from internal localization; empty channel is undefined | PR350 contract, algebra and controls |
| C04 | Each depth1 coupled module has the exact two-coordinate invariant sector and unique negative root; both conditional profiles have F=1 | PR354 theorem and certificate |
| C05 | Varying-depth module embeds 32 coordinates, has one negative eigenvalue, and 0<F_Theta-1<B with B approximately 2.21122e-18 | PR355 theorem and exact inequalities |
| C06 | Its negative mode lies in six depth-orbit coordinates with inherited metric diag(1,3,12,1,3,12); certified root and weights follow | PR356 embedding, interval and variance checks |
| C07 | PR352 serialized arrays satisfy its frozen numerical checks; sigma=.00133 does not supply negative-low-mode coverage | PR352 receipt, payload and verifier |
| C08 | PR358 encloses true stored-matrix ground eigenvalues and separates assembly shifts from solver-return errors; all12 low-mode residual checks retain the original threshold | PR358 min-max/perturbation/variance proof and AUDIT.json |

C01–C06 are exact conditional mathematical claims under the declared source model. C07 is a numerical provenance/check claim. C08 supplies exact rational bounds conditional on the source anchors and immutable stored binary64 bytes. None identifies a particle or an energy/time unit. All require review before any requested promotion.

## Read order and main results

Start with the source `docs/hmulti_r6b.py` and the PR350 contract. Fix eta=185/192, delta=7/192, the depth rule, parity, clean graph and identity site metric before reading the reductions. The recovered archive is source data; do not execute its scripts for this review.

Then read PR354, PR355 and PR356 in order. The depth1 root is approximately -5.058799395853153e-10. The varying-depth root is approximately -1.6145247540177632e-8, with W_rho approximately 4.343066396722202e-9 and F_Theta-1 approximately 5.751575710350898e-19. These are dimensionless source-model quantities.

Read PR352's original receipt before PR358. Floating assembly shifts the four low roots upward by about 4.39648e-14. PR358's stored-matrix eigenvalue enclosures are narrower than 1e-23. The error budget does not silently replace the source model with the floating matrix, or treat eigensolver residuals as source-assembly checks. It does not certify floating channel profiles.

## Reproduce pinned evidence

Use a checkout containing this packet and Python 3 with NumPy. The prior recorded numerical environment was Python3.12.14, NumPy2.3.5 and SciPy1.17.0. The packet verifier does not call an eigensolver; it uses NumPy for payload checks and the prior numerical verifier. Exact certificate work uses standard-library fractions. A different numerical environment can change a displayed residual without changing the frozen acceptance rule.

Fetch the six exact commits if they are missing locally:

```bash
git fetch origin b6837b5c00a0235344c642b2cdfa9fb07914535a 524f180d3f903267925d48599add52acb9301d6b 4afee8f58a24d398dc7f77c0355279c05ccd62e6 dd865ff16d102c6aa2a2e8ad2e08dcda17eaa85a 58fdeeb4858ae65aeb5c7edfc0f2030697910664 98d084191b2c6471b1e73aae2985abefc8bc80ff
python3 captures/2026-10-21T205638Z-codex-r6b-review-packet-a1dc32f8/verify_packet.py --repo .
```

The verifier checks all44 upstream inventoried files and three source hashes, materializes disposable copies, and runs only seven explicitly selected fresh constructor checks. It does not execute recovered source scripts, rerun the original eigensolver, or modify any upstream capture. Six regenerated exact/assembly JSON results must equal their pinned originals; the PR352 floating verification is judged by its original thresholds rather than exact float-output equality. REPRODUCTION.json records this constructor run. Rerunning writes that local receipt; preserve a reviewer's own receipt separately and append it as a new capture rather than overwriting published evidence.

## Adversarial review questions

1. Independently enumerate the edges from the address rule. Does the implemented graph actually have the claimed connected components at L=4, and does the general N/64 reading need any level qualifications?
2. Reconstruct the Theta projectors and ranks without relying on the constructor's matrix builder. Are the spectrum coefficients and positive gaps correct?
3. Derive the conditional diagnostic from normalized probabilities. Test empty channels, one occupied module, mixtures, degenerate rotations and arbitrary scaling. Does any numerical floor mask an undefined profile?
4. Check each invariant embedding by hand on a representative group. Does HB=BK establish invariance, and is the complement bound strong enough to justify uniqueness of the negative mode?
5. Verify the Schur-inertia and interlacing arguments. Are the codimension-one restrictions positive as claimed? Could a zero or extra negative root have been missed?
6. In the varying-depth module, does positivity of the ground Theta vector justify strict nonuniformity? Check the depth-potential ordering over the whole certified interval.
7. Independently derive the six-coordinate quotient and its inherited metric. Does the integer embedding give B^T B=4G? Check every channel-weight multiplicity and the pairwise variance identity.
8. Check rational bisection signs, absence of negative poles, two-by-two reconstruction and outward interval arithmetic. Could a rounded display be mistaken for a certified endpoint?
9. Trace raw payload bytes through hashes and matrix ordering. Are the three depth1 byte matrices gauge equivalent, and does that permit the sparse three-module mixtures used in the audit?
10. Derive the stored lambda2 lower bound from the source codimension-one form and row-sum perturbation bound. Derive the residual-variance enclosure without assuming floating invariance of a source reduction.
11. Recalculate at least one assembly interval and one solver-error interval independently. Check all512-coordinate residuals use the original normalization and frozen 5e-12 tolerance.
12. Identify any unacknowledged use of physical targets, source changes, fitted tolerances, particle identification, or unit assumptions. Record any failure even if the constructor script passes.

Passing the supplied scripts confirms reproduction of this construction; it does not answer all12 review questions independently.

## Review receipt and decision boundary

REVIEW_RECEIPT_TEMPLATE.json is blank and explicitly unsubmitted. The reviewer should create a new receipt with identity, non-constructor declaration, reviewed commit hashes, independent methods, per-claim PASS/FAIL/OPEN findings, counterexamples, and limitations. Do not merely check a global approval box. Submit review evidence as a new append-only capture or PR. A mixed outcome must preserve which claims remain open or fail.

The attached CRL-2 governance requires non-constructor review and a custodian ruling for promotion. The historical replay was already exposed, and its own receipt states development freeze, not independent preregistration. Review now cannot retroactively make it target-blind or establish CRL-2b. Any future bridge needs its own source-selected observable and metric, action-unit map, pre-exposure registration, and the applicable review/blinded-execution gates. No CRL status is assigned by this packet.

This packet does not send a review request to a person, assign reviewers, merge upstream PRs, or alter governance. Independent review remains unperformed. Floating eigenvector/profile certification, particle correspondence and parameter-free physical action units remain OPEN. The missing `Gap2_FINAL_Finite_Genesis.png` is not a dependency and was not used.
