# THM-534 v2.26 — Certified preparation and signed capture receipts

This capture supplies a concrete full-field preparation certificate for the v2.25 five-amplitude guard. The initial field is -e_face014 + (e_vertex3-e_vertex4)/1000, with any 23-dimensional perturbation of norm at most 1/1000000.

The unique first event lies in [1979/2500,39581/50000]. Both switch normal speeds stay nonzero; the determinant lies in (-1/950,-1/1250). Captured core stock exceeds 1/4. The full-output inverse has a conservative time-error bound of 3000 times the readout error on the stated branch.

Read THM534_PREPARATION_INTERVAL_AND_SIGNED_CAPTURE_CERTIFICATE_v2.26.md for proofs, assumptions and rational receipt tables. PREPARATION_CONTRACT.json fixes the preparation, error classes, generator masks and common observation parameter. CLAIM_DEPENDENCY_LEDGER.json preserves open source dependencies.

Reproduce with Python standard library:

    python verify_preparation.py
    python verify_controls.py

The verifier writes RESULTS.json and SIGNED_CELL_RECEIPTS.json. It uses rational outward intervals, analytic Taylor remainders, 20 branch subintervals, six distinct spectral/Taylor full-flow controls and 256 exact continuity polynomial checks. Three altered inputs/models must be rejected; clean replay must match results and stdout byte for byte.

Signed receipts are integrated net currents certified by the exact continuity identity and endpoint enclosures. They are not independent quadrature measurements. Stocks have zero jump at switching. Holding the core and face record does not freeze the cell-owned stock or whole field.

The protocol supplies its nonzero clock and sticky mode with ideal first-crossing execution. Native preparation, event detection, persistence, reset/renewal and physical correspondence remain open. Gate-mask mistakes and noisy/delayed event execution are outside this certificate. This is not an empirical preregistration or parameter-free preparation law.

Development only; independent review pending. Physical promotion: 0.
