# Nonlinear orbital instability of the neutral flat stationary family

Status: DERIVED CONDITIONAL under the unchanged candidate joint Hamiltonian. Constructor verified; independent review pending; development lane, no registry promotion; physical promotion 0.

## Main theorem and boundary

For every fixed finite rank r, a>0 and nonzero neutral vertex amplitude alpha, the flat stationary family is nonlinearly orbitally unstable at kappa>=0 except for six explicitly unresolved positive values of t=a*kappa/r:

    {2/3, 8/3, 16/(6-sqrt(2)), 16/(6+sqrt(2)),
                 16/(4-sqrt(2)), 16/(4+sqrt(2))}.

This is a theorem about the declared action and this background family. It does not decide those six cases, every other stationary branch, or physical dynamics.

At positive stiffness in the proved domain, exactly Gauss-admissible initial data approach the stationary orbit while preserving both species norms 4 alpha^2. Exact nonlinear trajectories reach a fixed positive higher-simplex matter stock at times O(1/epsilon). This stock is invariant under local gauge and species phases and is zero on every stationary-family orbit. The zero-stiffness counterexample instead uses a fixed diamond-holonomy departure.

## New exact structure

Define the simplex parity Gamma=(-1)^dimension and w=Gamma bar(chi), in the common mu-rotating frame. Both psi and w obey the same anti-Hermitian transport equation. Their entire 2x2 Gram matrix is conserved. Equivalently f=(psi+w)/2 and d=(psi-w)/2 co-move, so their norms and overlap are constant.

The relation d=0, or chi=Gamma bar(psi), is an exact force-canceling invariant sector. It differs from chi=bar(psi) on odd-dimensional simplices. The old neutral curvature seed is not retracted.

The Hermitian source difference Q=psi psi^dagger-w w^dagger evolves by conjugation. Its trace norm is constant. This gives the uniform bound

    field_energy(s) <= H_0(0)+4 ||Q(0)||_1,
    ||Q(0)||_1 <=4 ||f(0)|| ||d(0)||,

where H_0=H-mu(N_psi+N_chi). A small mismatch therefore stays small, and fields can remain uniformly weak while the common matter shape departs on long times.

## Nonlinear argument

The exact Coulomb equations retain longitudinal electric momentum through Gauss law. With d=epsilon D and transverse field angles/momenta scaled by epsilon, the leading matter flow has frequencies 0,+2,-2 and the bilinear field source has frequencies 0,2,4. Away from field frequencies 2 and 4, an explicit bounded particular response removes that source. The resulting leading flow is a product of rotations; its first correction has only finitely many Fourier weights. A bounded homological primitive and Gronwall estimate justify the averaged evolution for fixed slow time tau=epsilon s.

At f=alpha k, a real edge perturbation in the gradient or cycle sector has averaged drift

    d f_bar/d tau =2 i a alpha^2 f_j(t) D_j,

    f_g(t)=-2(t-1)(7t-4)/(34t^2-48t+16),
    f_c(t)= 2(5t-4)/(14t^2-32t+16).

Their zeros never coincide. Stroboscopic times s=n*pi remove the native fast matter rotation and give a fixed observable departure. The proof controls the nonlinear remainder; it does not extrapolate a linear Jordan solution without bounds.

At the four coupled field-frequency-2 resonances, an exactly force-canceling pure-field oscillation drives matter through a nonzero first averaged matrix element. The stiffness-6 frequency-2 resonance and five frequency-4 resonances remain OPEN. At kappa=0 exact force-canceling cycle drift closes the orbital instability counterexample.

The scalar construction embeds into one active color at arbitrary rank, with magnetic coefficient kappa/r. Higher-simplex stock remains invariant under the full local gauge group, so additional color gauge directions cannot remove the counterexample.

## Verification and next gate

42 exact constructor algebra checks passed. Three separately typed full nonlinear numerical campaigns corroborate finite departure with decreasing perturbation size and report energy, Gram and reconstructed Gauss residuals. These are numerical diagnostics, not empirical data or a substitute for the written averaging proof.

The prior positive-stiffness zero-matter vacuum stability theorem and complete Hamiltonian flow remain valid. The action was not modified. G05 physical action normalization, the physical group, units and experimental correspondence remain open.

Next: resolve the six remaining resonant parameter values with dedicated nonlinear normal forms before asserting a parameter-wide nonlinear obstruction. An action repair would be a separate candidate branch requiring a source rationale.
