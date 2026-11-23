# Native full-3D junction pre-event selection and metric audit — v0.1

**2026-11-23 UTC | development, not accepted canon | EXACT_CONDITIONAL / NO-GO_SCOPED / OPEN_CONSTITUTIVE_SOURCE | Physical Promotion = 0**

## 1. Authorized scope and source/version register

Question: Do already sourced UD pre-event variables determine when the two filled tetrahedra form a common 3D junction, determine its relative-orientation-dependent geometry, and preserve native squared-amplitude support without importing Euclidean overlap as a constructor or adding a fitted reserve/metric?

- **UD main pin:** `2e47d8718742cdd56ed81c41941b1cc3d42ad74b`; `AGENTS.md`, `docs/governance/UD-SCOPE-001-observable-domain-falsifiability.md` (2026-11-11); no unproved physical promotion.
- **UD-Physics main pin:** `6401ef38d4190f26492a06160aff763ed89cdb59`; `BOOTLOADER.md` v1.1, `instructions/UD_DISCOVERY_v1.2.md`, `docs/UD_MATHEMATICAL_METHOD_v1.0.md` and `docs/CONCURRENCY.md` v2.0.
- **Pinned UD source ledger:** `captures/2026-10-21T151000Z-codex-exit03-recovery-98dc7b12/library_LEDGER_v0.85.json`, Git blob `93e2ca31eba625989087275a71c4857848e321c6`, embedded scientific revision v0.43; rows Q165–Q179, Q194, Q198, Q200, Q210. Q169 is the skew fixed-complex generator; Q170 local Hasse support; Q177–Q179 existing-complex ownership; Q198 is a *conditional receipt-index* operator; Q210 preserves the missing constitutive obligation rule.
- **Immediate predecessor:** UD draft [PR #611](https://github.com/ud-tetra/UD/pull/611), SHA `ed7e860a0912d9480a19707be42771f155d0dee0`, report §§2–5; companion Discovery [PR #459](https://github.com/ud-tetra/UD-Physics/pull/459), SHA `2825f2e7e5c2f4a9d166b48dec73a3bb90bfda11`. Their *prescribed* octahedral 3D fan, graded transfer and Gram data are immutable input, not a source-derived formation law.
- **Independent source control:** UD-Physics `experiments/pachner-interface-defect/README.md` v0.1, blob `4a7ee4e2994d8903f9ae4e52e145f198684a5b3a`, distinguishes event-chain maps and reserve receipts from a native trigger and post-event memory dynamics.
- **External conceptual antecedent only:** Dan Echegoyen, *Structure of Existence Video 3.1 narrated*, 2020-04-03, https://youtu.be/UDGeXvDRwgU (chapter 18:16), previously tested/refuted in UD PR #609 for unrestricted orientation-independent exact edge contacts. Not used as a physical-law premise.

All **geometry** below is explicitly supplied dimensionless Euclidean geometry for an adversarial comparison. It is not in the pure K4 incidence/Θ state. There is no physical clock, SI length, calibrated energy, or measured quantity. All calculations are rational or algebraically exact. The test is hypothesis-led, not preregistered confirmatory physical research.

## 2. Typed state and identifiability question

Let `K_old=Δ³_A ⊔ Δ³_B` be two **separately labelled** filled tetrahedral chain complexes, and let `C_old = ⊕_{k=0}³ C_k(K_old;R)` with dimensions `(8,12,8,2)` and source metric `I30`. Let `X_native` contain the ordered old incidence, real amplitudes c, an optionally matched three-bit Θ state, hard integrity gates, and recorded Q169/Q170/Q198 intrinsic source receipts. These are model coordinates and not physical positions. A pre-event candidate selector factoring only through `X_native` is a function F:X_native→JunctionData.

Now define two *external comparison* realizations of exactly the same abstract state `x` in dimensionless `R³`:

\[
v_0=(1,1,1),\quad v_1=(1,-1,-1),\quad v_2=(-1,1,-1),\quad v_3=(-1,-1,1),
\]
\[
w_i(Q)=-Qv_i,\quad Q\in SO(3).
\]

Each tetrahedron's halfspace constraints are `v_i·r≥-1` or `(-Qv_i)·r≥-1`. Test `Q=I` against the exact rational proper rotation

\[
Q_*={1\over87}\begin{pmatrix}-61&-22&58\\62&-19&58\\-2&82&29\end{pmatrix},\quad Q_*^TQ_*=I,\ \det Q_*=1.
\]

**EXACT:** All 36 pairs of their infinite supporting edge lines are noncoplanar at `Q_*`. Both solids nonetheless contain the centered Euclidean ball of radius `1/sqrt(3)`, so both have positive volume overlap. From the eight closed halfspaces, independently enumerate every three-plane intersection and retain points satisfying all eight inequalities.

| Realization | Overlap vertices | Overlap edges | Overlap facets | Facet sizes |
|---|---:|---:|---:|---|
| Q=I | 6 | 12 | 8 | eight triangles (regular octahedron) |
| Q=Q_* | 12 | 18 | 8 | six pentagons, two triangles |

The two overlap boundaries are each polyhedral 2-spheres, but have different `f`-vectors. Neither 3D shape is reconstructible from the common abstract packet state unless the relative embedding/relationship is introduced in a well-typed state/readout map.

**NO-GO_SCOPED — shape nonfactorization:** If `F` uses only the same intrinsic pre-event tuple `x`, then F(x) is one value. It cannot equal both exact outputs `K_overlap(I)` and `K_overlap(Q_*)` since their boundary vertex counts are 6 and 12. Thus the **relative-orientation-dependent geometric junction shape** does not factor through the current embedding-blind tuple. This does **not** obstruct a binary answer "some 3D overlap exists" on this special concentric control, since both have it; it does not obstruct a new intrinsically sourced *combinatorial* gluing unrelated to these embeddings. It identifies an indispensable missing typed relational input for this geometry-dependent claim.

`S4×Θ` is a finite exposure carrier, not a continuous `SO(3)` orientation map. A seam connection may someday carry an appropriate relational variable but no reviewed source-defined intertwiner from that connection to the Euclidean polygonal overlap is supplied. Numeric resemblance does not instantiate the map.

## 3. No-reserve event gate from the frozen conditional transfer

The **prescribed** geometric fan transfer `T:C_old→C_new` from PR #611 maps two old tetrahedra into a new 3D octahedral union complex of chain dimension 117 and has `T^TT=diag(I8,2I12,4I8,M3)`, where

\[
M_3=\begin{pmatrix}12&-8\\-8&12\end{pmatrix}.
\]

`M3` has eigenvalues exactly 4 and 20. Under these *particular source and target unit coefficient metrics* the native support discrepancy is

\[
G(c)=\|Tc\|^2-\|c\|^2=\|c_1\|^2+3\|c_2\|^2+3(a^2+b^2)+8(a-b)^2.
\]

Its full 30-dimensional Gram-defect spectrum is `0^8,1^12,3^9,19^1`. Every term is nonnegative. Therefore

\[
\boxed{G(c)=0\ \Longleftrightarrow\ c_1=c_2=0\ \text{and}\ a=b=0.}
\]

**NO-GO_SCOPED — zero-reserve support gate:** A deterministic event satisfying simultaneously (i) this prescribed `T`, (ii) the old and new unit simplex norms, and (iii) `R^+=R^-=0` with no other stock carrier, can admit only vertex-only preparations. Any nonzero edge/face/top amplitude violates exact stock balance. For pure top amplitude `(a,b)=(1,0)` the exact stock creation is 11; for `(1,1)` it is 6; an isolated old unit edge creates 1. These dimensionless numbers are model stock, **not physical energy**.

Vertex-only inputs avoid the *instantaneous* norm defect, but **do not solve event authorization or evolution continuity**. PR #611 exactly records `A_new T≠T A_old` with commutator rank 28 under the inherited unweighted generators; a zero-gain input is not a proof of a persistent covariant junction. A candidate reserve inequality `R^-≥G(c)` makes an event *conditionally affordable* but its source, ledger role, time/update, replenishment and interaction remain OPEN. Do not invent `R` as an already present Q170 reservoir; Q172 interface face stock is a different typed object.

## 4. Positive metric loophole does not select a native law

`T` has full column rank in the chosen prescribed geometry. Let `M=T^TT>0`, `P_T=T M^{-1}T^T` be the orthogonal image projector, and let `λ>0`. Define a strictly positive-definite **nonlocal**, grade-preserving model metric on the **new** coordinate space:

\[
\boxed{H_\lambda=T M^{-2}T^T+\lambda(I-P_T).}
\]

Then `T^T H_λ T=I` *exactly*, and `H_λ` is positive: it is the ordinary old norm on `im(T)` and `λ` times the unit norm on its orthogonal complement. **EXACT / CONDITIONAL:** a mathematical metric can eliminate the transfer's instantaneous apparent stock gain without an auxiliary reserve. This does not contradict the previous **positive diagonal target 3-cell metric no-go**, because `H_λ` is non-diagonal/nonlocal wherever old top simplices share target cells.

The same source data allows infinitely many choices `λ>0`, and the construction uses the already prescribed `T`. No current UD source selects the target geometry, this metric, its normalization or λ. Moreover, the source's **unit-skew** generator `A_new` generally fails to be skew-adjoint with respect to `H_λ`: the additional condition `A_new^T H_λ+H_λ A_new=0` must be checked before claiming post-event conservation in this new metric. A small rational toy transfer `[[1,0],[0,1],[1,-1]]` shows nontrivial metric-defect for an independent skew rotation of the first two target coordinates; both main and independent replays verify the family identity at λ=1/2,1,2.

This establishes two distinct honest branches: use a source-funded reserve under inherited unit norm, or use a newly derived nonlocal metric plus an appropriate generator. Neither has yet been selected. **A metric derived from a prescribed event is not evidence the event was sourced pre-event.**

## 5. Pre-event acceptance rule and falsifiers

A complete native forward rule must provide: (1) a pre-event **relational** state `r_AB` with specified domain, gauge action and preparation, discriminating the canonical and rotated geometry if the target is a geometry-dependent junction; (2) a source-derived constructor `K^+(x,r_AB)` with **all** cofaces, unique simplex identities and legal link topology; (3) an admissible event trigger that does not consult the chosen post-event target; (4) graded transfer `T(x,r_AB)` or a typed reserve with initial state and update; (5) matched support/energy/work and lineage receipts with stated metric and update; (6) post-event evolution compatibility or an explicitly supported memory generator; (7) a pre-registered signed/phase readout that outperforms conventional Euclidean contact geometry.

**Acceptance rule:** `PASS_NATIVE` only after (i) both test realizations give the correct different polyhedral shape with the **same declared pre-event data except lawful source-derived relational input**, (ii) no target-chosen Euclidean Q, γ, λ, κ, spring penalty or after-the-fact event flag, (iii) all chain, support and clock/gauge receipts close and (iv) a repeatable conditional prediction differs from ordinary source-imposed geometry. Until then `OPEN_CONSTITUTIVE_SOURCE` and Physical Promotion=0.

**Failure gates:** if the selector is Q-blind and still claims both exact shapes, it is falsified for this scope; if the event uses `T` and unit metric with an active edge but no reserve, it violates stock accounting; if a nonlocal metric is inserted without a source/generator, it is mathematical calibration/choice, not a native derivation. A change of domain/codomain/metric creates a separate versioned branch, not a repeal of an existing obstruction.

## 6. Verification, limits, and release scope

- Main `verify.py`: exact SymPy proper rotation, 56 triple-plane supports, polyhedral facets/edges, 36 line noncoplanarity controls, transfer Gram algebra, and a model positive-metric family. PASS locally.
- Independent `replay_stdlib.py`: a separately written pure `fractions.Fraction` Gaussian elimination, convex halfspace filter, 36 line determinants, direct symbolic stock square checks and three different metric choices. PASS locally; independent *implementation*, same constructor and **not** an external scientific review.
- Both produce JSON results. No instrument or physical mapping; `Qstar` is a deliberately sourced geometric control, not a predicted native frame. No lattice-wide exhaustive SO3 scan: only two exact rotations and a general factorization argument.
- Full repository CI/test suites and DPR-Coder non-constructor review are separate pending gates. These audit outputs do not overwrite the frozen v0.85 ledger or source manuscripts.

**Recommendation:** AUTO_FREEZE claim of a *source-selected Euclidean full3D junction* under present variables and inherited unit metric; preserve exact counterexamples, narrow positive-metric existence and topology facts. Reopen only with a new pre-event relational geometry/coface source plus source-funded reserve or native metric/generator, tested without fitting. **Physical Promotion = 0.**
