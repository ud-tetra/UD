# J1 passive damping and further-refinement audit v0.1

**DERIVED / EXACT CONDITIONAL. Development — no registry entry.** Constructor checks only; independent review absent; physical promotion0. Refs #218,#136 and pending PR219/220. Existing files/results are unchanged. This extends the explicitly declared P1 scalar-wave benchmark, not a native UD source law.

## 1. Result and scope receipt

The prior J1 port law H(s)=20/(s²+20) holds on the two diagonal meshes and the square-center mesh investigated in PR220. It is NOT invariant under every conforming refinement. A concrete14-vertex,16-tetrahedron midpoint refinement changes the driven response. That does not retract the prior three-mesh theorem; any extrapolation to arbitrary refinement or the continuum is now explicitly rejected by exact counterexample. The project next gate must be convergence/control of a declared distributed port, not repetition of the coarse eigenvalue.

## 2. Mesh and port contract

Keep the same J1 domain, a=1, tau=ct/a, volume normalization Vref=sqrt2/12 and exact P1 stiffness K and consistent mass M as in PR220. The coarse two tetrahedra share(apex0,V1,V3). Bisect all nine edges, making14 unique vertices. Split each parent into four corner tetrahedra and split its internal midpoint octahedron into four tetrahedra along the local(01)-(23) opposite-midpoint diagonal. Shared triangular faces have the identical four-triangle subdivision, so this is conforming. Each child has volume Vparent/8, verified by exact edge-Gram determinants; there are24 exterior triangles. RESULTS.json lists the coordinates/cells, prolongation P and all rational matrices.

P evaluates each coarse affine basis at fine vertices. The exact identities P^T Kf P=Kc and P^T Mf P=Mc verify nested energy/mass preservation. This is an actual refinement of the original domain, not a shape change or independently normalized operator.

Two distinct force/readout functionals agree on the coarse mesh:

* Retained point port: coarse p=(0,1,0,-1,0), fine gp=(p,0,...,0). Force gp f, readout gp^T q. This is the same difference of two nodal point values. Its point-evaluation interpretation does not supply a bounded three-dimensional H1 continuum load/readout or a convergence theorem. For example, a fixed-height bump supported within radius epsilon of a vertex has point value1 while its three-dimensional gradient energy is O(epsilon) and mass is O(epsilon³); its H1 norm tends to0. This prevents bounding that point functional by the H1 energy norm.
* Fixed volume port: define u0=x+y on J1 and the normalized functional ell(u)=10 integral(u0*u)dV/Vref. Its fine load is gv=10 Mf Pp; on the coarse mesh10 Mc p=p. Force gv f and readout gv^T q retain the same volume functional under refinement. This is a distinct spatial source from a point port, despite equality on the coarse space.

Both satisfy P^T gf=p. Neither is silently substituted for the other. The fixed volume functional is bounded in L2 by Cauchy-Schwarz; exact integral10² integral(u0²)/Vref=20 fixes its squared dual L2 norm. This boundedness makes convergence a meaningful next problem; it does not prove convergence here.

## 3. Passive damping theorem

Declare proportional material damping C0=2 gamma M, gamma>=0. Then

    M q'' + C0 q' + K q = g f,
    E=(q'^T M q'+q^T K q)/2,
    E'= f y' - 2 gamma q'^T M q', y=g^T q.

Adding a passive damper at the same port, C=C0+zeta g g^T, zeta>=0, subtracts zeta(y')². Energy is nonincreasing without forcing. gamma>0 damps every velocity mode; a constant displacement remains a Neumann equilibrium and is not claimed to decay to a unique origin. For gamma=0, one port damper need not damp unobserved modes. Geometry supplies neither gamma nor zeta.

For the prior coarse J1 port, exact identities Mp=p/10 and Kp=2p give

    H_gamma(s)=20/[s²+2 gamma s+20],
    H_gamma,zeta(s)=20/[s²+(2 gamma+20 zeta)s+20].

For regular Kminus replace20 in the stiffness term by40. Hence the geometric distinction remains within those coarse models under the same declared damping. On any finite mesh, for the identical collocated load/readout and where the inverses exist,

    H_zeta(s)=H_0(s)/[1+zeta s H_0(s)].

This follows directly by solving the rank-one feedback equation (or multiplying the inverse identity); it does not assume coarse modal invariance. With positive-real s=sigma>0, every matrix is positive definite and the displayed denominator is positive. These values are Laplace-domain tests, not measured sinusoidal frequency responses or finite resonant gains.

## 4. Exact refinement counterexample

Set gamma=1/10, sigma=1 and zeta=0. These are declared audit controls, not fitted theory constants. Coarse H=50/53 for either port. Exact refined values are:

| Fine port | Hfine | Hfine-Hcoarse |
|---|---|---|
| Retained point | 204800/117863 | 4961250/6246739 |
| Fixed volume | 113550/117863 | 125000/6246739 |

The fixed-volume difference is about0.02001044, while the retained-point difference is about0.79421439. These are exact finite-mesh differences at a positive real Laplace parameter; they are not estimates of continuum error. The functionals' equal coarse coordinates concealed markedly different fine responses.

The prolonged affine field Pp also fails Kf Pp=20 Mf Pp. No broad claim that the coarse two-channel modal subspace remains invariant under all refinements survives this counterexample. The earlier three-mesh identity remains true on its stated scope.

## 5. Residual error theorem, uniform in positive real parameter

Write alpha=sigma²+2 gamma sigma>0 and A=K+alpha M. For either source above, let qc=Ac^(-1)p and r=gf-Af P qc. Exact nested identities and P^T gf=p give P^T r=0. If qf=Af^(-1)gf, then Galerkin orthogonality yields

    Hf-Hc = (qf-Pqc)^T Af(qf-Pqc)
          = r^T Af^(-1)r >=0.

This is a same-functional, same-domain Galerkin comparison. It is not an arbitrary comparison of meshes with unrelated loads. Since Af>=alpha Mf,

    0 <= Hf-Hc <= (r^T Mf^(-1)r)/alpha.

For this mesh we also certify a lower squared-frequency gap10 on the mass-orthogonal complement of constants. Let w=Mf*1 and choose basis columns ej-(wj/w0)e0. The checker verifies every exact positive LDL pivot of U^T(Kf-10 Mf)U. Thus Kf>=10 Mf on that complement. Here1^T r=0, so its Mf-Riesz representative lies in that complement, giving the stronger bound

    0 <= Hf-Hc <= (r^T Mf^(-1)r)/(alpha+10).

This bound holds for all sigma>0,gamma>=0 in this fixed mesh/port contract. The exact gap certificate is not a claim that the gap equals10. For the fixed-volume example in Section4 the stronger upper bound is31250/137641, versus actual difference125000/6246739. It is conservative, not a tight forecast. The coarser mass-only upper bound is125000/58989.

No imaginary-axis uniform bound follows by replacing sigma with i omega: alpha positivity is essential. Resonance/near-pole certification requires damping-dependent resolvent bounds on a separately declared frequency band.

## 6. Verification, provenance and next gate

193 exact constructor assertions PASS: child Gram volumes, conforming face incidence, nested forms, source pullbacks, affine prolongation, noninvariance, positive mass/stiffness pivots, certified gap, residual identities/bounds, and passive rank-one damping identities for18 port/parameter fixtures. Checks at gamma in{0,1/10,1},sigma in{1/2,1,2},zeta in{0,1/5} are witnesses supporting the written algebraic theorems, not a substitute for their general proofs.

Replay `python3 verify_refinement.py`; standard-library rational arithmetic only. No imported/archived programs executed. New code reconstructs the source geometry and functional explicitly. CONTRACT.json hash-binds the prior report/checker and attached ledger/governance provenance. The CRL2 amendment is still a proposal; no registry/CRL promotion is asserted.

Next: fix the bounded distributed source/readout as the continuum-facing contract; derive mesh-convergence and frequency-band bounds with declared positive damping; then derive or reject a mapping to native UD chain/source variables. Shape selection, arbitrary-refinement invariance, native action selection, physical horn transmission and experimental validation remain OPEN. Physical promotion0.
