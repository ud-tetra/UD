# THM-534 v2.4 — Claim/dependency and branch firewall

**Date:** 2026-10-22. **Proof lane:** development / no registry promotion. **Physical promotion:** 0. **Parent:** THM-534 v2.3 PR #391, head `1444359cc7d4e7603f3de00e270e2ffcd4d34429`, originally based on `957d443e25008632ab9d9328c162343b6a651ee7`. **Context:** Q169–Q179 frozen signed support flows and ownership; v2.0 fixed real canonical contact model.

| Claim | Label | Typed objects | Dependencies | Conclusion | Reopening gate |
|---|---|---|---|---|---|
| P3 | EXACT / NO-GO | x,y in R^9, q,p in R^8, constant cotangent Poisson | frozen v2.0 x-dot=A(q)x for all y, unrestricted y | H linear in y, unbounded below for Ax != 0 despite bounded positive potential | restrict y or change Poisson/carrier/x dynamics as explicit new branch |
| P4 | EXACT CONDITIONAL | ψ in C^9, q,p in R^8, Hermitian iA_e | declared changed complex symplectic carrier, U>0, 0<=χ<=1, degree max 4 | H≥K+R≥0 | independent UD selection of symplectic carrier and energy origin |
| P5 | EXACT CONDITIONAL | ψ support amplitudes, real-part complex face/core current | P4, real skew contact operators | conserved H, ||ψ||², owned support readout with J=2dχ Re(ψ*_f ψ_c) | derive native complex amplitude/readout and physical time |
| P6 | EXACT CONDITIONAL | isolated one-contact ψ pair, initially real up to one phase | P4, v2.3 U profile, q=p=0, no overlapping potentials | isolated K+R=βS/2 and arrival fractions 3/5 and 2/5 | network coupling and gate reset; physical resource bridge |
| P7 | EXACT / NO-GO | two symmetric shared-face contacts | equal β/profile and unbroken apex-swap symmetry, shared face initially populated | equal wake accelerations; no exclusive deterministic contact selection | independently sourced orientation/asymmetry, non-equivariant input or stochastic selection |
| P8 | OPEN_GATED | physical source law and original UD support carrier | P3–P7 | positivity of shifted math H does not identify physical energy, original real canon, reset or THM-534 hop probabilities | source-complete carrier/action/measurement rule plus independent review |

**Scope controls**: No silent override of v2.3. The cotangent P3 no-go is retained. The complex Ψ replaces (x,y); equal real state components at initial time do not mean the two Hamiltonian systems are the same theory. The added shift 4||ψ||² is a conserved mathematical lower-bound offset, not a Planck, mass or action constant. The old Q171 real bilinear is preserved only on real relative-phase preparations; extension uses Re of complex coherence. All constants β and the gate profile remain supplied model parameters. No physical promotion.

**Execution**: exact 6,561 rational profile assignments, 256 Hermitian binary network checks, 250 random continuous-profile derivative tests, explicit unbounded cotangent controls, symmetric wake and exact isolated fractions. Verification by same constructor only. No independent adversarial reviewer, no blinded physical test, no physics calibration.

**Next programme gate**: test a native source rule that selects either the old real dual carrier or complex symplectic support and supplies exclusive contact admission and reset. Do not use existence of a positive mathematical Hamiltonian as evidence of physical energy correspondence.