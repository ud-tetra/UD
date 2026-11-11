# Recovered docs: source ingestion, gap impact and new information

RESULT — Substantial source recovery, selective mathematical validation, no physical promotion. Pinned GitHub main: `82362e78ce0ca13185ba5c5ad5793c00fbf46ece`. This is an append-only development audit, not a replacement of source texts or a new registration receipt.

## 1. What was ingested

All 170 files under `docs/` at the pinned commit: 82 Markdown, 21 JSON, 20 PDF, 10 HTML, 9 TeX, 4 ZIP, 12 Python, 7 SVG, 2 JSX, one CSV, one XLSX and one TXT; 10,812,767 original bytes. Every top-level file has a SHA-256 inventory. The four ZIPs contain 139 recursively indexed member occurrences, 69 distinct payload hashes, down to depth eight. All 119 declared SHA256SUMS entries checked successfully, including repeated nested packages. Repetition is not independent evidence.

PDF text was extracted with Poppler; source/HTML/JSX/Python were read as data. No imported code, archived instruction block, HTML script, builder, simulation or remote asset was executed. The nine workbook sheet names were inventoried; its cells and formulas were not scientifically audited. Image-only PDF/diagram content was not comprehensively inspected or OCR'd. This is complete file-level ingestion with targeted claim review, not a claim that all 170 documents' proofs have been certified.

The files remain in their original repository locations. SOURCE_INVENTORY.json and RECURSIVE_ARCHIVE_MEMBERS.json pin their identities; SEARCH_HITS.json records scoped source excerpts. Both duplicate gauge-mode PDFs are byte-identical; both native-trigger Markdown versions are byte-identical. Filename suffixes do not establish independent versions or replication.

## 2. Gap-by-gap disposition

| Prior gap | New source evidence | What is filled | What remains open |
|---|---|---|---|
| THM-534 microscopic transport derivation | THM-561; LS1–8,10–11; APS manuscript transport subsection | More downstream uses and an explicit matrix definition with self/opposite/cross entries 1/2,1/6,1/12 | No original THM-534 document, event count/measure, renewal law or physical clock recovered. The APS text names IFS weights but does not derive them there. Rate-source gate stays open. |
| Quark/lepton coupling construction | THM-563a,565a,565b,566,567,568; THM-562 full note/PDF | Concrete joint involutions, candidate Higgs operators, orthogonal face extension, 2x2 coupling map and simplex-representation argument | Physical chirality, gauge/species identification, VEV, fermion masses, anomaly cancellation and full three-generation Yukawa remain separate. Two source overclaims require scoped corrections below. |
| Lepton phase/action mechanism | Lepton Sector Derivation Block; April28 consolidation; April24 handoff | Explicit proposed phase 2/9, held phase-injection obligation, correction kernel 1/61, eight audited unsuccessful routes and target-selection history | No forward phase-injection action, native mass readout or unexposed prediction. Historical 'effectively closed' is not our current completion status. |
| Localization code and measured/simulated outputs | shell1*.py, hmulti*.py, R6b/Hmulti/B_rho JSON, Oscar diagnostic | Actual archived implementations and reported numerical output now available; source-availability gap substantially filled | Outputs mix prescribed profiles, different operators, ansatze and eigensolves. No fresh replay or independent validation; per-probe diagnostic output not located. Numerical localization is not experimental matter evidence. |
| Recalled pentagonal carrier | 600-cell Hopf and reduced-dynamics notes | Precise pentachoron controls and a declared C10 quaternion/fibration sector construction, with fivefold stabilizer context | No explicit C5/pentagonal-carrier proof found in the extracted text. These are distinct from J1/Kminus. Fivefold symmetry or a pentachoron name does not identify the recalled carrier. |
| Open-system stock, local recovery and renewal | Local Recovery/Occupancy; Positive Stock/Balanced Recovery; nested thermal-memory ZIPs | Conditional positive-register completions, protected-port constraints, explicit write/read/bath protocols and hash-bound supporting packages | Signed state is not automatically positive occupancy. Source amplitudes, gate/clock/stock rules, bath preparation and native renewal remain added premises. These packages explicitly leave G05/G06 open. |
| Dimensional action/unit map | Four-Coordinate Physical Realization; Gibbs renewal and record-energy packages | Declared SI apparatus maps, component-dependent energy/time calibration and resource accounts | Apparatus calibration is supplied; hbar is used in pulse laws, not derived. No universal A0/hbar normalization or parameter-free fundamental action quantum recovered. |
| Gauge action and finite stability | Gauge Transport, Joint Hamiltonian, Gauge Reduced Modes, Nonlinear Instability, Resonance Closure, Curved Branch, Higher Rank and Residual Gauss PDFs | A substantive conditional research lane with explicit added link fields/action, Gauss law, backreaction and stability restrictions | Not a source derivation of the same model from native scalar incidence; no SM identification, physical coefficients or empirical bridge. Existing constructor receipts are not revalidated by ingestion. |
| T2.6 / generations | Historical review-readiness notes claim three; April24/28 notes use A4/V4; prior HTML T3.0 says observation-anchored | Alternative historical arguments and status conflicts are now visible | No explicit T2.6 entry found by the bounded scan. A quotient of order three does not itself force exactly three physical generations. Reconciliation remains open. |
| Registration / independent review | Preregistration packet, protocol amendments, errata and external-review brief; parity executor JSON | Concrete historical discriminator design, corrections and declared dependencies | These concern other contracts. No automatic transfer of CRL or blinded-run status to this particle bridge. Constructor/executor labels alone do not establish independent review or custody. |
| Cosmological support selection | Path-alpha and RG-depth reports/results | Named competing S0=43/7 and S_Lambda=44/7 choices and explicit held falsifier/selection obligations | Candidate support choice is not a uniquely derived action. No cosmological promotion follows from selecting the closer historical residual. |

## 3. New exact checks and necessary corrections

These checks were constructed here using exact rational arithmetic. They are narrowly scoped and do not validate the remaining historical theorem collection. Originals remain unchanged.

### 3.1 Coupling invariants survive; universal nonzero entries do not

Use the declared Pplus basis with u=(1,1,1)/sqrt3, L1=e1, L2=e3, R=e2 and the allowed V_half orthonormal basis w1=(1,-1,0)/sqrt2, w2=(1,1,-2)/sqrt6. With Hj=u wj^T+wj u^T, the coupling matrix is

\[
Y=\begin{pmatrix}0&2/\sqrt{18}\\-1/\sqrt6&-1/\sqrt{18}\end{pmatrix},\qquad
YY^T=\begin{pmatrix}2/9&-1/9\\-1/9&2/9\end{pmatrix}.
\]

EXACT: squared singular values are 1/3 and 1/9, so their ratio is sqrt3. Real orthogonal Higgs-basis rotations preserve these singular values. The corresponding column-angle extremum has |cos(angle)|=1/2, giving the conditional 60–120 degree bound. The absolute determinant is 1/(3 sqrt3); its sign changes when the ONB orientation is reversed, so an arbitrary-ONB signed determinant claim must be qualified.

CORRECTION: <L1|H1|R>=0 in this explicitly admitted ONB. THM-565a's claim that every such matrix element is nonzero is false as quantified; the numerical table only illustrates one basis. Nonzero coupling exists, and the invariant full-rank matrix result survives. No mass interpretation follows.

The joint S/star eigenspaces have the stated (2,1,1,2) dimensions under those definitions, but that does not imply invariance under T. On Pplus, T=(1/2)I+(1/6)J and star=diag(1,-1,1); [T,star]12=-1/3. Thus dynamical chirality preservation needs a separate condition.

### 3.2 Fidelity requires a metric contract

CORRECTION: THM-LS1(iii) asserts invariance under every invertible U while retaining the standard inner product. In an orthonormal two-eigenvector subspace take T=diag(1,1/2), psi=(1,1), U=diag(2,1). U commutes with T, but the fidelity changes from 9/10 to 81/85. This exactly falsifies the unrestricted assertion.

Repair: retain unitary basis changes with the fixed metric, or transport the metric under general changes as G'=(U^-1)^dagger G U^-1. The spectral formulas, positive-kernel convergence and unitarily invariant versions need not be discarded. This matters directly for our action/observable map: metric choices cannot be silently removed by a change of coordinates.

## 4. Exposure and historical conflicts recovered

The April28 consolidation records that the bare tau/muon ratio overshot the observed target, then a systematic test involving Delta=7 produced the 1/61 correction. Its numerical agreement is historical target-informed selection, not a blind forecast. The same packet explicitly holds theta=2/9 and lists eight unsuccessful phase derivations; these rejected routes should be retained as constraints on future work.

The April22 handoff corrects d_s=4/3 from a random-walk spectral dimension to a UD spectral parameter and calls the former labeling an overclaim. The April28 consolidation and lepton block nevertheless reuse the random-walk/spectral-anomaly interpretation. Therefore H=16+(3-4/3)/2=101/6 is an arithmetic identity at supplied inputs; this archive does not justify treating its two physical readings as independent derivations.

Generation labels also conflict across sources: dihedral stability, A4/V4 and observation-anchored T3.0 cannot be flattened into a single proof. Current physical promotion remains 0; historical maturity language is source data.

Errata recover another practical constraint: the proposed third-slip discriminator needs returned leakage Lambda2 to distinguish nonstationary leakage from autocatalysis, and depends on validated n=2 and n=3 carriers. The erratum says the n=3 endpoint was not constructed in that source. A discriminator design is not an available experiment merely because its scoring algebra is written.

No fresh particle targets were fetched or scored. The recovered manuscripts, fits, comparisons and held parameters extend the exposure record. They cannot restore naive global blindness.

## 5. What the simulation recovery actually changes

The prior two-HTML audit correctly found no code/data in those two inputs. The expanded docs set now supplies both. This is an additional-source update, not a contradiction of that bounded search.

The initial B_rho output describes hierarchical exponential profiles and an imposed long sigma2 length, while later outputs name sparse eigsh on explicit Hamiltonians. Multi-component outputs introduce supplied coupling constants and selection criteria. The R6b outputs report sigma2 F values about 5.69,7.42,18.88 across levels 5–7; the Oscar note asks whether probe targeting causes the anomaly. Its per_probe_sigma2 JSON schema occurs in the request, not in a recovered output JSON. These distinctions preclude counting all records as corroborating the same frozen model.

A useful next execution is a static code/output/operator provenance audit, then a small eigenproblem replay with declared tolerances, eigensolver residuals and subspace observables that are stable within degeneracies. Imported code has not been run during this ingestion.

## 6. Recommended order

1. Priority 100: rebase the particle algebra on explicit unsigned-versus-signed operators and the two exact corrections above. Freeze matrix/metric definitions before using coupling invariants as a bridge candidate.
2. Priority 98: build the shell code-to-output provenance map and perform a bounded probe-bias diagnostic. Source recovery makes this executable in principle; it does not authorize historical results as independent validation.
3. Priority 96: recover THM-534's original microscopic derivation or explicitly start a new forward source programme. Additional citations to its matrix do not substitute for its counting law.
4. Priority 94: use the lepton failed-route/exposure ledger to constrain a new phase-injection programme. Keep 2/9,1/61 and generation count outside any target-blind proof premise.

Gap2_FINAL_Finite_Genesis.png was unavailable in the supplied attachments and was not used. Please retry that upload if it is intended as evidence; no missing-image inference is included here.

Generated: inventories, gap map and source/correction report. Checked: hashes and selected exact algebra; constructor only. Captured: unique append-only event and manifest. Publication status is reported separately; no automatic merge, registry upgrade or physical identification is asserted by this document.
