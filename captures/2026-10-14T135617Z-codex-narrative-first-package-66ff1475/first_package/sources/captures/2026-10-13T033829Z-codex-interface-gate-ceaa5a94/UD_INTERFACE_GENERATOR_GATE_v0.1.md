# UD vertex interface and cross-event generator gate v0.1

**13 October 2026 UTC · development, no registry entry · physical promotion 0.** Constructor and adversarial self-check: Codex; independent non-constructor review pending. Extends the [bounded two-event branch v0.1, §§1–4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-13T031858Z-codex-bounded-transfer-c082fca1/UD_BOUNDED_SUBDIVISION_TWO_EVENT_GATE_v0.1.md) with an exact obstruction under a declared boundary readout. It does not retract the conditional two-event support ledger.

## 1. Source and contract

[UD Paper I review draft 1.1.1, §§4, 6.1, 7.4, 8.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) and the supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165–Q173 provide the Euclidean squared-amplitude support carrier and unweighted global fixed-complex skew incidence generator `A_K=B_K^T−B_K`. Q170 gives a control-volume support equation; Q177–Q179 give equal-top-star ownership. Q157–Q160 leave recursive support ingress and predictive open-system source/sink terms open. Q167 and Q173 concern separately typed gated channels; they do not select a new generator on barycentric subdivision or an interface metric. The supplied CRL2 subdivision governance proposal v1.0, §§1–4, does not promote a new law.

Let `K` be one filled oriented tetrahedron and `K'=sd K` its ordinary oriented barycentric subdivision. Work in unit orthonormal simplex coefficient bases of `C(K)` and `C(K')`. The following is a **candidate strict interface contract**, not a source-authored one:

1. The native linear transfer `T:C(K)→C(K')` is contractive in the Q165 Euclidean support: `||Tc||≤||c||` for every old chain; lost native norm may enter a separately typed residual carrier.
2. For every old vertex basis vector `e_i`, its coefficient at the corresponding singleton barycentric vertex `[\{i\}]` remains exactly **1**. This is an explicitly unit-calibrated, coefficient-level vertex readout. It is stronger than simply preserving a decoded observable or total support in a control volume.
3. The native fixed-complex flows join without an event-local generator defect: `A_{K'}T=TA_K`. Both `A` are the sourced unweighted incidence generators. This is a demanding cross-event continuity/intertwining condition, not a property claimed in Paper I.

The interface contract has no physical units or time calibration. The result below tests its mathematical consistency. No boundary-chain condition is needed for the obstruction, so adding `∂'T=T∂` cannot repair it.

## 2. EXACT no-go under the strict contract

For any old vertex `e_i`, `||e_i||=1`. The unit readout and contraction give

\[
1=|\langle e_{\{i\}},Te_i\rangle|^2\le||Te_i||^2\le1.
\]

Equality in the orthonormal coefficient basis forces `Te_i=e_{\{i\}}` with every other new coordinate zero. In old `K4`, `e_i` has three incident edges, so `||A_K e_i||²=3`. In `sd K4`, the singleton `[\{i\}]` is joined to every strict nonempty face containing `i`: three original edges, three original triangles, and the tetrahedron, for **seven** incident edges; `||A_{K'}e_{\{i\}}||²=7`. If intertwining held, contraction would imply

\[
\sqrt7=||A_{K'}Te_i||=||T A_K e_i||\le||A_K e_i||=\sqrt3,
\]

a contradiction. **NO-GO:** there is no such `T` satisfying all three requirements, even without demanding a chain map. The coefficient and generator metrics must remain as declared; a different weighted post-event generator, weaker readout, or externally funded noncontractive native transfer defines a different branch.

## 3. Readout and dynamical checks on the bounded candidate

The prior bounded scalar chain map `T=S/√24` is contractive, has `∂'T=T∂`, and stores the complementary norm in a residual carrier. It gives `T e_i=e_{\{i\}}/√24`, so it **fails the unit vertex readout**. Its generator commutator on one vertex has the exact integer-matrix result

\[
||(A_{K'}S-SA_K)e_i||^2=7,
\qquad ||(A_{K'}T-TA_K)e_i||^2=\frac7{24}.
\]

The `verify.py` replay enumerates 149 new simplex coordinates, checks the integer chain identity and Gram factors `(1,2,6,24)`, and independently counts the old and new incident edges `(3,7)` and the unscaled commutator norm 7. These finite checks support the exact algebraic proof; the conclusion does not rely on floating point root finding.

In Q177–Q178's equal-top-star allocation, one old unit vertex belongs to one top tetrahedron, so its total owned support is 1. Its descendant singleton belongs to six child tetrahedra; under `S/√24`, each child's equal share is `(1/24)/6`, whose sum is `1/24`. Thus the bounded map also attenuates that **specific** aggregate vertex stock. Q177–Q179 specify how to allocate a *given* state on each complex; they do **not** require the aggregate to be invariant across a geometry event or prescribe an amplitude rescaling. Imposing that extra invariant would be a new interface law.

The source equations alone do not choose among common-scalar chain maps `T_a=aS`, `0<a≤1/√24`: each is contractive, boundary-compatible and admits `D_a=(I-T_a^TT_a)^{1/2}` as a support-preserving residual completion, but gives a different vertex readout `a`. In this scalar family, requiring vertex amplitude 1 sets `a=1` and expands top support by 24. Hence the fixed-complex substrate plus support conservation **underidentifies** the event interface; a constitutive selection or calibrated observable is required.

## 4. Disposition

**EXACT / conditional:** strict contract contradiction `7>3`, integer commutator, Q177–Q178 aggregate-stock calculation, and nonuniqueness of scalar bounded maps. **CANDIDATE:** the strict unit vertex interface and the earlier attenuated interface. **NO-GO:** simultaneous Euclidean native contraction, unit singleton vertex coefficient, and unweighted-generator intertwining on `K4→sd K4`. **OPEN:** a UD-sourced boundary readout, event-local generator or current, support source/sink semantics, later-event causality, physical clock and Lorentzian bridge. Physical promotion 0. `Gap2_FINAL_Finite_Genesis.png` was unavailable and not used.

Run `python3 verify.py` with NumPy to regenerate `results.json`. This check uses integer incidence matrices; the mathematical no-go is the norm proof in §2. A different boundary readout or a nonzero event defect must be stated as a versioned new branch and independently tested, rather than silently grafted onto the bounded construction.
