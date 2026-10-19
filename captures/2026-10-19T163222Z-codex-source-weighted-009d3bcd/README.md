# Source-weighted whole encoded-ball shift certificate

**The ideal exact-SVD/exact-least-squares shift bound now clears the unchanged published allowance over the entire admitted encoded ball. The bound at the existing returned-factor error ceiling remains HOLD. This is a shift certificate, not a universal floating-estimator or all-policy-gates certificate.**

PR #217 is merged at `cb47f5202e6b8fdac21a6804a10b1b2050c882fa`; its successful integrity CI and integration preserve the parallel APP04 capture. This new capture extends its coarse envelope without deleting it or changing a numerical gate. Development — no registry entry. Physical promotion 0.

## Quantified improvement

At per-preparation/time 62-vector encoded radius `2^-48`, with exact least squares:

| Basis/quality premise | PR217 upper | Source-weighted upper | Published shift allowance sufficient? |
|---|---:|---:|---|
| Ideal exact top209 SVD | <2.309064e-9 | **<4.339082e-10** | **YES, shift only** |
| Returned basis, actual helper's Frobenius-quality ceiling | <2.629186e-9 | **<7.540376e-10** | HOLD |
| Returned basis, abstract operator-only quality ceiling | <6.933911e-9 | <5.058853e-9 | HOLD |

The unchanged allowance lower is about `5.563206409135e-10`. These are upper enclosures: a HOLD is insufficient proof, not a lower bound on the worst case or an exhibited v2 failure. Earlier finite v2 PASSs and the directed fixed-basis old-gate obstruction are unchanged. A separate normal-equation ceiling produces the same Pythagorean returned-solve correction as PR217. The illustrative `2^-45` ceiling is not asserted for the three saved prior floating outputs.

## What makes the bound smaller

For the fixed baseline approximation `L0=U0 C0`, propose one binary64 LU inverse of `C0 C0^T`. Treat it as an untrusted auxiliary witness. Form `K=C0^T M` by exact integer products. The exact residual `rho=||C0 K-I||F<1` establishes the true pseudoinverse identity `C0†=K(C0 K)^-1`; row-space membership is essential. An arbitrary right inverse cannot be substituted.

The raw record's quantum is `2^-48`. Within a 62-vector Euclidean radius of one quantum, each encoded integer difference is zero or a single signed unit coordinate. Consequently every permitted time correlation obeys

\[
\|E S K\|_F\le\delta\sqrt{8191}\sum_{a=0}^{36}\max_{c=0}^{61}\|(S K)_{37c+a,:}\|_2,
\qquad S=A/128.
\]

The maxima and row-squared norms are exact integers; only square roots are enclosed. This covers the entire original **encoded lattice** ball. It is not an assertion about arbitrary real vectors in the same Euclidean ball; an exact counterexample is included in the controls. PR217's broader real-ball envelope remains available.

The baseline weighted error `||(B0-U0 C0)K||F` is computed directly using exact dyadic differences. Its bound is <2.602666e-13; the weighted noise multiplier is <52996.291; inverse closure is <2.290051e-13. These have different types from the old unweighted residual/noise constants and are not identified merely by numerical size.

Riccati self-map, contraction, and spectral-separation inequalities certify the leading singular subspace as a graph over the reference. Source weighting bounds the forcing through the full coefficient pseudoinverse instead of dividing all perturbations by the weakest singular value. The graph bound transfers to simultaneous Frobenius/operator basis distances, then to the unchanged shift residual and normal-residual formulas. See THEOREM.md and the retained same-team derivations.

## Source custody and scope

The nine source members are read from hash-pinned existing repository archives. They include baseline basis/coefficient data and three integer sketch chunks. The latter belong to the **cyclic perturbed record**, not to the baseline. The verifier subtracts the frozen cyclic channel/sign projection exactly, then checks the frozen baseline integer norm and its complete exact unweighted residual fraction. No raw-record generation or acquisition is run; no state-estimator fit/SVD is run. One auxiliary inverse proposal is created and retained as a witness.

The source order bound, prior raw custody/projection, parent full-factor norm semantics, and published allowance remain explicit dependencies. They are not silently counted as newly executed proofs. If their premises are revised, dependent claims require re-derivation. The PNG `Gap2_FINAL_Finite_Genesis.png` is unavailable and was not used.

## Verification and portable replay

Original numerical code/input hashes were frozen before the auxiliary proposal and new weighted calculations. The auxiliary proposal was then hash-frozen before verification. The replay/control supplement was frozen after the weighted results were known; no blinded preregistration is claimed. All bytes and receipts are retained.

Run from this directory with requirements.txt available:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python replay.py --repo /absolute/path/to/UD --out /absolute/path/to/new-review
```

The output directory must be new. Fresh data-only intake verifies 9 archive members (32,914,496 bytes), recomputes the exact weights and all 12 bound rows, and runs five scope/refusal controls. It reuses the frozen auxiliary inverse instead of treating floating regeneration as exact or forcing a particular output. The clean replay receipt/logs are included. Same-team graph replay and code/math reviews are not outside independence.

## Remaining frontier

The ideal shift inequality is closed at the original radius. Uniform floating-estimator admission still needs a stronger source-bound numerical-error argument and guarantees for the remaining output gates; the present returned-F ceiling alone does not close it. No radius, SVD gate, shift allowance, or phase target was relaxed. External review remains PENDING; the earlier sent request is not acceptance or a review verdict. No physical/SI identification, native full-Hankel extraction, or recovery of the nominal747-dimensional hidden observer space is established.
