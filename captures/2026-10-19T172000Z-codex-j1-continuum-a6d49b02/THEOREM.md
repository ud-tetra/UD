# Fixed J1 volume port: continuum convergence and damped frequency-band bounds v0.1

**DERIVED / EXACT CONDITIONAL. Development — no registry entry.** Constructor only; independent review absent; physical promotion0. Refs #218,#136; extends merged PR219–221 without changing their records. The fixed contract is for the declared scalar-wave benchmark. It does not derive a native UD action, material or physical correspondence.

## 1. Fixed continuum contract

Use the edge-a J1 domain with the user coordinates, scale X=x/a and tau=ct/a, then write x,y,z for dimensionless coordinates. Normalize measure dmu=dV/Vref with Vref=sqrt2/12 in these coordinates; mu(Omega)=2. The outer boundary has natural homogeneous Neumann conditions. The connected convex domain has diameter sqrt2. Work in the complex zero-mean space V={v in H1(Omega;C): integral v dmu=0}, norm ||v||V=||grad v||L2(mu). Removing constants fixes the Neumann gauge and is compatible with every conforming constant-containing finite element space.

FIXED source shape F(x,y,z)=10(x+y). The force functional and displacement readout are the same spatial integral:

    ell(v)=integral F v dmu;   y=ell(u),
    forcing density=F f(tau).

Exact integrals give integral F=0, ||F||L2²=20. Cauchy-Schwarz makes ell a bounded L2 functional. This spatial definition is fixed before any mesh evaluation; each mesh load is gi=integral F phi_i dmu with exact consistent volume quadrature. On the original5-node mesh g=p=(0,1,0,-1,0); that coordinate coincidence does not license replacing ell by point evaluation on finer meshes. Both distributed source and readout remain unchanged across refinement.

Declare homogeneous positive material damping gamma in[gamma0,gamma1], gamma0>0. For the time-domain field, u_tt+2 gamma u_t-Delta u=F f. Zero initial mean displacement/velocity stay zero. Material energy E=(||u_t||L2²+||grad u||L2²)/2 satisfies E'=f y'-2 gamma||u_t||L2². No numerical value of gamma is supplied by geometry or treated as a UD constant.

## 2. Continuum Poincare anchor, separate from the finite-mesh gap

Use the Payne-Weinberger inequality on bounded convex domains: ||v||L2 <= diam(Omega)/pi ||grad v||L2 for zero-mean v. Here diam²=2, so the continuum Neumann gap is at least pi²/2. Since pi>3, a conservative rational lower bound is

    lambda*=4,  ||v||L2 <= (1/2)||v||V,  ||ell||V' <= sqrt5.

Normalization of volume cancels in this inequality. This imports a stated external mathematical theorem, not an experimentally calibrated UD constant. The prior exact finite-mesh gap10 is NOT transferred to the continuum.

Primary source anchor: Esposito,Nitsch,Trombetti, 'Best constants in Poincare inequalities for convex domains', arXiv1110.2960, introduction equation1.4 (p=2 convex-domain bound). https://arxiv.org/abs/1110.2960 . Standard conforming Galerkin framework reference: Finite-element course, chapter5, Cea/interpolation and convergence: https://finite-element.github.io/L5_convergence.html . The frequency rotation, fixed-port identities and flux certificate below are derived here.

## 3. Uniform frequency-band well-posedness

For real omega, let z=-omega²+i2 gamma omega and define

    a_z(u,v)=integral [grad u dot grad(conj v)+z u conj v] dmu.

Solve a_z(u,v)=integral F conj(v)dmu for all v in V; define H(omega,gamma)=ell(u). This is the normalized displacement transfer at s=i omega. Dimensional angular frequency is(c/a)omega. This convention differs from a positive-real Laplace parameter and is not obtained by substituting i omega into a positive-matrix estimate.

For omega>0 choose phi with cos(phi)=2 gamma/sqrt(omega²+4 gamma²), sin(phi)=omega/sqrt(omega²+4 gamma²). Then Re(exp(-i phi)z)=0 exactly, hence

    Re[exp(-i phi)a_z(v,v)] = beta ||v||V²,
    beta=2 gamma/sqrt(omega²+4 gamma²)>0.

For omega<0 use the conjugate rotation, and for omega=0 use phi=0,beta=1. When omega²<4 the real part alone also yields beta_low=1-omega²/4; one may take the larger of beta and beta_low. Continuity holds with

    B(omega,gamma)=1+(omega²+2 gamma|omega|)/4.

The rotated Lax-Milgram argument yields existence, uniqueness and ||u||V<=sqrt5/beta. Every conforming Galerkin subspace inherits the SAME coercivity and continuity constants, without a mesh-frequency stability restriction at fixed positive damping. Constants deteriorate as gamma0 tends to0 or the band expands; no undamped resonance claim is made.

On a declared compact band |omega|<=Omega, gamma in[gamma0,gamma1], use

    beta_* = 2 gamma0/sqrt(Omega²+4 gamma0²),
    B_* = 1+(Omega²+2 gamma1 Omega)/4.

These are computable, mesh-independent bounds. For the illustrative audit band Omega=6,gamma0=1/10,gamma1=1: beta_*²=1/901 and B_*=13. These numbers are audit controls, not fitted or universal theory values.

## 4. Continuum convergence theorem and rate qualification

Let Vh be continuous P1 functions on a conforming tetrahedral mesh of the SAME exact polyhedron, intersected with V by exact mean subtraction. Assume a uniformly shape-regular family with maximum element diameter h->0 and exact integration of the stated forms/load. This is an explicit mesh-family condition: one finite midpoint-refinement check does not prove the condition for an infinite implementation sequence. Boundary approximation, quadrature error and algebraic solve error are excluded unless separately bounded.

For e=u-uh, Galerkin orthogonality gives the rotated Cea estimate

    ||e||V <= (B/beta) inf_vh ||u-vh||V.

Proof: rotate a_z(e,e), use a_z(e,uh-vh)=0 and continuity. Constants are unchanged on Vh. Smooth functions are dense in H1 on this Lipschitz polyhedron; Taylor interpolation of smooth functions on a shape-regular P1 family followed by mean subtraction approximates them in V. Thus the right-hand approximation infimum tends to0. This proves continuum convergence without assuming H2 regularity or claiming a computed rate constant.

The port is collocated and F is real. Using the COMPLEX SYMMETRIC BILINEAR form b_z(w,v)=integral(grad w dot grad v+z w v)dmu gives the additional exact identity

    H-Hh = b_z(e,e),
    |H-Hh| <= B ||e||V²
             <= (B³/beta²)[inf_vh ||u-vh||V]².

This is a bilinear identity, not |e|² positivity. At nonzero frequency the transfer error can be complex and need not be nonnegative. Its proof is ell(e)=b_z(u,e)=b_z(e,e)+b_z(uh,e); symmetry and Galerkin orthogonality annihilate the last term.

These convergence conclusions are UNIFORM on the compact band above. To see this, z->u_z is Lipschitz in V on the parameter set by the resolvent identity, with bound ||u_z-u_w||V <= |z-w| sqrt5/(4 beta_*²). Its solution image is compact. Finite epsilon nets plus density show E_h=sup_band inf_vh||u-vh||V ->0. Therefore sup_band|H-Hh| <= B_*³ E_h²/beta_*² ->0.

If, additionally, a certified approximation estimate E_h<=C_app h^r R is available, the displayed result gives the explicit rate |H-Hh|<=B_*³ C_app² R² h^(2r)/beta_*². For P1 H2 solutions r=1 is the usual conditional case. This turn does not compute a global H2 constant, C_app or an h-to-tolerance stopping rule. Uniform qualitative convergence is proved; a numerically calibrated convergence rate remains separate.

## 5. Guaranteed continuum residual bound and exact flux witness

For any conforming uh and any flux tau in H(div;Omega) with zero normal trace, define

    R=F-z uh+div tau,
    eta=||tau-grad uh||L2 + (1/2)||R||L2.

Integration by parts gives residual r(v)=integral[R conj v+(tau-grad uh) dot grad(conj v)]dmu; hence ||r||V'<=eta. The same coercivity and symmetric port identity prove

    ||u-uh||V <= eta/beta,
    |H-Hh| <= B eta²/beta².

This is a continuum error bound. It does not use a second finite mesh as the reference truth. Fluxes may be chosen by a verified H(div) reconstruction; eta is useful only to the extent that that reconstruction is accurate. A valid loose bound is not a passed precision target.

An explicit coarse-mesh witness is provided. Use coordinates (x,y,t) with t=sqrt2 z. A contravariant flux j corresponds to physical tau=(jx,jy,jt/sqrt2); div physical tau=div_(x,y,t)j, and physical flux norm has weights(1,1,1/2). The checker solves the RT1 polynomial constraints on the two original tetrahedra:

    j in P1^3 + (x,y,t)*homogeneous_P1,
    div j=-(x+y),
    continuous normal trace across the shared face,
    zero exterior normal trace.

RT1 normal traces are affine, so testing them at the three face vertices proves the whole-face constraint; divergences are affine, so four cell-vertex tests prove the cell identity. Exact rational integration and minimization over the two remaining coefficient freedoms give

    ||tau0||L2² = 43/3360,
    integral tau0 dot grad(x+y) dmu = 1/5,
    ||20 tau0-grad(x+y)||L2² = 47/42.

All coefficients are included in RESULTS.json with the basis order and coordinate convention. For the coarse solution uh=c(x+y), c=10/(20+z), choose tau=20 c tau0. Then R=0 identically and

    eta² = (47/42)|c|²
          = (4700/42)/[(20-omega²)²+4 gamma² omega²].

Together with Section3 this gives an explicit guaranteed frequency-dependent continuum-error envelope for that coarse model. At omega=0, beta=B=1, so |H(0)-1|<=47/168. The static Galerkin energy identity additionally gives

    1 <= H(0) <= 215/168.

This is a coarse continuum bracket, not a claim that its width is small or optimal. Near a coarse resonance the flux envelope can be very loose; convergence and band stability do not certify coarse-mesh spectral accuracy. Reconstructing the flux on finer meshes can produce sharper certificates but has not been computed here.

## 6. Uniform gain bound and passive collocated port damping

By the self-adjoint nonnegative Neumann Laplacian on zero-mean L2, lambda>=4. For gamma>=1/10 and t=omega²,

    |lambda-omega²+i2 gamma omega|²
      >= (lambda-t)²+t/25
      = (t-lambda+1/50)²+(lambda-4)/25+399/2500
      >=399/2500.

Consequently |H|<=||F||L2²/(sqrt399/50)=1000/sqrt399. This conservative bound holds throughout the illustrative band (indeed all real omega at that damping lower bound), and every conforming mesh inherits it by the same Poincare/Rayleigh argument. It is a finite upper bound, not a measured amplification or resonance-location certificate.

For an additional passive damper zeta>=0 at this SAME distributed port, the exact continuum weak feedback gives H_zeta=H/(1+i omega zeta H). Energy balance implies -omega Im H>=0, so |1+i omega zeta H|>=1. Therefore |H_zeta|<=|H|, and for the exact Galerkin transfer Hh,

    |H_zeta-Hh_zeta| <= |H-Hh|.

The uniform convergence and residual-output bound thus transfer to any fixed nonnegative collocated port damper. This statement is not for noncollocated forcing/readout, active damping, different spatial sources or an undamped limit.

## 7. Verification and open gates

85 exact constructor assertions PASS: RT1 face/divergence constraints, minimum-norm stationarity, exact volume moments and flux norms, damping rotation cancellation, rational frequency controls, completed-square gain identity and static error coefficient. Source Poincare and standard Galerkin density results are external mathematical anchors; the checker does not pretend to prove those general theorems by sampling. The compact-band convergence and passivity proofs above are analytic arguments. Constructor checking is not independent review.

Run `python3 verify_continuum.py` and compare parsed JSON with RESULTS.json. New standard-library Fraction code only, no archived script executed. Open gates: independent review; a verified infinite mesh-family implementation and sharper fine-mesh flux certificates; a numerical h-to-tolerance rule or precise resonance intervals; native UD action/state/units bridge; actual hardware or horn validation. Physical promotion0.
