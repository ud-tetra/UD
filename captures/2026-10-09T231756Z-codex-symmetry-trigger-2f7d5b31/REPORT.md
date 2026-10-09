# UD localized mask trigger: symmetry and event-address audit v0.1

**Date:** 9 October 2026 UTC. **Status:** exact conditional structural theorem; trigger law open. **Physical promotion:** 0. Constructor checks only; independent review pending.

## Source boundary and question

The provenance ledger Q156 gives the hard edge predicate \(h_e=C_{{\rm cl},e}^{\rm hard}T_{{\rm int},e}^{\rm hard}\); Q167 and Q173 give typed edge- and face-mask effects. Neither specifies which particular edge/face changes at a primitive event. The [mask decision capture](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-09T183221Z-codex-hard-mask-72ae8f01) and [predictive record capture](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-09T231315Z-codex-predictive-record-8e45dc2b) separated that missing event map from the conditional 22-coordinate amplitude quotient and Boolean factor memory.

This audit tests a necessary **covariance** condition for any future deterministic, local switch selector. It does not claim UD admits such a selector.

## Carrier symmetry and exact mask census

Let \(K=\langle0123,0124\rangle\). Its unlabeled simplicial automorphism group is \(G=S_3\times S_2\), order \(3!2!=12=2^2\cdot3\): permute the shared triangle vertices \(0,1,2\), and optionally exchange apices \(3,4\). It acts on the nine edges and seven faces by relabeling.

| Objects | Automorphism orbits | Orbit sizes | Invariant binary masks |
| --- | --- | --- | ---: |
| Edges | Three shared-triangle edges; six triangle-to-apex edges | 3, 6 | \(2^2=4\) |
| Faces | Shared face 012; six private faces | 1, 6 | \(2^2=4\) |

A binary mask is fixed by all relabelings exactly when it is constant on each orbit. Distinct invariant edge masks differ on 3, 6, or 9 edges; distinct invariant face masks differ on 1, 6, or 7 faces. The singleton shared face is an important exception: its one-face switch is symmetry-compatible.

## Conditional no-go and constructive escape

Let \(F\) be a deterministic mask-update function equivariant under \(G\): \(F(gx)=gF(x)\). If its complete input \(x\), including the pre-mask and all event data it is allowed to read, is fixed by \(G\), then

\[
gF(x)=F(gx)=F(x)\quad\text{for every }g\in G.
\]

Thus the next mask must be invariant. In particular, **no exactly one-edge switch can be selected from a fully symmetric input by such a rule** on this carrier. The proof does not forbid a whole three-edge orbit switching, nor does it forbid an isolated shared-face switch. The uniform vertex 0-chain \(N\), with all five vertex coefficients 1 and all higher coefficients 0, is an exact nonzero \(G\)-fixed native null mode. An all-open or all-closed pre-mask is also fixed. These supply a concrete symmetric input sector; the future event must itself be symmetric for the theorem to apply.

The obstruction disappears when the input includes a typed address. An edge-marked defect \(\delta_e\) transforms to \(\delta_{g e}\); the selector \(F(\delta_e)=\delta_e\) is covariant and picks exactly one edge. The replay verifies all \(9\times12=108\) address/relabeling cases. A nonuniform amplitude can likewise carry an address if an admissible law actually reads it. This theorem does **not** demand extra memory bits universally; it demands a source of asymmetry when a localized event is claimed from otherwise symmetric data.

For the separately declared candidate complete-boundary face lift \(h_f=\prod_{e\subset f}h_e\), the four invariant edge masks map to only three face patterns \((h_{012},h_{\rm private})\in\{(0,0),(1,0),(1,1)\}\). The invariant independent Q173 face family also allows \((0,1)\). This difference is evidence that the AND lift is an added restriction, not a source-complete Q173 selector.

## Replay and next source test

Run `python3 verify.py` in this release directory. Standard-library exact enumeration checks all 12 carrier automorphisms, all 512 edge masks, all 128 face masks, orbit transition supports, the native null mode, the 108 typed-address covariance cases and the candidate face-lift restriction. **18 named assertions pass.** These are constructor checks, not independent verification.

**EXACT / CONDITIONAL:** equivariance forces orbit-constant output at a symmetric complete input. **NO-GO for that premise:** deterministic one-edge switching. **OPEN:** source-selected primitive event address or symmetry-breaking input; factor update dynamics; face-event relation; event ordering and timing. Physical promotion remains 0.

The next candidate source contract must say what carries a local edge/face address (a tagged defect, a transport failure localized to a declared edge, or another typed datum), how that address is obtained **before** the switch, and how it transforms under relabeling. A source map should then update \((C,T)\), issue a pre/post receipt, and be replayed on nonsymmetric as well as symmetric states. A selected edge in a retrospective receipt is not automatically a prospective address.
