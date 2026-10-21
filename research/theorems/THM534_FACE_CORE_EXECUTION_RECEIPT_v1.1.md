# THM-534 v1.1 — Executed proof and GitHub publication receipt

**Date:** 2026-10-21 · **State:** PASS_SCOPED, development/no registry promotion · **Physical promotion:** 0. 

## Source identity and version
- Frozen source: `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, entries Q156/Q162/Q169–Q173 (face/core currents, boundary stocks and separate hard face gating). Prior v1.0 THM-534 support-readiness gate is not overwritten.
- New theorem: `THM534_FACE_CORE_RECEIPT_GATE_v1.1.md`, S42–S48. Exact mathematical calculations are conditional on a **continuously admitted face-to-cell channel** (Q173 face hard gate =1), a chosen unit metric and event-Cayley step ε=1/4. The native closure/boundary sign and AND rule is not derived from source.
- No externally fitted particle/mass/electromagnetic inputs, and no target-blind confirmation. Historical THM-534 weights already exposed.

## Local executions
- `verify_thm534_face_boundary_receipt_v1_1.py` (SymPy): **PASS**. Fourteen exact Cayley face/core updates with current-step Q162 burden movement and next-step edge gate readout, exact midpoint face and cell receipts, dual conservation, all 24 signed S4 relabelings at four event epochs, symmetric and full-off controls.
- `verify_thm534_face_boundary_receipt_fraction_v1_1.py` (standard-library Fraction): **PASS**. Independent-method 14-step exact recurrence, signed face/cell flux, burden+reservoir stock, nonuniform edge-gate chronology and nonzero burden-face circulation. Same constructor; **not** an external independent reviewer.
- Initial face/cell support norm exactly `3`; combined vertex burden+reservoir stock exactly `5` throughout the witness. First completed face-to-cell receipt is `(-18,50,16,16)/289`, with core support increase `64/289`.
- Gate sequence at events 0,1,4,7: `000000 → 001011 → 000000 → 010101`. Face-to-cell coupling remains operational despite all edge gates being off.
- Q162 face circulation at event 1: `(0,-3/16,-3/16,0)`; 7/14 checked events had nonzero circulation in this constructed finite witness. **The passive source budget guarantees eventual decay of Q162 circulation** (v0.9 S31).

## Recorded correction
An exploratory, earlier candidate used the *pre-event* instantaneous signed Q171 current as the binary event gate directly. The exact n=3 check falsifies identification with the **completed** finite event: prospective core current is `9678240/24137569 >0`, but core squared amplitude actually changes by `-932746816/6975757441 <0`. The v1.1 theorem now uses **actual midpoint flux receipts** and applies the selected mask at the next event. Earlier prospective signals are diagnostics only, not quietly promoted to receipts.

## Exact no-go and acceptance limits
- If all higher face-to-cell contacts are themselves hard-blocked, this model cannot bootstrap from all-off; likewise zero face/core support remains zero. Recovery has been shown from **edge-only all-off**, not globally disabled/no-source packets.
- Face permission bits are positive-ingress status, not native geometric closure existence. Face/core squared support, vertex burden, candidate vertex reservoir and physical energy stay typed separately.
- Asymmetric face dark-mode input is required for nonuniform lower masks in the witness; a symmetric face input yields uniform masks and zero Q162 face curl.
- Face hard admission `h_f^{23}=1` is assumed rather than selected from UD upstream primitives; the physical/ontological source of gate closure, damage, reset and actual field/energy coupling remains OPEN.
- The AND-vs-OR of incident face admission and positive-vs-negative sign criteria remain separate admissible candidate constitutive choices. No unique physical transition is derived.
- Independent non-constructor review, true physical clock, U(1) phase, Born readout, THM-534 six-edge hop weights, geometry/GR correspondence all remain OPEN; physical promotion 0.

## Files and checksums
The local release ZIP `THM534_FACE_CORE_RECEIPT_v1.1_RELEASE.zip` was checked with the Python zip reader, and has SHA-256:

`5dd7a2ce8df3de9dd323ca428ba024370a0bd5173d868a9b9e210bf46c6b1bc8`

It contains manuscript, claim-ledger delta, **locally executed** full source scripts, console receipts and SHA-256 file manifest. Source-file hashes and statuses are in `THM534_FACE_CORE_RECEIPT_v1.1_MANIFEST.json`.

All four principal files (theorem, ledger, SymPy verifier, Fraction verifier) were committed to `research/thm-534-theorem-session-audit-20261021` and their **Git blob SHA-1** verified equal to locally computed source bytes. This is a publication identity check, not an independent code replay. Draft PR #346 and issue #347 are the tracking entry points. Direct GitHub Project #1 membership is unverified. Independent reviewer pending.
