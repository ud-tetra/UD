# UD Edge Closure and Transport Integrity Hard-Gate Derivation v0.1

**Execution date:** 2026-08-21  
**Research mode:** RETAINED-EXISTENCE FORMATION FLOOR / TYPE REPAIR / EDGE-LOCAL ADMISSION  
**NEXUS:** HELD  
**CROWN:** OFF  
**Physical promotion:** 0  

## Verdict

\[
\boxed{
\texttt{PARTIAL\_PASS\_HARD\_GATE\_TYPING\_CLOSED\_\_CONTINUOUS\_MARGINS\_NOT\_DERIVED}
}
\]

The current source corpus supports \(C_{\rm cl}\) and \(T_{\rm int}\) as foundational
formation-floor conditions, but it does not supply a source-complete smooth numerical score
for either object.

The scientifically safest current form is therefore to type them as **hard local admission predicates**.

---

## I. Closure is not transport flatness

Current graph-first UD distinguishes:

1. combinatorial / admissibility closure of a face or cell;
2. transport holonomy around that closed boundary.

A completed face may satisfy its combinatorial closure grammar while carrying

\[
H_{\partial \sigma}\neq I.
\]

Therefore:

\[
\boxed{
\text{combinatorial closure}
\neq
\text{flat transport}.
}
\]

### AUTO_LOCK

`COMBINATORIAL_CLOSURE_AND_TRANSPORT_FLATNESS_ARE_DISTINCT_EDGE_GATE_TYPES_THEOREM_v0.1`

### AUTO_FREEZE

`CLOSURE_GATE_EQUALS_LOOP_HOLONOMY_IDENTITY`

Nontrivial holonomy is not, by itself, failure of the closure gate.

---

## II. Hard closure receipt

Let

\[
r_\alpha^{\rm cl}\in\{0,1\}
\]

denote the already-admitted binary closure receipt for a local object
\(\alpha\) required to support edge \(e\).

Let

\[
\operatorname{Req}_{\rm cl}(e)
\]

be the set of local closure receipts required by the declared packet/patch context.

Define

\[
\boxed{
C_{\rm cl}^{\rm hard}(e)
=
\min_{\alpha\in\operatorname{Req}_{\rm cl}(e)}
r_\alpha^{\rm cl}.
}
\]

Since every receipt is binary,

\[
\boxed{
C_{\rm cl}^{\rm hard}(e)
=
\prod_{\alpha\in\operatorname{Req}_{\rm cl}(e)}
r_\alpha^{\rm cl}.
}
\]

Thus

\[
C_{\rm cl}^{\rm hard}(e)=1
\]

iff every required local closure receipt exists.

### AUTO_LOCK

`EDGE_CLOSURE_HARD_GATE_IS_CONJUNCTION_OF_REQUIRED_LOCAL_CLOSURE_RECEIPTS_THEOREM_v0.1`

### Scope guard

This theorem does not decide, universally, whether the required objects are the two
incident faces, one retained tetrahedral cell, several neighboring cells, or a higher
patch. That set is supplied by the Context of Use.

Within a fully retained \(K_4\) cell, every required local closure receipt is already present,
so the closure hard gate is uniform:

\[
\boxed{
C_{\rm cl}^{\rm hard}(e)=1
\quad\forall e\in E(K_4).
}
\]

Therefore a fully retained equal-cell \(K_4\) does not obtain a smooth internal anisotropy
from the closure predicate alone.

---

## III. Hard transport-integrity predicate

Let

\[
\mathcal A_i
\]

denote the locally admitted state fiber at node \(i\), and let

\[
U_{ij}
\]

be the declared oriented transport map on edge \(e=(ij)\).

Define

\[
\boxed{
T_{\rm int}^{\rm hard}(e)=1
}
\]

iff all transport conditions required by the current Context of Use are satisfied, including:

1. \(U_{ij}\) is a well-typed map on the declared local state channel;
2. admissible input states are carried into the declared admissible target domain;
3. required overlap / transition compatibility is satisfied;
4. any inverse or reverse-map requirement explicitly present in that transport sector is satisfied.

Otherwise,

\[
T_{\rm int}^{\rm hard}(e)=0.
\]

### AUTO_LOCK

`EDGE_TRANSPORT_INTEGRITY_IS_LAWFUL_LOCAL_TRANSITION_PREDICATE_NOT_LOOP_FLATNESS_RULE_v0.1`

### Critical guard

The local predicate does **not** require

\[
H_C=I
\]

for every loop containing \(e\).

A lawful connection may carry nontrivial holonomy.

### AUTO_FREEZE

`NONTRIVIAL_HOLONOMY_IS_AUTOMATIC_TRANSPORT_INTEGRITY_FAILURE`

---

## IV. Hard structural formation gate

Define

\[
\boxed{
h_e
=
C_{\rm cl}^{\rm hard}(e)
T_{\rm int}^{\rm hard}(e)
\in\{0,1\}.
}
\]

Then

\[
h_e=1
\]

iff both foundational edge conditions pass.

### AUTO_LOCK

`EDGE_FOUNDATIONAL_FORMATION_GATE_IS_CLOSURE_AND_TRANSPORT_CONJUNCTION_RULE_v0.1`

This is a veto variable, not a smooth response amplitude.

### AUTO_FREEZE

`HARD_CLOSURE_OR_TRANSPORT_PREDICATE_USED_AS_SMOOTH_STIFFNESS_COEFFICIENT_WITHOUT_MARGIN_LAW`

---

## V. Aggregate support does not replace local vetoes

The normalized six-edge support tensor is

\[
M_E(v)
=
5E^{\mathsf T}\operatorname{diag}(v_e)E.
\]

Consider the flat state with one edge removed from support:

\[
v=(0,1,1,1,1,1).
\]

Then exactly

\[
M_E
=
\begin{pmatrix}
10&0&0\\
0&15/2&-5/2\\
0&-5/2&15/2
\end{pmatrix}
\]

with eigenvalues

\[
\boxed{
10,\quad10,\quad5.
}
\]

Hence

\[
M_E\succ0
\]

even though one edge has failed.

For one failed opposite-edge pair,

\[
v=(0,0,1,1,1,1),
\]

\[
\boxed{
M_E=\operatorname{diag}(10,5,5)\succ0.
}
\]

Thus redundancy can preserve an aggregate positive spatial support tensor while local
formation gates fail.

### AUTO_LOCK

`POSITIVE_AGGREGATE_SPATIAL_SUPPORT_DOES_NOT_IMPLY_ALL_LOCAL_EDGE_FORMATION_GATES_PASS_THEOREM_v0.1`

### AUTO_FREEZE

`M_SUPPORT_POSITIVE_DEFINITE_USED_AS_SUBSTITUTE_FOR_WEAKEST_LOCAL_EDGE_GATE_SELECTOR`

This is the edge-space analogue of the already-locked result that determinant/log-det
statistics do not replace the weakest-gate selector.

---

## VI. Scientific consequence

The formation architecture now separates into:

\[
\boxed{
\text{hard structure}
\;\land\;
\text{soft margin}.
}
\]

The hard structure is

\[
h_e=C_{\rm cl}^{\rm hard}(e)T_{\rm int}^{\rm hard}(e).
\]

The still-open continuous margin must come from the remaining formation gates:

\[
B_{\rm tol},
\qquad
D_{\rm ct},
\qquad
P_{\rm rec},
\]

or from future source-complete continuous refinements of closure/transport if such refinements
are independently derived.

This is a stronger architecture than forcing all five mechanical gates onto the same numerical scale.

---

## VII. Current open burden

No present source-complete formula was recovered for a smooth numerical

\[
C_{\rm cl}(e)
\]

or

\[
T_{\rm int}(e)
\]

that could be used as an anisotropy amplitude without adding assumptions.

Therefore these two gates are closed only at the **admission-predicate** level.

The next soft source audit must begin with the remaining mechanical margins, with
burden tolerance \(B_{\rm tol}\) first because burden is already an explicit packet-state variable.
