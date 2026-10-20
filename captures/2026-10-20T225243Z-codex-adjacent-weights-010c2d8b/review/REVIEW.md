# C25 independent review: uniform grade rates and local column weights

Two distinct perturbation classes give different conclusions. Every constant nonzero uniform grade-rate triple preserves the nominal747-dimensional kernel for this downward-closed62-coordinate readout. A local whole-tetrahedron column weight can make the old fundamental-cycle preparation visible, while a moved stationary hidden line persists. No reduction of the total weighted kernel has been proved.

## General formula and the special subcomplex theorem

Write A=A1+A2+A3. The chain identities imply AiAj=0 for i≠j. The mutually orthogonal spaces Ei=im Ai and H=intersection ker Ai decompose the carrier. Ai is invertible and skew on Ei, and zero on the other summands. For nonzero constants ai, let G_lambda be the direct sum of complex channel eigenspaces whose weighted signed frequencies ai*omega equal lambda. Then exactly

    N_w complexified = direct_sum_lambda ker(R restricted to G_lambda),

including the whole harmonic space in G_0. This follows from linear independence of distinct exponential functions; cancellations within one shared frequency remain possible. With no cross-channel weighted-frequency collision the formula separates into H_dark plus three channel kernels. Commutation alone does not imply nominal-kernel invariance. For example, two identical independent rotation planes observed through the sum of their first coordinates have a dark difference plane at equal rates; it is not invariant under either individual rotation, and unequal rates expose it.

For the actual readout a stronger argument removes the noncollision requirement. Let R_k restrict to the k-simplices of the link L. Downward closure gives

    R1 B1^T = B_L1^T R0,     R2 B2^T = B_L2^T R1.

Suppose the weighted output of x_H+x1+x2+x3 is zero for every time. Time averaging first isolates R x_H=0 because all Ei motions have nonzero frequencies when ai≠0. Grade0 then sees only x1. Its zero lower-degree output makes the derivative of its grade1 output zero by the first restriction identity. That constant grade1 output must itself be zero: Ei has no stationary frequency. Removing this channel, grade1 sees only x2; the second identity similarly forces its grade2 output to vanish. The remaining grade2 output belongs to x3 and must vanish; C3 has no direct readout. Thus each channel is individually dark. Conversely a sum of individually dark channels and a dark harmonic is dark.

Consequently N_w=H_dark orthogonal-sum N1 orthogonal-sum N2 orthogonal-sum N3 for every constant ai≠0, independent of weighted-frequency collisions or signs. Comparing with ai=1 proves N_w=N_nominal of dimension747. Each Ai preserves this space. Any locally integrable real time-varying grade rates therefore also leave every nominal hidden state invisible. Only inclusion is claimed in that case: zero rates can freeze additional snapshot-dark states, so equality is not automatic. This proof uses subcomplex closure, not a new2640-dimensional rank calculation; the old1893/747 theorem remains an inherited premise.

## Local column weights: changed hidden line, not a rank certificate

Let B=B3 and D=I+epsilon P_J, with0<|epsilon|<=1/2. Replace the top block by B D and its Euclidean transpose D B^T. This is skew, adjacent-grade and has the same nonzero incidence support; B2 B D=0. The nonunit coefficients are a constitutive/basis weight, not new literal unweighted simplicial incidences, a Pachner move or a supplied physical law.

For the single tetrahedron tau=(0,33,34,41), source index0, exactly one facet belongs to L: (33,34,41), global output coordinate1680. The nominal normalized fundamental cycle h has tau coefficient+1/sqrt600. Hence the old preparation satisfies

    (R K_D h)_1680 = -epsilon/sqrt600.

It is therefore outside the new continuous kernel whenever epsilon≠0. Nevertheless z=D^-1 h satisfies K_D z=0 and Rz=0. An invisible stationary line persists. This proves the hidden subspace changes, not that its dimension shrinks or the full system becomes observable.

The declared C10 orbit J=[0,9,227,432,447,582,538,347,332,141] gives a symmetry-preserving example. Its ten tetrahedra share no triangular facet; the selected boundary columns have Gram4I. Thus ||K_D-A||=2|epsilon|. The vector B P_J h0 has squared norm40, and exactly two observed coefficients are nonzero, both+1 at global coordinates1680 and1689. Weighting the whole orbit preserves the signed C10 action; a single-cell weight breaks it. Both choices remain adjacent-grade and retain odd chain-parity anticommutation. For m=|J|, the angle between the old and new hidden lines in the fixed Euclidean x coordinates is

    sin²theta = m(600-m)epsilon² /
      [600((600-m)(1+epsilon)²+m)].

This follows by setting r=(1+epsilon)^-1, ||D^-1h||²=(600-m+m r²)/600 and <h,D^-1h>=(600-m+m r)/600. Exact source checks cover m1 and m10; this angle is not a total-kernel distance or rank claim.

## A finite response bound and its coordinate scope

Sparse source row counts give ||A||<=12. The column estimate gives ||K_D||<=13 and ||K_D h||=sqrt40|epsilon|/sqrt600<7|epsilon|/sqrt600 for the orbit example. At t=1/64 the named face's leading term is -epsilon/(64sqrt600). Odd chain parity kills the even Taylor terms in that face projection. The skew propagator has norm1, so the third-order integral remainder is at most t³||K_D||²||K_D h||/6. Relative to the leading term this is strictly less than1183/24576<1/16. The signal therefore has sign -sgn(epsilon), with magnitude strictly between15|epsilon|/(1024sqrt600) and17|epsilon|/(1024sqrt600). The same conservative bound also covers the single-cell example. This is a finite mathematical response certificate, not a noise tolerance, admission gate, experimental measurement or observability-rank certificate. If a total scalar error bound is independently justified under each of the nominal and alternative hypotheses, a budget below half the certified signal lower bound is a sufficient disjointness condition. It supplies no actual error evidence and must include preparation, readout, timing, modelling and numerical contributions applicable to each hypothesis.

Coordinate transport matters. Put F=diag(I,I,I,D), y=F x and H=diag(I,I,I,D^-2). Then

    K_y = F K_D F^-1 = H^-1 A,     R y = R x.

K_y is H-skew and ker K_y=ker A. This is equality of the stationary generator kernels, not equality of dynamical observer kernels for arbitrary H. Its numeric fundamental vector h remains harmonic because A h=0. The counterexample's fixed x=h preparation maps to y=D h; a fixed numeric y=h instead corresponds to x=D^-1h. Hence changing coordinates/metric cannot be described as exposing the same numeric fundamental vector in H^-1 A. Preparations, norms and readout must be transported together. Neither this rewrite nor chain isomorphism makes K_D a Euclidean similarity to unchanged nominal A.

Independent checks read only pinned archive JSON:1813 sparse/source checks verify boundary cancellations, both cochain restrictions and the single-cell witness; additional exact checks verify orbit support, response constants, angle formulas and row counts. An additional96 independent checks match all eight root angle/signal cases and their directed160-bit enclosures, including the conditional half-lower error budget. No archived program, raw acquisition, fit, SVD, estimator or large observation-rank computation was executed. Weighted full-kernel ranks and a justified physical perturbation class remain OPEN. Development — no registry entry. External promotion review PENDING. Physical Promotion=0.
