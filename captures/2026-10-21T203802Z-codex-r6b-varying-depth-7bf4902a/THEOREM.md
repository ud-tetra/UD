# R6b fourth-module reduction and departure from uniformity

Status: EXACT CONDITIONAL on the clean rational L=4 R6b equations and the identity metric. Constructor verification only; physical promotion 0. This result supplies neither particle identification nor action units, target-blind registration, independent review, or CRL2b completion. No archived program was executed.

## 1. Source and coordinates

Source: `docs/hmulti_r6b.py` at base commit `4c264504f1ec8ce8965b097356d7193103c9382a`. We interpret its constants rationally, eta=185/192 and delta=7/192, before floating assembly. The fourth module here means the previously unresolved module with first address digit 0, not its position in a numerical eigensolver output. Its 64 sites have addresses (0,d2,d3,d4). The identity metric and dimensionless source coefficients are retained.

Set a=eta^4, b=eta^6,

\[
v_h=\delta(1-\eta^h),\qquad
c_h=\eta^2\delta(1-\eta^h)(\eta^h-\eta^{2h}),\qquad
r_h=4\eta^2+v_h.
\]

Divide the sites into 16 sibling groups of four, indexed g=0,...,15 in source address order. Depth h is constant in each group: one group has h=4, three have h=3, and twelve have h=2. Let D be the source parity diagonal. Define orthonormal group vectors t_g=1_g/2 and p_g=D t_g. Each p_g sums to zero within its sibling group.

Embed 32 coordinates by Q(x,y)=(sum x_g p_g, sum y_g t_g). Its range is invariant under the source 128-by-128 module matrix H. In these coordinates,

\[
K=Q^T H Q=\begin{pmatrix}R&C\\C&L\end{pmatrix},\quad
R=\operatorname{diag}(r_{h_g}),\quad C=\operatorname{diag}(c_{h_g}),
\]

\[
L_{gg}=12a+48b,\qquad
L_{gj}=\begin{cases}-4a&g\ne j,\ \lfloor g/4\rfloor=\lfloor j/4\rfloor,\\-4b&\text{otherwise}.\end{cases}
\]

The executable verifier builds H independently from rational edge contributions and checks all 4096 entries of HB=BK, with B=2Q, and B^T B=4 I_32. This tests an invariant embedding, not only a Rayleigh compression.

## 2. Complement and exactly one negative eigenvalue

Write E_n for averaging over consecutive n-coordinate groups in the 16-coordinate quotient. Directly,

\[
L=64b(E_4-E_{16})+(16a+48b)(I-E_4).
\]

Thus its spectrum is 0 (rank 1), 64b (rank 3), and 16a+48b (rank 12). The positive gap is gamma=64b, since a>b. Its kernel vector is u=(1,...,1)/4.

The 96-dimensional orthogonal complement of range Q has rho vectors orthogonal to p_g in each group and Theta vectors with zero group mean. These conditions are preserved by the parity coupling. Its Theta stiffness is exactly g0=12a+48b; its rho block is bounded below by v_min I. The quadratic-form bound is

\[
\langle z,Hz\rangle\ge {v_{\min}\over2}\|x\|^2+
\left(g_0-{2c_{\max}^2\over v_{\min}}\right)\|y\|^2.
\]

The verifier checks the second coefficient is greater than v_min/2>0. Hence this complement contributes no zero or negative eigenvalues.

On the 32-coordinate sector, R is positive. At zero, Sylvester inertia reduces the negative count to the Schur complement L-C R^{-1} C. Define

\[
M=\max_{h=2,3,4}{c_h^2\over r_h}.
\]

On u-perp its quadratic form is at least (gamma-M)||y||^2>0. On u its quadratic form is strictly negative. Eigenvalue interlacing with that positive codimension-one restriction therefore gives exactly one negative eigenvalue and no zero eigenvalues. Together with the positive complement, the full 128-coordinate module has a unique negative eigenvalue lambda.

## 3. Root enclosure and profile bound

Eliminate rho at the negative eigenvalue:

\[
x=-(R-\lambda I)^{-1}Cy,\qquad
[L-V(\lambda)]y=\lambda y,\quad
V(\lambda)=\operatorname{diag}\left({c_h^2\over r_h-\lambda}\right).
\]

Since lambda is the ground eigenvalue of H, H-lambda I is positive semidefinite. Its Schur complement is positive semidefinite too, so lambda is the lowest eigenvalue of L-V(lambda). The Rayleigh principle gives lambda>=-M. Define

\[
m=\min_{h=2,3,4}{c_h^2\over r_h+M}.
\]

Then m I<=V(lambda)<=M I. Testing L-V(lambda) on u gives lambda<=-m<0. Thus

\[
-M\le\lambda\le-m.
\]

Normalize the Theta quotient vector to ||y||=1 and decompose y=alpha u+e, e perpendicular to u. The graph of L has strictly negative off-diagonal entries, so the lowest eigenvector of L-V can be chosen strictly positive: taking absolute values cannot raise its Rayleigh quotient, and a zero coordinate contradicts its eigen-equation. Consequently alpha>0.

Let d_min and d_max be the extreme diagonal entries of V(lambda), and d0=(d_min+d_max)/2. Projecting its eigen-equation perpendicular to u gives

\[
[L-(\lambda+d_0)I]e=P_{u^\perp}(V-d_0 I)y.
\]

The left-hand operator on u-perp is bounded below by gamma-M; the right-hand side has norm at most (M-m)/2. Therefore

\[
\|e\|\le\epsilon={M-m\over2(\gamma-M)}.
\]

Each quotient amplitude occupies four identical Theta sites. The conditional within-module diagnostic is consequently

\[
F_{\rm within}=16\sum_{g=0}^{15}|y_g|^4.
\]

For q_g=|y_g|^2, F_within-1=16||q-1/16||^2. Using alpha^2=1-||e||^2 and u_g=1/4, the linear part of q-1/16 has norm at most ||e||/2. The remaining part is the orthogonal projection of (|e_g|^2)_g onto the zero-sum subspace, with norm at most ||e||^2. Hence

\[
0\le F_{\rm within}-1\le4\epsilon^2(1+2\epsilon)^2.
\]

This is a bound on the channel normalized by its own nonzero weight; no denominator floor is used.

## 4. Strict nonuniformity

The verifier checks the strict rational inequalities

\[
{c_4^2\over r_4+M}>{c_3^2\over r_3},\qquad
{c_3^2\over r_3+M}>{c_2^2\over r_2}.
\]

For every lambda in the certified interval, the effective potentials therefore satisfy d4>d3>d2. If the positive ground Theta vector were uniform, its eigen-equation with Lu=0 would require these three potentials to coincide. They do not. Thus F_within>1 strictly.

Combining exact rational inequalities:

\[
\boxed{0<F_{\rm within}-1\le B<10^{-17}},\quad
B=4\left({M-m\over2(\gamma-M)}\right)^2
\left(1+{M-m\over\gamma-M}\right)^2.
\]

Decimal displays (not interval endpoints): M approximately 8.31376899744e-8, m approximately 6.97909701436e-9, epsilon approximately 7.43508511641e-10, B approximately 2.21121963410e-18. The machine-checked bound B<1e-17 is exact. Therefore prior numerical displays of 1 do not establish exact uniformity. This proof does not certify a floating assembly or its eigensolver output.

## 5. Verification and remaining gap

Run `python3 <this capture>/verify_reduction.py`; it uses only Python standard-library exact fractions. CERTIFICATE.json records the exact rational constants and checked inequalities; decimal strings serve only as readable displays. The mathematical implications above remain subject to independent review; the constructor's assertions do not substitute for it.

The three constant-depth modules were treated in draft PR354. This append-only result resolves the varying-depth module without changing that evidence or the old replay thresholds. A next useful task is the further 6-coordinate reduction under the remaining depth-group symmetries, followed by a certified root interval and channel-weight calculation. Particle correspondence, parameter-free physical action units, and any empirical bridge to quarks or leptons remain OPEN. The unavailable attachment `Gap2_FINAL_Finite_Genesis.png` is not a dependency and was not used.
