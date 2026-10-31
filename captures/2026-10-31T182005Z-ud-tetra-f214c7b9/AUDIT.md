# UD historical Wilson face-response audit v0.1
Date: 2026-10-31.
Status: EXACT_CONDITIONAL_HESSIAN_AND_SOURCE_FREE_NO_GO; CURRENT_ACTION_NOT_PROMOTED.
PHYSICAL PROMOTION: 0. Non-constructor human review: PENDING.

## Source and conflict resolution
March 12, 2026 Distinction Dynamics manuscript §4 Eq.(7) writes a loop-curvature penalty Tr(I-U_C), plus separate burden and vertex-orientation penalties. To obtain a REAL U(1) potential, we explicitly specialize to V_W(alpha)=kappa*sum_f[1-cos(Phi_f)], Phi=B2^T alpha and kappa>0. This is a *historical conditional action branch*, not an independently derived 2026 current native law.
Ledger v0.39 Q140 fixes delta_U=1-ReTr(U)/d but does not fix the face stiffness. Its G05 loop scalar was source-blocked. The recovered public v0.85 JSON has G05 RETIRED from the mainline as universal scalar and O09 as the active lifted loop-history-to-Hodge action map. No verified identification O09=V_W or source of the edge-phase kinetic term exists. v0.85 Q140 retains the normalized mismatch scalar. There is NO authorization to reuse G05 as a global physical coupling.

## Exact type-separated theorem
On T=Delta3 with signed incidence B1:C1->C0, B2:C2->C1, B3:C3->C2, B1B2=B2B3=0. The real Abelian link phase alpha is a separate typed variable from any packet amplitude q previously placed in C1. Let Phi=B2^T alpha, and adopt the stated historical real Wilson potential V_W=kappa sum_f(1-cos Phi_f).
Then
    d_alpha V_W=kappa B2 sin Phi
    H_W=d^2_alpha V_W=kappa B2 diag(cos Phi_f) B2^T.
Thus w_f^H/kappa=cos Phi_f=1-delta_U(U_f), NOT 1+delta_U(U_f). This sign is an exact conditional source-stratum result, and not the physical sign in an unknown current UD action.

## Edge-current and spectral readout
One edge phase alpha=(phi,0,0,0,0,0) yields Phi=(phi,phi,0,0), B3^T Phi=0, so one-face-only flux is NOT edge-link admissible.
Its Hessian eigenvalues on full C1 are kappa*{0,0,0,4,4-2delta,4-4delta}, delta=1-cos phi.
With separately supplied uniform positive kinetic pairing the small-phase relative modal frequency changes are (0,-phi^2/8,-phi^2/4)+O(phi^4). The previous unselected positive-stiffness branch had the opposite sign.
The full edge-source current required to HOLD a nonzero background is J=kappa sin(phi)*(2,-1,-1,1,1,0), satisfying B1 J=0. Its quasistatic work from flat is 2kappa*(1-cos phi). J is *required*, NOT sourced from burden.
At phi=pi/3 the transverse Hessian is positive with eigenvalues {2,3,4}kappa; at phi=pi/2 a transverse eigenvalue vanishes; at phi=2pi/3 it is negative.

## Scoped NO-GO for persistent nonzero response
Assume no external/matter source, the isolated filled tetrahedron and principal face phases each in (-pi/2,pi/2). Stationarity B2 sin Phi=0 and ker B2=im B3 imply sin Phi=t B3. Sine is injective; Phi=(arcsin t) B3. Bianchi B3^T Phi=0 modulo 2pi, and |B3^T Phi|<2pi, so 4 arcsin t=0, t=0, Phi=0. Nonzero stationary stable Wilson curvature therefore requires a source, changed branch or other gate. Nonzero transients or nonconvex sectors are outside this statement.

## NO-GO for inferring constitutive law from 2:1
For ANY two-equal-face weight w, K(w)=B2 diag(w,w,1,1)B2^T has active eigenvalues {4,2+2w,4w}. The signed squared-eigenvalue shift ratio (4w-4)/[(2+2w)-4]=2 for w!=1. The earlier w=1+delta and this Wilson-Hessian w=1-delta BOTH give 2, with opposite physical sign. It is a support-pattern invariant, not a native stiffness or experiment-facing prediction.

## Missing source dependencies and terminal ruling
Original separate burden and vertex-orientation penalties contain no alpha source on a declared independent product space. O09 does not supply a link-phase response action or coupling to source current; kappa physical units, kinetic pairing, time, Lorentzian causal principal symbol, actual photon polarizations and instrument readout remain OPEN.
Do not target-fit a phi or kappa to alpha_EM, n_s, leptons, redshift or laboratory residuals. Physical promotion 0. Next step: derive typed J(rho,theta,U,history) with conservation and donor/work receipts from the current accepted source/action map, or freeze the Wilson branch as a historical conditional comparison.

## Verified files and release boundary
Locally generated full package UD_FACE_RESPONSE_ACTION_AUDIT_v0.1.zip SHA256 adea23b803a45e2ce1192fb931e8037a4f0c7d5d6792fa526bb767ea46f55265 includes complete 2-page A4 PDF, full 12K technical note, generated-incidence SymPy and independent hardcoded/finite-difference scripts, receipts, claim ledger and SHA-256 manifest. Local scripted checks passed.
The present GitHub branch mirrors only THIS TEXT CAPTURE, compact exact replay, source lineage and manifest/event; full PDF/ZIP are NOT committed. No prior scientific artifact modified, no main branch merged, no website edit, and no independent physical validation.

## Primary source locators
- Manuscript: distinction_dynamics_manuscript.pdf SHA256 909ac4bfbb07ab815d15463648278877a7452989797589bf630564a0afa9f1ef, §4 Eq.(7).
- Ledger v0.39 SHA256 1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63, Q140/G05/Q153–154.
- Recovered v0.85 source: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json entries G05/O09/Q140.
- Prior conditional candidate: https://github.com/ud-tetra/UD/pull/470
- External Wilson-action comparison: https://pmc.ncbi.nlm.nih.gov/articles/PMC12026112/
