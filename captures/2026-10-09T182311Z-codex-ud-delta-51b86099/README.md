# UD delta and admissibility closure audit, 2026-10-09

This capture preserves the five releases created during the pattern-and-delta analysis in chronological order. Each release archive preserves every original stage file and contains a replay script, exact result matrices, report, and local hash manifest. The adjacent HTML report and verifier entry point are convenient browseable copies with identical bytes to those inside the corresponding archive. Stage-specific manifests are also mirrored directly.

| Stage | Result for selected two-cell and shared-face observables |
|---|---|
| 01 | Fixed closed two-tetrahedron generator: minimum exact linear record 6 (cells alone 4); counterexample to snapshot sufficiency. |
| 02 | Shared-face incidence switching: six-coordinate closure; hidden eligibility counterexample. |
| 03 | Outer face incidence switching: minimum 10; all eight independent face–cell incidences: 14. |
| 04 | Deliberately broader edge–face and single-end vertex–edge stress tests: 16, 22, then 23. The 23 result depends on independent single-end control. |
| 05 | Source-typed face masks from ledger Q173: 14; conditional whole-edge extension of Q167 to the paired carrier: 22. Uniform vertex mode remains hidden. |

## Provenance and scope

Carrier: two filled tetrahedra `<0123,0124>` on a 23-coordinate real chain register. Baseline `A=B^T-B` with unit incidence metric. Results concern exact autonomous linear records for specified observables and arbitrary real initial states under the gate families stated in each report. Mask eligibility, timing, topology transitions, computational speedup, and physical identification have not been derived. The whole-edge construction on the two-tetrahedron carrier is a conditional extension of ledger Q167, whose six-edge verification concerned a single tetrahedron. Q173 was verified for seven face masks on the paired carrier. Constructor checks do not constitute independent review. Physical promotion: 0.

Historical context: attached `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, including Q145, Q153, Q167, Q169, Q172 and Q173, and `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` (marked a proposal). Their original bytes are not modified by this capture. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read and is not captured. The public portal was not freshly audited for this sequence; this capture does not claim to supersede its current manuscripts.

## Replay

Unpack each stage archive into a separate empty directory and run its entry script with standard Python. The archive preserves the script dependencies for that stage. Constructor assertions are 18, 21, 28, 83, and 47 new checks by stage respectively. These counts describe scoped assertions, not independent replication or hardware evidence.

The repository `MANIFEST.json` records SHA-256 and byte length of every path. Do not treat an imported report as a public theorem or a claim of physical promotion. Subsequent corrections should be new captures with `supersedes` links.
