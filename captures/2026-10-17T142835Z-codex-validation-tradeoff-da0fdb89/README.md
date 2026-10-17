# Validation precision–work frontier

Read `UD_VALIDATION_PRECISION_WORK_FRONTIER_v0.1.md`. The recommended profile
reduces readings by1/6 and permits64x more total response error while retaining
the history targets. A strict profile reduces readings by1/3 at the previous
precision and retains all previous intermediate limits.

```bash
python certify_tradeoff.py
python check_controls.py
python -m unittest -v test_optimized.py
python validate_tradeoff.py
```

`optimized_gate.assess_epoch(Y, profile="recommended")` accepts one epoch of
blank-corrected exact rational data with shape5x260x189. The `strict` profile
uses4x260x189. Require passage in both epochs, all static row/global/unused
gates and every matched pair filter. Blank measurement and all preparation,
timing, noise, family and stability receipts remain external.

The source code/stencil fault family is unchanged. A pass does not establish
family membership. The precision floor applies only to the specified error
envelope, not physical instruments. Physical promotion0; no apparatus data or
independent review are supplied.
