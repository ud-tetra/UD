# UD graphite registry-to-mode hypothesis test v0.1

2026-10-21. Development — no registry entry. Constructor verification only; non-constructor review pending. Physical promotion 0.

## Result and disposition

PASS_SCOPED exact rigid-registry calculation; OPEN material-mode coupling. Geometry alone reproduces the conventional reciprocal-lattice filtering account. It does not establish an additional UD protected dissipative sector. The stronger claim that the measured angles have such protection is held pending independent physical mode and damping inputs.

## Sources and scope

Chen et al., Physical Review Letters 137, 166201 (14 October 2026), DOI https://doi.org/10.1103/ly48-b4l2, abstract: small sharp friction peaks at 21.8 and 38.2 degrees have negligible load dependence; other higher-order commensurate configurations have no detectable signal. Full paywalled article and supplement not acquired. No friction dataset inspected.

Lebedeva et al., arXiv:2511.01338v1, 3 November 2025, https://arxiv.org/html/2511.01338v1, section 2 equations (1)-(2): commensurate geometry and reciprocal filtering. This source already accounts for small corrugation in commensurate patterns; our geometric calculation is an independent arithmetic check of this conventional mechanism, not a new UD derivation of graphite.

UD source: docs/UD_Protected_Retention_Robustness_and_Port_Condition_v0.1.md section 2, repository snapshot cba43cce947438074e6125d242e9a3f957705c85. Its PF=0 theorem concerns a declared finite chain carrier and reciprocal burden port; it supplies a method analogy, not a material identification. Refreshed repository base recorded in the manifest. Supplied ledger v0.39 is historical context, not a current coefficient source. Supplied CRL-2 amendment remains a proposal. No 7/768 or other UD numerical ratio is used. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused.

## 1. Rigid periodic registry calculation — EXACT under stated assumptions

Assume identical infinite rigid honeycomb layers, no strain or defects, periodic bulk averaging, and a translationally invariant interlayer interaction with a convergent Fourier expansion. Let A have columns (1,0), (1/2,sqrt(3)/2), and B=A^(-T); the omitted 2pi/a factor sets physical reciprocal units. For each common reciprocal vector G in Lambda* intersect R_theta Lambda*,

U_bulk(x,z)=U0(z)+sum_(G != 0, common) C_G(z) exp(i G dot x),
F_parallel=-grad_x U_bulk.

Coefficients include both honeycomb basis structure factors and the physical interaction transform; geometry does not determine them. For basis offset (a1+a2)/3 the factor is 1+exp[2pi i(h+k)/3], with magnitude 1 or 2, hence no additional zero from the two-atom basis alone. G=0 gives no lateral corrugation but can retain normal adhesion. This is the conventional separation between mean adhesion and lateral registry forces.

With N=m^2+mn+n^2, c=(m^2+4mn+n^2)/(2N), t=(m^2-n^2)/(2N), the exact reciprocal rotation is

T=B^(-1) R_theta^T B = [[c-t,2t],[-2t,c+t]].

A reciprocal integer pair (h,k) survives iff T(h,k) is integral. Its normalized squared length is Q=h^2+k^2-hk. Exact enumeration gives:

| Interface | cos(theta) | Nc, minimal cell | min Q | min |G|/|b| |
|---|---:|---:|---:|---:|
| aligned | 1 | 1 | 1 | 1 |
| (2,1) | 13/14 | 7 | 7 | sqrt(7) |
| (3,1) | 11/13 | 13 | 13 | sqrt(13) |

Angles are approximately 0,21.7867892983,32.2042275040 degrees; 38.2132107017 is the hexagonal complement of (2,1). Aligned uses the primitive cell; the unreduced (1,1) formula is not assigned Nc=3. The integer search covers [-12,12]^2. Since Q >= (h^2+k^2)/2, every omitted pair has Q >=169/2, exceeding 13. Thus the reported minima are globally proved, not guessed from a finite search. Six shortest vectors for each case appear in RESULTS.json.

Higher common reciprocal wave numbers can have much weaker interaction coefficients. Geometry supplies the selection rule; decay rates, pressure dependence and friction values need material inputs. Neither exact zero friction nor load independence follows from the shell table. The numerical value 7 is a crystallographic index, not a UD capacity numerator.

## 2. Registry-to-mode map — DERIVED conditional form, physical entries OPEN

Let x be imposed displacement along a fixed unit direction e (metres), and q in R^d internal Cartesian displacement coordinates (metres), excluding or constraining rigid zero modes. Let U_theta(x,q,z) be independently specified energy (joules), with z set by a declared normal-load equilibrium protocol. On a smooth stable branch qeq(x), U_q=0 and K=U_qq is positive definite. Define g_theta=U_qx, a d-component vector with units N/m. Differentiation gives qeq'=-K^(-1)g_theta, dimensionless. Its modal components are the desired registry-to-mode coupling; they are not obtained from a scalar bulk PES alone.

M qddot + Gamma qdot + U_q=0, with M positive definite (kg), Gamma positive semidefinite (kg/s), is an explicitly added passive mechanical law. For quasistatic constant-speed sliding v, a smooth periodic stable branch and an established steady response,

Pheat=v^2 < g^T K^(-1) Gamma K^(-1) g > + o(v^2),
Fdiss=v zeta + o(v), zeta=<||Gamma^(1/2) K^(-1)g||^2>.

Average over one physical sliding period; zeta has units kg/s. Include K(x), Gamma(x), and g(x) pointwise if variable. This limit excludes stick-slip branch switching, thermal activated events, uncontrolled rigid modes and finite-speed resonances. The prior response omitted these regularity and steady-response premises; they are explicit here. Semidefinite damping requires initial/steady-state conditions eliminating persistent undamped transients; positive stiffness alone is insufficient.

For a fixed linearized harmonic drive, D(omega)=K-omega^2 M+i omega Gamma. When D is invertible, dissipated power is omega^2/2 times ||Gamma^(1/2) D^(-1) fhat||^2. A static kernel condition need not persist at finite frequency if M,K mix damped and undamped sectors. A robust all-frequency protected sector needs a suitable common invariant subspace plus absent bath coupling; no such graphite subspace is established here.

## 3. Conditional obstruction and counterexamples

Exact quasistatic protection requires Gamma^(1/2)K^(-1)g=0 all along the branch. If Gamma is positive definite, it requires g=0: there is no nontrivial exact dissipative nullspace. Small damping eigenvalues can allow approximate suppression, but they must be measured or calculated rather than chosen.

Bulk force cancellation is weaker. Two local force responses (+1,-1) sum to zero yet have sum of squares 2 under independent unit damping. A vanishing net first-shell force does not imply vanishing phonon excitation.

Static registry cannot identify damping. Take U=V(x)+q^Tq/2-q1 sin(x) in illustrative dimensionless units. K=I and qeq=(sin x,0). Both Gamma0=diag(0,1) and Gamma1=diag(1,0) have the identical relaxed potential V(x)-sin(x)^2/2. They give zeta0=0 and zeta1=1/2, respectively. The arbitrary reference V may even make the relaxed potential constant. At each unit tangent coupling the script verifies quadratic forms 0 and 1; averaging cos(x)^2 yields 1/2. This is an identifiability counterexample, not a graphite simulation.

If the lossy coupling vector h(epsilon)=Gamma^(1/2)K^(-1)g equals epsilon h1+O(epsilon^2) with h(0)=0, its dissipation begins at epsilon^2||h1||^2. With nonzero h0 there can instead be a linear cross term. Therefore the earlier quadratic-strain suggestion is only conditional and is not a universal strain prediction. Geometry must determine whether strain actually opens this coupling.

## 4. Target-blind next test

Acquire independently parameterized U_theta, force Hessians, mode-resolved damping or bath spectra, masses, boundary conditions, normal-load relaxation, temperature and sliding direction. Use the same material law across aligned,(2,1),(3,1); do not fit one damping matrix per angle to match friction. Account for finite contact edges and defects separately.

Compute the mixed derivative g and response-weighted overlap zeta before friction target access. Compare against a full conventional atomistic/phonon baseline, not merely a scalar corrugation amplitude. Low-speed dissipation is itself conventional mechanics; relabeling the response overlap as UD is not an extra explanation. A distinctive UD branch requires an independently derived constraint on the coupling or bath map and a prediction the baseline does not already supply.

Acceptance rule remains OPEN until measurement errors and predictive uncertainties are available. A proposed comparison statistic is held-out friction predictive error under the same calibration budget, plus independently checked mode excitation. No numerical success threshold is fabricated. Failure to derive a nontrivial physical constraint ends the additional-protection branch, preserving the conventional shell result.

## Verification and limitations

verify.py uses only Python standard-library exact Fraction arithmetic. It proves the reciprocal-shell minima and checks explicit damping-orientation, local-cancellation and declared leakage controls. Angular decimals are numerical displays. No DFT, phonon Hessian, bath calculation, friction experiment or independent adversarial review was executed. Initial verifier attempt required absent SymPy; it was replaced with exact standard-library fractions before producing the result. No scientific formula changed to fit outcomes.
