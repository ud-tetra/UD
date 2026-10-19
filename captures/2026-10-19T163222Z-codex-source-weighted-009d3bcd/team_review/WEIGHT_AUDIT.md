# Same-team audit: source-weighted subspace bounds

Development — no registry entry. Physical promotion0. This review derives/audits proof conditions; no new weighted coefficients or numerical outcomes were computed. Same-team review is not externally independent review.

## Simple graph coordinates are not a meaningful first-order gain

For the normalized returned retained frame Qa, write Qa=Q0 C+Z with C=Q0^T Qa and Q0^T Z=0. If ||Z||2<=z2<1, then ||C||2<=1 and ||C^-1||2<=1/sqrt(1-z2^2). A graph comparator C^-1*Tbar0*C yields

Jgraph<=sqrt(1+eta)*[sigma0F+zF*(1+M0/sqrt(1-z2^2))].

The in-span correction is quadratic, but the graph condition factor is also quadratic. At tiny angles this does not remove the leading(1+M0) term and can even be slightly worse than Procrustes. An off-span temporal antiphase component can make Zplus and Zminus*T reinforce. Neither projection into least-squares residual space nor graph coordinates alone justifies a sqrt2 gain or removal of that leading term.

## Exact row-space construction is essential

Let C0 be the exact dyadic q-by-p baseline coefficient used in the pinned approximation U0*C0. Put G=C0*C0^T. Propose a dyadic q-by-q M, then construct K=C0^T*M in EXACT dyadic arithmetic. Set R=C0*K=G*M. If rho>=||R-I||2 and rho<1, R and M are invertible and

C0_dagger=C0^T*G^-1=K*R^-1.

Consequently ||F*C0_dagger||F<=||F*K||F/(1-rho) for any conforming F. A small right-inverse defect for an arbitrary K is insufficient: its columns could contain null(C0) components, so the corrected right inverse would not be Moore-Penrose. The exact C0^T*M construction supplies the missing row-space condition. A rounded matrix product must not silently replace that exact construction.

For orthonormal baseline Q0=U0*G0^-1/2, G0=U0^T U0, the coefficient is D=G0^1/2*C0. Its Moore-Penrose inverse is D_dagger=C0_dagger*G0^-1/2. Thus a weighted upper established through K requires the additional factor1/sqrt(1-eta0), where eta0>=||G0-I||2<1.

## Uniform encoded-noise weighting

At the frozen radius delta=2^-48, each encoded preparation/time block of62 raw differences is either zero or one signed quantum. Let S=A/128 and define row vectors w_ac=(A*K)[37c+a,:]. For every time,

||noise_row*S*K||2 <= delta/128 * sum_a max_c ||w_ac||2.

Therefore all8191 times satisfy

||noise*S*D_dagger||F
 <= delta*sqrt(8191)/(128*(1-rho)*sqrt(1-eta0))
    * sum_a max_c ||w_ac||2.

This is valid for arbitrary correlations; no independence is assumed. It is an encoded onehot-ball bound, not a generic real62-vector Euclidean-ball bound. For robust computation, form exact squared row norms of dyadic A*K, take exact integer maxima over the62 channels per preparation, then outward-round square roots and their sum. A floating argmax among uncertain norms is unnecessary.

The weighted baseline term is

||(B0-U0*C0)*D_dagger||F
 <= ||(B0-U0*C0)*K||F/[(1-rho)*sqrt(1-eta0)].

It must use the same pinned U0,C0, exact baseline hash and projection as the old residual. A cyclic anchor is not the baseline unless its known perturbation is removed. Exact cross-Grams or direct integer cancellation can certify the weighted residual; reject inconsistent negative exact squared residuals rather than clipping.

For a returned full-factor error Fsvd, use ||Fsvd*D_dagger||F<=epsilonF*||D_dagger||2 in the Frobenius-certified lane. An operator-only premise instead permits epsilon2*||D_dagger||F; do not infer epsilonF=epsilon2 without the established Frobenius construction.

## Scope of a weighted graph/Riccati improvement

The opportunity is to bound the directionally weighted perturbation ||Delta*D_dagger||F instead of replacing it wholesale by ||Delta||F/alpha. This can improve a conservative source envelope only if the newly certified weighted constants are smaller. It is a source-aware proof refinement, not an alteration of the raw noise domain, engineering gates, outputs or solver behavior.

Keep operator and Frobenius bounds explicit in any graph/Riccati closure, require a positive retained singular margin, and separately retain the actual floating normal-residual premise. A passing uniform residual upper would remain conditional on full-factor quality and the declared normal ceiling; a larger upper is proofHOLD, not observed failure. Existing finite certificates, same-basis obstructions and old HOLDs remain unchanged.

Freeze coefficient/inverse proposals, source hashes, exact-construction code and acceptance rules before evaluating the new constants. A zero inverse proposal must fail rho<1. Successful inverse closure must establish the exact row-space identity above, not merely reproduce a small floating residual. No external acceptance/review is inferred from outreach.
