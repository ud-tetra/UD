# OP03 coordinate-seat and null-window test protocol v0.2.1 — candidate freeze

**Frozen 11 October 2026 UTC before any new independent endpoint exposure.** This is a test protocol for a proposed amendment, not a replacement of OP03 acquisition v0.2 and not physical promotion.

## Inputs frozen before targets

For every candidate index (n), retain the v0.2 source packet and hash: ordered oriented (C_1) action; frame basis and extraction route; pre-event (\theta^-\); active and output lineage identifiers, continuation and addition maps; pair-seat images or an explicit frozen seat assignment; viability, equivalence, integrity, and burden receipts; previous completed Θ event (\tau_\Theta); producer identity and code/version hashes. If testing the memory route, freeze ((q,p)) six-basis probes and the separately sourced observed/co-moving 12D maps. Declare the frame route **once per producer** before any endpoint target.

## Candidate decision order

1. Run the existing exact frame gate, receipt-index, feasibility and tie gates; preserve every hold reason.
2. On coordinate-complete output lineage (\mathcal L^+=\operatorname{span}\{e_p:p\in S^+\}\), require (\{p:\theta^+_p=0\}=S^+\), and require integrity on every open seat. If no such endpoint exists, return `SEAT_INTEGRITY_HOLD`. Non-coordinate output lineage without an independently frozen address map returns `SEAT_MAP_MISSING`; no nearest coordinate completion.
3. Compute (a=\bar\theta^-\oplus\theta^+\). If (a=000), emit `ADMISSIBLE_NO_CHANGE`. If (a\ne000), emit `THETA_SWITCH`, even when (\mu_\Theta=0\). Keep frame-only updates in a separate typed register; they do not automatically reset (\tau_\Theta\).
4. A no-change result does **not** advance the previous-completed-Θ-event index. The first predicted Θ switch is the minimum candidate (n>\tau_\Theta\) with all source gates passed and (a\ne000\). Consecutive no-change windows remain in coverage and timing denominators.

## Target-blind scoring

Hash the prediction stream before accessing sealed endpoint frame and Θ receipts. Report exact coverage, hold reasons, event-versus-no-change confusion counts including null windows, first-switch index, (\mu_\Theta\), seat assignment, (a\), and full affine receipt separately. A valid in-domain wrong switch/no-switch or seat prediction fails its respective universal candidate claim; zero failures in a finite corpus gives at most scoped partial pass. Missing or target-derived seat receipts make the record `INVALID_REPLAY`. Any exposure before this freeze makes reanalysis exploratory and requires a fresh cohort for confirmation.

## Rollback

On a counterexample, revert only the candidate seat/no-op source claim and its dependent timing predictions. Preserve independently checked incidence identities, the 12D native memory lift, rank-nullity and the conditional frame extractor. Physical promotion remains 0.
