# THM-534 source-law recovery gate: S4 classification, Markov nonuniqueness and a forward control
**Version:** v0.2 | **Date:** 2026-10-21 | **Status:** EXACT mathematical obstruction + OPEN microscopic source law | **Lane:** development, no registry promotion | **Physical promotion:** 0

**Parent capture:** [THM-534 session theorem packet v0.1](UD_THM534_SESSION_DISCOVERIES_THEOREM_PACKET_v0.1.md). **Tracking:** [PR #346](https://github.com/ud-tetra/UD/pull/346), [issue #347](https://github.com/ud-tetra/UD/issues/347), earlier [PR #339](https://github.com/ud-tetra/UD/pull/339).

## 1. Source recovery receipt
- Read `THM-561_Weak_Color_Mass_Split_v1.0.md` (source version 1.0, §1.4 and §3): THM-534 is **cited** as supplying `T_self=1/2`, `T_opposite=1/6`, `T_cross=1/12`, not derived there. Its original micro-event count, measure, renewal rule and normalization are absent.
- Searched available Project/Library files for `THM-534`, `THM-561`, and hop weights. Search recovered THM-561, THM-562, THM-563a and downstream sources but no original THM-534 proof.
- Searched GitHub `ud-tetra/UD` indexed files for THM-534 and the three weights; no original was returned. [PR #339](https://github.com/ud-tetra/UD/pull/339) independently records an unsuccessful bounded recovery and explicitly freezes the missing source gate.
- Searched mounted `DistinctionDynamics_Full_Repository_v1.zip` (55 entries) by filename and text; no THM-534 occurrence. Scanned mounted text/HTML corpus: THM-534 reference only in THM-561. A public targeted search for the exact theorem identifier produced no relevant original.
**Scope:** Bounded retrieval failure, **not** proof that the original never existed. Do not backsolve an event law from the desired matrix.

## 2. THM-534-N1 — Full S4-invariant edge Markov family (EXACT)

**Carrier and symmetry.** Let `E=\{\{i,j\}:0≤i<j≤3\}`, `|E|=6`, `V=R^E`. The natural `S4` action permutes vertices and therefore edges. Equip V with the standard orthonormal edge basis. Let `T:V→V` be an entrywise nonnegative row-stochastic linear operator commuting with this action.

**Conclusion.** There exist unique `a,b,c≥0` with `a+b+4c=1` such that
```text
T_{ef} = a if e=f;
       = b if e∩f=∅;
       = c if |e∩f|=1.
```
Conversely every such triple yields an `S4`-equivariant, symmetric, doubly stochastic and uniform-reversible Markov operator.

**Proof.** The diagonal `S4` action on ordered pairs `E×E` has exactly three orbits: identical, disjoint and vertex-sharing edges. An equivariant matrix is constant on each orbit. There are one identical, one opposite and four adjacent destinations per row. Nonnegativity and normalization give the stated simplex. Each orbit relation is symmetric, hence `T=T^T` and uniform detailed balance. QED.

**Exact spectrum.** Write S for the opposite-edge swap and J for the all-ones matrix:
```text
T = aI + bS + c(J-I-S).
```
The eigenspaces are the constant line `V0` (dim 1), the symmetric-pair zero-sum space `V+` (dim 2), and antisymmetric-pair space `V−` (dim 3), with
```text
λ0 = a+b+4c = 1;
λ+ = a+b−2c   (multiplicity 2);
λ− = a−b      (multiplicity 3).
```
Proof: J acts by 6 on constants and by 0 on the other spaces; S acts by +1 on V0,V+ and −1 on V−.

**Consequences.** Tetrahedral symmetry, positivity, stochastic normalization, reversibility and uniform stationarity leave **two real degrees of freedom**. None selects the THM-534 weights.

## 3. THM-534-N2 — Exact counterexample to symmetry-only selection (NO-GO)
**Target historical triple:** `(a,b,c)=(1/2,1/6,1/12)`, giving `(λ0,λ+,λ−)=(1,1/2,1/3)`.

**Alternative strict-positive lazy triple:** `(a,b,c)=(3/5,1/10,3/40)`, giving `(λ0,λ+,λ−)=(1,11/20,1/2)`. Both are symmetric, doubly stochastic, S4-equivariant, strictly positive and satisfy `a≥1/2`. Their spectra differ. Therefore these assumptions do not identify THM-534. QED.

**Inverse-identification warning.** If one **assumes** `λ+=1/2` and `λ−=1/3`, the equations in §2 solve uniquely to `(a,b,c)=(1/2,1/6,1/12)`. This is an inverse spectral reconstruction, **not** a forward microscopic derivation. It must not be advertised as the missing THM-534 proof.

## 4. THM-534-N3 — Continuous-time reversible dynamics still do not select rates (NO-GO)
For arbitrary `u,v>0`, define a continuous-time Markov generator on edges by
```text
Q_{ef}=u if e∩f=∅; Q_{ef}=v if |e∩f|=1;
Q_{ee}=−u−4v.
```
Then `Q` is S4-equivariant, symmetric, irreducible, conservative and reversible with uniform stationary law. Its eigenvalues are `0,−6v (×2),−2u−4v (×3)`; hence `e^{tQ}` has eigenvalues `1,e^{−6vt},e^{−(2u+4v)t}`.

**Proof.** Apply the orbit decomposition in §2 to the generator; the three eigenvalues follow by substitution. Positive off-diagonal rates make the finite chain irreducible; symmetry yields detailed balance. QED.

The historical spectrum at `t=1` can be **inverse fitted** by
```text
v = (ln 2)/6,
u = (ln 3)/2 − (ln 2)/3 > 0.
```
But no native source rule fixes these logarithmic rates. Continuous-time semigroup dynamics, irreducibility and reversibility alone therefore do not recover THM-534.

## 5. THM-534-N4 — Forward-derived uniform vertex-transposition control (EXACT)
**Native control rule fixed without reference to THM-534 weights:** at each event select one of the six vertex transpositions of K4 uniformly; apply it to the current **unordered edge** `e∈E`.

For each edge, two transpositions (its own endpoints and the complementary endpoints) leave it fixed, four transpositions send it to four different adjacent edges, and none sends it to its disjoint opposite. Thus its one-step transition is
```text
T_transposition = (a,b,c) = (1/3,0,1/6),
spec(T_transposition) = {1,0 (×2),1/3 (×3)}.
```
**Proof.** Exact counting of six equally likely transpositions. QED.

This is a **source-complete microscopic rule** on the same carrier, but it **does not** reproduce THM-534. The negative result is useful: tetrahedral symmetry and a canonical local relabeling event do not automatically yield the historical weights.

## 6. Minimal remaining source law and preregistration gate (OPEN)
To attempt a new forward derivation, freeze **before** inspecting desired weights:
1. **State carrier:** six unoriented edges, signed edge cochains, or packet-state extension? Specify inclusion/projection and whether the Markov readout loses orientation.
2. **Primitive event alphabet and admissibility:** exact finite set of moves and which events are allowed, with provenance for each.
3. **Selection measure:** uniform counting or source-derived nonuniform weights; prove its normalization from the primitive rule.
4. **Renewal:** iid, quenched, state-dependent, memory-bearing, or deterministic scheduler; specify initial state and event-count clock. One-step T does not decide this (see THM-534-R2).
5. **Forward prediction:** enumerate or symbolically calculate `(a,b,c)` from the frozen events, **without** using `(1/2,1/6,1/12)` or the desired eigenvalues to choose the measure.
6. **Controls:** compare against uniform vertex transpositions, uniform full S4 action (`a=b=c=1/6`), strict-positive alternatives, and two-step return under at least two renewal rules.
7. **Independent acceptance:** exact event enumeration, invariant/relabeling checks, negative controls, non-constructor review, and only then comparison with historical THM-534. A mismatch is a **negative result** for the chosen source model, not grounds to tune probabilities.

**Frozen decision:** historical THM-534 micro-origin **SOURCE-BLOCKED**. N1–N4 are new mathematical results in the development lane; they do not retrospectively certify THM-534 or downstream Standard Model claims.

## 7. Verification and reproduction
Script: `verify_thm534_source_law_v0_2.py` (Python 3 standard library). Constructor execution on 2026-10-21: PASS — 24 S4 relabelings, exact six-vector eigenchecks, exact normalization and strict-positive alternative, exact uniform-transposition enumeration, and floating sanity of inverse logarithmic rates. No external dataset, empirical fit, or independent reviewer. Physical promotion 0.
