# Parity contract review packet v0.1

**READY FOR REVIEW; NO REVIEW ATTESTATION SUPPLIED.** Constructor packaging and replay only. Physical promotion0. This packet concerns the prospective parity contract, not the separately versioned floating-estimator review campaigns.

Target contract SHA-256: `860713fe9386d5d08559d79565be0013edc424685dfdb715b9ff7e25d883cdfe`. TARGETS.json SHA-256: `95f00600e4bf47746a710004bdc72e457f03e5913ff53a36540a9dd534257f3e`. The outer repository MANIFEST binds the ZIP; verify its hash before extracting into a new empty folder. All ZIP paths are relative and no links are included. The retained paths make the pinned reconstruction self-contained; no network, pip dependencies, credentials, or full repository checkout are needed.

## Minimal replay

Use Python3.12 (constructor-tested runtime; portability beyond it is not certified). From the extracted packet:

```bash
python3 review.py
python3 review.py --replay --output-dir /absolute/path/to/a/new-empty-output-directory
```

The output directory must not exist and must be outside the packet. The launcher verifies all payload hashes before running code, then runs only the frozen prospective self-test and new public constructor probes. It never runs historical C/D scripts; those files are source data only. The input/program paths preserve their original bytes. Capture the printed and written receipts, Python/platform context and any new reviewer-owned attacks. Process exit status alone is not the candidate verdict: inspect the frozen validator's JSON status. `validate(case,a,p)` is a low-level helper; the CLI rebuilds trusted A/P through `source()`.

These commands replay constructor fixtures. They do not establish reviewer independence, a fresh blinded cohort, numerical interval certification or physical parity. A replay receipt is deliberately UNQUALIFIED until an attributable reviewer supplies a return.

## Submit a scoped return

Copy REVIEW_RETURN_TEMPLATE.json outside the immutable packet. Fill reviewer attribution, relationship/independence declarations, UTC time, methods and the items actually checked. Keep unperformed items explicit; no prefilled PASS or signature is supplied. Add relative-path SHA-256 entries for your execution files if claiming a fresh execution. Run:

```bash
python3 check_return.py /absolute/path/to/your/return.json
```

RETURN_STRUCTURALLY_COMPLETE means fields and hashes are coherent; it does not authenticate a reviewer, prove independence, adjudicate science or enact promotion. Partial static review may validly return OPEN. External-AI, human and constructor-team records remain different classes. A new blind campaign needs its own frozen protocol and evidence; this packet is not that campaign.

The current source ledger and governance proposal keep their original versions. No proposal provision is enacted by preparing this review. Gap2_FINAL_Finite_Genesis.png is unavailable and unused.
