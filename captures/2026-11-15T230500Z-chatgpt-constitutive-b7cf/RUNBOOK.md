# Review capture completeness and runbook

Local v0.3 package was constructed and exact checked 2026-11-15. The full source ZIP SHA256 is `99bd803422f03fc1edfd5d6ea14242192f0834ad696ec4a430be2aaefb291ab0`; it contains verify.py, replay_stdlib.py, full results, logs, a byte manifest and 5 source inputs.

**Files on this GitHub branch:** exact-byte REPORT.md (source original local SHA256), independent stdlib verifier, evidence index, and receipt/event. The 672-state SymPy main verifier and the unabridged JSON result are in the locally delivered ZIP and **not copied into GitHub by the connector**. This must be completed before claiming a GitHub-complete reproduction.

Run `python3 replay_stdlib.py` to test the 112-state exact independent marginal. Its script source is the same as the local v0.3 replay (Git blob match check requested separately). For the full matrix/boundary and 672-state enumeration, obtain original v0.3 ZIP, verify SHA-256, run `python3 verify.py`, `python3 replay_stdlib.py`, compare `results.json`. Install SymPy for the main verifier. The code does not require experimental data.

March source laws *do not* select p(d), κ, or a physical event clock. Q05/G05 and G06 remain gated. This is a research **draft**, no non-constructor review or independent empirical test. Do not merge until completeness and repo integrity checks are addressed.
