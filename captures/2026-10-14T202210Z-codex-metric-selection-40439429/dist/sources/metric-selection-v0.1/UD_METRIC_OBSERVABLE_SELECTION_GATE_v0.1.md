# Metric and observable selection gate v0.1

Date: 2026-10-14. Public reading edition0.12. Development — no registry entry. Physical promotion **0**. Constructor-team checks only; independent human review pending. Exact consequences and proposed constitutive premises are separated below.

## 1. What the sources actually select

The fixed-complex source commitments are specific: real coefficients in a declared orthonormal oriented-simplex basis; Q165 total support Σσ cσ²; Q169 generator A=Bᵀ−B; Q170 region stock Σσ∈U cσ²; Q171/Q172 separate top/face stocks; Q177/Q178 equal-top-star ownership. Their source-fidelity rule is:

**Theorem MS.1:** on that fixed carrier and in that fixed basis, retaining the declared total stock for every state selects G=I, and retaining the region stock for every state selects D_U=diag(1σ∈U).

Proof: equality of the quadratic forms for every real vector determines the symmetric matrices by polarization. This is preservation of a declared source definition, not a new dynamical selector. C0176 also proves that a positive diagonal conserved stock under the unchanged unit-incidence generator must have equal weights on each connected Hasse component; fixing its reference unit yields I.

Those commitments do not state that an ordinary subdivision event must preserve the old norm, nor prescribe coarse readout, residual calibration or observable ordering. C0243 explicitly distinguishes parameter-free optimization from source derivation; C0173 supplies admissible but nonunique geometric metrics; C0559 distinguishes coarse-first from local-first observation and leaves its selector open. The attached historical ledger Q157–Q160 leaves recursive source/sink semantics open. The attached CRL document is a governance proposal, not a selection or promotion receipt. The reconstructed attachments master_action.md, carrier_definition.md, coherence_equation.md and packet_field_equation.md contain placeholder text, not a functional that could select this interface. They supply no missing variational equation.

The existing public source texts are snapshotted with their original catalog IDs, exact content-field SHA-256 and provenance. Text hashes do not imply recovery or independent verification of original PDFs/release bytes. No archived scientific programme is executed. The unavailable Gap2 image is not used.

## 2. Full classification of compatible metrics

Retain the verified15→149 ordinary barycentric chain map S, old positive pairing G and boundaries B,B′. Require SᵀHS=G and A′H S=S A_G, with H positive definite and the correct weighted adjoints. Since B′S=SB, the generator equation is equivalent to the adjoint equation.

**Theorem MS.2:** every such H induces the chain retraction

R_H=G⁻¹SᵀH, with R_H S=I and R_H B′=B R_H.

Set Q_H=I−S R_H. Then

H=R_HᵀG R_H+Q_HᵀH Q_H.

Proof: isometry gives the left inverse. The adjoint equation is B′ᵀHS=HS G⁻¹BᵀG. Transpose it and multiply by G⁻¹ to obtain the retraction chain identity. The image of S and kernel of R_H are H-orthogonal, so the direct-sum norm gives the displayed decomposition. Conversely any chain retraction R with RS=I, together with a positive pairing on ker R, yields H=RᵀGR+QᵀWQ, Q=I−SR, and all three norm/boundary/generator equations. Degree-block choices preserve orthogonal chain grading.

Thus the complete compatible metric class is parameterized by a **chain retraction and a positive complement pairing**, not by S and G alone. With a fixed R, all compatible metrics for which R is the metric adjoint of S have exactly this form; only W restricted to ker R matters. An extension of W outside the complement is redundant.

## 3. Exact metric and observable nonselection witnesses

For the affine barycenter retraction R from subdivision gate v0.1, G=I and Q=I−SR, consider

H_w=RᵀR+wQᵀQ, for every w>0.

They all satisfy the three equations and full signed S4 covariance. The same R is induced by every H_w. Let x be the unit fine vertex at face barycenter{0,1}. Then Rx=(e0+e1)/2, and Qx=x−(e{0}+e{1})/2. Hence

||Rx||²=1/2, ||Qx||²=3/2, xᵀH_w x=1/2+3w/2.

In particular H1 gives2 while H2 gives7/2. These are unequal metrics satisfying the same mathematical consistency and symmetry conditions. Positivity, covariance and complete coarse compatibility therefore do not select a unique fine metric. This is a no-go for uniqueness from those premises, not an impossibility of a further law selecting one.

These particular uniform-w witnesses establish norm/calibration freedom. They do not by themselves assert distinct fine generators; scaling an entire reducing complement pairing uniformly can leave its adjoint unchanged. More general degree-dependent complement pairings remain in the classified family.

Even fix H1. The positive quadratic observables

K_λ=RᵀR+λQᵀQ, 0≤λ≤1,

all obey 0≤K_λ≤H1 and SᵀK_λS=I. They have the same calibrated coarse-code total stock but give the chosen fine vector values1/2,5/4,2 atλ=0,1/2,1. Metric selection alone and calibration only on Sc therefore do not select the observable. These λ and w values are mathematical counterexamples, not adopted coefficients.

## 4. Why an additive diagonal fine metric cannot repair the map

**Theorem MS.3:** no strictly positive diagonal fine metric H makes ordinary S intertwine its weighted adjoint with the old unit adjoint, hence none gives full source-generator inheritance.

Take old vertex0 and fine edge flag[{1}⊂{0,1}]. S e0 is the singleton vertex{0}. B′ᵀS e0 has zero coefficient on that flag because its endpoints are{1} and{0,1}. A diagonal metric changes incidence coefficients but not this support. Thus B′†H S e0 has coefficient0 there for every positive diagonal H. However Bᵀe0 contains−edge(0,1), and S[0,1]=[{0}⊂{0,1}]−[{1}⊂{0,1}], so S Bᵀe0 has coefficient+1. The downward terms already agree, so the full generator equation fails.

This is stronger than the earlier failure of Hdiag,k=I/(k+1)!. It excludes arbitrary positive simplex weights for this ordinary S and the full old unit generator. A common nonzero rate multiplier does not remove the support mismatch. A changed transfer, larger carrier/readout contract or explicitly nonzero interface defect is outside this theorem.

Consequently retaining the source fine-simplex additive stock, selecting G′=I by MS.1 and demanding exact old-generator inheritance through ordinary S are incompatible. The native fixed-carrier source remains well defined; it does not secretly select a successful dense refinement metric.

## 5. A uniquely selecting conditional rule

The following is an explicit **candidate constitutive contract**, not a source-derived UD law. It supplies the missing inputs before evaluating any physical or clock target.

**Premise A — affine coarse observation.** A face-vertex F is read as an affine combination supported on its original vertices, with coefficients summing to1 and invariant under relabelings within F. Its coefficients must all equal1/|F|. Require higher-degree readout to respect exterior products. This uniquely fixes the affine R used above. The affine/exterior requirement is additional amplitude semantics, not a consequence of the fact that the source basis is simplicial.

**Premise B — independently calibrated coarse and residual norm.** For every x=Sc+z with z∈ker R, require the coarse norm cᵀGc, H-orthogonality of the two sectors and the declared unit Euclidean residual norm zᵀz. This fixes

**Theorem MS.4:** H*=RᵀG R+QᵀQ.

Indeed xᵀH*x=cᵀGc+zᵀz, which uniquely determines a symmetric H* by polarization. Its generator compatibility follows from the retraction identities, not a fitted rate. The scalar1 in the residual pairing is a stated unit-calibration premise. It is not selected by positivity, symmetry, minimality or lack of fit parameters. Applying Q165's unit convention only to the residual sector while changing mixed/coarse fine stocks is a new composite norm contract; it is not unchanged149-coordinate Q165 support.

**Premise C — complement-blind positive coarse observation.** Supply the original region observable D_U, require K_U≥0, exact code calibration SᵀK_U S=D_U and zero response on the retained complement QᵀK_U Q=0. Then

**Theorem MS.5:** K_U=RᵀD_U R, uniquely.

Positivity implies K_U Q=0 when QᵀK_UQ=0. For x=Sc+z the quadratic readout therefore equals cᵀD_U c; polarization proves uniqueness. A calibrated linear amplitude readout ℓ with complement blindness similarly has unique extension L=ℓR. Without positivity or full shift-blindness, zero response on pure complement states alone could leave cross terms; those assumptions are explicit here.

The law thus derived is a conditional selector for R,H* and K_U. Its extra premises are logically visible and testable. The current governed sources do not supply their adoption or physical calibration. No minimization objective, numerical physical target or universal sqrt2 principle is inserted.

## 6. Complete positive receipts and the recovered coarse current

For old G=I, let K_σ=RᵀΠ_σR for each of the15 old simplex coordinate projectors. Add a separate complement observable K_comp=QᵀQ. Then

Σσ K_σ+K_comp=H*.

All are positive. For nonzero fine x, the16 fractions xᵀK_a x/(xᵀH*x) are nonnegative and sum to1. They are exact quadratic support receipts, not a laboratory instrument, a quantum state-preparation claim or a derived Born law. A physical measurement channel and its disturbance/retention must be declared separately.

For the fine barycenter witness, old vertices0 and1 each have numerator1/4 and normalized fraction1/8. Every other coarse simplex fraction is0; the complement fraction is3/4. The complete total is1. Renormalizing only the two visible coarse outcomes to1/2 each would hide the3/4 complement support and would need an explicitly conditional/postselected interpretation.

The retraction is the metric adjoint of S and both sectors reduce the generator, so R A′H*=A_G R. Thus c=Rx obeys the old fixed-complex equation for every fine input, including retained z. The decoded old stocks q_σ=cσ² satisfy the sourced signed currents J_ση=2B_ση cσ cη, and a region U has its old Hasse cut continuity equation. This recovers Q170 on the **decoded coarse observables**, not additive fine-simplex stocks. The choice is coarse-first: C0559's local-first nonlinear observation can retain different covariance information and is not selected by these identities.

The residual remains in Qx. Coarse complement-blind readout is an observation contract, not an operation deleting residual information. The fine dimension149 includes134 direct-sum complement directions; those are not134 qubits or a tensor donor bank. Fine metric implementation, nonlocal cross terms, readout, initialization, clock, outgoing records and reset costs remain separate obligations.

## 7. Exact checks and source-selection frontier

Root replay uses the retained freshly generated subdivision implementation, not archived imported scientific scripts. It checks three H_w values, induced retractions and the complete classification identity, nine positive observable cases, the16-outcome partition, exact barycenter fractions, the diagonal support contradiction and16 decoded current replays. A separate constructor-team checker verifies H1/H2, all24 symmetries, observable witnesses and classification identities. The written proofs give the universal positive-metric and observable uniqueness statements; finite examples demonstrate nonselection rather than sampling a selected physical law. Source review checks provenance and the added premises. These are not independent human/CRL review.

The source record now distinguishes three outcomes: **EXACT native fixed-carrier selection** of I and coordinate stocks; **EXACT underdetermination/diagonal obstruction** for ordinary refinement under the tested inheritance requirements; and **EXACT conditional uniqueness** after premises A/B/C. The outstanding gate is a source-authored constitutive or measurement argument for those additional premises, or an alternative specified interface/current law. Current sources select neither the dense metric nor the cross-refinement observable ordering. Physical promotion remains0; no registry or global proof closure follows.
