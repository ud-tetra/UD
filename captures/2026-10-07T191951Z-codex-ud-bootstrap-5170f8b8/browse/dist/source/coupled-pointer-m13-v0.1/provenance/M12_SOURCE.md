---
title: "A Pair-Only Autonomous Endpoint and an Independent-Work Retention Limit"
subtitle: "UD M12 development addendum 0.1"
author: "Benjamin Walker Mayes / Codex constructor"
date: "5 October 2026"
---

**Development — no registry entry. Independent review pending. Physical promotion 0.** This follows WBS 5.2 with an explicit changed-generator candidate, WBS 5.3/4.3 with its full-state window test, and WBS 3.1–3.2 with small-instance structure/cost calculations. It does not implement the full 380-qubit bank, native preparation or a general autonomous pair controller. M11's direct encoded-generator obstruction remains valid and unchanged.

# 1. Candidate scope and its predeclared small resource envelope

Keep M11's clock encoding: addresses 0,1,2 correspond to binary 00,01,11, with 10 padding. There are two clock qubits and one work qubit B. Clock dimension 3 is prime; encoded clock capacity is 4=2^2. Full encoded dimension is 8=2^3, valid dimension is 6=2·3, and padding dimension is 2. Initial clock |00> and the work state are supplied. The work may be entangled with arbitrary external spectators. No external switch or pulse timestamp acts after launch.

Choose positive engineered frequency scale kappa_C, distinct from the full-controller scale kappa_0=4096. For this toy, set N_max=3 binary factors, grouped onsite/pair norm cap h_max=3·kappa_C/2, and total term-norm cap J_max=4·kappa_C. These are finite design limits for this small test, not measured capability, native constants or full-controller limits.

The three-address free clock encoded on its two qubits has generator
\[
H_C^{\mathrm{enc}}=\frac{\kappa_C}{\sqrt2}(IX+ZX+XI-XZ).
\]
Replace the dressed gate-history generator with an independent clock and an onsite work rotation:
\[
H_{\mathrm{pair}}=H_C^{\mathrm{enc}}\otimes I_B-\kappa_C I_C\otimes Y_B
=\frac{\kappa_C}{\sqrt2}(IXI+ZXI+XII-XZI)-\kappa_C IIY.
\]
Every term acts on at most two binary factors. The full generator, including the clock, is pair-supported; there are no extra ancillary qubits. The encoded valid clock subspace is invariant. Unlike M11's global zero extension, the padding block here contains work precession -kappa_C·Y. That explicitly declared changed extension is allowed; the candidate is not claimed equal to M11's generator on the full space.

The clock and work do not interact. This is an **endpoint-compressed comparator**, not a timer that causes chronological X-then-Z execution. The known product ZX=iY has been supplied directly in the work generator. That operation is unusually simple; no general many-qubit source word is thereby synthesized.

# 2. WBS 5.2: exact joint endpoint with a constant pair generator

**Theorem M12.1 (ready-clock endpoint).** For any work input, including its entanglement with any spectator, at T_C=pi/(2·kappa_C),
\[
e^{-iT_C H_{\mathrm{pair}}}|00\rangle|\psi\rangle
=-|11\rangle ZX|\psi\rangle.
\]
The encoded clock stays valid at every time. At 2T_C=pi/kappa_C, the complete encoded unitary is -I, hence its channel returns to identity.

*Proof.* The clock and onsite work terms commute and have disjoint support. Their propagator factors. The free three-address spin clock transfers |00> to -|11> at T_C; the work factor is $e^{i\kappa_C T_CY}=iY=ZX$. Their tensor product gives the same joint ready-clock endpoint as M11. The clock free spectrum is -2·kappa_C,0,0,2·kappa_C on its encoded space, so it returns at 2T_C. The work propagator then equals -I. Clock invariance follows from its support-wise encoded free-clock construction; the work term cannot leave the clock code. Spectator tensoring preserves these identities. $\square$

Thus an autonomous pair-only endpoint exists for this tiny supplied task. M11's positive direct-generator distance never implied endpoint impossibility. The intermediate joint trajectories differ: M11 correlates its clock prefixes with X and ZX, while this candidate keeps the clock independent and continuously rotates B about Y. A numerical midpoint comparison records that difference. No source-production, capture, donor-renewal or failure-history claim is inherited from endpoint equivalence alone.

# 3. WBS 4.3 and 5.3: compute the actual full-state window error

Fix the auxiliary target **before** execution as the same freely propagated encoded clock state chi_C(t). The work target is the completed ZX operation. Therefore, for an arbitrary work/spectator state rho_BR,
\[
\rho_{\mathrm{actual}}(t)=\chi_C(t)\otimes
[(e^{i\kappa_CtY}\otimes I_R)\rho_{BR}(e^{-i\kappa_CtY}\otimes I_R)],
\]
\[
\rho_{\mathrm{target}}(t)=\chi_C(t)\otimes
[(ZX\otimes I_R)\rho_{BR}(ZX\otimes I_R)^{\dagger}].
\]
Because the clock is identical and independent in these two explicitly proved states, tensoring it preserves trace distance. This is a legitimate full-state reduction for **this candidate**, not permission to ignore timer correlations in another design.

**Theorem M12.2 (worst joint error).** With trace distance using the one-half convention, the supremum over work inputs and arbitrary spectators at a fixed time is
\[
E(t)=|\sin(\kappa_Ct-\pi/2)|.
\]
For the interval [pi/(3·kappa_C),2·pi/(3·kappa_C)], its uniform supremum is exactly 1/2, attained at either endpoint by work |0>. Consequently the candidate fails M11's 11/100 window threshold even with perfect preparation and exact couplings.

*Proof.* Relative to ZX the work evolution is a Y rotation through delta=kappa_C·t-pi/2, up to an irrelevant global phase. For any purified work/spectator input, its overlap with the rotated state is cos(delta)+i·sin(delta)·expectation(Y). Its squared magnitude is at least cos(delta)^2, so pure-state distance is at most |sin(delta)|. Partial trace gives the same upper bound for mixed inputs. Work |0> has expectation(Y)=0 and attains it. Delta ranges from -pi/6 to pi/6 on the selected interval, giving the exact maximum 1/2. $\square$

On the common left-endpoint work input |0>, M11's joint error is sqrt(247)/16, while this candidate's is 1/2. The improvement is real but insufficient. Reducing the requested interval to a narrower neighborhood would change the contract: E(t)<=epsilon near T_C requires $|t-T_C|\le\arcsin(\epsilon)/\kappa_C$ for 0<=epsilon<=1. We do not change the interval or the threshold to admit this candidate.

# 4. A scoped family limit: higher winding does not rescue the window

Consider the broader **independent-clock, single-work-qubit** family. The clock follows the chosen common reference independently, while B evolves under any time-independent Hermitian H_B. Require the complete work channel at T_C to equal ZX for every work/spectator input. Identity energy shifts are irrelevant to this channel.

**Theorem M12.3 (best independent-work uniform retention).** Every such H_B has form alpha·I+omega·Y with omega=(2m+1)·kappa_C for an integer m. Over the same interval, its worst joint error is at least 1/2. The least winding magnitude, |omega|=kappa_C, attains 1/2; all larger allowed magnitudes attain error one somewhere in the interval.

*Proof.* Endpoint channel equality means $e^{-iT_CH_B}=e^{i\phi}ZX$. A Hermitian generator commutes with its exponential; because ZX has distinct eigenvalues, H_B must commute with Y and hence has the displayed qubit form. Its two eigenphase difference must be an odd multiple of pi, so $2\omega T_C=(2m+1)\pi$, giving the stated frequencies. At time T_C+s its worst error is |sin(omega·s)|. The interval includes all s between -T_C/3 and T_C/3. For minimal frequency, the sine argument reaches pi/6 and the maximum is 1/2. For larger odd magnitudes, this range contains pi/2 and the maximum is one. $\square$

This is a lower bound on actual worst channel error in the stated family, not a Duhamel sufficient-bound failure. It does not rule out clock/work coupling, additional work/timer/mediator factors, different allowed encodings, dissipative models with fully owned environments, or other architectures. Those changes require new full-domain proofs and resource accounting. The result identifies which family cannot meet the present contract.

# 5. WBS 1.3, 3.1–3.2: bounded small-instance structure and costs

Group the clock pair terms on support C_0,C_1 and keep the three onsite terms separate. Their norms are kappa_C/sqrt(2), kappa_C/sqrt(2), sqrt(2)·kappa_C and kappa_C. Their sum is (2·sqrt(2)+1)·kappa_C, less than 4·kappa_C; the maximum is sqrt(2)·kappa_C, less than 3·kappa_C/2. Thus the declared small-instance h and J caps hold.

The full candidate spectrum is {-3·kappa_C, -kappa_C repeated three times, kappa_C repeated three times, 3·kappa_C}; its norm is 3·kappa_C. For supplied clock |00> and work |0>, the mean energy is zero and variance is 3·kappa_C^2. Compared with M11, the generator norm and that variance rise by a factor 3/2. Norm and variance do not measure preparation work or prove native coupling availability.

The exact Pauli structure is small enough to evaluate, advancing the WBS method without constructing a dense 380-qubit operator:

| Quantity | Exact toy value | Scope |
|---|---|---|
| Nonidentity strings L | 5 | Four clock strings and one work string |
| Coefficient norm Lambda | $(2\sqrt2+1)\kappa_C$ | Sum of absolute Pauli coefficients |
| Anticommute coefficient C | $\kappa_C^2$ | Two anticommuting clock pairs, each contributing kappa_C^2/2 |
| Literal parity basis action B | $15\pi/2$ | M10 compiler action summed over the five strings |
| Extra ancillary qubits | 0 | Three qubits include the encoded clock and work |

The anticommuting pairs are IXI with XZI and ZXI with XII. IIY commutes with all clock terms. If one chose an external digital approximation, M9/M10 would give digital norm error at most t^2·kappa_C^2/r and literal pulse action r·(15·pi/2)+t·(2·sqrt(2)+1)·kappa_C. That approximation is **not needed by the specified autonomous analog generator**, and an external pulse implementation would change its autonomy claim. The B calculation is a structural cost comparison, not a hidden driving schedule.

For an actual autonomous implementation with full generator defect bounded by delta, Duhamel adds at most t·delta to the ideal full-state error, plus separately admitted preparation defects. These sufficient debits cannot repair an ideal actual error already above 11/100. No gain, calibration, background or preparation capability has been measured.

# 6. WBS dispositions and next admitted attempt

| Package | Executed work | Remaining work |
|---|---|---|
| 5.2 | Changed pair-only generator has the exact joint endpoint | Candidate rejected for the selected window; full architecture remains open |
| 5.3 / 4.3 | Full-state error and independent-work family limit proved | Coupled/resource-extended autonomous retention design |
| 3.1 | Exact structured toy operator and valid-code action | Complete retained controller operator |
| 3.2 | Toy L, Lambda, C and B evaluated | Useful full-controller bounds and synthesis costs |
| 1.3 | Small finite N/h/J envelope specified and met | Full-controller numerical resource envelope remains open |

The next WBS 5.2 attempt must leave the failed independent single-qubit family: specify genuine clock/work or mediator coupling with all extra factors owned, audit pair support, then prove its interval error under finite resource limits before scaling. WBS 3.1–3.2 should separately continue on the structured retained source word. No complete-controller gate is marked closed by this small comparator.

Replay separates exact Gaussian-integer support/commutation and rational cost/cap inequalities from floating-point spectra, propagated entangled inputs, padding, return and winding witnesses. The written family theorem supplies the general conclusion; six sampled winding choices do not replace its proof. M11 source/receipt and attached governance/ledger are preserved. Constructor checking does not constitute independent review. Missing Gap2_FINAL_Finite_Genesis.png was unavailable and not used.
