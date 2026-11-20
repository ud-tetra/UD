# Tetrahedral Packet Complexes: Hodge–Dirac Transport, Projective Receipts, and Retriangulation

**Benjamin Walker Mayes**

**Manuscript state:** `LEAN JOURNAL REFACTOR v2.3 — POC-1 PUBLIC-CORPUS ADMISSIBILITY NO-GO`  
**Source scientific baseline:** `UD JOP v1.9 + provenance ledger v0.44`  
**Scientific change:** `APPEND-ONLY EMPIRICAL SOURCE-ADMISSIBILITY NO-GO`

## Abstract

We study a finite relational dynamics on tetrahedral packet complexes while separating exact discrete mathematics from physical interpretation. The local carrier is the tetrahedral graph \(K_4\) with automorphism group \(S_4\), together with an opposite-edge binary fiber \(\Theta\cong\mathbb F_2^3\). On the filled tetrahedron we use the oriented simplicial chain complex of dimensions \(4,6,4,1\) and a real skew Hodge–Dirac generator. The single-cell carrier satisfies the exact identity
\[
\mathcal A^2=-4(I-P_{H_0}),
\]
which yields one harmonic zero mode, fourteen nonzero directions at frequency magnitude \(2\), and exact conservation of the quadratic chain support. On glued tetrahedral complexes we derive oriented Hasse-current balance laws and analyze a finite \(2\leftrightarrow3\) Pachner relay. The current A/B/C relay has exact spectra with B/C signed-permutation covariance and no finite nonzero common recurrence. The central new observable-facing result is a Projective Support Receipt (PSR). We prove that current receipt summaries do not identify the chain ray, derive a sufficient PSR consisting of normalized simplex supports, forest-relative signs, and one root sign per support component, and prove exact projective reconstruction and event-level covariance through the current relay. For the fully supported filled tetrahedron, the Hasse graph provides an intrinsic \(28=14+14\) reconstruction/held-out split. A coherent photonic map is given as a faithful representation of the support and bilinear-current observables; its held-out experimental test remains pending. No identification with physical spacetime, energy, elementary particles, or empirical coupling constants is claimed.

## 1. Introduction and contribution boundary

This paper isolates a finite mathematical core of the Unified Dynamics (UD) research program. The object studied here is not assumed to be physical spacetime, a quantum field, or a completed unification theory. The aim is narrower: define a finite tetrahedral carrier, derive its transport and receipt structure exactly, identify what information is and is not reconstructible, and specify a falsifiable observable realization without importing downstream physical constants.

The construction uses standard ingredients from simplicial homology, Hodge/Dirac-type finite operators, finite group actions, and finite-dimensional operator theory. Those ingredients are background. The claimed contribution is their specific organization on the declared tetrahedral packet carrier together with the following results:

1. a symmetry-resolved \(S_4\times\Theta\) finite exposure architecture with \(\Theta\cong\mathbb F_2^3\);
2. exact single-cell and glued-carrier support transport identities on the declared chain complex;
3. exact finite retriangulation constraints, including B/C signed-permutation covariance and a no-common-recurrence result for the current A/B/C relay;
4. receipt-conditioned \(\Theta\) transport identities and an exact source-complete relative-frame extractor;
5. a chain-ray nonidentifiability theorem for the pre-PSR receipt set;
6. a sufficient PSR and exact projective reconstruction theorem;
7. PSR forest-choice gauge equivalence and A/B/C event covariance;
8. an intrinsic \(28=14_{\rm reconstruction}+14_{\rm heldout}\) falsification design on the fully supported filled tetrahedron.

The main unresolved scientific issue is constitutive: the finite transport architecture does not by itself determine which event occurs. Source-complete frame extraction is available; general event polarity/multiplicity remains conditional on additional source receipts. This constitutive gap is treated as an explicit open problem rather than repaired by fitting.

The remainder of the paper is mathematical. Physical correspondence is discussed only as an open map.

## 2. Tetrahedral carrier and oriented chain complex

### 2.1 Tetrahedral carrier and opposite-edge fiber

Let
\[
V(K_4)=\{1,2,3,4\},
\qquad
E(K_4)=\{12,13,14,23,24,34\}.
\]

Then
\[
|V(K_4)|=4,
\qquad
|E(K_4)|=\binom42=6,
\qquad
\operatorname{Aut}(K_4)\cong S_4.
\]

The three perfect matchings are
\[
M_A=\{12,34\},\qquad
M_B=\{13,24\},\qquad
M_C=\{14,23\}.
\]

Assign one binary coordinate to each opposite-edge class:
\[
\Theta:=\mathbb F_2^3.
\]
The Hamming observable
\[
w_H(\theta)=\theta_A+\theta_B+\theta_C
\]
has shell multiplicities
\[
1,3,3,1.
\]

The product carrier
\[
\mathcal X_1=S_4\times\Theta
\]
has cardinality
\[
|\mathcal X_1|=24\cdot8=192.
\]
This is a finite carrier count only.

### 2.2 Filled tetrahedral chain carrier

Use the ordered vertices
\[
0<1<2<3,
\]
edge basis
\[
(01,02,03,12,13,23),
\]
face basis
\[
(012,013,023,123),
\]
and oriented 3-cell \(0123\).

The chain dimensions are
\[
\boxed{
\dim C_0=4,\qquad
\dim C_1=6,\qquad
\dim C_2=4,\qquad
\dim C_3=1.
}
\]

With the canonical orientation, the boundary maps satisfy
\[
\boxed{
B_1B_2=0,
\qquad
B_2B_3=0.
}
\]

Their ranks are
\[
\operatorname{rank}B_1=3,\qquad
\operatorname{rank}B_2=3,\qquad
\operatorname{rank}B_3=1,
\]
so the filled tetrahedron has
\[
\boxed{
\dim(H_0,H_1,H_2,H_3)=(1,0,0,0).
}
\]

The explicit matrices are retained in Appendix A.

## 3. Hodge–Dirac transport and support continuity

### 3.1 Skew transport and conserved support

On
\[
\mathcal C=C_0\oplus C_1\oplus C_2\oplus C_3,
\]
define
\[
\boxed{
\mathcal A=
\begin{pmatrix}
0&-B_1&0&0\\
B_1^T&0&-B_2&0\\
0&B_2^T&0&-B_3\\
0&0&B_3^T&0
\end{pmatrix}.
}
\]

Then
\[
\mathcal A^T=-\mathcal A.
\]

For
\[
\dot c=\mathcal A c,
\]
the quadratic support
\[
S_\mu(c)=c^Tc
\]
obeys
\[
\boxed{
\frac{dS_\mu}{ds}=0.
}
\]

This is finite norm conservation. No physical energy interpretation is assumed.

### 3.2 Exact single-cell spectrum and decomposition

Let \(P_{H_0}\) be the orthogonal projector onto the uniform vertex harmonic mode. The canonical tetrahedral incidence matrices satisfy
\[
\boxed{
\mathcal A^2=-4(I-P_{H_0}),
\qquad
\mathcal A^3+4\mathcal A=0.
}
\]

Equivalently,
\[
\det(\lambda I-\mathcal A)=\lambda(\lambda^2+4)^7.
\]

Thus the single-cell carrier contains one harmonic zero mode and fourteen nonzero directions with frequency magnitude \(2\). The resulting recurrence parameter is \(\pi\); it is an internal flow parameter, not physical time.

The chain carrier decomposes orthogonally as
\[
\mathcal C
=
H_0
\oplus
(C_0^\perp\oplus\operatorname{im}B_1^T)
\oplus
(\operatorname{im}B_2\oplus\operatorname{im}B_2^T)
\oplus
(\operatorname{im}B_3\oplus C_3),
\]
with dimensions
\[
1,\;6,\;6,\;2.
\]

On \(C_1\),
\[
\Pi_{\rm cut}=\frac14B_1^TB_1,
\qquad
\Pi_{\rm cyc}=\frac14B_2B_2^T,
\qquad
\Pi_{\rm cut}+\Pi_{\rm cyc}=I_{C_1}.
\]
Because \(H_1=0\),
\[
\ker B_1=\operatorname{im}B_2.
\]

For a normalized pure edge-cycle \(z\in\ker B_1\),
\[
c_1(s)=\cos(2s)z,
\qquad
c_2(s)=\frac12\sin(2s)B_2^Tz,
\qquad
c_0(s)=c_3(s)=0.
\]

### 3.3 Hasse currents and control-volume balance

For incident adjacent-degree simplices \(\sigma\subset\eta\), define
\[
\boxed{
J_{\sigma\eta}
=
2B_{\sigma\eta}c_\sigma c_\eta.
}
\]

For any finite Hasse control volume \(\mathcal R\),
\[
S_\mu(\mathcal R)=\sum_{\sigma\in\mathcal R}c_\sigma^2.
\]

**Theorem 3.1 (Exact support control-volume balance).**
\[
\boxed{
\frac{d}{ds}S_\mu(\mathcal R)
=
J_{\rm in}(\mathcal R)-J_{\rm out}(\mathcal R),
}
\]
where only Hasse incidences crossing the cut \(\mathcal R\,|\,\mathcal K\setminus\mathcal R\) contribute.

Internal incidence-current contributions cancel pairwise. Taking \(\mathcal R=\mathcal K\) recovers global support conservation.

On a glued tetrahedral complex, shared simplices occur once in the global chain carrier. Equal-top-star ownership
\[
w_{\sigma\tau}^{\rm eq}=\frac1{n_3(\sigma)}
\]
partitions each unique-simplex support exactly:
\[
\sum_{\tau\supset\sigma}w_{\sigma\tau}^{\rm eq}=1.
\]
Hence
\[
\sum_\tau S_{\mu,\tau}^{\rm eq}=S_\mu^{\rm global}.
\]

These gluing identities are exact finite bookkeeping statements.

## 4. Branch and receipt dynamics

### 4.1 Exact Hamming branch structure

On the basis \(\{|\theta\rangle:\theta\in\Theta\}\), define
\[
W_\Theta|\theta\rangle=w_H(\theta)|\theta\rangle.
\]

For \(w\in\{0,1,2,3\}\), define
\[
P_w^\Theta
=
\prod_{\substack{m=0\\m\neq w}}^3
\frac{W_\Theta-mI}{w-m}.
\]

Then
\[
P_w^\Theta P_{w'}^\Theta=\delta_{ww'}P_w^\Theta,
\qquad
\sum_wP_w^\Theta=I_\Theta,
\]
and
\[
\boxed{
\operatorname{rank}
(P_0^\Theta,P_1^\Theta,P_2^\Theta,P_3^\Theta)
=
(1,3,3,1).
}
\]

The induced \(S_4\) action permutes the three matching coordinates and preserves Hamming weight:
\[
[\rho_\Theta(g),W_\Theta]=0.
\]

The complement involution obeys
\[
\mathcal C W_\Theta\mathcal C^{-1}=3I-W_\Theta,
\]
so the weight-one and weight-two sectors are exactly paired. Shell multiplicity therefore does not select one over the other.

If an operator \(U_e^\Theta\) is supplied, branch preservation is exact iff
\[
\boxed{
[U_e^\Theta,W_\Theta]=0.
}
\]

### 4.2 Receipt-conditioned affine transport

For exposure endpoints
\[
x^-=(g^-,\theta^-),
\qquad
x^+=(g^+,\theta^+),
\]
define the relative-frame receipt
\[
r_e=g^+(g^-)^{-1}
\]
and the parity-transition receipt
\[
a_e=\theta^+\oplus P_{\pi(r_e)}\theta^-.
\]

The receipt-conditioned visible operator is
\[
\boxed{
U_e^{\Theta,\rm aff}
=
X(a_e)\Gamma_\Theta(\pi(r_e)).
}
\]

It is unitary. If
\[
r=w_H(a_e),
\]
then the branch-transition ranks satisfy
\[
\operatorname{rank}
\left(
P_{w'}^\Theta
U_e^{\Theta,\rm aff}
P_w^\Theta
\right)
=
\binom rs
\binom{3-r}{w-s},
\qquad
s=\frac{w+r-w'}2,
\]
for admissible integral \(s\), and vanish otherwise.

Moreover,
\[
\boxed{
\frac18
\|[U_e^{\Theta,\rm aff},W_\Theta]\|_F^2
=
w_H(a_e).
}
\]

Thus branch mixing can be nonzero while the receipt-conditioned transport remains unitary.

### 4.3 Exact relative-frame extraction

Let the ordered pre-event transport on the oriented edge carrier be
\[
\mathcal T_{1,n}^{\rm pre}.
\]

Since
\[
B_1B_1^T=4I_4-J_4,
\]
define
\[
\boxed{
\widehat P_{0,n}
=
\frac14
\left(
B_1\mathcal T_{1,n}^{\rm pre}B_1^T+J_4
\right).
}
\]

If \(\widehat P_{0,n}\) is exactly a four-vertex permutation matrix and
\[
\boxed{
B_1\mathcal T_{1,n}^{\rm pre}
=
\widehat P_{0,n}B_1,
}
\]
then there is a unique \(r_n\in S_4\) satisfying
\[
P_0(r_n)=\widehat P_{0,n}.
\]

Let \(P_1(r_n)\) be the induced signed edge action and define
\[
K_n=P_1(r_n)^{-1}\mathcal T_{1,n}^{\rm pre}.
\]
Then
\[
\boxed{
B_1K_n=B_1.
}
\]

Thus the residual transport is boundary silent. If \(\mathcal T_{1,n}^{\rm pre}\) is orthogonal, the residual fixes the cut space and acts only on the cycle space.

### 4.4 Receipt-index constitutive event operator

For receipt-complete events the constitutive frontier can be narrowed further.

Let
\[
\mathcal L_n^-
\]
be the finite viable pre-event obligation space and
\[
\mathcal L_n^+
\]
the finite viable output-obligation space constructed from target-hidden source receipts. For any pre-specified continuation map
\[
F_n:\mathcal L_n^-\to\mathcal L_n^+,
\]
finite rank-nullity gives
\[
\operatorname{ind}F_n
=
\dim\mathcal L_n^- - \dim\mathcal L_n^+.
\]

Hence the net Hamming budget is
\[
\boxed{
\mu_{\Theta,n}
=
\dim\mathcal L_n^- - \dim\mathcal L_n^+.
}
\]

The explicit predecessor/continuation map is therefore unnecessary for the **net** event budget once the two obligation spaces are independently constructed. It remains necessary for separate sink/addition counts and lineage provenance.

After exact frame alignment,
\[
k_n^+
=
w_H(\bar\theta_n^-)+\mu_{\Theta,n}.
\]
Carrier admissibility requires
\[
0\le k_n^+\le3.
\]

The integrity-constrained endpoint set is
\[
\mathcal A_{k_n^+}(T)
=
\left\{
\theta\in\Theta:
w_H(\theta)=k_n^+,\ 
(1-\theta_p)(1-T_p)=0
\right\}.
\]

Using only the pre-event quadratic burden histories,
\[
\Theta_{{\rm opt},n}
=
\operatorname*{arg\,min}_{\theta\in\mathcal A_{k_n^+}(T)}
\sum_p\theta_pW_{p,n}^{B2}.
\]

A singleton optimizer predicts \(\theta_n^+\) without endpoint access. Empty admissibility is a source inconsistency; an exact optimum tie returns hold.

Define
\[
c_{\Theta,n}
=
(1-\bar\theta_n^-)\odot\theta_n^+,
\qquad
o_{\Theta,n}
=
\bar\theta_n^-\odot(1-\theta_n^+),
\]
and
\[
a_n=c_{\Theta,n}\oplus o_{\Theta,n}.
\]

Then
\[
\boxed{
|c_{\Theta,n}|-|o_{\Theta,n}|
=
\mu_{\Theta,n},
}
\]
while
\[
\boxed{
|c_{\Theta,n}|+|o_{\Theta,n}|
=
w_H(a_n).
}
\]

Thus a source-complete receipt packet and unique burden optimum determine net polarity, net multiplicity, gross pair-toggle multiplicity, and directed addresses. The earlier signed-support sign law is retained only as an independent consistency diagnostic on this domain.

The remaining upstream gap is no longer the event operator itself. It is the native construction of the pre-event obligation spaces \(\mathcal L_n^\pm\) from more primitive packet dynamics.


### 4.5 Primitive-facing obligation-space candidate

The receipt-index event operator still requires a source construction for \(\mathcal L_n^\pm\). The current exact support/route structure narrows the possible constructor.

For each edge,
\[
\Lambda_e^S
=
2|c_{1,e}|
(|c_{0,i}|+|c_{0,j}|)
\]
is the pre-gate latent support activity. For each opposite-edge pair define
\[
\Lambda_p^{\rm pair}
=
\sum_{e\in M_p}\Lambda_e^S,
\]
and
\[
T_p^{\rm pair}
=
\prod_{e\in M_p}
T_{{\rm int},e}^{\rm hard}.
\]

Gated route flow cannot serve as the source because a closed pair has zero gated throughput even when its pre-gate latent activity is nonzero. A reopening-aware source must therefore precede the closure gate.

The minimal source-bound binary candidate is
\[
\boxed{
\omega_p^{\rm lat}
=
T_p^{\rm pair}
\mathbf1[
\Lambda_p^{\rm pair}>0
].
}
\]

This object is exactly \(S_4\)-covariant and uses no fitted tolerance.

The constitutive step is the POC-1 hypothesis:

> a viable latent pair-support lane is an obligation for that pair to be open at the next completed local event.

At a completed event boundary this gives the saturation receipt
\[
1-\theta_{\tau_\Theta}
=
\omega_{\tau_\Theta}^{\rm lat}.
\]

At the first subsequent exact change in \(\omega^{\rm lat}\), define
\[
\mathcal L^-=
\operatorname{span}\{e_p:\omega_{p,\tau_\Theta}^{\rm lat}=1\},
\]
and
\[
\mathcal L^+=
\operatorname{span}\{e_p:\omega_{p,n_\star}^{\rm lat}=1\}.
\]

Then
\[
\mu_\Theta
=
\dim\mathcal L^--\dim\mathcal L^+.
\]

The pair-addressed minimal-capacity endpoint is
\[
\boxed{
\theta_{\rm POC1}^+
=
\mathbf1-\omega_{n_\star}^{\rm lat}.
}
\]

Conditional on POC-1, the net and gross multiplicity identities of Sec. 4.4 follow exactly and the burden optimizer becomes an independent diagnostic rather than the address source.

The mathematical carrier does not prove the POC-1 interpretation: a lawful source/sink mechanism could extinguish or create obligations beyond instantaneous latent activity. POC-1 is therefore a preregistered constitutive candidate, not an exact primitive theorem. Its held-out falsifier is exact endpoint disagreement after previous-event saturation and source-authenticated pre-event acquisition.


## 5. Retriangulation and finite covariance constraints

### 5.1 Oriented Pachner pair

On vertices \(0,1,2,3,4\), define
\[
K_-=[0123]-[0124],
\]
and
\[
K_+=-[1234]+[0234]-[0134].
\]

Then
\[
\boxed{
K_--K_+=\partial[01234],
}
\]
so
\[
\boxed{
\partial K_-=\partial K_+.
}
\]

A separate exact no-go shows that no fixed binary vertex labeling makes all five participating tetrahedra simultaneously satisfy the declared \(2{:}2\) condition. Topological admissibility therefore does not imply fixed-label micro-admissibility.

### 5.2 Finite A/B/C relay

Use
\[
A=\{0123,0124\},
\]
\[
B=\{0123,0124,0134\},
\]
\[
C=\{0134,0234,1234\}.
\]

Their exact \(f\)-vectors are
\[
f(A)=(5,9,7,2),
\]
and
\[
f(B)=f(C)=(5,10,9,3).
\]

The involution
\[
p=(0\ 3)(1\ 4)
\]
with \(2\) fixed induces a signed-permutation simplicial isomorphism
\[
B\cong C.
\]

### 5.3 Exact spectra and no common recurrence

The global unique-simplex Hodge–Dirac spectra are
\[
\boxed{
\operatorname{Spec}(\mathcal A_A)
=
0^{(1)}
\cup
(\pm i\sqrt3)^{(4)}
\cup
(\pm i\sqrt5)^{(7)},
}
\]
and
\[
\boxed{
\operatorname{Spec}(\mathcal A_B)
=
\operatorname{Spec}(\mathcal A_C)
=
0^{(1)}
\cup
(\pm i\sqrt2)^{(2)}
\cup
(\pm i\sqrt5)^{(11)}.
}
\]

Equivalently,
\[
\chi_A(\lambda)
=
\lambda(\lambda^2+3)^4(\lambda^2+5)^7,
\]
\[
\chi_B(\lambda)
=
\chi_C(\lambda)
=
\lambda(\lambda^2+2)^2(\lambda^2+5)^{11}.
\]

Since
\[
\sqrt{\frac53}\notin\mathbb Q,
\qquad
\sqrt{\frac52}\notin\mathbb Q,
\]
there is no finite \(T>0\) satisfying
\[
e^{T\mathcal A}=I
\]
for the full flow on any of the current A/B/C complexes.

\[
\boxed{
\text{The current A/B/C relay admits no finite nonzero global Hodge–Dirac recurrence.}
}
\]

Thus the exact single-cell recurrence cannot be promoted to a universal clock on the glued carriers.

Detailed intertwiners, inclusion residuals, protected/vulnerable sector decomposition, and canonical internal action-transfer results are preserved in Supplement S4 and the source manuscript.

## 6. Projective Support Receipt

### 6.1 Ray nonidentifiability before PSR

The previously available event, route, lineage, Hasse-current, and total-support receipts do not identify one chain ray. In particular, the parity-degree rescaling
\[
G_\lambda(c_0,c_1,c_2,c_3)
=
(\lambda c_0,\lambda^{-1}c_1,\lambda c_2,\lambda^{-1}c_3),
\qquad
\lambda>0,
\]
leaves adjacent-degree bilinear Hasse currents invariant.

An additional exact witness preserves \(S_\mu\) while changing the ray. Therefore
\[
\boxed{
\{\text{event/route/lineage receipts}
+\text{all Hasse currents}+S_\mu\}
\not\Rightarrow[c].
}
\]

This is a scoped identifiability no-go.

### 6.2 Sufficient receipt and reconstruction theorem

For \(c\neq0\), define
\[
\rho_\sigma=\frac{c_\sigma^2}{S_\mu(c)}.
\]

On the Hasse graph restricted to nonzero-support simplices, choose a deterministic spanning forest \(F\). For each forest incidence record
\[
\chi_{\sigma\tau}
=
\operatorname{sgn}(c_\sigma c_\tau)
=
\operatorname{sgn}(B_{\sigma\tau}J_{\sigma\tau}),
\]
and record one coefficient sign \(\epsilon_C\) at a root of each connected support component.

Define
\[
\boxed{
\operatorname{PSR}(c)
=
\left(
\{\rho_\sigma\},
\{\chi_{\sigma\tau}\}_{F},
\{\epsilon_C\}
\right).
}
\]

Propagate signs through the forest and set
\[
\widehat c_\sigma=s_\sigma\sqrt{\rho_\sigma}.
\]

Then
\[
\boxed{
\mathcal R(\operatorname{PSR}(c))
=
\frac{c}{\sqrt{S_\mu(c)}}.
}
\]

Thus the PSR determines the positive projective chain ray while leaving absolute support normalization separate.

### 6.3 Pre-event acquisition algebra

At a frozen pre-event state, acquire
\[
q_\sigma=c_\sigma^2
\]
for each unique simplex and
\[
J_{\sigma\tau}=2B_{\sigma\tau}c_\sigma c_\tau
\]
on the forest incidences.

The exact consistency identity is
\[
\boxed{
J_{\sigma\tau}^2=4q_\sigma q_\tau.
}
\]

One common sign flip per connected support component remains invisible to stocks and bilinear currents. For a deterministic root \(r\), a matched calibrated probe gives
\[
q_r^+=(c_r+\alpha)^2,
\qquad
q_r^-=(c_r-\alpha)^2,
\]
so
\[
\boxed{
q_r^+-q_r^-=4\alpha c_r.
}
\]

The probe amplitude is a measurement control, not an internal coefficient.

### 6.4 Forest gauge and A/B/C event covariance

Let \(T\) denote the canonical A-to-B inclusion and \(P\) the signed B-to-C simplicial permutation. At the event map,
\[
T^TT=I_A,
\qquad
P^TP=I_B,
\qquad
\mathcal A_CP=P\mathcal A_B.
\]

The PSR reconstruction commutes with these event maps:
\[
\boxed{
\mathcal R_B(\operatorname{PSR}(Tc_A))
=
T\mathcal R_A(\operatorname{PSR}(c_A)),
}
\]
and
\[
\boxed{
\mathcal R_C(\operatorname{PSR}(Pc_B))
=
P\mathcal R_B(\operatorname{PSR}(c_B)).
}
\]

A mapped forest and a freshly recomputed canonical forest may use different incidence edges yet reconstruct the same ray. Forest choice is therefore a receipt-serialization gauge rather than a new state variable.

These are event-level statements. They do not erase the known dynamical residual of the dimension-changing A-to-B move.

### 6.5 Authentication and interval uncertainty

Receipt consistency does not establish source authenticity:
\[
\boxed{
\text{PSR schema integrity}
\not\Rightarrow
\text{identity with a separately intended external state}.
}
\]

A measurement-facing receipt therefore separates source authentication from mathematical feasibility. Cryptographic authentication establishes packet integrity and trusted-key possession; it does not establish physical truth.

For strictly positive measured support intervals, write
\[
x_\sigma=\ln q_\sigma.
\]
The exact current law gives the interval constraint
\[
2\ln\!\left(\frac{J_{\sigma\tau}^{\min}}2\right)
\le
x_\sigma+x_\tau
\le
2\ln\!\left(\frac{J_{\sigma\tau}^{\max}}2\right).
\]

Together with the logged support intervals, magnitude compatibility becomes a linear feasibility problem in the transformed measured fields. If a required support or sign interval crosses zero, the result is indeterminate rather than repaired by a fitted tolerance.

## 7. Faithful observable realization and held-out test

### 7.1 Intrinsic held-out design

The fully supported filled tetrahedron has 15 simplex coordinates and exactly 28 Hasse incidences:
\[
12_{C_0\leftrightarrow C_1}
+
12_{C_1\leftrightarrow C_2}
+
4_{C_2\leftrightarrow C_3}
=
28.
\]

A spanning tree on the 15 supported simplex vertices contains
\[
15-1=14
\]
incidences. The remaining 14 incidences are not required for reconstruction. Hence
\[
\boxed{
28
=
14_{\rm reconstruction}
+
14_{\rm heldout}.
}
\]

The training PSR defines a frozen feasible set \(\mathcal F_{\rm PSR}\). For each held-out Hasse incidence,
\[
\boxed{
I_{\sigma\tau}^{\rm pred}
=
\operatorname{range}_{c\in\mathcal F_{\rm PSR}}
\left(
2B_{\sigma\tau}c_\sigma c_\tau
\right).
}
\]

Held-out data are released only after these predictions are frozen. The held-out channels may not repair the reconstruction receipt.

### 7.2 Coherent photonic representation

A coherent multi-mode interferometer provides a faithful representation of the PSR observables. Assign one optical mode to each simplex coordinate and define
\[
P_{\rm science}=\sum_\tau |E_\tau|^2.
\]

Then
\[
\boxed{
\rho_\sigma
=
\frac{|E_\sigma|^2}{P_{\rm science}}.
}
\]

For one Hasse-adjacent pair, a calibrated 50:50 analyzer yields
\[
P_+
=
\frac{|E_\sigma+E_\tau|^2}{2},
\qquad
P_-
=
\frac{|E_\sigma-E_\tau|^2}{2},
\]
and therefore
\[
P_+-P_-
=
2\operatorname{Re}(E_\sigma^\ast E_\tau).
\]

On the admitted common real quadrature,
\[
\boxed{
J_{\sigma\tau}^{\rm opt}
=
B_{\sigma\tau}
\frac{P_+-P_-}{P_{\rm science}}
=
2B_{\sigma\tau}\widehat c_\sigma\widehat c_\tau.
}
\]

A phase-locked auxiliary provides the matched root-sign probe.

Under the publication correspondence scale adopted here, this optical map is **CRL-1: faithful representation**. It establishes an explicit observable algebra map; it does not identify the optical processor as the physical UD substrate.

### 7.3 Experimental status

A public-corpus admissibility audit was performed against the frozen POC-1 source fields. The strongest surveyed external datasets included a physical \(K_4\) quantum-walk experiment, raw voltage/current switching datasets, experimental simplicial-oscillator time series, photonic processor reproducibility packages, and repeated-syndrome QEC corpora. None simultaneously exposes the native four vertex-chain channels, six independent edge-chain channels, hard edge-integrity receipts, prior three-pair \(\Theta\) state, ordered pre-event history, and a separately hidden next \(\Theta\) endpoint.

Accordingly,

\[
\boxed{
\text{no currently surveyed public corpus is source-complete for a native POC-1 score}.
}
\]

No empirical POC-1 verdict is reported. Constructing a new proxy map after corpus selection is prohibited. The next admissible empirical route is a purpose-built independent acquisition or a future public corpus whose correspondence map is frozen before target exposure.

A 20-mode implementation has been preregistered with
\[
1\text{--}15=\text{science},
\qquad
16=\text{reference},
\qquad
17=\text{root auxiliary},
\qquad
18\text{--}20=\text{calibration/guard}.
\]

The deterministic 14 reconstruction and 14 held-out incidences are frozen. Device/laboratory qualification, authenticated calibration intake, and zero-touch held-out release tooling are maintained as supplementary reproducibility artifacts.

No real held-out optical result exists at this manuscript state. Thus:

\[
\boxed{
\text{CRL-1 mathematical representation: specified},
}
\]
\[
\boxed{
\text{CRL-2 operational same-observable test: pending},
}
\]
\[
\boxed{
\text{CRL-3 constitutive physical-carrier identification: open}.
}
\]

## 8. Discussion

### 8.1 Novelty relative to standard machinery

The paper does not claim novelty for the existence of simplicial boundary operators, Hodge/Dirac-style finite generators, controlled-unitary constructions, or Kraus dilation identities. The intended new contribution is the specific finite tetrahedral packet architecture and the receipt structure derived on it.

The strongest distinct results are the PSR identifiability no-go, sufficient projective reconstruction theorem, forest-gauge result, event covariance through the current A/B/C relay, authenticated interval-feasibility construction, and the intrinsic \(28=14+14\) held-out design. The source-complete relative-frame extractor and the finite retriangulation spectral constraints are additional framework-specific results.

### 8.2 What is not claimed

Nothing in this paper identifies
\[
S_\mu
\]
with physical energy,
\[
\mathcal A
\]
with a quantum Hamiltonian,
the finite tetrahedral carrier with physical spacetime,
the \(\Theta\) fiber with a Standard Model gauge or matter degree of freedom,
or any internal finite ratio with a measured physical coupling.

The optical representation is a test of the receipt/observable algebra in a calibrated medium. Even a successful held-out optical test would establish operational implementability of the mapped observables in that device, not a constitutive theory of nature.

### 8.3 Highest open problem

The highest upstream gap is constitutive event selection.

The framework currently contains exact transport structure, exact receipt reconstruction once source data exist, and a falsifiable observable layer. It does not yet derive from the closed finite carrier alone a unique source law that decides the general event polarity and multiplicity.

This gap is upstream of most proposed physical interpretations. Progress on the constitutive source law therefore has greater explanatory value than adding additional analog hardware platforms or numerical correspondences.

## 9. Conclusion

The finite tetrahedral carrier supports a replayable chain complex, exact skew Hodge–Dirac support transport, finite branch structure, retriangulation constraints, and an exact projective receipt for the chain ray. The PSR identifies precisely which support and sign information is sufficient, proves which earlier receipt summaries are insufficient, and yields an intrinsic held-out test on the same observable algebra.

These results define a finite mathematical and experimental-methods program. They do not yet constitute a physical theory of spacetime, matter, gauge fields, or measured constants. The next scientific step is therefore twofold but ordered: execute the already-preregistered observable realization, and independently advance the constitutive event-source law that determines which receipt is produced.

# Appendix A. Explicit tetrahedral boundary matrices

In the ordered bases
\[
(01,02,03,12,13,23),
\qquad
(012,013,023,123),
\]
the canonical matrices are
\[
B_1=
\begin{pmatrix}
-1&-1&-1&0&0&0\\
1&0&0&-1&-1&0\\
0&1&0&1&0&-1\\
0&0&1&0&1&1
\end{pmatrix},
\]
\[
B_2=
\begin{pmatrix}
1&1&0&0\\
-1&0&1&0\\
0&-1&-1&0\\
1&0&0&1\\
0&1&0&-1\\
0&0&1&1
\end{pmatrix},
\]
and
\[
B_3=
\begin{pmatrix}
-1\\
1\\
-1\\
1
\end{pmatrix}.
\]

Direct multiplication gives
\[
B_1B_2=0,
\qquad
B_2B_3=0.
\]

# Appendix B. Retriangulation spectra and preserved relay details

The exact characteristic polynomials used in Section 5 are
\[
\chi_A(\lambda)
=
\lambda(\lambda^2+3)^4(\lambda^2+5)^7,
\]
\[
\chi_B(\lambda)
=
\chi_C(\lambda)
=
\lambda(\lambda^2+2)^2(\lambda^2+5)^{11}.
\]

The full source manuscript additionally derives:
- the exact B/C signed-permutation chain isomorphism;
- the dimension-changing A-to-B inclusion residual;
- protected and vulnerable spectral subspaces;
- exact action-budget transfer through the current relay;
- the lifted loop-history action functional;
- the no-go for one universal scalar conversion from endpoint loop defect to accumulated action.

Those statements are preserved unchanged in Supplement S4 and in the full v1.9 source manuscript. They are not required for the central PSR theorem chain.

# Appendix C. PSR proof and uncertainty details

For positive support on one forest edge \((\sigma,\tau)\),
\[
J_{\sigma\tau}^2=4q_\sigma q_\tau.
\]
A resolved relative sign and one root sign per support component determine every coefficient sign on the forest. The normalized coefficient magnitudes are \(\sqrt{\rho_\sigma}\), so reconstruction follows by sign propagation.

With certified current interval
\[
0<J_{\min}\le |J_{\sigma\tau}|\le J_{\max},
\]
and \(x_\sigma=\ln q_\sigma\),
\[
2\ln(J_{\min}/2)
\le
x_\sigma+x_\tau
\le
2\ln(J_{\max}/2).
\]
Together with the logged stock intervals, the magnitude feasibility problem is linear. Root-probe constraints remain exact quadratic preimages. Zero-crossing support or sign intervals are reported as indeterminate.

The complete derivations, authenticated receipt schema, robustness cases, and experimental custody protocol are retained in the supplementary research package.

---

## Publication claim boundary

This v2.0 manuscript is an editorial refactor of the governed v1.9 scientific source. No theorem, no-go, claim status, ledger value, or provenance ruling is changed by this refactor.
