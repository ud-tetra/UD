# Frozen acquisition review packet

Start with `UD_FROZEN_ACQUISITION_CONTRACT_v0.1.md`. Status: constructor-frozen proposal, independent review pending, physical promotion0. No experiment executed.

The primary exact contract is `FROZEN_CONTRACT.json`; its hash and construction checks are in `FREEZE_CERTIFICATE.json`. The run template is intentionally unfilled. The two CSV files fix preparation and channel order. The copied source certificates and diagnostic replay archive are evidence dependencies, not new claims of independent verification.

```sh
python freeze_protocol.py
python -m unittest -v test_protocol.py
python validate_protocol.py
python audit_run.py RUN_RECEIPT_TEMPLATE.json --data-dir PATH_TO_RUN
```

The final command returns NOT_EXECUTED for the unfilled template. It checks record structure and declared budgets; it cannot authenticate review, metrology or numerical proofs from their reference hashes. Read `INDEPENDENT_REVIEW_FORM.md` for the remaining review questions.

The history record's fixed-point encoding and the separate higher-precision diagnostic encoding are implemented in `exact_encoding.py`. A validated full-size spectral solver is not included. Do not allocate a dense Hankel matrix merely to audit raw records.
