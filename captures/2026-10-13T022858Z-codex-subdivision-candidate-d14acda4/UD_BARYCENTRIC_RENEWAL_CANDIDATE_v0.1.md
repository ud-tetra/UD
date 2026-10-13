# UD barycentric renewal candidate and exact gate review v0.1

**13 October 2026 UTC · development, no registry entry · physical promotion 0.** Constructor and adversarial self-review: Codex. No non-constructor review. This is a proposed rule deliberately tested *before* reusing the conditional spatial symbol in [capture v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T020255Z-codex-spatial-symbol-753fe949/UD_SPATIAL_REFINEMENT_SYMBOL_v0.1.md). It responds to the [source gate v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T021320Z-codex-native-refinement-212e6436/UD_NATIVE_REFINEMENT_SOURCE_GATE_v0.1.md), which found no accepted native mesh/refinement selector.

## 1. Sources and status

- [UD Paper I, review draft 1.1.1, §§1, 4, 6.1, 6.5, 7.4, 8.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md): each supplied finite oriented 3-complex has unique-simplex real chain carrier, unit Euclidean pairing and `A_K=B_K^T−B_K`; the paper does not source geometry creation, jump, timing or admission.
- Supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q25–Q26 and Q169–Q170: unit global skew carrier is separate from open state-dependent edge weights and routing source. Supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, §§1, 3–6, is a proposal; independent non-constructor review and custodian ruling would be needed for registry promotion.
- **Imported ingredient:** ordinary barycentric subdivision `sd(K)` is a standard combinatorial operation, not a UD-derived event or force. Defining it here does not grant it source authority. A compact historical/research attachment `Gap2_FINAL_Finite_Genesis.png` could not be inspected; re-upload if it supplies a move law.

## 2. Declared candidate state/evolution/renewal

Let `K_n` be an oriented finite tetrahedral triangulation of a compact *supplied* 3D domain, geometrically realized in a dimensionless Euclidean chart; for the exact replay start with one simplex `[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]`. Let `c_n∈C_•(K_n;R)` and a prepared, external integer renewal address `n`. Between renewals evolve by `dc_n/ds=A_{K_n}c_n`, with specified starting `c_0`, inherited boundary condition on the outer surface, no forcing and conserved unit chain norm. No physical seconds or lengths are assigned to `s` or to the chart.

**CANDIDATE R1 (synchronous):** At the supplied renewal address, mark all top tetrahedra together, set `K_{n+1}=sd(K_n)`, identify shared barycenters only once, pass the declared state through one of the two transfer choices below, increment `n`, and resume the new fixed-complex flow. Face histories are batch-synchronous; there is no exclusive tie. Geometric legality holds for a triangulated domain and the rule is equivariant under vertex relabeling. A local state predicate, source of renewal addresses, energy/reservoir, and physical clock are absent. The trigger `n→n+1` is an explicit external input; replacing it with “closure holds” would be tautological because `B²=0` already holds for every simplicial complex in the declared domain.

For an oriented `k`-simplex `σ=[v_0…v_k]`, standard chain subdivision `S_kσ` is the signed sum of the `(k+1)!` complete barycentric flags of its nonempty faces. Each descendant oriented simplex has coefficient `±1`; supports from two distinct old basis `k`-simplices do not overlap in grade `k`. The two proposed transfer paths are:

| Transfer | Domain → codomain | Declared aim |
|---|---|---|
| `S=⊕_k S_k` | `C_•(K_n)→C_•(sd K_n)` | Preserve simplicial boundary and exterior chain |
| `T=⊕_k S_k/√((k+1)!)` | same | Preserve the source's unit Euclidean chain norm |

Both are mathematical *candidate* state jumps, not native UD dynamics. No interpolation, thermodynamic resource, or physical correspondence is inferred.

## 3. EXACT geometry scaling and local overload

Each old tetra produces `4!=24` distinct children. A tetra incident to a fixed old corner produces `3!=6` children still incident to that corner. For an initial tetrahedron, therefore, `N_n^{tet}=24^n` and the number of tetrahedra incident to the original corner is `6^n`. Every incident tetra has a distinct barycenter adjacent to the corner in the next subdivision, so its graph degree `d_{n+1}≥6^n`; the degree is unbounded. The exact rational construction in `verify.py` gives:

| `n` | Tetrahedra | Vertices | Degree at old corner | Incident tetrahedra |
|---:|---:|---:|---:|---:|
| 0 | 1 | 4 | 3 | 1 |
| 1 | 24 | 15 | 7 | 6 |
| 2 | 576 | 149 | 25 | 36 |
| 3 | 13,824 | 2,745 | 121 | 216 |

For nested faces `A⊂B` in a parent simplex of diameter `D`, `b_B=(|A|/|B|)b_A+(|B|-|A|)/|B|·b_{B\setminus A}`. Hence `|b_B-b_A|≤(3/4)D` in dimension three. Each child edge joins barycenters of nested faces, so the maximum cell diameter `h_n≤(3/4)^n h_0→0`. This is a controlled shrinking *supplied geometric chart*, not a dynamically selected length. The bound does not establish uniform tetrahedral aspect ratio or bounded-degree spatial operators.

## 4. EXACT state-transfer obstruction for the natural maps

The standard subdivision chain map satisfies `∂S_k=S_{k-1}∂`, but with Paper I's unit simplex basis,

\[
\|S_k e_σ\|^2=(k+1)!\qquad(k=0,1,2,3),
\]

giving `1,2,6,24`. Its supports on distinct original same-grade simplices are disjoint. Consequently `||S c||²=Σ_{k=0}^3(k+1)!||c_k||²`: the conserved source support increases at renewal for every state with nonzero higher-grade content. Thus `S` fails the unsourced norm-preserving-jump requirement, except for a vertex-only input or an explicit reservoir/exchange model.

The scaled transfer `T_k=S_k/√((k+1)!)` is an isometry on the whole graded chain carrier, but

\[
\partial T_k={1\over\sqrt{k+1}}T_{k-1}\partial\ne T_{k-1}\partial
\]

on a simplex with nonzero boundary in grade `k≥1`. On a single edge `[a,b]` with barycenter `m`, `S_1[a,b]=[a,m]+[m,b]` has squared norm `2` and boundary `[b]-[a]`; `T_1` has norm `1` but boundary `([b]-[a])/√2`. This is a complete one-edge obstruction to the joint contract of **boundary-fixed original endpoints, chain compatibility and Euclidean isometry** on that edge, where no alternate path exists. It does not prove all more general state-transfer maps impossible on a full tetrahedral complex or an enlarged reservoir carrier.

Moreover `S` does not intertwine the full skew generators: on that edge `A_{sd K}S_0[a]=-[a,m]`, whereas `S_1 A_K[a]=-[a,m]-[m,b]`. A jump may legitimately change generators, but it must specify the resulting energy/support accounting and restart rule; chain compatibility alone cannot be called dynamic equivalence.

**NO-GO under R1 with native unit support and the two declared maps:** neither standard `S` nor grade-normalized `T` meets simultaneously norm conservation, chain compatibility and same-law generator intertwining. A prescribed age/tick is not a state-dependent UD admissibility source. `d_n→∞` invalidates the previous report's *bounded-degree sufficient gate* for this candidate; it does not alone refute all possible continuum convergence with appropriate mass weights or weak limits.

## 5. Constructor adversarial review and next decision

| Challenge | Result | Status |
|---|---|---|
| Does R1 choose a 3D cell family without label bias? | Canonical global `sd`, relabeling equivariant | **EXACT conditional geometry** |
| Does it give `h_n→0`? | `h_n≤(3/4)^n h_0` for supplied Euclidean embedding | **EXACT conditional** |
| Is admission determined by the UD pre-event state? | External renewal address; no source predicate or timing | **NO-GO for native admission** |
| Is transferred chain state both unit-norm and boundary-compatible? | `S` fails norm; `T` fails boundary | **NO-GO for declared transfers** |
| Are degree/shape and continuum symbol controlled? | Original corner degree diverges; shape and spectral/sector convergence unproved | **OPEN** |
| Is the earlier Freudenthal tensor `C=2I+2J` reproduced? | Different, nonuniform family; Fourier offsets no longer apply | **NO-GO for direct reuse** |
| Is an independent review/promotion receipt present? | Constructor self-review only | **OPEN**, physical promotion 0 |

**Disposition:** Preserve R1 as a **CANDIDATE** and freeze any claim that it establishes a UD-native Lorentzian metric. The successful result is a precise discriminating obstruction. A successor needs a source-authored event trigger and a typed state transfer (possibly with an explicit support reservoir), then a controlled weighted/mass-normalized continuum analysis on the actually selected family. Any target-blind candidate must list its new weights and units as assumptions until the current Q25/Q26 source gap closes. Do not treat a merely relabeling-symmetric subdivision as a prediction of when the universe refines.
