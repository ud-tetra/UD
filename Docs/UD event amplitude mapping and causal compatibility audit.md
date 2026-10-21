The proposed BCC wave update cannot be obtained from the current binary cell and readiness state alone if preparations leave amplitude unchanged and every commit advances that update once. Under those assumptions, only stationary harmonic amplitudes survive. Retained history removes this recurrence obstruction, but a history mapping must also preserve source locality, independent event order, conserved support, and recording semantics.

This audit provides conditional proofs, exact countermodels, and a limited positive construction. The replay passes **150 exact checks**, with no floating-point tests. It checks all 160 two-commit control cases and all 192 independent leaf-swap cases on a five-cell source witness; all 24 orders of four independent leaves followed by their center; the full 26-coordinate amplitude obstruction at eight sign characters; and rational amplitude, conservation, and capacity certificates. These checks verify the stated contracts and derivations. They do not establish a native physical mechanism. Physical promotion remains 0.

## Current source and target

The current minimum time model v0.11 was read from its retained file for this continuation. It selects a candidate binary decoration x on tetrahedral cells, four readiness predicates per cell, zero-weight face preparations, and one atomic flip and reset per completed cell commit. Its retained implementation uses complete observed stars, nonwrapping edge versions, coherent receipts, and active buffers that can inhibit commits. The full inspected source baseline and prior amplitude audit are pinned in the release index.

The amplitude target is the previous proposed kick-and-drift update Tδ on real chain coordinates, using δ=1/8 for the full branch. This is a computational comparison law; its parameter is a declared resolution control. The source does not identify a cell commit with this update, choose an amplitude launch, or calibrate a duration.

At the real scalar character q=(π,0,0), the native singular frequency is 4. In its normalized two-coordinate sector the exact target is:

```text
M = [[3/4, -1/2],
     [1/2,    1]]

H = [[1,   1/4],
     [1/4,   1]]

Mᵀ H M = H
det(M) = 1
trace(M) = 7/4
```

The illustrative launch is ψ=(1,0). This supplied launch is used to distinguish mappings; it is not a newly derived source state. The prior scalar impulse preparation and continuum clock are not changed by this audit.

## Current control mapping theorem

Consider any map Φ(x,R) from current binary cell and readiness control to the real target amplitudes. It need not be linear. Add the following two assumptions locally:

1. Every face preparation leaves Φ unchanged.

2. Every admissible cell commit changes Φ to TδΦ, using the same target step for every actor.

Preparation can complete any readiness set without changing x. Therefore Φ(x,R)=φ(x), where φ is its value at full readiness. A commit at actor v followed by re-preparation of that actor gives:

```text
φ(x + e_v mod 2) = Tδ φ(x)
```

Two such cycles return x and readiness to their starting values. Hence φ(x)=Tδ²φ(x). In a nonzero singular-frequency sector σ, Tδ has determinant 1 and trace 2-δ²σ². For 0<δ²σ²<4:

```text
det(Tδ² - I) = δ²σ² (4 - δ²σ²) > 0
```

Thus every nonstationary sector of φ must vanish. The surviving image lies in the harmonic kernel of the original generator. For the exhibited scalar pair, det(M²-I)=15/16. For the full system, exact rank checks show an eight-dimensional allowed kernel at q=0 and a zero-dimensional allowed kernel at each of the seven nontrivial sign characters. The singular-pair proof applies at every stable wavevector; at generic nonzero wavevectors the prior full-mode audit supplies no harmonic sector.

This excludes the specified current-control mapping for propagating amplitudes. It does not exclude amplitude changes during preparation, a different target update, history or version dependent mappings, other event groupings, or additional state. Zero event weight alone does **not** imply amplitude invariance: the source explicitly says readiness affects future enablement. If preparations move amplitudes, that motion and its conservation law must be supplied, and commit count alone will not describe all amplitude changes.

The theorem also does not erase readiness from the source dynamics. A map that ignores readiness may match selected amplitudes while losing the distinction between enabled and disabled continuations. An actual causal correspondence must preserve that distinction through its state or its gating contract.

## A history encoding exists but does not derive the law

For a supplied ψ and target Tδ, define Φ(h)=Tδ raised to N(h), applied to ψ, where N is source commit activity. This exactly intertwines preparation with identity and commits with Tδ on mathematical histories. It conserves the target's modified support. Because h or N distinguishes recurrent occurrences, the current-control theorem no longer applies.

This construction encodes an independently chosen wave law into the event history. It does not infer that law from the source. It also loses spatial distinctions between actors when it applies the same global step to every commit.

For two disconnected source components, each satisfying the identifying-graph condition, take a comparison target with two uncoupled copies of M. A commit in component A must leave an amplitude observable belonging only to component B unchanged if the mapping is to respect that component locality. A global activity clock instead applies diag(M,M). Starting from ψ in both components, a commit in A changes the B spectator from (1,0) to (3/4,1/2), despite no B event or target coupling. This is an exact counterexample to that mapping's locality. It is conditional on the declared association of each target copy with its source component; it is not a claim that every history encoding must fail.

## Source concurrency gives an amplitude ordering condition

The replay constructs an abstract tetrahedral complex with central tetrahedron {0,1,2,3} and one neighbor across each of its four faces, each neighbor using its own new vertex. It is pure, has at most two cells incident to any face, and its full dual graph is a five-cell star. The observed component has size five, and its actor signatures are nonempty and distinct. No Euclidean embedding of this witness is required or claimed.

Its four leaves use disjoint observed-edge slots and can commit independently under the inspected protocol. Their receipts have no parents. After the leaf receipts release their slots, the center can commit with those four leaf events as parents. All 24 leaf orders produce exactly the same retained receipt set, actor signatures, parent structure, field, and readiness cut. There are five events and causal depth two.

If amplitudes depend only on this retained causal object, rather than an additional ordering record, independent source events must satisfy the amplitude diamond condition:

```text
U_v U_w Φ(E) = U_w U_v Φ(E)
```

This equality is required on the admitted image of Φ. Full-space operator commutation is a sufficient condition, not automatically necessary. An added serial schedule or a restricted image could change the obligation, but neither may be silently supplied by a choice of replay order.

## The proposed overlapping assignment fails two gates

As a deliberately tested comparison, assign M to coordinates (0,1) for one leaf event and to (0,2) for another, leaving each unused coordinate fixed. Both assignments reuse the prior target coefficients. They share coordinate 0 although their source events are independent. With launch (1,0,0):

| Source order | Final amplitude |
| --- | --- |
| Leaf 1 then leaf 2 | (9/16, 1/2, 3/8) |
| Leaf 2 then leaf 1 | (9/16, 3/8, 1/2) |
| Difference | (0, 1/8, -1/8) |

The identical causal source record yields different amplitudes, so this assignment fails the ordering condition on that launch. It also fails conservation more strongly than merely changing the original norm: the exact linear system for a symmetric 3 by 3 matrix Q satisfying both U1ᵀQU1=Q and U2ᵀQU2=Q has rank six in its six unknowns. Its only solution is Q=0. Therefore these particular two assignments have no shared nonzero quadratic conserved form, including no positive one.

For a direct proof, invariance under the first assignment forces the cross terms between its rotating pair and the unused coordinate to vanish. Its pair metric is proportional to H. Invariance under the second assignment similarly kills the first pair's off-diagonal term, forcing that proportionality constant to zero; the remaining entries then vanish. The exact rank certificate checks the complete equations.

These are failures of a particular actor-to-coordinate assignment. They are not a no-go theorem for every local operator family or for UD. Preserve this assignment as a rejected candidate, with its launch, matrices, failure mode, and replay conditions. A repair must derive a different assignment, justify an image restriction, or explicitly modify the source independence or ordering contract.

## Activity depth and retained counts are distinct

| Quantity at the five-event cut | Value | Consequence for the illustrative target |
| --- | --- | --- |
| Source activity N | 5 | M^5ψ = (-989/1024, 305/512) |
| Maximum causal depth D | 2 | M^2ψ = (5/16, 7/8) |
| Retained global receipts after release | 5 | Equals activity only once all published events are recorded |
| Retained receipts before any leaf recording | 0, with source activity 4 | Does not reveal four already published events |

After one independent leaf commits, D=1. A second independent leaf keeps D=1 while activity rises to two. A depth-only encoding therefore cannot advance M once per commit on this launch. Counting one target step per completed layer instead is a different event grouping; the protocol does not supply a global layer-completion barrier or a conversion to duration.

The buffer test publishes all four leaves before recording any: source activity is 4, retained count is 0, and unrecorded published count is 4. The center is blocked until every pending leaf slot is released. This tests the source balance N=|R|+|U| and preserves recording backpressure. A retained-receipt count used as if it were the source clock advances at the wrong operation unless the delayed observation is modeled explicitly.

For one observer receiving the center receipt before its four parents, received-set sizes 1,2,3,4,5 have parent-closed subset sizes 0,1,2,3,5. A mapping that evolves from causal records must specify whether it accepts such incomplete cuts, waits for their closure, or represents missing state. A receipt's arrival order is not a native global amplitude schedule.

## Memory capacity for a nonrepeating target orbit

M's eigenvalues are stable rotations with 2cos(θ)=7/4. A finite orbit of a nonzero rotating state would require a root of unity eigenvalue. Its eigenvalue plus inverse would then be an algebraic integer. Since a rational algebraic integer must be an integer, 7/4 rules out that finite orbit. This is an exact argument, not a conclusion from finite sampling.

To encode ψ,Mψ,...,M^Hψ exactly and distinguish these H+1 possibilities requires at least H+1 distinguishable total encoding states. A binary encoding needs at least ceil(log2(H+1)) bits for this distinction. If the recurrent cell bit already retains commit parity, the larger parity class still requires floor(H/2)+1 extra states. For H=1000 this means 1001 total distinguishable states, or at least 10 total binary bits; with parity already supplied, at least 501 auxiliary states, or 9 auxiliary binary bits, are needed. These are finite-horizon distinguishability bounds, not physical memory or energy limits. An unbounded exact horizon needs an unbounded number of distinguishable encoding states.

The example also exposes an exact arithmetic cost. Let u_n be the first coordinate of M^nψ and set a_n=4^n u_n. Then a0=1, a1=3, and a_(n+2)=7a_(n+1)-16a_n. Every a_n is odd, so the reduced denominator of u_n is exactly 4^n. The second coordinate has reduced denominator 2^(2n-1) for n≥1. The replay verifies these formulas and conservation through n=64. Explicit integer-fraction storage therefore needs growing precision. A compact phase or counter encoding can represent the same orbit differently, but it adds an encoding and reconstruction contract; the denominator result does not assert a universal linear memory lower bound.

The retained protocol's growing edge versions and immutable receipts provide one possible distinction between recurrent source occurrences. The replay performs two commits and re-preparations at one leaf: binary field and readiness return, while two versioned receipts remain distinct. This demonstrates how history evades the control recurrence. It does not derive amplitude values from those receipts.

## Limited positive construction

For two disconnected source components, use separate component counts N_A and N_B and define the amplitude as M^N_Aψ in A and M^N_Bψ in B. The operators diag(M,I) and diag(I,M) commute, preserve a common block-diagonal H, and leave each spectator unchanged. The replay verifies these properties and a nontrivial count example exactly.

This is a constructive compatibility example for a coarse component association. It does not supply actor locality within a connected component, the BCC chain-to-cell mapping, a native memory implementation, preparation dynamics, a connected propagating field, or a physical clock. It shows that the next source obligation concerns a compatible family of actor operations, rather than the mere existence of a counter.

## Concrete source admission contract

Before claiming an event-derived BCC law, supply a state or history map Φ, a causal cut convention, amplitude operators U_v for commits, any preparation operators P_vf, one conserved form Q, and an explicit event grouping if a stencil step combines commits. Then prove the following within the declared domain:

| Obligation | Required statement | Current result |
| --- | --- | --- |
| State and readiness | Φ includes the information needed to distinguish enabled continuations | Current-control map with unchanged preparations cannot carry target waves |
| Event update | Φ after an admitted commit equals U_v applied to Φ before it | Global activity gives a formal encoding only |
| Source independence | Independent swaps give equal amplitudes on the admitted image | Tested overlapping assignment rejected |
| Locality | Events leave uncoupled, untouched component observables unchanged | Global activity assignment rejected; component construction passes a limited test |
| Conservation | All admitted operations preserve the same Q, or account for declared reservoirs | Tested overlapping assignment has only Q=0 |
| Acquisition and records | Published, retained, and observer-known cuts have an explicit mapping and memory policy | Recording lag and incomplete causal cuts remain material |
| Aggregate wave law | The admitted event schedule produces the target chain update and its BCC long-wavelength structure | Open; no actor-to-primal-chain map supplied |
| Clock and metric | Event grouping, spatial embedding, refinement clock, and any empirical units have independent provenance | Open; no physical correspondence established |

The next bounded target is to find an independently supported face or commit operation that meets the common-conservation and source-independence gates on a connected carrier. If preparation must move amplitudes, its operation must be stated and tested rather than erased. Adding a serial schedule, cross-term metric, or record-based phase solely to reproduce the desired wave law would be a new axiom, with its scope and cost recorded.

## Replay and retained limitations

Run `python verify_ud_event_amplitude_bridge_v0_1.py --out replay_results` with the unchanged macrocell helper beside it. Only Python's standard library is required. The release includes exact results, the source admission contract, rejected-candidate risk records, pinned source snapshots, the report, and a SHA256 manifest. Earlier hash-locked artifacts remain unchanged.

The source interpreter replays a scoped candidate contract; it is not a native mechanism implementation. The five-cell witness is abstract and does not select a metric. The full-mode kernel certificates cover the declared characters, with the general statement supplied by the singular-pair proof. No detector design, empirical calibration, physical experiment, independent review, or canonical source amendment occurred. All statements concern internal mathematics and explicitly supplied mappings; no external physical correspondence is promoted.

## Saved evidence and prior work

[UD_EVENT_AMPLITUDE_INTERTWINER_AUDIT_v0.1.md](library-file:file_0000000080f481f69030bfc579a91059)

[UD_EVENT_AMPLITUDE_BRIDGE_RESULTS_v0.1.json](library-file:file_00000000b2e481f6821717d567e47443)

[UD_EVENT_AMPLITUDE_SOURCE_ADMISSION_CONTRACT_v0.1.json](library-file:file_00000000b2e881f6a7b8a258035a3043)

[UD_EVENT_AMPLITUDE_REJECTED_CANDIDATES_RISK_RECORD_v0.1.json](library-file:file_00000000d79481f68236d1620af41e05)

[UD_EVENT_AMPLITUDE_BRIDGE_v0.1_RELEASE.zip](library-file:file_00000000451c81f6a71450b16920badc)

[UD_EVENT_AMPLITUDE_BRIDGE_v0.1.sha256](library-file:file_00000000dd4881f6ba9434b2439b1cad)

[Previous causal update audit](https://chatgpt.com/space/page_0861ced6d9048191809c73c970dbaea9)