---
title: "Finite Tetrahedral Complexes and Skew Hodge–Dirac Support Flow"
subtitle: "Paper I · Review edition 1.0"
author: "Benjamin Walker Mayes"
date: "16 September 2026"
---

**Independent researcher**  
ORCID: [0009-0002-5813-0724](https://orcid.org/0009-0002-5813-0724)

## Abstract

We study dimensionless linear algebra on finite oriented tetrahedral simplicial complexes. The setup is the standard simplicial boundary complex with its Euclidean inner products and skew Hodge–Dirac generator. We distinguish an eight-element binary space indexed by the three perfect matchings of \(K_4\) from a matching stabilizer of the same order. An explicitly defined edge projection partitions the labeled state set \(S_4\times\mathbb F_2^3\) into six fibers of size 32; this count carries no sequential interpretation. We give exact unique-simplex gluing identities and compute the spectra of three specified tetrahedral complexes. Irrational ratios of their nonzero frequencies exclude a positive exact period for each full flow. Recorded event data define affine maps on the binary space, with exact Hamming-sector transition ranks and a commutator identity. These conditional maps do not supply a pre-event source law. We separate norm preservation, changes of a second quadratic form, sector mixing and contraction effects. Proofs and a standard-library Python reproduction package identify precisely which statements are general and which concern the declared finite examples. These results are finite identities and no-gos on a declared simplicial carrier. They are not a derivation of spacetime geometry, gauge theory, or empirical couplings.

# 1. Scope and mathematical question

A finite complex, a linear evolution on its chain space, and a rule for changing the complex are different mathematical objects. This paper keeps them separate. It asks what follows exactly from a specified tetrahedral complex and a fixed skew generator, and what additional information is needed to define a discrete event map.

The starting point is conventional: oriented simplices form bases of real chain spaces; signed incidence defines the boundary; the boundary and its adjoint define a Hodge Laplacian. We use the skew combination of these maps to obtain an orthogonal flow. Norm preservation is a standard consequence of skew symmetry, not a new unification principle. The specific calculations concern a matching-indexed binary state, three finite glued complexes, and conditional maps determined by recorded finite data.

The notation is chosen to make each object recognizable before introducing any project terminology. A finite oriented tetrahedral simplicial complex is sometimes called a *packet complex* in the wider Unified Dynamics project. The Euclidean squared chain norm is denoted \(S_\mu\), or *support*. A *receipt* means only recorded finite data supplied to a stated map. None of these names changes the mathematical type of the object.

> **What this paper does not claim.** The finite chain space is not identified with physical space, a physical field, matter or energy. The evolution parameter has no assigned physical unit. The binary coordinates are labels, not measured degrees of freedom. No microscopic source of the event receipts is derived. No physical coupling, action scale, experimental validation or universal recurrence is inferred from the calculations. A structural or numerical correspondence with another construction would not, by itself, identify the two objects.

The result sequence is deliberately short. Section 3 defines the labeled state set and its symmetries. Section 4 fixes the chain convention and records standard operator identities. Section 5 establishes local norm balance and gluing accounting. Section 6 gives the exact A/B/C spectra and their recurrence obstruction. Section 7 is one conditional argument: given event receipts, the affine binary map is exact; the pre-event source of those receipts remains open. Section 8 distinguishes several often-confused notions of preservation. The claim table and executable checks provide a finite review surface.

Projective reconstruction is developed in the separate companion paper. Optical acquisition is a separate proposed protocol. Neither is required to prove a statement here.

# 2. Related work and the contribution boundary

Discrete exterior calculus, combinatorial Hodge theory, Dirac operators on complexes, lattice gauge theory and bistellar moves already supply much of the relevant mathematical language. They are the starting point, rather than discoveries of this paper.

Hirani's discrete exterior calculus [1] develops discrete forms and metric-dependent operators using primal and dual complexes. The present work uses a much narrower choice: an orthonormal simplex basis and ordinary transposes. It introduces neither a circumcentric Hodge star nor a convergence theorem for a continuum equation. The comparison is to the discrete incidence/adjoint construction; the thesis abstract and the author's overview [2, PDF pp. 1–3] identify this setting. We do not infer that the unit-weight matrices here approximate an externally specified metric.

Horak and Jost [3, arXiv version pp. 4–6, Definition 2.1] define the up, down and total combinatorial Laplacians using coboundaries and adjoints. Our block Laplacian is the unweighted, nonaugmented specialization of that familiar construction. Our calculation adds the explicitly listed spectra of the selected A/B/C complexes and their consequences for exact periods, not a new general Hodge theory.

Knill [4, pp. 1–2] describes \(D=d+d^*\), its square, and the simplex-incidence graph. His Section 17, p. 18, also uses \(d-d^*\) and its relation to the Laplacian. Accordingly, the skew operator and norm conservation below are standard setup. We apply them to a declared finite family and state exactly which inclusion is an isometry and which relabeling is a dynamical intertwiner.

Pachner's theorem [5] concerns equivalence of triangulations of piecewise-linear manifolds under elementary changes. Lickorish [6, p. 302, Definition 2.3; p. 315, Theorem 5.9] states the local bistellar replacement and the global equivalence theorem. We use the three-dimensional 2-to-3 replacement and verify its oriented boundary identity. We claim neither a new move nor the global equivalence theorem. Equality of the exterior boundary does not imply equality of the interior chain operator or its spectrum.

Wilson's lattice gauge theory [7, Section III, pp. 2448–2450] introduces gauge variables and gauge-invariant lattice constructions. A binary label permutation or a change of serialization forest is not thereby a lattice gauge field. There is no Wilson action or gauge-field dynamics in this paper. Kraus's operator formalism [8] is relevant only to the final distinction between an operator contraction and a norm-preserving map; no new dilation theorem is asserted. The cited article is the original operator-theoretic source, not a source for any physical interpretation of our chain coefficients.

The reviewable differences from these literatures are therefore restricted to the following constructions and calculations:

1. the explicit opposite-edge indexing of \(\Theta\cong\mathbb F_2^3\), distinguished from the matching stabilizer;
2. the selected unique-simplex A/B/C matrices, their exact spectra, and the irrational-frequency obstruction;
3. the receipt-conditioned affine \(\Theta\)-map and its exact transition counts;
4. a typed comparison of Euclidean norm, a second quadratic form, sector mixing and contraction effects.

The companion paper treats the reconstruction statistic, its parity-degree ambiguity and the frozen-tree covariance map. We do not assert a priority claim for general graph synchronization, linear covariance propagation, or sufficient data for sign reconstruction.

# 3. Labeled tetrahedral states

## 3.1 Vertices, edges and perfect matchings

Let \(V=\{0,1,2,3\}\) and let \(K_4\) be the complete graph on this vertex set. Its six edges are the two-element subsets of \(V\). Every permutation of \(V\) preserves adjacency, so \(\operatorname{Aut}(K_4)=S_4\).

The three perfect matchings are
\[
M_1=\{01,23\},\qquad M_2=\{02,13\},\qquad M_3=\{03,12\}.
\]
Each partitions the four vertices into two disjoint edges. A vertex permutation induces a permutation of this three-element set. Write
\[
\pi:S_4\longrightarrow S_3
\]
for that action.

**Proposition P3.1 (matching action).** The map \(\pi\) is onto and has kernel
\[
V_4=\{1,(01)(23),(02)(13),(03)(12)\}.
\]

*Proof.* Each listed double transposition preserves all three matchings. A transposition of vertices fixes one matching and exchanges the other two, and suitable vertex permutations therefore generate all permutations of the three matchings. The kernel of a surjection from a group of order 24 onto one of order 6 has order 4. The four listed elements exhaust it. \(\square\)

Assign one bit to each matching:
\[
\Theta=\mathbb F_2^{\{M_1,M_2,M_3\}}\cong\mathbb F_2^3.
\]
For \(p\in S_3\), use the coordinate action \((P_p\theta)_{p(j)}=\theta_j\). This convention fixes the direction of later composition formulas.

**Proposition P3.2 (equal order is not group identity).** The stabilizer of one matching in \(S_4\) has order 8 and is nonabelian. It is not the additive group of \(\Theta\).

*Proof.* Orbit-stabilizer gives order \(24/3=8\). In the stabilizer of \(M_1\), independently swap the two vertices of each edge, and also exchange the edges. Thus the group is \((C_2\times C_2)\rtimes C_2\), with the last factor exchanging the first two. For example, the within-edge swap \((01)\) and edge exchange \((02)(13)\) do not commute. The additive group \(\mathbb F_2^3\) is abelian. \(\square\)

The distinction is structural, not merely terminological. A matching indexes a coordinate; its stabilizer is a group of vertex permutations. The coordinate space is not obtained by identifying those two objects.

## 3.2 The edge projection and its fibers

Define the labeled state set
\[
\mathcal X=S_4\times\Theta.
\]
This is a product of sets. It has 192 elements. To make a fiber count meaningful, a projection must be declared. Fix the reference edge \(e_0=\{0,1\}\) and define
\[
p_E(g,\theta)=g(e_0).
\]
The second coordinate does not enter this projection.

**Proposition P3.3 (uniform edge fibers).** Every edge has 32 inverse images under \(p_E\). Consequently
\[
|\mathcal X|=192=6\times32.
\]

*Proof.* A permutation sending \(e_0\) to a specified edge can assign its two vertices in two orders and assign the two complementary vertices in two orders. There are four such permutations. Each can be paired with any of the eight binary vectors, giving \(4\times8=32\) states. The six fibers partition \(\mathcal X\). \(\square\)

The integer factors are \(192=2^6\cdot3\), \(6=2\cdot3\), and \(32=2^5\). They record the specified counting construction, not a dynamical scale. In quotient/remainder notation, \(192=6(32)+0\) and \(192\equiv0\pmod{32}\): six complete groups leave no remainder.

**No-go NG3.4 (cardinality does not specify depth).** The size 32 of a fiber does not imply 32 successive update stages, a 32-cycle, or a required duration.

*Proof.* On the same 32-element fiber one may define the identity map, a transposition, or a 32-cycle. Their update histories differ while the underlying cardinality is unchanged. No transition map is included in the fiber definition. Therefore no sequential depth follows from that definition alone. \(\square\)

## 3.3 Hamming sectors

On the eight-dimensional vector space with basis \(e_\theta\), define
\[
W e_\theta=w_H(\theta)e_\theta,
\qquad w_H(\theta)=\theta_1+\theta_2+\theta_3.
\]
These eigenspaces are called Hamming sectors; “branch” will not be used to imply a physical process.

**Proposition P3.5 (sector dimensions).** The four spectral projectors
\[
P_w=\prod_{\substack{j=0\\j\ne w}}^3\frac{W-jI}{w-j},
\qquad w=0,1,2,3,
\]
have ranks \(1,3,3,1\). Coordinate permutations commute with \(W\). Complementation \(Qe_\theta=e_{\theta\oplus111}\) satisfies \(QWQ^{-1}=3I-W\).

*Proof.* There are \(\binom3w\) binary vectors of weight \(w\). The displayed polynomials equal one at their designated eigenvalue and zero at the other three. Coordinate permutations preserve the number of ones; complementation replaces that number by three minus itself. \(\square\)

For any linear map \(U\) on this space, preservation of every Hamming sector is equivalent to \([U,W]=0\). Indeed, the commutator vanishes exactly when all matrix blocks between different eigenvalues vanish. Equal dimensions of the weight-one and weight-two sectors do not choose a preferred sector.

# 4. Oriented chains and the standard skew generator

## 4.1 Chain convention

A simplicial complex in this paper contains each nonempty simplex once, including all faces of every maximal simplex. Increasing vertex order fixes a basis orientation. With real coefficients, let \(C_k(K)\) be the chain space of \(k\)-simplices, and put
\[
\mathcal C(K)=\bigoplus_{k=0}^3 C_k(K).
\]
We use the nonaugmented complex: no empty-simplex coordinate is included. The boundary is
\[
\partial_k[v_0\ldots v_k]
=\sum_{j=0}^k(-1)^j[v_0\ldots\widehat v_j\ldots v_k].
\]
Its matrix is \(B_k\), with rows indexed by \((k-1)\)-simplices and columns by \(k\)-simplices. Inner products make these oriented basis vectors orthonormal. Adjoint therefore means transpose.

**Lemma L4.1 (standard chain identity).** For every such complex, \(B_{k-1}B_k=0\).

*Proof.* Every codimension-two face occurs twice in the iterated boundary. Removing vertices in the opposite order changes one deletion index by one, so the two signs are opposite. The terms cancel. \(\square\)

For the filled tetrahedron \(\Delta^3\), use vertices \((0,1,2,3)\), edges \((01,02,03,12,13,23)\), faces \((012,013,023,123)\), and cell \(0123\). Then
\[
(\dim C_0,\dim C_1,\dim C_2,\dim C_3)=(4,6,4,1).
\]
The explicit incidence matrices appear in Appendix A. Their ranks are \((3,3,1)\). The homology dimensions are consequently \((1,0,0,0)\). This is the filled tetrahedron, not its boundary sphere and not just its edge graph; confusing those carriers changes homology and the operator.

## 4.2 Closed linear flow

**Definition D4.2.** On \(\mathcal C(K)\), define
\[
\mathcal A_K=\begin{pmatrix}
0&-B_1&0&0\\
B_1^T&0&-B_2&0\\
0&B_2^T&0&-B_3\\
0&0&B_3^T&0
\end{pmatrix},\qquad
S_\mu(c)=c^Tc.
\]
The closed flow is \(\dot c=\mathcal A_Kc\), with dimensionless real parameter \(s\).

**Lemma T4.3 (standard skew-flow conservation).** The generator is skew, and every solution satisfies \(dS_\mu/ds=0\).

*Proof.* Transposing the block matrix gives \(\mathcal A_K^T=-\mathcal A_K\). Therefore \(d(c^Tc)/ds=c^T(\mathcal A_K^T+\mathcal A_K)c=0\). Equivalently, \(e^{s\mathcal A_K}\) is orthogonal. \(\square\)

Let \(d\) denote the block map with \(B_k^T\) in the degree-raising positions. Then \(\mathcal A=d-d^T\), while \(D=d+d^T\) is the usual symmetric Hodge–Dirac operator. Since \(d^2=0\),
\[
-\mathcal A^2=D^2=L,
\]
where \(L\) is block diagonal with
\[
L_k=B_k^TB_k+B_{k+1}B_{k+1}^T,
\]
using zero terms at the ends. These identities are valid for the declared Euclidean metric. Changing weights requires changing the adjoints consistently.

## 4.3 The single tetrahedron

**Proposition T4.4 (single-cell identity).** Let \(P_0\) project onto the uniform vertex vector and vanish on all higher degrees. For the filled tetrahedron,
\[
\mathcal A^2=-4(I-P_0),\qquad
\mathcal A^3+4\mathcal A=0,
\]
and
\[
\det(\lambda I-\mathcal A)=\lambda(\lambda^2+4)^7.
\]

*Proof.* Direct multiplication of Appendix A gives
\[
L_0=4I_4-\mathbf1\mathbf1^T,\quad L_1=4I_6,\quad
L_2=4I_4,\quad L_3=4I_1.
\]
Thus \(L=4(I-P_0)\) and \(\mathcal A P_0=0\). On the fourteen-dimensional orthogonal complement, \(\mathcal A^2=-4I\). A real skew matrix has conjugate eigenvalues in pairs, giving seven copies of each of \(2i\) and \(-2i\), and one zero eigenvalue. \(\square\)

The flow can be written without numerical diagonalization:
\[
e^{s\mathcal A}=P_0+\cos(2s)(I-P_0)+\frac{\sin(2s)}2\mathcal A.
\]
It has full-operator period \(\pi\). In clock notation, \(s=\pi\) gives phase \(2s=1(2\pi)+0\), equivalently \(2s\equiv0\pmod{2\pi}\). This is a periodic parameterization of a matrix flow, not a physical clock.

**Proposition P4.5 (orthogonal edge decomposition).** On \(C_1(\Delta^3)\),
\[
P_{\rm cut}=\frac14B_1^TB_1,\qquad
P_{\rm cycle}=\frac14B_2B_2^T
\]
are orthogonal rank-three projectors, with sum \(I_6\). In particular, \(\ker B_1=\operatorname{im}B_2\).

*Proof.* The degree-one block of \(L\) is \(4I_6\). The two summands have zero product by \(B_1B_2=0\); their sum is \(4I_6\). Squaring the sum relation after multiplying by either summand shows each squared summand is four times itself. Their ranks are the ranks of \(B_1\) and \(B_2\), both three. The chain identity gives inclusion of the image in the kernel, and dimensions give equality. \(\square\)

For a unit vector \(z\in\ker B_1\) initially placed in degree one, the solution has
\[
c_1(s)=\cos(2s)z,\qquad c_2(s)=\tfrac12\sin(2s)B_2^Tz,
\qquad c_0(s)=c_3(s)=0.
\]
This example describes exchange between two chain degrees. It is not transport of a material substance.

# 5. Incidence balance and unique-simplex gluing

## 5.1 A local quadratic balance

For incident simplices \(\sigma\subset\eta\) of adjacent degree, define the bilinear incidence current
\[
J_{\sigma\eta}=2B_{\sigma\eta}c_\sigma c_\eta.
\]
A positive value is directed from the lower degree \(\sigma\) to the upper degree \(\eta\). This sign convention follows the chosen \(\mathcal A\); it is not an extra direction assigned to the geometric edge.

For any set \(R\) of simplex coordinates, write \(S_R=\sum_{\sigma\in R}c_\sigma^2\). The set need not be a subcomplex.

**Proposition T5.1 (exact cut balance).** Along the closed flow,
\[
\frac{dS_R}{ds}=J_{\rm in}(R)-J_{\rm out}(R),
\]
where only adjacent-degree incidences crossing \(R\) and its complement contribute.

*Proof.* The pair \((\sigma,\eta)\) contributes \(-2B_{\sigma\eta}c_\sigma c_\eta\) to the derivative of \(c_\sigma^2\) and the opposite amount to that of \(c_\eta^2\). If both coordinates belong to \(R\), these cancel; if neither belongs to \(R\), they do not enter. A crossing incidence contributes with the stated incoming or outgoing sign. Summing over pairs proves the identity. \(\square\)

The global conservation lemma is the special case containing every coordinate. The local statement additionally identifies which bilinear terms account for a change in a selected sum. It makes no assertion about a physical current observable.

## 5.2 Shared faces are not duplicated degrees of freedom

For a pure tetrahedral complex, let \(n_3(\sigma)\) be the number of top-dimensional tetrahedra containing simplex \(\sigma\). It is positive for every simplex in this setting. Define an equal ownership weight
\[
w_{\sigma\tau}=\begin{cases}1/n_3(\sigma),&\sigma\subseteq\tau,\\0,&\text{otherwise},\end{cases}
\]
and a cell-attributed norm
\[
S_\tau^{\rm eq}=\sum_\sigma w_{\sigma\tau}c_\sigma^2.
\]

**Proposition T5.2 (partition of global support).** One has
\[
\sum_\tau S_\tau^{\rm eq}=S_\mu(c).
\]

*Proof.* For each unique simplex, the weights of its containing tetrahedra sum to \(n_3(\sigma)/n_3(\sigma)=1\). Interchange the two finite sums. \(\square\)

For two tetrahedra sharing a face, the three vertices, three edges and that face are common coordinates. They are not copied into independent local chain spaces when forming the global complex. Equal ownership distributes their contribution for accounting, but does not alter the global incidence matrices.

Other nonnegative ownership weights summing to one also give a partition. Equal ownership is a convention, not a derived constitutive law. A naive sum of unweighted cell norms double-counts shared coordinates and does not equal the unique-simplex norm. The theorem requires purity only so the displayed denominator is defined; lower-dimensional components would need a separate attribution rule.

# 6. A finite retriangulation family

## 6.1 The oriented 2-to-3 identity

On five ordered vertices, use formal oriented 3-chains
\[
K_-=[0123]-[0124],
\qquad K_+=-[1234]+[0234]-[0134].
\]
The first consists of two tetrahedra sharing face \(012\); the second consists of three sharing edge \(34\).

**Proposition T6.1 (equal exterior boundary).**
\[
K_--K_+=\partial[01234],\qquad \partial K_-=\partial K_+.
\]

*Proof.* Expanding the alternating boundary of \([01234]\) gives
\[
[1234]-[0234]+[0134]-[0124]+[0123],
\]
which is the difference above. Apply \(\partial^2=0\). \(\square\)

This is a chain identity. For a legal geometric Pachner move, the link and missing-simplex conditions of the bistellar definition must also hold. The equality does not authorize arbitrary changes in any ambient complex. In particular, it does not identify the two interior operators or give a canonical dynamical interpolation between them.

## 6.2 The three specified complexes

Let each list below generate its downward-closed simplicial complex:
\[
A=\langle0123,0124\rangle,\quad
B=\langle0123,0124,0134\rangle,\quad
C=\langle0134,0234,1234\rangle.
\]
Their numbers of unique simplices are
\[
f(A)=(5,9,7,2),\qquad f(B)=f(C)=(5,10,9,3).
\]
Thus \(\dim\mathcal C(A)=23\) and \(\dim\mathcal C(B)=\dim\mathcal C(C)=27\). The intermediate complex \(B\) is a declared comparison object, not a claim that a Pachner event physically traverses that state.

**Proposition T6.2 (signed B/C isomorphism).** The vertex permutation \(p=(0\ 3)(1\ 4)\), with vertex 2 fixed, maps \(B\) to \(C\). Its degreewise signed simplex permutation \(P\) satisfies
\[
P^TP=I,\qquad \mathcal A_CP=P\mathcal A_B.
\]

*Proof.* Apply \(p\) to the three maximal simplices and sort each image; the resulting sets are the three maximal simplices of \(C\). The sign of each sorting permutation supplies the oriented chain map. Boundaries commute with this map. Since it is a signed permutation, its inverse is its transpose; the adjoint boundary maps commute as well. Assemble the blocks. \(\square\)

**Proposition P6.3 (inclusion is not flow equivalence).** The coordinate inclusion \(T:\mathcal C(A)\to\mathcal C(B)\), zero on the new coordinates, satisfies \(T^TT=I\), but
\[
\mathcal A_BT-T\mathcal A_A\ne0.
\]

*Proof.* Distinct old simplex basis vectors remain distinct orthonormal vectors, proving isometry. For a concrete residual, vertex 3 is in \(A\), but edge \(34\) is new in \(B\). The degree-raising block sends the vertex-3 coefficient into the new edge with coefficient \(-1\), while the included A-flow has no such edge coordinate. Therefore the residual is nonzero. \(\square\)

This example prevents an event-level norm identity from being mistaken for a continuous-time intertwining theorem. The B/C relabeling has the stronger property; the A/B inclusion does not.

Both B and C have complete edge graph on five vertices, but neither is the full clique complex of that graph. Their listed maximal tetrahedra determine which faces and higher simplices exist. Completing every clique would create a different carrier and invalidate the displayed dimensions and spectra. The input is the simplicial complex, not only its one-skeleton.

## 6.3 Exact spectra

**Theorem T6.4 (declared A/B/C spectra).** With unique-simplex bases and the unit inner products of Section 4,
\[
\chi_A(\lambda)=\lambda(\lambda^2+3)^4(\lambda^2+5)^7,
\]
\[
\chi_B(\lambda)=\chi_C(\lambda)
=\lambda(\lambda^2+2)^2(\lambda^2+5)^{11}.
\]

*Proof by exact matrix certificate.* Construct the three incidence systems using the deletion rule in Section 4.1 and Appendix B. Set \(L_K=-\mathcal A_K^2\). Integer matrices and rational row reduction give the following nullities:

| Complex | \(\dim\ker L\) | \(\dim\ker(L-2I)\) | \(\dim\ker(L-3I)\) | \(\dim\ker(L-5I)\) |
|:--|--:|--:|--:|--:|
| A | 1 | 0 | 8 | 14 |
| B | 1 | 4 | 0 | 22 |
| C | 1 | 4 | 0 | 22 |

In each case the listed nonzero eigenspaces and kernel exhaust the chain dimension. The symmetric matrix \(L_K\) has no further eigenvalues. Since \(\mathcal A_K\) is real skew, a positive eigenvalue \(\nu\) of \(L_K\) splits equally into \(\pm i\sqrt\nu\) for \(\mathcal A_K\). This yields the stated characteristic polynomials. The archived matrices and exact row-reduction implementation reproduce every nullity. \(\square\)

This is a finite certificate rather than a numerical eigenvalue fit. In particular, no floating-point tolerance is used to distinguish zero, two, three or five. The proof depends on the actual complex, not merely on its numbers of simplices. An isomorphic orientation convention gives conjugate matrices and the same result.

**No-go NG6.5 (fixed binary 2:2 labels).** No fixed binary labeling of the five vertices gives exactly two ones in every four-vertex tetrahedron on this set.

*Proof.* Write the total number of ones as \(N\), with label \(b_i\) at vertex \(i\). The five conditions are \(N-b_i=2\). Thus all \(b_i\) are equal. If all are zero, each four-set has zero ones; if all are one, it has four. Both contradict two. \(\square\)

This excludes one particular auxiliary labeling condition. It does not obstruct the Pachner move itself or rule out another state representation.

## 6.4 Exact recurrence and its limits

**No-go NG6.6 (no positive full-flow period).** For each \(K\in\{A,B,C\}\), there is no \(T>0\) for which \(e^{T\mathcal A_K}=I\).

*Proof.* For \(A\), a full period requires integers \(n,m>0\) with
\[
T\sqrt3=2\pi n,\qquad T\sqrt5=2\pi m.
\]
Thus \(\sqrt{5/3}=m/n\). If this were rational in lowest terms, \(3m^2=5n^2\), contradicting the even valuations of squares at primes 3 and 5. The same argument using primes 2 and 5 rules out \(\sqrt{5/2}\) for B and C. \(\square\)

The clock form of the required equalities is \(T\sqrt3\equiv T\sqrt5\equiv0\pmod{2\pi}\) for A, and analogously for B/C: both spectral pointers would have to return to zero after integer full rotations. The irrational ratio forbids a common nonzero exact return.

This statement is about the identity of the entire evolution operator. A harmonic state is fixed. A state supported in a single frequency subspace is periodic. Approximate returns are not excluded; simultaneous rational approximation of phases can bring a bounded finite-dimensional orthogonal flow close to its initial operator. We make no claim about a minimum approximate-return time. The single-cell period \(\pi\) therefore cannot be assigned to all glued complexes, but recurrence of selected states remains possible.

# 7. Recorded events determine affine binary maps

## 7.1 What data are supplied

Fix pre- and post-event labeled states \((g^-,\theta^-)\) and \((g^+,\theta^+)\). Define the relative vertex permutation and binary offset
\[
r=g^+(g^-)^{-1},\qquad
 a=\theta^+\oplus P_{\pi(r)}\theta^-.
\]
The pair \((r,a)\) is the recorded event data. If those endpoints are observed only after the event, the pair is retrospective. To predict an event, a separate pre-event process must supply \((r,a)\) without using the held-out endpoint.

**Definition D7.1.** For supplied \(r\in S_4\), \(a\in\Theta\), define the affine map
\[
F_{r,a}(\theta)=a\oplus P_{\pi(r)}\theta,
\]
and its permutation operator \(U_{r,a}e_\theta=e_{F_{r,a}(\theta)}\).

**Proposition T7.2 (exact receipt-conditioned map).** The map is a bijection, its permutation operator is orthogonal, and endpoint-derived data satisfy \(F_{r,a}(\theta^-)=\theta^+\).

*Proof.* Coordinate permutation and translation in \(\mathbb F_2^3\) are both bijections. The inverse is \(\theta\mapsto P_{\pi(r)}^{-1}(\theta\oplus a)\). A bijection of an orthonormal basis gives an orthogonal matrix. Substituting the endpoint definition of \(a\) cancels the repeated binary vector. \(\square\)

For consecutive supplied events, the maps compose as
\[
F_{r_2,a_2}\circ F_{r_1,a_1}
=F_{r_2r_1,\ a_2\oplus P_{\pi(r_2)}a_1}.
\]
This is an affine-group identity. It does not say which events occur or assign probabilities to them.

## 7.2 Exact Hamming-sector consequences

**Theorem T7.3 (sector transition counts).** Let \(h=w_H(a)\). For weights \(w,w'\),
\[
\operatorname{rank}(P_{w'}U_{r,a}P_w)
=\binom ht\binom{3-h}{w-t},
\qquad t=\frac{w+h-w'}2,
\]
when \(t\) is an integer satisfying \(0\le t\le h\) and \(0\le w-t\le3-h\); otherwise the rank is zero. Furthermore,
\[
\frac18\|[U_{r,a},W]\|_F^2=h.
\]

*Proof.* Coordinate permutation preserves weight. Of the \(h\) coordinates flipped by the offset, let \(t\) initially contain a one. The output weight is \(w+h-2t\). There are \(\binom ht\binom{3-h}{w-t}\) input basis vectors with these properties. Distinct inputs have distinct outputs, so counting them gives the block rank.

For the commutator, its squared norm is the sum of squared weight changes over the eight basis vectors. For a uniformly selected binary vector, each flipped coordinate contributes independently either \(+1\) or \(-1\), equally often. The expected square of their sum is \(h\), since the cross terms cancel. Multiply by eight. \(\square\)

Thus a map may mix Hamming sectors while preserving the Euclidean norm of every vector on the eight-state space. For example, a one-bit flip has normalized commutator square one but remains a permutation matrix. Hamming-sector preservation for this affine family occurs exactly when \(a=0\).

## 7.3 Recovering a relative frame when an edge map is supplied

A specified edge map can sometimes determine the vertex permutation in the receipt without reference to the post-event binary endpoint. This remains a conditional extraction problem: the edge map itself must already be available.

**Proposition P7.4 (unique relative-frame extraction).** Let \(M:C_1(\Delta^3)\to C_1(\Delta^3)\) be a supplied real matrix, and let \(J_4=\mathbf1\mathbf1^T\). Form
\[
\widehat P=\frac14(B_1MB_1^T+J_4).
\]
If \(\widehat P\) is a vertex permutation matrix and \(B_1M=\widehat P B_1\), there is a unique \(r\in S_4\) with \(P_0(r)=\widehat P\). With the induced signed edge map \(P_1(r)\), the residual \(R=P_1(r)^{-1}M\) satisfies \(B_1R=B_1\). If \(M\) is orthogonal, \(R\) fixes the cut space pointwise and preserves the cycle space.

*Proof.* A permutation matrix uniquely specifies its vertex permutation. Boundary equivariance gives \(B_1P_1(r)=P_0(r)B_1\), so substitution gives \(B_1R=B_1\). Transposing yields \(R^TB_1^T=B_1^T\). If \(R\) is orthogonal, multiply by \(R\) to obtain \(RB_1^T=B_1^T\); hence it fixes the cut space. Orthogonality then preserves its orthogonal complement, the cycle space. Conversely, if an edge map satisfies \(B_1M=P_0B_1\) for a permutation \(P_0\), multiplication by \(B_1^T\) and use of \(B_1B_1^T=4I-J_4\), \(P_0J_4=J_4\), recovers the stated formula. \(\square\)

The two admission checks are essential. The formula alone may yield a matrix that is not a permutation, and a visually nearby permutation is not an exact substitute. Even successful extraction leaves the parity offset \(a\) unspecified. This illustrates the distinction between recovering a frame from sufficient recorded data and deriving an event source.

## 7.4 The unresolved source question

The logical conclusion is deliberately conditional:
\[
\text{supplied }(r,a)\quad\Longrightarrow\quad\text{an exact affine }\Theta\text{-map}.
\]
It is not a derivation of \((r,a)\) from the chain state or from a microscopic law. Extracting an offset from observed endpoints always fits that pair of endpoints by definition; it cannot count as a successful prediction of them. Many different offset-selection rules are compatible with the same carrier, group action and closed norm conservation.

Later conditional constructions in the research archive introduce finite update interfaces, source packets, recovery criteria and event-admission rules. They specify what a source would have to provide. They are not used as premises of the theorems above and are not stacked into the main argument. In particular, an executable rule that accepts source terms as input is not a derivation of those terms. The source of predictive receipts remains outside this paper.

# 8. Four preservation statements with different types

Let \(T\) be a linear map between Euclidean chain spaces. Its Gram defect is
\[
G_T=T^TT-I.
\]
It measures a change in squared chain norm: \(\|Tc\|^2-\|c\|^2=c^TG_Tc\). This must not be confused with Hamming-sector mixing on the separate eight-state space.

Suppose a second quadratic form is specified by a symmetric matrix \(Q\). The change of that form is
\[
c^T(T^TQT-Q)c.
\]
A project may call such a second functional *burden*, but the word supplies no physical meaning and no relation to \(S_\mu\). The matrix \(Q\) and its carrier must be stated before the expression is meaningful.

**Proposition P8.1 (norm preservation does not imply preservation of another form).** There is an orthogonal \(T\) for which \(T^TQT\ne Q\).

*Proof.* In two dimensions, let \(T\) exchange the coordinates and \(Q=\operatorname{diag}(1,2)\). Then \(T^TT=I\), but \(T^TQT=\operatorname{diag}(2,1)\ne Q\). \(\square\)

Finally, a contraction \(K\), satisfying \(K^TK\preceq I\), has the nonnegative complementary effect \(E=I-K^TK\). Choosing \(L=E^{1/2}\) gives
\[
K^TK+L^TL=I.
\]
This is the elementary finite operator identity behind a retained/lost split. In a complex quantum-operation setting it is familiar from Kraus representations. Here it is only linear algebra. A permutation mixing Hamming sectors can have zero Gram defect and zero complementary effect; a contraction can have nonzero complementary effect without any binary-state interpretation.

These examples explain why numerical agreement between four diagnostics would not make them one object. Each has a domain, codomain and defining map. Calling all of them “leakage,” “transport” or “burden” would erase premises needed by a referee to check the claim.

# 9. Limitations and operational checks

The results depend on fixed finite carriers, unit simplex inner products and the stated event maps. The relay spectra are calculations for three complexes, not a classification of all tetrahedral complexes. Norm conservation is too weak to select the skew generator uniquely. The matching-labeled state set is a chosen representation, not a derived ontology. The receipt-conditioned map leaves constitutive dynamics open. The contribution relative to existing Hodge and graph-operator work is correspondingly narrow, and no general novelty is asserted for the standard lemmas.

> **Referee checks.** A nonzero \(B_1B_2\) or \(B_2B_3\) refutes the supplied chain construction. Unequal fibers under the declared \(p_E\) refute P3.3. A nonzero commutator refutes a claim of exact Hamming-sector preservation for that operator. Different exact nullities refute the spectral certificate. A verified positive period for the full A, B or C operator would contradict the recurrence argument; a period for one state would not. A failure of the ownership weights to sum to one refutes the stated gluing partition.

These are operational internal checks. They do not require cosmological, particle or optical observations. The companion reconstruction paper supplies its own data-consistency and held-out falsifiers.

# 10. Claim table and reproduction

The table is an index of proof obligations, not a count of scientific merit. “Standard lemma” identifies conventional setup. “Finite calculation” identifies a reproducible specialization. Artifact references point to the supplement's `data/exact_artifacts.json` and `verify.py`.

| ID | Statement | Status | Proof / artifact | Depends on |
|:--|:--|:--|:--|:--|
| P3.1 | Matching action has kernel \(V_4\) | Proposition | Group argument; exhaustive action | Three matchings |
| P3.2 | Matching stabilizer differs from \(\Theta\) | Proposition | Noncommuting elements | P3.1 |
| P3.3 | Six edge fibers each have 32 states | Proposition | Four permutations per edge | Declared \(p_E\) |
| NG3.4 | Fiber size does not imply depth | No-go | Three maps on the same set | P3.3 |
| P3.5 | Hamming ranks are 1,3,3,1 | Proposition | Binary enumeration | \(W\) |
| L4.1 | Boundary squared vanishes | Standard lemma | Sign cancellation; matrices | Orientation rule |
| T4.3 | Closed flow conserves \(S_\mu\) | Standard lemma | Skew identity | D4.2 |
| T4.4 | Single-cell squared generator | Finite calculation | Exact block multiplication | Appendix A |
| P4.5 | Edge cut/cycle projectors | Proposition | Projector identities | L4.1, T4.4 |
| T5.1 | Cut norm balance | Proposition | Pairwise cancellation | D4.2 |
| T5.2 | Ownership sums to global norm | Proposition | Partition of unity | Unique simplices |
| T6.1 | Pachner exterior boundaries agree | Standard identity | Alternating boundary | L4.1 |
| T6.2 | Signed B/C intertwiner | Finite calculation | Signed permutation matrix | Specified B/C |
| P6.3 | A/B inclusion is not an intertwiner | Counterexample | New edge 34 residual | Specified A/B |
| T6.4 | Exact A/B/C spectra | Finite theorem | Rational nullity certificates | D4.2 |
| NG6.5 | No common binary 2:2 labeling | No-go | Five sum equations | Five vertices |
| NG6.6 | No positive full-flow period | No-go | Irrational frequency ratios | T6.4 |
| T7.2 | Supplied receipts give affine bijection | Proposition | Inverse map | D7.1 |
| T7.3 | Transition ranks and commutator | Finite theorem | Counting; exhaustive replay | P3.5, D7.1 |
| P7.4 | Admitted edge map fixes relative frame | Proposition | Boundary identity; permutations | Supplied edge map |
| P8.1 | Norm and second-form preservation differ | Counterexample | Two-dimensional matrices | Declared \(Q\) |

Run `python verify.py` from the extracted reproduction package. It regenerates the ordered simplex bases, incidence matrices, generators, A/B/C maps, nullity certificates, matching actions, affine transition counts and the companion PSR fixtures. Only the Python standard library is required. The README records the measured execution time; the exact algebra uses integers and rational numbers rather than Monte Carlo or fitted tolerances.

The replay verifies finite algebraic instances and supplied artifacts. The general cancellation, counting and reconstruction arguments are the written proofs. Agreement of software output is not independent mathematical peer review. The package also records file hashes so a reviewer can identify the exact files tested; those hashes are not premises of any theorem.

# Appendix A. Single-cell matrices

With the bases in Section 4,
\[
B_1=\begin{pmatrix}
-1&-1&-1&0&0&0\\
1&0&0&-1&-1&0\\
0&1&0&1&0&-1\\
0&0&1&0&1&1
\end{pmatrix},
\]
\[
B_2=\begin{pmatrix}
1&1&0&0\\
-1&0&1&0\\
0&-1&-1&0\\
1&0&0&1\\
0&1&0&-1\\
0&0&1&1
\end{pmatrix},\qquad
B_3=\begin{pmatrix}-1\\1\\-1\\1\end{pmatrix}.
\]
The vertex block product is
\[
B_1B_1^T=\begin{pmatrix}
3&-1&-1&-1\\-1&3&-1&-1\\-1&-1&3&-1\\-1&-1&-1&3
\end{pmatrix}.
\]
The uniform vertex projector is \(\mathbf1\mathbf1^T/4\), extended by zero to the other eleven coordinates. Multiplication gives \(B_1B_2=0\), \(B_2B_3=0\), \(B_1^TB_1+B_2B_2^T=4I_6\), \(B_2^TB_2+B_3B_3^T=4I_4\), and \(B_3^TB_3=4\).

An orientation reversal multiplies a simplex basis vector by minus one. Reversing several orientations gives diagonal sign matrices \(R_k\), changes the boundary to \(R_{k-1}B_kR_k\), and conjugates the full generator by \(\operatorname{diag}(R_0,R_1,R_2,R_3)\). Hence the spectrum and global norm do not depend on this basis choice.

# Appendix B. Reconstructing the finite certificates

A reviewer can construct every matrix without any private source or conversation. For each listed maximal tetrahedron, enumerate every nonempty subset. Deduplicate equal vertex sets, sort by dimension and then lexicographically, and orient every simplex by increasing vertex order. Insert the alternating deletion signs into the boundary matrices. This determines the generator without a free matrix entry.

For A, the edge list is
\[
01,02,03,04,12,13,14,23,24,
\]
and the face list is
\[
012,013,014,023,024,123,124.
\]
For B the extra edge is \(34\), the extra faces are \(034,134\), and the extra tetrahedron is \(0134\). C follows by the vertex permutation in T6.2; its independent lexicographic construction is also supplied. The exact boundary ranks are \((4,5,2)\) for A and \((4,6,3)\) for B/C, giving one degree-zero homology class and no higher homology in each case.

The squared-frequency certificate can be checked by Gaussian elimination over rational numbers. For A the ranks of \(L\), \(L-3I\), \(L-5I\) are \(22,15,9\); subtracting from 23 gives \(1,8,14\). For B/C the ranks of \(L\), \(L-2I\), \(L-5I\) are \(26,23,5\), giving \(1,4,22\). The dimensions sum to the full space, so the displayed eigenvalues exhaust a symmetric matrix's spectrum.

One need not approximate square roots to verify the absence of a full period. Only the exact squared frequencies and the elementary irrationality arguments in NG6.6 enter that conclusion. Likewise, one need not integrate the differential equation numerically to verify support conservation.

# References

[1] A. N. Hirani, *Discrete Exterior Calculus*, PhD thesis, California Institute of Technology (2003). [doi:10.7907/ZHY8-V329](https://doi.org/10.7907/ZHY8-V329).

[2] A. N. Hirani, *Discrete Exterior Calculus*, IPAM lecture, 15 July 2004, PDF pp. 1–3. [Author lecture](https://helper.ipam.ucla.edu/publications/mbi2004/mbi2004_3836.pdf).

[3] D. Horak and J. Jost, “Spectra of combinatorial Laplace operators on simplicial complexes,” *Advances in Mathematics* **244**, 303–336 (2013). [doi:10.1016/j.aim.2013.05.007](https://doi.org/10.1016/j.aim.2013.05.007). Comparison uses [arXiv:1105.2712](https://arxiv.org/pdf/1105.2712), PDF pp. 4–6.

[4] O. Knill, “The Dirac operator of a graph” (2013), [arXiv:1306.2166](https://arxiv.org/pdf/1306.2166), pp. 1–2 and 18.

[5] U. Pachner, “P.L. homeomorphic manifolds are equivalent by elementary shellings,” *European Journal of Combinatorics* **12**, 129–145 (1991). [doi:10.1016/S0195-6698(13)80080-7](https://doi.org/10.1016/S0195-6698(13)80080-7).

[6] W. B. R. Lickorish, “Simplicial moves on complexes and manifolds,” *Geometry & Topology Monographs* **2**, 299–320 (1999). [arXiv:math/9911256](https://arxiv.org/pdf/math/9911256). Local move: p. 302; equivalence theorem: p. 315.

[7] K. G. Wilson, “Confinement of quarks,” *Physical Review D* **10**, 2445–2459 (1974). [doi:10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445), Section III, pp. 2448–2450.

[8] K. Kraus, “General state changes in quantum theory,” *Annals of Physics* **64**, 311–335 (1971). [doi:10.1016/0003-4916(71)90108-4](https://doi.org/10.1016/0003-4916(71)90108-4).
