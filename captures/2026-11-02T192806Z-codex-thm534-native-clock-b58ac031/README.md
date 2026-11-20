# THM-534 v2.25 — Local clock and phase-retaining capture

The original native gradient sector supplies a clock readable on a private vertex star. A revised five-amplitude guard stores its event phase in the existing protected face sum, using the original hold mask. This is conditional local capture, with clock preparation and autonomous mode execution still open.

Read THM534_LOCAL_NATIVE_CLOCK_AND_EVENT_MEMORY_OBSTRUCTION_v2.25.md for definitions, proofs, source sections, counterexamples and limits. CAPTURE_CONTRACT.json fixes the candidate branch; CLAIM_DEPENDENCY_LEDGER.json records its scope.

Reproduce with Python standard library:

    python verify_clock.py
    python verify_controls.py

The first command regenerates RESULTS.json. The second rejects two altered models and verifies a fresh byte-identical replay. No numerical solver or external dependency is needed. Analytic claims are proved in the manuscript; finite controls do not substitute for those proofs.

EXACT controls: 128 masks, 512 Cayley clock cases, 8 hold masks, 56 ownership cross terms, 72 revised event/hold cases, original and revised switch ranks. The revised rational witness has determinant -1/3 and full carrier rank 23. The original peak guard remains singular even with a passive prepared clock.

This candidate uses a declared guard coefficient one, a prepared nonzero clock, known clock branch and supplied sticky Load/Hold execution. It is not a parameter-free autonomous law. Lower clock stock improves peak proximity but worsens event-time precision. Continuous and Cayley clock parameters are not interchangeable.

Development — no registry entry. Constructor checks only; independent review pending. Physical promotion: 0.
