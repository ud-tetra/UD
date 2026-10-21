# Synthetic storage CLI review

The unchanged actual `c33_pack.py` and `c33_unpack.py` CLIs passed a source-excluded synthetic fixture test. The application inputs were the previously sealed diagonal 1999-row synthetic frame, not actual UD rows. Both source hashes matched `c33_TOOLING_FREEZE.json` before and after testing.

Packing produced exactly 32 parts: 31 containing 64 rows and one containing 15. An independent parser compared every packed row's compressed bytes with the existing fixture. Actual unpacking then restored all 1,999 compressed row files and `FULL_FRAME.json` byte-for-byte.

All ten rejection controls exited nonzero without a completed `FULL_FRAME.json`: wrong pack metadata hash; wrong unpack index or metadata hash; corrupt part; authenticated wrong magic; authenticated trailing bytes; forged part path; forged start row; missing last part; and authenticated forged row output path. Every command, stdout, stderr and result is preserved. Partial output is permitted on rejected runs; a completed frame receipt was never emitted.

“Authenticated” variants deliberately supplied a matching digest for modified test input to exercise the parser's internal constraints. This does not establish the modified input's provenance. The codec proves integrity relative to trusted index/metadata bytes; trusted expected hashes, source commit and root remain external premises. This review grants no UD source admission, physical accuracy claim or external promotion authority.

To avoid another 1,999-file fixture copy, restored test row files were hashed and then removed from these test output directories only. The sealed original fixture remained untouched. The 32 verbatim packed parts, successful metadata, `RESTORED_ROW_HASHES.json`, partial-output hash inventories and all CLI logs remain available. The test source and plan were frozen before any codec execution.

`FREEZE.json` binds the source, plan and fixture. `REVIEW_RECEIPT.json` contains the detailed checks and cleanup counts; `REVIEW_MANIFEST.json` binds execution artifacts. `FINAL_MANIFEST.json` additionally binds this report and the execution inventory. Physical promotion is zero and external promotion review remains pending.
