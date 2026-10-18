# UD fixed-reference temporal-span certificate v0.1

The new amplitude-independent span proof certifies the saved coherent-DC
floating output that the previous fixed-amplitude residual proofs left on HOLD.
The estimator, its outputs, the fixed reference phases and strict matching gates
are unchanged. Physical promotion 0; development — no registry entry;
independent review pending.

| Saved floating output | New certified phase error, radians/sample | Previous certificate |
| --- | --- | --- |
| coherent_dc | <1.256e-11 | Frobenius and operator-residual proofs HOLD |
| dense_sign | <0.000502361 | Operator-residual proof <0.000889144; Frobenius HOLD |
| phase_2neg20 | <3.802e-7 | Floating residual proof <1.805e-5 |

These are upper bounds on emitted-phase error relative to a fixed fitted
reference, not observed errors, physical-frequency measurements, or a uniform
noise-ball guarantee. All previous HOLD receipts are preserved; the new version
adds a separate sufficient proof. No re-fitting or fresh estimator execution
was performed. The known constructor controls and outputs were available
before the new code/control freeze; no blinded or independent data is claimed.

## Why it helps

A stationary amplitude offset may change the record while leaving its temporal
span unchanged. The prior proof charges the entire model-amplitude discrepancy
against phase uncertainty. The new verifier directly encloses ||P-U D||_2, where
P is the fixed real reference frame, U is the actual saved floating basis and D
is an untrusted auxiliary reduction. The polar factor of U has exactly the same
range, so this residual bounds the reference component outside the captured
span. Full-rank coefficient changes preserve that span; arbitrary noise or
loss of excitation need not. THEOREMS.md gives the exact conditional theorem.

The phase frame is evaluated with validated 512-bit arithmetic. Actual floats
are encoded exactly as dyadic integers; an exact 105-by-105 Gram bounds the
residual operator norm. Reference frame conditioning and separation constants
are recomputed from the fixed phase integers and checked against their parent.
Actual shift, eigenpair, inverse, angle and ties-to-even emission checks remain
unchanged. No numerical SVD/eigensolver accuracy assumption is required.

## Verification and replay

Three saved-output certificates and three separate exact-array replays agree.
Eight checks pass, covering the real/complex frame scaling, amplitude/span
identity, exact encoding, corrupted reduction, wrong span, singular basis,
shift/inverse/argument refusal and hash tampering. Two additional frozen controls
corrupt the actual coherent-DC reduction and shift; both produce HOLD and replay
identically. These are constructor checks, not independent review.

Extract the core ZIP and all three floating-witness ZIPs listed in
WITNESS_INDEX.json into one directory, then run:

```
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

Runtime: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0.
The runner verifies every package/witness hash and recomputes all span, shift,
eigenpair, inverse, argument and frame-constant bounds in a temporary copy.
Existing receipts remain intact. Every float array needed for this new proof
and every new reduction is retained. The reference proposal, actual proposals,
parent verdicts, freeze and controls are included.

This proof uses saved floating outputs from PR187 and PR186. It projects zero
new raw readings and reruns no estimator or full-Hankel verification. The parent
raw-to-sketch checks and exact sketches remain in those parent packages; their
source custody is not re-established here. OMISSION/PROVENANCE identify that
boundary. Independent replay #130, review HOLD #177, metrology and acquisition
qualification remain open. The 747-dimensional nominal dynamical observer
kernel, 62 history channels and separate 189 diagnostic outputs are unchanged.
O03 tolerances remain protocol controls; no CRL or physical promotion is made.
