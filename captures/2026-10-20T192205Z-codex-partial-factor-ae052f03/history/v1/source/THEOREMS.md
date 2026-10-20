# A posteriori bounds from a retained partial factor

Development — no registry entry. Physical Promotion=0. External promotion review PENDING.

Let Z be a real m×n matrix, q≤min(m,n), U and V be the saved m×q and n×q retained factors, and S=diag(s1,…,sq) have descending positive entries. Assume certified operator bounds

    ||UᵀU−I||≤a<1, ||VᵀV−I||≤b<1, ||ZV−US||≤r.

These can be supplied by exact Frobenius enclosures. They concern the actual saved factors. Hash identity binds evidence but does not prove these inequalities. This capture inherits the existing per-case exact norm certificates; it does not recompute their large matrix arithmetic or raw projections. It checks enclosure-square consistency and the saved singular array directly.

## Partial-factor floor and restricted conditioning

V has full column rank. For any coefficient vector c, the equation and Gram bounds give

    ||ZVc|| ≥ [sqrt(1−a) sq−r] ||c||,
    ||ZVc|| ≤ [sqrt(1+a) s1+r] ||c||,
    sqrt(1−b)||c|| ≤ ||Vc|| ≤ sqrt(1+b)||c||.

Consequently, on the q-dimensional subspace W=range(V) with its induced Euclidean norm, the least and greatest gains satisfy

    gain_min(Z|W) ≥ [sqrt(1−a) sq−r]/sqrt(1+b),
    gain_max(Z|W) ≤ [sqrt(1+a) s1+r]/sqrt(1−b).

All displayed lower numerators must be positive before dividing to bound an inverse or condition number. The Courant–Fischer singular-value variational principle gives sigma_q(Z)≥gain_min(Z|W). No assertion that W is an exact invariant or singular subspace is required.

For exact rational evaluation use sqrt(1−a)≥1−a, sqrt(1+b)≤1+b, sqrt(1+a)≤1+a and sqrt(1−b)≥1−b. If (1−a)sq−r>0, define

    ell = [(1−a)sq−r]/(1+b),
    h = [(1+a)s1+r]/(1−b),
    d = sq−ell = [sq(a+b)+r]/(1+b).

Then sigma_q(Z)≥ell>0, sq−sigma_q(Z)≤d, ||(Z|W)^†||≤1/ell, and kappa(Z|W)≤h/ell. The pseudoinverse is for the map W→Z(W). In particular d<2^-41 proves ONLY that proposal sq does not overstate sigma_q(Z) by 2^-41. It does not imply an absolute-error bound or a lower bound on the proposal relative to sigma_q(Z). It does not discharge PR281's two-sided ordered-error premise, nor prove automatic satisfaction of the original proposal-floor gate for other inputs.

If a separately justified tail enclosure sigma_(q+1)(Z)≤t also satisfies t<tau<ell, exactly q exact singular values exceed tau, with none equal to tau. This conclusion is conditional on that tail premise. A retained lower bound alone cannot exclude additional large singular values.

## Why the one-sided and restricted qualifications matter

Take Z=diag(5/3,1,0), U=[e1,e2], V=[(3/5,0,4/5),e2], S=I2. Both Grams are I and ZV=US exactly, so a=b=r=0. Restricted gains and condition equal1. Yet sigma1(Z)=5/3 and sigma2(Z)=1, giving ambient leading condition5/3. Thus the partial-factor premises do not imply two-sided ordered singular-value accuracy or that the restricted condition equals an ambient leading-spectrum condition. This rational example is a logical countermodel, not a failure of the fixed floating backend.

Likewise Z=diag(2,1), q=1,U=V=e1,S=[2] satisfies exact retained conditions but has two singular values above tau=1/2. A tail bound is indispensable for exact cutoff count. Cutoff equality at either end is not strict certification.

## Applied scope

Apply to the two unchanged maximal-encoded-noise computational records from PR279. The source upper bound on sigma210 is inherited from the pinned nominal-order certificate plus the SAME exact rational noise multiplier C and original delta0=3*2^-49. No tighter retrospective noise radius is substituted. The separately checked saved singular list still contains209 entries strictly above tau=2^-24. The per-case retained Gram/equation certificates remain inherited premises; the new rational consequences do not constitute a fresh large-factor or raw-record audit.

The reporting condition threshold1888 is only an outward summary of calculated bounds. It is not an acceptance cap, theory constant, native1893-coordinate condition, full Hankel condition or finite-field result. No source singular spectrum, exact spectrum(T), primitive-frequency unaliasing, physical six-ratio accuracy or hardware claim follows. No new estimator call, raw generation or factor copy occurs. Actual all-history backend conformance B0–B6 and independent acquisition/calibration requirements remain OPEN. Earlier gates and HOLD/NO-GO verdicts remain unchanged.
