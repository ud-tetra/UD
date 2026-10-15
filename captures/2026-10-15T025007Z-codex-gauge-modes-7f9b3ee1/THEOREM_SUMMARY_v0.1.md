# Gauge-reduced modes and stability of neutral flat backgrounds

Status: DERIVED CONDITIONAL under the declared joint Hamiltonian. Constructor checked; independent review pending; development lane; physical promotion 0.

## Stationary family and reduction

At mu=0 all strictly stationary flat-link backgrounds, up to gauge and constant species phases, have identity links, zero electric momentum and psi=chi=alpha k e1, where k is one on the four vertices and zero on higher simplices. Alpha>=0 is free, with each species norm 4 alpha^2. For mu>0 the same family rotates by the common global species phase exp(-i mu s); it is a relative equilibrium, analyzed in that rotating frame. Curved and excited stationary branches are not classified.

For r=1 and alpha>0, imposing 15 independent Gauss constraints and removing 15 gauge directions leaves 86 real dimensions. The explicit Coulomb reduction retains the longitudinal electric momentum required by Gauss law and the global neutrality condition. It has one physical semisimple zero pair, not 30 leftover gauge zero directions.

## Exact spectrum

The diamond stiffness K=C^T C has eigenvalues 0 (14 gauge gradients), 6 (multiplicity 2), and 6-sqrt(2), 6+sqrt(2), 4-sqrt(2), 4+sqrt(2), each of multiplicity 3. Hence there are 14 link oscillators with squared frequencies a kappa times those five positive stiffnesses.

With t=a kappa, define

    F_t(lambda) = (lambda^2+6t)^2
       [(lambda^2+6t)^2-2t^2]^3
       [(lambda^2+4t)^2-2t^2]^3.

The Abelian reduced characteristic polynomial is

    lambda^2 (lambda^2+4)^28 F_t(lambda).

Frequencies are independent of alpha>0, but Jordan couplings are not. Imaginary eigenvalues do not establish bounded motion.

## Stability result

Every nonzero member of this neutral family is spectrally stable but has an unbounded gauge-reduced linear flow. For generic positive t, each of +2i and -2i has six size-two and sixteen size-one Jordan blocks. At t=4/7, 4/5 or 1, three size-two blocks remain. The gradient and cycle resonant forcing functions

    f_g(t) = -2(t-1)(7t-4)/(34t^2-48t+16),
    f_c(t) =  2(5t-4)/(14t^2-32t+16)

never vanish together. The field resonance t=2/3 adds uncoupled eigenvectors. At the four coupled field resonances t=4/(6 +/- sqrt(2)) and t=4/(4 +/- sqrt(2)), size-three chains yield quadratic secular terms. Kappa=0 also has cycle drift. No choice of positive magnetic stiffness alone makes the linear flow about this nonzero family bounded.

A rational real Gauss-admissible witness at a=kappa=alpha=1 obeys

    exp(L n pi) w = w - (n pi/8) L(L^2+4I)w.

Its growth is nongauge. A separately typed numerical diagnostic checks this identity. Nonlinear Lyapunov or orbital stability of the nonzero family remains OPEN; no exponential instability is asserted.

## Higher rank and vacuum

At rank r>1, a residual U(r-1) stabilizer remains. The symplectic slice has dimension 28 r^2+56 r+2 and characteristic polynomial

    lambda^2 (lambda^2+4)^(28r) F_(a kappa/r)(lambda)^(r^2).

This is not a claim that the singular physical quotient is a smooth space of that dimension. The active rank-one scalar sector is exactly invariant, and its secular modes survive the residual quotient.

At zero matter the vacuum is singular. A separate conserved functional,

    Vcal = H+(5-mu)(N_psi+N_chi)
         >= a/2 sum tr(E^2) + V_magnetic + N_psi+N_chi,

proves nonlinear Lyapunov stability of the vacuum gauge orbit for kappa>0, for all finite ranks. Its zero set is precisely the flat zero-matter vacuum orbit. At kappa=0 an exact matter-free cycle solution drifts away and proves nonlinear instability.

## Scope and next gate

All conclusions depend on the candidate action, opposite-charge species and internal-time conventions. None identifies physical coupling strengths, proton decay or monopoles. The prior Hamiltonian global-existence theorem is preserved: completeness and bounded nonlinear norms do not guarantee bounded variational flow.

Next: constrained normal-form analysis of nonlinear orbital stability for the nonzero family. Adding a new restoring term would be a separate candidate action branch, with new assumptions.
