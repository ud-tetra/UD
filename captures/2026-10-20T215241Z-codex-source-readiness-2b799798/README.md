# Source-readiness audit after the executable numerical handoff

Development — no registry entry. Ledger v0.39 / CRL-2. External promotion review PENDING; Physical Promotion=0.

The PR296 numerical handoff is complete. This turn checked whether the published circuit sources can supply its missing acquisition premises. No qualifying native record or calibration bundle was obtained. No extra numerical wrapper, new fit, replay of the old large records or full Hankel allocation was needed.

## Primary-source return

The live-request heiDATA API still reports release1.0, published2022-02-03. All71 file metadata entries were inspected. All32gzip metadata tuples (path, size, PID and published checksum) exactly match the earlier PR253 audit. Checksums of those32raw archives were not recomputed; no raw archive was downloaded. Filename inventories cannot exclude calibration information embedded in unopened files, and the finite source/search scope does not prove no appropriate evidence exists elsewhere.

The previously unavailable utility.c was recovered via exact-commit GitHub retrieval. Its3100bytes and drive1's8200bytes each match their published deposit size and MD5; independently calculated Git blob IDs match the returned exact-commit IDs. SHA256 bindings are in SOURCE_BINDINGS.json. This binds repository source bytes to published metadata, not to an acquisition binary or instrument. Remote deposited source contents were not separately downloaded.

| Source at author commit265b6671dde799d7c73f32247fa3ee93ae70e0f2 | Static observation | Applicability |
|---|---|---|
|utility.c|A selectable-decimation helper uses a nominal20-samples-per-cycle target; its acquisition helper uses a software trigger.|No inference that this helper acquired the selected waveform.|
|u1_drive1.c|Direct setup uses /64 and external negative-edge triggering, delay7992; it calls other utility functions.|It does not call either acquisition/decimation helper above. Including a header does not select those helper settings.|

These source observations do not establish firmware, board identity, actual clock, skew, anti-alias coverage or gain calibration. The earlier conditional drive1 recipe is unchanged. The two different trigger paths must not be merged into one purported experimental configuration. No author program was compiled or executed.

The paper's AppendixA describes empirical driven-system dissipation k=0.0045 adjusted to observations. AppendixF uses measured site amplitudes in frequency-shift predictions. A future comparison must declare these conditioning inputs and partition scored outcomes; they are not untouched predictions merely because equations are published. AppendicesB/C discuss feedback tuning and background removal. None of these paper passages supplies the required source-bound joint calibration/error certificate or native UD observation map. This is a scoped reading of that paper, not rejection of its own scientific conclusions.

## Decision and concrete next work

The uninspected05-28 candidate remains under its unchanged metadata gate. Its own source/channel map, prior exposure, calibration and reviewed physical predictor/comparator/score freeze are required before confirmatory raw inspection. The new source read supplies none of those missing records. The prior128 request blockers have not been rerun or resolved; that count is inherited from PR250/253, not a new preflight result.

For native62-channel admission, obtain one actual source-bound acquisition bundle with preparation/raw/projection and coordinate-unit receipts, independently justified calibration/timebase/aliasing coverage and the native observation-map contract. For this ten-channel circuit, use its separate component contract and explicitly retrospective model-development scope unless its own fresh-confirmation gate is satisfied. Do not pad or rename it into the37×8191×62 experiment. No native1893/747, six-ratio/SI or physical-correspondence claim advances here.

Until new source evidence arrives, further replay of the same two matrices cannot close acquisition provenance. Keep the runner ready and tasks open. No new challenge, synthetic preparation, fitted comparator, signatures, timestamps or custodian receipt was manufactured. No outreach or public-site deployment occurred.

## Evidence and reproducibility

DEPOSIT_METADATA.json retains normalized public file metadata only; SOURCE_BINDINGS.json gives source-byte identities, SOURCE_ACCESS.json records successful and failed routes and limited paper paraphrases, METADATA_COMPARISON.json binds the32record comparison. RESULT.json records finite scope. Root checks SHA256/MD5/Gitblob/size on the fetched source bytes and textual call-site distinctions; this is not a compiled-program correctness proof. The captured root script documents original execution paths; source-byte replay needs separately retrieved exact-commit files with those identities. Separate same-team review in review/ is not external nonconstructor promotion review. Primary source URLs are recorded below.

- https://heidata.uni-heidelberg.de/api/datasets/:persistentId/?persistentId=doi:10.11588/DATA/6MEKHI
- https://github.com/tychon/U1CircuitsData/blob/265b6671dde799d7c73f32247fa3ee93ae70e0f2/redpitaya-measurements/c/utility.c
- https://github.com/tychon/U1CircuitsData/blob/265b6671dde799d7c73f32247fa3ee93ae70e0f2/redpitaya-measurements/c/u1_drive1.c
- https://arxiv.org/html/2108.01086v1 (AppendicesA/B/C/F)

Web retrieval initially failed for all3pages; Firecrawl recovered paper/deposit and GitHub recovered exact source. An exact-repository calibration search returned0hits; that failure is retained without an absence inference. No instrument/error bound is filled using generic manufacturer specifications. Historical immutable sources, gates and HOLD/NO-GO conclusions are unchanged. No new mathematical retractions or frozen-source correction; full-session retraction ratio NOT_COMPUTABLE without a complete denominator. O03 controls remain protocol choices, not theory constants. PNG unavailable/unused; re-upload if needed. Notes/ASTER available but unused. Publication/CI/merge/tracking receipts are reported separately.
