# UD theory manuscript: gap inventory and closure order

14 October 2026 · Development — no registry entry · Physical promotion: 0

## Audit scope and result

Audited the complete current Library text of `UD_Theory_Narrative_Manuscript_v0.1.md`: 525 lines, 34,614 bytes, all 13 main sections, abstract, scope statement and appendices. The source read was complete. This is a manuscript audit, not a new audit of the live portal or the full UD programme. An item missing here may already be developed elsewhere; source reconciliation must precede declaring a project-wide gap.

The audit identifies **33 distinct development obligations** after consolidating repeated wording, plus **four editorial/provenance obligations**. Several are conditional on the larger interpretation being pursued. An explicitly supplied primitive is sufficient for a conditional model; it becomes a derivation gap only when the manuscript seeks to explain that primitive natively. Proved obstructions are not counted as unproved results.

The central gaps concern three missing connections: binary labels to amplitude evolution; existing complexes to configuration-changing dynamics; and prepared finite apparatus to a complete operating cycle. Geometry, units and gravitational normalization are downstream of these connections for the narrative's proposed unified route.

## Ranking method

Priority is a recommended work order, not a measured readiness score. It weighs dependency leverage, importance to the manuscript's central thesis, specificity of the next mathematical output, and feasibility within the present finite setting. Within a branch, prerequisites precede dependent claims. Across branches, independent work may proceed concurrently; no total order is mathematically mandatory.

- **P0:** definitions and comparison contracts needed to make closure testable.
- **P1:** finite theoretical connections and tractable mathematical gaps.
- **P2:** complete record mechanisms, preparation and resource closure.
- **P3:** physical geometry, normalization and identification bridges.
- **P4:** optional stronger architecture claim.

Dependencies listed below describe this recommended programme. They are not a theorem that no other route can succeed. Source coefficients, alternative observations or different apparatus architectures could change the graph.

## Ranked development inventory

| Rank / ID | Priority | Location and exact gap language | Required closure output | Dependencies in this programme |
|:--|:--|:--|:--|:--|
| 1 / G01 | P0 | §§2.1, 7.3: “depends on the output distributions, permitted decisions and error criterion”; “name the retained property, tolerance and duration” | Fix the state/readout pair, retained property, admissible initial states, disturbances, duration and resource budget. Define success and failure before comparison. | None; different branches need their own contracts |
| 2 / G02 | P1 | §8: “only after noise or finite resolution is specified” | Specify a readout channel and derive distinguishability/error versus time, including snapshot zeros and conditioning. Preserve the noiseless result rather than pretending it already supplies a gradual loss curve. | G01 |
| 3 / G03 | P1 | §7.2: “do not select … a frequency spectrum … or a stability advantage” | Compute the exact five-cell spectrum and observable sectors; compare the core-star with a declared alternative under equal preparation, coupling and observation constraints. Distinguish spectrum calculation from robustness or selection. | Carrier already given; comparison uses G01 |
| 4 / G04 | P1 | §9.4: “does not certify coverage without a probability model”; “requires residual cross-covariances” | Import or derive a correlated-noise model, exact residual covariance and a justified simultaneous decision/coverage rule. Existing Paper II formulas should be integrated before attempting new theory. | G01; G02 if using the same readout channel |
| 5 / G05 | P1 | §2.2: “A source law relating them must be supplied or derived” | Define the joint binary/amplitude state and an event rule linking amplitude history to label changes, with frame covariance and conservation/resource conditions. | G01 |
| 6 / G06 | P1 | §5: “Symmetry and norm conservation alone do not force that selection”; “A constitutive rule must answer how strongly” | Declare a source functional for the three allowed skew channels; derive its coefficients or prove residual freedom. Fixed unit weights remain legitimate declared inputs if no stronger claim is made. | G01; G05 if coefficients use binary events |
| 7 / G07 | P2 | §5: “its scalar strength remains a separate choice” | Supply the auxiliary context state, its dynamics and an independently normalized interaction strength. Symmetry typing and tensor covariance are already available; do not redo them as the missing scalar derivation. | G06, and G05 if the context is label-sourced |
| 8 / G08 | P1 | §6.2: “require an explicit identification map” | Define passage from independent cell copies to unique-simplex interface coordinates, including residual modes, sign/phase data, adjoints and the support/resource balance. | G01; no selector required for an interface theorem |
| 9 / G09 | P1 | §§6.3, 13: “native configuration-changing rule”; “source must still determine which attachment occurs” | Specify legal moves and their source-dependent admission rule, including refusal and tie cases. Separate move availability from event selection. | G05, G06, G08 for a native integrated route |
| 10 / G10 | P1 | §§6.3, 13: “its own state-transfer law”; “complete state transfer” | Define the state update across differing carrier dimensions. Explicitly choose which mutually incompatible linear contracts are relaxed, or supply a nonlinear/state-restricted/reservoir extension; prove the chosen balance. | G08, G09 |
| 11 / G11 | P1 | §7.3: “when a stated interaction makes that agreement alter formation or survival” | Define compatibility and prove how it changes attachment, leakage, survival or an admission observable. An agreement score alone is insufficient. | G01, G06, G09, G10 |
| 12 / G12 | P1 | §7.1: “Open or nonlinear dynamics requires a separate analysis”; §4.1: “how disturbances affect the model” | Derive perturbation bounds under an admitted disturbance law. If attracting formation is claimed, declare and analyse dynamics outside the fixed orthogonal flow; identify what is dissipated or exported. | G01, G06; G10 for changing carriers |
| 13 / G13 | P1 | §7.3: “common initial ensemble, configuration-changing rules, state transfers, disturbances and resources” | Compare formation probability, survival conditional on formation, occupancy and growth separately. Derive a finite preference result under common opportunities and resources; avoid universal ranking from one fixture. | G09–G12, G01 |
| 14 / G14 | P1 | §10: “Every apparatus claim must name that encoding, its joint state and its readout”; “not a derivation of quantum theory” | Specify the map from classical/complex chain description to the declared quantum apparatus representation, including equivalence classes and operational observations. A conditional encoding may suffice; deriving quantum theory is a distinct stronger target. | G01; G05 for the full common-substrate route |
| 15 / G15 | P2 | §§9.2–9.3: “not an authentication or acquisition theorem”; “References are part of … required resources” | Specify a local receipt-acquisition instrument with root signs/phases, zeros, backaction and correlated reference reuse. Establish that its output matches the reconstruction statistic on its admitted domain. | G02, G04, G14; G16 for a supplied reference mechanism |
| 16 / G16 | P2 | §§10.1, 11.2–11.3: “prefixes and preparation are supplied”; “must enter the ledger”; “clock preparation” | Give a complete initial clock/reference/fuel preparation contract, with admitted nonstationary coherence, seed energy, variance and preparation errors. Distinguish a resource supplied as input from a native preparation derivation. | G14, G01 |
| 17 / G17 | P2 | §11.1: “donor … independent”; “admitted bank error” | Define a complete bank state and derive/certify its distance from the independent target, preserving history correlations. Good marginal donor quality cannot substitute for this result. | G16, G01 |
| 18 / G18 | P2 | §10.1: “do not prove locality on the work registers” | Construct the dressed-word interactions under explicit locality, coupling-norm and connectivity restrictions; bound any simulation/ancilla overhead on the joint domain. | G14, G16 |
| 19 / G19 | P2 | §13: “complete production-to-capture trigger” | Derive a completion-sensitive trigger with false-trigger and missed-trigger branches, timing/launch uncertainty and owned control costs. A terminal projector or endpoint time alone does not implement it. | G16, G18 |
| 20 / G20 | P2 | §§10.2–10.3: “off-switch”; “open-system mechanisms with their own resources”; “not continuously monitored survival probabilities” | Choose timed shutdown/protection, a bounded static horizon, or an open reservoir. Prove retention under disturbances and, if monitoring is claimed, derive the monitored instrument and survival statistic separately. | G01, G12, G19 for triggered retention |
| 21 / G21 | P2 | §11.1: “uniform operation bounds on the admitted joint states”; “Isolated-input results do not automatically meet” | Prove every production/capture/renewal comparison on one compatible joint domain, with arbitrary retained spectator and interleaving. Then apply telescoping without hidden independence or postselection. | G14, G17–G20; each operation may be proved as it is built |
| 22 / G22 | P2 | §§11.3, 13: “does [not] establish an autonomous router”; “failure histories and exhaustion” | Construct finite donor/output routing, correlation export, attempt accounting and END_OF_SUPPLY refusal. Include failed attempts; prove no resource wrap. | G17, G19–G21 |
| 23 / G23 | P2 | §11.3: “Cost requires …”; “information-per-cost comparisons can omit” | Produce a complete vector resource ledger and a retained-information comparison for one architecture. Name the scalar objective if costs are collapsed; account for energy, variance, switching, time, blanks and renewal. | G15–G22 for the complete apparatus; partial ledgers may start earlier |
| 24 / G24 | P2 | §12: “Entropy must follow from a declared state and coarse-graining”; “not a thermodynamic entropy-production theorem” | Declare the joint state, coarse-graining and thermodynamic environment. Derive record-quality quantities separately from coarse-grained entropy and entropy production; identify irreversibility and exported correlations. | G14, G20–G23 for an apparatus-specific derivation |
| 25 / G25 | P3 | §12: “Physical boundary area requires a geometric map and units” | Define the relevant boundary and a metric/area functional with scaling and units. A purely combinatorial proxy can be closed earlier but must retain that label. | G27–G29 for physical area; finite boundary definitions can start now |
| 26 / G26 | P3 | §12: “a capacity or scaling mechanism must link the declared records to that boundary” | Prove retained-information or record-entropy scaling under complete resources, including correlations, nonuniformity and finite-size corrections. Distinguish an upper capacity bound, extensivity and equality with area. | G23–G25 |
| 27 / G27 | P3 | §12: “controlled coarse-graining” | Define coarse-graining maps and admissible ensembles; prove which observables survive and control approximation error/refinement dependence. A finite reduction result alone is not a continuum theorem. | G01, G08, G12; G24 for record-based coarse-graining |
| 28 / G28 | P3 | Abstract, §§3.2, 12: “does not derive a physical metric”; “physical geometry” | Construct the effective metric, signature and causal/transport interpretation from the declared variables; establish covariance and refinement behaviour. Declared coordinate Euclidean norm is insufficient. | G27; additional constitutive input must be explicit |
| 29 / G29 | P3 | §§4.1–4.3, 10, 12: “no laboratory unit assigned”; “does not calibrate proper time”; “action scale and a clock map” | Supply a consistent dimensions/units dictionary, connect model evolution and event counts to clocks, and independently determine normalization. Separate mathematical scale conventions from empirical calibration. | G01; G28 for metric-derived proper time; may run alongside G27–G28 |
| 30 / G30 | P3 | §3.1: “does not … derive the dimension of physical space” | If pursued, demonstrate why the emergent physical dimension follows from the effective description or a selection principle. Topological cell dimension and register dimension cannot be substituted. | G13, G27, G28 for a selection-based route |
| 31 / G31 | P3 | §1: “earn each … interpretation through a further map to observables”; §§4.2, 5: “needs an independent observation map”; “not … a derived physical gauge group” | Build explicit observable/identity maps for physical current, energy, material structures and any gauge field claim. State separate equations and conservation laws for each identification. These are several physical dictionaries, not one numerical match. | G06, G13–G15, G28–G29, according to the claimed identity |
| 32 / G32 | P3 | §12: “does not derive … gravitational entropy density, Newton's constant or Einstein's equations”; “independently normalized couplings” | Derive the horizon/thermodynamic construction, its admissibility conditions and source normalization without backsolving from G, then demonstrate the gravitational field relation. Retained information per boundary alone is insufficient. | G24–G29, G31 and an explicit horizon/energy-flux bridge |
| 33 / G33 | P4 | §3.1: “does not prove uniqueness among candidate architectures” | Compare admissible alternative carriers under common requirements. Prove uniqueness only if required; otherwise retain tetrahedra as a declared candidate and explain the choice without a universal claim. | G01; deeper comparison may use G13, G27–G30 |

## Section-by-section coverage

| Manuscript area | Consolidated obligations |
|:--|:--|
| Abstract and source/scope | G09, G16–G22, G25–G32; E01 below |
| §1: purpose and packet interpretation | G01, G09–G13, G31 |
| §2.1: state and resolvability | G01, G02, G14 |
| §2.2: binary labels | G05; clock/count distinction in G29 |
| §3.1: carrier choice and dimension | G30, G33 |
| §3.2: declared inner product | G28; carrier typing already defined |
| §4.1: flow and disturbances | G06, G12, G29 |
| §4.2: physical current interpretation | G31 |
| §4.3: recurrence versus clock | G29 |
| §5: interaction typing and strengths | G06, G07, G31 |
| §6.1: spectra and irreversible history | G24 if irreversible records are claimed; the displayed spectra and no-period result are not gaps |
| §6.2: independent-copy assembly | G08 |
| §6.3: topology/state transfer | G09, G10 |
| §7.1: attraction and perturbation | G12 |
| §7.2: prepared growth and five-cell example | G03, G09, G13, G25/G28 for physical embedding |
| §7.3: preference, survival and agreement | G01, G11–G13 |
| §8: reduced observation and visible dynamics | G02; visible-closure criterion is already proved |
| §§9.1–9.3: identifiability and acquisition | G15, G16; real/complex reconstruction is already proved |
| §9.4: uncertainty and acquisition | G04, G15 |
| §10: quantum apparatus dictionary | G14, G21, G29 |
| §10.1: word, clock and locality | G16, G18, G19, G21 |
| §10.2: capture and retention | G19–G21 |
| §10.3: closed first-entry limitation | G20; the obstruction itself is not open |
| §11.1: bank, renewal and composition | G17, G21, G22 |
| §11.2: coherent supply | G16, G17 |
| §11.3: cost and router | G22, G23 |
| §12: entropy, area, geometry and gravity | G24–G32 |
| §13: next targets | Repeats G05–G13, G16–G23, G27–G31; no additional distinct obligation |
| Appendices and references | E01–E04; optional expansion does not add an unproved theorem automatically |

## Four editorial and provenance obligations

These are important manuscript tasks but should not inflate the count of missing theoretical mechanisms.

| ID | Priority | Passage / issue | Closure |
|:--|:--|:--|:--|
| E01 | Immediate | Scope and Appendix B: “No fresh audit of subsequent live portal or GitHub amendments” | Reconcile current papers and amendments against M5, record exact hashes and determine which G-items already have later solutions. |
| E02 | High | Appendix A: detailed contact family deferred | Integrate the source's contact-readiness/admission results where they reduce the formation gap; retain their supplied source contracts. |
| E03 | Medium | Appendix A: radial refinement deferred | Add a confinement/refinement chapter if needed by the theory narrative. Existing conditional compact-resolvent and convergence results are not newly open merely because omitted. Audit any newly asserted completeness or cyclicity separately. |
| E04 | High before publication claims | Appendix B: constructor checking is not independent review; selective synthesis | Improve theorem-level source citations, include a precise novelty boundary and obtain non-constructor review before registry promotion. Review does not substitute for deriving a missing mechanism. |

## Proved limitations: change the contract, not the conclusion

1. **Counts do not force dynamics (§2.2).** A fiber size cannot derive a stage count or period. G05/G29 need additional laws.
2. **Symmetry does not select channel strengths (§5).** More representation arithmetic will not determine a source coefficient. G06/G07 need constitutive input.
3. **The stated linear jump contracts conflict (§6.3).** The norm-2-to-norm-3 witness excludes simultaneous chain compatibility, boundary fixation and isometry. G10 must explicitly relax or extend the contract.
4. **Fixed orthogonal flow cannot attract to a different fixed point or invariant subspace (§7.1).** G12 needs a different declared mechanism if attraction is the target.
5. **Incomplete observations can hide preserved differences (§8).** A smaller snapshot is not a complete state; G02/G15 must respect the observation map.
6. **Stocks and adjacent products are not generally sufficient (§9.1).** Real reconstruction already supplies the missing normalized stocks and root-sign requirements; acquisition is G15, not a new identifiability theorem.
7. **Covariance does not give arbitrary coverage (§9.4).** G04 needs a valid distributional or distribution-free decision contract.
8. **Good marginals do not certify a good bank (§10).** G17/G21 must stay joint.
9. **Exact permanent first-entry storage is excluded for a finite static closed Hermitian model (§10.3).** G20 must use finite horizons, switching or an admitted open system.
10. **Stationary covariant complete supply cannot produce the target coherent packet arbitrarily well (§11.2).** G16 must admit and count nonstationary resources or change the target/contract.

## Logical closure pathways

### Carrier and formation pathway

Start with G01. Derive G05/G06 and the interface G08. Specify legal configuration changes G09 and their transfer G10. Then derive compatibility response G11 and perturbation/stability G12. Only afterward make formation/survival/growth preference claims G13.

G03 is a useful early exact calculation on a prepared carrier. It supports understanding of shape function but does not bypass the formation pathway. G07 is a separate context branch, required only when that coupling is used.

### Information and apparatus pathway

Start with G01/G02 and the representation contract G14. Develop acquisition G15 together with admitted reference preparation G16. Certify the bank G17, construct local execution G18 and the trigger G19, and choose the retention mechanism G20. Prove uniform joint comparisons G21 while constructing each operation. Close routing and finite exhaustion G22, then compare complete resources G23 and derive apparatus-specific entropy G24.

This branch can be analysed conditionally with supplied carriers before native formation is solved. That conditional closure must not be described as native common-substrate closure. It is therefore not necessary to wait for G13 before doing useful record mathematics.

### Geometry and physical pathway

Develop controlled coarse-graining G27 and effective geometry G28, with dimensions/clock normalization G29. These support physical area G25. Combine it with a complete record/entropy account G24 and cost G23 to test a scaling law G26. Physical interpretation G31 and, where asserted, dimensional selection G30 need their own criteria. Gravity G32 additionally needs a specified horizon and thermodynamic bridge; it does not follow from G26 alone.

There is no universal necessity to solve every native formation question before proving a conditional continuum theorem. The order here is for the manuscript's intended unified explanatory route.

## Recommended first work package

1. **E01: reconcile later sources.** Avoid solving again a gap already closed in a later paper or capture.
2. **G01: freeze one comparison contract.** Use the two-cell readout and one prepared core-star/chain comparison as concrete cases.
3. **G02/G04: close the noisy observation account.** Specify a channel and derive error/information with correct dependence and uncertainty.
4. **G03: compute the five-cell exact operator and visible sectors.** An exact finite output is available without fitting physical constants.
5. **G08/G10: formulate one interface and state-transfer contract.** Identify the preservation conditions that can actually coexist.
6. **G05/G06/G09: derive the native source and move-selection rule.** This is the highest-leverage mechanistic frontier, although harder than the first finite calculations.

The easiest outputs and the most important mechanistic outputs differ. G02/G03/G04 are tractable finite work; G05/G06/G09/G10 supply the connections required for a stronger theory narrative. G32 should not be used as the next target while these underlying mechanisms remain unspecified.

## Manuscript repairs suggested by the audit

- Replace the five-item sequence in §13 with the three dependency pathways above; its current ordering places preparation after trigger without making that dependency clear.
- Give each unresolved mechanism a stable G-ID and a concrete closure criterion. This prevents repeated “additional work” language from appearing as many independent gaps.
- Distinguish mathematical freedom from an unresolved source law. Unit weights or supplied clocks may be accepted primitives for conditional theorems.
- State explicitly that physical identity requires evidence beyond mathematical closure; the theory-only work packages cannot authorize physical promotion.
- Integrate contact and radial material selectively, guided by the argument rather than by a requirement to include every equation.

No manuscript text was modified during this audit. No G-item is marked solved by compiling it. This inventory represents the obligations expressed or implied by this manuscript, not a claim that UD as a whole lacks 33 solutions.
