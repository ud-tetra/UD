# UD-PM-PRED06-SEL-002 v1.0 — Conditional local burden/flux seed and port selector

**Kind:** LEMMA (positive conditional construction). **Status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0.

## Source and new assumptions

Source: ledger v0.39 Q156 gives the *hard* link factor \(h_e=C_e^{\rm hard}T_e^{\rm hard}\), and Q162 gives conditional relaxational burden flux \(j_e=-\frac14h_e(\partial_1^\mathsf Tb)_e\). Q153 leaves the constitutive source law open. The comparison predicate and threshold below are **new assumptions**, not an AUTO_LOCK rule imported from the source. In particular, the numerical structural capacity \(7/768\) is **not** inserted as a burden threshold.

Let \(K_4\) have real site loads \(b_v\), binary typed hard contact permissions \(h_{\{u,v\}}\in\{0,1\}\), and an arbitrary declared threshold \(\tau\in\mathbb R\) in the same native burden units as \(b\). For a vertex \(v\) and outgoing oriented contact \(v\to w\), define the Q162-based directional current
\[
J_{v\to w}:=\tfrac14 h_{\{v,w\}}(b_v-b_w).
\]
Define the *candidate decision predicate* \(S(v)\) by \(b_v>\tau\) and \(b_v>b_w\) for every neighbor \(w\). If exactly one \(v\) passes and exactly one incident contact maximizes strictly positive \(J_{v\to w}\), output the pair \((v,w)\); otherwise output HOLD. No global coordinate or fixed vertex ID appears in this rule.

## Lemma

On one full K4, the rule is graph-local, invariant under changes of edge orientation convention, and \(S_4\)-equivariant. If there is one burden maximum strictly above \(\tau\), and among its incident open contacts exactly one carries the greatest positive outward burden current, the rule selects one seed and one port. If the burden is fully uniform, all contacts close, or the maximum-current outgoing ports tie, the rule returns HOLD rather than breaking symmetry using hidden labels.

**Proof.** Every vertex can evaluate \(S(v)\) from its own load and three adjacent loads. On complete K4, two distinct vertices cannot both be strict maxima against each other, so at most one seed is selected. The current formula is the Q162 current expressed in the outgoing direction: reversing the global edge orientation reverses both incidence gradient and current sign, leaving physical outward current unchanged. A unique positive maximizer defines a unique incident port. Every ingredient is a scalar, an incident relation, or a typed contact mask, so relabeling the K4 vertices by any permutation relabels the output by the same permutation. Uniform or tied inputs fail strictness and produce HOLD. QED.

## Exact witness and limitations

For \(b=(4,3,2,0)\), \(\tau=0\), and all six gates open, the unique seed is vertex 0. Its outgoing fluxes are \(1/4,1/2,1\) toward vertices 1,2,3 respectively; hence its selected port is \(0\to3\). The \(24\) relabeled examples produce exactly relabeled outputs. This proves a mathematical conditional selector, not an autonomous source generator.

**Important limits:** On a general multi-packet graph, multiple separated strict local maxima may coexist; K4-local uniqueness does not imply global one-defect uniqueness. A supplied current/permission does not determine when a cell is excised. The source laws Q153 and Q156 do not produce \(b=(4,3,2,0)\), choose \(\tau\), or force the topology-changing update. Nor does this scalar selector yield a canonical integer winding lift or physical clock. The full endogenous source requirement remains OPEN_GATED.
