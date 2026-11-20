# O09 phase-current source gate / K4 cubic selector v0.1

**STATUS:** scoped exact mathematical theorem and explicit candidate extension. **Physical promotion: 0.** No laboratory values or measured residuals used.

This package distinguishes three conclusions:

1. **EXACT / NO-GO:** The O09 modal action-history map does not specify a Hamiltonian or local modal-to-edge intertwiner, so it cannot determine a unique local conserved phase source by itself.
2. **EXACT:** For one dimensionless vertex scalar `b in C0(Delta3;R)` and full `S4` equivariance, the polynomial source into the three-dimensional oriented edge-cycle sector has no homogeneous components of degree 0, 1 or 2. The unique cubic generator is `J=B2 t`, `t_ijk=(bi-bj)(bj-bk)(bk-bi)`. It is gauge-compatible and satisfies `B1 J=0` and `B3^T t=0`.
3. **CANDIDATE:** A separately written compact coupling `-g sum t_f sin(Phi_f)` has an exact nonflat locally stable stationary solution and a conserved source current. It is not selected by O09; donor/work law and physical correspondence remain open.

Files:

- `TECHNICAL_NOTE.md` – full type-controlled proof, sources, limits and next gate.
- `UD_O09_CUBIC_CURRENT_GATE_v0.1.pdf` – 3-page A4 typeset mathematical report.
- `UD_O09_CUBIC_CURRENT_GATE_v0.1.tex` – editable LaTeX source.
- `verify_cubic_source.py` – generated K4 incidences, full 24-permutation covariance, exact characters and cubic current.
- `independent_character_check.py` – independently constructs monomial permutation traces through degree 3.
- `independent_action_check.py` – independently checks O09 variation, periodic interaction, nonflat equilibrium and explicit conservation/sink receipts.
- `CLAIM_DEPENDENCY_LEDGER.csv` – exact, conditional, source-blocked and physical-status rows.
- `SOURCE_LINEAGE.json` – versioned source IDs and URL provenance.
- `verification.json` – executed checks, receipts and source/target limitations.
- `MANIFEST.json` and `verify_manifest.py` – SHA-256 manifest and integrity check.

Reproduce:

```bash
python verify_cubic_source.py
python independent_character_check.py
python independent_action_check.py
python verify_manifest.py
```

Python 3 and SymPy are required. Tests use small exact matrices and no network or physical datasets. The source action is O09; the optional periodic coupling is a **new candidate** and must not be represented as current adopted UD physics. Independent non-constructor scientific review is pending.
