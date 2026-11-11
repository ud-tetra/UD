# Exact hidden-breathing memory, v0.1

RESULT / STATUS: DERIVED conditional exact reduction; NUMERICAL verification PASS on 36 retained configurations. Physical promotion 0. Native UD/material correspondence and physical bath remain OPEN/HOLD. Development — no registry entry. Constructor verification is not independent review.

## Scope and coordinates

The input is the frozen constrained stiffness archive from the axial-observable closure audit. The two earlier observable rowspaces coincide with the orthogonal complement of the same geometry-fixed relative-layer breathing vector b. They are not counted as independent dynamical models here. There are 36 unique matrices, each of dimension n=27 or51, at four relaxed geometries, three cutoffs and three imposed smoothing widths. The retained sectors are primitive-periodic and vertical; this does not establish full-supercell, Bloch, nonlinear or driven sliding dynamics.

Take a geometry-fixed orthonormal basis Z for b-perp. For q=Zx+bz and q''=-Hq, define A=Z^T HZ, a=Z^T Hb, k=b^T Hb and omega=sqrt(k). Common scalar carbon mass has been absorbed in the mathematical time coordinate; times and frequencies here are in model units and do not identify a physical clock or friction coefficient. x is an orthonormal encoding of the observed rowspace, not the raw redundant bond-vector output.

## Exact elimination

The full split equations are

    x'' + A x + a z = 0
    z'' + k z + a^T x = 0.

For arbitrary initial x0,z0,v0,w0, let zh(t)=z0 cos(omega t)+w0 sin(omega t)/omega. Duhamel's formula gives

    z(t) = zh(t) - integral_0^t sin(omega(t-s))/omega * a^T x(s) ds
    x'' + A x - integral_0^t M(t-s) x(s) ds = -a zh(t)
    M(t) = a a^T sin(omega t)/omega.

The negative sign before displacement memory follows from reciprocal conservative coupling; changing it fails to recover the full equations.

Integration by parts gives the equivalent velocity-memory representation:

    S = A - a a^T/k
    K(t) = a a^T cos(omega t)/k
    x'' + S x + integral_0^t K(t-s) x'(s) ds
        = -a (z0 + a^T x0/k) cos(omega t)
          -a w0 sin(omega t)/omega.

The initial-slip term a^T x0/k must be retained. Conditional-equilibrium preparation z0=-a^T x0/k,w0=0 removes the right-hand side, but leaves memory. Other initial preparations cannot be called thermal noise without specifying an ensemble and temperature.

For zero initial data, Laplace elimination gives dynamic stiffness s^2 I+A-a a^T/(s^2+k). The hidden oscillator has poles at +/-i omega. These are poles of the eliminated subsystem; they are not assertions that omega is an eigenfrequency of the fully coupled matrix H.

## Reversibility and claim boundary

Because a is nonzero, the kernels have rank one whenever their scalar factor is nonzero, and rank zero at its zeros. K(t) oscillates and changes sign. A sign-changing time-domain kernel alone does not disprove passivity: this kernel comes from a conservative passive oscillator. It does rule out identifying it with a constant positive Markov friction term without an additional approximation and source justification.

The exact full energy

    E = (|x'|^2 + z'^2 + x^T A x + 2 z a^T x + k z^2)/2

is conserved. Equivalently E=(|x'|^2+x^T Sx)/2 + z'^2/2 + k(z+a^T x/k)^2/2. Energy exchanged with the hidden coordinate remains in this finite closed system. No stochastic reservoir, irreversible drain, physical Gamma, or experimentally measured friction follows from eliminating one coordinate. Nor does this result exclude dissipation in a larger, genuinely open physical system.

The geometry-fixed hidden breathing coordinate explains why the earlier instantaneous observable dynamics failed closure. Its exact elimination yields history dependence, not autonomous smaller dynamics. This reduction is conventional linear mechanics; calling it a native UD protected mechanism still requires a source-selected material dictionary and bath coupling.

## Frozen numerical checks and results

The protocol was written before computing these outcomes. Four initial preparations per configuration, six times through two hidden periods and 256/512-point Gauss-Legendre history quadrature give 864 state-time checks at each quadrature order. The integrals are evaluated on original-H spectral trajectories, rather than relabeling an augmented ODE as a memory check. Full versus transformed-block spectral trajectories, energy, hidden reconstruction and both integral equations pass the declared normalized tolerances.

Maximum displacement-memory residual: 7.06e-15. Maximum velocity-memory residual: 7.07e-15. Hidden reconstruction error: 2.90e-13. Full/block trajectory discrepancy: 4.69e-13. Quadrature-order discrepancy: 1.86e-14. Relative energy error: 8.39e-15. Residual normalizations are max(1,term norms); they are numerical consistency checks, not uncertainty bounds on the force model.

Across the 36 configurations, k lies in [0.28239708,0.28255042], omega in [0.53141046,0.53155472], |a| in [0.14609055,0.14939488], and ||K(0)||2 in [0.07557597,0.07901862], all in inherited model units. Every Schur complement is positive definite, with minimum eigenvalue between1.2974 and3.6404. These ranges describe the qualified finite family; they are not convergence bounds or fitted physical constants.

A second constructor script checks block reconstruction and compares independent adaptive DOP853 evolution with the original-H spectral solution, then reverses endpoint velocity and integrates back. Detailed errors are in VERIFICATION.json. The calculate.py time-reversal identity is only an algebraic consistency check; the ODE reversal supplies the separate numerical test. Neither script constitutes non-constructor review.

An initial implementation stopped before producing results because a max() helper mishandled an empty list of comparison terms. Its source is preserved under development_failure; the correction changes only residual normalization plumbing. No scientific threshold or protocol was changed.

## Reproduction and next gate

Run calculate.py then verify.py with NumPy/SciPy and the preserved sibling input graphite-closure/CLOSURE.npz. FREEZE.json hashes that input. MEMORY.npz retains all blocks and per-state quadrature records; the input archive contains the original H and b. RESULTS.json and VERIFICATION.json preserve all 36 cases.

The next useful gate is a source-reservoir audit: specify which additional physical or native UD degrees of freedom could act as a bath, what fixes their coupling and loss, and what observation would distinguish that hypothesis from ordinary conservative mode exchange. Physical promotion remains0 until an independently tested correspondence has its own receipt.
