# PB3 radial memory decay

CYCLE-088 (#592) · PB5 comparison (#593) · **Physical Promotion = 0**

## Exact result

PB3 already has exponential decay of the selected Mori–Zwanzig memory kernel for every fixed positive radial sink strength with zero exterior damping. Three cells are minimal within the family of bipyramids over simple polygonal rims.

## Fixture and kernel

Use the unit coefficient metric on the 27 simplex coordinates of the downward closure of tetrahedra 0134, 0234, 1234, with counts $(5,10,9,3)$. Set $A=\partial-\partial^\mathsf{T}$ with increasing-vertex orientation. Let $U$ contain the three vertex indicators, $G=U^\mathsf{T}U$, $E=UG^{-1/2}$, and $Q=I-EE^\mathsf{T}$. The cell indicators overlap on shared faces, so the projection uses their Gram matrix.

Let $R$ select the spine edge 34 and the six edges from the poles to the rim. The rank-seven sink $D=R^\mathsf{T}R$ equals $MM^+$ for the assembled radial face-edge flags. The carrier is the Complex B fixture. PR #456 uses a separate four-coordinate sink and a separate uncompressed damping partition.

On $\operatorname{im}Q$ set $L_0=QAQ$, $L_\gamma=L_0-\gamma D$, and $F=QAE$. The sink kills $E$, giving the kernel

$$K_\gamma(t)=-F^\mathsf{T}e^{tL_\gamma}F.$$

## Exact certificate

The rows of $[R;U^\mathsf{T}]$, extended by right multiplication with $L_0$, have cumulative ranks $10,17,19,19$. Their common nullspace $N$ is the maximal $L_0$-invariant subspace of $\operatorname{im}Q\cap\ker R$. Its dimension is eight and its characteristic polynomial is $(z^2+2)^2(z^2+5)^2$. For a basis matrix $V$ of $N$, exact arithmetic gives $V^\mathsf{T}QAU=0$.

Skew symmetry and $DN=0$ make $N^\perp\cap\operatorname{im}Q$ invariant under $L_\gamma$. An imaginary-axis eigenvector $x$ in this complement would satisfy $0=\operatorname{Re}(x^*L_\gamma x)=-\gamma\lVert Rx\rVert^2$. At positive coupling this requires $Rx=0$, so $L_0x=L_\gamma x$ and $x\in N_\mathbb{C}$, a contradiction. The 16-dimensional complement therefore has strictly negative spectral abscissa for every $\gamma>0$ and contains the image of $F$. Thus $\lVert K_\gamma(t)\rVert_F\le C_\gamma e^{-\kappa_\gamma t}$ for suitable positive constants depending on $\gamma$.

The exact squared initial Frobenius norm is $1251/25$. At zero coupling the compressed flow is skew and the kernel recurs arbitrarily close to its initial value. The replay gives diagnostic samples at zero and unit coupling. At time 20 the unit-coupling norm is approximately $6.814\times10^{-4}$.

## Scope

PB3 and PB5 both exhibit decay under the same internal radial sink construction. The two-cell shared-face result uses a different interface geometry. This certificate concerns asymptotic decay for each fixed coupling. Uniform rates, finite settling horizons, exterior-coupling scaling, and a controlled Markov approximation remain separate CYCLE-088 questions.
