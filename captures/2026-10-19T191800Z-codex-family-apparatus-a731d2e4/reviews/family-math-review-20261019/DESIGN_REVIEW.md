# Uniform cutoff under bounded preparation remixing and per-vector noise

Same-team mathematical design review. No new records, estimator fits or phase outcomes are evaluated. Let h=2^-48 denote the raw quantum, reserving r=209 for the signal cutoff rank.

## Explicit premises

Flatten the raw observation tensor into Y0 of size8191-by-2294 with column index37c+a. There are n=37*8191*62 scalar entries and v=37*8191 preparation/time vectors of length62. Let B_T be the repeated preparation map on those columns; its operator norm equals that of the37-by-37 T, without an extra sqrt62 factor. The Frobenius norm F0=||Y0||F includes all channels/preparations/times in model units, not integer numerator units.

Assume there exists a specified exact source matrix Ystar with rank at most209 and entrywise error |Y0-Ystar|<=d0. This source rank/error statement is a pinned premise from the validated clock-family generation proof; encoded Y0 itself need not have exact algebraic rank209. Assume each family T is exactly real orthogonal, with the stated same-parity block structure. Exact rational/signed anchors Tj are members of the same domain.

Define the actual family matrix before sketching as

R(T)=round_h(Y0 B_T)+E,

where rounding is coordinatewise nearest with error at most h/2 and each preparation/time62-vector of E has Euclidean norm at most h. Then ||E||F<=h*sqrt(v). If claiming encoded records or the integer projection backend, also require E in hZ^n. Otherwise the theorem is valid for real matrices but it does not imply integer/dyadic encoding or exact int64 implementation. It is not the old ball about the original baseline.

The fixed sketch S=Aint/128 has a validated operator upper k. The Frobenius upper k=||Aint||F/128 is sufficient. The complete projected matrix is Z(T)=R(T)S; no full Hankel or dynamical observer claim is involved.

For each anchor, use the actual certified record

Zj=[round_h(Y0 B_Tj)+Ej]S,

with its own ||Ej||F<=h*sqrt(v) and a validated lower gj<=sigma209(Zj). Keep the anchor records, transforms, per-vector eligibility and cutoff receipts bound together. A lower bound from an unperturbed or differently rounded anchor is not interchangeable with gj.

## Anchor-distance lower bound

For ||T-Tj||2<=rho, repeated block structure gives

||(Y0 B_T)-(Y0 B_Tj)||F <= F0*rho.

Subtracting two nearest-rounding errors contributes at most h*sqrt(n). Subtracting the two admissible noise tensors contributes at most2h*sqrt(v). Therefore

||Z(T)-Zj||2 <= k*[F0*rho+h*sqrt(n)+2h*sqrt(v)] = D(rho).

Weyl yields sigma209(Z(T))>=gj-D(rho). For the union of equal-radius neighborhoods of all six anchors, g=min_j gj is sufficient. A Frobenius-radius condition ||T-Tj||F<=rho implies the needed operator-radius condition, so the same formula also covers that smaller family. No extra sqrt62 or sqrt37 multiplier belongs in F0*rho.

## Uniform tail bound, independent of anchor distance

Orthogonality gives ||(Y0-Ystar)B_T||F=||Y0-Ystar||F<=d0*sqrt(n). The rank of Ystar B_T S is at most209. Hence

sigma210(Z(T)) <= k*[(d0+h/2)*sqrt(n)+h*sqrt(v)] = tau.

This bound does not depend on rho. Same-parity preservation is sufficient to keep each preparation in the declared clock class, but is not mathematically necessary for this global rank/Frobenius argument: any orthogonal preparation map preserves the aggregate temporal column span and source-error norm. If the accepted stored T is only approximately orthogonal, an exact ||T||2 upper must multiply the source-error term instead of silently using1.

## Positive common radius and exact threshold statement

Let c=2^-24. Require tau<c and

m = g-c-k*h*(sqrt(n)+2sqrt(v)) > 0.

For F0>0, every radius satisfying

rho < m/(k*F0)

then guarantees sigma209(Z(T))>c and sigma210(Z(T))<c, uniformly for every allowed T/E in those neighborhoods. Exactly209 singular values exceed the unchanged cutoff. An implementation can choose a downward dyadic radius, but must verify the original strict inequalities at that exact radius before freezing a closed-radius family. Equality or inconclusive directed comparisons are HOLD. The radius expression is a sufficient contour, not a necessary excitation limit or failure boundary.

This is a statement about the exact projected matrices. It does not prove floating SVD convergence, retained-factor quality, the fixed normal-residual cap, eigenpair/inverse gates, emitted phases, all-eight-gate policy admission, or physical source/apparatus qualification for all members. Those need separate returned-output certificates.

## Limits of broader claims

Orthogonality and source-rank preservation alone do not give global excitation through a fixed sketch. For a two-coordinate example embedded in one same-parity preparation block, take a rank-one row source along e1 and sketch S=e1. An orthogonal quarter-turn moves that source direction to e2 and annihilates the observed signal. Thus an unrestricted same-parity orthogonal family can lose observed rank even though its unsketched rank and norm are preserved. This generic counterexample does not claim such a failure for the actual fixed600-cell-derived data; it identifies why the anchor neighborhood/margin premise is necessary.

The uniform tail proof is stronger than a radius-dependent bound, but says only that at most209 singular values can exceed the cutoff. Excitation of all209 is supplied by the anchored lower bound. A source dimension of209, trace conservation or preparation orthogonality cannot replace that lower-margin certificate.

The two-rounding/two-noise anchor bound is conservative and generally remains nonzero as rho tends to zero. At an exactly identical transform its rounding differences can cancel, but a general real neighborhood may cross rounding boundaries. No smooth or Lipschitz rounding map is assumed.

Physical Promotion=0. Same-team review; external review pending. No new empirical or SI interpretation.

## Additive larger-noise family

The same proof supports a family perturbation E with per62-vector norm at most delta, while anchor noise Ej still has norm at most h. Replace the two-noise term2h*sqrt(v) by `(delta+h)*sqrt(v)`, and the uniform tail becomes

B(delta)=k*[(d0+h/2)*sqrt(n)+delta*sqrt(v)].

Choose delta=m*h with integer m>=0 if a quantum-multiple radius is desired. This is a Euclidean vector-ball radius; it does not mean that only m coordinates or one coordinate may vary. For encoded observations impose E in hZ^n separately. A sufficient source-only half-cutoff design requires B(delta)<c/2 and a positive remaining excitation margin

G = g-c-k*[h*sqrt(n)+(delta+h)*sqrt(v)] > 0.

Choosing a fixed positive power-of-two radius rho strictly below G/(2*k*F0) is sufficient for a closed-radius family: it leaves at least half the remaining margin for the transform perturbation. The selected exact radius must be substituted back into both strict cutoff inequalities before publication. Neither the half-tail nor half-margin choice is necessary for exact threshold stability; they are explicit conservative design budgets.

The maximum integer satisfying this particular half-tail upper-bound contour is `ceil(mcrit)-1`, where

mcrit = [c/(2*k)-(d0+h/2)*sqrt(n)]/[h*sqrt(v)].

It can be certified by B(m*h)<c/2 and B((m+1)*h)>=c/2. Flooring a directed lower bound and then subtracting1 is safely conservative but is generally not maximal. State which construction is used. Even contour maximality is not an actual noise-tolerance limit, since the Frobenius sketch bound and source-error budgets can be loose.

For the actual source waveform, the shared parity-dependent rate and alternating jitter do not increase the209 temporal rank: each parity/frequency has only the two common functions cos(psi_p,j(k)) and sin(psi_p,j(k)); fixed preparation origins enter coefficients. The time parity factor is already inside those shared functions, not an independent freely adjustable coefficient family. This is a two-step clock-family rank statement, consistent with the pinned source proof.
