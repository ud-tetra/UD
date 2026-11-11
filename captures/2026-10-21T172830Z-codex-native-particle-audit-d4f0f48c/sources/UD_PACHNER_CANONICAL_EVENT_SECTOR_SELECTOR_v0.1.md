# UD_PACHNER_CANONICAL_EVENT_SECTOR_SELECTOR_v0.1

**Date:** 2026-09-18  
**Status:** EXACT CANONICAL RANK-6 HODGE SECTOR SELECTOR / EVENT DYNAMICAL IDENTITY STILL OPEN  
**Physical promotion:** 0  
**Depends on:** `UD_PACHNER_EVENT_GENERATOR_INTERTWINER_AUDIT_v0.1`

---

## 1. Problem

The nonzero \(S_4\)-standard Hodge sector of

\[
\partial\Delta^4
\]

contains four copies of \(V_3\), so representation theory alone leaves a

\[
\mathbb{CP}^1
\]

family of six-dimensional invariant subspaces of type

\[
V_3\oplus V_3.
\]

The target is to determine whether the **Pachner move itself** removes this ambiguity.

---

## 2. Common event carrier

Let

\[
\mathcal A
=
\mathcal A_{\partial\Delta^4}
\]

be the unit skew Hodge–Dirac operator on the full five-tetrahedron boundary.

On the nonzero sector,

\[
\mathcal A^2=-5I.
\]

Define the Hodge complex structure

\[
\boxed{
J
=
\frac{\mathcal A}{\sqrt5},
\qquad
J^2=-I,
\qquad
J^\top=-J.
}
\]

Let

\[
P_{\rm std}
\]

be the exact \(S_4\)-character projector onto the standard-isotypic component:

\[
\boxed{
P_{\rm std}
=
\frac{3}{24}
\sum_{g\in S_4}
\chi_{\rm std}(g)\rho(g).
}
\]

Its rank is

\[
\boxed{
\operatorname{rank}P_{\rm std}=12.
}
\]

---

## 3. Raw Pachner response

Embed the two Pachner sides in the common 30-dimensional \(\partial\Delta^4\) chain basis.

Define

\[
L_\pm=-\widetilde{\mathcal A}_\pm^2
\]

and the symmetric move-response operator

\[
\boxed{
D=L_+-L_-.
}
\]

A single labeled move breaks the full \(S_4\) event symmetry.

Therefore \(D\) alone must not be used to select the event sector if the target event object is \(S_4\)-typed.

---

## 4. Canonical Reynolds restoration of \(S_4\)

Average the move-response operator over the event \(S_4\) action:

\[
\boxed{
\overline D
=
\frac1{24}
\sum_{g\in S_4}
\rho(g)D\rho(g)^\top.
}
\]

This is the unique equal-weight Reynolds projection of \(D\) onto the \(S_4\)-commutant.

Therefore

\[
[\overline D,\rho(g)]=0
\]

for every

\[
g\in S_4.
\]

No fitted group weights are introduced.

---

## 5. Standard-sector response

Restrict the averaged move response to the standard isotypic component:

\[
\boxed{
R_{\rm std}
=
P_{\rm std}\overline D P_{\rm std}.
}
\]

This is \(S_4\)-equivariant but need not preserve the Hodge complex structure \(J\).

To select an event phase-space sector, retain the \(J\)-compatible symmetric part:

\[
\boxed{
C_{\rm move}
=
\frac12
\left(
R_{\rm std}
+
J^\top R_{\rm std}J
\right).
}
\]

Since

\[
J^\top=-J,
\]

equivalently

\[
\boxed{
C_{\rm move}
=
\frac12
\left(
R_{\rm std}
-
JR_{\rm std}J
\right).
}
\]

This operator satisfies

\[
\boxed{
[C_{\rm move},J]=0
}
\]

and

\[
\boxed{
[C_{\rm move},\rho(g)]=0
\qquad
\forall g\in S_4.
}
\]

Thus its eigenspaces are simultaneously Hodge-invariant and \(S_4\)-invariant.

---

## 6. Exact spectrum on the standard sector

The exact nonzero eigenvalues of \(C_{\rm move}\) are

\[
\boxed{
\lambda_-
=
\frac{115-\sqrt{8065}}{80}
}
\]

and

\[
\boxed{
\lambda_+
=
\frac{115+\sqrt{8065}}{80}.
}
\]

Each has multiplicity

\[
\boxed{6}.
\]

Numerically,

\[
\lambda_-
\approx0.3149331868436516,
\]

\[
\lambda_+
\approx2.5600668131563484.
\]

Their exact relations are

\[
\boxed{
\lambda_-+\lambda_+
=
\frac{23}{8}
}
\]

and

\[
\boxed{
\lambda_-\lambda_+
=
\frac{129}{160}.
}
\]

Factor structure:

\[
129=3\cdot43,
\]

\[
160=2^5\cdot5,
\]

\[
8065=5\cdot1613.
\]

---

## 7. Canonical lower-response projector

Because

\[
\lambda_-<\lambda_+,
\]

the lower-response six-dimensional sector is uniquely selected.

Define

\[
\boxed{
P_{\rm evt}^{\rm Hodge}
=
\frac{
\lambda_+P_{\rm std}-C_{\rm move}
}{
\lambda_+-\lambda_-
}.
}
\]

Then

\[
\boxed{
(P_{\rm evt}^{\rm Hodge})^2
=
P_{\rm evt}^{\rm Hodge},
}
\]

\[
\boxed{
\operatorname{rank}
P_{\rm evt}^{\rm Hodge}
=
6,
}
\]

\[
\boxed{
[P_{\rm evt}^{\rm Hodge},J]=0,
}
\]

and

\[
\boxed{
[P_{\rm evt}^{\rm Hodge},\rho(g)]=0
\quad
\forall g\in S_4.
}
\]

Its image has representation type

\[
\boxed{
\operatorname{im}
P_{\rm evt}^{\rm Hodge}
\cong
V_3\oplus V_3.
}
\]

### AUTO_LOCK

`PACHNER_REYNOLDS_HODGE_RESPONSE_HAS_UNIQUE_LOWER_RANK6_STANDARD_SECTOR_v0.1`

---

## 8. Resolution of the prior \(\mathbb{CP}^1\) ambiguity

Representation theory alone gave a continuous family of six-dimensional sectors.

The additional move-response structure breaks that degeneracy:

\[
\mathbb{CP}^1
\quad\longrightarrow\quad
\left\{
\mathcal H_-,
\mathcal H_+
\right\},
\]

where

\[
\mathcal H_\pm
=
\ker(C_{\rm move}-\lambda_\pm I).
\]

The lower-response principle then selects

\[
\boxed{
\mathcal H_{\rm evt}^{\rm cand}
=
\mathcal H_-.
}
\]

This selection introduces no numerical tuning parameter.

### AUTO_LOCK

`PACHNER_MOVE_RESPONSE_REMOVES_CONTINUOUS_EVENT_SECTOR_AMBIGUITY_v0.1`

---

## 9. Generator on the selected sector

On

\[
\mathcal H_{\rm evt}^{\rm cand},
\]

the Hodge generator obeys

\[
\boxed{
\mathcal A^2=-5I_6.
}
\]

Thus the selected sector has native Hodge frequency

\[
\sqrt5.
\]

The current event mode has frequency

\[
\omega_\star
=
\sqrt{\frac{33}{8}}.
\]

Therefore a scaled event-generator pushforward would still require

\[
\boxed{
c_{\rm evt\leftarrow HD}
=
\sqrt{\frac{33}{40}}.
}
\]

The present result closes **which Hodge sector** should be tested.

It does not by itself derive the clock scaling.

---

## 10. Remaining map ambiguity

The sector projector is canonical, but an explicit coordinate isomorphism

\[
T:
\mathcal H_{\rm evt}^{\rm cand}
\longrightarrow
W_3^Q\oplus W_3^P
\]

still has basis/phase freedom unless the event symplectic form and Hamiltonian are pulled back and matched explicitly.

Therefore:

### CLOSED
- canonical six-dimensional Hodge sector;
- \(S_4\) representation type;
- Hodge invariance;
- lower-response selection.

### OPEN
- canonical coordinate map \(T\);
- exact symplectic normalization;
- generator pushforward;
- recurrence-clock promotion.

---

## 11. Governance

### AUTO_LOCK
- Reynolds-averaged move response;
- Hodge-compatible move-response operator;
- exact two-sector split;
- unique lower-response rank-6 projector;
- continuous \(\mathbb{CP}^1\) ambiguity removed.

### AUTO_FREEZE
- selecting the high-response sector without an independent law;
- identifying the selected sector with the event Hamiltonian before the coordinate/generator map closes;
- promoting \(\sqrt{33/40}\) as a free clock coefficient.

**Physical promotion:** 0.
