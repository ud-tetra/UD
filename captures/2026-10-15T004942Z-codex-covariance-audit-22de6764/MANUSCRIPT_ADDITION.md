## D.17 Receipt consistency, covariance and errors it cannot reveal

### D.17.1 The declared signless tree map

The filled tetrahedron has a Hasse graph with 15 simplex vertices and 28 adjacent-degree containment edges. Choose the 14-edge spanning tree and 14 chords specified in the certificate [30]. For a declared latent field $z\in\mathbb R^{15}$, let $S,H\in\{0,1\}^{14\times15}$ map $z$ to endpoint sums on tree and chord edges. These are signless observation matrices, not the signed boundary operator or skew generator.

The graph is bipartite by simplex-degree parity. Let $v$ have value $-1$ on even degrees and $+1$ on odd degrees. Then $Sv=Hv=0$. Connectivity gives $\ker S=\operatorname{span}\{v\}$, so every chord row is in the tree row space. Along its odd-length tree path, alternating the endpoint sums cancels internal vertices and retains the two endpoints. Hence

\[
H=CS,\qquad C\in\{-1,0,1\}^{14\times14}.
\]

For the supplied tree, $\operatorname{rank}S=14$ and $\operatorname{rank}H=\operatorname{rank}C=10$. The longest chord path has seven edges. A different tree can change $C$ and its error amplification. The graph argument is standard incidence/path algebra; the certificate identifies this particular split, not a new general reconstruction method.

A possible magnitude-receipt application requires a separate map. On full nonzero support, if a product receipt is $|J_{ij}|=2|B_{ij}||c_i||c_j|$, define $z_i=\log|c_i|$ and $y_{ij}=\log(|J_{ij}|/(2|B_{ij}|))$. Then $y_{ij}=z_i+z_j$. Zero amplitudes, phase/sign information and calibration require additional treatment. Applying these signless matrices directly to the chain amplitudes instead defines another observable. The null direction $v$ is a measurement gauge: $Av\ne0$ for the native canonical generator, so it is not a harmonic carrier mode.

### D.17.2 What zero residual covariance establishes

For noiseless observations $Y_S=Sz$ and $Y_H=Hz$,

\[
r=Y_H-CY_S=0
\]

holds for every realization, independently of Gaussianity or the dynamics that generated $z$. With finite second moments, $\Sigma_{HH}=C\Sigma_{SS}C^T$ and $\Sigma_{HS}=C\Sigma_{SS}$. If $M=(I;C)$, any positive semidefinite supplied training covariance produces

\[
\Sigma_{28}=M\Sigma_{SS}M^T\succeq0,
\quad \operatorname{rank}\Sigma_{28}=\operatorname{rank}\Sigma_{SS}.
\]

The equality of ranks follows because $M$ has the left inverse selecting its first 14 rows. The 14 independent columns of $(-C^T;I)$ lie in the covariance kernel. They span the entire kernel only when $\Sigma_{SS}$ is positive definite; otherwise the kernel is larger.

Thus zero residual from the same generated latent field confirms the enforced observation identity. It does not independently validate the carrier evolution, a source law or a physical prediction. Any alternative latent history passed through the same matrices satisfies it too. A covariance propagation identity is not an empirical held-out success.

### D.17.3 A residual error contract and its blind subspace

Now declare independently acquired channels with errors, allowing arbitrary correlations:

\[
\widetilde Y_S=Sz+e_S,\qquad\widetilde Y_H=Hz+e_H,
\qquad r=e_H-Ce_S.
\]

Writing $R_{ij}=\operatorname{Cov}(e_i,e_j)$, finite second moments give

\[
\operatorname{Cov}(r)=R_{HH}+CR_{SS}C^T-R_{HS}C^T-CR_{SH}.
\]

The cancellation of $z$ is pointwise, so this formula does not require the errors to be independent of $z$. For zero-mean independent equal-variance errors across all 28 channels it becomes $\sigma^2(I+CC^T)$, positive definite when $\sigma>0$. For componentwise error bounds,

\[
\|r\|_\infty\le\varepsilon_H+7\varepsilon_S
\]

on this tree. The row-specific coefficient is its path length, ranging from three to seven here. These are supplied noise contracts, not a derived sensor law. The residual mean must also be tested: a constant nonzero $e_H=b$, $e_S=0$ has zero covariance but residual $b$.

Finally set $L=(-C,I)$. Its full blind error subspace is

\[
\ker L=\{(u,Cu):u\in\mathbb R^{14}\},\qquad\dim\ker L=14.
\]

Such errors change both blocks consistently and produce zero residual. Since $S$ is surjective, each is the observation of some latent-field perturbation. Additional roots or stock references can resolve aspects of the measurement gauge, but a dynamics test still needs a specified temporal prediction or other independent observable. The residual can detect failures of the declared receipt consistency relation; passing it cannot establish that all state estimates, event sources or physics are correct. This distinction qualifies how the sampled receipts of D.16 can be audited without claiming unearned predictive validation.
