# v0.3.2 completion of executable-code capture

The original v0.3 draft record recorded the full 672-state `verify.py`, `run.log`, and `replay.log` as unavailable to the GitHub connector. This *additive* capture provides exact-byte Git blobs of all three files, verified against their original local Git blob hashes. The source original and earlier draft documents remain preserved.

| File | Source SHA-256 | Git blob |
| --- | --- | --- |
| `verify.py` | `dd62b30990797a2042014188861daf997ee72608d40396fe10169d93c174e708` | `48f94e05b8bfb0beeba4f933876eecf1e30d6949` |
| `run.log` | `9c545d45e0aa034d1acf3fc2a7e25ad1574772275064769796bb3c8164c2f1b6` | `5f8189edede7be3e44ec54a2452bcacf6a8bd7ea` |
| `replay.log` | `038c68d553b43eee1f8903062a7a0e15544fef2c2e7afd68af1b9abc7a51caba` | `b70624e5e3b6b3fb223436637634ffe3f9e03ba5` |

Now both runnable verification programs are on this branch. The original full `results.json` has **not** been transferred (the executable `verify.py` creates it deterministically); preserve its original local SHA-256 `46c149dcd8a006437a551b203e9d5c0c35439480a4080c624ff725ac5efb434a` and do not claim exact-byte GitHub preservation of that file. A local ZIP with all original artifacts remains the user download.

**Status**: local exact and independent verification passed; repository CI and independent non-constructor review pending. Physical promotion 0.
