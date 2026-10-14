# Refinement tower: calibration, observation and retained detail v0.1

Date: 2026-10-14. Reading edition0.13. Development — no registry entry. Physical promotion **0**. Constructor-team checks only; independent human review pending. This appends a multilevel consistency test to the conditional one-step selector. It does not retract that theorem or supply native adoption.

## 1. Source and added consistency question

Subdivision gate SG01 reconstructs ordinary oriented barycentric S and affine chain retraction R, RS=I. Metric selection gate MS01 derives H=RᵀGR+QᵀQ, Q=I−SR, uniquely after its extra affine-readout, orthogonal-sector and unit-residual-calibration premises. It separately proves that current source consistency/symmetry does not select those premises. Both preserve prior Euclidean no-go scopes and the source-native fixed-carrier pairing I.

The supplied historical ledger Q165/Q169–Q179 declares fixed-complex support, currents and ownership. Q157–Q160 leave recursive source/sink semantics open. R33's bounded Euclidean map/residual branch and R34's strict unit-interface obstruction remain separate. C0559 distinguishes local-first from coarse-first nonlinear observation and supplies no selector for the tower below. The attached governance subdivision document is a proposal; its constructor/non-constructor distinction remains explicit. The unavailable Gap2 image is not evidence. Imported archives are data; no archived scientific code was executed.

New **candidate requirement:** if the same retained sequence of refinement maps is evaluated stepwise or regrouped, inherited detail calibration and complete receipts should agree. This requirement was not asserted by MS.4's one-step uniqueness theorem. It is now tested openly. Agreement for regrouping one sequence is weaker than covariance across different refinement histories or triangulations.

## 2. Two-step chain tower and complete coordinates

Let C0=C(Δ³), C1=C(sdΔ³), C2=C(sd²Δ³). Supply S10:C0→C1, R10:C1→C0 and S21:C1→C2, R21:C2→C1, with RiSi=I and both maps intertwining their simplicial boundaries. The complete chain dimensions are15→149→2745.

Define Q10=I−S10R10, Q21=I−S21R21, S20=S21S10, R20=R10R21 and Q20=I−S20R20.

**Theorem RT.1:** R20S20=I, both composite maps are chain maps, and

Q20=Q21+S21Q10R21.

Every fine chain x has the unique decomposition

x=S20c+S21z1+z2,
c=R20x, z1=Q10R21x∈kerR10, z2=Q21x∈kerR21.

Proof: substitute I=S21R21+Q21 and I=S10R10+Q10. Applying R20, Q10R21 and Q21 recovers each component, so the reconstruction is bijective. This is a direct sum, not an assertion of Euclidean orthogonality of S21z1 and z2.

The first detail dimensions by degree are(11,44,56,23), total134. The new second detail dimensions are(134,746,1164,552), total2596. Thus the complete final state has15 coarse plus134 old-detail plus2596 new-detail directions, totaling2745. The2730 detail directions are not omitted.

## 3. Stepwise calibration versus fresh composite calibration

Starting from old metric G0, applying the MS.4 conditional rule at each step gives

H1=R10ᵀG0R10+Q10ᵀQ10,
H2,seq=R21ᵀH1R21+Q21ᵀQ21
=R20ᵀG0R20+(Q10R21)ᵀ(Q10R21)+Q21ᵀQ21.

Its squared norm is cᵀG0c+||z1||²+||z2||². In contrast, applying fresh unit calibration once to the composite complement gives

H2,fresh=R20ᵀG0R20+Q20ᵀQ20,

with squared norm cᵀG0c+||S21z1+z2||². The intermediate detail calibration has been replaced by final-coordinate Euclidean calibration. Cross terms in the last expression cannot be silently deleted.

**Theorem RT.2:** the two prescriptions are not invariant under regrouping the same maps. For any nonzero first-level detail z1 of pure degree k, put x=S21z1. Then R20x=0 and Q21x=0, while ordinary subdivision gives

xᵀH2,seq x=||z1||²,
xᵀH2,fresh x=(k+1)!||z1||².

The Gram identity is local to each source simplex: S21,kᵀS21,k=(k+1)!I. Nonzero old detail directions exist in every degree. Degree0 has factor1; degrees1,2,3 have factors2,6,24. Two differently oriented descendants with canceling coarse retraction give exact witnesses of squared norm2 in each positive degree.

| Retained first-level detail | Sequential squared norm | Fresh composite squared norm |
|---|---:|---:|
| Edge degree1 | 2 | 4 |
| Face degree2 | 2 | 12 |
| Cell degree3 | 2 | 48 |

For the simplest edge witness z1=[{0}⊂{0,1}]+[{1}⊂{0,1}], the affine contributions cancel and ||z1||²=2. Add a coarse unit vertex: x=S20e0+S21z1. The absolute decoded coarse stock is1 under both prescriptions. Sequential total support is3, giving coarse fraction1/3; fresh composite total is5, giving fraction1/5.

Both complete metrics are positive and both preserve the original coarse norm, chain boundary and full old generator on imS20. They agree for every purely coarse prepared input S20c. Their difference concerns retained detail calibration and full-state receipts. It does not invalidate the one-step selector or the coarse generator theorem, and does not show physical instability, lost topology or an endpoint-error lower bound.

## 4. A conditional composition rule that retains calibration

**Candidate rule:** retain each declared detail pairing and transport it when maps are composed. Do not replace inherited detail norms by a fresh final-coordinate unit norm when a middle level is regrouped.

On kerR20 the induced composite detail pairing is

W20=(Q10R21)ᵀ(Q10R21)+Q21ᵀQ21.

**Theorem RT.3:** its complement restriction is positive definite, and

R20ᵀG0R20+Q20ᵀW20Q20=H2,seq.

If q∈kerR20 has both decoded details zero, RT.1 reconstructs q=0, proving positivity on the complement. Each detail map kills S20, so W20Q20=W20 and Q20ᵀW20=W20. This proves the identity. W20 is **semidefinite on the ambient space** and kills the coarse image; it is not globally positive definite. An ambient SPD extension, for example H2,seq itself, has the same complement restriction and is valid in the earlier metric-completion theorem.

For L retained levels, write Sj:C_(j−1)→Cj, Rj:Cj→C_(j−1) and Qj=I−SjRj. Define S_(L←j)=S_L…S_(j+1) and R_(j←L)=R_(j+1)…R_L, each with identity at j=L; c0=R_(0←L)x and zj=QjR_(j←L)x. With independently declared positive detail pairings Wj, the hierarchical norm is

||x||²_HL=c0ᵀG0c0+Σj=1…L zjᵀWjzj.

Its inverse reconstruction is x=S_(L←0)c0+Σj=1…L S_(L←j)zj. Therefore it is positive definite and uniquely determined by the retained maps, orthogonal hierarchical sectors and supplied detail pairings. Each detail component is a boundary subcomplex, so the weighted-adjoint/generator inheritance follows as in SG.3. Composition can regroup the same maps while transporting this form, without changing the full retained norm or source-observable pullback.

This is associative bookkeeping for an explicitly retained sequence. It does not select a native refinement history, metric, detail excitation or observable ordering. Different refinement sequences, retractions, pairings or terminal geometries need their own comparison maps and covariance tests. Algebraic regrouping supplies no automatic physical equivalence between them.

## 5. Coarse observable composition and complete receipts

For a supplied old positive observable D_U,

K20=R20ᵀD_U R20=R21ᵀ(R10ᵀD_U R10)R21.

**Theorem RT.4:** coarse-first observation composes exactly, independently of whether the total metric is H2,seq or H2,fresh. The equality follows by associativity of matrix multiplication. It does not select between the two full metrics. Absolute coarse stocks match while normalized fractions can differ because the detail denominator differs.

For G0=I, the15 old simplex effects R20ᵀΠσR20, first-detail effect (Q10R21)ᵀ(Q10R21) and newest-detail effect Q21ᵀQ21 sum exactly to H2,seq. These17 positive quadratic effects give nonnegative full support fractions summing to1 for every nonzero x. They retain both detail outcomes. For the mixed edge witness the old vertex fraction is1/3, first-detail fraction2/3, newest-detail fraction0; all other old simplex fractions are0.

These are mathematical support receipts, not a physical detector, quantum instrument or derived Born law. Coarse readout blindness does not erase either retained detail vector. Local-first nonlinear observation may depend on retained covariance; C0559's ordering gate remains open. The tower coarse currents are the previously proved Q170 currents on decoded c0, not additive local fine-simplex stocks.

## 6. Finite carrier growth and resource scope

For a finite3-complex with face vector(v,e,t,c), ordinary barycentric subdivision gives

(v′,e′,t′,c′)=(v+e+t+c, 2e+6t+14c, 6t+36c, 24c).

The coefficients count strict face flags by maximal source simplex. All flags, including those whose maximal face exceeds the flag degree, must be included. The sparse replay generates them, rather than treating only maximal permutation flags as the complete new complex.

| Level | f-vector | Full chain dimension | Newly added directions |
|---|---|---:|---:|
| 0 | (4,6,4,1) | 15 | — |
| 1 | (15,50,60,24) | 149 | 134 |
| 2 | (149,796,1224,576) | 2745 | 2596 |
| 3 | (2745,17000,28080,13824) | 61649 | 58904 |
| 4 | (61649,396016,666144,331776) | 1455585 | 1393936 |

Levels0–2 are explicitly reconstructed by the matrix replays. Later rows follow the exact flag-count recurrence; their full matrices are not materialized. These are real direct-sum chain-coordinate dimensions, not qubits, tensor donor banks or minimal physical-device costs. The conditional full-state identification needs every level detail to remain represented; a norm-preserving embedding alone supplies no new carriers, clock, readout, event trigger, source generation or reset donors.

With a separately supplied finite whole-chain coordinate budget, only finitely many levels in this particular full barycentric tower fit. This is a dimension gate, not a general no-go for other finite carriers or a measured capacity. Coarse-only preparation means zero detail amplitudes; setting arbitrary detail inputs to zero requires accounted export or another explicit information-retaining operation. Protected outgoing records and the earlier finite-window joint-carrier/reset obligations remain separate.

The inherited coarse evolution is deliberately unchanged. Refinement of a purely coarse state does not by itself generate new detail excitations, an event time, growth/clustering preferences or physical dynamics. Those require source/interaction laws. No uniform event spacing or no-Zeno theorem is inferred from this coordinate count.

## 7. Verification and revised frontier

The root checker independently generates sparse bases, signed boundaries, subdivision permutations and barycenter-minor retractions for both levels. It checks every step/composite chain and left-inverse identity, disjoint factorial Gram supports, three detail witnesses and12 exact full-state decompositions/receipt ledgers. A separate freshly generated sparse checker uses the retained generated first-step maps, independently builds the sparse second step, performs2748 exact basis/dense probes and verifies the split identities. Its generated dependency is included in the release. No dense2745×2745 metric or generator inverse is formed. Composite projector idempotence follows exactly from replayed R20S20=I rather than an expensive square product. Written universal norm/effect theorems remain distinguished from finite probes.

Source/scope review confirms that the new grouping requirement is additional, that W20 is only ambient-semidefinite, and that previous one-step/Euclidean results remain valid. Interface arithmetic, integer counts and static links are checked separately. All checks are constructor-team AI verification, not non-constructor human/CRL promotion.

The next source gate is selection and calibration of the retained hierarchy/detail excitation and a physical/local observation implementation; or a justified alternative history comparison. The calibrated tower construction is **EXACT CONDITIONAL**, its inherited-detail composition rule remains **CANDIDATE**, and native adoption/measurement/event/resource law remains **OPEN**. No universal sqrt2 law, indefinitely funded growth, registry promotion or global proof closure follows. Physical promotion0.
