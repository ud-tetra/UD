# Subdivision metric source and scope review v0.1

14 October 2026 UTC. Development — no registry entry. Physical promotion 0.
Reviewer: constructor-team source/scope audit; not independent human/non-constructor review.

## Sources actually inspected

Current atlas `dist/assets/sources.json`, full records R31, R33, R34 and C0243; C0173's geometric metric interface; attached historical coefficient ledger v0.39, Q157–Q179, and complete CRL2 subdivision governance proposal v1.0. The missing `Gap2_FINAL_Finite_Genesis.png` was not available and supplies no evidence. Source code was not executed.

R31 retains ordinary barycentric subdivision S with SᵀS = ⊕(k+1)! I, old Euclidean support Q165 and unweighted incidence generator Q169. Its 11-dimensional donor and 123-dimensional blank-bank completion funds the unnormalized Euclidean target Sc. R33's common scalar S/√24 makes the target contractive but attenuates the unit vertex readout and fails generator intertwining. R34 proves a strict Euclidean/unweighted contradiction: unit singleton vertex readout plus contraction forces Te_i=e_{singleton i}; old and new generator squared norms are 3 and 7. This excludes that declared contract, not every alternative metric/operator.

C0243 separates fixed-metric operator modification from transported coordinates. A nonorthogonal basis change must transport the metric, source and observation, and leaves original dynamics similar. A changed metric with incidence fixed is a genuinely conditional new operator. C0173 demonstrates admissible but unselected Gram-ratio metrics; it explicitly does not establish subdivision invariance, a unique norm, physical energy or shape dynamics. Neither selects the construction below.

The historical ledger's Q165/Q170/Q171/Q172 are sums of squared simplex coefficients and local incidence currents in the original Euclidean carrier. A dense metric is not their direct continuation. Q175's √2 is a specified K+ spectral frequency, not a universal subdivision factor. Q157–Q160 and Q178 retain renewal/source semantics open. The governance proposal allows analysis in a development lane without registry promotion, and requires non-constructor review plus custodian ruling for promotion; this review does not satisfy that gate.

## Exact conditional construction

Let K be the filled oriented tetrahedron. Let K′=sd K be its ordinary barycentric flag complex, with increasing flag orientation and signed usual subdivision map S. Counts are f=(4,6,4,1), f′=(15,50,60,24), total dimensions 15 and 149.

For every nonempty original face F, define p_F = |F|⁻¹ Σ_{i∈F} e_i. Define the degree-preserving affine exterior chain retraction

R_k[F_0<...<F_k] = p_{F_0} ∧ ... ∧ p_{F_k},

expanded in the original increasing simplex basis. Each p_F has augmentation 1, so contraction with the augmentation functional proves ∂R=R∂′. For an original k-simplex, each permutation flag in its subdivision has determinant sgn(π)/(k+1)!. Including subdivision orientation sgn(π), all (k+1)! flags contribute 1/(k+1)! of the original simplex. Hence RS=I exactly.

Set Q=I−SR. Then Q²=Q, im Q=ker R, QS=0, RQ=0 and ∂′Q=Q∂′. In every degree choose an independently supplied SPD matrix W_k on the new coefficient space and set

H = RᵀR + QᵀWQ.

For every x, xᵀHx = ||Rx||² + (Qx)ᵀW(Qx). If this is zero, Rx=Qx=0 and x=SRx+Qx=0. Thus H is SPD. Also HS=Rᵀ and SᵀHS=I. The old image im S and ker R are orthogonal under H and are both boundary-invariant subcomplexes.

Let ∂′†_H = H⁻¹∂′ᵀH and A′_H=∂′†_H−∂′, while A=∂ᵀ−∂ uses the old Euclidean metric. Because the decomposition is orthogonal and reducing for ∂′, it also reduces ∂′†_H. Testing against Sc and ker R proves ∂′†_H S=S∂ᵀ; therefore A′_H S=SA. The source subspace exactly retains its old dynamics and old norm.

This is a conditional construction satisfying all three map tests: SᵀHS=I, ∂′S=S∂, A′_H S=SA. It retains the literal old-vertex singleton coefficient for Sc. It does not contradict R34: target contraction is under H and the post-event generator is A′_H, rather than Euclidean norm and unweighted A′.

## Why diagonal degree compensation is insufficient

The naive choice H_k=I/(k+1)! gives SᵀHS=I and retains the chain identity, but generally does not make im S a reducing boundary subcomplex. For one old vertex i, H_0=I and H_1=I/2 give ∂′†_H S_0e_i=2∂′ᵀe_{singleton i}. It has seven incident flag edges. S_1∂ᵀe_i instead has six segments from the three old incident edges. In explicit flag orientation their difference has magnitude 1 on three first edge segments, magnitude 1 on three other-end segments, and magnitude 2 on the three vertex-to-face flags plus vertex-to-tetrahedron flag. Thus

||(A′_H S−SA)e_i||²_Euclidean = 22,
||(A′_H S−SA)e_i||²_H = 11.

Both are nonzero. The old unweighted defect squared norm was 7, as R34 records. Norm preservation and chain compatibility alone do not guarantee adjoint/generator compatibility.

## Resource, readout and selection limits

The complement has degree dimensions (11,44,56,23), total 134. Its boundary ranks are (11,33,23); it is an acyclic subcomplex. The full 149-coordinate carrier is not identical to the 15-coordinate old carrier. An isometric old-code embedding is not a full device with zero initialization/reset cost. A complete reversible interface requires an explicit 134-dimensional complement input/output, its preparation, retained records and any reset resources. The conditional linear identification (c,z)↦Sc+z, z∈ker R, is an isometry from the direct-sum metric ||c||²+zᵀWz to H; physical preparation and operation remain open.

On the admitted code Sc, R decodes exactly to c. On arbitrary states the complement can affect coordinate readouts, so simply reading singleton coefficients is not an automatically robust old observable. Sources, readout and code admission must be specified. Dense H includes cross terms, so it does not supply nonnegative per-simplex Q170 stocks or the original local Q166/Q171/Q172 currents. Complement weights, nonlocal weighted-adjoint couplings, locality, readout and spectrum must be charged to the model scope.

W is not selected by the source. Degree-dependent choices can alter complement dynamics while leaving old-code intertwining intact. Positivity, chain identities and exact inheritance therefore establish existence, not a native UD constitutive law. Any change in metric, map, complement law, geometry or readout requires descendant re-derivation. No universal √2, distortion-free physical renewal, unlimited refinements, saturation ceiling, energy balance, laboratory clock or GR/QFT bridge follows.

Recommended disposition: EXACT CONDITIONAL existence and inherited-code identities; CANDIDATE authored metric/retraction interface; old R31/R33/R34 no-go scopes preserved; OPEN source selection, complement dynamics/resource accounting, physical norm/readout, locality, iterated behavior and human review. Physical promotion 0.
