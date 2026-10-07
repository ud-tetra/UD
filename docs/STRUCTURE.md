# Repository structure and archive recovery

| Path | Purpose |
|---|---|
| captures/ | Immutable per-session scientific files, source snapshots and manifests |
| events/ | One independent JSON event per contribution or amendment |
| state/ | Versioned checkpoints; new files supersede rather than overwrite |
| manuscripts/ | Versioned paper sources and PDFs |
| docs/ | Contribution and capture procedures |
| scripts/ | Import, integrity and reconstruction tools |
| .github/ | Review templates, ownership and CI |

The initial capture combines the complete accessible portal snapshot, current UD-named Library files and supplied session attachments. Each inventory item retains a source identity, original path, SHA-256 and byte size. The raw snapshots use deterministic gzip tar bundles, split into small binary parts for ordinary Git storage. `python3 scripts/restore_capture.py captures/<capture-id>/MANIFEST.json <destination>` verifies every part and restores the original snapshot tree. The tool refuses to replace an existing destination file or traverse outside the chosen destination.

The import does not contain hidden model state, deleted/unexported conversations, inaccessible versions or unavailable attachments. Those limitations are recorded in the capture receipt. Imported files are preserved evidence, not automatic canon or new physical results.
