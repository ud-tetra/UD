# Graphite material port: measured conservative coupling and the damping source gap

22 October 2026. **Development — no registry entry; physical promotion 0.** This is a follow-on to the graphite working paper in draft PR #402. It does not edit that capture. All numerical values are constructor results from the archived frozen graphite sliding-port model in draft PR #334; no independent review or new friction measurement is claimed.

## 1. What can be calculated from the existing atomic model

Let the two layers have equal populations among \(N=1008\) carbon atoms. Let \(B\) contain the archived orthonormal internal Cartesian basis and let \(T_x,T_y\) be the relative-layer translation vectors with entries \(\sigma_i/\sqrt N\), \(\sigma_i=\pm1\) by layer. The internal coordinates \(q\) and normalized port \(r\) both have length units. The physical relative translation is \(\boldsymbol\delta=2\mathbf r/\sqrt N\). For a constrained, internally stationary reference at fixed layer registry,

\[
U(q,r)=U_0-b_r^Tr+\frac12 q^THq+q^TCr+\frac12r^TPr+O(\|(q,r)\|^3),
\quad H=B^T\nabla^2 U B,\ C=B^T\nabla^2 U T.
\]

Thus the **material mixed coupling** to physical slip is

\[
G_\delta:=\frac{\partial^2U}{\partial q\partial\delta}
=\frac{\sqrt N}{2}C. \tag{1}
\]

This is an exact coordinate conversion for the declared basis, not a new fitted coefficient. It has units eV/Å² with \(q,\delta\) measured in Å. The archived PR #334 `C_norm` is \(\|C\|_F\), not a single scalar oscillator drive or a damping coefficient. The captured input candidate has shape `(1008,3)` and SHA-256 `039c16de70222344c1bdf314d32b0bac1c019613182782fcec47d4005a6e3022`; the archived `RESULTS.json` has SHA-256 `9ef5e2a7efc6d5a5e5143813b465cc4959d08ff32a64f871a65b4f699e5affad`.

| Held-registry preparation | \(\|C\|_F\) (eV/Å²) | \(\|G_\delta\|_F\) (eV/Å²) | What this licenses |
|---|---:|---:|---|
| `21_dir_0` | 0.160141240752 | 2.542163386053 | Resolved nonzero conservative coupling in this constrained model |
| `21_dir_10024` | 0.159515834529 | 2.532235370045 | Same, distinct archived preparation |

The two source labels are not proved to be distinct physical minima. The references were internally stationary under maintained registry, and some relaxed sliding stiffnesses were negative; releasing the sliding clamp changes their preparation. These norm values cannot be read as a force amplitude for the first moiré harmonic. The subsequently released (2,1) endpoint full 81-coordinate Hessians failed the frozen one-sided and step/directional qualifications. Equation (1) is a conversion of *earlier scoped derivatives*, not a way around that HOLD. No load series was computed here.

To produce a mode-resolved drive for a declared sliding direction \(e\), let \(u_j\) be a mass-orthonormal eigenmode of an accepted internal \(H\) and define \(c_j=u_j^T G_\delta e\). An actual periodic trajectory needs the full position-dependent \(g_j(x,N)=\partial^2 U/\partial q_j\partial x\), not just one tangent \(c_j\); it may be Fourier-decomposed as \(g_j(x,N)=\sum_k g_{jk}(N)e^{ikx}\). No unique \(g_{jk}\) follows from the Frobenius norms in the table.

## 2. Derive the memory kernel before calling anything damping

Assume a stable, fixed harmonic internal block with positive modal frequencies \(\omega_j\), masses \(m_j\), and constant couplings \(c_j\) to the imposed slip coordinate \(\delta\). The conservative Hamiltonian has terms \(\tfrac12m_j\dot q_j^2+\tfrac12m_j\omega_j^2 q_j^2+c_jq_j\delta\). Solving the \(q_j\) equations and integrating by parts gives, after separating the elastic Schur complement, a slip reaction containing

\[
\int_0^t K_{\rm mem}(t-s)\dot\delta(s)\,ds,
\qquad K_{\rm mem}(t)=\sum_j{c_j^2\over m_j\omega_j^2}\cos(\omega_jt). \tag{2}
\]

Initial-state and slip-at-\(t=0\) terms must also be retained. For vector slip, replace \(c_j^2\) with \(c_jc_j^T\). This agrees in form with the archived finite-harmonic-memory identity. The factors have units N/m, so integrating against velocity gives force. The bath spectral density is the distribution

\[
J(\omega)={\pi\over2}\sum_j{c_j^2\over m_j\omega_j}\,\delta_{\rm D}(\omega-\omega_j),
\qquad K_{\rm mem}(t)={2\over\pi}\int_0^\infty {J(\omega)\over\omega}\cos(\omega t)\,d\omega. \tag{3}
\]

For **any finite positive-frequency harmonic block**, the Abel-regulated zero-frequency friction is

\[
\eta_{\rm dc}:=\lim_{\epsilon\downarrow0}\int_0^\infty e^{-\epsilon t}K_{\rm mem}(t)\,dt
=\lim_{\epsilon\downarrow0}\sum_j{c_j^2\over m_j\omega_j^2}{\epsilon\over\epsilon^2+\omega_j^2}=0. \tag{4}
\]

This is a precise **no-go for deriving a nonzero constant Markov damping coefficient from the finite, closed, positive-frequency archived harmonic sector**. It does not say an actual macroscopic graphite contact has zero friction. Finite systems have transient and resonant energy transfer; sustained resonant driving lacks a finite stationary loss rate without an export mechanism. Gapless continua, anharmonic decay, defects, boundaries, thermal reservoirs, or externally maintained nonequilibrium modes can change the limit.

A nonzero low-frequency Ohmic coefficient requires a separately justified continuum/sink limit for which \(\eta=\lim_{\omega\downarrow0}J(\omega)/\omega\) exists and is positive, with a stated order of thermodynamic, long-time, and low-speed limits. Alternatively, under a valid equilibrium projection and Markov separation, a constrained force-fluctuation calculation would use \(\eta=\beta\int_0^\infty\langle R(t)R(0)\rangle_{\rm eq}\,dt\), where \(R\) is the force of the orthogonal bath dynamics and the same slip/load preparation is held. A raw unprojected force autocorrelation is not automatically this kernel. Neither measurement was performed in the graphite archive. A static Hessian supplies frequencies and couplings on its qualified subspace; it does not supply the lifetime, projected bath correlations, or thermodynamic limit.

## 3. The UD mapping and unit obstruction

The physical honeycomb graph of nearest-neighbor C–C bonds is bipartite and has **no three-edge cycles**. Its six-membered rings and the triangular Bravais lattice of either same-sublattice set are different complexes. A direct edge-for-edge identification of a physical carbon-bond triangular face with a UD triangular transport face therefore does not exist. A candidate coarse-graining can use second-neighbor triangular paths, but it must specify the path weights, overlapping hexagon ownership, orientation, layer registry, and an interlayer transport rule. It cannot borrow the UD finite-complex `PF=0` theorem as a graphite fact.

For a physical correspondence, declare maps \(D_k:C_k^{\rm carbon,coarse}\to C_k^{\rm UD}\) obeying \(D_{k-1}B_k^{\rm carbon}=B_k^{\rm UD}D_k\), an energy pairing, and a port \(F_{\rm mat}\). A proposed protected sector has to verify \(P_{\rm UD}F_{\rm mat}=0\) or a quantified leakage; no such maps or projection checks currently exist. A purely mathematical UD burden-mixing rate (ledger Q162/Q163) cannot be identified with the material \(\eta\) in kg/s.

Indeed let the native variables be normalized using energy \(E_*\), time \(t_*\), and slip length \(\delta_*\). A native dimensionless low-speed response \(\zeta_*\) would map to

\[
\eta_{\rm physical}={E_*t_*\over\delta_*^2}\,\zeta_* . \tag{5}
\]

Derivation: \(P_{\rm heat}=(E_*/t_*)\zeta_*(dx/ds)^2\) and \(dx/ds=t_*v/\delta_*\); compare \(P_{\rm heat}=\eta_{\rm physical}v^2\). The current UD program supplies neither this material triple \((E_*,t_*,\delta_*)\) nor a graphite-specific loss port or source-selected \(\zeta_*\). Equation (5) makes the missing normalization explicit; inserting an arbitrary clock or the dimensionless \(4/3\) from Q163 would be a unit error.

## 4. Quantitative next calculation with a falsifiable gate

1. Compute \(g_j(x,N)\) and the phonon spectral measure with the **same** interlayer potential and force implementation at both mirrored (2,1) angles, the aligned interface, and a (3,1) control. Specify finite area, edge conditions, temperature, and load equilibrium; first qualify derivatives and stable modes. The earlier resolved norm in Eq. (1) is a useful instrumentation check, not a fit target.
2. Determine \(J_{ab}(\omega;\theta,N)\) or a projected force correlation from a declared bath with actual energy export. Assess convergence under area/time/broadening changes before extracting \(\eta\). A finite discrete spectrum alone fails the DC gate in Eq. (4).
3. Construct and freeze the physical UD chain/coarse-graining map and its normalization independently of the target friction curves. Compare its predicted coupling/loss projection to a conventional atomistic plus bath baseline at held-out \((\theta,N,v)\). A fit-equivalent oscillator or a relabeled conventional phonon channel is not an additional UD mechanism.

**Result:** scoped nonzero material conservative port coupling is already numerical in the archive; the dissipation kernel and its finite-bath DC limit are derived here. A physical positive damping coefficient and UD-specific residual friction remain OPEN/NO-GO until a bath and native-to-material map are supplied. Constructor derivation only; physical promotion 0.
