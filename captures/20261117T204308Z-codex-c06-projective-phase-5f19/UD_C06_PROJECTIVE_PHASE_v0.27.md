# C06 projective stock and directed phase v0.27

**EXACT / CONDITIONAL** for the common-rate aligned odd oscillator. **CANDIDATE** for any dynamical connection from this reduction to the hinged net or the port cut. **Physical Promotion = 0.**

Let \(u,v\) be the aligned odd carrier and record amplitudes, with \(\dot u=-\omega v,\ \dot v=\omega u\), \(\omega>0\), and \(N=\|u\|^2+\|v\|^2>0\). The flow commutes with simultaneous nonzero real rescaling. It descends to real projective space of the joint registers, or to the unit sphere with antipodal identification. A sphere of carrier states alone discards the record variables.

On this quotient \(f=\|v\|^2/N\) is a smooth observable. Its incoming derivative is
\[
\dot f=2\omega\langle u,v\rangle/N=\dot R/N.
\]
This derives the normalized flux as the derivative of a geometric quadratic fraction. There is no division by a desired transfer fraction. The v0.26 fold law still uses the independent choice \(\phi=2\phi_* f\). On a prepared incoming trajectory the prescriptions \(\phi=\phi_* f/f_c\), for any chosen \(0<f_c<1\), are scale invariant and close first at \(f=f_c\). They can be stopped there. The real-ray reduction therefore supplies the observable and does not select the hinge law or port action.

## Directed crossings for dephased preparations

Define the real-ray observables \(D=(\|u\|^2-\|v\|^2)/N\) and \(C=2\langle u,v\rangle/N\). Then
\[
\dot D=-2\omega C,\qquad \dot C=2\omega D,\qquad
D^2+C^2=1-\frac{4(\|u\|^2\|v\|^2-\langle u,v\rangle^2)}{N^2}.
\]
Thus \(D+iC\) rotates at \(2\omega\), and its modulus \(\rho\) is constant in \([0,1]\). The fraction \(f=(1-D)/2\) ranges from \((1-\rho)/2\) to \((1+\rho)/2\). For \(\rho>0\), upward half-stock events are exactly \(D=0,C=\rho\), with slope \(\dot f=\omega\rho\). Their timing depends on the initial phase. When \(\rho=0\), equal nonzero squared stocks and orthogonal registers give \(f=1/2\) identically, so the directed guard never fires. There is no uniform positive slope over all dephased preparations. Empty records imply \(\rho=1\), with the first event at \(\pi/(4\omega)\).

## Complex phase quotient and actuation

For the aligned oscillator complex structure \(w=u+iv\), the incoming flow is multiplication by \(e^{i\omega t}\). Passing to complex rays for that complex structure therefore collapses the entire trajectory to one point. For example, \((u,0)\) and \((0,u)\) represent one complex ray and have fractions zero and one. The balance observable cannot descend to that quotient. This statement pertains to identifying the oscillator phase, not to quotients by unrelated symmetries.

The exact normalized derivative requires an active reciprocal exchange under the declared port, and the target fold-angle relation needs a further mechanical law. The same-event transition applying \(G(I-P_-)\), reciprocal mechanical coupling, and Stage 2 remain open. Correction to the v0.26 note accompanying the user summary: the low-stock witness bounds hinge angle, while apex height is a sine of angle. The loading proof remains in UD #553, and the fold-current proof in UD #554.

Run python3 replay_c06_projective_phase.py for exact controls of rescaling, rational rotations, complex-ray collapse and the stationary dephased preparation.
