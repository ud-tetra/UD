# UD factor-state jet nonidentifiability v0.1

**10 October 2026 UTC.** Physical promotion **0**. Constructor replay; independent review pending.

## Source, premise, and question

The UD coefficient ledger Q156 defines the hard edge product
\(h_e=C^{\rm hard}_{\rm cl,e}T^{\rm hard}_{\rm int,e}\). Q166 defines native adjacent-degree incidence currents, Q167 the hard-gated vertex–edge current, and Q173 the hard-gated face–cell current. The [first-jet activity audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T153453Z-codex-current-jet-34cb9e72) detects activity on a fixed native generator. Here the question is different: can arbitrarily many **pre-event amplitude/current derivatives** identify which factor caused a closed product gate?

This is a **conditional** information result. Assume that before the next primitive event the amplitude generator and the observed currents depend on the edge factors only through \(h_e\), with all other gates, including face gates, fixed. It does not assert that UD has admitted a particular full gated generator, physical time law, repair event, or factor-independent preparation. An independently sourced observation of a factor, or a generator term that depends separately on \(C\) and \(T\), escapes this premise.

## Exact obstruction

For an edge \(e\), \((C,T)=(0,1)\) and \((0,0)\) both give \(h_e=0\). Put identical initial amplitudes \(c_0\) in those two factor states. If \(A(C,T)=A(h)\) over the pre-event interval, then

\[
A(0,1)=A(0,0),\qquad A(0,1)^k c_0=A(0,0)^k c_0\quad(k\geq0).
\]

Consequently their entire analytic pre-event amplitude trajectories coincide, as do every derivative of any current or observation computed from those amplitudes and fixed masks. This follows from equality of the operators, so is an **all-orders theorem**, not an extrapolation from a finite jet test. No rule using only that observation history can always determine whether transport is open or closed in these two states.

To show why the ambiguity matters, declare the diagnostic intervention \(R_C:(C,T)\mapsto(1,T)\). It is **hypothetical**; the ledger does not admit this as a UD event. From \((0,1)\), it opens the product; from \((0,0)\), it leaves the product shut. Thus identical pre-event observation records are compatible with different post-event hard masks under the same factor-specific action. A predictor that receives only the product-mask amplitude history has insufficient input to pick the correct branch. A source law could also forbid one preparation or make \(R_C\) inadmissible; that would resolve this particular witness by changing the premises.

## Exact rational replay

`python3 verify.py` builds the 23-coordinate two-tetrahedron register \(\langle0123,0124\rangle\) with 47 adjacent-degree incidences. It uses the skew incidence test operator with the Q156 hard product on vertex–edge links, and all edge–face and face–cell weights fixed at one. This operator is a **diagnostic product-only lift**, not a promotion of a source-complete gated dynamics. It compares \((0,1)\) and \((0,0)\) at edge \(01\), keeps every other edge open, and starts with \(c_0=e_0+e_{01}\).

The two complete matrices agree. Amplitude jets through order 8 and all 47 Q166 current jets through order 5 agree exactly as rational numbers. Under the diagnostic \(R_C\), \(h_{01}\) becomes 1 versus 0. At the same amplitude immediately after the proposed event, the post-operator derivative difference (first state minus second) is exactly \(+e_0-e_1-e_{01}\), with all other coordinates equal. Twelve named assertions pass. The finite checks catch construction mistakes; the all-orders conclusion follows algebraically from identical matrices.

The immediate vertex–edge gated current is also still zero on an edge whenever its hard mask is zero; a current-based switch test cannot read the missing factor from that zero. This example is about **factor identifiability**, not the previous activity-detection theorem.

## Consequence for the predictive gate

The Q156 product is a compact sufficient input for following a **given** hard-mask trajectory, provided the specified dynamics factor through that product. It is not by itself a sufficient predictive state for factor-specific future events. An admissibility predicate can restrict an event, but to decide an event prospectively it needs a sourced primitive state and update rule.

A candidate source-complete event contract should state, before the event: the addressed edge or face, primitive closure receipts and transport state (or an equivalent sufficient state), the admissibility predicate, event ordering and timing parameter, the allowed factor update, and a cause-tagged pre/post receipt. It must specify the relation of edge product gates to Q173 face gates and be covariant under carrier relabeling. It must handle simultaneous candidates and null/reduction cases without a retrospective tie-break. Each clause is a **source request**, not a derived UD law.

**Stop rule:** Taking higher derivatives of observations that factor only through the same hard mask cannot distinguish its hidden Boolean decompositions. The next evidence gate is an explicit sourced factor/receipt transition law, or a proof that the separate factor states in this witness cannot both occur. Until then, mask-switch prediction remains **OPEN**, and physical promotion stays **0**.
