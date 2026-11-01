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
