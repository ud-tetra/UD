# Averaging and signed-current memory audit v0.1

Development — no registry entry. Exact conditional identities and constructor replay. Independent review pending. Physical promotion 0. No numerical target evaluated.

## Frozen source and declared rules

Input: the prior response capture's 15D real skew Hodge–Dirac A, with A^2=-4(I-H0), and its explicit candidate seven paired-stock sensors. The body stock is retained as an eighth group where mass accounting is needed. Group sizes are (2,2,2,2,2,2,2,1). These observation groups are not an identification of physical channels or thermodynamic variables.

Update index n remains primitive. Introduce an independently declared uniform internal step h, theta=2h, c=cos theta and s=sin theta. The exact internal propagator is

\[
U=H0+c(I-H0)+\frac{s}{2}A.
\]

No h or physical clock is selected by matching a target. The rational pair c=3/5,s=4/5 is a frozen algebraic test fixture, not a native empirical coefficient.

Three rules are compared:

- A: erase off-diagonal moment entries after every propagation, starting from a diagonal moment.
- B: additionally redistribute each paired group's diagonal stock equally between its two simplices after every propagation.
- M: keep native propagation unchanged and predict sampled outputs from a finite compatible history.

A and B are explicitly added averaging operations. They are not consequences of the skew native flow or silently admitted physical mechanisms.

## A1 — Coordinate averaging closes a 15-stock process, not native repeated propagation

For diagonal M0=diag(p0), define Delta(M)=diag(diag M). Then the declared process

\[
M_{n+1}=\Delta(UM_nU^T)
\]

has

\[
p_{n+1}=Bp_n,\quad B_{ij}=U_{ij}^2.
\]

B is nonnegative and doubly stochastic by orthogonality of U. For this source, it is also symmetric: the support of H0+c(I-H0) is disjoint from the entrywise support of A, so squaring entries removes the antisymmetric signs. Delta is an exact average over all independent coordinate-sign conjugations; it is positive and trace preserving.

This agrees with one native step from a diagonal moment. Native propagation regenerates correlations, however; applying Delta discards them. At the fixture and initial vertex v0, native and averaged second-step stocks differ by L1 distance 1197/1250. This is an exact failure control, not a measurement or numerical tolerance.

Thus the averaging rule passes as its declared stochastic process and fails as an exact replacement for repeated coherent dynamics.

## A2 — Dephasing does not make the paired stocks strongly lumpable

Let C8 aggregate each of the seven pairs and the body. A closed grouped Markov law for every micro-allocation would require equal columns of C8 B within every group.

At the fixture, a unit stock on vertex v0 and a unit stock on its opposite face have identical grouped input. Their grouped outputs are respectively

\[
(49/100,1/100,1/100,1/100,4/25,4/25,4/25,0),
\]

\[
(9/25,0,0,0,4/25,4/25,4/25,4/25).
\]

They differ. Therefore coordinate correlation erasure alone fails strong lumpability even after the body is included. The source location inside the paired group matters.

## A3 — Equal redistribution supplies a closed eight-stock response

Define L8 to split each paired stock equally between its two coordinates and retain the single body stock. C8 L8=I8. Rule B applies

\[
M_{n+1}=\operatorname{diag}\!\left[L8 C8\operatorname{diag}(UM_nU^T)\right],
\]

starting with M0=diag(L8 g0). Then

\[
\boxed{g_{n+1}=K8 g_n,\qquad K8=C8 B L8.}
\]

This is exact under Rule B. It does not show that the native system performs equal redistribution.

For all c in [-1,1], set u=1-c^2, a=(1+3c)/4 and b=(1-c)/4. The coefficients are

- VF diagonal: (a^2+c^2)/2; other VF entries: b^2/2.
- VF/EE entries in both directions: u/4.
- Body to each VF: u/4; each VF to body: u/8.
- EE and body diagonal: c^2; all other entries zero.

Every column sums to one. The stationary probabilities are pi=(2,2,2,2,2,2,2,1)/15, and K_ij pi_j=K_ji pi_i. The mass-form K8 is therefore not generally symmetric in the unweighted coordinate metric; detailed balance uses the group cardinalities.

Its full spectrum is

\[
1,\quad
\left[\frac{c(1+3c)}4\right]^{[3]},\quad
(c^2)^{[3]},\quad
\frac{15c^2-7}{8}.
\]

**Proof:** the VF contrast subspace gives the first factor (dimension 3). The EE contrasts give two copies of c^2, and the scalar EE/body contrast gives its third copy. The remaining scalar mass block on (VF total, EE total, body) is

\[
\begin{pmatrix}
1-7u/8&u&u\\
3u/4&1-u&0\\
u/8&0&1-u
\end{pmatrix},
\]

with eigenvalues 1,c^2,(15c^2-7)/8. These spaces span all eight coordinates. QED.

At the fixture the nonconstant response factors are 21/50, 9/25 and -1/5. They are derived from the frozen fixture and declared operations, not selected native constants. Negative response factors describe alternating modes in a positive transition process, not negative stock.

For normalized g, the weighted quadratic discrepancy Phi(g)=sum_i (g_i-pi_i)^2/pi_i contracts by at most rho(c)^2 per step, where rho is the maximum absolute nonconstant factor. At the fixture rho^2=441/2500. This is a mathematical ensemble-discrepancy bound, not physical heat, energy, entropy production or a calibrated thermodynamic step-down.

Uniform nonconstant response would require c(1+3c)/4=c^2=(15c^2-7)/8. The first equality forces c=0 or c=1; c=0 fails the second, while c=1 gives identity. Thus Rule B has no nontrivial uniform active screen. This scoped result does not prohibit a different source-defined averaging law.

## M1 — Exact five-sample native memory

Keep the native flow unchanged. Every quadratic observable y(s)=tr(C M(s)) lies in the span of constant, cos(2s), sin(2s), cos(4s), sin(4s). This follows from the generator spectrum {0,+2i,-2i} and moment-frequency sums/differences.

For a uniform sampled step h, the shift E therefore satisfies

\[
\boxed{(E-1)(E^2-2cE+1)(E^2-2dE+1)y_n=0,\quad d=2c^2-1.}
\]

This gives an exact order-five recurrence for every paired stock, body stock and each of the 28 individual signed Hasse currents. It requires compatible native history, unchanged generator and uniform declared h. It remains valid at aliasing steps but need not be minimal there.

At c=3/5,d=-7/25,

\[
y_{n+5}=\frac{41}{25}y_{n+4}-\frac{246}{125}y_{n+3}
+\frac{246}{125}y_{n+2}-\frac{41}{25}y_{n+1}+y_n.
\]

Replay verifies this as an observable-operator identity, so it holds for all initial PSD native moments rather than only the test trajectories. It predicts future sampled outputs without erasing the native correlations. It does not reconstruct the complete chain ray, license arbitrary histories, or establish positivity for fabricated histories.

## M2 — Four samples suffice for aggregate signed response; individual circulations differ

The sampled aggregate response z_n=(D J(M(nh))) is the internal derivative of each stock observable. Differentiation removes the constant-frequency component, leaving

\[
(E^2-2cE+1)(E^2-2dE+1)z_n=0.
\]

At the fixture,

\[
z_{n+4}=\frac{16}{25}z_{n+3}-\frac{166}{125}z_{n+2}
+\frac{16}{25}z_{n+1}-z_n.
\]

This four-sample rule applies to stock-current divergences, including the body balance. It is not a blanket reduction of all individual current histories: all 28 individual current observables can possess stationary circulation components. Their native five-sample operator rule was checked separately.

## M3 — Memory size and failure controls

At the fixture, one VF stock observable has exact scalar Krylov rank 5; its derivative has rank 4. Thus their scalar recurrences cannot be shortened there while retaining validity for all native moments.

For the seven stock observables, the sampled observable-span ranks after one through five steps are 7,14,21,24,27. The five-step span is closed by M1. Including body stock gives dimension 28. These are dimensions of linear output-observable realizations on native moments, not the chain dimension of another tetrahedral complex or a PSR code count. They do not assert a minimal nonlinear/rank-one state representation.

Changing the fifth propagation step to a different sampled angle violates the frozen recurrence and is rejected by the exact failure control. Source changes, nonuniform sampling, injections, averaging or new event operators require a new response contract or retained source forcing. Physical seconds remain open.

## Disposition

| Rule | Declared-process closure | Preserves native coherent response |
|---|---|---|
| Coordinate correlation erasure | Yes on 15 simplex stocks; fails eight-group lumpability | No across repeated steps |
| Erasure plus equal pair redistribution | Yes on eight grouped stocks | No; additional stochastic operation |
| Compatible sampled native memory | Exact sampled outputs; five-sample stock/current histories or four aggregate-response histories | Yes for unchanged generator and sampling |

For the stated goal of predicting the signed native response, Rule M is the supported development route. Rule B is a conditional averaging model with explicit source-derived relative coefficients, while its physical averaging mechanism and sampling step are unadmitted.

Next: construct a packet that certifies native history, generator identity, internal sampling, body balance and recurrence residuals, then test reset/source-change cases. No numerical target is evaluated or fitted by this audit.

Gap2_FINAL_Finite_Genesis.png remains unavailable and was not read or used.
