# Append-only capture-manifest repair v0.1

**12 October 2026 UTC. ADMINISTRATIVE / EXACT byte inventory, not scientific review.** Physical promotion 0.

The existing [repository verifier](https://github.com/ud-tetra/UD/blob/main/scripts/verify_repository.py) failed on main-base commit `904d9902f60b121acb91e8036e837bff18aa3d9e` when [PR #36's integrity workflow](https://github.com/ud-tetra/UD/actions/runs/38188333768) enumerated six unmanifested files in two earlier capture directories. The same pre-existing issue can block [PR #35](https://github.com/ud-tetra/UD/pull/35). This repair adds **only new** `MANIFEST.json` files in the original capture directories and new immutable event files, plus this uniquely named explanatory capture. None of the six original files is modified, deleted or reclassified as independently reviewed.

| Pre-existing capture | Original files | Byte verification | Chronology limit |
|---|---:|---|---|
| `captures/2026-10-11-codex-op03-frame-alignment-v01/` | 4 | Current Git blob SHA-1, size and SHA-256 match the local original copies; the original internal `OP03_FRAME_ALIGNMENT_MANIFEST_v0.1.json` contains its own hashes for the three work files. | This retroactive repository `MANIFEST.json` does not claim an earlier freeze than the original commits. |
| `captures/2026-10-11T120000Z-codex-op03-outreach-prep/` | 2 | Current Git blob SHA-1, size and SHA-256 match the local original outreach file and a byte-exact fetched copy of the existing time note. | The timestamp embedded in its directory is a staging label, **not** a verified capture time; the original `CAPTURE_TIME_NOTE.md` says to use commit and PR #31 metadata. |

The new manifest describes the existing files as **retrospectively inventoried**, including their exact SHA-256 and sizes, and points to this repair. The new events date the repair itself; they do not backdate original evidence custody or turn constructor checks into independent results. The governing scientific statuses remain: OP03 target `NOT_RUN`, producer/review outreach artifact originally unaddressed and unsent, independent review pending, physical promotion 0. The audit of whether anyone later sent an invitation is a separate record and is not inferred from the historical file.

The repository verifier's implementation requires a `MANIFEST.json` beside every capture and a matching event; it rejects files not listed in the corresponding manifest. The old internal alignment manifest has a different filename and schema, so it does not satisfy that check. These additions reconcile the index without overwriting it. The branch should run `python3 scripts/verify_repository.py --base 904d9902f60b121acb91e8036e837bff18aa3d9e`; this administrative pass is not proof of any UD dynamical law.
