# THM-534 v2.23 — Peak-event information and native clock receipts

**27 October 2026.** Exact conditional audit of the continuous peak-and-hold candidate. Native metric and generators are unchanged. Kinematic record constructions are distinguished from native writing dynamics.

## Abstract

The v2.22 continuous peak rule preserves field norm in each phase. Its state-dependent event map nevertheless loses one continuous degree of freedom when the peak guard is made invariant by the hold mask. We derive the rank-22 switch differential and an explicit family of fixed-time collisions. An event-time receipt restores local invertibility. If the original field map is retained, a separate fixed-norm Euclidean record needs at least two prepared amplitudes to encode that receipt continuously.

The existing native carrier also contains a protected two-coordinate plane. A phase code can be placed there kinematically without adding stock, provided the output observable is changed from scalar core stock to the plane's projected norm. Writing that code requires event-time information and a pure generator that is outside the instantaneous native mask span. A neighboring-core guard supplies a full-rank counterexample, with a substantial capture penalty. These results constrain controller construction; they do not establish its native realization.

## 1. Setup

Use the original 23-dimensional real carrier of $[0123]$, $-[0124]$, with unit simplex metric, signed boundaries and whole-face gates. Faces are ordered $012,013,014,023,024,123,124$. The native skew generator is

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix}.
$$

Let $A=A_{(1,1,1,1,1,1,1)}$ be the loading generator and
$B=A_{(0,1,0,1,0,1,0)}$ the hold generator. The closed faces isolate core $1=0124$, including both contacts of the shared face.

For face vector $f$ and core vector $c=(c_0,c_1)$, put

$$
\beta=B_3^{\mathsf T}f,\qquad
K=B_3^{\mathsf T}B_3=\begin{pmatrix}4&-1\\-1&4\end{pmatrix}.
$$

Embed the gradient of $\beta_1$ as a full field vector $n$, so $n^{\mathsf T}x=\beta_1$ and $\|n\|^2=4$. The loading peak guard is

$$
n^{\mathsf T}z=0,\qquad c_1(4c_1-c_0)>0.
$$

Its incoming normal speed is

$$
d=n^{\mathsf T}Az=c_0-4c_1\ne0.
$$

The local event time $\tau(x)$ is the first admitted transverse guard hit. The v2.22 preparation ball gives one domain where this event is unique. The discrete load/hold mode is supplied as before.

## 2. The hold mask freezes the guard as well as the core

**Lemma.** Let $q=e_{\mathrm{core}\,1}$ and $p=n/2$. Then $p,q$ are orthonormal and

$$
Bp=Bq=0.
$$

This holds for every choice of the other three private-face gates.

*Proof.* The core column vanishes because all its incident gates are closed. The face vector in $p$ is half the boundary of cell $1$. Its lower image is zero by $B_2B_3=0$; its upper image is zero because every gate on its support is closed. $\square$

Consequently both $c_1=q^{\mathsf T}x$ and $\beta_1=2p^{\mathsf T}x$ are constant under hold. A trajectory captured at $\beta_1=0$ remains on that surface.

For the stated hold mask, exact rank calculation gives $\operatorname{rank}B=20$. Its full kernel is spanned by the uniform vertex vector, $p$ and $q$. The active cycle/face/core sector therefore has exactly this two-dimensional protected plane. This is selected-mask storage, not storage under all masks.

## 3. Norm preservation does not imply reversible capture

Define the event-indexed field map

$$
P(x)=e^{\tau(x)A}x.
$$

It records the field at its guard hit and omits the event time. At a common model time $T$, after all nearby trajectories have switched, the field map is

$$
\Phi_T(x)=e^{(T-\tau(x))B}e^{\tau(x)A}x.
$$

Both maps preserve the original field norm.

**Theorem 1 (one lost phase degree).** On a transverse peak-event domain, $DP$ and $D\Phi_T$ have rank $22$. In particular, the full field map after capture is locally non-injective even at a common model time; retaining only the load/hold bit does not remove this loss.

*Proof.* Write $z=P(x)$, $f_-=Az$, $f_+=Bz$. Implicit differentiation of the guard gives

$$
D\tau(x)=-\frac{n^{\mathsf T}e^{\tau A}}d.
$$

Therefore

$$
DP(x)=\left(I-\frac{f_-n^{\mathsf T}}d\right)e^{\tau A}.
$$

The bracket is identity plus a rank-one matrix and annihilates $f_-\ne0$. Its rank is exactly $22$.

Differentiating the common-time map gives

$$
D\Phi_T(x)=e^{(T-\tau)B}S(z)e^{\tau A},
\qquad
S(z)=I+\frac{(f_+-f_-)n^{\mathsf T}}d.
$$

This switch differential obeys

$$
\det S=\frac{n^{\mathsf T}f_+}{n^{\mathsf T}f_-}=0,
\qquad
\ker S=\mathbb R(f_--f_+),
\qquad
n^{\mathsf T}S=0.
$$

The numerator vanishes by the lemma. The rank-one perturbation thus has rank exactly $22$. Both exponential factors are invertible. $\square$

For an explicit collision family, take a strict event point $z$ and incoming event parameter $\tau_0$. For sufficiently small $s$, set

$$
z_s=e^{-sB}z,\qquad
x_s=e^{-(\tau_0-s)A}z_s.
$$

The hold flow leaves the guard invariant, and strict incoming transversality persists locally. On a first-event domain, $x_s$ hits the guard at $\tau_0-s$. Hence

$$
\Phi_T(x_s)
=e^{(T-\tau_0+s)B}e^{-sB}z
=e^{(T-\tau_0)B}z.
$$

The inputs are distinct: their tangent at $s=0$ is
$e^{-\tau_0A}(Az-Bz)\ne0$. They all have the same norm. A continuum of phases is therefore collapsed by the same field map.

At the rational event point $z=q$, the switch differential is particularly simple:

$$
S=I-\frac14nn^{\mathsf T}.
$$

It is a rank-22 orthogonal projector. This is the **differential of the switching process**, not a claim that the field is reset by this projector.

The lost direction is tangent to the norm sphere because
$z^{\mathsf T}(Az-Bz)=0$. Norm receipts cannot recover it. A known lower-dimensional preparation family can avoid phase ambiguity by fixing phase at preparation; the obstruction concerns its open preparation domain, including phase perturbations.

These statements concern state-dependent continuous stopping. The fixed-parameter Cayley load of v2.22 remains an invertible orthogonal field map on its prepared mode slice. Global reversibility of its one-way mode record and reset is a separate question.

## 4. What receipt is sufficient?

**Theorem 2 (event-time receipt and its norm budget).** The augmented event map

$$
x\longmapsto (P(x),\tau(x))
$$

is locally invertible on a first-event branch, with inverse $x=e^{-\tau A}z$. For the common-time field output $y=\Phi_T(x)$, the inverse with known receipt $\tau$ is

$$
z=e^{-(T-\tau)B}y,\qquad x=e^{-\tau A}z.
$$

A finite-valued record cannot make the unchanged field map injective on the collision family of Theorem 1.

*Proof.* The inverse formulas are direct. The time derivative is nonzero on the event map's lost direction; equivalently, augmenting its rank-22 Jacobian by the time row gives rank $23$. A finite label cannot distinguish a continuum of equal field outputs. $\square$

This requires one continuous event-time coordinate locally, not a physical-clock identification. At finite prescribed resolution, finitely many labels can encode finitely many time bins; that is a different, approximate task.

The common-time inverse assumes the observation parameter $T$ is known. If it is not recorded or supplied, the continuing hold evolution also needs its elapsed-parameter information. The event-indexed inverse uses the field at the event itself. Neither formula supplies an autonomous or physical clock.

Suppose a separate Euclidean record starts in a fixed known state and the field output remains the same norm-preserving $P(x)$ or $\Phi_T(x)$. Total norm conservation forces the record's norm to stay at its prepared value. Then:

- A zero-stock record stays zero and cannot store the receipt.
- One real record amplitude of fixed norm has at most two values.
- Two prepared real amplitudes suffice kinematically on a local time domain.

For example, for supplied $r>0$, $\omega\ne0$, the rational circle code

$$
k(\tau)=r\left(\frac{1-u^2}{1+u^2},
                   \frac{2u}{1+u^2}\right),
\qquad u=\omega\tau
$$

has norm $r$, with inverse

$$
\tau=\frac{k_2}{\omega(r+k_1)}.
$$

This code does not supply a dynamical clock. Its initial stock $r^2$, scale $\omega$, writing interaction and reset are additional source requirements. The lower bound assumes the unchanged field map, a separate product Euclidean metric and exact recovery on an open phase family. It is not a heat, energy or action-unit law.

## 5. Existing native storage capacity and a blocked primitive writer

The protected plane $\operatorname{span}\{q,p\}$ allows a different **kinematic** option. At a peak point write $z=w+rq$, with $w\perp q,p$, $r=c_1\ne0$. Given an event-time receipt, define

$$
y=w+r\left(\frac{1-u^2}{1+u^2}q+
                 \frac{2u}{1+u^2}p\right),
\qquad u=\omega\tau.
$$

The original field norm is unchanged. Both plane coordinates remain fixed under hold. On a local branch of known sign of $r$, let

$$
Q=q^{\mathsf T}y,\quad R=p^{\mathsf T}y,\quad
r=\operatorname{sgn}(c_1)\sqrt{Q^2+R^2}.
$$

Then

$$
\tau=\frac{R}{\omega(r+Q)},\qquad
z=y-Qq-Rp+rq.
$$

The construction can store the receipt in existing field coordinates without adding norm stock, but it changes the retained observable to

$$
S_{\rm plane}=Q^2+R^2.
$$

This is the orthogonal projected-plane norm, not scalar core stock $Q^2$ or the original diagonal cell-ownership sum. Selecting it as output needs its own observable justification. The unchanged peak protocol has $R=0$ and does not perform this encoding.

**Theorem 3 (capacity is not a native writing law).** The pure plane-rotation generator

$$
J=pq^{\mathsf T}-qp^{\mathsf T}
$$

is not in the instantaneous linear span of the original native mask generators.

*Proof.* Every $A_h$ satisfies, in the stated basis,

$$
(A_h)_{012,\mathrm{core}\,0}
+(A_h)_{012,\mathrm{core}\,1}=0.
$$

It is the shared-star constraint: one face gate controls both opposite signed incidences. But $J$ has no contact to core $0$, and

$$
J_{012,\mathrm{core}\,0}
+J_{012,\mathrm{core}\,1}=\frac12.
$$

The same linear functional vanishes on the entire native instantaneous span, proving the claim. $\square$

Finite controlled compilation is not excluded by this span test; Lie-bracket synthesis is a separate question. Moreover, a reset depending only on $z$ cannot obtain the omitted $\tau$ from $z$: different arrival phases have the same event field. A clock must generate and retain that information before it is discarded. The formula is therefore a capacity and receipt contract, not a source-derived local gate update.

The plane's five-coordinate footprint is geometrically local. The shared-contact constraint shows why that fact alone does not make its writer an admitted native primitive.

## 6. A guard-specific obstruction: neighboring-core timing

The rank loss at a common time is not a theorem against every native event switch. Let $n_0^{\mathsf T}x=\beta_0$ and switch on the neighboring core's strict peak instead. During load and hold,

$$
n_0^{\mathsf T}Az=c_1-4c_0,\qquad
n_0^{\mathsf T}Bz=-3c_0.
$$

The same calculation gives

$$
\det S_0=\frac{-3c_0}{c_1-4c_0}.
$$

It is nonzero whenever both normal speeds are nonzero. The continuing neighboring field can preserve phase at a common observation time even though the chosen output core is isolated.

At the rational guard point $c_0=1,c_1=2$, with faces zero, the determinant is $3/2$ and the differential has rank $23$. For the v2.22 private-face preparation with $v>0$, the neighboring core's first peak occurs at

$$
t_N=\frac{2\pi}{\sqrt3+\sqrt5}.
$$

Here

$$
\frac{c_1}{c_0}
=\frac{\sqrt5-\sqrt3}{\sqrt5+\sqrt3},
\qquad
\det S_0=\sqrt{\frac35}.
$$

The first-event statement follows from
$\beta_0/v=\sin((\sqrt3+\sqrt5)t/2)\sin((\sqrt5-\sqrt3)t/2)$, which is positive before $t_N$, then crosses down. Exact rational interval bounds put retained **core** stock $c_1(t_N)^2/v^2$ between $0$ and $1/1000$. The earlier output-core peak captures more than $1/4$. This alternative preserves local fixed-time rank at a substantial capture penalty.

Full rank gives local invertibility on the prepared loading branch, not global reversibility of the mode logic. The factor $\sqrt{3/5}\ne1$ also shows that full rank is not an isometry or a proof of a closed Hamiltonian implementation. Event-indexed first-hit maps still omit their event time; the distinction here is the common-time field map.

## 7. Reproduction and next construction target

Run from this capture directory:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_event_information.py

The checker uses standard-library rational arithmetic. It verifies 64 transverse peak/hold Jacobians of rank 22 and 64 augmented full-rank event receipts; the exact projector witness; hold-kernel rank; 51 native-plane code/inverse controls; 33 separate fixed-radius codes; the native writer constraint for all 128 masks; the neighboring rational full-rank witness; and rational intervals for the canonical neighboring event.

The continuous peak-and-hold candidate therefore needs an information receipt or a changed switching construction for reversible operation on an open phase domain. The native carrier has a protected plane capable of holding a receipt under a changed output observable, but its clock source and writing law remain open.

The next concrete target is a native clock-generation and writing protocol with explicit gate, norm, output-observable and reset receipts. A different guard must be assessed for both retained information and capture quality. Physical clock, action-unit and particle correspondences remain unestablished. Independent review is pending; physical promotion remains zero.
