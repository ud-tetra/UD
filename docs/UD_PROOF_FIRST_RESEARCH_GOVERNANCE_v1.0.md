# UD Proof-First Research Governance v1.0

**Scope:** Unified Dynamics across all research branches and associated repositories.
**Date:** 2026-10-31.
**Status:** User-directed operational instruction, staged for reviewed GitHub integration.
**Physical promotion:** 0. Non-constructor review deferred, not waived.

## Scientific identity and primary progress measure

Unified Dynamics (UD) is a **mathematical proof-based theoretical research program, not a software development program**. Its core milestones are proved lemmas, theorems, exact identities, rigorously scoped no-go results, counterexamples, material corrections, and resolved theorem dependencies.

Source code, simulations, workflows, CI, sites, GitHub issue counts and releases are supporting verification and archive infrastructure. Their successful execution does not, by itself, prove a theorem or identify a physical law. Do not headline software/test/release metrics as scientific closure.

Each research response should lead with (1) the mathematical statement or obstruction, (2) assumptions and proof, (3) verified scope and counterexamples, (4) unresolved theoretical or physical bridge, and (5) captured milestone receipt.

## Proof milestone admission

Create a distinct immutable milestone for each substantive closed proof, under its exact hypotheses, including:
- THEOREM or LEMMA with complete argument;
- EXACT IDENTITY changing the reasoning frontier;
- NO_GO or COUNTEREXAMPLE with a precise hypothesis set;
- finite exhaustive certificate with stated, completely covered finite domain;
- material CORRECTION or theorem narrowing with explicit supersession.

Conjectures, diagrams, fits, computer experiments, code tests, discussion and governance edits are development records, **not proved milestones**. Preserve meaningful failed attempts too, without advertising them as proof closures.

Use orthogonal evidence fields: proof_kind (THEOREM, LEMMA, IDENTITY, NO_GO, COUNTEREXAMPLE, CORRECTION, FINITE_EXHAUSTION); proof_status (CANDIDATE, PROVED_CONDITIONAL, VERIFIED_SCOPED, REVIEWED, FAILED, SUPERSEDED, OPEN_GATED); review_status (DEFERRED, CONSTRUCTOR_ONLY, NON_CONSTRUCTOR_REVIEWED); and physical_promotion (default 0). EXACT_CONDITIONAL describes correctness *under the stated model*, not truth of its primitive hypotheses or physical identification.

## Proof record requirements

Every substantive proved milestone must identify:
1. Proof ID, version, immutable source path and date.
2. Mathematical object, domain/codomain, coefficient ring or field, metric, orientation, units, normalization, and update/initial/boundary conditions where relevant.
3. Exact theorem statement, assumptions and conclusion; identify newly added premises and target-informed choices.
4. Full derivation or valid exact proof, not analogy or agreement with a target number.
5. Counterexamples, degeneracies, limits, and precise hypothesis failures.
6. Typed source/dependency IDs, versioned citations and status of unmerged source claims.
7. Verification methods and actual results; separately say if a non-constructor reviewer did not check it.
8. Physical mapping, measured observable, calibration, uncertainty, null and acceptance rule or OPEN_GATED if absent.
9. Correction/supersedes/reopening links; proof, review and physical status separately.
10. Proof capture and content hashes.

## Canonical append-only records

Proof file: proofs/milestones/PROOF-ID_vX.Y.md
Ledger entry: proofs/ledger/PROOF-ID_vX.Y.json
Template: proofs/templates/PROOF_MILESTONE_TEMPLATE_v1.0.md
Machine-readable template: proofs/templates/PROOF_MILESTONE_RECORD_v1.0.json
Evidence capture: captures/<UTC-unique-ID>/ with MANIFEST.json and SHA-256, plus events/<unique-ID>.json.

Do not overwrite a historical proof, failed result or frozen theorem. Corrections create a new version with supersedes pointer; any index is derived navigation, not claim authority. Capture milestone outputs in the same substantive research turn when tools are available; if blocked, provide local artifacts and record the gap. This is a per-turn obligation, not a background automation.

## Governance and physics boundary

Keep the separate development/registry and CRL physical correspondence gates. Exploratory mathematical assumptions, reverse engineering and FIT remain allowed, but proof inside a fitted model is only a conditional mathematical result. A chain of conditional citations cannot strengthen its premise. If a source premise fails, all dependent proof claims become OPEN_GATED until rederived.

Non-constructor physical review is currently deferred, not waived. Do not label a constructor-only check as independent review or infer physical correspondence from any exact theorem. Physical promotion remains 0 unless specifically supported by an independent physical-bridge receipt.

**Summary: The theorem is the milestone; code is an auxiliary verifier; the repository is the proof archive.**
