# UD mathematical proof milestones

**UD is a proof-first theoretical research program.** The theorem, lemma, no-go or counterexample is the scientific milestone; GitHub is its archive.

Read [proof-first governance](../docs/UD_PROOF_FIRST_RESEARCH_GOVERNANCE_v1.0.md), the [proof template](templates/PROOF_MILESTONE_TEMPLATE_v1.0.md) and the [append-only ledger](ledger/README.md).

## Initial source-bound scoped proof records
- [UD-PM-PRED01-001: WBX1 four-event identity and singular parameter branch](milestones/UD-PM-PRED01-001_v1.0.md) — VERIFIED_SCOPED, EXACT_CONDITIONAL, review deferred, physical promotion 0.
- [UD-PM-PRED02-001: iid 27-class replay-collision expectation bound](milestones/UD-PM-PRED02-001_v1.0.md) — VERIFIED_SCOPED, EXACT_CONDITIONAL, review deferred, physical promotion 0.

Only these two statements were independently rechecked for this seed register. All historical THM-* documents retain their source statuses until individually audited. A passing test or a merged PR does not create an additional mathematical theorem. Future proofs receive stable IDs, complete statements, immutable JSON entries, SHA-256 capture and unique event.


## PRED-04 independent proof audit (2026-10-31, review deferred)

- [UD-PM-PRED04-TOPO-001 — K4 star-column excision yields integral winding only under explicit excision](milestones/UD-PM-PRED04-TOPO-001_v1.0.md). **EXACT_CONDITIONAL**, physical promotion 0.
- [UD-PM-PRED04-WORK-002 — sharper distributed positive-work upper bound 9/5](milestones/UD-PM-PRED04-WORK-002_v1.0.md). **EXACT_CONDITIONAL**; prior 41/5 bound remains valid but loose.
- [UD-PM-PRED04-CAUSAL-003 — immediate-excision live-edge propagation NO-GO](milestones/UD-PM-PRED04-CAUSAL-003_v1.0.md). **EXACT_CONDITIONAL / NO_GO** on the stated online update ordering.

All records are scoped to source PR #479 (unmerged), proof-governance PR #473 (unmerged), and explicit assumptions. The independent verification results, counterexamples and hashes are preserved in the versioned capture; non-constructor review deferred, physical promotion 0.

## PRED05 transfer-before-excision and stiffness proofs — 2026-10-31

- [UD-PM-PRED05-EVOL-001 — transfer-before-excision state evolution and restricted winding persistence](milestones/UD-PM-PRED05-EVOL-001_v1.0.md): EXACT_CONDITIONAL; native seed and direction port assumed.
- [UD-PM-PRED05-SCALE-002 — harmonic-norm logarithmic theorem and running-stiffness obstruction](milestones/UD-PM-PRED05-SCALE-002_v1.0.md): EXACT_CONDITIONAL; unweighted edge metric.
- [UD-PM-PRED05-IDENT-003 — absolute stiffness nonidentifiable from static geometry](milestones/UD-PM-PRED05-IDENT-003_v1.0.md): EXACT_CONDITIONAL / NO_GO.
- [UD-PM-PRED05-PERSIST-004 — retained memory does not alone protect winding](milestones/UD-PM-PRED05-PERSIST-004_v1.0.md): EXACT_CONDITIONAL / NO_GO.

These are assumption-scoped proof milestones from the new stacked proof-audit branch. Numerical GF2 cases and software tests corroborate, but do not replace the proofs. Non-constructor review is deferred; physical promotion 0. The 41/5 and 9/5 prior work bounds remain valid within their declared hypotheses; the new theorem adds a necessary stiffness running condition without deriving a native amplitude.


## PRED06 source selector and action normalization audit (scoped, review deferred)

- [UD-PM-PRED06-SEL-001 — symmetric K4 deterministic selection no-go](milestones/UD-PM-PRED06-SEL-001_v1.0.md).
- [UD-PM-PRED06-SEL-002 — conditional local burden/flux selection lemma](milestones/UD-PM-PRED06-SEL-002_v1.0.md).
- [UD-PM-PRED06-PAR-003 — finite parity-to-integer lift no-go](milestones/UD-PM-PRED06-PAR-003_v1.0.md).
- [UD-PM-PRED06-FIX-004 — fixed incidence cannot change homology](milestones/UD-PM-PRED06-FIX-004_v1.0.md).
- [UD-PM-PRED06-ACT-005 — flat harmonic sectors are invisible to derivative-only action](milestones/UD-PM-PRED06-ACT-005_v1.0.md).
- [UD-PM-PRED06-MET-006 — uniformly elliptic metric logarithmic stiffness obstruction](milestones/UD-PM-PRED06-MET-006_v1.0.md).

Each theorem is EXACT_CONDITIONAL under its explicit premises. Numerical/exact finite checks corroborate but do not replace the proof. Source dependencies include open PR #487 and the v0.39 typed coefficient ledger. The native source and metric-to-action bridge remain OPEN_GATED. Non-constructor review DEFERRED; physical promotion 0.

## PRED07 — K4 burden instability and sector-action audit (2026-11-01)

- [UD-PM-PRED07-BUR-001 — Conservative K4 nonlinear burden amplifier, threshold gamma*M>4](milestones/UD-PM-PRED07-BUR-001_v1.0.md): EXACT_CONDITIONAL. Gain gamma, asymmetric input and excision trigger remain OPEN_GATED.
- [UD-PM-PRED07-MET-002 — S4 + unit-edge norms do not fix a general cochain action metric](milestones/UD-PM-PRED07-MET-002_v1.0.md): EXACT / NO-GO under unrestricted symmetric SPD metrics.
- [UD-PM-PRED07-ACT-003 — Gauge-invariant real-period action exists, but tau and unwrapped lift unsourced](milestones/UD-PM-PRED07-ACT-003_v1.0.md): EXACT_CONDITIONAL. Not invariant under large compact U(1) gauge identification of integer lifts.

Proof dependencies: PRED06 PR #490 and PRED05 PR #487; program governance PR #473. Source typed coefficient ledger v0.39 Q153/Q162/Q169/G05. Full proofs and checks are in the unique hash-verified capture `captures/2026-11-01T164437Z-gpt6-pred07-proof-f3a1/`. Review DEFERRED; physical promotion 0. Code and CI verify scoped calculations but do not establish source-native physics.
