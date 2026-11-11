## D.15 A carrier-driven admission candidate with finite activity

### D.15.1 Declare the response rule rather than infer it from a stock identity

Keep a single filled tetrahedron, the signed $S_4$ action and the constant generator $A(a,b,c)$ of §5.1. Write its real state as $x(s)$, with $\|x\|=R>0$. For each opposite-edge pair $p$, let $D_p$ project onto its two edge coordinates and define

\[
q_p=x^TD_px,\qquad 0\le q_p\le R^2.
\]

These are squared carrier amplitudes, not physical energies. Introduce three response-memory bits $\vartheta_p$ and two supplied common thresholds $0<\ell<h<R^2$. The candidate rule sets $\vartheta_p:0\to1$ on reaching $q_p\ge h$, and $\vartheta_p:1\to0$ on reaching $q_p\le\ell$. Between the thresholds it retains its previous value. Start with a supplied consistent memory: a zero bit has $q_p<h$ and a one bit has $q_p>\ell$. At each first guard hit update every enabled bit in one batch. Leave $x$ unchanged and continue the same $A$.

This is a deterministic passive hybrid readout once its initial state and thresholds are supplied [27]. The common thresholds make it covariant under fixed vertex relabeling, since signed permutations transport $D_p$ to the corresponding pair projector and commute with $A$. All integrity gates are held open; forced resets, changing gates or feedback to $A$ are outside this contract. The response memory may be used as a candidate binary label, but no identification with native closure, obligation saturation or geometric replacement is derived. Hysteresis and dwell-time analysis are established control methods [28]; the following constants and collision example concern this particular carrier.

### D.15.2 Exact stock-speed and event-count bounds

For any orthogonal projector $D$ and skew $A$, set $B=DA(I-D)$ and $\beta_D=\|B\|$. Direct differentiation gives

\[
q'=x^T(DA-AD)x
=2(Dx)^TA(I-D)x,
\qquad
|q'|\le2\beta_D\sqrt{q(R^2-q)}\le\beta_D R^2.
\]

The commutator $DA-AD$ is symmetric and, in $D\oplus(I-D)$ blocks, has off-diagonal blocks $B,B^T$; its norm is $\beta_D$. For an opposite-edge pair of the tetrahedron, the two nonzero rows of $B$ have Gram matrix

\[
BB^T\big|_{\operatorname{im}D_p}=2(a^2+b^2)I_2,
\qquad \beta=\sqrt{2(a^2+b^2)}.
\]

Each edge has two vertex and two face incidences; opposite edges have disjoint vertex and face supports. This proves the identity and explains why the cell/face coefficient $c$ does not enter the direct bound. If $a=b=0$, the pair stocks are constant and no subsequent switches occur from a consistent initialization.

For $\beta>0$, consecutive switches of any one address are separated by at least

\[
d_* =\frac{\arcsin\sqrt{h/R^2}-\arcsin\sqrt{\ell/R^2}}{\beta}
\ \ge\ \frac{h-\ell}{\beta R^2}>0.
\]

To prove this, a switch back requires traversal of the threshold band. On that band, differentiating $\arcsin\sqrt{q/R^2}$ bounds its absolute speed by $\beta$. Integrating along the traversal proves the first inequality, and $2\sqrt{q(R^2-q)}\le R^2$ proves the second. Nonmonotone motion cannot shorten this required traversal. For the canonical generator, $\beta=2$, the angular bound is attainable: if $e$ is a unit coordinate vector on one edge in the pair, the invariant plane spanned by $e,Ae/2$ has a unit-norm trajectory with $q_p=\sin^2(2s)$. Its increasing crossing time between the two levels equals $d_*$.

Consequently, in an interval of length $S$, the total number of individual toggles is bounded by

\[
N_{\rm toggle}(S)\le3\left(1+\left\lfloor S/d_*\right\rfloor\right).
\]

The batch count is no larger. Thus no finite interval contains infinitely many switches. This is a per-address dwell bound and a finite-activity result, not a uniform positive separation between all distinct event times. Different addresses can cross arbitrarily close together.

### D.15.3 Bounded observation error and crossing-time sensitivity

If the observed stocks satisfy $|\widehat q_p-q_p|\le\varepsilon<(h-\ell)/2$, consecutive switches of an address require the true stock to move between at least $h-\varepsilon$ and $\ell+\varepsilon$. Replace $d_*$ above by

\[
d_{*,\varepsilon}=
\frac{\arcsin\sqrt{(h-\varepsilon)/R^2}
-\arcsin\sqrt{(\ell+\varepsilon)/R^2}}{\beta}
\ \ge\ \frac{h-\ell-2\varepsilon}{\beta R^2}>0.
\]

The event-count bound follows with this replacement. The strict half-gap condition is necessary for a uniform count bound based only on this error amplitude and carrier constants. For the canonical flow choose orthonormal opposite-edge vectors $e_1,e_2$ in the same pair and put $w_i=Ae_i/2$. The unit trajectory

\[
x(s)=\frac{\cos(2s)e_1+\sin(2s)w_1+\sin(2s)e_2-\cos(2s)w_2}{\sqrt2}
\]

has constant $q_p=1/2$. With $\ell=3/8$, $h=5/8$ and smooth measured stock $\widehat q_p=1/2+\sin(Ms)/8$, the error is exactly half the gap and the controller switches at successive maxima and minima. Arbitrarily large $M$ gives arbitrarily many toggles on a fixed interval while the true stock remains constant. This refutes a uniform amplitude-only count bound at the boundary; it does not assert infinite activity for any one fixed smooth noise signal.

For a well-defined continuous measured guard signal the first-hit rule applies directly; at supplied sample times the same count bound holds, but sampling delay needs a separate bound. If $\widehat x=x+e$, $\|e\|\le\delta$, then

\[
|\widehat x^TD_p\widehat x-x^TD_px|
\le2R\delta+\delta^2.
\]

Hence $\delta<\sqrt{R^2+(h-\ell)/2}-R$ is sufficient for a positive noise-adjusted gap. This is a declared norm-error contract, not an inferred apparatus noise law.

Event timing needs more than a gap. Suppose a matched ideal rising crossing $s_*$ is isolated, the previous response state agrees, no earlier noisy guard hit is possible, and $q'_p\ge\nu>0$ throughout the local band $[h-\varepsilon,h+\varepsilon]$. Continuity of the measured signal then gives

\[
|\widehat s_*-s_*|\le\varepsilon/\nu.
\]

Indeed the measured first hit lies between the true crossings of $h-\varepsilon$ and $h+\varepsilon$, each at most $\varepsilon/\nu$ from $s_*$. Descending crossings have the corresponding $-q'_p$ bound. Without isolation and a lower slope, small errors can create, erase or reorder crossings; no such timing guarantee is claimed at grazing or simultaneous events.

### D.15.4 Symmetric collisions obstruct a universal one-pair selector

For the canonical generator, start from the unit vertex state $x(0)=e_0$ and $\vartheta=000$. All three pair stocks are

\[
q_p(s)=\tfrac14\sin^2(2s).
\]

Choose, solely as an exact test fixture, $\ell=1/16$ and $h=3/16$. All three bits turn on at $s=\pi/6$ and off at $s=5\pi/12$, with crossing slopes $\pm\sqrt3/4$. The stabilizer of vertex 0 is $S_3$ and permutes the three pair addresses transitively while fixing the complete carrier trajectory and initial response. A deterministic equivariant rule required to select exactly one of these enabled addresses would have to return an address fixed by that stabilizer. None exists. It can hold or select the invariant batch; a one-address choice requires an additional reference/asymmetric state or a stochastic rule. Symmetry requires equal probabilities among the three if that is the only available information, but does not source randomness or its clock.

The batch $000\to111$ is not a primitive edge of D.13's no-flip/one-flip graph. Its endpoint transformation belongs to the 48-element closure in D.14. Serializing it into three one-flip events creates six possible orders; if a realized order matters, recovering it requires six values, hence three worst-case fixed-length bits conditional on the known batch. These are information requirements, not a derived physical work cost or three physical elapsed ticks.

There is also no uniform global dwell bound even away from exact collision. For $x(0)=(e_0+\eta e_1)/\sqrt{1+\eta^2}$ with small $\eta>0$,

\[
q_A=\frac{(1-\eta)^2}{4(1+\eta^2)}\sin^2(2s),\qquad
q_B=q_C=\tfrac14\sin^2(2s).
\]

The A onset occurs just after the B/C onset, with a separation tending to zero as $\eta\to0$. Per-address dwell and finite activity remain valid. Constructor checks cover the exact carrier, all signed symmetries, stock identities, transverse fixture and collision stabilizer [27].

The result supplies a testable candidate readout rule with explicit assumptions and proves its event and noise limits. Its thresholds, memory preparation, continuous observation, collision semantics and implementation resources remain supplied. It does not select native events from the carrier alone, alter the reconciled obligation/flux audit, or close G05/G06, physical winding, apparatus renewal or entropy-area normalization.
