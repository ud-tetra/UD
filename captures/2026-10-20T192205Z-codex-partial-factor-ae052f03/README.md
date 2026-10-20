# Partial-factor posterior certification

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

This capture derives additional rigorous, conditional consequences of two unchanged saved floating-estimator outputs from PR279. It executes no estimator, raw generation, raw projection, large factor-norm recomputation or factor copying. The existing exact retained Gram/equation norm statements are inherited premises; saved singular entries and exact enclosure-square consistency are rechecked directly. This is post-hoc analysis of known outputs, not blinded or prospective validation.

## Results

For Z, retained U,V and diagonal proposals S, let a,b bound both retained Gram defects and r bound ||ZV−US||. With sq>0 and (1−a)sq−r>0, exact rational bounds are

    ell=[(1−a)sq−r]/(1+b),
    h=[(1+a)s1+r]/(1−b),
    sigma_q(Z)>=ell, kappa(Z|range(V))<=h/ell.

The restriction uses the Euclidean norm induced on the q-dimensional right-factor range; it need not be an exact singular subspace. Its pseudoinverse norm is at most1/ell. No complete321-column left factor is required for these bounds.

| Saved case | All321 ordered proposal overstatement upper (outward summary) | qth proposal overstatement upper (outward summary) | Restricted condition upper (outward summary) |
|---|---:|---:|---:|
| boundary_pair_block | 3.530e-13 | 4.739e-14 | 1887.238 |
| boundary_pair_rotating | 3.384e-13 | 4.674e-14 | 1887.238 |

Both all321 overstatement bounds are strictly below2^-41. Every retained prefix inherits the same Gram/equation bounds, so sigma_j(Z)>=[(1−a)sj−r]/(1+b) for j<=209. The largest retained overstatement debit occurs at s1. For the remaining112 proposals, sigma_j(Z)>=0 and descending saved proposals give overstatement<=saved_s210. Taking the maximum proves the all321 one-sided bound. Exact rational pairs are in primary/CERTIFICATE.json. Display decimals are reporting relaxations, not new operational acceptance caps.

Both qth posterior lower bounds exceed0.00288043008098 and improve the inherited source lower bound. Restricted condition is <1888 and inverse norm <348. Combining the posterior lower with the unchanged, inherited original-radius tail upper approximately1.0656170268898675e-10 gives exactly209 exact singular values strictly above2^-24, with no equality. That is cutoff count, not algebraic rank209. The source tail and nominal-order proof remain inherited, not rederived.

## What remains open

One-sided overstatement does not bound underestimation or absolute indexed error. It does not discharge PR281's two-sided B1 premise or prove automatic satisfaction of the original lower proposal-floor gate on other histories. It does not imply ambient leading-spectrum, full-Hankel or native1893-coordinate conditioning. Rational countermodels explicitly demonstrate these missing implications; they are not actual failures of the frozen SciPy backend. The unchanged previous operational profile, saved output verdicts and prior HOLD/NO-GO results remain intact.

Actual all-input backend conformance B0–B6, whole-program correctness, exact spectrum(T), primitive-frequency unaliasing, independent physical acquisition/calibration, SI or six-ratio accuracy and native1893/747 recovery remain OPEN. No new acquisition search, outreach, hardware execution, public-site or Project-board update occurred.

## Reproduction and provenance

Use partial/derive.py with --repo /absolute/UD and --out /absolute/new-output, setting PYTHONDONTWRITEBYTECODE=1. It checks partial/FREEZE.json source hashes and code identities, rechecks saved singular ordering/rank cutoff and square-enclosure consistency, then evaluates exact Fraction consequences. It does not validate the original norm measurements merely by checking hashes. Compare output CERTIFICATE.json and CONTROLS.json byte-for-byte with primary; replay retains matching output. The independent reviewer separately implements Fraction arithmetic and countermodels. That same-team review is not external promotion authority.

Active source/results are V3. V1's original qth result and V2's source-binding hardening remain under history/, with version notes; V3 adds the prefix extension. No earlier mathematical conclusion was retracted in this capture. The session-wide retraction ratio cannot be computed from this scoped capture. Supplied governance bytes remain exact. Protocol error/reporting budgets are O03 controls, not theory constants.

Gap2_FINAL_Finite_Genesis.png is unavailable and unused. Notes and ASTER are available but unused. Publication, CI, merge and tracking receipts are reported after completion; this immutable capture does not preclaim them.
