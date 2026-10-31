# Native 3+1 spectral-transport derivation v0.1 -- scoped mathematical capture

DATE: 2026-10-31
STATUS: EXACT_FINITE_KERNEL; CANDIDATE_ACTION_AND_FACE_COST; PHYSICAL_BRIDGE_OPEN.
PHYSICAL PROMOTION: 0. Independent non-constructor scientific review PENDING.

## Exact source-free geometry
Let T be filled oriented tetrahedron, with C1(T,R) dimension 6, B1:C1->C0, B2:C2->C1 and B3:C3->C2. Boundaries obey B1 B2=B2 B3=0. Define co-closed 1-cycle sector Z=ker B1 of dimension 3, and projector P=I6-B1^T B1/4. Then K0=B2 B2^T=4P, giving spec(K0) on C1 = {0^3,4^3}. This is not a physical photon carrier; three co-closed modes differ from two continuum photon polarizations.

The signed S4 edge representation on Z has character (3,-1,0,-1,1) on conjugacy class sizes (1,6,8,3,6). Its character-square average is 1, so the complex representation is irreducible. A fully S4-equivariant linear response on this sector must be scalar: NO-GO for mode splitting with those exact premises.

## Source-bound holonomy and NEW constitutive candidate
The earlier v0.39 Q140 source defines delta_U=1-ReTr U/d = ||I-U||^2/(2d) for unitary face holonomy, a mathematical curvature/transport cost. For U1, delta(phi)=1-cos(phi). The map from delta to a spectral stiffness has NOT been derived. Here, as a NEW and separately labeled candidate only, set w_f=1+delta_f and K=B2 diag(w_f) B2^T. No physical target numbers were used to choose this declaration.

One-face stiffness change (1+epsilon,1,1,1) gives spectrum {0^3,4^2,4+3epsilon}. It is only a source-control. For an honest closed-tetrahedron U1 edge-link phase alpha on edge 01, B2^T alpha=(phi,phi,0,0), obeying B3^T B2^T alpha=0. A single nonzero face holonomy alone fails the discrete Bianchi rule.

Consequently the two face weights 1+delta,1+delta yield EXACT transverse squared-frequency spectrum (4,4+2delta,4+4delta), delta=1-cos(phi)>=0.
The squared-frequency increment ratio is EXACTLY 2:1 for delta>0.
Small-phase RELATIVE FREQUENCY shifts are (0,phi^2/8,phi^2/4)+O(phi^4).
Averaging over all six edge-source placements restores S4 and gives K_avg=(1+delta/2)K0 with NO splitting.
All these are exact conditional finite-matrix claims; the phase source evolution and stiffness selection are OPEN.

## Exact 3+1 slab and event action
The staircase triangulation of Delta3 x I has four oriented pentachora:
[0,4,5,6,7]-[0,1,5,6,7]+[0,1,2,6,7]-[0,1,2,3,7].
Entire slab f-vector (8,22,28,17,4), 3 canceled interior tetrahedral faces, 14 exterior tetrahedral faces, boundary squared=0. Topology alone does not select a future time direction or scale factor.

Define an explicitly chosen action on q_n in Z with event step h>0:
S=sum_n {||q_(n+1)-q_n||^2/(2h) -(h/2) q_n^T K_n q_n}.
The Euler equation is q_(n+1)-2q_n+q_(n-1)+h^2 K_n q_n=0, given two initial states and boundary sector. For time-independent K, the exact discrete event energy
E_(n+1/2)=||q_(n+1)-q_n||^2/(2h^2)+q_n^T K q_(n+1)/2
is conserved. For varying K_n, exact source/work receipt:
E_(n+1/2)-E_(n-1/2) = q_(n-1)^T(K_n-K_(n-1))q_n/2.
This source-work term cannot be omitted as free spectral dressing. Neither h nor E is SI time or physical energy.

## External cosmological clock conditional, NOT a native redshift derivation
Supply an external positive scale sequence a_n and conformal proper-clock contract d tau=a_n h. For a fixed modal conformal phase theta_j, define omega_local(j,n)=theta_j/(h a_n). Then 1+z_(m->n)=a_n/a_m, achromatically, and the product across slabs telescopes exactly. This is imported FLRW/Maxwell kinematics. The same simplicial topology permits a_n constant (z=0) and changing (z nonzero), hence NO-GO for redshift selection from incidence alone. Constant face spectral splitting alone does not generate chromatic propagation redshift. Actual photon transport requires larger spatial complex, two physical polarizations, Lorentzian principal symbol, calibrated clock and detector and independent experiments.

## Evidence and release
Full local package: UD_NATIVE_3PLUS1_SPECTRAL_TRANSPORT_v0.1.zip
SHA256 b5b1c02893c50d68be3b4e6d7a0615f69ccecc48c4bbb8ab26cf47302d3a919e
Contains complete 5-page A4 PDF, 2,000-word source-linked technical note, two separate exact SymPy checkers, 18-entry claim/dependency ledger, deterministic receipt and SHA256 byte manifest.
This GitHub capture mirrors a smaller text summary and a minimal exact checker, NOT the PDF or full ZIP. All full local files available as user download. No main merge, physical claim, public site update, external peer review or measurement comparison.

Next gate: derive native phase history and w(delta) action from packet source without target fitting; derive 3+1 Lorentzian metric and proper clock from source/flux accounting; extend beyond isolated K4 to photon-compatible propagating/glued carriers; preregister chromatic and observer null tests.
