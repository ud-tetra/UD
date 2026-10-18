# UD_PACHNER_EVENT_DARBOUX_MAP_AND_GENERATOR_PUSHFORWARD_v0.1

**Date:** 2026-09-18  
**Status:** EXACT INTERNAL DARBOUX MAP + EXACT CONDITIONAL EVENT-GENERATOR PUSHFORWARD  
**Physical promotion:** 0  
**Depends on:** `UD_PACHNER_CANONICAL_EVENT_SECTOR_SELECTOR_v0.1`

## 1. Target

Construct an explicit symplectic coordinate map from the canonically selected rank-6 Pachner Hodge sector

\[
\mathcal H_{\rm evt}^{\rm Hodge}
=
\operatorname{im}P_{\rm evt}^{\rm Hodge}
\]

to a canonical \(V_3^Q\oplus V_3^P\) coordinate space and test the event-generator pushforward.

## 2. Canonical vertex-standard seed

Let \(P_{0,\rm std}\) project the \(C_0(\partial\Delta^4)\) vertex chain onto the \(S_4\)-standard subspace carried by vertices \(0,1,2,3\).

The selected event projector satisfies

\[
\boxed{
P_{0,\rm std}
P_{\rm evt}^{\rm Hodge}
P_{0,\rm std}
=
\alpha P_{0,\rm std}
}
\]

with

\[
\boxed{
\alpha
=
\frac12
\left(
1+\frac{89}{\sqrt{8065}}
\right)
}.
\]

Numerically,

\[
\alpha\approx 0.995516163029957.
\]

Thus the selected rank-6 sector projects nondegenerately and isotropically onto the unique vertex-standard \(V_3\).

### AUTO_LOCK

`PACHNER_SELECTED_EVENT_SECTOR_HAS_NONDEGENERATE_VERTEX_STANDARD_PROJECTION_v0.1`

## 3. Canonical \(Q\)-embedding

Define

\[
\boxed{
\iota_Q
=
\alpha^{-1/2}
P_{\rm evt}^{\rm Hodge}
P_{0,\rm std}.
}
\]

Restricted to the three-dimensional vertex-standard domain,

\[
\boxed{
\iota_Q^\top\iota_Q
=
I_3.
}
\]

The alternating form

\[
\iota_Q^\top J\iota_Q
\]

is \(S_4\)-invariant on the real standard irrep. No trivial alternating two-form exists on this irrep, and the exact matrix calculation gives

\[
\boxed{
\iota_Q^\top J\iota_Q=0.
}
\]

Therefore the image of \(\iota_Q\) is a canonical Lagrangian three-plane inside the selected rank-6 Hodge sector.

### AUTO_LOCK

`VERTEX_STANDARD_PROJECTION_GIVES_CANONICAL_LAGRANGIAN_Q_HALF_v0.1`

## 4. Canonical \(P\)-embedding

Let

\[
J=\frac{\mathcal A}{\sqrt5}
\]

be the Hodge complex structure.

Define

\[
\boxed{
\iota_P
=
J\iota_Q.
}
\]

Then

\[
\iota_P^\top\iota_P=I_3,
\qquad
\iota_Q^\top\iota_P=0,
\qquad
J\iota_P=-\iota_Q.
\]

Thus

\[
\boxed{
\mathcal H_{\rm evt}^{\rm Hodge}
=
\operatorname{im}\iota_Q
\oplus
\operatorname{im}\iota_P.
}
\]

## 5. Explicit three-coordinate standard basis

Choose the fixed tetrahedral vertex-standard basis

\[
u_1
=
\frac1{\sqrt2}(1,-1,0,0,0),
\]

\[
u_2
=
\frac1{\sqrt6}(1,1,-2,0,0),
\]

\[
u_3
=
\frac1{\sqrt{12}}(1,1,1,-3,0)
\]

in \(C_0\).

Let

\[
U=(u_1,u_2,u_3).
\]

Define

\[
\boxed{
Q=\iota_QU,
\qquad
P=JQ.
}
\]

The full six-frame is

\[
\boxed{
W=(Q\;P).
}
\]

Exact checks:

\[
\boxed{
W^\top W=I_6
}
\]

and

\[
\boxed{
P_{\rm evt}^{\rm Hodge}W=W.
}
\]

The component-level exact matrix is supplied in the companion CSV.

## 6. Darboux coordinate map

Define

\[
\boxed{
T_H
=
W^\top
:
\mathcal H_{\rm evt}^{\rm Hodge}
\rightarrow
\mathbb R^3_Q\oplus\mathbb R^3_P.
}
\]

For

\[
x\in\mathcal H_{\rm evt}^{\rm Hodge},
\]

the coordinates are

\[
\boxed{
q=Q^\top x,
\qquad
p=P^\top x.
}
\]

Conversely,

\[
\boxed{
x=Qq+Pp.
}
\]

Define

\[
\mathbb J_0
=
\begin{pmatrix}
0&-I_3\\
I_3&0
\end{pmatrix}.
\]

Then

\[
\boxed{
W^\top JW
=
\mathbb J_0.
}
\]

Therefore \(T_H\) is an exact Darboux/symplectic coordinate map for the selected Hodge sector.

### AUTO_LOCK

`PACHNER_SELECTED_EVENT_SECTOR_HAS_EXPLICIT_DARBOUX_MAP_v0.1`

## 7. Exact Hodge-generator pushforward

Because

\[
\mathcal A=\sqrt5\,J,
\]

the selected generator satisfies

\[
\boxed{
T_H\mathcal A W
=
\sqrt5\,\mathbb J_0.
}
\]

Equivalently, in \((q,p)\) coordinates,

\[
\boxed{
\dot q=-\sqrt5\,p,
\qquad
\dot p=\sqrt5\,q.
}
\]

Thus the selected Hodge sector is an exact isotropic three-mode Hamiltonian oscillator with internal frequency

\[
\boxed{\sqrt5}.
\]

## 8. Event-generator pushforward

Current event geometry supplies

\[
\omega_\star
=
\sqrt{\frac{33}{8}}.
\]

If the current named event generator on

\[
W_3^Q\oplus W_3^P
\]

is the isotropic Hamiltonian generator

\[
\boxed{
G_{\rm evt}
=
\omega_\star\mathbb J_0,
}
\]

then

\[
\boxed{
G_{\rm evt}T_H
=
c_{\rm evt\leftarrow HD}
T_H\mathcal A P_{\rm evt}^{\rm Hodge},
}
\]

where

\[
\boxed{
c_{\rm evt\leftarrow HD}
=
\sqrt{\frac{33}{40}}.
}
\]

This factor is not fitted; it is the unique frequency ratio.

### Classification

`PACHNER_TO_EVENT_GENERATOR_PUSHFORWARD_v0.1`

**EXACT CONDITIONAL** on the named event generator being the isotropic \(\omega_\star\mathbb J_0\) generator.

Current source still states that the event-space dynamical identity is separate, so that final identification is not silently promoted.

## 9. What is now closed

### EXACT
- canonical selected rank-6 Hodge sector;
- canonical \(Q\)-Lagrangian half from vertex-standard projection;
- canonical \(P=JQ\) half;
- explicit Darboux map \(T_H\);
- exact Hodge oscillator generator \(\sqrt5\mathbb J_0\);
- unique clock ratio \(\sqrt{33/40}\).

### OPEN
- source theorem that the named event generator is exactly \(\omega_\star\mathbb J_0\) in the current event coordinates;
- physical-time map;
- recurrence-refractory promotion.

## 10. Governance

### AUTO_LOCK
- exact coefficient \(\alpha\);
- canonical Lagrangian polarization;
- explicit symplectic coordinate map;
- exact internal generator pushforward.

### AUTO_FREEZE
- claiming Q121 alone already proves the event Hamiltonian identity;
- treating \(\sqrt{33/40}\) as a free coefficient;
- physical-time interpretation.

**Physical promotion:** 0.
