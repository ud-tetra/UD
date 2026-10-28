# Finite controlled writer operator certificates

Read THM534_FINITE_CONTROLLED_WRITER_OPERATOR_CERTIFICATE_v2.24.md for the operator proof, scope and receipts. WRITER_CONTRACT.json states what is supplied and what remains open.

On a working copy, run:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_writer.py
    PYTHONDONTWRITEBYTECODE=1 python3 verify_certificate_controls.py

The first uses only standard-library integer and Fraction arithmetic to regenerate RESULTS.json and SIGNED_RECEIPT_SUMMARY.json. Decimal display fields are not proof authority. Numerical search is not needed for verification.

WRITER_SCHEDULES.json contains two fixed programmes, u=1/2 and u=-1/2, each with 160 positive rational steps. The first rotates the protected plane; the second approximates its inverse. The full operator bound covers all 14 active directions, including the complement meant to remain unchanged. The uncontrolled gradient sector is not fixed. Norm is preserved exactly on the full carrier.

The integer elimination only proposes rational matrices. Exact midpoint residuals and the exact rational basis Gram inverse certify the bound. No proposal accuracy is assumed. Changed parameters, a mask bit and target sign are rejected by separate integrity controls.

Intermediate isolation is not maintained: the unit core witness loses more than 99/100 of its stock from the record plane during each programme. Full native lower contacts and shared-face constraints remain intact. The signed receipt summary encloses the actual unit-input path; proposal defects are not sources. The ideal unit-core endpoint ownership split is 2/25 to cell0 and 23/25 to cell1.

After writing, any of eight isolating masks preserves the actual plane coordinates. A consecutive known write/unwrite pair approximately restores the active field. Holding between the programmes protects the plane but allows the complementary field to evolve; no whole-field reset is inferred.

Construction-only search_writer.py requires NumPy/SciPy. It searches fixed benchmarks using supplied masks and parameters; its output is not itself a proof. Only the saved rational programmes are certified.

The programmes do not generate event time, select an unknown clock angle, recover information already lost by peak stopping, erase an unknown receipt, or source their own clock/mode. They use implicit full-carrier Cayley updates, without a bounded-radius implementation theorem or physical-time identification.

Development only. Independent review pending. Physical promotion: 0.
