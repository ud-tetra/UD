# Uniform ideal-family frame and nonunique phase enclosure

Development; Physical Promotion=0. Same-team derivation, not external review. No new records, estimator fits, SVD executions or returned phase-output evaluations occur here. The PR233 family and all prior finite-output certificates remain unchanged.

## 1. Exact family and norm provenance

Use the PR233 closed preparation/noise family: exact same-parity orthogonal37-by-37 T within operator radius2^-20 of one of its six anchors; nominal coordinatewise nearest rounding at h=2^-48; encoded E in hZ with each preparation/time62-vector norm at most1127h. Its exact8191-by-321 projected matrix Z satisfies

sigma209(Z)>=gamma,
||Z-Zstar(T)||F<=tau,
rank(Zstar(T))<=209,

where Zstar(T)=Ystar B_T S lies in the fixed209-clock temporal span. Here gamma is the validated PR233 sigma209 lower, about0.0016037985060919312. The stronger source-error bound is explicitly

tau=kA*((d0+h/2)*sqrt(n)+delta*sqrt(v)),

with n=18,790,154, v=303,067 and kA squared738137/4096. It is recomputed from the source model. A sigma210 upper alone would not identify this Frobenius approximation or its source span. For the wide family, tau is about2.979654257365468e-8.

Since gamma>tau, Weyl implies sigma209(Zstar)>=gamma-tau>0. Thus Zstar has rank209 and its column span equals the fixed209-dimensional clock span Sstar. All following statements use that span equality. Rank preservation alone, without source-error and excitation margins, would not suffice.

The pinned baseline U0 has Gram defect eta0 and source reduction D. The old receipt supplies an OPERATOR bound s0 on ||Phi-U0 D||2 and an inverse bound hD on ||D^-1||2. Inspection of the original certify.py confirms s0 was computed by an operator Gram bound plus the source-evaluation allowance. It is not a Frobenius residual. The source inverse norm includes the old inverse-residual factor: hD=source_inverse_norm/(1-source_inverse_residual).

Let Q0=polar(U0). Because

sigma_min(Phi D^-1)>=sqrt(1-eta0)-s0*hD>0,

Phi has rank209. Its columns span Sstar. Projection therefore gives baseline-to-source sine bounds

t0,2 = s0*hD/sqrt(1-eta0),
t0,F = sqrt209*t0,2.

The sqrt209 is necessary for the Frobenius statement absent a separate Frobenius span certificate. In BOUNDS.json, source_rank_margin_lower is the displayed singular margin for the SCALED frame Phi D^-1, not for unscaled Phi.

## 2. Exact leading-SVD subspace and frame

Let Q be an orthonormal basis of the exact leading209 left singular subspace of Z. Its retained singular equations and projection off Sstar give

||(I-Pstar)Q||2<=tau/gamma,
||(I-Pstar)Q||F<=tau/gamma.

The denominator is gamma, because these are singular equations of actual Z; replacing it by gamma-tau would be safe but weaker. The cutoff gap also makes the retained subspace well-defined even if singular values inside it repeat.

For equal-rank orthogonal projectors, operator distance equals the largest principal-angle sine and Frobenius distance divided by sqrt2 equals the Frobenius norm of all principal-angle sines. Their triangle inequalities therefore give simultaneous bounds relative to Q0:

t2=tau/gamma+t0,2,
tF=tau/gamma+t0,F.

When t2<1, one common orthogonal alignment has

c=sqrt(2/(1+sqrt(1-t2^2))),
d2=c*t2,
dF=c*tF.

The existence of a source-coordinate approximation X to Q with

min_X ||Q-U0 X||F<=tF

follows from orthogonal projection onto span(U0). It is not a guarantee that an arbitrary floating auxiliary-X proposer returns the minimizing coordinates. The old raw-frame policy measures its actual proposed-X residual and remains a separate gate.

## 3. Exact ideal lag-two least squares

Write A=Q[:-2], B=Q[2:] and Tideal=A^dagger B. The pinned normalized baseline comparison has Frobenius residual sigma0, operator norm at most M0 and deleted-row margin beta. Its sigma0 is Frobenius-derived in the parent receipt; the baseline reduction/source-inverse norms are operator bounds. If dF<beta, the common alignment gives

sigma_min(A)>=beta-dF,
||B-A*Tideal||F<=JF=sigma0+(1+M0)*dF.

This follows because an aligned baseline comparator has residual at most JF, and exact least squares is the orthogonal projection residual. No numerical normal-equation error exists in this IDEAL lane. Neither the saved baseline transition nor a future returned transition is silently assumed exact least squares.

Subtracting the actual ideal and saved baseline shift equations bounds the normalized transition difference by

b=[sigma0+JF+dF*(1+M0)]/(beta-dF).

This deliberately uses the conservative common Frobenius frame bound for all terms. An operator-only refinement could use d2 and the projection residual's operator bound, but is unnecessary for the present nonunique result.

Let k0=sqrt((1+eta0)/(1-eta0)), dD be the pinned source-reduction operator norm and LJ its intertwining residual with the exact normal source clock matrix J. Set

K=k0*hD*dD,
L=hD*LJ,
R=L+K*b.

The hD*LJ term has no extra k0: it is the residual after conjugation by the normalized source reduction. The transition-operator perturbation receives k0. These are exactly the source similarity factors in the finite-output parent proof.

## 4. What the wide enclosure certifies

The source J is normal and has unit-circle spectrum. Every eigenvalue of Tideal lies within R of SOME source eigenvalue by normal-source resolvent/Bauer–Fike containment. For R<1, the ideal eigenvalue is nonzero and its circular phase is within asin(R) of some source phase. Overlapping disks do not give a target permutation or guarantee that every target is represented.

For the PR233 wide family, directed scalar arithmetic gives:

| Quantity | Upper bound |
|---|---:|
| Aligned frame distance dF |1.8579692931167845e-5|
| Exact ideal LS shift residual JF |3.764682929814078e-5|
| Nearest-some-source eigenvalue radius R |0.008534149639382939|
| Nearest-some-source two-step phase error asin(R) |0.008534253235563631 radians|

The exact rational endpoints are in BOUNDS.json; decimals are only readable displays. This is a nontrivial uniform enclosure for exact leading-SVD/exact-LS reduced models, not a certificate of a particular floating implementation.

The old raw-frame residual budget about2.48958e-10 and source shift allowance about5.56321e-10 cannot be certified by these upper bounds. Likewise2R and2asin(R) exceed the source minimum chord about7.28542e-7, so unique/bijective target matching remains HOLD. An upper bound exceeding a gate is a failure of this sufficient proof; it is not a witnessed gate failure or a lower bound on the actual worst case. Earlier finite-pattern PASS/HOLD receipts are unchanged.

## 5. Explicitly conditional future floating-output inflation

PR233 cutoff count alone supplies no returned-basis quality. For a conditional full-factor lane, require a finite projection-aware orthonormalized data approximation Zhat whose ordered left singular frame is precisely polar(Ufull) for the SAME saved full returned factor. Its leading209 columns Qtop must have retained singular values at least gamma-eps2. Also require

||Zhat-Z||2<=eps2.

For the qualified Frobenius lane additionally require ||Zhat-Z||F<=epsF. A numeric operator gate does not imply the same Frobenius bound. With only the operator certificate, its projection onto the209 right singular vectors has Frobenius norm at most sqrt209*eps2; the script uses this projected inflation in its operator-only lane. All certificates refer to the exact mathematical Z; any backend projection/cast error must be included.

The off-source singular equations then give

t2=(tau+eps2)/(gamma-eps2)+t0,2,
tF=(tau+epsF)/(gamma-eps2)+t0,F,

where the operator-only lane substitutes sqrt209*eps2 for epsF. Require gamma>eps2 and t2<1. If eta bounds the FULL left Gram defect in Frobenius norm, p(eta)=eta/(1+sqrt(1-eta)) bounds its polar displacement in Frobenius norm. Polar normalization of all321 columns can change the first209 span. The separately normalized returned209 basis differs from Qtop by at most2p(eta), so conservatively add2p(eta) to both aligned distances after applying c(t2). This term is not needed if the quality witness directly uses the normalized retained basis and its singular equations, but no such different witness is assumed here.

For the same actual returned raw basis U=Qreturned*S and finite real transition T, let eta be the checked retained/full Gram cap and nu bound the EXACT measured normal residual ||Uminus^T(Uplus-Uminus*T)||F. Then

JFraw=sqrt(1+eta)*[sigma0+(1+M0)*dF],
amin=sqrt(1-eta)*(beta-dF),
H=sqrt(JFraw^2+(nu/amin)^2)

bounds the actual raw shift Frobenius residual. This is least-squares Pythagoras plus a measured normal-residual premise; no library-wide nu guarantee is asserted. Its normalized residual is at most H/sqrt(1-eta).

For actual saved eigenvectors V, diagonal Lambda and inverse proposal Hinv require rhoV=||V Hinv-I||2<1, inverse norm bound hV and eigenpair residual eV. The nearby diagonalizable correction has distance Delta=eV*hV/(1-rhoV) to T. Actual polar similarity multiplies Delta by ka=sqrt((1+eta)/(1-eta)). Thus

Rfloat=L+K*([sigma0+H/sqrt(1-eta)+dF*(1+M0)]/(beta-dF)+ka*Delta).

Each emitted circular phase is within asin(Rfloat)+validated_argument_error of SOME source target if Rfloat<1. It is not an exact-spectrum(T) or target-permutation theorem when the disjointness gates fail. Inserting the old quality caps conditionally gives about0.008534386751069158 radians for the qualified full-factor Frobenius lane, or0.008536139454507473 in the operator-only projected-F lane. Neither certifies the old frame/unique-phase policy. Eta, normal, eigenpair, inverse and emission gates must be measured separately on each future output; they do not follow from cutoff stability and cannot replace a data/basis-quality premise.

## 6. Narrowing without inventing a PASS

The same-rho one-quantum noise family still has a sufficient phase upper about6.71823e-5 radians. Even the optimistic zero-noise/zero-radius limit of this coarse proof has source-error floor kA*(d0+h/2)*sqrt(n), reference operator-to-Frobenius offset and phase upper about3.59802e-5. These formulas are monotone in nonnegative radius/noise, so merely shrinking those parameters cannot produce a unique-phase PASS through this proof. This does not prove the actual zero-noise family fails.

Useful future work would sharpen source-weighted/per-anchor error transport, obtain a separately norm-typed Frobenius source-frame witness, or verify actual returned factors/frames directly. No physical target or engineering gate has been backsolved or changed. The nominal observer kernel, apparatus qualification, source/SI mapping, two-step modulo-pi ambiguity and external review remain open or unchanged as previously recorded.
