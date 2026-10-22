# Consistent finite element mass on the 12-cell octahedral refinement

22 October 2026. **EXACT conditional volume-mesh audit; constructor verified; physical promotion 0.** This capture extends the graphite manuscript draft in PR #412. It tests a concrete, conventional local *kinetic metric* rather than the reverse-engineered positive correlated witness. The tetrahedral volume is a mathematical test carrier, not a model of a one-atom-thick graphite sheet.

## Mesh and mass rule

Use the regular tetrahedron with vertices \((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\), its six edge midpoints, and centroid. The eight centered octahedral cells each have volume \(1/6\); the four corner tetrahedra each have volume \(1/3\). Their sum is \(8/3\), the original tetrahedron volume. For continuous piecewise-linear (P1) nodal scalar functions \(\phi_i\), take the consistent mass form \(M_{ij}=\int_\Omega\phi_i\phi_j\,dV\), in unit density/coordinate units. Each fine tetrahedron \(T\) contributes

\[
M_{ij}^{(T)}=\frac{|T|}{20}
\begin{cases}2,&i=j\in T,\\1,&i\ne j\text{ and }i,j\in T,\\0,&\text{otherwise.}\end{cases}\tag{1}
\]

The resulting 11×11 matrix is strictly positive definite: for nonzero nodal vector \(x\), the continuous P1 function has \(\int_\Omega(\sum_i x_i\phi_i)^2>0\). An exact rational LDL elimination verifies eleven positive pivots. Its entries vanish unless two vertices share a fine cell. The centroid and each original corner share no cell, hence \(M_{o,v_i}=0\).

## Fixed UD vertex injection

The UD subdivision \(S_0\) used in draft PRs #407–#412 inserts an old vertex chain at that same old vertex. It does not assign midpoint or centroid nodal values. For its uniform seed vector \(u=(1,1,1,1)^\mathsf T\), direct exact assembly gives

\[
S_0^{\mathsf T}MS_0=\frac1{30}I_4,\qquad
MS_0u=\begin{cases}
1/30,&\text{each old corner and each midpoint},\\
0,&\text{centroid}.
\end{cases}\tag{2}
\]

Multiplying the whole mass matrix by 30 makes the coarse pullback unit. The incidence covector then differs only across the six centroid–midpoint edges and has squared Euclidean norm

\[
\|\widetilde B_1^{\mathsf T}(30M)S_0u\|_2^2=6.\tag{3}
\]

This is above the sharp one-hop lower bound 4 in PR #410. For the Euclidean-normalized seed mode \(u/2\), the squared covector residual is \(3/2\). If one also chooses an algebraic unit edge metric \(H_1=I\), that is its instantaneous weighted edge action. The factor 30 is a *normalization for this comparison*, not a measured material mass or physical frequency. No damping or friction is inferred.

## Standard P1 interpolation is a different embedding

An ordinary finite element coarse-to-fine nodal interpolation \(T_0\) places value \(1/2\) at each incident edge midpoint and \(1/4\) at the centroid for each coarse hat function. Therefore \(T_0u=\mathbf1_{11}\), whereas \(S_0u\) vanishes on seven new vertices. The coarse pullback of the same mass form is

\[
(T_0^{\mathsf T}MT_0)_{ij}=
\begin{cases}4/15,&i=j,\\2/15,&i\ne j.\end{cases}\tag{4}
\]

This is exactly the consistent P1 mass matrix on the unsplit original tetrahedron. For the uniform coarse vector, the fine mass covector \(MT_0u=M\mathbf1\) has entries \(1/12\) at old corners and \(1/3\) at all midpoints and the centroid. Consequently

\[
\|\widetilde B_1^{\mathsf T}MT_0u\|_2^2
=12(1/3-1/12)^2=3/4.\tag{5}
\]

The coarse uniform vector remains a zero mode for the matched coarse mass form because the coarse mass row sums are equal. The fine weighted-incidence operator nevertheless mixes it under this P1 interpolation: the fine nodal mass row sums are unequal. Equation (5) is in the unrescaled unit-density volume convention and is **not** directly compared in magnitude with Eq. (3). The two embeddings must be specified separately in any proposed physical correspondence.

## Implication for the graphite program

A standard local volume P1 mass metric does not meet the exact seed-invariance condition under either vertex injection \(S_0\) or ordinary nodal interpolation \(T_0\) with the stated weighted-incidence rule. This does not rule out the correlated metric of PR #409, alternate discretizations, a two-dimensional sheet mass/elasticity construction, or changing the dynamical operator. It shows why simply calling the octahedral metric “ordinary mass” is unsupported. The actual graphite bridge must specify the physical field, atom-to-chain map, mass or response bilinear form, and damping/readout before the manuscript can predict the (2,1) residual peaks or load slope. The coefficient ledger v0.39(2) and proposed CRL-2 rules leave physical promotion at 0.

## Reproduction

Run `python3 verify_fe_mass.py`. It reconstructs the cells and all 30 edges, evaluates volumes and Eq. (1) with exact fractions, checks positive LDL pivots, and verifies Eqs. (2)–(5). `RESULTS.json` retains the values. This is a constructor audit of a specified three-dimensional discretization, not independent material review.
