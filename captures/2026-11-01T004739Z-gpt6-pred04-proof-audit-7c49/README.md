# UD PRED-04 independent proof audit v1.0

**Research date:** 2026-10-31 (America/Chicago). **Evidence:** EXACT_CONDITIONAL / scoped NO-GO. **Review:** non-constructor external review deferred. **Physical promotion:** 0.

This proof-led research package independently audits *both* authorized lines:

1. **UD-PM-PRED04-TOPO-001** — K4 star-column excision from a tetrahedral 3-ball produces `H_1 ≅ Z` only under the stated **topology-changing** removal rule. Legal Pachner moves preserve homology and cannot create the hole themselves. A seed/direction native selector remains missing.
2. **UD-PM-PRED04-WORK-002** — Independent exact proof tightens the distributed positive-work inequality from `41/5` to **`9/5`** under the **same** one-pass, temporarily nonclosed, `n=2`, `μ=λ`, unit-gap normalization and `d_F ≤ 6` hypotheses. This is a model-action bound, not a physical energy measurement.
3. **UD-PM-PRED04-CAUSAL-003** — Under immediate vertex-star excision, pure surviving-K4-edge token transport cannot move to the next vertex. The antecedent code instead calculates the complete token trail *before* removal. Autonomous local propagation requires a transfer-before-pruning order or a separately typed source/control network.

## Source precedence

Canonical antecedent: [`ud-tetra/UD` PR #479](https://github.com/ud-tetra/UD/pull/479), **unmerged** when audited, head `b5c8146ae4b956279e6f399553e02cffbc42c7ea`. Source `docs/UD_PRED01_LOCAL_DEFECT_SELECTION_AND_BOUNDED_SOURCE_v0.4.md`, Git blob `abefbc821bd7897e9c469b2ff12bd7cccab56c99`, §§2–5. The older v0.3 fixed-three-edge no-go is preserved under its original hypotheses. Proof-first tracking proposal is UD PR #473, not assumed merged.

## Reproduction

Run using Python 3.10+ standard library; no SciPy needed to establish the new claims:

```bash
python3 independent_topology_work_audit.py --out INDEPENDENT_AUDIT_replay.json
python3 -m unittest discover -s . -p 'test_independent_proof_audit.py' -v
```

The first script derives every 3D simplex from six monotone paths in a unit cube and independently performs exact mod-2 boundary/rank checks, exact face-action fraction sweeps, seven Freudenthal edge types, a partial-excision counterexample and a legal 2↔3 move witness. The proofs in the three milestone Markdown files provide **unbounded-resolution mathematical arguments**. The finite tests are supporting corroboration, not a proof by examples.

`SOURCE_REPLAY_RESULTS.json` was generated separately by re-running the antecedent PR #479 code and is byte-identical to its original result (SHA-256 `9ea3bb3ae0ad2fffe876b65bb07640657ff6c296e4fcc57f3ba598368cbdbd4d`). This source replay is dependent on the previous implementation, while the new exact-code audit has no imports from it.

## Claims and exclusions

- The topological **integral** result follows from an annulus-by-interval homotopy argument, not merely mod-2 rank checks.
- The `9/5` work bound uses a sharp per-triangle **2/3** quadratic variation inequality. It is not necessarily sharp globally.
- Staging is one update per edge, at arbitrary order; loops, repeated toggles, fixed sparse cut, or time-dependent work are different protocols.
- The unit retained gap is imposed by `λ_N||h_N||²=2/5` and does not determine a native physical action scale. Without this calibration, the theorem still gives a uniform bound on the dimensionless *ratio* `W_N^+/Δ_N` when `μ_N/λ_N=1`.
- No native K4 burden/parity seed, directed transport, physical clock, SI energy, apparatus, independently measured leakage, persistent defect dynamics or observed physical correspondence was constructed.
- Non-constructor review remains **DEFERRED** and physical promotion remains **0**.

## Artifact integrity

`MANIFEST.json` lists file paths, byte sizes and SHA-256 values for every source-bound file in this package (excluding `MANIFEST.json` itself to avoid a self-hash cycle). `PROOF_LEDGER_*.json` are append-only candidate entries with separate mathematical, review and physical statuses. GitHub publication is recorded separately: a branch or PR is not a merged or independently reviewed theorem.
