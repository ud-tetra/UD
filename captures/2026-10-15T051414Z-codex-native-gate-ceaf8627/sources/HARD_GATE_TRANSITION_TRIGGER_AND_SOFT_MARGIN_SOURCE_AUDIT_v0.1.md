# Hard-Gate Transition Trigger and Soft-Margin Source Audit v0.1

**Date:** 2026-08-28  
**Current authority:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39`  
**Upstream:** `CLASS_DEPENDENT_GATE_TRANSITION_AND_BOUNDARY_ASYMMETRY_SOURCE_AUDIT_v0.1`  
**Physical promotion:** 0  
**Classification:** `PASS_NO_GO__HARD_GATE_STATE_AND_RECEIPTS_ARE_SOURCE_COMPLETE__FACTOR_FAILURE_IDENTITY_SOFT_MARGIN_AND_PREDICTIVE_TRIGGER_ARE_NOT_DERIVABLE_FROM_CURRENT_BOOLEAN_GATE_DATA`

---

## 1. Executive ruling

Current Q156 defines

\[
\boxed{
h_e
=
C_{{\rm cl},e}^{\rm hard}
T_{{\rm int},e}^{\rm hard}
}
\]

with hard Boolean factors.

Current Q167/Q173 derive gate-conditioned support receipts.

This closes:

- the binary gate state;
- support-current evaluation conditional on that state;
- the exact \(W_2\) shape jump once a gate transition is supplied.

It does not close:

- which hard factor failed when \(h_e=0\);
- any distance to the closure/integrity threshold;
- a soft conductance;
- the transition trigger;
- transition timing or event rate.

Therefore current hard-gate data cannot generate a predictive \(W_2\) kinetic history by themselves.

---

## 2. Boolean-factor identifiability

For one edge,

\[
h=CT,
\qquad
C,T\in\{0,1\}.
\]

If

\[
h=1,
\]

then uniquely

\[
\boxed{
(C,T)=(1,1).
}
\]

If

\[
h=0,
\]

there are three possibilities:

\[
\boxed{
(C,T)
\in
\{(0,0),(0,1),(1,0)\}.
}
\]

Thus a closed hard edge does not identify whether failure arose from:

- closure only;
- integrity only;
- both.

### AUTO_LOCK

`HARD_GATE_ZERO_DOES_NOT_IDENTIFY_CLOSURE_VS_INTEGRITY_FAILURE_v0.1`

---

## 3. Full connected-K4 decomposition count

The 38 connected binary \(K_4\) masks distribute by open-edge count as

\[
\boxed{
16\text{ masks with }3\text{ open edges},
}
\]

\[
\boxed{
15\text{ masks with }4\text{ open edges},
}
\]

\[
\boxed{
6\text{ masks with }5\text{ open edges},
}
\]

\[
\boxed{
1\text{ mask with }6\text{ open edges}.
}
\]

For a mask with \(z\) zero edges, each zero has three Boolean factorizations while each open edge has one.

Therefore the number of \((C_{\rm cl}^{\rm hard},T_{\rm int}^{\rm hard})\) assignments compatible with a mask is

\[
\boxed{
3^z.
}
\]

Across all 38 connected masks the total number of compatible hard-factor assignments is

\[
\boxed{
16\cdot3^3
+
15\cdot3^2
+
6\cdot3
+
1
=
586.
}
\]

Prime factorization:

\[
\boxed{
586=2\cdot293,
}
\]

with \(293\) prime.

This count is an identifiability receipt, not a state probability.

---

## 4. Soft-margin no-go

Suppose one attempts to introduce underlying margins

\[
m_{{\rm cl},e},
\qquad
m_{{\rm int},e}
\]

with

\[
C_{\rm cl}^{\rm hard}
=
\mathbf1[m_{\rm cl}\ge0],
\]

\[
T_{\rm int}^{\rm hard}
=
\mathbf1[m_{\rm int}\ge0].
\]

The hard gate retains only the signs needed for the Boolean product.

For any strictly increasing functions \(f,g\) satisfying

\[
f(0)=g(0)=0,
\]

the transformed margins

\[
m_{\rm cl}'=f(m_{\rm cl}),
\qquad
m_{\rm int}'=g(m_{\rm int})
\]

produce the same hard gates.

Infinitely many magnitudes and slopes therefore correspond to the same hard-gate history.

Hence:

\[
\boxed{
h_e
\not\Rightarrow
(m_{{\rm cl},e},m_{{\rm int},e})
}
\]

and

\[
\boxed{
h_e
\not\Rightarrow
\dot h_e
}
\]

without an independently sourced evolution law.

### AUTO_LOCK

`HARD_BOOLEAN_GATE_DOES_NOT_IDENTIFY_SOFT_MARGIN_OR_TRANSITION_VELOCITY_NO_GO_v0.1`

---

## 5. Current Q156 status is exactly consistent with this no-go

Q156 records

\[
g_{\rm boundary}^{\rm hard}
=
\frac1{|\partial_ES|}
\sum_{e\in\partial_ES}h_e
\]

and explicitly states:

**smooth conductance open**.

Thus a proposal such as

\[
a_e=f(m_{{\rm cl},e},m_{{\rm int},e})
\]

requires a new source law.

It cannot be recovered from \(g_{\rm boundary}^{\rm hard}\) alone.

---

## 6. Event-conditioned W2 impulse law

Although the transition trigger is open, its geometry consequence is exact.

Define hard class weights

\[
W_A^{(h)}
=
\frac{h_{01}+h_{23}}2,
\]

\[
W_B^{(h)}
=
\frac{h_{02}+h_{13}}2,
\]

\[
W_C^{(h)}
=
\frac{h_{03}+h_{12}}2,
\]

and

\[
c_i^{(h)}
=
\frac{W_i^{(h)}}{S_h}
-\frac13.
\]

For a supplied gate event

\[
h^-\rightarrow h^+,
\]

the exact normalized pairing impulse is

\[
\boxed{
\Delta c_i^{(h)}
=
c_i^{(h,+)}
-
c_i^{(h,-)}.
}
\]

The normalized accessibility jump is

\[
\boxed{
\Delta\widehat{\mathsf A}
=
-\frac32
\operatorname{diag}
(
\Delta c_A,
\Delta c_B,
\Delta c_C
).
}
\]

For every connected-to-connected single-edge \(K_4\) transition,

\[
\boxed{
\Delta c^{(h)}\neq0.
}
\]

Therefore the current theory already provides a **conditional discrete \(W_2\) impulse response**.

### AUTO_LOCK

`HARD_GATE_EVENT_CONDITIONALLY_DEFINES_EXACT_DISCRETE_W2_IMPULSE_v0.1`

---

## 7. Discrete derivative scope

With update index \(n\), one may write the event receipt

\[
\boxed{
\Delta_n c_i
=
c_i^{(n+1)}-c_i^{(n)}.
}
\]

This is a discrete update difference.

Do not divide it by physical time.

The current event/update clock does not yet supply physical seconds.

Thus the allowed language is:

**\(W_2\) shape impulse per admitted packet update**,

not:

**physical \(W_2\) strain rate**.

---

## 8. Predictive trigger requirements

A predictive gate source needs one of the following to be independently derived:

1. closure/integrity soft margins;
2. a Boolean update law for \(C_{\rm cl}^{\rm hard}\) and \(T_{\rm int}^{\rm hard}\);
3. a state-machine transition rule tied to current packet variables;
4. a stochastic transition law with source-derived probabilities/rates.

It must state:

- state variables;
- threshold/projection rule;
- update law;
- symmetry;
- source provenance;
- gate-event receipt;
- reduction/null behavior;
- falsification/rollback conditions.

No threshold may be selected merely to create \(W_2\) activity.

---

## 9. Source audit verdict

Current source-complete information gives:

\[
\boxed{
h_e
}
\]

and gate-conditioned receipts.

Current source does not give:

\[
\boxed{
m_{\rm cl},
\quad
m_{\rm int},
\quad
\dot m_{\rm cl},
\quad
\dot m_{\rm int},
\quad
P(h^{n+1}|h^n),
\quad
\text{or a deterministic trigger}.
}
\]

Therefore a predictive hard-gate transition law remains a genuine source gap.

---

## 10. Verdict

```text
ARTIFACT:
HARD_GATE_TRANSITION_TRIGGER_AND_SOFT_MARGIN_SOURCE_AUDIT_v0.1

CLASSIFICATION:
PASS_NO_GO

CLOSED:
hard Boolean gate state
hard gate factor product
gate-conditioned support receipts
event-conditioned W2 jump

NOT IDENTIFIED:
failure subtype when h=0
soft margins
margin magnitude
margin rate
transition trigger
transition probability/rate

CONNECTED K4:
38 masks
586 compatible underlying hard-factor assignments

PHYSICAL PROMOTION:
0
```

---

## 11. Brightest frontier

The \(W_2\) source question has now reached a true trigger boundary.

Do not add arbitrary soft thresholds.

The next productive gap is:

`GATE_EVENT_CONSTRAINT_IMPULSE_AND_SEAM_COMPATIBILITY_AUDIT_v0.1`

Question:

When a legitimate hard-gate event is externally supplied or later source-derived, can the exact discrete \(W_2\) metric jump be reconciled with:

- shared-face metric compatibility;
- support receipts;
- the temporal burden-curvature constraint?

This tests whether the already-earned conditional gate impulse is dynamically admissible before investing in a predictive trigger theory.
