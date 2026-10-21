# THM-534 inter-grade permission audit, v1.2

October 21, 2026. EXACT CONDITIONAL finite classification and candidate completion. Development, no registry entry. Physical promotion 0. Outside peer review pending. Proposition labels P1–P5 are local labels, not global theorem allocations.

## Source reconciliation and limits

Main was read at `f0a2ee841cb0feed3ec5e700bfc0a6521cbda2f4`. The THM research branch advanced to `b8701df319db7391a1065aa56c4f957f221844a5`, adding `THM534_FACE_CORE_RECEIPT_GATE_v1.1.md`. That source explicitly leaves native face admission and sign/AND selection open. Its isolated face–cell support system and subsequent burden-mask readout are distinct from PR370's full support-amplitude readiness selector.

The attached reconstructed files `packet_modulation_layer.md`, `seam_phase_transport.md`, `coherence_equation.md`, `master_action.md`, `packet_field_equation.md` and `carrier_definition.md` contain only a placeholder heading and placeholder sentence. They provide no permission predicate. Q169–Q173 of the attached coefficient ledger provide the underlying chain, support continuity and hard face contacts, but do not establish that every transport-masked operator must itself remain a chain complex.

This audit therefore asks a **conditional structural question**: if the effective gated boundary operators must retain both chain identities, which diagonal contact masks are allowed? This is an additional requirement under test, not a recovered native UD selection law. Nonzero effective chain products are reported as algebraic defects, not physical curvature.

## Exact contact family

Let B1, B2, B3 be the standard signed boundaries of the filled tetrahedron, in edge order 01,02,03,12,13,23 and face order 012,013,023,123. Write

\[
d=B_3=(-1,1,-1,1)^{\mathsf T},
\quad B_1B_2=B_2B_3=0.
\]

Declare binary contact masks

\[
h\in\{0,1\}^6,\qquad a,t\in\{0,1\}^4,
\]

and the particular effective boundary family

\[
D_1=B_1\operatorname{diag}(h),\quad
D_2=B_2\operatorname{diag}(a),\quad
D_3=\operatorname{diag}(t)B_3.
\]

Here h masks vertex–edge support coupling, a masks each face's edge–face column, and t masks individual face–cell contacts. These three roles are distinct. The results are restricted to this family, not arbitrary incidence-by-incidence masks, soft gates, changing simplex metrics or general connection operators. No geometric simplex deletion is implied.

## P1 — Complete chain-compatibility classification

The identities

\[
D_1D_2=0,\qquad D_2D_3=0
\]

hold if and only if both conditions below hold:

1. Every face with a_f=1 has its three boundary-edge h bits equal, either 000 or 111.
2. The four products a_f t_f are all equal, either all zero or all one.

**Proof.** A selected face's column in D1D2 is the signed boundary of its triangle weighted by its three edge h values. At each of its vertices, cancellation requires equality of the two incident triangle-edge values. Thus all three must agree, and equality also suffices.

For the second condition,

\[
D_2D_3=B_2\operatorname{diag}(a_ft_f)d.
\]

The tetrahedron has ker B2=span(d). To verify this directly, the three columns for faces 012,013,023 are independent on rows 12,13,23, while B2 d=0 and d is nonzero. Hence B2 has rank three and a one-dimensional kernel. A vector with entries a_f t_f d_f lies in that kernel exactly when its four coefficients a_f t_f agree. QED.

No symmetry assumption on h,a,t is needed. The condition itself is covariant under signed simplex relabeling.

## P2 — Exhaustive counts and a forced separation

Among all 2^(6+4+4)=16,384 binary triples, exactly **1,652** satisfy both identities. With every face–cell contact off, 162 do; with every face–cell contact live, 66 do.

**Proof of counts.** The numbers of h masks with m monochromatic triangle boundaries are

| m | Number of edge masks |
|---:|---:|
| 0 | 18 |
| 1 | 32 |
| 2 | 12 |
| 4 | 2 |

For a fixed h, a may select any subset of its m monochromatic faces. When m<4, the product condition requires a_f t_f=0, giving

\[
\sum_{s=0}^m\binom ms 2^{4-s}=2^{4-m}3^m
\]

choices. For m=4, there is one additional all-one product choice, giving 82. Thus

\[
18(16)+32(24)+12(36)+2(82)=1652.
\]

When t=0, every admissible a is allowed, giving 18+32(2)+12(4)+2(16)=162. When t=1, a is either all zero, for any of the 64 edge masks, or all one, requiring h to be uniform, for two further cases. Hence 66. The exact verifier independently multiplies the matrices for all 16,384 triples and checks equivalence to P1, not just these totals. QED.

**Corollary.** In this family, if all face–cell contacts are live and h is mixed, chain compatibility forces

\[
a=(0,0,0,0).
\]

**Proof.** With t=1, P1 requires a to be constant. If a=1, every triangle's h values agree; overlapping triangles then force all six h values to agree. This contradicts a mixed h. Therefore a=0. QED.

This separates permissions by grade. It does not mean all support dynamics stop: D3 remains live even when D2=0.

## P3 — Consequence for the PR370 recovery branch

PR370's enabled-face branch fixes a=t=1 and allows the prospective support selector to change h. The initial all-off h=0 is compatible with both chain identities. Its exact first reopening is h=100000, which is mixed. Keeping a=t=1 at that next event gives

\[
D_1D_2=B_1\operatorname{diag}(1,0,0,0,0,0)B_2\ne0,
\qquad \|D_1D_2\|_F^2=4.
\]

The rank of this defect is one: it is the outer product of the nonzero B1 column for edge 01 and the nonzero B2 row for that edge.

Thus PR370's norm conservation and exact reopening remain valid, but its permanently enabled edge–face permission cannot be called chain compatible throughout that mixed-mask history. Its text already excluded a claim of effective chain nilpotency. This audit sharpens that limitation without retracting the conditional witness.

The shared-edge-permission variant D2=diag(h)B2 has the same first product, since h is binary. It also does not automatically restore the first chain identity at mixed masks. These variants must not be silently identified with the diagonal face-column family of P1.

## P4 — A unique maximal completion under explicit extra assumptions

Add all three assumptions:

- the effective chain identities hold;
- every face–cell contact stays live, t=1;
- subject to those constraints and the supplied h, maximize the number of live face columns a_f.

Then the unique completion is

\[
a^*(h)=
\begin{cases}
(1,1,1,1),&h\text{ is uniform},\\
(0,0,0,0),&h\text{ is mixed}.
\end{cases}
\]

**Proof.** For mixed h, P2 leaves only a=0. For uniform h, both a=0 and a=1 satisfy P1, and all-one a uniquely maximizes the count. QED.

This is a **candidate maximal-permission policy**, not a native law. Maximal contact availability is an extra constitutive preference; neither norm conservation nor the chain identities alone supplies it. The policy is permutation-equivariant and introduces no additional continuous coefficient. That does not establish parameter-free physical dynamics: the step, metric, input preparation, h selector and maximality assumption remain declared ingredients.

For the PR370 support preparation

\[
x=(3,2,1,0),\quad y=(1,1,1,1,1,1),
\quad f=(-3,-3,0,0),\quad w=0,
\]

retain the original prospective h selector and dimensionless Cayley step epsilon=1/4, but recompute a=a*(h) before every event. The skew generator has the corresponding D1,D2,D3 blocks and their negative transposes. It remains pointwise norm-preserving, and both chain products vanish at every event.

The first event still reopens edge 01, because h=0 permits maximal a=1 and therefore its first update is unchanged. At the next mixed mask h=100000, a becomes 0000. The new eight-event history is recorded in RESULTS.json; it is not represented as the unchanged PR370 trajectory. The full support norm remains 38. The exact checker verifies 64 supplied edge masks and 24 signed permutations at three representative epochs, as well as each event's dynamic latent-support receipt.

Closing a does not discard the existing face amplitudes or edge amplitudes. Both remain in the full state and norm. It changes their transport permissions only.

## P5 — Reconcile the new face–cell receipt branch without merging typed states

The newer research-branch v1.1 intentionally isolates face–cell support transport, with D2=0 and D3=B3. If vertex–edge support dynamics were adjoined as a direct sum, any D1 would retain both chain identities. Thus its isolated higher-grade architecture avoids P3's particular chain defect.

However, its actual edge mask controls **vertex-burden transport**, selected from a completed face/core receipt. It is not PR370's support-amplitude product selector. It has no specified C0/C1 support preparation that can be equated to PR370's. Its support total is 3 and burden/reservoir total is 5, versus PR370's full support total 38 and separate stock total 4. None of these totals has a physical-unit conversion supplied here.

The v1.1 isolated face–cell skew convention has upper block −B3 and lower +B3 transpose. PR370 uses the opposite cell-block convention. A diagonal change of cell-amplitude sign conjugates one chart to the other; signed receipts must be transformed consistently before comparing. The new verifier checks that conjugacy rather than silently mixing the two charts.

The new exact verifier independently reconstructs the v1.1 fourteen-event oscillator and midpoint face receipts, reproduces the first receipt

\[
\mathcal J_0^{23}=\tfrac1{289}(-18,50,16,16),
\]

and checks stock nonnegativity, total 5, support total 3, and the inherited passive burden variance bound at every event. No upstream script is imported or executed by this checker. Its successful replay remains constructor verification, not outside peer review.

## Decision reached and next dependency

The inter-grade freedom is now constrained by an exact classification. Under the additional effective-chain requirement, selective vertex–edge permissions plus live face–cell transport force a disconnected edge–face interface in the stated family. A conditional maximal-contact completion exists and preserves the first recovery event.

What has **not** been recovered is an upstream rule requiring effective-chain nilpotency for transport masks, maximal contact count, persistent face–cell admission, or the receipt sign/AND selector. The underlying filled complex's B1B2=B2B3=0 does not by itself require those identities after arbitrary transport masking. Keeping a transport defect is a mathematically different branch and must be accounted for, not labeled physical curvature by analogy.

The next source requirement is therefore specific: does the native packet law preserve the chain identities for its effective transport operators, and does it maximize admitted contacts or use another constitutive criterion? A source that answers neither cannot uniquely select the completion. No held-out recovery test or physical claim is advanced while that selection remains open. Intrinsic geometric closure, physical action units and matter correspondence remain separate dependencies. Physical promotion 0.
