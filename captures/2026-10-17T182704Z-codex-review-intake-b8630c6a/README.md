# Review intake — HOLD

Both submissions have been preserved. **Independent review is not established; physical promotion remains0.** The previous constructor-verified numerical results are unchanged.

| Frozen target | Listed existing files | SHA256 matches | SHA256 mismatches |
|---|---:|---:|---:|
| Noisy-record campaign v0.1 | 12 | 0 | 12 |
| Record-only certificate v0.2 | 12 | 0 | 12 |

All digest strings are syntactically valid. They fail to bind the claimed review to the named delivered bytes. The two later review files per submission are absent from the original targets, as expected; their original bytes were not supplied for authentication.

The main scope corrections are:

- Lossless coding reconstructs the finite observation array, not the unobservable bulk state or a unique generator.
- The single-vector test meets the global vector ceiling at equality and exceeds the sufficient coordinate ceiling. Full acquisition-contract membership was not verified.
- The same record has algebraic rank at least2203 while retaining1893 values above the frozen threshold. Numeric threshold count and exact rank are different objects.
- Separate generator/verifier roles do not identify an independent reviewer. Arithmetic statements are independent of runtime duration; acquisition timing and review chronology still matter.

See [the audit report](AUDIT_REPORT.md), [per-file hash audit](HASH_AUDIT.json), [claim audit](CLAIM_AUDIT.json), [formal disposition](REVIEW_DISPOSITION.json) and [resubmission template](RESUBMISSION_TEMPLATE.json). Correct constructor reference inventories are in `reference/`; they are not replacement reviewer attestations.

To repeat the byte checks, provide the original two ZIP archives:

```bash
python audit_reviews.py --noise-archive PATH_TO_NOISE_ZIP --record-archive PATH_TO_RECORD_ZIP --output NEW_AUDIT_DIRECTORY
```

The archive digests are pinned; a different reviewed revision must be identified explicitly. `python check_counterexample.py` reproduces the rational rank bound from the byte-bound evidence copies.

For reconsideration, provide an attributable reviewer identifier and independence statement, exact reviewed archive/revision, matching manifest and corrected scope. Label the review static, replayed or partial; supply execution evidence for reproduction claims. No reviewer identity or verdict has been invented here.
