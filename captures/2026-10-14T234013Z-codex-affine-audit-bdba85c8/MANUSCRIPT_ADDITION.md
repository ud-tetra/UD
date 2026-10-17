## D.14 Composition of controls and the limits of phase extensions

### D.14.1 Primitive controls generate an affine action group

The 24 primitive controls of D.13.1 are not closed under composition. Their closure is

\[
G_{\rm aff}=\mathbb F_2^3\rtimes S_3,\qquad
(v,g)(u,h)=(v\oplus P_g u,gh),\qquad |G_{\rm aff}|=48.
\]

Indeed, the primitive set contains all coordinate permutations and each single-bit translation. Composing the latter generates every translation in $\mathbb F_2^3$; conversely, affine composition never leaves the displayed set. Its action on the eight configurations is faithful: evaluation at zero recovers $v$, and evaluation at the three unit vectors recovers $P_g$. This identifies a consequence of repeated controls in the declared graph, not a new native admission or rate law [26].

There is also an explicit abstract isomorphism $G_{\rm aff}\cong C_2\times S_4$. Center the Boolean cube: an affine action becomes a signed permutation matrix $M=\operatorname{diag}((-1)^{v_j})P_g$. Its determinant sign gives $\delta\in C_2$, and its permutation of the four opposite-vertex pairs gives $\sigma\in S_4$. A signed permutation fixing all four pairs is $\pm I$. To see this, the four diagonal lines are in general position: three span the space and the fourth has all three coordinates nonzero in that basis, forcing a common eigenvalue. The determinant distinguishes $I$ and $-I$. Hence $(\delta,\sigma)$ is injective and, since both groups have 48 elements, bijective.

An endpoint transformation does not identify the intervening word. In particular, twice applying a single flip acts as the identity while using two primitive steps. Neither the 48-element closure nor a receipt of the final transformation determines a history cost or the graph-cycle counter of D.13.4. Thus the state-action group, event word and retained history functional remain separate objects.

### D.14.2 A finite phase label does not establish physical winding

Appending a central $C_{13}$ factor produces a mathematically admissible group of order 624 with quotient $S_3$ after removing $\mathbb F_2^3\times C_{13}$. This does not identify its 104-element kernel with the four-element Klein kernel of $S_4\to S_3$. No native connection, parallel transport or integer winding follows from the appended label. A $C_{13}$ character can distinguish a declared counter only modulo 13; an unbounded integer counter still requires a lift and its acquisition contract.

Nor does the affine group force projective phases to be trivial. With the preceding coordinates let $p(g)$ be the parity of $\sigma(g)$. For the Pauli matrices $X,Z$, define

\[
R(g)=X^{\delta(g)}Z^{p(g)},\qquad
R(g)R(h)=\alpha(g,h)R(gh),\qquad
\alpha(g,h)=(-1)^{p(g)\delta(h)}.
\]

The additive characters $p,\delta$ make $\alpha$ a normalized two-cocycle. Choose a central element with $(\delta,\sigma)=(1,1)$ and an element with $\delta=0$ and odd $\sigma$. They commute in the group, but their lifts $X,Z$ anticommute. Rephasing either lift cannot change this commutator, so the projective class is nontrivial. Letting $C_{13}$ act trivially preserves this counterexample for the extended group. This disproves the imported assertion that all projective classes vanish; it does not assert a physical anomaly. A physical gauge-anomaly calculation requires a specified physical action and field content, neither supplied here. The exact replay checks the affine isomorphism, all $48^3$ cocycle triples and this witness [26].

