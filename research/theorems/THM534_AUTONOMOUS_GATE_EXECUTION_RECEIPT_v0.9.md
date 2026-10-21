# THM-534 v0.9 execution, correction and release receipt

**Date:** 2026-10-21 | **Scientific state:** scoped exact mathematical theorem and constructed autonomous candidate | **Constructor checks:** PASS_SCOPED | **Independent non-constructor review:** PENDING | **Physical promotion:** 0.

**Primary:** [THM534_AUTONOMOUS_GATE_RESERVOIR_v0.9.md](THM534_AUTONOMOUS_GATE_RESERVOIR_v0.9.md) (S29–S34).  
**Claim delta:** [THM534_AUTONOMOUS_GATE_CLAIM_LEDGER_DELTA_v0.9.md](THM534_AUTONOMOUS_GATE_CLAIM_LEDGER_DELTA_v0.9.md).  
**Published compact exact code:** [verify_thm534_autonomous_reservoir_v0_9.py](verify_thm534_autonomous_reservoir_v0_9.py).  
**Alternative implementation:** [verify_thm534_reservoir_fraction_v0_9.py](verify_thm534_reservoir_fraction_v0_9.py) (Python standard-library arithmetic).

## Source and execution contract
- K4 filled, oriented unit simplicial boundary.
- Q162 \(j=-H B_1^\mathsf T\rho/4\) and Q156 product-form hard edge mask.
- **New candidate:** vertex reservoir \(r\ge0\), availability proxy \(\chi^{avail}_v=1[r_v>0]\), local selector \(h_{uv}=\chi^{avail}_u\chi^{avail}_v\beta_u\beta_v\tau_{uv}\), with static β,τ in primary sweep.
- **New candidate:** reciprocal exchange \(s=(r-p)/4\), \(\rho'=p+s\), \(r'=r-s\), \(p=\rho+B_1j\); 1/4 reservoir coefficient is an explicit **separate conditional choice**, not a derivation from Q161.
- This model provides a **complete transition rule on its declared state space**, not a derivation of the native UD closure/admissibility ontology; it does not replace the frozen v0.39 source ledger.

## Local constructor replay (full executed script)
The actual full local source file \`verify_thm534_autonomous_reservoir_v0_9.py\` (longer than GitHub compact verification) was executed. SHA-256 **60e3454b13888bfd162c8c2b66b4a1f28578cf64ec455afb29f9bf78fd57c359**.

Results:
- **4,096** exact initial support/boundary/integrity control cases.
- **24** S4 relabelings of the declared complete update.
- Exact first mask \(h=(1,1,0,1,0,0)\) and vertex/reservoir stocks \((5/8,7/16,7/16,0)\), \((7/8,13/16,13/16,0)\).
- Exact sourced nonzero signed face circulation \((0,1/4,1/4,0)\).
- Exact contrast eigenvalues \((15\pm\sqrt{97})/32\), decay identity for 12 exact steps.
- **9** reversible rotor control steps, face012 component exactly one at every event.
- **8,192** numerical finite updates (32 initial states × 256 steps), of which **4,096** have nonuniform selected masks and **1,574** have nonzero face norm \(>10^{-12}\).
- Maximum combined-stock numerical drift \(1.7763568394002505\times10^{-15}\); maximum negative Lyapunov remainder from floating error \(1.1401454618356886\times10^{-16}\); oriented face-closure residual zero on the tested stencil.

## Independent-implementation arithmetic (same constructor)
The different, standard-library-only \`verify_thm534_reservoir_independent_v0_9.py\`, SHA-256 **cb82b82a12c5e04a91bf1f7129607c688f3a8d88362ae9aef632408e2c3c34d0**, returned PASS:
- 64 exact independent Fraction control cases; **24** have nonzero face circulation;
- positive stocks and total stock preserved;
- exact local paired-reservoir source accounting, oriented \(B_3^\mathsf TF=0\), and eight-slot Lyapunov inequality verified.

This counts as *independent implementation method*, **not non-constructor adversarial review or replication**.

## Corrections
A preliminary constructor run failed because \`int(sympy.logic.boolalg.BooleanTrue)\` is not a valid Python integer conversion. The code was repaired to \`int(bool(...))\` before tests; no mathematical or numerical source input was changed to fix a theorem mismatch. The final actual source hashes above identify the passing scripts. Preserve this development correction; no previous source is overwritten.

## Release package
A local conversation ZIP \`THM534_AUTONOMOUS_GATE_RESERVOIR_v0.9_RELEASE.zip\` contains the **full executed** constructor source, separately implemented pure-Fraction script, result JSON, console receipt, README, SHA-256 manifest. ZIP SHA-256: **fe6957a62e45448fa89b4bfedb119978902f846ae9bcebc8668eb9c0ba9fd73e**. It is a local artifact and has **not been copied into GitHub as a binary**; published GitHub compact source differs in bytes, so only the specific local script SHA refers to the original passing execution.

## Decision / block
**EXACT conditional:** the specified model conserves paired vertex/reservoir stocks, generates a nonuniform positive gate from its *own* state, produces nonzero transient face circulation, and obeys a finite total circulation budget. An *additional independently oriented conservative rotor* can sustain nonzero circulation but is **not** Q162 and has no sourced phase/framing dynamics.

**OPEN/FREEZE:** stock-availability bit is not the native UD closure predicate; β/τ still supplied; no model of gate closure/fracture, physical reservoir/energy, intrinsic rotor orientation, endpoint source work, physical clock or original THM-534 six-edge Markov probabilities. No physical promotion, no independent review, no confirmatory target-blind study.

**Next closure gate:** obtain and prove a primitive admitted dynamic closure/transport-integrity rule and state-dependent reservoir ownership (including a gate-closing/reset mechanism), then test genuine physical/source equivalence only after independent correspondence.
