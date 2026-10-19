# Portable replay correction — version 0.2

Root review found that the original verifier requires seven absolute scratch paths. Its recorded PASS is valid only for that original environment; it does not establish portability to another checkout.

All ten original files, including MANIFEST.json, remain byte-identical. Version 0.2 adds explicit --repo and optional --governance-root parameters. INPUT_BINDINGS_v0.2.json classifies five repository inputs by stable paths relative to the supplied checkout and two governance inputs by canonical filenames beneath the supplied governance directory. No original absolute path fallback exists. A missing governance root returns HOLD; it never reports those attachments as checked.

Canonical governance filenames:
- UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md
- UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md

The caller can supply these as captured copies or independent external inputs with exactly the original bound hashes. Relative input paths and their resolved targets must remain beneath the declared roots; escaped symlinks return HOLD. The verifier has no output path option and prints JSON to stdout only. It performs no network, waveform, fitting or hardware action.

The scientific observations, 128 unresolved qualification blockers, candidate embargo and conditional timing lemma are unchanged. This is a post-review portability correction, not a new calibration result or independent review.

Before the first v2 execution, PORTABILITY_FREEZE_v0.2.json binds the v2 runner, stable bindings, control code and this correction. The control runs from a renamed temporary audit directory and a separate minimal relocated checkout. Empty or wrong supplied roots must fail even while the original absolute inputs remain accessible. Hash mutations, missing governance, escaped symlinks and optimized Python are refused. All staging writes occur only in temporary directories, which are removed afterwards.

