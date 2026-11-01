# Unified Dynamics — Cross-Channel Facet Competition and Newborn Initialization Audit v1.5

**Date:** 2026-11-01  
**Claim lane:** `DEVELOPMENT_NO_REGISTRY_ENTRY`  
**Status:** `EXACT_PAIR_ONLY_NO_GO / DIAGNOSTIC_COMPETITION_NONIDENTIFIABLE / NEWBORN_SOURCE_OPEN`  
**Physical promotion:** 0. Constructor verified; no nonconstructor review.

## Scope and source-bound types

- **Spatial object:** already-filled tetrahedral simplex `[0123]` with four frontier faces `012,013,023,123`, and binary graph labels `(0,0,1,1)` under the historically target-aware coface rule. An extension through a face is a **new tetrahedron**, not a four-simplex. The rule selects the *required graph label conditional on a face*, not the face or birth time.
- **Opposite-pair state:** three binary `Theta` pair-closure values indexed by matchings `01|23`, `02|13`, `03|12`. These are NOT the four oriented triangle seam holonomies or the binary vertex labels.
- **Burden:** scalar vertex stock `rho`, with the dimensionless **conditional** Q162 relaxational current `j_ij = -(1/4)(rho_j-rho_i)` when all six hard gates pass. Squared-current face diagnostics have burden-current-squared units, not action/energy units.
- **Seam:** group-valued edge transports. U(1) additive-angle and finite Z4 gauges are comparator branches; their group type is not equated with UD's Spin(3) transporter without an explicit typed mapping. `1-cos(phi)` is dimensionless mismatch, not an action coefficient.
- **Newborn:** new vertex `w` with three new edge transports and new burden/phase/framing/normal data. The three old triangle edges are inherited by identity.
- **Resource:** additive formation free/bound balances distinct from burden and from Q165 squared-amplitude support; no map to physical joules is assumed.

**Controlling sources:**

1. `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, 2026-08-22, Q153–Q158, Q162, Q165–Q173 and G05. Q153/Q158 are source accounting and residual identities, **not** predictive costs; G05 leaves the master loop-action coefficient open.
2. `Docs/UD conditional paired gate feedback and persistence audit.md` (repository blob SHA `124ef2aa89a8a936a429554d46d23fe48ceae81c`), *Source and declared scope*: conditional fixed-Hamming opposite-pair swap, prepared burden and open/closed pair, selected integrity gates, first-event origin and clock external.
3. `Docs/UD receipt constrained gate reachability audit.md` (blob SHA `3644c6aa8f19f15c2bf2ee4dda45fee4d179be0`), *Retrieved source rules* and *Event source boundary*: pair-closure gate belongs to both opposite edges; no universal first-close event or edge environment.
4. `Docs/UD event admission and interface memory.md` (blob SHA `6719d0f77622eac59c5c88fc163b49adda664e6`), *What the source actually supplies*: a local conditional candidate, no general shared authorization or formation trigger.
5. `Docs/UD native coface growth and cluster selection audit.md` (blob SHA `9ac884d727e65ddd4ed1c277d2ed4a7b91135d73`), *Source boundaries*, *Local completion result*: candidate graph-first fresh-vertex growth, nonunique cluster topology, native scheduler and material source open.
6. Historical newborn suite `UD_COFACE_RESOURCE_INHERITANCE_EXACT_THEOREMS_v0.1.md` and `UD_COFACE_NEWBORN_PACKET_INHERITANCE_MATRIX_v0.1.md`: three new seams and newborn burden, framing, phase and positive cost all unselected.
7. Development predecessor `UD_COFACE_SYMMETRY_SOURCE_AND_NEWBORN_IDENTIFIABILITY_AUDIT_v1.4.md` (2026-11-01): exact burden and seam conflict controls. This work is a new narrower proof, not a silent amendment of any frozen rule.
8. Designated public research portal (accessed 2026-11-01): Paper I–III v1.1.1, Paper IV v0.1; physical promotion 0.

## Workload 1 — no-go for a Theta-only tetrahedral-face selector

Define `P` as the set of three opposite-edge perfect matchings of four vertices and `F` as the set of four triangular faces. `S4` acts naturally on both. The Klein four subgroup

```
V4 = {identity, (01)(23), (02)(13), (03)(12)}
```

is exactly the kernel of `S4 -> Sym(P)`: it fixes each matching individually. It acts **transitively** on the four faces (faces are complements of vertices).

**EXACT theorem (not merely linear):** For any `S4`-equivariant deterministic score function `s : {0,1}^P -> R^F`, one has `s(theta)_f=s(theta)_g` for all faces `f,g`. Proof: every `k in V4` fixes the input `theta`, hence equivariance gives `s(theta)=k s(theta)`; transitivity forces all outputs equal. The same result holds for arbitrary pair-valued input data with the natural matching-permutation action, not only bits. In particular **there is no equivariant deterministic map from the matching state alone to one singleton face**.

**Stronger linear identity:** Every linear intertwiner `A:R^P -> R^F` satisfies `A=gamma 1_4 1_3^T`. The 12 matrix coefficients form one orbit under the simultaneous `S4` action; the constraint matrix has rank 11. No nonconstant face information survives.

**Already binary-labeled seed:** With labels `(0,0,1,1)`, the label-preserving permutation `(01)(23)` still belongs to the matching kernel and swaps all four individual faces. It fixes the binary labels and any ordinary opposite-pair data, so a covariant singleton selector from *just those two types* also fails. An orientation-sensitive independent seam or named face history may remove this stabilizer; the theorem does not forbid that.

This clarifies the archived fixed-Hamming conditional B2 swap: even an exact unique selection among **three edge pairs** is not a unique selection among **four triangular cofaces**. A chosen pair-to-face lookup table breaks `S4` unless furnished with an additional covariant vertex/face marker.

### Competing typed diagnostics and a deliberately arbitrary mixing witness

Using the v1.4 prescribed prestate `rho=(0,1,2,4)` with all gates one, the face-local quadratic current diagnostic is

```
faces     012      013      023      123
D_B       3/8      13/8     3/2      7/8
```

Its unique maximum is `013`. An existing v1.4 U(1) comparator, with old link phases in units `pi/6` of `(-1,1,0,-1,0,0)` on ordered edges `(01,02,03,12,13,23)`, generates oriented face holonomies `(-3,-1,+1,-1) pi/6` and seam mismatch `D_U=(1, 1-sqrt(3)/2, 1-sqrt(3)/2, 1-sqrt(3)/2)`. Its unique maximum is `012`. These maxima are **not** native source selections.

To establish underdetermination even after ad hoc normalization, set `b_f=D_B(f)/(13/8)` and **CANDIDATE illustration only**

\[
  S_f(\lambda) = \lambda b_f+(1-\lambda)D_U(f),\quad 0\le\lambda\le1.
\]

The top face changes at the exact switch

\[
 \lambda_* = \frac{13\sqrt3}{20+13\sqrt3}.
\]

For `lambda=1/4` unique top is `012`; for `lambda=3/4` it is `013`; at `lambda=lambda_*` the two tie. All three outcomes respect relabeling covariance of the respective diagnostics and use the identical old state. **No value of lambda is native**. The normalization and linear addition also are not source-owned. This is an identifiability counterexample, not a recommendation for a mixing law.

**No-go scope:** The inspected G05 master-action normalization is OPEN, and no joint burden/seam action functional on the correct typed spaces was recovered in the cited source scope. Such a functional might exist in another future or inaccessible source; absence from the inspected corpus is not a universal no-go.

## Workload 2 — newborn state, symmetry and formation-resource nonidentifiability

For child `[w012]`, the old boundary edges and old face are inherited; the three new U(1) links can be represented by additive turns `(a_w0,a_w1,a_w2)` modulo 1. An independent gauge change at `w` adds the same phase to all three. The gauge-invariant relative data are

\[
 (a_{w1}-a_{w0},\ a_{w2}-a_{w0})\in U(1)^2.
\]

An exhaustive four-point per-link control `a_wi in {0,1/4,1/2,3/4}` has `4^3=64` raw states and `4^2=16` gauge classes, with exactly two independent relative phases. Old face data do not select one class. For group `G`, fixed-boundary newborn gauge quotient `G^3/G ~ G^2` (free diagonal gauge) has formal dimension `2 dim G`; for `SU(2)~Spin(3)` this is 6 real dimensions locally, not six physical spacetime dimensions.

The **three new triangle loops** obey the (abelian) oriented Bianchi constraint

\[
 \Phi_{w01}+\Phi_{w12}+\Phi_{w20}=\Phi_{012}\pmod{2\pi}.
\]

If old face holonomy is nonflat, all three new loops cannot be flat. Thus applying `newborn all-flat` as an automatic rule would fail on legitimate curved seeds. The 4-angle exhaustive grid verified the constraint for all `4 * 4^3=256` old/new combinations. Nonabelian parallel transports have a path-ordered version; no U(1) result has been silently treated as its full proof.

The newborn `rho_w, theta_w, sigma_w`, framing/normal and seam choice remain independent typed gaps. Two conserved scalar burden allocations from the same initial `(1,1,1,1)` are `((1-x/4)^4,x)` and `(1-x,1,1,1,x)` for `0<x<=1`; they have the same total 4 but different donors. These are accounting counterexamples, **not** source-flow solutions. Formation-resource transfers of 1 and 2 from initial `(R_free,R_bound)=(3,4)` both preserve total 7 but are different events; this shows cost nonidentifiability, not physical energies. `M_form` is an *admission viability threshold*, not a positive formation debit.

**Additional scope:** A fixed positive minimum debit cannot be inferred from real-amplitude quadratic support alone; scaling an allowed nonzero amplitude by `epsilon` makes squared support arbitrarily small while preserving the symbolic mode structure. A finite event charge would require a separately declared capacity/quantization/threshold/source law.

## Decision register and reopen conditions

| Claim | Verdict | Condition for promotion/reopening |
|---|---|---|
| Theta-only covariant singleton-face selector | **NO-GO** under ordinary opposite-pair action | Add independently sourced face/vertex asymmetry or change representation and rederive |
| Linear pair-to-face intertwiner | **EXACT** one-dimensional constant-map family | None for mathematical statement |
| Burden diagnostic vs U(1) seam diagnostic | **EXACT** conflicting maxima under declared preparations | A source-owned typed joint action or independently pre-registered competition rule |
| U(1) newborn seam from inherited boundary | **NO-GO** unique inference | New group-valued normal/seam preparation map; gauge-equivalence readout |
| Curved-boundary all-flat newborn | **NO-GO** abelian Bianchi scope | Allow curved new triangles or change typed transport law |
| Newborn burden donor and formation debit | **OPEN / nonunique under accounting** | Constitutive positive debit + donor + event log + sign/units receipt |
| Native face selection, clock, physical energy | **OPEN** | Source-owned predictive event scheduler and independently tested bridges |

**Source governance:** No new internal coefficients, no new graph/facet priority functional, no physical time/energy units, and no frozen coefficient update. AUTO_FREEZE use of pair-only matching scores as a native face selector and zero-curvature newborn inference on curved old faces. AUTO_LOCK eligible only for scoped group/action theorem and exact finite controls after independent review; this capture alone does not update the canonical registry.

## Reproduction

- `verify_v1_5.py`: SymPy+Fractions; 904 passing exact assertions across `S4/V4`, linear intertwiner rank, mixed-score switches, finite new-edge gauge classes, Bianchi, conservation.
- `independent_check_v1_5.py`: independent stdlib-only finite group/fraction implementation; 763 passing exact assertions, including twelve matrix-entry transitivity orbits.
- Exact result files and run transcripts accompany this document. Both verifiers were authored by the same constructor: **not independent external peer review**.
- Earlier v1.4 controlled preparations are treated as source-provenance inputs, not retuned to produce the new theorem. Repository-wide checker pending at submission; GitHub publication, if performed, is a separate step from local verification.
