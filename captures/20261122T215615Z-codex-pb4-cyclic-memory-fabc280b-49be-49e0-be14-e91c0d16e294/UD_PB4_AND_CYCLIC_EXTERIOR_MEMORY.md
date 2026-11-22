# PB4 radial memory and the cyclic bipyramid exterior resolvent

**Physical Promotion = 0.** Constructor evidence for independent review. The radial ordering compares stable spectral gaps for PB3, PB4, and PB5. For PB4 the exact transfer also identifies the leading memory decay rate.

## PB4 radial pencil and transfer

Take the tetrahedra $(j,j+1,4,5)$ around the square rim with indices modulo four. Work with the unit simplex coefficient metric, the oriented total boundary $\partial$, the skew operator $A=\partial-\partial^\mathsf T$, and the orthogonal projector $P$ onto the span of the cell vertex indicators. Put $Q=I-P$. The face vector is $(6,13,12,4)$. Each rim vertex receives the two neighboring cell coefficients, and each pole receives their sum. The only indicator relation is the alternating one. Hence $P$ has rank three and $Q$ has rank 32. Let $S$ project onto the axial and eight spoke edges. The radial generator on $Q$ is $Q(A-gS)Q$.

Define $q_c(z)=z^2+gz+c$ and $p_4(z)=z^3+gz^2+4z+2g$. The replay constructs the exact incidence and projection matrices and verifies the monic characteristic polynomial on $Q$,
$$
(z^2+2)^2(z^2+4)^2(z^2+6)^2 q_4^2 q_6^4 q_{16/3}p_4^2.
$$
The first three factors describe 12 undamped dimensions. On the normalized forcing support, the three transfer channels are the collective channel and the two transverse channels from the resolved vectors $v_0-v_2$ and $v_1-v_3$. The replay verifies their pairwise orthogonal invariant spaces and reads off the normalized Laplace transform
$$
-\operatorname{diag}\left(
\frac{z}{q_{16/3}},\,
\frac{2z^2+gz+8}{2p_4},\,
\frac{2z^2+gz+8}{2p_4}\right).
$$
The numerator and denominator resultants are $16/3$ and $2g^4$ up to a constant from numerator normalization, so no factors cancel for $g>0$. The minimal memory realization has dimension eight. Multiplicity across channels and a double pole at critical damping are counted as dimensions. The neutral sector and the $q_4,q_6$ factors contribute zero to this transfer.

## All-positive-coupling stable gap order

The cubic discriminant is $-8(g^2-13/4)^2-343/2<0$. Parameterize its unique real root by $-r$, with
$$
g=\frac{r(r^2+4)}{r^2+2},\qquad s=\frac{g-r}{2}=\frac{r}{r^2+2}.
$$
The map $r\mapsto g$ is strictly increasing from zero to infinity. The conjugate pair has real part $-s$, strictly to the right of $-r$. For each PB4 quadratic and every stable factor of PB3, translate by $p(z-s)$. The replay checks that all leading Hurwitz minors are strictly positive for $r>0$ by coefficient signs. Thus these roots all lie strictly left of $-s$ before translation. In particular $s$ is both the PB4 stable gap and its leading memory decay rate.

Use the PB5 stable sextic and PB3 factor inventory from [PR #597](https://github.com/ud-tetra/UD/pull/597), also used by [PR #605](https://github.com/ud-tetra/UD/pull/605). The PB5 sextic's fifth leading Hurwitz minor at this shift is
$$
-\frac{2r^3(2r^8+25r^6+155r^4+484r^2+340)}{(r^2+2)^3}<0.
$$
If all its shifted roots lay in the closed left half-plane, an additional arbitrarily small shift of the roots to the left would make every leading Hurwitz minor positive. Continuity of the minors in the polynomial coefficients would force this fifth minor to be nonnegative. The contradiction puts a stable PB5 root strictly to the right of $-s$ in the unshifted pencil. Hence
$$
\Delta_{\rm PB5}(g)<\Delta_{\rm PB4}(g)=\Gamma_{\rm PB4,mem}(g)<\Delta_{\rm PB3}(g)
\qquad (g>0).
$$
This proof uses stable spectra for PB3 and PB5. PB5 all-coupling memory-pole visibility and the PB5/PB3 ratio supremum remain open.

## Exterior-only resolvent for every cyclic bipyramid

Let $N\ge3$ and take cells $(j,j+1,a,b)$ for $j$ modulo $N$, with rim vertices $j$ and axial poles $a,b$. Use the exterior Whitney edge sink of [PR #606](https://github.com/ud-tetra/UD/pull/606) with zero radial damping. Let $D$ denote the vertex-edge boundary matrix, $L=DD^\mathsf T$ and $B=-D^\mathsf T$ on the resolved vertex space. This $B$ is the forcing block $QAP$ because $A$ maps vertices into edges. On such forcing vectors, $A_Q=QAQ$ satisfies $A_Q Bv=-QLv$. The potential face component vanishes by $\partial^2=0$.

For a cyclic Fourier coefficient vector of frequency $m$, the rim part of the cell-average map is multiplication by a phase factor of the form $1+e^{\pm 2\pi i m/N}$. The axial part is zero when $m\ne0$. The sole missing mode is $m=N/2$ for even $N$. Thus the resolved rank is $r_N=N-\mathbf 1_{2\mid N}$. For each retained nonzero frequency, its rim-vertex mode is an eigenvector of $L$ since its rim sum vanishes. Therefore $A_Q Bv=0$ on transverse forcing.

At frequency zero the resolved vector before normalization is the sum of cell indicators, with value $2$ on each rim vertex and $N$ at each pole. Let $v$ be its unit normalization and $e$ the unit constant vertex vector. The component of $v$ perpendicular to $e$ is an $L$ eigenvector with eigenvalue $N+2$. Indeed, on rim-constant, pole-symmetric vertex values $(x,y)$, $L$ acts as $(2(x-y),N(y-x))$. If $c=e^\mathsf T v$, then
$$
c^2=\frac{(4N)^2}{(N+2)(4N+2N^2)}=\frac{8N}{(N+2)^2},\qquad
Qe=e-cv.
$$
Thus $A_Q Bv=(N+2)cQe$ and $A_Q^2 Bv=-(N+2)c^2Bv$. No resolved vector is a nonzero constant, so $B$ is injective on the resolved space.

The face restriction of each gradient $Bv$ has zero signed circulation. The local Whitney edge matrix therefore acts on it as $2I/3$. Each rim or spoke edge is contained in two exterior faces, and the axial gradient is zero because the resolved pole values agree. The exterior sink consequently acts as $4I/3$ on the forcing space and vanishes on the vertex partner $A_Q Bv$.

Write $d=4g_{\rm ext}/3$ and $C_N=(N+2)c^2=8N/(N+2)$. With $P_0$ the projector onto the collective channel in normalized forcing coordinates, the exterior-only transfer and active determinant are
$$
\widetilde{\widehat K}_N(z)
=-\frac{I-P_0}{z+d}-\frac{zP_0}{z^2+dz+C_N},\qquad
\mathcal D_N(z)=(z+d)^{r_N-1}(z^2+dz+C_N).
$$
The rational replay cross-checks the invariant-space identities for $N=3,4,5,6,7,8$. The Fourier and zero-mode calculation proves the formula for every integer $N\ge3$. This carrier family excludes the two-cell control, which uses a separate complex.

## PB4 finite-horizon benchmark and numerical correction

At $g_{\rm ext}=4$, the PB4 exterior poles are $-4/3$, $-4$ and $-16/3$. The squared linear determinant factor represents two transverse channels. The collective and transverse time channels are
$$
k_0(t)=\tfrac12 e^{-4t/3}-\tfrac32 e^{-4t},\qquad
k_\perp(t)=-e^{-16t/3}.
$$
The normalized operator norm equals the maximum of their absolute values. The two opposite-sign collective terms give the upper envelope $\max(\tfrac12 e^{-4t/3},\tfrac32 e^{-4t},e^{-16t/3})$. The exact pointwise error after retaining the slow collective residue is the maximum of the last two terms.

The replay uses rational Taylor brackets at $t=29/10$. Each envelope term decreases, proving $\|\widetilde K_4(t)\|_2<0.0105<1/62$ and slow-residue approximation error $<1.4\times10^{-5}$ uniformly from then onward. This includes the shared two-cell horizon. At $t=29/10$ the norm exceeds $0.0104$ and the error exceeds $7.204\times10^{-6}$. These lower bounds correct the incoming brief's proposed uniform bounds of $0.00123$ and $7.204\times10^{-6}$. The benchmark concerns the normalized kernel and slow-residue approximation. Optimized settling parameters, resolved-evolution closure error, and physical calibration remain open.

## Replay and review

Run `python3 replay_pb4.py` with SymPy installed and compare stdout with `replay-results.txt`. Check the monic factorization and the radial invariant spaces, the shift orientation and Hurwitz signs, the Fourier argument for arbitrary $N\ge3$, and the corrected rational settling bounds.
