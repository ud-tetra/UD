# Four-face selector recovery and recursion scope audit v0.1

Status: EXACT CONDITIONAL mathematical derivation / development — no registry entry. Constructor verified; independent review pending. Physical promotion: 0.

## Recovered source scope

The captured v0.39 ledger P07–P09 retains the default selector four, dense alternate twelve, and an open branch-generalization gate. The 2026-09-18 branch-ergodicity source, sections 1–2, identifies the default as face-sharing and proves normalized face weights 1/4 in an S4-unbroken closed-cell sector. Chapter 20 explicitly describes default face-sharing versus dense vertex-sharing; it is pedagogical source context, not new canon. The local 3-manifold audit sections 2–3 and 9–12 restrict a proposed ordinary spatial growth rule to boundary faces with one incident tetrahedron; they explicitly forbid identifying dense selector twelve with face top-star multiplicity.

Recovery is partial: these texts identify the default mechanism and its symmetric weights. This search of recovered plain-text UD material and archive member names did not recover the original executable selector for the dense branch or a universal law choosing default over dense. No claim that such a source does not exist elsewhere is made. The topology addendum remains a scoped candidate; this replay assumes its face-use rule, without globally admitting it.

## Conditional result 1: local face channels

A tetrahedron on vertices {0,1,2,3} has precisely four triangular facets, each obtained by omitting one vertex. The 24 permutations of S4 act transitively on those four facets. If each permitted attachment uses one facet and at most one neighboring tetrahedron can use it, the seed has four potential attachment slots.

If normalized weights w_f are invariant under this S4 action, all weights coincide and sum_f w_f=1 forces w_f=1/4. Enumeration below checks the action and orbit; the transitivity argument proves uniqueness. Face weights and vertex capacity allocation are distinct objects despite equal 1/4 values. A correspondence between them still needs a source map.

This establishes local cardinality and conditional weighting. It does not show that all slots are occupied, that all are equally likely when symmetry is broken, or that face-sharing is preferred to another branch by physical dynamics.

## Conditional result 2: fresh-vertex boundary attachment

Declare a finite abstract simplicial complex of tetrahedra. Attach one new tetrahedron along an existing boundary triangle using a globally fresh fourth vertex. The selected triangle changes from boundary degree one to interior degree two. The three remaining triangles are new boundary faces, since each contains the fresh vertex. Thus one attachment changes cell count T by +1, interior face count I by +1, and boundary face count B by +2.

Starting from one tetrahedron and repeating only this operation yields

\[
I=T-1,\qquad 4T=2I+B,\qquad B=2T+2.
\]

The dual cell graph is a tree: every new cell attaches to exactly one older cell, and no other shared triangle is possible with the fresh vertex. Its root has up to four outward slots; each attached cell has one parent face and three unused outward faces. The total number of incidences four is not the number of new children at every depth.

For synchronous full-frontier expansion, attach once to every boundary triangle present at the beginning of each round. New faces wait until the next round. Then

\[
T_{n+1}=T_n+B_n,\quad B_{n+1}=3B_n,\quad
T_0=1,\ B_0=4,
\]

so

\[
T_n=2\,3^n-1,\qquad B_n=4\,3^n.
\]

| Round n | Cells T_n | Boundary triangles B_n | Interior triangles I_n |
|---|---|---|---|
| 0 | 1 | 4 | 0 |
| 1 | 5 | 12 | 4 |
| 2 | 17 | 36 | 16 |
| 3 | 53 | 108 | 52 |
| 4 | 161 | 324 | 160 |

This is an exact recurrence for the declared combinatorial operation. It is not a general recursion law for UD exposure counts. In particular, T_n counts cells, B_n counts frontier triangles, and N2=G1 N1 is a branch-specific exposure count. No map identifying these quantities is established here.

The boundary count twelve at round one is numerically equal to G1_dense=12. The carriers and derivations differ; the equality supplies no dense-selector derivation. No universal twelve-neighbor result or regular tetrahedral Euclidean tiling is claimed.

## Scope controls

Reusing an interior face is rejected by the declared boundary-only operation. Allowing an existing apex can create other shared interfaces and cycles, invalidating the fresh-vertex derivation. Non-manifold, event-space, internal-fiber and other admitted dimensional sectors require their own rules. No continuum metric, physical packing, stable-cluster preference, clock or support survival has been established.

## Gap disposition and next work

Closed within declared scope: four-facet enumeration, symmetric face weighting, fresh-vertex boundary recurrence and reproducible finite checks.

Still open: original dense-branch selector, general branch-selection dynamics, Theta reference-state exclusion predicate, face-to-vertex capacity map and recursive exposure semantics. The next useful source audit is to recover the predicate distinguishing the single excluded Theta state; simply removing a bitstring by convention would not close it.

No ledger row is overwritten or promoted by this capture. It supplements the earlier 7/768 audit. The governance CRL-2 subdivision attachment labels itself a proposal; it is not silently adopted. Constructor replay is not independent review.

Gap2_FINAL_Finite_Genesis.png was unavailable and was not read or used.
