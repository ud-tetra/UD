# THM-534 Session Consolidation Index — v1.2

**As-of:** 2026-10-22 (America/Chicago)  
**Repository:** [ud-tetra/UD](https://github.com/ud-tetra/UD) · **Research branch:** research/thm-534-theorem-session-audit-20261021 · **Draft review:** [PR #346](https://github.com/ud-tetra/UD/pull/346) · **Open dependency:** [issue #347](https://github.com/ud-tetra/UD/issues/347) · **Project:** [Unified Dynamics Project #1](https://github.com/users/ud-tetra/projects/1)

**STATUS:** Research/development only. Historical and current mathematical claims remain **typed by their stated hypotheses**. Independent non-constructor adversarial review remains PENDING. No physical bridge or registry promotion. **Physical promotion = 0**. Project-board item membership remains unverified; linking the Project URL here is not proof of membership. Nothing on this branch is merged to main.

## 1. Complete theorem-development chronology

| Version | Main source, next proof layer | Results | Correct scoped status |
|---|---|---|---|
| [v0.1](../theorems/UD_THM534_SESSION_DISCOVERIES_THEOREM_PACKET_v0.1.md) | Historical THM-534/561/562/563a/565a/565b source/quantifier audit | R1/R2 plus scoped downstream repairs | Conditional 6-edge spectrum; one-step kernel does not determine renewal |
| [v0.2](../theorems/THM534_MICRO_SOURCE_RECOVERY_AND_NO_GO_v0.2.md) | Natural S4 action on 6 unordered K4 edges | N1–N4 | Exact 2D family of equivariant Markov weights; symmetry, reversibility and continuous-time homogeneity do not select historical weights |
| [v0.3](../theorems/THM534_FORWARD_INCIDENCE_EVENT_PROGRAMME_v0.3.md) | Uniform lower/upper incidence events | N5–N7 | Both give different kernel than historical THM-534; arbitrary independent nonnegative length mixtures NO-GO; unit edge Hodge Laplacian = 4I |
| [v0.4](../theorems/THM534_ORIENTED_SEAM_GENERATOR_AUDIT_v0.4.md) | Flat and nonflat signed seam incidence | S1–S4 | Flat gauge no edge mixing; nonflat curvature example is a separate candidate, not a lawful topological boundary |
| [v0.5](../theorems/THM534_NATIVE_SEAM_SELECTION_RIGIDITY_v0.5.md) | U(1) and Z2 edge-face phases | S5–S9 | Ordinary chain closure forces flat gauge; 4096 Z2 sign masks tested; nonzero source required |
| [v0.6](../theorems/THM534_COVARIANT_SOURCE_CONTINUITY_v0.6.md) and [v0.6.1](../theorems/THM534_QUADRATURE_FLUX_TYPING_AMENDMENT_v0.6.1.md) | Marked curvature source, skew full-chain Cayley, phase quadrature | S10–S17 | Explicit conditional model preserves amplitude norm; phase source not physical current, magnitude-only sign NO-GO, source bound |
| [v0.7](../theorems/THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md) | Q162 gated vertex burden and signed face circulation | S18–S22 | Conditional conserved burden and nonzero abelian face cochain; gate/phase not source-selected |
| [v0.8](../theorems/THM534_GATE_SELECTION_AND_CIRCULATION_BUDGET_v0.8.md) | Hard-gate nonuniqueness, Lyapunov budget | S23–S28 | Under Q162 source-free relaxation all face circulation square-summable, hence decays; source route undetermined |
| [v0.9](../theorems/THM534_AUTONOMOUS_GATE_RESERVOIR_v0.9.md) | Positive-stock local reservoir/availability proxy | S29–S34 | A complete *candidate* state rule generates a nonuniform mask and transient circulation; passive replenishment still decays |
| [v1.0](../theorems/THM534_SUPPORT_READINESS_GATE_v1.0.md) | Prospective signed C0/C1 support-current integrity gate | S35–S41 | Exact candidate open→close→reopen, conserved separate supports; all masked-off no-reset obstruction |
| [v1.1](../theorems/THM534_FACE_CORE_RECEIPT_GATE_v1.1.md) | Q171–Q173 face/cell midpoint support receipts | S42–S48 | Conditional higher-degree reopening after all edge gates off; globally inactive face gates remain absorbing; repair of pre/current sign |
| [v1.2 final](../theorems/THM534_GLUED_FACE_CONTACT_RESET_v1.2.md) | Kminus 2-tet gluing, shared-face equal ownership, reset/no-reset contrast | S49–S55 | Exact chain/contact receipts; a conditional shared-face reset after externally admitted unshared-face contact; 256 masks, signed 12-element automorphism covariance; globally all-off NO-GO |

Names with **S** or **N** are versioned scoped theorem IDs; these are not physical laws or endorsements of historical theorem interpretations. Results from v0.1–v1.1 were previously committed and readback-confirmed. The **final v1.2 release** supersedes an earlier short v1.2 copy; S55 and its 12 signed automorphisms appear only in the final v1.2. Git commit history preserves the earlier draft.

## 2. Source and numerical provenance

- Frozen source stratum: **UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2)**, especially Q153–Q163 (burden, gate/current) and Q165–Q179 (chain support, gluing, equal-share cell ownership). Never treat equal numbers from distinct carriers as the same coefficient.
- **Historical THM-534 original proof** of weights \((1/2,1/6,1/12)\) is still *not recovered* from bounded prior retrieval. THM-561 cites those weights but does not prove their microscopic source. This absence does not establish nonexistence.
- **Q156** provides gate factorization, not a unique packet-state predicate. Conditional S23 selectors and v0.9 availability proxy are not frozen geometric closure.
- **Q171–Q173** provide support currents and hard contact multiplication; choosing sign of an executed face–cell midpoint receipt to determine next edge admission is a separately proposed constitutive readout.
- **Q177–Q179** supply unique equal-share ownership on glued cells, not a complete contact-admission/reset mechanism.
- **Physical time**, U(1) seam/holonomy normalization, Born six-edge outcome probability, empirical parameters and physical mass-energy conservation remain OPEN.

## 3. Final v1.2 release — exact bytes and reproducibility

- [Final S49–S55 manuscript](../theorems/THM534_GLUED_FACE_CONTACT_RESET_v1.2.md).
- [Final proof/dependency delta](../theorems/THM534_GLUED_CONTACT_CLAIM_LEDGER_DELTA_v1.2.md).
- [SymPy complete replay](../theorems/verify_face_reset_v1_2.py) and [independent-code Fraction replay](../theorems/verify_face_reset_fraction_v1_2.py).
- [Executed SymPy receipt](../theorems/receipts/v1.2/sympy_receipt.txt) and [Fraction receipt](../theorems/receipts/v1.2/fraction_receipt.txt).
- [Source and SHA-256 manifest](../theorems/THM534_GLUED_FACE_CONTACT_RESET_v1.2_MANIFEST.json).
- [Exact original ZIP](../releases/THM534_GLUED_FACE_CONTACT_RESET_v1.2_RELEASE.zip).

The two scripts were **replayed locally** on the final v1.2 release ZIP during the 2026-10-22 sync. PASS: exact 23-simplex Kminus gluing, 256 binary face–cell gate masks, shared ownership, conditional next-face reset witness, both original signed support receipts, all 12 signed carrier automorphisms. Every standalone v1.2 file and ZIP was published by Git blob with its original SHA-1 Git blob identity verified against the locally hashed bytes. This is **same-constructor replay**, not independent non-constructor review.

Specific exact witness (S52–S53): independent admitted face 013→cell 0123 gives cell-core stock gain \(256/4225\); a **postulated** next-event reset enables the shared-face contact and gives signed shared current \(J=-61824/511225\). Equal-share ownership then assigns \(J/2=-30912/511225\) and \(-J/2=30912/511225\) to the two owned cell accounts. The neighboring disabled contact is not thereby active. Without an admitted higher contact or external/latent source, an entirely contact-dead state remains absorbing.

## 4. Session release archives

Exact-byte ZIPs (seven historical plus v1.2 final) are present in [research/releases](../releases) and individually inventoried in [SHA-256/Git-blob archive manifest](../releases/THM534_SESSION_RELEASES_SHA256_v1.2.json). For v0.1–v0.4 the theorem documents/verifiers are present as text; there were no historical release ZIPs in the locally available session uploads. Binary publication does not retroactively make a candidate a theorem.

**Artifacts covered:** theorem-form manuscripts, compact and local-executed verifier scripts where supplied, raw numerical/exact receipt logs, source hashes and release bundles. Some loose v0.5–v1.0 historical text files in Git predate exact archive publication and may differ in formatting or abbreviated content from the original ZIP; the exact ZIP manifest and archived bytes take precedence for matching the original executed release.

## 5. Contradictions, negative findings and scope repairs preserved

1. Spectral equality or sector degeneracy does **not** prove Standard Model particles, physical masslessness or electron identification.
2. Signed oriented face-boundary kernel and the unsigned S4 face-sum representation are not the same typed module without an explicit intertwiner.
3. Target spectrum inversion is *not* a forward THM-534 transport-event derivation.
4. Flat seam rephasing cannot create edge transfer for the given unit-Hodge generator; genuinely nonflat twists break old simplicial nilpotency and require a separate covariant source accounting.
5. Chain-amplitude squared norm, Q162 vertex burden, Q171–Q172 face/cell squared support, Q177 owned support and empirical energy are distinct conserved/accounted objects.
6. Q162 passive relaxation plus arbitrary gate switching has finite total circulation and cannot sustain asymptotic nonzero face circulation. The v0.9 passive reservoir also cannot overturn this no-go.
7. A separately stipulated oriented rotor can sustain a cyclic current, but its native packet source/evolution rule is OPEN.
8. A sign predicate on **prospective** Q171 instantaneous current can disagree with the sign of executed **midpoint** stock transfer (S48). The v1.1 corrected delayed rule remains CANDIDATE.
9. Edge-only all-off can recover if a separate higher-degree contact is admitted. If **every face/cell contact** is also off and no memory/source drives it, the all-off state is absorbing (v1.1 S46, v1.2 S51).
10. Glued equal-share ownership does not derive the unique reset predicate; local and permanently-off interpretations can both satisfy continuity. The final S55 verifies only covariance under the twelve actual Kminus automorphisms, not a larger physical symmetry.

## 6. What is still missing for the central physical bridge

**OPEN_GATED:**
- native generator of hard **face–cell contact admission** \(h_f^{23}\) from primitive \((\chi,b,\tau,\sigma,\rho)\) plus boundary/initial and source/sink account, beyond the conditional flags;
- positive-stock open-system source, reservoir ownership and recovery/reset receipts that remain valid across glued complexes, including a globally contact-dead case;
- independent route/holonomy selection, action normalization, event-clock correspondence and measured observable;
- microscopic source of original THM-534 six-channel stochastic probabilities, renewal/memory mechanism and Born-facing outcomes;
- truly independent external reviewer and held-out physical tests with frozen acceptance rules.

**Next highest-value execution:** recover or derive Q173 contact admission and a positive reset source on a glued carrier, then independently test its signed ownership/current ledger. Continue development only on a *separately named assumption branch* if an unproved source or reset is introduced. Preserve source-free no-go results.

**Governance:** no claim promotion from the existence of a formula or finite numerical replay. Development only / physical promotion 0.
