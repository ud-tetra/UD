# UD-PM-PRED04-CAUSAL-003 v1.0 — Immediate-excision live-edge propagation obstruction

**Proof kind:** NO_GO / explicit update-order counterexample  
**Evidence:** EXACT_CONDITIONAL, finite constructed witnesses  
**Review:** DEFERRED  
**Physical promotion:** 0  
**Source:** UD PR #479 head `b5c8146ae4b956279e6f399553e02cffbc42c7ea`, `UD_PRED01_LOCAL_DEFECT_SELECTION_AND_BOUNDED_SOURCE_v0.4.md`, L1–L3 in §2, source implementation `native_defect_and_readout.py` functions `source_prop` and `build_complex`.

## A. Objects and hypotheses

Let `K` be a pure finite 3-dimensional simplicial complex made of K4 tetrahedra. Let a unit token occupy a vertex `v∈K` and have a preferred neighboring vertex `w` joined by an edge `(v,w)`. Assume the following **online** update order at a given time step:

1. Excise **all** tetrahedra containing `v`.
2. Keep only faces and lower-dimensional simplices supported by the surviving tetrahedra; delete unsupported vertices/edges.
3. Transfer the same token along a live edge of the *remaining* complex from `v` to `w`.

The token has no alternative control graph and the transfer is not permitted to occur before the excision. These additional sequencing and support restrictions are essential to the NO-GO statement.

## B. Theorem and proof

**NO-GO:** Under A, step 3 is impossible for every occupied `v` (regardless of the local topology of `K`).

*Proof.* After deleting all tetrahedra containing `v`, no surviving tetrahedron contains `v`. Every retained edge and vertex is, by assumption, a subface of some surviving tetrahedron. Therefore `v` is not a vertex of the updated complex; in particular no edge with endpoint `v`, including `(v,w)`, survives. Consequently there is no live edge incident to the token site along which step 3 can act. ∎

## C. Relevance to PR #479

The source implementation `source_prop` first constructs the full token trail on the original graph. Separately, `build_complex` then removes all tetrahedra incident to the marked trail vertices. The code therefore **does not implement** the blocked online schedule (excise current support, then transfer on the surviving graph), and should not be read as having proved autonomous propagation on the changing K4 complex.

A finite independent Freudenthal construction at `N=4,6,8` confirms that when only the bottom seed is excised, the seed vertex and its outgoing vertical edge are absent from the supported 3-complex. The remaining complex also retains `β_1(F_2)=0` in these examples: a single seed excision alone need not create the completed tunnel.

## D. Legitimate reopening branches

1. **Transfer-before-excision:** define an explicit sequential generator where the token moves along the intact edge and the vacated site is then excised. Require a proof that future moves remain available and stock is conserved.
2. **Separate persistent control graph:** source labels and transport may evolve on a different carrier while the K4 geometric complex is pruned. This is permitted but must be typed, coupled and independently specified; it is not purely live-edge transport on the remaining complex.
3. **Retained faces/edges outside surviving tetrahedra:** change the pruning contract to keep a control skeleton. This alters the original carrier and may alter its topology/homology and action.
4. **Simultaneous nonlocal update:** mark/propage an entire path before topology changes. This restores the original implementation but does not establish a strictly local *online* selector.

The NO-GO does **not** say local source dynamics are impossible under all mechanisms. It only excludes the precise excision-before-transfer rule with pure surviving-3-simplex support and live-edge-only transport.

**Proof status:** VERIFIED_SCOPED EXACT_CONDITIONAL NO_GO. **External review:** DEFERRED. **Physical promotion:** 0. **Next gate:** construct and formally verify a conservation-preserving coupled state machine with specified transfer/excision ordering and recovery law.
