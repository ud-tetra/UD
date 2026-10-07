---
title: "Tetrahedral Symmetry, Radial Spectra and Finite Collective Mechanisms"
subtitle: "Paper III - Consolidated integration draft 1.1"
author: "Benjamin Walker Mayes"
date: "3 October 2026"
---

**Independent researcher**  
ORCID: [0009-0002-5813-0724](https://orcid.org/0009-0002-5813-0724)

**Edition status.** Integration draft for independent review. Source baseline: portal version 161, commit `62a7c594e0c7ab02f1c87702d0586a39352170d5`. Mathematical assertions retain the premises of their declared carriers and maps. Source-audited calculations are distinguished from new derivations. Physical promotion: zero. Independent human review: pending.

## Abstract

We consolidate symmetry, radial refinement and prepared collective developments on declared tetrahedral carriers. Signed filled-tetrahedron chains have commutant dimensions 13, 10 and 3 for the full, self-adjoint and skew-adjoint families. Explicit annulus and center-filled shell constructions retain exact topology and representation decompositions. A confining depth operator has compact resolvent and fixed-index finite-shell convergence; four low spectral enclosures are repaired with new rational polynomials, exact root counts and an explicit infinite min-max proof. Scalar Weyl descriptions are restricted to visible modes pending infinite cyclicity. The six-edge relation algebra and minimum context dimension three are retained, with an explicit compatible basis proving covariance of the supplied context tensor. Prepared shape, burden, renewal, finite controller, timed capture and static capture-window results are integrated with their resource ledgers and no-gos. No universal relation strength, native preparation, perpetual storage or physical Hamiltonian is derived.

# 1. Scope and contribution boundary

The purpose of this paper is to collect a set of post-companion mathematical results that enlarge the finite tetrahedral carrier while preserving a narrow claim boundary. The results concern finite $S_4$ representation theory, pure simplicial shell constructions, a declared radial operator family, and its infinite-volume spectral reduction. The basic chain conventions and skew Hodge--Dirac setup are those of the companion finite-carrier paper; the deterministic reconstruction problem is treated separately in the companion projective-receipt paper. Neither companion is logically required for the new shell triangulation once the tetrahedral vertex action is fixed.

The ordinary background is standard. Finite-group characters and Schur's lemma are used in the usual sense [1]. Simplicial boundary operators and combinatorial Laplacians follow the familiar discrete-exterior-calculus and simplicial-Laplacian setting [2-4]. The infinite radial reduction belongs to the general spectral theory of Jacobi-type difference operators and Weyl functions [5].

#### What is not claimed.

The shell index is not a principal quantum number; the declared $H_{r,\beta}$ is not asserted to be a physical Hamiltonian; $E$ and $T_2$ are representation labels, not particle names; the radial depth is an internal combinatorial function, not a physical radius; and no energy, action, mass, charge, or time unit is supplied. Any later correspondence to a physical system would require an independently specified carrier map and empirical test.

# 2. Representation theory of the filled tetrahedron

## Chain decomposition

Let $P\cong\mathbb{R}^4$ be the natural permutation representation of $S_4$ on the vertices of a tetrahedron. With the increasing-order orientation convention, the chain spaces identify with exterior powers, $$C_0\cong\Lambda^1P,\qquad C_1\cong\Lambda^2P,\qquad C_2\cong\Lambda^3P,\qquad C_3\cong\Lambda^4P.$$ We use the conventional irreducible labels $A_1,A_2,E,T_1,T_2$ for the five real irreducible representations of $S_4$.

::: {#thm:chain-dec .theorem}
**Theorem 1** (Oriented-chain decomposition). *Under the natural $S_4$ action, $$\boxed{C_0=A_1\oplus T_2},\qquad
\boxed{C_1=T_2\oplus T_1},$$ $$\boxed{C_2=T_1\oplus A_2},\qquad
\boxed{C_3=A_2}.$$ Consequently, $$\mathcal C=C_0\oplus C_1\oplus C_2\oplus C_3
=A_1\oplus2A_2\oplus2T_1\oplus2T_2.$$ In particular, $E$ is absent from the linear chain carrier.*
:::

::: proof
*Proof.* The natural permutation representation decomposes as $P=A_1\oplus T_2$. Taking exterior powers and reducing the corresponding characters gives the displayed sequence. Equivalently, the decomposition follows directly from the character table of $S_4$ and the character formula for exterior powers. The dimensions $4,6,4,1$ provide the independent dimension check. \(\square\)
:::

::: {#cor:hodge-typing .corollary}
**Corollary 2** (Symmetry typing of adjacent Hodge channels). *The equivariant boundary maps couple only common irreducible sectors. Thus the three adjacent-degree exchange channels are $$\boxed{T_2:\ C_0\leftrightarrow C_1},\qquad
\boxed{T_1:\ C_1\leftrightarrow C_2},\qquad
\boxed{A_2:\ C_2\leftrightarrow C_3},$$ with an isolated harmonic $A_1$ vertex mode.*
:::

::: proof
*Proof.* Equivariance of each boundary map with the vertex-permutation action and Schur's lemma imply that inequivalent irreducible sectors cannot couple. The dimensions in Theorem [1](#thm:chain-dec){reference-type="ref" reference="thm:chain-dec"} then identify the active channel in each adjacent pair. In particular, $\ker B_1\cong T_1$ and the uniform vertex vector spans the $A_1$ harmonic sector. \(\square\)
:::

## Quadratic traceless parent

::: {#prop:quad-parent .proposition}
**Proposition 3** (Quadratic $E\oplus T_2$ sector). *For the standard three-dimensional $T_2$ representation, $$\operatorname{Sym}^2(T_2)=A_1\oplus E\oplus T_2,$$ so after removing the scalar trace, $$\boxed{\operatorname{Sym}^2_0(T_2)=E\oplus T_2}.$$*
:::

::: proof
*Proof.* The symmetric-square character is $\chi_{\mathrm{sym}^2}(g)=\frac12(\chi(g)^2+\chi(g^2))$. Reducing this character against the five irreducible characters of $S_4$ gives one copy each of $A_1,E,T_2$. The $A_1$ summand is the trace. \(\square\)
:::

::: {#ng:schur .nogo}
**No-go 4** (No linear $E\to T_2$ intertwiner). *There is no nonzero $S_4$-equivariant linear map $J:E\to T_2$: $$\boxed{\operatorname{Hom}_{S_4}(E,T_2)=0}.$$*
:::

::: proof
*Proof.* The two representations are inequivalent irreducibles, so the statement is Schur's lemma. \(\square\)
:::

The useful interpretation of Proposition [3](#prop:quad-parent){reference-type="ref" reference="prop:quad-parent"} and No-go [4](#ng:schur){reference-type="ref" reference="ng:schur"} is therefore representation-theoretic: $E$ and $T_2$ can appear as sibling summands of a common quadratic parent, but they cannot be identified by an $S_4$-equivariant linear isomorphism.

## 2.3 The full signed commutant

**Proposition III.S1 (equivariant family dimensions).** On all fifteen signed filled-tetrahedron chain coordinates the decomposition is
\[
A_1\oplus2A_2\oplus2T_1\oplus2T_2.
\]
The real commutant has dimension 13, its self-adjoint part dimension 10 and its skew-adjoint part dimension 3.

*Proof.* All the listed irreducibles have real scalar endomorphism algebra. An isotypic multiplicity \(m\) contributes \(m^2\), \(m(m+1)/2\) and \(m(m-1)/2\) to these three spaces. The multiplicities \(1,2,2,2\) give \(1+4+4+4=13\), \(1+3+3+3=10\), and \(0+1+1+1=3\). The signed-action verifier additionally constructs thirteen independent commuting matrices for all 24 permutations. \(\square\)

The three skew channels permit separate coefficients for the adjacent common irreducibles. The canonical boundary/adjoint generator is a particular choice within this family. Symmetry and norm conservation alone do not force it. This finite \(S_4\) action is not a derived continuous gauge group, and no \(SU(5)\) physical identification follows from the commutant count.


# 3. A repeated-shell graph warm-up

Before constructing a pure three-dimensional shell complex, it is useful to record an exactly separable graph family. Let $$G_r=P_r\square K_4,$$ where $P_r$ is the path on $r$ shell labels and the diagonal $S_4$ action acts on the $K_4$ factor.

::: {#prop:graph-shell .proposition}
**Proposition 5** (Repeated-shell decomposition). *The vertex carrier of $G_r$ is $$\boxed{\mathcal V_r=rA_1\oplus rT_2}.$$ Its graph Laplacian separates as $$L(G_r)=L(P_r)\otimes I_4+I_r\otimes L(K_4).$$ Writing $$\rho_j=2-2\cos\frac{\pi j}{r},\qquad j=0,\ldots,r-1,$$ one has $$\boxed{\lambda_{j,A_1}=\rho_j},\qquad
\boxed{\lambda_{j,T_2}=\rho_j+4}.$$*
:::

::: proof
*Proof.* The representation statement follows from $\mathbb{R}^4=A_1\oplus T_2$ on every shell. The Laplacian identity is the standard Cartesian-product formula. Since $L(K_4)$ has eigenvalue $0$ on $A_1$ and $4$ on $T_2$, the spectrum separates as stated. \(\square\)
:::

This graph family supplies an exact radial-mode index within a declared graph product, but it is not itself a pure face-glued three-dimensional tetrahedral complex.

# 4. A pure $S_4$-equivariant tetrahedral annulus

## Construction

Take outer shell vertices $O_i$ and inner shell vertices $I_i$, $i=0,1,2,3$. For each tetrahedral edge $ij$, introduce one rectangle-center vertex $R_{ij}$, and for each tetrahedral face introduce one prism-center vertex $P_\ell$. Thus $$4+4+6+4=18$$ vertices are used. Each of the four triangular prisms between corresponding inner and outer faces is triangulated by retaining the two triangular shell faces, splitting each side rectangle through $R_{ij}$, and coning each resulting boundary triangle to the prism center. The complete tetrahedron list is supplied in the reproduction package.

::: {#thm:annulus .theorem}
**Theorem 6** (Pure annulus). *The resulting pure simplicial complex $A$ has $$\boxed{f(A)=(18,76,116,56)}.$$ Its boundary is exactly the disjoint union of the inner and outer tetrahedral $2$-spheres, and its Betti numbers are $$\boxed{(b_0,b_1,b_2,b_3)=(1,0,1,0)}.$$ The full set of 56 tetrahedra is invariant under all 24 vertex permutations in $S_4$.*
:::

::: proof
*Proof.* Enumerating all nonempty faces of the 56 listed tetrahedra and deduplicating by vertex set gives the stated $f$-vector. Exactly eight triangles have tetrahedral incidence one: the four inner and four outer shell faces; every other triangular face has incidence two. Exact boundary-matrix ranks are $$\operatorname{rank}B_1=17,\qquad \operatorname{rank}B_2=59,\qquad \operatorname{rank}B_3=56,$$ which gives the displayed Betti numbers. Relabeling $O_i,I_i,R_{ij},P_\ell$ by any $g\in S_4$ preserves the tetrahedron list. \(\square\)
:::

## Vertex representation and Laplacian blocks

The four vertex orbits have permutation representations $$O\cong A_1\oplus T_2,\quad
I\cong A_1\oplus T_2,\quad
R\cong A_1\oplus E\oplus T_2,\quad
P\cong A_1\oplus T_2.$$ Therefore $$\boxed{C_0(A)=4A_1\oplus E\oplus4T_2}.$$ For the unit-weight vertex graph Laplacian, the multiplicity-space blocks in orbit order $(O,I,R,P)$ are $$L_{A_1}^{A}=\begin{pmatrix}
7&-1&-\sqrt6&-3\\
-1&7&-\sqrt6&-3\\
-\sqrt6&-\sqrt6&6&-\sqrt6\\
-3&-3&-\sqrt6&9
\end{pmatrix},$$ $$L_{T_2}^{A}=\begin{pmatrix}
11&-1&-\sqrt2&1\\
-1&11&-\sqrt2&1\\
-\sqrt2&-\sqrt2&6&\sqrt2\\
1&1&\sqrt2&9
\end{pmatrix},$$ while the single $E$ copy has eigenvalue $6$ with multiplicity two.

# 5. Center filling and radial refinement

## Center-filled 3-ball

The annulus has an inner boundary and therefore does not itself contain a central core. Add one $S_4$-fixed center $C$ and cone it to the four inner-shell triangles.

::: {#thm:ball .theorem}
**Theorem 7** (Center-filled shell). *The resulting pure 3-ball has $$\boxed{f=(19,80,122,60)},$$ Betti numbers $$\boxed{(1,0,0,0)},$$ and vertex representation $$\boxed{5A_1\oplus E\oplus4T_2}.$$ Its only boundary is the outer tetrahedral sphere.*
:::

::: proof
*Proof.* Four center-to-inner-shell tetrahedra fill the inner boundary of Theorem [6](#thm:annulus){reference-type="ref" reference="thm:annulus"}. Exact ranks are $18,62,60$ for $B_1,B_2,B_3$, respectively, giving the displayed homology. Adding the fixed center adds one $A_1$ to the annulus vertex representation. \(\square\)
:::

## Arbitrary finite refinement

Let $K_1$ be the center-filled single tetrahedral shell, and define recursively $$K_{r+1}=K_r\cup_{S^2_{\rm tet}}A$$ by gluing a fresh copy of the annulus along the current outer tetrahedral boundary.

::: {#thm:refine .theorem}
**Theorem 8** (Radial shell recurrence). *For every $r\ge1$, $$\boxed{f(K_r)=(14r-9,\ 70r-60,\ 112r-102,\ 56r-52)}.$$ Every finite $K_r$ is a pure tetrahedral 3-ball, and $$\boxed{C_0(K_r)=(3r-1)A_1\oplus(r-1)E\oplus(3r-2)T_2}.$$*
:::

::: proof
*Proof.* Each annulus attachment adds 14 new vertices, 70 new edges, 112 new faces, and 56 new tetrahedra after subtracting the shared tetrahedral boundary. The topological assertion follows by gluing a 3-ball to $S^2\times I$ along one boundary sphere. The new vertex orbits contribute $3A_1\oplus E\oplus3T_2$ at every step, giving the representation formula by induction. \(\square\)
:::

The construction itself supplies an integer depth. We write $$d(C)=0,\qquad d(S_s)=2s-1,\qquad d(R_s)=d(P_s)=2s.$$ This is a combinatorial depth function only.

# 6. A declared confining operator family

The following operator is introduced as a mathematical family on the refined carrier; it is not derived as a physical Hamiltonian.

::: {#def:Hrb .definition}
**Definition 9** (Radial graph operator). For $\beta\ge0$, let $$\boxed{H_{r,\beta}=L_0(K_r)+\beta D_r},$$ where $L_0$ is the unit-weight vertex Laplacian and $D_r$ is multiplication by the depth $d$.
:::

Because both terms are $S_4$-invariant, $H_{r,\beta}$ splits into $A_1,E,T_2$ isotypic blocks.

::: {#prop:E-ladder .proposition}
**Proposition 10** (Exact $E$ ladder). *For every annulus layer $s=1,\ldots,r-1$, the $E$ doublet carried by the rectangle-center orbit is an exact eigenspace with $$\boxed{\lambda_{E,s}=6+2s\beta}$$ of multiplicity two.*
:::

::: proof
*Proof.* Only the rectangle-center orbit contains $E$. The $E$ component has unit-Laplacian eigenvalue $6$, the depth is constant $2s$ on that orbit, and there are no interlayer $E$ copies on any other vertex orbit that could couple to it. \(\square\)
:::

The remainder of the spectral analysis will specialize to the declared benchmark $\beta=1$. This specialization is a mathematical normalization inside Definition [9](#def:Hrb){reference-type="ref" reference="def:Hrb"}; no empirical parameter is inferred from it.

# 7. Infinite refinement and spectral convergence

Let $K_\infty=\bigcup_{r\ge1}K_r$ and define on $\ell^2(V(K_\infty))$ $$H_\infty=L_0(K_\infty)+D.$$ The graph has uniformly bounded degree, with maximum degree 17, so the graph Laplacian is bounded.

::: {#thm:compact .theorem}
**Theorem 11** (Compact resolvent). *The operator $H_\infty$ has compact resolvent. Consequently its spectrum is purely discrete and may be written $$\lambda_1^\infty\le\lambda_2^\infty\le\cdots\to\infty.$$*
:::

::: proof
*Proof.* The multiplication operator $D$ has finite multiplicity at each finite depth and tends to infinity along every sequence escaping to radial infinity. Therefore $(D+1)^{-1}$ is compact. Since $L_0$ is bounded, $H_\infty=D+L_0$ is a bounded perturbation of $D$, and the resolvent identity preserves compactness. \(\square\)
:::

Let $H_r$ denote the finite free-boundary operator on $K_r$. At $r=1$ an outer-shell vertex has degree 4 in $K_1$ and 11 after an annulus is attached; at $r≥2$ the respective degrees are 10 and 17. In both cases the difference is 7. If $P_{S_r}$ projects onto the four outer-shell coordinates, then the principal compression of the infinite operator is $$\boxed{H_r^D=P_rH_\infty P_r=H_r+7P_{S_r}}.$$

::: {#thm:fixedindex .theorem}
**Theorem 12** (Fixed-index spectral convergence). *For every fixed eigenvalue index $k$, $$\boxed{\lambda_k(H_r)\longrightarrow\lambda_k(H_\infty)}.$$ More precisely, if $\mu_k(r)=\lambda_k(H_r^D)$ and $\nu_k(r)=\lambda_k(H_r)$, then $$\mu_k(r)\downarrow\lambda_k(H_\infty)$$ and, for any $r$-independent upper bound $C_k$ on the first $k$ free-boundary eigenvalues for sufficiently large $r$, $$\boxed{0\le \mu_k(r)-\nu_k(r)\le\frac{7C_k}{2r-1}}.$$*
:::

::: proof
*Proof.* Nested finite-support subspaces form a form core for $H_\infty$, so the Dirichlet eigenvalues decrease to the infinite-volume eigenvalues by the min--max principle. On the first-$k$ free-boundary spectral subspace, $H_r\ge D_r$ gives outer-shell mass at most $C_k/(2r-1)$. The boundary correction $7P_{S_r}$ therefore shifts the Rayleigh quotient by at most $7C_k/(2r-1)$. The two estimates squeeze $\nu_k(r)$ to the same limit. \(\square\)
:::

# 8. Block-Jacobi and Weyl reduction

The $A_1$ and $T_2$ multiplicity spaces may be grouped into radial cells $$x_s=(S_s,R_s,P_s)^T.$$ At $\beta=1$, the $A_1$ first cell is $$A_1^{(A_1)}=\begin{pmatrix}
9&-\sqrt6&-3\\
-\sqrt6&8&-\sqrt6\\
-3&-\sqrt6&11
\end{pmatrix},$$ and for $s\ge2$, $$A_s^{(A_1)}=\begin{pmatrix}
2s+13&-\sqrt6&-3\\
-\sqrt6&2s+6&-\sqrt6\\
-3&-\sqrt6&2s+9
\end{pmatrix},$$ with intercell block $$B_{A_1}=\begin{pmatrix}-1&0&0\\-\sqrt6&0&0\\-3&0&0\end{pmatrix}.$$ The central coordinate has diagonal 4 and coupling $-2$ to $S_1$.

For $T_2$, $$A_1^{(T_2)}=\begin{pmatrix}
13&-\sqrt2&1\\
-\sqrt2&8&\sqrt2\\
1&\sqrt2&11
\end{pmatrix},$$ $$A_s^{(T_2)}=\begin{pmatrix}
2s+17&-\sqrt2&1\\
-\sqrt2&2s+6&\sqrt2\\
1&\sqrt2&2s+9
\end{pmatrix},\qquad s\ge2,$$ $$B_{T_2}=\begin{pmatrix}-1&0&0\\-\sqrt2&0&0\\1&0&0\end{pmatrix}.$$ Both intercell blocks have rank one.

::: {#thm:weyl .theorem}
**Theorem 13** (Schur and Weyl reduction on its stated domain). For $X\in\{A_1,T_2\}$ and $z\in\mathbb C\setminus\mathbb R$, the self-adjoint tail resolvents define the recursive block Schur matrices
$$M_s(z)=zI-A_s-B_X[M_{s+1}(z)]^{-1}B_X^T.$$
For fixed such $z$, the confining diagonal gives $[M_s(z)]^{-1}=O(s^{-1})$ for sufficiently large $s$; the finite-section resolvents converge to the infinite tail resolvent. With $B_X=b_Xe_1^T$, define $m_s=e_1^TM_s^{-1}e_1$. Wherever $R_s=zI-A_s$ and the displayed scalar denominator are invertible,
$$m_s=g_s+\frac{c_s^2m_{s+1}}{1-d_sm_{s+1}},$$
where $g_s=e_1^TR_s^{-1}e_1$, $c_s=e_1^TR_s^{-1}b_X$, and $d_s=b_X^TR_s^{-1}b_X$.
:::

*Proof.* Block elimination gives the Schur recursion. The finite-support spaces form a core for the depth operator and its bounded graph perturbation, giving resolvent convergence in the nonreal half-planes. Tail lower bounds grow linearly in $s$, yielding the stated inverse estimate. Sherman-Morrison gives the scalar formula on the explicit inverse domain. Intermediate local inverses are not guaranteed merely by being off the full real spectrum; singular local factors require the block form or continuation.

For a probe $v$, the scalar measure is
$$m(z)=\sum_\lambda\frac{\|P_\lambda v\|^2}{z-\lambda}.$$
It detects only eigenvalues with nonzero probe overlap. The equation $z-4-4m_1^{(A_1)}(z)=0$ is the center Schur equation where the tail inverse exists; poles of $m_1^{(T_2)}$ identify visible modes. Neither description is asserted to exhaust all eigenvalues without an infinite cyclicity/no-dark-mode proof. Full finite Krylov ranks 25 and 24 at $N=8$ do not establish infinite cyclicity. The matrix operator, compact-resolvent result and the min-max enclosures below do not depend on this unresolved scalar completeness claim.

## Variational enclosures

The coupling norms are $$\|B_{A_1}\|=4,\qquad \|B_{T_2}\|=2.$$ For the constant parts of the radial cells, $$\lambda_{\min}(C_{A_1})=9-\sqrt{33},$$ while a sufficient exact lower bound in the $T_2$ sector is $$\lambda_{\min}(C_{T_2})\ge 6-2\sqrt2.$$ Cutting after cell $N$ gives tail lower bounds $$\boxed{\tau_{A_1}(N)=2N-1-\sqrt{33}},\qquad
\boxed{\tau_{T_2}(N)\ge2N+2-2\sqrt2}.$$ Let $H_N$ be the principal $N$-cell compression and $L_N=H_N-\|B\|Q_N$, with $Q_N$ the projector onto the final cell. Once the tail floor lies above the spectral window of interest, $$\boxed{\lambda_k(L_N)\le\lambda_k(H_\infty)\le\lambda_k(H_N)}.$$ **Proposition III.R1 (reconstructed infinite enclosures).** For each displayed sector the first two infinite multiplicity-space eigenvalues lie strictly in the rational intervals below.

$$\frac{1033383283816991}{500000000000000}<\lambda_{A1,1}^\infty<\frac{1033383283818821}{500000000000000}.$$

$$\frac{1047884525038269}{250000000000000}<\lambda_{A1,2}^\infty<\frac{2095769050167537}{500000000000000}.$$

$$\frac{2674412199079}{400000000000}<\lambda_{T2,1}^\infty<\frac{208938453053047}{31250000000000}.$$

$$\frac{2241757927796809}{250000000000000}<\lambda_{T2,2}^\infty<\frac{2241757927796987}{250000000000000}.$$

*Proof.* A rational diagonal similarity with positive metric $\operatorname{diag}(1,6,9)$ in $A_1$ and $\operatorname{diag}(1,2,1)$ in $T_2$ removes radicals without changing spectra. The supplementary reconstruction computes the integer characteristic polynomials of $H_8,L_8$, checks nonzero endpoints and counts exactly $k-1$ roots of $L_8$ below the lower endpoint and $k$ roots of $H_8$ below the upper endpoint. For the infinite comparison, each tail cell has $A_s=2sI+C$. The cross-term inequality costs at most $\|B\|$ on either side of an edge; internal tail edges cost at most $2\|B\|$ per cell, and the cut costs $\|B\|$ on the final retained cell. Thus
$$H_\infty\succeq L_N\oplus\tau_X(N)I.$$
At $N=8$, $\tau_{A_1}>9$ since $\sqrt{33}<6$, and $\tau_{T_2}>15$ since $\sqrt2<3/2$. Both floors exceed both respective spectral windows, so min-max and the principal-compression upper bound give the strict intervals. $\square$

The exact polynomials and root counts are newly reconstructed from the displayed blocks, not recovered original author certificates. Decimal renderings are only optional numerical views of these rational intervals. No physical scale or scalar completeness premise enters this proof.

## Asymptotic radial recurrence

Eliminating the local $R_s,P_s$ coordinates gives a scalar three-term recurrence $$u_{s+1}=Q_X(s,z)u_s-P_X(s,z)u_{s-1},$$ with rational coefficients. As $s\to\infty$, $$P_{A_1}\to1,\qquad Q_{A_1}=2s-z-2+O(s^{-1}),$$ $$P_{T_2}\to1,\qquad Q_{T_2}=2s+14-z+O(s^{-1}).$$ Thus the minimal tail is of discrete-Stark/Bessel type. The exact named object used here is the matrix Weyl function / continued fraction; no reduction of the full rational recurrence to an ordinary scalar Bessel or hypergeometric family is asserted.

# 9. Six-edge relation algebra and second-order pair currents

The six unordered tetrahedral edges form a permutation module $$\mathbb{R}^6=A_1\oplus E\oplus T_2.$$ There are exactly two nontrivial $S_4$ orbits of unordered pairs of distinct edge coordinates: adjacent edges and opposite edges.

Let $A_{\rm adj}$ and $A_{\rm opp}$ be the corresponding adjacency matrices, and let $$L_{\rm adj}=4I-A_{\rm adj},\qquad L_{\rm opp}=I-A_{\rm opp}.$$ Then $$P_{A_1}=\frac16J,\qquad P_{T_2}=\frac12L_{\rm opp},\qquad P_{E}=I-P_{A_1}-P_{T_2},$$ and therefore $$\boxed{L_{\rm opp}=2P_{T_2}},\qquad
\boxed{L_{\rm adj}=6P_{E}+4P_{T_2}}.$$ The two relation Laplacians order $E$ and $T_2$ oppositely, so symmetry alone does not choose a preferred ordering or a unique positive linear combination.

::: {#ng:ratio .nogo}
**No-go 14** (No source-forced universal relation ratio). *The finite hard gates and unary edge route weights of the companion source grammar do not determine a universal scalar ratio $w_{\rm opp}/w_{\rm adj}$ for the two relation Laplacians.*
:::

The no-go is a type statement: a binary matching gate and a state-dependent weight on a single edge are not second-order edge-pair couplings. Relation counts alone also fail to decide the ratio: equal weight per relation pair gives one convention, while equal total weight per relation orbit gives another.

A coefficient-free second-order object can nevertheless be derived from any declared nonnegative six-edge source lane $\lambda$.

::: {#def:paircurrent .definition}
**Definition 15** (Quadratic pair-current lift). Set $$\mathbb J^{(2)}_{ef}=(1-\delta_{ef})\lambda_e\lambda_f.$$
:::

The adjacent and opposite relation masks have exact source expressions $$\boxed{A_{\rm adj}=|B_1|^T|B_1|-2I},\qquad
\boxed{A_{\rm opp}=P_\Theta^TP_\Theta-I},$$ where $P_\Theta$ is the $3\times6$ matching-address matrix. Therefore $$J_{\rm adj}^{(2)}=\frac12\lambda^TA_{\rm adj}\lambda,\qquad
J_{\rm opp}^{(2)}=\frac12\lambda^TA_{\rm opp}\lambda.$$ If $W_p=\sum_{e\in M_p}\lambda_e$, then the same quantities are recovered from the existing matching aggregates: $$\boxed{J_{\rm opp}^{(2)}=\frac12\left(\sum_pW_p^2-\sum_e\lambda_e^2\right)},$$ $$\boxed{J_{\rm adj}^{(2)}=\frac12\left[\left(\sum_e\lambda_e\right)^2-\sum_pW_p^2\right]}.$$ Their ratio is state dependent and is not promoted to a universal constitutive constant.

# 10. Minimum symmetry type for cross-sector context

The preceding sections are closed finite mathematics. A final representation-theoretic corollary identifies what symmetry type an auxiliary context would need in order to linearly couple $E$ and $T_2$.

::: {#thm:context-min .theorem}
**Theorem 16** (Minimum context dimension). *Let $R$ be an irreducible $S_4$ context representation. A nonzero equivariant map $$R\otimes E\longrightarrow T_2$$ can exist only for $R=T_1$ or $R=T_2$. In particular, the minimum possible context dimension is three.*
:::

::: proof
*Proof.* The exact tensor products are $$E\otimes A_1=E,\qquad E\otimes A_2=E,$$ $$E\otimes E=A_1\oplus A_2\oplus E,$$ $$E\otimes T_1=T_1\oplus T_2,\qquad
E\otimes T_2=T_1\oplus T_2.$$ Thus $T_2$ is absent for all one- and two-dimensional context irreps and present for both three-dimensional irreps. \(\square\)
:::

The three-state weight-one and weight-two Hamming shells of the matching-bit carrier transform as $A_1\oplus E$, so they do not by themselves meet the criterion in Theorem [16](#thm:context-min){reference-type="ref" reference="thm:context-min"}. This is a representation-type no-go, not a statement about coupling strength.

## 10.1 Explicit context bases and tensor covariance

The source supplies three matrices \(\Gamma_a:E\to T_2\). To remove basis ambiguity, put
\[
Q=\begin{pmatrix}0&\sqrt2/2&-\sqrt2/2\\
\sqrt6/3&-\sqrt6/6&-\sqrt6/6\\
\sqrt3/3&\sqrt3/3&\sqrt3/3\end{pmatrix},
\quad P=\operatorname{diag}(1,1,-1),
\]
and use the two diagonal traceless matrices
\[
D_1=\operatorname{diag}(\sqrt3/2,-\sqrt3/2,0),\quad
D_2=\operatorname{diag}(1/2,1/2,-1).
\]
For \(M_i=[\Gamma_1[:,i]\ \Gamma_2[:,i]\ \Gamma_3[:,i]]\), the supplied tensor satisfies exactly \(M_i=PD_iQ^T\). Its normalized tetrahedral frame is
\[
V=\frac12\begin{pmatrix}1&1&1\\1&-1&-1\\-1&1&-1\\-1&-1&1\end{pmatrix}.
\]
For a vertex permutation matrix \(R_4(g)\), set
\[
R(g)=V^TR_4(g)V,\quad
\rho_c(g)=QR(g)Q^T,\quad\rho_o(g)=PR(g)P^T,
\]
\[
[\rho_E(g)]_{ij}=\frac23\operatorname{tr}(D_iR(g)D_jR(g)^T).
\]
These formulas specify every action matrix rather than an unnamed basis convention.

**Proposition III.G1 (basis-level equivariance).** With \(\Gamma_\xi=\sum_a\xi_a\Gamma_a\),
\[
\Gamma_{\rho_c(g)\xi}\rho_E(g)=\rho_o(g)\Gamma_\xi
\qquad(g\in S_4).
\]

*Proof.* The matrices \(R(g)\) are signed permutation matrices. Conjugation preserves the two-dimensional diagonal traceless subspace, and the displayed trace formula gives its coefficients because \(\operatorname{tr}(D_iD_j)=3\delta_{ij}/2\). Thus \(R D_jR^T=\sum_i[\rho_E]_{ij}D_i\). For \(v=Q^T\xi\), the output at \(w\in E\) is \(P(\sum_iw_iD_i)v\). Applying the three declared actions gives exactly the displayed identity. \(\square\)

All 24 actions and all three context basis vectors give 72 exact matrix checks in the new replay. This is a source-derived compatible basis construction; unspecified historical action matrices were not recovered. For
\[
K_\xi=\begin{pmatrix}0&-\Gamma_\xi^T\\\Gamma_\xi&0\end{pmatrix},
\]
covariance follows under \(\rho_E\oplus\rho_o\). Its scalar interaction strength and physical polar-response interpretation remain candidate choices. Normalization of \(\Gamma\) does not fix a coupling constant.

# 11. Shape, completion and prepared growth

## 11.1 Tetrahedral frame and capped completion

**Proposition III.F1 (frame geometry; PT01).** With \(V\) above, \(VV^T=I_4-\mathbf1\mathbf1^T/4\). Its diagonal is \(3/4\), its off-diagonal \(-1/4\), and its normalized distinct-vertex cosine \(-1/3\).

*Proof.* Multiply the displayed matrix. Dividing the off-diagonal inner product by the common squared row norm gives the cosine. \(\square\)

The capped-coface proposal (PT02) specifies an alphabet with occupancy \(c_i\in\{0,1,2\}\) and deficit \(\sum_i(2-c_i)\). Its terminal support has \(2q\) vertices and simplex dimension \(2q-1\); the balanced binary \(K_4\) case is one specialization. The cap, alphabet and completion rule are supplied primitives, not consequences of the skew chain law.

## 11.2 Fresh boundary attachment and a nonregular icosahedral cone

**Proposition III.F2 (stacked-ball count; PT03).** Starting with one tetrahedron, attach each new tetrahedron to one boundary face using a fresh vertex. For \(m\) tetrahedra,
\[
f=(m+3,3m+3,3m+1,m),\qquad f_{2,\partial}=2m+2.
\]

*Proof.* Each attachment adds one vertex, three edges, three faces and one tetrahedron. It removes one boundary face and adds three. Induction from \((4,6,4,1)\) gives the formulas. The dual graph adds one leaf at each step and is a tree. Both chain and star patterns occur, so this rule does not choose a unique growth shape, size or metric. \(\square\)

PT10's icosahedral cone has twenty congruent but nonregular tetrahedra and
\[
f=(13,42,50,20),\qquad\dim\mathcal C=125.
\]
Its reduced integral homology vanishes by cone contraction. Under the source coordinates, radial edge squared length is \((5+\sqrt5)/2\), while exterior edge squared length is 4. This explicitly excludes regular tetrahedra in that construction. Five regular Euclidean tetrahedra around an edge have a positive angular gap, so the regular alternative cannot be obtained merely by renaming these cone cells. The carrier is supplied; its spontaneous formation is not proved. PT04's fixed-skew distance preservation likewise excludes attracting formation on that closed finite flow, while volume preservation of a nonlinear candidate needs a separate divergence calculation.

# 12. Burden, motif memory and renewal

## 12.1 Retention is distinct from localized binding

PT05 specifies a four-coordinate averaging law
\[
T(s)=P_0+e^{-4s/3}(I-P_0).
\]
For \(x=B\mathbf1/4+\delta\), \(\mathbf1^T\delta=0\), its contrast squared is \(e^{-8s/3}\|\delta\|^2\), and the normalized inverse participation ratio is
\[
\frac14+e^{-8s/3}\|\delta\|^2/B^2\quad(B\ne0).
\]
Total burden is retained, but contrast disappears. Uniform retention is not a compact bound cluster. A squared-decay integral carries the factor \(1/(2\alpha)\) for \(e^{-\alpha s}\) amplitude decay; omitting this factor of two overstates integrated squared contrast.

## 12.2 Ownership and temporal burden can rank motifs differently

PT06's local ownership increment \(+2\) and global unique-edge rebase \(-7/4\) concern different counting conventions. They are not incompatible physical energy measurements. The prepared chain \(0123,1234,0125,1246\) has local row totals \((9,17,17)\), global totals \((27,35,20)\), and source burden vector \((0,0,4,1,0,1,1)\). These finite identities preserve the distinction among incidence ancestry, unique ownership and a selected response norm.

The stock-capacity obligation B-NORM and the obstruction-composition obligation B-COMP remain separate. B-NORM asks for a genuinely sourced capacity \(B_*\); B-COMP asks which independently admitted obstruction contributions may be combined. A normalized stock or a successful obstruction calculation does not close the other obligation. Both must be stated before a collective burden or selection claim is promoted.

For PT07, the star and chain share the declared initial operator and prepared burden \((1,0,0,5,2,1,0)\). With graph Laplacian \(L\), the integrated contrast memory is
\[
\mathcal I=x^T(L+\mathbf1\mathbf1^T/7)^{-1}x/N.
\]
The common initial value is \(9271/5712\); the post-event values are \(2903/2856\) and \(1733/952\), with changes \(-165/272\) and \(+161/816\). Their temporal contrasts cross in \((1,2)\); the source gives a positive neighborhood of radius \(1/96\). Thus initial incidence or one scalar burden does not universally order histories. These are the specified source fixtures, not a ranking theorem for all motifs.

## 12.3 Quiescence, incomplete observation and mixing assumptions

PT08's strict-unanimous, quiescent-tie rule uses 49 zero quadratic moments and Cayley--Hamilton to establish its finite criterion. Under the connected source-free Q162 hypothesis it gives
\[
\|x(s)\|\le e^{-s/72}\|x(0)\|
\]
on the contrast subspace. Its switch clock is unbounded. Quiescence does not mean a protected nonuniform pattern. PT09's linear observation criterion and seven signed interface memories are integrated as II.M1; forgetting their signs prevents visible autonomous closure without contradicting complete PSR.

Face-reflection moments, daughter and recursive kernels, harmonic mixing, dynamic weights and renewal candidates require their declared kernels and mixing assumptions. Finite schedule telemetry cannot establish isotropy at every wavevector or a continuum limit. The four-face history lift supplies amplitudes, schedule and embedding; it does not supply native geometry creation or a collective admission law. These developments remain conditional until their preparation and source selections are derived or measured.

# 13. Finite controllers, capture and complete resource ledgers

These are conditional prepared mechanisms, consolidated through the living-audit revisions ending at v0.28. They belong here as operator comparisons and finite limitations. A possible dedicated fourth paper would carry their full apparatus and acquisition program; this edition makes no new fourth-paper publication claim.

## 13.1 Engineered history clocks and coherent fuel

PT11 uses a spin clock with links \(\kappa\sqrt{(j+1)(n-j)}\). Its comparator has terminal probability \(\sin^{2n}(\kappa t)\), transfer time \(T=\pi/(2\kappa)\), recurrence \(2T\), and spectrum \(\kappa(n-2j)\). A native/comparator mismatch bounded by \(d\) gives propagator error at most \(|t|d\) by Duhamel's identity. The history, controller and prepared finite resources are supplied.

PT12's coherent binary fuel creates a uniform ladder of length \(L=2^q\) using specified energy-conserving transfers. For stationary covariant inputs, distance from the required coherent target is bounded below by \(1-1/L\) under the source metric. This is a preparation obstruction for stationary inputs, not an impossibility result for nonstationary coherent donors. Reservoir, pump, occupation, timer and donor costs remain finite and must be counted.

## 13.2 Timed capture and its failure branches

PT13 supplies a matched involutive SWAP \(J\), source/output coordinates, a flag, and a terminal projector \(P_n\). For the supplied capture pulse,
\[
\gamma_c=\tau_c\kappa n,\qquad
a_C=\sqrt n\,\kappa\sigma+(T+\sigma)d.
\]
The source bounds failure to capture by \(\min\{1,(a_C+\gamma_c)^2\}\) and false capture by \(\gamma_c^2\). Exact native protection after capture requires the supplied pulse to be off and the factorized guard to hold. Timing, switching, successful and failed branches are all part of this claim.

**No-go III.C1 (exact closed first-entry storage; PT14).** A proper invariant subspace for a finite static Hermitian operator is reducing; a state initially in its orthogonal complement cannot first enter it. An expectation exactly constant on an open late-time interval is constant for all time.

*Proof.* Hermiticity makes the orthogonal complement invariant, so evolution cannot transfer into the invariant subspace. A finite-dimensional unitary expectation is a finite sum of exponential functions and is real analytic. Constancy on an open interval therefore extends identically. Neither argument excludes approximate capture, supplied switching or an open-system interaction. \(\square\)

## 13.3 Renewal exports correlations and consumes donors

PT15's matched SWAP exports the complete old correlations, including history, into the donor bank. Each attempt consumes donor and fresh-output stock; replacing marginal records does not reset the full joint state. The source's bank error is charged once, then combined with unconditional telescoping bounds across attempts. There is no resource wrap or perpetual renewal claim.

An exact elementary witness demonstrates the marginal/joint distinction: the equally weighted three-bit strings \(110,101,011\) give each slot success probability \(2/3\), but zero probability that all three succeed. Thus three good marginals do not certify a good joint output. Native preparation, full export, complete reset and reusable cycles remain open source obligations.

## 13.4 Static capture is a finite window, separate from timed protection

PT16 supplies a constant post-launch spin clock of length \(N+1\), rate \(\lambda\), first link \(J_*\) and later links identity. If actual/comparator Hamiltonian mismatch has norm at most \(h_p\), the complete-joint error obeys
\[
\epsilon(t)\le\min\{1,t h_p+2|\cos(\lambda t)|^N\}.
\]
On \([\pi/(4\lambda),3\pi/(4\lambda)]\),
\[
\epsilon(t)\le\min\{1,3\pi h_p/(4\lambda)+2\,2^{-N/2}\}.
\]
Comparator transfer is exact at \(\pi/(2\lambda)\), and reverses at \(\pi/\lambda\). These are pointwise finite-window bounds, not the probability of never failing under continuous monitoring. A static coupled clock is not an exactly decoupled protected output. The switched PT13 mechanism and the static PT16 comparison retain different hypotheses; neither implies permanence or inexhaustible resources.

# 14. Open choices and physical qualification

The shell triangulations and their decompositions are exact for their declared carriers. The depth potential, parameter \(\beta\), relation weights, polar context response, renewal kernel and controllers are separate supplied choices. Symmetry fixes available types and invariant spaces but does not force these coefficients. Scalar spectral visibility remains limited to the probe's spectral measure until infinite cyclicity is proved. The block operator and variational enclosures do not require that unproved completeness claim.

Prepared completion, stacked growth, an icosahedral cone and a finite history controller do not derive an initially absent carrier, a material identity or a physical formation law. Action, clock and units dictionaries do not determine empirical couplings or time. The engineering and external-data records remain conditional or dataset-scoped, and LC Stage 0 remains UNSCORED. Physical promotion is zero. Constructor and AI-assisted checks do not supply independent human review.

# 15. Claim index

| ID | Statement | Premise / evidence |
|:--|:--|:--|
| 1-2 | Signed chains and adjacent common irreps | Character decomposition and boundary equivariance |
| 3-4 | Quadratic parent; no direct E to T2 map | Exact representation argument |
| 5 | Product-graph separated spectrum | Declared graph product |
| 6-8 | Annulus, ball and shell recurrence | Explicit lists, ranks and attachment induction |
| 9-10 | Depth operator and E ladder | Declared family, beta normalization |
| 11-12 | Compact resolvent and fixed-index convergence | Bounded degree, confining depth, min-max |
| 13 | Schur/Weyl recursion on explicit domain | Nonreal tail resolvent, local inverse conditions |
| 14-15 | Relation-ratio no-go and pair-current lift | Unary source versus second-order relations |
| 16 | Minimum context dimension three | S4 tensor products |
| III.S1 | Commutant 13 / symmetric 10 / skew 3 | Signed multiplicities, exact action replay |
| III.G1 | Compatible-basis Gamma equivariance | Explicit bases and 72 exact matrix checks |
| III.R1 | Four strict infinite enclosures | Rational polynomials, Sturm counts, tail proof |
| III.F1-F2 | Frame and fresh-boundary growth counts | Matrix multiplication and induction |
| III.C1 | No exact closed first-entry storage | Reducing subspace and analyticity |
| PT02, PT05-PT16 | Conditional completion, burden and controllers | Supplied mechanisms; source proofs retained |

# 16. Reproduction and data availability

The release contains the baseline Papers I/II verifier, the bounded symmetry/radial verifier and its declared data, signed commutant sources, the explicit Gamma-basis reconstruction, and the new rational radial certificate reconstruction. The general proofs appear in this manuscript; software checks finite instances and supplied data. See `REVIEW_README.md` for commands, scope and dependencies. The radial certificate replay requires SymPy and uses exact arithmetic.

The package also retains the M1 source snapshot, addendum inventory and hash index, plus all 984 M2 dispositions. An unavailable historical certificate is not represented as included. No permanent archival identifier, independent peer review, physical validation or public deployment is implied by this draft package.

# Appendix A. Source integration and evidence authority

This edition consolidates the 26 thematic source families from the M1 inventory. The companion `INTEGRATION_DISPOSITIONS.json` and filterable register contain all 984 routed records (955 registered items and 29 additional addendum paths), with original paths, hashes, disposition and this edition's body/digest anchors. The addendum inventory contains 166 paths and 145 distinct hashes; repeated snapshots are cross-references, not additional evidence. Inventory coverage and editorial integration are not independent certification of every underlying proof. Detailed historical apparatus reports remain linked source evidence rather than new physical claims.

Legacy proposition IDs from Papers I and II edition 1.0 are retained even where a section moved. New IDs carry the paper prefix. Paper III uses the consecutive statement numbers 1-16 of its retained core, followed by the explicitly prefixed new statements. Section numbers and claim-table IDs therefore need not coincide.

A CRL label is a dated governance assertion. The supplied CRL2 subdivision proposal distinguishes proposal, preregistration/review, blinded execution and independent replication; it is not evidence that the last stages occurred. Citation depth does not deepen evidence, and a changed assumption demotes dependent conclusions until reviewed. Candidate amendments remain development-lane proposals. The coefficient ledger v0.39 supplied with older packages is an August baseline, not the ceiling for later amendments.

Original unavailable artifacts are named as provenance gaps. Reconstructed proofs and certificates have their own identity and never stand in for recovered historical bytes. Full portal publication and presentation reconciliation remain a subsequent release task.

Archive authority is determined by bytes and embedded edition together: the v2.33-named checkpoint embeds v2.32, and the v2.40-named checkpoint embeds older v2.36 text. Both names are retained as lineage, without silently treating their filenames as current scientific assertions. The journal core v0.3.2 supersedes the earlier v0.3.1 event-time account for the present digest.

## F13. Finite controllers, banks, export and capture {#F13}

**Body location:** 13. **Evidence class:** CONDITIONAL / NO-GO / OPEN. **Source records:** 74.

Account for all living-audit revisions through 0.28. Summarize controller/timer, finite reservoir, coherent fuel, occupation pumps, finite banks, record/export/reset, timed latch and static capture; carry detailed source links and budgets into appendices.

**Remaining limit:** Timed pulse-off protection and static finite-horizon capture are distinct. Permanent finite closed storage, exact first-entry absorption and stationary coherent fuel remain constrained; no native hardware or inexhaustible resource is implied.

- Source record `AD056`: UD SOURCE ADDENDUM CONTROLLER CELL CANDIDATE v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD057`: UD SOURCE ADDENDUM MATCHING CONTROLLER CANDIDATE v0.1. Original path and SHA-256 are retained in the companion register.

## F14. Signed S4 commutant and symmetry types {#F14}

**Body location:** 2.3. **Evidence class:** EXACT / OPEN choice. **Source records:** 2.

Add full commutant dimension 13, self-adjoint dimension 10 and skew-adjoint dimension 3 on signed filled-tet chains. Explain canonical boundary/adjoint choice and distinguish finite S4 from a physical gauge group.

**Remaining limit:** Symmetry permits a family; it does not uniquely derive a physical Hamiltonian or SU(5) interpretation.

- Source record `s29S4`: Exact S4 chain projectors. Original path and SHA-256 are retained in the companion register.
- Source record `s29Symmetry`: Carrier symmetry: full versus skew commutant. Original path and SHA-256 are retained in the companion register.

## F15. Radial shells, compact resolvent and variational spectra {#F15}

**Body location:** 7-8. **Evidence class:** EXACT for declared operator / OPEN completeness. **Source records:** 12.

Correct r=1 outer degree wording; add source-derived rational characteristic polynomials and exact root counts for all four N=8 enclosures. Make Schur inverse domains and scalar spectral-visibility limits explicit.

**Remaining limit:** Four exact enclosures repaired by source-derived polynomials and min-max proof; infinite scalar cyclicity and original certificate recovery remain open.

- Source record `paperIII`: Paper III - Symmetry and Radial Spectra. Original path and SHA-256 are retained in the companion register.
- Source record `symmetryRadialSource1`: Provenance.Md. Original path and SHA-256 are retained in the companion register.
- Source record `symmetryRadialSource2`: T2 Context Gamma Matrices.Csv. Original path and SHA-256 are retained in the companion register.

## F16. Relation algebra, anisotropy and minimum context {#F16}

**Body location:** 9-10.1. **Evidence class:** EXACT / CONDITIONAL / CANDIDATE / NO-GO. **Source records:** 10.

Unify adjacent/opposite edge projectors, quadratic pair currents, ordering-dependent refinement and minimum context dimension three. Distinguish Gamma normalization/polar examples from covariance in declared representation bases.

**Remaining limit:** Explicit compatible Gamma bases and 72 exact equivariance checks supplied; physical scalar interaction and original unnamed historical basis provenance remain open.

- Source record `refinementOrderingProgram`: Refinement and Observable Ordering. Original path and SHA-256 are retained in the companion register.
- Source record `harmonicAnisotropyProgram`: Harmonic Context and Anisotropy Routes. Original path and SHA-256 are retained in the companion register.
- Source record `edgeAnisotropy`: S4 Edge-to-Anisotropy Intertwiner. Original path and SHA-256 are retained in the companion register.

## F17. Shape frame, completion, growth and icosahedral carrier {#F17}

**Body location:** 11. **Evidence class:** EXACT / CONDITIONAL / NO-GO. **Source records:** 8.

Integrate PT01-PT04 and PT10: tetrahedral frame, cap completion, fresh-boundary stacked ball, growth nonuniqueness, volume-preserving no-attraction and 20 nonregular congruent tetrahedra.

**Remaining limit:** No spontaneous primitive, regular 20-tet Euclidean assembly, unique shape growth or attracting formation law is established.

- Source record `publicTheorems`: Public theorems: persistence, clustering limits and finite control. Original path and SHA-256 are retained in the companion register.
- Source record `shapeScreen`: Shape screen: frame, propagation and no-attraction controls. Original path and SHA-256 are retained in the companion register.
- Source record `shapeGrowth`: Local completion and boundary-growth limits. Original path and SHA-256 are retained in the companion register.

## F18. Burden, memory, motifs and collective retention {#F18}

**Body location:** 12; II 8.3. **Evidence class:** EXACT / CONDITIONAL / NO-GO / OPEN. **Source records:** 87.

Consolidate ancestry/unique ownership, response capacity, global rebase, semigroup retention and PT05-PT09. Include +2 local versus -7/4 global, star/chain contrast, quiescence and signed interface memory. Repair integrated squared contrast factor 1/2.

**Remaining limit:** Counting conventions, selected norm, temporal burden and spatial manifold admission are distinct; no native collective selector follows.

- Source record `r1003CollectiveObjective`: Collective objective and ownership counterexamples. Original path and SHA-256 are retained in the companion register.
- Source record `shapePersistence`: Uniform burden persistence and recovery. Original path and SHA-256 are retained in the companion register.
- Source record `collectiveMotifs`: Collective motif retention: proofs and controlled comparisons. Original path and SHA-256 are retained in the companion register.

## F19. Renewal, harmonic mixing and coarse isotropy {#F19}

**Body location:** 12.3. **Evidence class:** CONDITIONAL / CANDIDATE / NO-GO. **Source records:** 23.

Merge face reflection moments, daughter/recursive kernels, dynamic weights, candidate ergodicity and finite schedule telemetry. State the required mixing and renewal assumptions beside each limit.

**Remaining limit:** A finite scan is not all-wavevector isotropy, a continuum limit or physically realized renewal.

- Source record `renewalJointState`: Changing Face Weights and Conditional Mixing. Original path and SHA-256 are retained in the companion register.
- Source record `renewalKernel`: Proposed Recursive Support Kernel. Original path and SHA-256 are retained in the companion register.
- Source record `renewalRamanujan`: Proposed Ramanujan Identification. Original path and SHA-256 are retained in the companion register.


# References

[1] J.-P. Serre, *Linear Representations of Finite Groups*, Graduate Texts in Mathematics 42, Springer (1977). doi:10.1007/978-1-4684-9458-7.

[2] A. N. Hirani, *Discrete Exterior Calculus*, PhD thesis, California Institute of Technology (2003). doi:10.7907/ZHY8-V329.

[3] D. Horak and J. Jost, "Spectra of combinatorial Laplace operators on simplicial complexes," *Advances in Mathematics* 244, 303-336 (2013). doi:10.1016/j.aim.2013.05.007.

[4] O. Knill, "The Dirac operator of a graph," arXiv:1306.2166 (2013).

[5] G. Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, Mathematical Surveys and Monographs 72, American Mathematical Society (2000).

[6] U. Pachner, "P.L. homeomorphic manifolds are equivalent by elementary shellings," *European Journal of Combinatorics* 12, 129-145 (1991). doi:10.1016/S0195-6698(13)80080-7.

[7] W. B. R. Lickorish, "Simplicial moves on complexes and manifolds," *Geometry & Topology Monographs* 2, 299-320 (1999). arXiv:math/9911256.

[8] B. W. Mayes, Papers I and II, consolidated integration drafts 1.1 (3 October 2026), supplied in the same package.
