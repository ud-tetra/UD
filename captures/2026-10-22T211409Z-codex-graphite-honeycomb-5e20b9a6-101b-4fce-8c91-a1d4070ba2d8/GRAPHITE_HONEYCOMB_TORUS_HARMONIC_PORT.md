# A seven-cell honeycomb torus and its geometry-selected sliding port

22 October 2026. **EXACT conditional cellular topology and unit-metric spectrum; CANDIDATE translation interpretation; physical promotion 0.** This is a planar alternative to assigning atomistic graphite to the 3D midpoint-octahedral chain. It builds the nearest-neighbor cell complex of a single ideal periodic honeycomb layer at the (2,1) coincidence index. The interlayer force and dissipative material law remain separate.

## 1. The seven-cell quotient determines the graph and faces

Label the seven triangular Bravais cosets by (k=p-2q\pmod7). The direct primitive steps have labels (a_1\mapsto1) and (a_2\mapsto5). A two-site honeycomb basis has physical positions (A_n=n), (B_n=n+\tau), with (\tau=(a_1+a_2)/3). Under periodic identification there are 14 atom sites (A_k,B_k). Each (B_k) has three nearest-neighbor bonds to (A_k,A_{k+1},A_{k+5}). Thus there are 21 bonds.

The graph has seven hexagonal faces under the inherited periodic planar embedding. Its cell counts and Euler characteristic are

\[
 (f_0,f_1,f_2)=(14,21,7),\quad\chi=14-21+7=0,\quad
 (b_0,b_1,b_2)=(1,2,1).\tag{1}
\]

This is a cellular torus: the last Betti assertion is verified by the explicit signed boundaries below. It is not a triangulation by atom sites, and its 42 cellular coordinates are not 14 atoms times three Cartesian displacements.

For a compact exact constructor, triangulate the **dual** triangular lattice quotient on seven vertices using positively oriented triangles

\[
 T^A_k=[k,k+1,k+5],\qquad T^B_k=[k+1,k+6,k+5],\quad k\in\mathbb Z/7.\tag{2}
\]

Every unordered vertex pair is one of its 21 edges (a (K_7) 1-skeleton). Each edge is in exactly two oppositely oriented triangles. Let (P_1\in\mathbb Z^{7\times21}), (P_2\in\mathbb Z^{21\times14}) be signed boundaries, so (P_1P_2=0), with ranks 6 and 13. The dual honeycomb complex takes its atom sites from these 14 triangles, bonds from the 21 edges, and hexagons from the seven vertices. After diagonal orientation flips (S_{ee}=\pm1) that orient each dual bond from (A) to (B), its boundaries are

\[
 B_1=P_2^T S\quad(14\times21),\qquad
 B_2=S P_1^T\quad(21\times7),\qquad
 B_1B_2=0.\tag{3}
\]

The ranks are (\operatorname{rank}B_1=13,\operatorname{rank}B_2=6). Therefore (\dim H_1=21-13-6=2), and Eq. (1) follows exactly. Seven hexagons, rather than the octahedron's 12 volume tetrahedra, are the immediate periodic geometry of this graphite cell.

## 2. Exact unit-metric cellular spectrum

The unit-edge vertex Laplacian (L_0=B_1B_1^T=P_2^TP_2) is the 3-regular honeycomb graph Laplacian. Fourier character (\zeta^k), (\zeta^7=1), has bipartite adjacency symbol (\phi_k=1+\zeta^k+\zeta^{5k}). At (k=0), (|\phi_0|=3). For (k=1,\ldots,6), the differences of the exponents (0,1,5) cover all six nonzero residues in conjugate pairs, so

\[
 |\phi_k|^2=3+\sum_{r=1}^{6}\zeta^{rk}=2.\tag{4}
\]

Consequently

\[
 \operatorname{spec}(L_0)=\{0^{(1)},6^{(1)},
 (3-\sqrt2)^{(6)},(3+\sqrt2)^{(6)}\}.\tag{5}
\]

The unit-face Laplacian (L_2=B_2^TB_2=P_1P_1^T=7I-J) has spectrum (\{0^{(1)},7^{(6)}\}), because the dual triangular 1-skeleton is (K_7). For the standard skew Hodge–Dirac generator on (C_0\oplus C_1\oplus C_2), the 42-dimensional characteristic polynomial is

\[
 \boxed{\det(\lambda I-A)=\lambda^4(\lambda^2+6)
 (\lambda^4+6\lambda^2+7)^6(\lambda^2+7)^6.}\tag{6}
\]

The four zero coordinates are the torus Betti modes (1+2+1); each nonzero singular value of (B_1) and (B_2) contributes a pair of imaginary generator eigenvalues. These numbers are unit-metric structural quantities, not frequencies in seconds or graphite phonon modes.

## 3. The harmonic 1-space selects a lateral translation readout

Orient every honeycomb bond from (A) to (B). In primitive direct coordinates with (a=1), the three physical bond directions are

\[
 d_0=(1/3,1/3),\qquad d_1=(-2/3,1/3),\qquad
 d_2=(1/3,-2/3),\qquad d_0+d_1+d_2=0.\tag{7}
\]

Let (G=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}) be the direct-coordinate Euclidean Gram matrix. For a planar vector (u), define the edge cochain (M u\in\mathbb R^{21}) by ((Mu)_e=d_e^TGu), using the appropriate (d_j) for each edge. The same three directions occur seven times. An exact calculation with Eq. (3) gives

\[
 B_1M=0,\qquad B_2^TM=0,\qquad
 M^TM=\frac72 G.\tag{8}
\]

Since (\dim H_1=2) and (M) has rank two, its image **is the entire unit-metric harmonic 1-space** (\ker B_1\cap\ker B_2^T). In these declared lattice units, the geometry-selected lateral readout of an arbitrary edge state (q\in C_1) is

\[
 \boxed{u_{\rm geom}(q)=(M^TM)^{-1}M^Tq
 =\frac27G^{-1}M^Tq.}\tag{9}
\]

The map depends on the actual honeycomb embedding and chosen unit edge metric; it is equivariant under the planar (C_3) rotation and has a known normalization. It is an *edge-cochain representation of a planar vector*, not an assertion that rigid intralayer translation strains the bonds or that a chain coordinate is literally an atomic displacement. It replaces the arbitrary selection of one of 26 octahedral rotation planes with a unique two-dimensional harmonic sector **for this planar carrier**.

For two ideal layers, form one harmonic plane per layer with each layer's rotated bond geometry. Their shared translation and relative translation are the diagonal and difference of the two geometric planes. The relative vector (u_{\rm top}-u_{\rm bottom}) is the lateral argument of the conventional registry energy from draft PR #416. The normalized relative cochain with (u_{\rm bottom}=-u/2), (u_{\rm top}=u/2) has squared unit-edge norm (\frac74u^TGu). Choosing that lift amounts to removing the common translation direction and using equal layer weights; unequal mass or edge metrics require a new normalization.

## 4. Dynamics and what is still missing

For a closed unit-metric Hodge–Dirac generator, every (q\in\operatorname{im}M) obeys (A(0,q,0)=0) exactly by Eq. (8). The native planar carrier therefore supplies a *protected zero sector and a normalized readout*, but no restoring corrugation, angular peak, viscous drag or physical time scale. Adding the first conventional common Fourier shell (E_1(u,z)) can lift relative translation by an externally sourced material amplitude (V_*(z)); any damping requires an explicit open-system bath. The scalar response model of draft PR #415 can then be applied to this **specified two-coordinate port**, conditional on its material stiffness and damping. None of the structural eigenvalues in Eq. (6) may be identified with a measured friction feature without the atomistic state/evolution map.

This planar result is a stronger *geometry-selection rule* than the 3D octahedral 84-to-84 dimension coincidence. It does not make the octahedral analysis false; the octahedron remains a finite subdivision study, while the honeycomb torus is the immediate periodic interface carrier. The paper should lead with the conventional (2,1) baseline and this planar harmonic port, then discuss the octahedral no-go as a warning about transferring a 3D carrier to graphite. Physical promotion stays 0.

## Verification

`verify_honeycomb_h1.py` constructs the exact signed integer boundaries and rational bond cochains. It checks both boundary ranks, Betti numbers, the unit-metric Laplacian polynomial identities and multiplicities, the harmonic conditions and Gram matrix, and the two-layer relative normalization. This is constructor validation, not independent peer review or a graphite fit. The source article's accessible abstract reports angular peaks and negligible measured friction load dependence, but its full data and supplement remain subscription restricted [1].

[1] W. Chen *et al.*, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Phys. Rev. Lett.* **137**, 166201 (2026), [doi:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2).
