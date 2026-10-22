# The (2,1) graphite coincidence cell and a symmetry obstruction to direct octahedral matching

22 October 2026. **EXACT conditional 2D lattice and representation audit; physical promotion 0.** This capture extends the three-dimensional finite element mass audit in draft PR #413 and supplies an explicit planar honeycomb carrier for the graphite manuscript. It does not construct an interlayer force law or infer a friction coefficient.

## 1. Triangular coincidence geometry

Use planar primitive vectors \(\mathbf a_1,\mathbf a_2\) at 60° with equal length. Coordinates \((p,q)\) have Gram matrix \(G=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\), up to a lattice-length factor. A triangular 60° rotation acts as \(J(p,q)=(-q,p+q)\). For \((m,n)=(2,1)\), set \(u=(2,1)\) and \(v=(1,2)\). Both have squared length 7 in the Gram form and \(u^{\mathsf T}Gv=13/2\), so

\[
\cos\theta=\frac{13}{14},\qquad
\theta=21.786789298\ldots^\circ,\qquad
60^\circ-\theta=38.213210702\ldots^\circ.\tag{1}
\]

The two 60° triangular supercell matrices and the rotation from the \(v\) cell to the \(u\) cell are

\[
B_u=[u\ Ju]=\begin{pmatrix}2&-1\\1&3\end{pmatrix},\quad
B_v=[v\ Jv]=\begin{pmatrix}1&-2\\2&3\end{pmatrix},\quad
R=B_uB_v^{-1}=\frac17\begin{pmatrix}8&3\\-3&5\end{pmatrix}.\tag{2}
\]

Both determinants are 7; \(R^{\mathsf T}GR=G\), \(\det R=1\), and \(Rv=u\). The common triangular lattice \(\Lambda\cap R\Lambda\) includes \(B_u\mathbb Z^2\), an index-seven sublattice of \(\Lambda\). Since the index is prime and \(R\) is not integral, the intersection is exactly \(B_u\mathbb Z^2\). Its quotient is cyclic of order seven, with cosets \((k,0)\), \(k=0,\ldots,6\), distinguished by \(q(p,q)=p-2q\pmod7\). A nontrivial quotient character sums to zero over those seven cosets. This is a discrete sampling identity; no sliding barrier cancellation follows without a specified interlayer potential and atomic basis weights.

## 2. The ideal honeycomb bilayer carrier

Choose the standard two-site honeycomb basis \(A=(0,0)\), \(B=(1/3,1/3)\) in triangular coordinates. The coincidence cell contains seven Bravais cells and therefore **14 carbon sites per monolayer** and **28 layer-labeled atoms for an ideal bilayer**. With three displacement components per atom, this is an 84-dimensional coordinate space. A different number of layers, frozen substrate, rigid slider, missing atoms, or contact boundary changes the count. The manuscript's octahedral refined chain has 85 coordinates and one topological zero mode, leaving 84 active coordinates. Equality of those two numbers does not establish a physical identification.

## 3. A C3 character test of the tempting 84-to-84 match

Restrict both ideal carriers to a physical 120° rotation \(C_3\) about a coincidence A site and zero lateral offset. This is a symmetry of each ideal honeycomb layer: \(R\) commutes with planar rotations, and 120° preserves each two-site honeycomb basis modulo translations. The exact coset calculation has two fixed atom sites per layer modulo the seven-cell superlattice; the remaining sites occur in triples. For a fixed atom, the standard *three-dimensional displacement vector* transforms by a proper 120° spatial rotation of trace \(2\cos120^\circ+1=0\). Permuted sites contribute zero to the trace. The entire 84-dimensional atomic displacement representation therefore has character

\[
\chi_{\rm atom}(e)=84,\qquad \chi_{\rm atom}(C_3)=0.\tag{3}
\]

As a real \(C_3\) representation it contains **28 trivial lines and 28 rotation planes** (one two-dimensional real irreducible for each plane).

For the full 12-tetrahedron UD refinement, a tetrahedral 3-cycle acts as the corresponding 120° spatial rotation on vertices and oriented simplices. The exact signed-simplex traces by grades \(k=0,1,2,3\) are \((2,0,2,3)\), totaling 7. Exact boundary ranks are \((10,20,12)\); the Betti numbers are \((1,0,0,0)\). The sole harmonic zero mode is the invariant constant vertex vector. Removing it leaves an 84-dimensional active chain representation of trace 6, decomposing as

\[
C_{\rm UD}^{\rm active}\downarrow C_3
\cong 32\,\mathbf1\ \oplus\ 26\,\mathbf2_{\rm rot},
\quad \chi_{\rm UD}^{\rm active}(C_3)=32-26=6.\tag{4}
\]

Equations (3)–(4) have different multiplicities. A real \(C_3\)-equivariant linear map from the active UD chain to the ideal atomic displacement space can match at most \(\min(32,28)=28\) trivial coordinates and \(2\min(26,28)=52\) rotation coordinates. Hence

\[
\boxed{\operatorname{rank}T\le80,\quad
\dim\ker T\ge4,\quad \dim\operatorname{coker}T\ge4.}\tag{5}
\]

This is a **conditional no-go for a direct invertible, symmetry preserving 84-to-84 identification**, despite the dimension coincidence. It does not forbid a non-invertible measurement map, extra hidden sectors, a different carrier, a different physical representation, or a contact whose preparation breaks \(C_3\). Any such change needs an explicit source rule and its own audit.

## 4. Consequences for the graphite paper

The exact seven-cell planar carrier supplies a meaningful atom-count and symmetry target for constructing an interfacial Hessian or damping kernel. It does not select the octahedral mesh: the latter is a three-dimensional refinement of a tetrahedron, and its 84 active coordinates transform differently under the shared 120° symmetry. A UD paper can report the octahedral transfer and this representation obstruction as mathematical findings. It should not say that seven-cell graphite directly realizes the 85-chain carrier or predict friction from the count \(28\times3=84\).

The primary graphite result identifies paired (2,1) angular friction peaks with negligible load dependence [1]. Predicting their *residual after the conventional moiré account* still requires a microscopic interlayer potential, contact preparation, normal-load response, physical clock, and a preselected atom-to-chain observable. The full article curves and supplemental data remain unavailable to this record. Physical promotion stays 0.

## Reproduce and provenance

`python3 verify_seven_cell.py` checks Eqs. (1)–(5) with exact rational lattice matrices, cosets, honeycomb positions modulo the coincidence cell, signed-simplex traces, and exact boundary ranks; numerical arccos is used only to display decimal degrees. `RESULTS.json` records the claims. This is constructor validation, not independent review. The coefficient ledger v0.39(2) and CRL-2 proposal do not supply the missing correspondence.

[1] W. Chen *et al.*, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Phys. Rev. Lett.* **137**, 166201 (2026), [doi:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), public abstract.
