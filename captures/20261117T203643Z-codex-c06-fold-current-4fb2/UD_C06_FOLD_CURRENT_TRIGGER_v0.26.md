# C06 fold-current trigger v0.26

**EXACT / CONDITIONAL NO-GO** for fixed linear flux-to-hinge velocity over arbitrary stock scales. **CANDIDATE** for normalized phase locking. **Physical Promotion = 0.**

The symmetric equilateral net closes with all hinge angles equal to \(\phi_*=\arccos(-1/3)\) from flat. At closure the three tips coincide, so the shared tip is at the slant-edge distance from all three base vertices. The sphere intersection fixes the two mirror apexes. On the chosen upward branch every hinge must reach the same angle. The signed closure \(1+3\cos\phi\) has slope \(-2\sqrt2\) there. For independent hinge errors the quadratic seam-distance coefficient is \(\ell^2(5I+J_3)/4\). Its Hessian is twice that matrix. The ratio \(8:5\) is a geometric sensitivity ratio and becomes a stiffness ratio only for an energy proportional to squared seam distance in those coordinates.

On the v0.18 aligned odd oscillator, let \(R_i\) be the squared record amplitude of pair \(i\), \(J_i=\dot R_i\) its signed flux, \(R=\sum_iR_i\), \(N>0\) the conserved initial odd stock, and \(f=R/N\). Start with empty records and a flat net. Test the prescribed kinematic input \(\dot{\boldsymbol\phi}=KJ\) for a fixed real \(3\times3\) matrix \(K\). Integration gives \(\boldsymbol\phi=K(R_1,R_2,R_3)^\mathsf T\) exactly. This law uses signed bilinear flux. It does not identify angular momentum with a native UD variable.

Under common-phase preparation, \(R_i=N_i f\) and the shares \(N_i/N\) may range over the full simplex. At half stock, pure-pair preparations force each column of \(K\) to equal \((2\phi_*/N)\mathbf1\) if closure is to occur for every preparation at that stock. This condition is also sufficient, since all other shares are convex combinations. Therefore a fixed linear law that works at one stock has identical rows and columns and must use total flux. Diagonal pair-to-hinge actuation cannot supply this map. Varying \(N\) makes even the common coefficient impossible to keep fixed.

For example calibrate the common gain \(\kappa=2\phi_*/N_0\). On a stock \(2N_0\), closure occurs at \(f=1/4\) during the incoming branch. On a stock \(N_0/4\), full transfer only reaches angle \(\phi_*/2\), leaving closure unreached on that branch. The test does not require varying hinge speed independently once the flux law has been imposed.

If the proposed coupling means torque, the simplest declared inertial law \(I\ddot\phi=\gamma\dot R\) from rest instead gives \(\dot\phi=\gamma R/I\). For \(f(t)=\sin^2(\omega_-t)\),
\[
\phi\!\left(\frac{\pi}{4\omega_-}\right)
=\frac{\gamma N}{8I\omega_-}(\pi-2).
\]
The half-stock angle depends on both stock and rate in this model.

## Candidate normalized law

The declared rule \(\dot\phi_i=2\phi_*\,(\sum_j J_j)/N\) gives \(\phi_i=2\phi_* f\) with the stated preparation and net initial condition. The closure event is then the first directed global half-stock crossing whenever that crossing exists. This identity continues to hold under dephasing if the flux is still the derivative of total recorded stock. A dephased preparation need not have a qualifying crossing. The normalized rule inserts both global stock access and the target factor \(2\phi_*\), and it is a candidate rather than a native derivation. It supplies no reciprocal mechanical reaction, terminal authorization, or same-event rank-three cut. The v0.25 hard drive constraint implements the cut only when imposed. Stage 2 remains open.

Run python3 replay_c06_fold_current.py for exact stock-rescaling and preparation-share controls. The code represents hinge angles in units of \(\phi_*\).
