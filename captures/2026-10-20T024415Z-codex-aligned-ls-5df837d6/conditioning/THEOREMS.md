# Gauge-aligned input conditioning and exact least-squares control

Development — no registry entry. Physical Promotion=0; external promotion review PENDING. This extends the PR254 retained-equation implication, not a new universal convergence theorem. Source rank209/frame/target premises remain inherited and hash-bound.

## Projector and coherent alignment

Let Zbar have rankq209 and orthonormal range frame W0. The original encoded baseline Z0 obeys ||Z0-Zbar||<=r. At per62-vector noise delta0=3*2^-49 the exact unchanged sketch obeys ||Z-Z0||<=C delta0. Let Z'=Z+E, ||E||<=zeta. Thus ||Z'-Zbar||<=e=r+C delta0+zeta.

Suppose a FUTURE returned q-column tuple actually satisfies ||Z'V-U Sigma||<=xi, ||U^TU-I||<=etaU<1, ||V^TV-I||<=etaV<1 and Sigma real diagonal with minSigma>=s*>0. Let R=(U^TU)^(1/2), Q=U R^-1, P=QQ^T and P0=W0W0^T. Then

 t=[e sqrt(1+etaV)+xi]/[s* sqrt(1-etaU)],
 ||P-P0||<=t.

Proof of offspan bound: (I-P0)U Sigma=(I-P0)(Z'-Zbar)V-(I-P0)F. Multiply on the right by Sigma^-1 R^-1 in that order; these factors need not commute. Equal-dimensional principal-angle blocks give ||P-P0||=||(I-P0)Q||. For a block with cosine c, projector difference eigenvalues are +/-sqrt(1-c²); common-range blocks have difference0. If t<1, right orthogonal O exists with ||QO-W0||<=d=t sqrt(2/[1+sqrt(1-t²)]). Sign/gauge choices do not change P. This bound is to the source subspace, not a statement that raw U is close to one selected SVD gauge or inside PR260's2^-49 box.

For saved shift T the normalized shift is TQ=R T R^-1; after aligning QO the shift is O^T R T R^-1 O. The residual is (Uplus-UminusT)R^-1 and has norm<=sA/sqrt(1-etaU). With source deleted-row singular lower beta, source comparison J satisfying ||W0plus-W0minusJ||<=lag0 and ||J||<=M0, beta>d yields

 ||O^T TQ O-J|| <= b=[lag0+sA/sqrt(1-etaU)+d(1+M0)]/(beta-d).

The beta-d denominator and polar similarity are essential. Raw T must not be identified with an orthogonally aligned shift without R. The unpolarized deleted basis has sigma_min(Uminus)>=sqrt(1-etaU)(beta-d).

The source normal-target transfer then uses Rtarget=hD*LJ+kappa0*hD*dD*(b+kappaA*eV*h/(1-rho)), with inherited source constants and kappaA=sqrt((1+etaU)/(1-etaU)). If Rtarget<1, 2Rtarget<sep and 2(asin(Rtarget)+a)<sep, the same resolvent-counting argument gives a bijective two-step target phase match. All future eigenpair/inverse/argument/encoding hypotheses must be checked; no arbitrary computed outputs are admitted by assuming a solver is stable.

## Exact least-squares map conditioning

Let A be full column rank, sigma_min(A)>=gamma>0, T*=A†B and R*=B-AT*, so A^TR*=0. For A'=A+DA, B'=B+DB with ||DA||<=alpha<gamma, ||DB||<=epsilon, the exact perturbed least-squares map obeys

 ||A'†B'-T*|| <= [epsilon+alpha||T*||]/(gamma-alpha) + alpha||R*||/(gamma-alpha)^2.

Indeed A'†B'-T*=A'†(DB-DA T*)+(A'^TA')^-1 DA^T R*. For source normalized A=W0minus,B=W0plus one may use ||T*||<=1/beta and ||R*||<=lag0; row deletions of an orthonormal frame are contractions. With aligned differences alpha=epsilon=d, this gives the recorded exact-map conditioning bound. Also ||T*-J||<=lag0/beta. These are exact arithmetic map statements, not a guarantee about an actual numerical least-squares implementation.

For ANY saved T and fixed A,B, N=A^T(AT-B) gives T-T*=(A^TA)^-1N. A separately certified positive lambda_lower<=lambda_min(A^TA) therefore proves ||T-T*||<=||N||/lambda_lower. This posterior exact residual certificate validates finite saved outputs without assuming an internal library rounding model. When changing to normalized coordinates, any such error needs the R similarity factor. Normal residual zero with nonzero primal lag is possible and must not be called zero data/model error.

## Rank selection and discrete qualification

Let s0 be the inherited exact encoded baseline qth-singular lower and tail0=min(baseline qplus1 upper,r). For input Z', singular values obey sigma_q>=s0-C delta0-zeta and sigma_qplus1<=tail0+C delta0+zeta. These follow from singular-value min-max perturbation and rankq approximation. The cutoff class is exactq when both straddle2^-24 strictly. A computed singular-value list with maximum absolute error STRICTLY less than the smaller cutoff margin would preserve that count. This is an implementation error requirement, not a proof that SciPy meets it uniformly. Proposed retained minSigma must separately satisfy s0-C delta0-zeta-2^-41>0; cutoff preservation alone does not prove this output premise.

Projection-conditionally an additional per-vector raw radius nu=zeta/C suffices for ||E||<=zeta, if layout/sketch/encoding/range checks and the stated per-vector contract hold. If nu<qraw=2^-48, the additional encoded lattice ball around a fixed record contains only zero. Likewise the total original-baseline per-vector ball has exactly the old zero/one/two-coordinate patterns while 2qraw²<=total_radius²<3qraw². Do not advertise a continuous bound as new encoded records, backend success, a rejected residual gate, SI/six-ratio or native1893/747 recovery.
