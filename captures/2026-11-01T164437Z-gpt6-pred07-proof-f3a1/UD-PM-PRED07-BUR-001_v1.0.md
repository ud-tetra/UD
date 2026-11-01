# UD-PM-PRED07-BUR-001 v1.0 — Conservative K4 burden instability under an added nonlinear redistribution rule

**Proof kind:** THEOREM / conditional constructive branch. **Proof status:** PROVED_CONDITIONAL, independently checked by a different algebraic method but not peer reviewed. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## 1. Source and new assumptions

- Source: `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22; SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`), Q153 (incidence balance, constitutive source open), Q156 (hard contact), Q162 (conditional relaxational flux), Q169 (fixed support incidence). The relevant no-go and conditional comparator are `UD-PM-PRED06-SEL-001` and `UD-PM-PRED06-SEL-002`, source PR #490 at commit `51c1885a140f732a9518760e1e3fcb2f431e2832` (unmerged).
- **New assumption B1:** Work on one completely connected K4 with *all six Q156 contacts open*; burden coordinates are real nonnegative scalars `b_i` with total `M=sum_i b_i>0`. This is a packet-level local model, not a proof that these coordinates are the source's canonical burden load.
- **New assumption B2:** Let `gamma>0` be a chosen nonlinear redistribution strength measured in an uncalibrated model time. Define the additional source vector

  \[s_i(b)=\gamma b_i\left(b_i-\frac{Q}{M}\right),\qquad Q=\sum_j b_j^2.\]

  This is a **candidate constitutive choice** absent from Q153/Q162, not a coefficient derived from `7/768`, the phase fiber, or a physical energy unit.
- **Update:** For oriented incidence \(B_1\in\mathbb R^{4\times6}\), put \(L=B_1B_1^T=4I-\mathbf1\mathbf1^T\) and

  \[\dot b=-\frac14Lb+s(b).\tag{B1}\]

  Initial conditions lie in the positive simplex of fixed total \(M\); the model has no physical boundary contact, cell excision, or measured clock.

## 2. Theorem: conservative, positive, equivariant, generically symmetry-amplifying

Under B1–B2:

1. **Positive conservation:** \(\sum_i b_i=M\) is invariant, the closed positive simplex \(b_i\ge0\) is forward invariant, and a global solution exists at all nonnegative model times.
2. **Full S4 equivariance:** The vector field commutes with all permutations of the four vertex labels; consequently an exactly uniform state \(b=(M/4)\mathbf1\) remains uniform for all times.
3. **Exact contrast equation:** For every pair of vertices \(i,j\),
   \[\frac{d}{dt}(b_i-b_j)=(b_i-b_j)\left[-1+\gamma\left(b_i+b_j-\frac QM\right)\right].\tag{B2}\]
   Therefore a strictly ordered initial burden tuple remains strictly ordered at every finite time; a unique highest vertex and a unique lowest neighbor determine a strictly greatest outgoing Q162 current **if and when** the separately proposed comparator is enabled.
4. **Uniform-state linear stability:** On the mass-preserving three-dimensional tangent subspace at uniform burden, the Jacobian has eigenvalue \(\sigma=\gamma M/4-1\) (multiplicity three). Uniform burden is linearly unstable if \(\gamma M>4\), and linearly attracting if \(\gamma M<4\). The equality case is not classified by linearization.
5. **Exact nonlinear amplification witness:** The invariant one-high/three-equal-low submanifold is parametrized by \(b_0=(M+3d)/4\), \(b_{1,2,3}=(M-d)/4\), \(0\le d\le M\). On it,
   \[\dot d=d\left[-1+\gamma\left(\frac M4+\frac d2-\frac{3d^2}{4M}\right)\right].\tag{B3}\]
   For \(M=4\), \(\gamma=2\), \(\dot d=d(1+d-3d^2/8)\). Each \(0<d(0)<d_*=(4+2\sqrt{10})/3\) increases monotonically to \(d_*\). In particular, for \(0<d(0)<1\), the explicitly **chosen** contrast gate \(d\ge1\) activates at a finite time. This proves amplification from arbitrarily small nonzero deviations, **not selection from exact symmetry**.

## 3. Proof

Conservation follows because \(\mathbf1^TL=0\) and \(\sum_i s_i=\gamma[Q-(Q/M)M]=0\). If \(b_i=0\) on a simplex boundary, then \(s_i=0\) and the diffusive part is \(M/4\ge0\); the vector field cannot cross into negative coordinates. Smoothness on the compact fixed-\(M>0\) simplex supplies global solutions. Both \(L\) and the scalar symmetric statistic \(Q/M\) are permutation equivariant, so the ODE is S4 equivariant. By uniqueness, uniform initial data remain invariant.

For vertices \(i,j\), the diffusion difference is \(-(b_i-b_j)\) because \(L=4I-J\). The nonlinear difference factors as \(\gamma(b_i-b_j)(b_i+b_j-Q/M)\), proving (B2). It is a scalar homogeneous equation in the contrast; its solution is the initial difference times the exponential of a finite real integral, so its sign never changes at finite model time. When all six hard gates are open, \(J_{v\to w}=(b_v-b_w)/4\), so the unique minimum of three distinct neighboring values is the unique maximum outward current from the winner.

For a zero-sum perturbation \(b=(M/4)\mathbf1+\varepsilon\), the derivative of \(Q/M\) in any zero-sum direction vanishes at \(\varepsilon=0\); the derivative of \(b_i(b_i-Q/M)\) is \((M/4)\varepsilon_i\). The diffusive eigenvalue is \(-1\) on the zero-sum subspace, yielding \(\sigma\) as stated. Permutation symmetry makes the one-high/three-low submanifold invariant; substituting its exact coordinates into (B2) proves (B3). For the selected rational values, the scalar growth factor \(1+d-3d^2/8\) is positive on \((0,d_*)\), zero at the positive root \(d_*\), and negative above it up to the endpoint of the simplex. Standard scalar ODE uniqueness yields monotone convergence to \(d_*\); on \([d(0),1]\), the growth factor is at least one, yielding the finite threshold crossing. QED.

## 4. Distinct port selection and assumption failures

The one-high/three-equal-low witness has **three tied ports**, so it is **not itself a full seed-and-port construction**. Choose arbitrarily small further initial perturbations that strictly order the lower vertices. The exact contrast sign theorem preserves the strict ranking, yielding a unique outgoing Q162 current. By finite-time continuous dependence, sufficiently small such perturbations still cross the threshold of the symmetric witness. This establishes existence of generic near-witness trajectories with both unique seed and unique port; it does not give an exact crossing time for all perturbations.

At exactly uniform preparation every vertex remains equivalent even when \(\gamma M>4\), consistent with the PRED06 S4 no-go. The identity of the winner is selected by **initial asymmetry**, not created without a symmetry-breaking input. If \(\gamma M<4\), infinitesimal contrast decays rather than grows. A closed Q156 contact alters the Laplacian and invalidates this exact spectrum and port claim. Neither \(\gamma\), a threshold, a physical noise distribution nor the topology-changing excision/restoration mechanism is derived by this proof.

**Additional exact provenance note:** Because \(\sum s_i=0\) and \(L=4I-J\), on K4 we may write \(s=B_1(B_1^Ts/4)\). Thus this added term is mathematically an *internal conservative flux redistribution*, not a newly derived nonconservative burden source from Q153. It increases burden contrast without identifying a physical energy reservoir or conserved energy law.

## 5. Verification and disposition

A separate exact SymPy audit checks the full polynomial identity, the linear stability eigenvalue, all 24 relabelings, the scalar reduction, the exact fixed point and conservative flux representation. A numerical ODE control uses an illustrative \(b(0)=(1.03,1.01,0.99,0.97)\), \(M=4\), \(\gamma=2\), and a lower-gain control \(\gamma=1/2\); no physical measurements. Non-constructor review **DEFERRED**, physical promotion **0**.

**OPEN_GATED:** source-complete nonlinear generator/stock exchange, initial perturbation statistics, symmetry-breaking boundary, native gate-trigger, cell occupancy, model-to-physical time, action/energy receipt, and laboratory readout. Proof status **EXACT_CONDITIONAL**; no claim of an autonomous UD defect from uniform state.
