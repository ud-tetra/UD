# UD Hankel excitation and coefficient field audit

**RESULT — The proposed Hankel indexing is valid, but adding shifted columns from one initial state cannot produce rank 1893. Its rank is at most 105. Furthermore, the canonical characteristic-13 observability rank is 1877, which remains 1877 over the degree-12 extension.** Multiple preparation columns address excitation; a larger coefficient field cannot undo rank loss caused by reduction modulo thirteen.

Physical promotion remains **0**. This is a development calculation with no registry entry and independent review pending. The earlier real conditioning certificates are not changed or reverified here.

## Three ranks that must remain distinct

Let A be the frozen real unit-metric 2640-by-2640 generator and R the original 62-channel coordinate observer. The exact observability operator is

\[
O_{105}=\begin{bmatrix}R\\RA\\\vdots\\RA^{104}\end{bmatrix}
\in\mathbb R^{6510\times2640},\qquad \operatorname{rank}O_{105}=1893.
\]

For a single unknown state x, the history `Y=O105 x` is a 6510-entry column. That column can encode all **1893 observable state coordinates** when the operator O105 is known. Its matrix rank of one does not mean it contains only one state degree of freedom. What fails is using the SVD of one data column to infer the dimension or basis of the whole observable space.

The same distinction applies to a time-shifted Hankel matrix. Its rank measures the subspace excited by the selected preparations and visible in the outputs; it need not equal the system's observability rank. A single trajectory can reveal vector-valued amplitudes at many frequencies while providing only one temporal column-space direction per distinct eigenvalue.

## Exact factorization and the one-trajectory obstruction

For `y_k=R A^k x0`, define the block Hankel matrix by

\[
H_{L,M}(x_0)_{(k,c),j}=(R A^{k+j}x_0)_c,
\quad0\le k<L,\quad0\le c<62,\quad0\le j<M.
\]

It has dimensions `62L by M` and factors exactly:

\[
H_{L,M}(x_0)=O_L K_M(x_0),\qquad
K_M(x_0)=[x_0,Ax_0,\ldots,A^{M-1}x_0].
\]

The frozen real generator has degree-105 minimal polynomial. Hence its powers above order104 reduce to lower powers, so

\[
\operatorname{rank}H_{105,M}(x_0)
\le\operatorname{rank}K_M(x_0)
\le\min(M,105).
\]

This bound holds even for 1893 columns or arbitrarily many columns. A generic real initial state can reach the temporal bound105 when all visible eigenvalues are excited, but it cannot span repeated-eigenvalue state directions merely through time shifts. `M>=1893` is only a necessary column-count condition for rank 1893 in an arbitrary matrix, and is insufficient for this structured matrix.

The supplied code also checks a small exact counterexample: A consists of three identical two-dimensional rotation blocks, and R is the six-dimensional identity. The system is fully observable with rank 6. A single-state Hankel matrix with 12 rows and 7 columns has rank 2. Three independent preparations raise the corresponding block Hankel rank to6. This illustrates why observable state dimension and one-trajectory Hankel rank differ.

The frozen recurrence can be written `p(A)=0`, where

\[
p(t)=t\,\left(q_L(x)/x\right)\big|_{x=-t^2},
\qquad\deg q_L=53,\quad\deg p=105.
\]

The real annihilator follows from the earlier exact full-carrier certificate and real skew-adjoint semisimplicity. In this audit, the reduced row identity `R p(A)=0 mod13` is checked directly as well. It makes the 105-column bound and finite history stabilization valid for the reduced output sequences without assuming finite-field semisimplicity.

## Correct multi-preparation structure

Choose p independently prepared states and collect them as

\[
X=[x_1,\ldots,x_p]\in\mathbb R^{2640\times p}.
\]

The corrected response Hankel matrix is

\[
H_{L,M}(X)=\left[RA^{k+j}X\right]_{k,j}
=O_L[X,AX,\ldots,A^{M-1}X].
\]

Its dimensions are `62L by pM`. A fully explicit flattened index is

\[
i=62k+c,\quad \ell=pj+a,\quad
H_{i,\ell}=(R A^{k+j}x_{a+1})_c,
\]

with `0<=a<p`. The block Hankel consistency condition relates the same preparation and channel: increasing k by one is equivalent to increasing j by one, whenever both indices remain in range. To build L-by-M windows, each preparation needs the derivative sequence through order `L+M-2`, or `L+M-1` vectors in total. The proposed L=105,M=1893 matrix would therefore require 1997 derivative vectors, not 1893.

The real rank 1893 condition is

\[
\operatorname{im}[X,AX,\ldots,A^{M-1}X]+\ker O_{105}
=\mathbb R^{2640}.
\]

This is the missing excitation condition. Column count alone is not a substitute.

For unrestricted real preparations, the frozen modal rank table sharpens the requirement. On each nonzero irreducible L-factor of degree d, divide its real observable dimension by2d to obtain the observable multiplicity of each complex A-eigenvalue. The maximum is **37**, attained by the squared-frequency factor `L-4`, whose real observable dimension is74. A single preparation supplies at most one direction within each complex eigenspace, so **at least37 preparations** are necessary.

For the semisimple real observable quotient,37 generic preparations are also sufficient when M=105: degree104 interpolation isolates every distinct eigenvalue, and the projected preparations generically span each visible eigenspace. The resulting sufficient layout has dimensions **6510 by 3885**, using 209 derivative vectors per preparation. This is an existence and genericity theorem; no specific 37 preparations or their conditioning are certified in this audit. It does not claim that M=105 is the smallest possible shift horizon.

A straightforward guaranteed alternative is `X=I2640`, M=1: the response matrix is exactly O105, with dimensions 6510 by 2640 and real rank 1893. This uses 2640 known basis preparations. Neither derivative design replaces the earlier bounded-error finite-sampling protocol.

## Exact characteristic thirteen calculation

The follow-up assumes that real rank 1893 carries into the degree-12 field. It does not. Reducing the actual integer A and R modulo13 and stacking the 105 derivative blocks gives:

| Coefficient field | Rows | Columns | Rank | Kernel dimension |
|---|---:|---:|---:|---:|
| Real numbers, frozen parent result | 6510 | 2640 | 1893 | 747 |
| F13, computed in this audit | 6510 | 2640 | **1877** | **763** |
| F_(13^12), same matrix after scalar extension | 6510 | 2640 | **1877** | **763** |

The modular rank was computed by exact elimination and rechecked by reduced row echelon form. A full 763-column kernel basis is included. Its free-coordinate submatrix is the identity, proving independence, and exact multiplication verifies `O105 N=0`. The reduced recurrence proves stabilization for all further formal power observations.

Field extension preserves the rank of a fixed matrix. Thus even all basis preparations cannot reach rank 1893 over this canonical reduced model. The drop of16 is a coefficient-field effect, not an extra physical loss or a contradiction of the real result. A redesigned field-valued generator would be a new model requiring its own calculation.

## Field indexing does not supply SVD or an exponential clock

Each field entry can validly be expanded as

\[
H_{(k,c),(j,a)}=\sum_{r=0}^2\sum_{s=0}^3
C_{k,c,j,a,r,s}\,b^r g^s,\qquad C_{k,c,j,a,r,s}\in\mathbb F_{13}.
\]

Use equality in the polynomial extension field. Integer congruence modulo13^12 denotes a different ring. The four powers `1,g,g^2,g^3` are a coefficient basis, not four or ten separate character sectors. The ten sectors are selected by the projectors P_m. The cubic powers likewise have no demonstrated identification as color or gauge components.

Ordinary real SVD and positive singular-value thresholds are not finite-field rank procedures. Use exact elimination over the stated field. A full restriction-of-scalars representation of an F_(13^12)-linear map uses12-by 12 multiplication blocks and multiplies both its domain/codomain dimensions and rank by 12. Merely listing twelve coefficients in each entry is not that construction and supplies no new observable state information.

Also distinguish derivative sequences from actual sampled dynamics. Over the reals, uniformly sampled data use `T=exp(Delta A)` and `y_j=R T^j x0`; their Hankel factorization uses T, not A. Since T is a function of the frozen semisimple A, one real trajectory still has at most105 temporal directions, potentially fewer under aliasing. Over characteristic13 the usual exponential series is not defined as written: factorials from 13 onward are noninvertible. A discrete transition matrix or another explicit valid construction must be supplied before using finite-field time samples.

There is still no derived nonabelian gauge spectrum or revived 1146 index theorem. Correct data layout and exact arithmetic answer excitation and rank questions. They do not select physical symmetries or calibrate an observation clock.

## Recommended next step

Use the real model for the existing finite-sample physical-bridge candidate. Select and certify independent preparations against the actual modal excitation condition, with explicit error bounds and conditioning. Keep the finite-field layer as a separate algebraic verification model with its measured rank 1877. A specific 37-preparation construction is a candidate next task, not an achieved result here.
