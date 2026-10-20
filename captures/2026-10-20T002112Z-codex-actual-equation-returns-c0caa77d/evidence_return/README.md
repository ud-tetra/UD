# Independent evidence return requirements

Development — no registry entry. External nonconstructor review PENDING. Physical Promotion = 0.

This is an **UNSENT request and return-content profile**, not evidence, an attestation, a data-release authorization or a physical qualification. It organizes the next external return rather than adding another general metadata validator. No recipient has been selected or contacted. No laboratory, reviewer, calibration value, signing identity or experiment result has been fabricated.

The profile has fourteen requested return artifacts. Their expected filenames are not files already received. The exact 128 original PR250 request paths map to a requested artifact and content section in BLOCKER_RETURN_CROSSWALK.json. Those 128 paths are an initial missingness diagnostic, not 128 independent scientific gates. Current candidate v0.2 has 170 null leaves, also not 170 independent gates. All actual qualification remains HOLD.

| ID | Requested evidence role | Expected return filename |
|---|---|---|
| R01 | Authority and independence | returned/01_authority_and_independence.json |
| R02 | Custody, configuration and domain | returned/02_custody_and_domain.json |
| R03 | Per-channel amplitude calibration | returned/03_channel_calibration.json |
| R04 | Clock and time-to-voltage propagation | returned/04_clock_and_time_domain.json |
| R05 | Passband and alias budget | returned/05_transfer_and_alias.json |
| R06 | Joint error coverage and allocation | returned/06_joint_coverage_and_budget.json |
| R07 | Validated computation | returned/07_validated_numerics.json |
| R08 | Primary physical model | returned/08_primary_model.json |
| R09 | State, preparation and readout | returned/09_state_preparation_readout.json |
| R10 | Drive, feedback, loss and energy | returned/10_drive_feedback_loss_energy.json |
| R11 | Justified physical comparator | returned/11_comparator_model.json |
| R12 | Pre-outcome model and score freeze | returned/12_frozen_analysis_protocol.json |
| R13 | Genuinely fresh source and error coverage | returned/13_fresh_source_lineage.json |
| R14 | Attributable external content review | returned/14_external_review_return.json |

Read UNSENT_EVIDENCE_REQUEST.md for the reviewable draft; RETURN_REVIEW_GUIDE.md for lane separation, evidence meaning, conditional propagation and decision order. EXTERNAL_RETURN_RECEIPT_TEMPLATE.json is deliberately blank and must never be cited as review. It lists R01–R13 as reviewed content; R14 is the return statement itself, pinned after completion by a separate manifest/custodian rather than a circular self-hash. EXAMPLES.json distinguishes a return eligible for content review from verified evidence and physical promotion.

The two joint-error routes are alternatives. A deterministic simultaneous enclosure need not supply a covariance model or a statistical coverage fraction. A statistical route must justify its population/dependence and simultaneous coverage. Inactive-route fields may be expressly N/A with a reviewed route and explanation. The crosswalk covers every original path without demanding both routes. No actual route has been chosen here.

Existing 05-21 records and 05-28 candidate have known exposure. Current 05-28 use is retrospective exploratory in the present model lineage; a new label, hash or local lack of waveform access cannot erase public outcome-derived parameter use. Fresh confirmation needs a new independently reviewed source/domain and a prospective model/comparator/score freeze. Current filenames, channel roles and drive labels are not calibration or wiring evidence. No candidate count/crop or old 1000-record/N16184 budget is transferred to a new source.

The synthetic 209-temporal test, native 62×37/1893-history observer and published 10-channel component are separate lanes. No padding/remapping or equation of internal q=2^-48 with volts or seconds is permitted. A physical realization, state/action/readout/unit map and its independent validation are separate requirements before any UD bridge.

SOURCE_BINDINGS.json pins the existing source requests, exposure findings, exact blocker map, timing lemma and governance. New external retrieval was unnecessary. The packet supplies no new raw data, numerical fit, physical model selection, hardware operation or external communication.

verify_inventory.py performs a read-only structural inventory/hash/crosswalk check with an explicit --repo root. It does not open evidence references or certify their truth. FREEZE.json was recorded before its first execution; INVENTORY_RECEIPT.json records the result. The parent capture supplies publication and merge status.
