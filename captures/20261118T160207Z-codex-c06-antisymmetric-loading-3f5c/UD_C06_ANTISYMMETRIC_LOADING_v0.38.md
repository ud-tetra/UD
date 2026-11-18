# C06 antisymmetric archive loading v0.38

**EXACT / NO-GO** for the shared vertex channel and copy-symmetric updates below. **CANDIDATE** for a separate oriented reciprocal transfer. **OPEN** for a native event that implements it. **Physical Promotion = 0.**

## Source scope

C06 v0.37 defines the stationary pair of equal signed-gradient registers coupled to a common vertex block. C06 v0.36 identifies the equivariant isometry \(L:W=T_2\to C=\operatorname{im}B_1^\mathsf T\) and the half-stock readback. C06 v0.34 supplies a conditional sum/difference concentration of an aligned held pair. Ledger v0.39 Q165–Q169 and the C06 v0.37 gate audit supply skew incidence and fixed masks. They supply no signed transfer between independently addressable gradient copies. The conditional finite even swap in C06 v0.6 and v0.35 supplies a stock-preserving comparator on its own matching channel, which annihilates \(W\).

## Fixed shared-channel and event obstruction

Use \(q\in V_0=\mathbf1_4^\perp\) and \(h_1,h_2\in C\), with their direct-sum Euclidean norm. Let \(B=B_1\). The shared channel evolves by
\[
\dot q=-B h_1-B h_2,\qquad \dot h_1=\dot h_2=B^\mathsf T q .
\]
The antisymmetric orbit coordinate \(d=(h_1-h_2)/\sqrt2\) is constant. The same argument holds under arbitrary common time-dependent controls, provided the two maps into that vertex block and their adjoints remain identical and the chosen gradient receiver is retained. More generally, a linear event map commuting with the involution that swaps the gradient copies and fixes the donor, vertex and other starting blocks cannot create an antisymmetric component from that symmetric starting state. This includes the bare copy swap as an update from an empty pair. For \((h,0)\) the fixed shared flow instead starts with \(\|h\|^2/2\) already in \(d\); it cannot increase that stock.

Declaring an incidence gate or recording a receipt does not itself introduce an oppositely signed input into the two copies. The above obstruction concerns common controls or commuting linear events. Unequal copy couplings and an independently oriented transfer have different premises.

## Exact candidate transfer with the shared block live

Let the positive odd stock be held in \((a,a)\in W^2\). In sum/difference coordinates the available concentration is \(s=\sqrt2a\), with zero difference and \(N=\|s\|^2\). Define \(J:W\to C^2\) by \(Js=(Ls,-Ls)/\sqrt2\). It is an isometry satisfying \([B\ B]J=0\). For \(y=(h_1,h_2)\), leave the shared vertex channel active and add the declared reciprocal loader
\[
\dot s=-g(t)J^\mathsf T y,\qquad
\dot y=(B^\mathsf Tq,B^\mathsf Tq)+g(t)Js .
\]
Keep the \(\dot q\) law above. Both operators are skew and the loader commutes with the shared generator because its range and access lie in the shared kernel. Thus the vertex and symmetric-copy dynamics are unchanged even for nonzero initial symmetric or vertex amplitudes. A separate even matching block remains unchanged by this direct-sum construction.

If the antisymmetric archive is initially empty, then at accumulated internal angle \(\theta=\int g(t)\,dt\) the donor is \(s_0\cos\theta\), the antisymmetric contribution is \(Js_0\sin\theta\), and total counted stock is invariant. At a first quarter turn followed by removal of the added coupling, the archive holds \((La,-La)\), with squared norm \(N\). Its calibrated direct odd readback is \(N/2=\|a\|^2\); the even Stage 2 observable continues to use its original matching record. The equivalent discrete candidate is the corresponding orthogonal rotation on the donor and the image of \(J\). For a missed angle \(\theta\), donor residue is exactly \(N\cos^2\theta\). With the loader left active, the archive can exchange stock back. The shared block remains live before, during and after loading.

This is a tested transfer law for the declared coordinates. A native mechanism must supply copy identity, the relative sign, the added reciprocal connection and its endpoint selection. None was found in the audited incidence, hard-gate, recorder or even matching swap interfaces. The handoff moves the already held odd stock and allows no independent fresh cycle with positive stock unless further stock is supplied.

## Replay

Run the adjacent Python replay. It checks the unnormalized integer incidence and cancellation, the fixed shared action on symmetric and antisymmetric inputs and exact rational rotation points. It checks the full-load endpoint and the half-stock readback without using a physical clock.
