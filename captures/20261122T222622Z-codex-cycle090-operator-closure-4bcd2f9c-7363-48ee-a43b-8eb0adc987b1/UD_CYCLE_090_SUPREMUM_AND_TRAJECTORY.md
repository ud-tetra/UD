# CYCLE-090 ratio supremum and exterior trajectory bound

**Physical Promotion = 0.** Constructor evidence pending independent review. The radial comparison uses zero exterior damping. The trajectory bound uses raw exterior coupling 4 and zero radial damping.

## Global PB5/PB3 ratio supremum

Let $R(g)=\Delta_{\rm PB5}(g)/\Delta_{\rm PB3}(g)$ for $g>0$ on the pinned stable spectra of [PR #605](https://github.com/ud-tetra/UD/pull/605). Let $L=5(10-\sqrt5)/57$, the exact weak-coupling limit from [PR #596](https://github.com/ud-tetra/UD/pull/596).

Parameterize the unique PB3 real cubic root as $-r$. Then
$$
g=\frac{r(r^2+5)}{r^2+2},\quad
\Delta_{\rm PB3}(g)=\frac{3r}{2(r^2+2)},\qquad r>0.
$$
The cubic has negative discriminant and the map $r\mapsto g$ is strictly increasing onto $(0,\infty)$. The complex pair lies to the right of $-r$. The replay independently checks that each PB3 quadratic translated by the displayed gap is strictly Hurwitz, completing the leading-root selection.

Let $s=L\Delta_{\rm PB3}$, and translate the pinned stable PB5 sextic $p_5(z)$ to $q(z)=p_5(z-s)$. To clear denominators, scale the roots of $q$ by $u=r^2+2$. If $q(z)=\sum_{k=0}^6 a_kz^{6-k}$, the rescaled monic polynomial has coefficients $a_ku^k$. The fifth Hurwitz minor scales by $u^{15}>0$.

The negative fifth minor of the rescaled polynomial belongs to $\mathbb Q(\sqrt5)[r]$ and has exactly 16 nonzero coefficients, on degrees $5,7,\ldots,35$. Every coefficient is strictly positive. The replay constructs the determinant in the exact quadratic field and verifies each sign by rational square comparisons, with zero coefficients checked through the degree inventory. Hence the original fifth minor is negative for every $r>0$. If the shifted sextic roots were all in the closed left half-plane, moving them a further arbitrarily small distance left and passing to the limit would make all Hurwitz minors nonnegative. Thus a stable PB5 root lies strictly right of $-s$ before translation, regardless of which PB5 branch has the largest real part. It follows that
$$
R(g)<L\quad(g>0),\qquad \sup_{g>0}R(g)=L.
$$
The supremum is approached as $g\downarrow0$. This proof is compatible with the eventual upturn established in [PR #598](https://github.com/ud-tetra/UD/pull/598).

## Uniform local-in-time trajectory error with prepared unresolved data

Use the exterior-only operator from [PR #606](https://github.com/ud-tetra/UD/pull/606) and the cyclic Fourier decomposition staged in [PR #607](https://github.com/ud-tetra/UD/pull/607), with $N\in\{3,4,5\}$ and $d=16/3$. Use the unit coefficient norm on the resolved subspace and impose $Qy(0)=0$. The local approximation is the zero-frequency memory closure $x'_{\rm loc}=M_0x_{\rm loc}$ with $M_0=\int_0^\infty K(s)\,ds$ in orthonormal resolved coordinates and the same $x(0)$.

The resolved skew block vanishes because the skew incidence operator sends vertices into edges. In each Fourier channel, the unnormalized kernel is the normalized kernel times the squared forcing norm $k$. Orthogonal channels follow from the circulation decomposition, with Fourier stiffness $k_m=2+4\sin^2(\pi m/N)$ for retained nonzero $m$. This is the rim cycle Laplacian plus the two spoke contributions. For the unit collective vector the squared forcing norm is
$$
k_0=(N+2)(1-c^2)=\frac{(N-2)^2}{N+2},\qquad c^2=\frac{8N}{(N+2)^2}.
$$
This uses the nonconstant part of the collective vector, on which the vertex Laplacian has eigenvalue $N+2$. The resulting collective quadratic constant together with the resolved feedback satisfies $C_N+k_0=N+2$.

**Collective channel.** Its signed kernel integral vanishes, so the local response to a unit initial coordinate is 1. The difference between the exact prepared response and 1 has Laplace transform
$$
-\frac{k_0}{z(z^2+dz+N+2)}.
$$
It is the negative integral of a nonnegative overdamped impulse response. Its magnitude is bounded for every time by $k_0/(N+2)\le9/49$. As time tends to infinity it attains that channel's limiting error magnitude $k_0/(N+2)$.

**Transverse channels.** Write $\alpha,\beta$ for the positive decay rates of $z^2+dz+k_m$, with $\alpha<\beta$. The largest stiffness is $(9+\sqrt5)/2<d^2(3/8)/(1+3/8)^2$, so $q=\alpha/\beta<3/8$. Put $\mu=k_m/d$. The exact prepared response minus the local response is
$$
\left(e^{-\alpha t}-e^{-\mu t}\right)
+\frac{\alpha}{\beta-\alpha}\left(e^{-\alpha t}-e^{-\beta t}\right).
$$
The terms have opposite signs since $\alpha>\mu$. The first magnitude is at most $((\alpha-\mu)/\mu)/e=q/e<3/16$, by the bound on $t e^{-\mu t}$. The second reaches its maximum $q^{1/(1-q)}$, by setting its derivative to zero. This maximum increases with $q$ since $q^{-1}-1+\log q>0$ for $0<q<1$. It is less than $(3/8)^{8/5}<21/100$, with the last comparison made exactly by taking fifth powers.

Taking the largest channel bound proves, for all $T\ge0$ and each of PB3, PB4, and PB5,
$$
\sup_{0\le t\le T}\|x(t)-x_{\rm loc}(t)\|_2
\le\frac{21}{100}\|x(0)\|_2 .
$$
The constant is an upper bound for the declared closure. The proof uses the full channel responses from the initial time. The kernel settling tolerance $1/62$ is a separate benchmark. The proof covers prepared initial data at the declared coupling. Bounds for general unresolved initialization, other coupling regimes, or stricter trajectory tolerances remain open. The PB4 carrier construction is still pending independent review in PR #607.

Run `python3 replay_supremum_and_trajectory.py` with SymPy and compare stdout with `replay-results.txt`. Review the PB3 root selection, shifted PB5 minor, and exact scalar closure bounds.
