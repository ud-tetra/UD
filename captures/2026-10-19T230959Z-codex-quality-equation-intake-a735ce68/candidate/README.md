# Candidate intake: explicit exposure, null calibration, no raw release

This continues PR252 for the 05-28 ten-channel archive `doi:10.11588/DATA/6MEKHI/NH8JC2`. The newly inspected immutable author notebook source explicitly uses the exact candidate to select spectral features, infer a coupling, and feed sections labelled Figures4,7,8. It cannot be promised untouched confirmation. The candidate is now scoped to retrospective exploratory use only, and remains HOLD before raw access.

`CANDIDATE_REQUEST_v0.1.json` preserves the filename CH9-empty / CH10-site5 mapping and the drive label without pretending that either is verified wiring or calibrated voltage. Raw SHA256, record/group counts, actual drive interval and all calibration/model evidence remain null. The complete original PR250 calibration/model request fields are retained unchanged. `REQUEST_SCHEMA_v0.1.json` is a new identity-specific schema, not a replacement or silent re-targeting of PR250.

`SOURCE_CELLS.json` retains selected source cells with original indices and immutable Git blob identifiers. Only source text was inspected; outputs were deliberately excluded. Author license is retained. Initial Firecrawl raw-notebook access failed; GitHub immutable blob retrieval supplied source cells. No new waveform archive download, raw inspection, fit, author-code execution, external communication or hardware action occurred.

`THEOREMS.md` gives the exposure obstruction and ordered pre-raw custody/calibration/model-freeze gates. `check_request.py` checks metadata only, writes stdout only, and opens no evidence URIs, raw records, notebook outputs, keys or signatures. It never authorizes data or counts qualification blockers as closed. A completely filled declaration is still unverified, and actual admission needs accepted evidence and nonconstructor review plus custodian ruling.

Replay: `PYTHONDONTWRITEBYTECODE=1 python replay.py`. This verifies the prospective source/code/request freeze and reruns frozen controls without raw or model fits. Review is same-team development; external nonconstructor review remains PENDING. Physical Promotion=0.
