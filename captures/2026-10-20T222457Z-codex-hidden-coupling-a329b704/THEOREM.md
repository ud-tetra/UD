# Hidden-mode coupling, rank activation and finite-sample conditioning

Development — no registry entry. DERIVED conditional finite-model theorems; exact source identities and rational bounds checked. External promotion review PENDING. Physical Promotion=0.

## 1. Fixed premises and objects

Use the existing unit-metric 600-cell chain generator A, A^T=-A, and the single vertex-link readout R with62 coordinate channels. Let N be its nominal dynamical kernel and V=N^perp. The inherited exact observer theorem gives dimN=747, dimV=1893, with one hidden and one visible stationary harmonic. These old ranks are premises here, not newly rerun. Because A is skew and N invariant, N and V reduce A; RN=0 and ||R||=1.

All operators below act in those same real Euclidean chain coordinates. Time is internal model time. Unknown physical units, preparation/calibration or actual-generator membership are not supplied by this analysis. A change of generator is a changed mathematical model, not a leak under unchanged nominal dynamics.

## 2. Internal hidden dynamics versus cross-coupling

**Theorem HC1 (exact invisibility of hidden-only changes).** For every real skew D=P_N D P_N, every initial state x and every real t,

\[
R e^{t(A+D)}x=R e^{tA}x.
\]

Proof: in V⊕N both generators are block diagonal, share A|V and have R=[R|V,0]. Their hidden blocks may differ arbitrarily. There are747·746/2=278631 independent real skew parameters on N. This parameter count does not preserve all other proposed UD constitutive constraints or make the hidden states gauge redundancy.

**Theorem HC2 (coupling-only transfer ceiling).** Let K be any constant real skew generator, with C=P_V K P_N and ||C||≤ε. Its diagonal blocks may have arbitrary norms. For n∈N,

\[
\|P_V e^{tK}n\|\le
\sin\!\left(\min\{\epsilon |t|,\pi/2\}\right)\|n\|.
\]

If the readout at actual time s is R+E_s, ||E_s||≤η, the signal from n has norm at most the preceding right side plus η||n||, with t replaced by s. For nominal0≤t≤T and |s-t|≤τ one may replace |s| by T+τ. This is an upper bound, not evidence that coupling/noise exists, and not a detectable-signal lower bound.

Proof: normalize ||n||=1 and split x(t)=v(t)+w(t). K is skew, so ||x||=1. The internal V block contributes zero to d||v||²/dt, giving |d||v||²/dt|≤2ε||v||||w||. Wherever0<||v||<1, its angle θ=arcsin||v|| has derivative at most ε. Continuity/one-sided limiting comparison from θ(0)=0 proves the sine ceiling up to π/2; the norm bound1 proves the rest. Apply the argument to -K for negative time. Finally ||R v+E_s x||≤||v||+η. The2D rotation attains the state-transfer ceiling. No exponential dependence on the hidden block's frequency or norm is needed. This theorem assumes Euclidean skewness; it is not transferred to a general nonnormal/dissipative plant.

## 3. Exact 600-cell harmonic coupling

Let u0 be one on all120vertex coordinates and zero elsewhere. Let h0 be the consistently oriented fundamental3-cycle with600coefficients±1 on tetrahedra. Set

\[
u=u_0/\sqrt{120},\quad h=h_0/\sqrt{600},\quad
K_\epsilon=A+\epsilon(uh^T-hu^T).
\]

New exact checks reconstruct all simplicial boundary-of-boundary cancellations, orient the connected tetrahedral dual graph, verify B3h0=0 and the uniform vertex gradient zero, reconstruct the vertex link and its62indices, and check the signed rightC10action against vertex images. Thus Au=Ah=0, u⊥h, ||u||=||h||=1, Rh=0 and ||Ru||²=12/120=1/10. Both u and h are fixed by the declared signed action T.

The perturbation has operator norm ε, commutes with T and is skew. Like A, it anticommutes with the chain-parity involution (-1)^grade. It does **not** preserve the even/odd state subspaces individually. It directly couples degrees0and3, so it is not the native adjacent-degree Hodge–Dirac form, a locality-preserving incidence perturbation, a Pachner move or a derived source law. Symmetry, parity and norm conservation alone therefore cannot enforce nominal blindness over this broader class.

Exactly,

\[
e^{tK_\epsilon}h=\cos(\epsilon t)h+\sin(\epsilon t)u,
\qquad \|R e^{tK_\epsilon}h\|=|\sin(\epsilon t)|/\sqrt{10}.
\]

Suppose ε>0 and ε² is not a root of the parent Laplacian polynomial q. The only changed invariant plane is span(u,h); all remaining old frequencies and readout maps remain unchanged. The visible stationary rank1 is replaced by rank2 at the distinct frequencies±ε. Consequently

\[
\operatorname{rank}O(K_\epsilon,R)=1894,\quad
\dim N(K_\epsilon,R)=746.
\]

The surviving kernel is the old oscillatory N∩h^perp. This is a constructive family with arbitrarily small nonzero perturbation: every ε=2^-k, integer k≥20, has nonintegral rational square, which cannot be a root of the monic integer polynomial q. The three displayed cases are also evaluated exactly. It does not say every arbitrarily weak coupling raises rank, or that missing dimensions can be stably reconstructed.

Since T fixes the harmonic plane, only m=0 changes: its isolated history rank255→256 and hidden dimension9→8. Other sector ranks are unchanged; the sum of isolated ranks2523→2524. The individually dark total117→116 and full kernel747→746 leave the mixed-sector quotient630unchanged. These are derived from the inherited sector ranks and the distinct-frequency argument; no new2640dimensional rank computation is claimed.

## 4. Finite-sample qualification and positive singular values

Define the normalized state-observation map

\[
F_{M,\epsilon}=M^{-1/2}\operatorname{stack}_{j=0}^{M-1}
 R e^{jK_\epsilon/2}.
\]

The new exact polynomial check establishes52distinct nonzero squared-frequency roots in(0,16); the inherited observer annihilator hence gives all old observed signed frequencies in(-4,4). For the displayed ε≤2^-20, the106observed signed frequencies have distinct half-step nodes: their phases lie in(-2,2), whose diameter4<2π. A106-row temporal Vandermonde separates all frequency coefficients. Thus for every M≥106 the sampled and continuous kernels coincide, and sampled rank is1894. This argument is essential: a small output from an arbitrary unit vector would not by itself bound the smallest positive singular value.

Let tbar=(M-1)/4 and a=εtbar. The orthonormal states

\[
h_\epsilon=\cos(a)h-\sin(a)u,\qquad
u_\epsilon=\cos(a)u+\sin(a)h
\]

lie in the sampled kernel's orthogonal complement. Their outputs are respectively Ru times sin(ε(tj-tbar)) and cos(ε(tj-tbar)). Grid reflection kills their cross-Gram. Write

\[
S_c=M^{-1}\sum_j\sin^2(\epsilon(t_j-\bar t)).
\]

The two-plane restricted Gram is diag((1-S_c)/10,S_c/10), in uε,hε order. When S_c≤1/2, the full map therefore satisfies

\[
\sigma_{\min,+}(F_{M,\epsilon})\le\sqrt{S_c/10},
\qquad
\kappa_+(F_{M,\epsilon})\ge\sqrt{(1-S_c)/S_c}.
\]

Here κ+ means largest divided by smallest **positive** singular value. The2640column map still has746zero singular values; its full-state inverse condition number is infinite. The two-plane lower singular enclosure below is **not** a lower bound for σmin,+ of the full map; other modes can be worse.

For |ε(tj-tbar)|≤1, exact elementary sine inequalities give

\[
\epsilon^2 v-\epsilon^4 w/3\le S_c\le\epsilon^2 v,
\quad v=(M^2-1)/48,
\quad w=(M^2-1)(3M^2-7)/3840.
\]

Both moments were independently checked by rational summation. Exact integer square-root brackets, not decimal outputs, carry the inequalities in RESULT.json. For M=4096:

| ε | Upper bound on σmin,+ of full map | Lower bound on κ+ |
|---|---:|---:|
|2^-20|<1.7830×10^-4|>1773.61|
|2^-30|<1.7412×10^-7|>1.8161×10^6|
|2^-40|<1.7004×10^-10|>1.8597×10^9|

The displayed numbers round outward from rational enclosures. These are model examples, not tolerances selected to pass an experiment. They certify that exact rank activation and finite-window recoverability differ sharply. They concern this state-observation map, not the37preparation Hankel matrix, the321column floating-estimator sketch, or the separate κ<2029 certificate. No prior gate or noise ceiling is changed.

## 5. Provenance, checks and remaining boundary

SOURCE_BINDINGS.json pins the immutable archive and its3JSONmembers. No archived script was executed. HARMONIC_WITNESS.json supplies the actual600orientation signs and62readoutindices. compute.py regenerates the new exact geometry/action/moment/polynomial checks and rational enclosures using only Python's standard library; give --repo and --out explicitly as documented in README. The original1893/747and isolated ranks are inherited proof premises, not repeated computations. No dense2640²perturbation or287GiBHankel was allocated.

These are conditional proofs and finite arithmetic checks. Separate same-team adversarial review does not constitute external promotion review. No experimental acquisition, fresh physical preparation, estimator fit, calibration/SI certificate, actual coupling estimate or source-supported physical realization was supplied. Existing nominal results and HOLD/NO-GO findings are preserved. A native perturbation class and independently justified bounds on cross-coupling/readout errors remain OPEN before applying HC2 to an apparatus.
