# Acquisition evidence audit and fresh-validation gate

Primary source audit completed 2026-10-19. Development — no registry entry. Physical Promotion=0.

The public author code now supplies a pinned acquisition recipe: nominal 125 MHz base, decimation 64 in drive1, 16384 samples, external negative edge trigger, averaging enabled, RP_HIGH input gain, and default precision %f output. It does not supply calibrated intervals or prove the binary and device configuration used for this released file. The oscilloscope GPIO header's /8 description conflicts with executable /64; a separate drive2 program uses /8. Program provenance must be resolved, rather than mixing their settings.

| Contract role | Evidence gained | Remaining admissibility gap |
|---|---|---|
| Source custody | heiDATA v1.0 release API; 32 raw archive PID / MD5 / size records | Published MD5 is metadata, not newly verified content or authenticity |
| Acquisition configuration | Pinned author code; channel / trigger recipe | Exact compiled binary, firmware/API version, boards/serials, physical wiring and sample file binding |
| Amplitude calibration | Nominal gain mode and decimal serialization setting | Per-channel gain, offset, domain, nonlinearity, noise and quantization intervals and accepted authority |
| Clock and timing | Nominal 125 MHz / 64 recipe and trigger chain description | Actual rate, origin, skew and jitter bound to this source and derivative / band domain; shared trigger is not shared clock proof |
| Anti-alias | Averaging flag seen | Analog / digital transfer and out-of-band alias error enclosure for actual configuration |
| Joint / computation | Code describes serialization; conditional timing error lemma supplied | Simultaneous coverage, budget without double counting and implementation rounding proof |
| Physical model | Existing three-wave mixing oscillator equations with amplitude dependence; feedback/loss relevant | Actual parameters, domains, readout, preparation and source-work history, justified alternative, validated solver / margins |
| Fresh confirmation | 32 archive metadata inventoried before any new raw | Existing 05-21 exposed; 05-28 filename is a candidate only, not independent fresh data |

No request field is silently filled. All 128 original template blockers remain unresolved as qualification evidence. BLOCKER_MAP.json maps every exact PR250 blocker path to relevant source IDs and missing evidence status. Presence of equations and hardware code does not establish calibrated physical prediction.

RAW_METADATA_INVENTORY.json contains only published metadata. Its 32 gzip files include 30 four-channel-labelled and two ten-channel-labelled archives. Selected 05-21 is already exposed. Candidate 05-28 is frozen before any raw read, has nominal 0.050 V drive and CH9 empty / CH10 site5 instead of CH9 site5 / CH10 empty. It requires a new versioned source and channel-lane request; the current packet bound to the exact source cannot simply be reused. Different folder, date or hash is insufficient for independent lineage. No fresh confirmatory source was admitted in this finite audit. It is not a claim that no appropriate data exist elsewhere.

CANDIDATE_INTAKE_FREEZE.json gates all candidate inspection on independent custody / exposure review, calibration coverage and a reviewed and frozen physical model, comparator and scoring plan. No model is invented or frozen just to open data. No raw download, new fit, notebook execution, hardware contact or outside outreach occurred. Generic manufacturer specifications are context only: they do not identify the board variant or supply this acquisition's calibration certificate.

TIMING_ENCLOSURE.md supplies a conditional mathematical timing-to-vector error map with exact nominal rate arithmetic and explicit unsupplied premises. It is not an empirical bound. verify_audit.py checks inventory shape, all 128 blocker keys, candidate pinning, exact timing identities and rational clock inequalities.

Sources and limited excerpts are in SOURCE_EVIDENCE.json, with actual access failures retained. The paper's 2026 HTML render date is distinguished from its 2021 arXiv submission and 2022 dataset release. Attachments/governance are bound in INPUT_BINDINGS.json. This work does not replace the PR250 source specific request or change old receipts.

