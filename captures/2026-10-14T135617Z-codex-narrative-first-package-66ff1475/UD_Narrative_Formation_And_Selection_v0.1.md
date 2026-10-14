# UD narrative development: why do structures endure and grow?

14 October 2026 · Development — no registry entry · Physical promotion: 0

## The next chapter — public draft

A world of changing states also contains recognizable things. A structure can carry activity, exchange with its surroundings, and remain identifiable through those exchanges. UD asks what conditions make that possible.

The first step is to distinguish a possible structure from an enduring one. Geometry specifies an arrangement and its available connections. Dynamics determines what happens within that arrangement. A persistence test asks whether a chosen property survives for a stated duration and under stated disturbances.

Different arrangements can support different behaviour. A shared face creates one pattern of coupling; a shared edge creates another. Calculating these differences gives shape a functional role. It lets us ask which arrangements transmit, isolate, recur, or make particular distinctions accessible.

But explaining the function of a shape is only one part of explaining its existence. If we begin with a tetrahedral complex, we can calculate its behaviour. To explain how that complex forms, we need rules that change the arrangement itself: rules for attachment, separation, replacement, or reconstruction.

This is the next causal question for UD. Under the same opportunities and resource constraints, which configurations are produced, which survive, and which can grow through further interaction? A long-lived structure may be rare because it is difficult to form. A frequently produced structure may disappear quickly. Growth requires both an available attachment pathway and a way to preserve the resulting assembly.

Coherent agreement can be investigated as one ingredient. Compatible phases or boundary states may enable particular exchanges. Whether that compatibility stabilizes a connection depends on the actual coupling and update rule. Agreement becomes explanatory when the model shows how it changes formation, survival, or growth.

This gives the narrative three connected questions. How is a structure generated? How does it retain its identity? How can its behaviour leave an accessible record? Each question requires a mechanism, and each mechanism can be tested within a declared model.

UD's ambition is to connect those mechanisms within a common framework. Its immediate task is to demonstrate the connections in small systems where the states, interactions, and outcomes can be inspected. The larger physical account must grow from those explicit results.

## A sharper central thesis

UD investigates whether constrained interactions can explain the formation of persistent structures and readable records, using tetrahedral packet complexes as a candidate mathematical architecture.

This thesis adds formation to the previous narrative without claiming it has been derived. It provides a place for coherent motion, shape-dependent function, event counting, and memory while retaining a clear causal question.

## Mathematical boundary: the fixed flow does not select an attracting state

Declare a fixed finite complex K and the unit-metric real flow \(\dot x=B_Kx\), with \(B_K^{\mathsf T}=-B_K\). For any two solutions,

\[
\frac{d}{dt}\|x(t)-y(t)\|^2
=2(x-y)^{\mathsf T}B_K(x-y)=0.
\]

Thus the evolution preserves distance. It cannot bring distinct states closer together in the full Euclidean state space.

In particular, if \(a\in\ker B_K\) is a fixed point, a different initial state cannot converge to a: its distance from a is constant. More generally, for an invariant subspace S, orthogonal evolution preserves distance to S. Therefore it cannot make states outside S approach S.

This does not rule out persistent modes, recurrence, localization under a chosen observable, or transient clustering in a projection. It rules out attraction to these fixed points or invariant subspaces under this specific full-state flow. It also does not apply unchanged to added nonlinear or open-system dynamics.

There is a separate and simpler formation boundary: K is a fixed parameter here. There is no topology-update variable, so this equation cannot perform attachment, deletion, or a 2-to-3 move. Formation is absent from the declared rule rather than a result hidden in its spectrum.

## Mathematical boundary: a spectrum does not determine shape preference

Suppose two candidate complexes A and C each have declared internal flows. Add a configuration label \(\kappa\in\{A,C\}\). To make configuration selection explicit, one possible illustrative extension is a switching process with positive rates \(r_{A\to C}\) and \(r_{C\to A}\). Its stationary probabilities are

\[
\pi_C=\frac{r_{A\to C}}{r_{A\to C}+r_{C\to A}},\qquad
\pi_A=\frac{r_{C\to A}}{r_{A\to C}+r_{C\to A}}.
\]

Holding both internal flows unchanged, rates proportional to 3:1 give \(\pi_C=3/4\), while rates proportional to 1:3 give \(\pi_C=1/4\). These are two mathematical extensions with opposite preferences and the same within-configuration spectra.

This is an underdetermination demonstration, not a proposed native selection law. A complete switching model also needs a state-transfer rule between the carrier spaces, especially when their dimensions differ. Nothing here supplies that transfer, its resource cost, or its physical interpretation.

The conclusion is specific: internal spectra alone do not fix configuration occupancy in this extension class. A selection claim needs an independently specified configuration-changing mechanism. The fractions above demonstrate freedom; they are not UD coefficients.

## Turn the shape intuition into explicit questions

| Intuition | Operational question | Required definition |
|---|---|---|
| Shapes have different functions | How does a fixed input produce different outputs on different complexes? | Comparable preparation, coupling scale, readout, and resource limits |
| Moving patterns have meaning | Which observable distinguishes patterns or predicts an outcome? | Observable map, history window, and prediction criterion |
| Agreement enables persistence | Does compatibility alter survival under a declared interaction? | Compatibility score and a source-derived effect on dynamics |
| Some shapes are preferred | Are those configurations more likely under the same formation process? | Configuration updates, transfer maps, and initial ensemble |
| Clusters grow | Does attachment produce assemblies that remain viable? | Attachment/detachment rule, capacity, and resource accounting |

## Define persistence without assuming the answer

Choose an observable O, a tolerance epsilon, a duration T, and a stated class of disturbances. Define a survival event in which a structure's diagnostic property remains within the acceptable set over the entire interval. For a declared initial ensemble and disturbance law, the survival probability can then be compared across candidate configurations.

The acceptable property could be retained source distinguishability, bounded leakage, a phase relationship, or a receipt that remains valid. These choices answer different questions; they should not be merged into a single unqualified persistence score.

For growth, declare the attachment operation and test the survival of its output against the same criterion. A favourable survival score does not establish that attachment occurs often. Formation probability, survival probability conditional on formation, and further-growth probability must be recorded separately.

## Where this fits in the public presentation

Use the chapter sequence:

1. Why differences that last are the organizing problem.
2. What a tetrahedral complex makes explicit.
3. How dynamics carries a distinction — the two-cell worked example.
4. Why shape changes function, and what is required to explain formation.
5. How an accessible distinction becomes a retained record.
6. What connects finite constructions to physical observables.

Each chapter should lead with a question and an example before formal notation. Put detailed proofs and source histories in linked technical material. Keep current results and proposed extensions visibly distinct.

## Source boundary and provenance

The supplied carrier-definition and master-theory Markdown files are reconstructed placeholders. They do not substantiate a native formation law.

The supplied historical Gap 2 status report describes nonlinear growth and clustering and quotes simulation-fit values. It does not supply, within that report, the complete update law, initial conditions, code, or data needed to reproduce those claims. Its numerical confirmation language is treated as a historical report, not as a new proof or a present physical identification.

The supplied v0.39 ledger itself scopes the genesis fit to historical simulation protocols and keeps physical promotion at zero. Accordingly this chapter does not reuse a fitted convergence rate as a native shape-selection coefficient, and makes no contemporary cosmological-observation claim.

The fixed-flow proof is derived directly from the declared skew condition. The switching calculation is an illustrative counterexample to uniqueness. Both belong to development; no registry status is advanced.

## Next source obligation

Recover one complete configuration-changing rule, including its state transfer and resources. Prefer a small, inspectable formation example over additional fitted constants. If no such native rule is available, keep formation as an explicit open chapter and use the existing fixed-complex calculations to explain function and information access.
