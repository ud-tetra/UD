# Receipt thermal-gap frontier and corrected deadline v0.1

Development — no registry entry. Physical promotion 0; independent review OPEN.

## Declared inputs and clock

Retain the twelve-face Gibbs collision kernel, beta J=ln(3)/2, ground encoding, perfect downstream fanout, independent decision flags, and receipt state from UD_GIBBS_FLAG_RECEIPT_JOINT_STATE_v0.1. The explicit decomposed write takes 34 primitive slots. A 44-slot deadline leaves 10 storage rounds; 32 post-write rounds require 66 slots. Pure preparation, refresh/reset after readout, routing, controller reuse and gate-energy implementation remain separate costs. Shorter thermal exposure is not an intrinsic lifetime improvement.

## Exact error and gap gates

Let e_r=(1-TV(P_0 K^r,P_1 K^r))/2 and s_r=(0.01-e_r)/(1-2e_r). With p=0.01, q=0.0001, u=(1-(1-2q)^4)/2, m_0=3p^2-2p^3, the exact receipt-seed error is s(c)=u+(1-2u)[m_0+c(1-2m_0)]. Thus e_final=e_r+(1-2e_r)s(c), and

c_exact(r)=[s_r-u-(1-2u)m_0]/[(1-2u)(1-2m_0)].

The broader sufficient union/moment bound gives c_robust(r)=[s_r-4q-3p^2]/[3(1-2p)]. In this declared Gibbs family, c=(1+exp(beta Delta_c))^-1 is strictly decreasing. Therefore c<=c_star is equivalent to beta Delta_c>=ln[(1-c_star)/c_star] whenever 0<c_star<1/2. This conversion is a requirement on a candidate gap, not a source derivation of that gap.

| Total slots | Storage rounds | Ideal storage error | Exact c ceiling | Robust c ceiling | Exact minimum beta Delta_c | Robust minimum beta Delta_c |
|---:|---:|---:|---:|---:|---:|---:|
|44|10|6.162706438e-05|0.00925486951|0.003142720419|4.673307471|5.75951881|
|66|32|0.009238831644|7.7964838e-05|2.567950424e-05|9.45917466|10.5697917|

All acceptance comparisons and collision propagation use exact rational arithmetic; logarithms are numerical displays. The 32-round result matches the preserved parent error exactly. At 66 slots c=10^-5 passes and c=10^-4 fails. At 44 slots both pass because storage age differs.

## Non-identifiability certificate

Fix the carrier incidence operator, coarse-graining, face graph and the declared controlled-XOR receipt interaction. Give the control flags Hamiltonian H_F=Delta_c n_C+Delta_p sum n_Z+Delta_q sum n_D and energetically degenerate targets. Every flag-controlled XOR leaves its flag unchanged, so it commutes with H_F. Both c=10^-5 and c=10^-4 define valid product Gibbs flag states, both use the same carrier and receipt permutation, and both respect this ideal energy-conservation condition. Yet they lie on opposite sides of the 66-slot accuracy gate. The supplied incidence/coarse-graining plus this conservation condition therefore do not uniquely select receipt performance. A source-authored state-preparation or gap/coupling selection rule is necessary. This is a no-go for inference from those inputs, not a no-go for all possible future UD completions.

There is also a scale freedom: multiply every apparatus and memory energy by alpha>0 and temperature by alpha. All beta Delta and beta J, Gibbs probabilities and dimensionless accuracy results stay fixed, while energies and work in joules scale by alpha. Separately, changing the geometric area unit a0 changes I/(12a0) without changing these finite probabilities. Neither dimensional full-resource cost nor physical entropy per boundary area is identified by the dimensionless apparatus model. No G matching has been used.

## Eight incoming flags and resource interpretation

At c=10^-5, p=0.01, q=0.0001 the incoming flag inventory has beta <H_F>=0.141652820805, S_F/kB=0.172213848417, and ln Z_F=0.0305610276118; S_F/kB=beta <H_F>+ln Z_F. The Gibbs reference free energy is -kBT ln Z_F. Preparing that same equilibrium state from the same equilibrium reference has zero free-energy difference. Its mean energy and entropy are not an extra per-use work bill. After use, matched swaps with eight fresh Gibbs cells export correlations. Their source, routing and finite-bank restoration must be included to establish a full cycle.

The source handoff requires: a native apparatus Hilbert space and embedding; an actual Hamiltonian with typed gaps and local couplings; a bath state and temperature rule; gate durations in relation to storage collisions; a reset channel and finite reservoir/controller accounting; and a geometric physical scale. These are the next dependencies to solve before claiming a complete retained-information-per-area efficiency or horizon normalization.

## Provenance and verification

Inputs: exact parent storage error, boundary face labels, and the explicitly declared prior apparatus equations. verify.py recomputes the collision kernel and corrected-clock errors, verifies the parent equality, constructs the gap frontier and checks the Gibbs energy/entropy identity. This is constructor verification. Native selection, physical promotion and independent review remain OPEN. The original twelve releases are immutable; this result extends their timing and gap analysis without superseding their fixed-age results.
