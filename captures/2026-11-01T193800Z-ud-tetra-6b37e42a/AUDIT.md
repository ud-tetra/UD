# UD Q81 Context Source and Odd-Observer Comparison — review capture v0.1

Scientific date 2026-11-01; PHYSICAL PROMOTION=0.
Status: EXACT_SCOPED_FINITE_MATH / CONDITIONAL_Q63_CONTEXT_MODEL / NO_GO_UNIQUE_ENVIRONMENT_SOURCE / OBSERVER_SELECTION_OPEN.
Independent non-constructor review PENDING. No target values or laboratory data fitted.

## Source identities
- Public UD Paper I §§4.3/6.3: graded skew Hodge A=B^T-B, filled K4 and named 2<->3 glued carrier spectra. https://unified-dynamics-public.ben-w-mayes.chatgpt.site/mathematics/
- Recovered typed ledger filename v0.85, inherited scientific_revision=v0.43: O09 (modal phase increments, positive frequencies only); Q63 (Tr sigma_E V_beta^dagger V_alpha); Q64 (magnitude); Q81 (relative context-phase Arg), Q82-84 (signed seam orientation, half phase and cosine); Q165/Q166/Q169/Q170 (quadratic stocks, signed currents, skew graded Hodge). https://unified-dynamics-public.ben-w-mayes.chatgpt.site/evidence/ledger-recovery/
- G05 universal scalar remains RETIRED. Current O09 does not source a local environment coupling, context preparation or physical detector.

## Workload 1 — exact candidate realization and source no-go
Introduce explicitly NEW branch carrier H_S=C2 and environment H_E=C2, sigma_E=diag(p,1-p), Z=diag(1,-1), G_SE(s)=g(s) |alpha><alpha| tensor Z. Set Gamma(s)=integral g(s)ds and V_alpha=exp(-i Gamma Z), V_beta=I. Then the Q63-compatible overlap is exactly
    K_ctx=cos Gamma - i(2p-1) sin Gamma.
Its modulus squared is cos^2 Gamma+(2p-1)^2 sin^2 Gamma.

A Q81 implementation by u(P_alpha)=K_ctx/abs(K_ctx), u(P_beta)=1 is an ADDITIONAL phasor normalization, defined only for K_ctx!=0. Q84 signed phase cosine is cos Gamma / abs(K_ctx), generally NOT raw Re K_ctx=cos Gamma. At Gamma=pi/3, p=1 gives phase -pi/3 and magnitude1, while p=1/2 gives phase0 and magnitude1/2, for the same unchanged K4 source.
With equal branch populations, the commuting interaction yields internal switch-work
    W_switch=(2p-1)/2 * [g(T)-g(0)].
A pulse g(s)=2Gamma0 sin(pi*s)^2 over 0<=s<=1 has nonzero Gamma0 but zero endpoint switch-work. This is NOT a physical free detector: preparation, control and clock resources remain OPEN. It proves that net switching work and O09-only data do not uniquely determine context phase or coupling.

The exact marked modal intertwiner for any positive L1 eigenpair lambda,r=P_lambda x !=0 on the graded source is
    T_r(X)=(<r,X>+i<Ar/sqrt(lambda),X>)/||r||^2,
    T_r(A X)=i sqrt(lambda) T_r(X);
on the prepared orbit it reads exp(i sqrt(lambda) s).
It is a mathematical real-to-complex isometry on that marked plane; no accepted source identifies it with Q81's context Hilbert space. Each eigenspace admits multiple marked references.

## Workload 2 — exact identical-fixture per-carrier observer comparison
On each carrier choose sorted oriented edge input x=(1,2,...,E), unit graded metric, and use same Hodge flow. Let L1=B1^T B1+B2 B2^T and P_lambda its rational orthogonal projectors.
- Source Q165 edge stock S_edge=sum q_lambda cos^2(sqrt(lambda)s) (no cross beats in this whole-edge region).
- Prepared mode references read each sqrt(lambda) as a first harmonic, but each requires a retained marked reference.
- Candidate S4-compatible odd cubic observer C3=sum_v[(B1 x_edge)_v]^3 yields observer harmonics and combination frequencies; it is not source selected.

EXACT fixtures:
K4: edge L1 eigenvalues 4x6; q4=91; C3=2016 cos(2s)^3 =1512 cos2s+504 cos6s.
K_minus tets 0123,0124: eigenvalues 3x3,5x6; q3=3/2,q5=567/2; C3=(999/4)cos(sqrt3*s)^2 cos(sqrt5*s)+(23001/4)cos(sqrt5*s)^3. Observer-generated lines at 2sqrt3 +/- sqrt5 are not source Hodge eigenfrequencies.
K_plus tets 0134,0234,1234: eigenvalues 2x1,5x9; q2=16/3,q5=1139/3; C3=20430 cos(sqrt5*s)^3. EXACT: B1 P2=0, so cubic is COMPLETELY BLIND to the sqrt2 source mode, while Q165 stock and prepared reference detect it.
GENERAL NO-GO: for any z in ker B1, and any function F, F(B1(x+z))=F(B1 x). Thus ANY divergence-only observable is blind to all edge-cycle degrees of freedom.

## Tests, evidence and release
- exact_compare.py SymPy: three graded chain incidences, edge Laplacians, rational projectors, T_r intertwiner, exact observable coefficients, Q63 controlled context and pulse-work tests PASS.
- independent_numeric.py SciPy: independently rebuilt graded incidence; 35 expm samples on each complex; all modal stock, cubic, phase-reference, norm and controlled-unitary comparisons PASS. Max unnormalized observer error 2.9468e-10.
- Additional GITHUB_MINIMAL_REPLAY.py passes exact K-plus dark mode and context kernel.
- Full local user release UD_Q81_CONTEXT_SOURCE_AND_ODD_OBSERVER_AUDIT_v0.1.zip SHA256 31d13d42e2ebd3b9082b2f6d3194910088e6a2a2609df4772816bb00015747e6, 16 members, 15 SHA256-hashed source files plus manifest; local two-page A4 proof visually inspected.
- This GitHub draft mirrors a compact text summary, minimal replay and a scoped claim ledger. Full PDF, full scripts, receipts and ZIP are LOCAL ONLY. No main merge, public site change, independent scientific review or physical promotion.

NEXT GATE: derive packet-to-environment V_alpha, sigma_E and retained Hodge reference from a CURRENT native interaction/source law with units, control-work/preparation receipts and held-out measurement contract. If unavailable, maintain this Q81/O09 physical interface as OPEN_GATED.