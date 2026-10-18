# Restricted local fault certificate

Read `UD_RESTRICTED_FAULT_HISTORY_CERTIFICATE_v0.1.md` for the declared family,
fit-independent visibility proof, finite error budget and history transfer.

```bash
python certify_restricted.py
python -m unittest -v test_restricted.py
python validate_restricted.py
```

`restricted_gate.assess_epoch(Y)` accepts one epoch of blank-corrected exact
rational readings with shape6x260x189. Require passage in both epochs and the
external total-error/family receipts. The raw experiment also includes one blank
per epoch; its error must already be included in the corrected-data receipt.

The source pair/stencil restrictions, parameter constancy and metrology bounds
are hypotheses. Passage does not prove family membership. No apparatus data or
independent review are supplied. Physical promotion remains zero.
