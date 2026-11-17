# C06 variational fold selection v0.28

**EXACT / CONDITIONAL** for the declared variational countermodels. **OPEN** for a native action, coupling selection and same-event cut. **Physical Promotion = 0.**

Use aligned odd carrier \(u\), record \(v\), common rate \(\omega>0\), and \(N=\|u\|^2+\|v\|^2>0\). The first-order carrier Lagrangian \(L_c=u\cdot\dot v-\omega N/2\) gives \(\dot u=-\omega v,\ \dot v=\omega u\). Let \(f=\|v\|^2/N\), and let \(\phi_*=\arccos(-1/3)\) denote the upward closure angle from flat. For the countermodel take identical hinges with \(I>0\), \(a>0\), and an arbitrary positive gain \(k\). Define
\[
L_k=L_c+\sum_{i=1}^3
 \left[\tfrac I2(\dot\phi_i-k\dot f)^2-\tfrac a2(\phi_i-k f)^2\right].
\]
This is an allowed test family of joint actions with a velocity-dependent coupling. It is symmetric under hinge permutations and leaves the hinge driving fraction invariant under joint carrier rescaling. Neither the family nor the derivative interaction is asserted to be a native UD law.

The invertible point change \(q_i=\phi_i-kf(u,v)\) makes the action the direct sum of \(L_c\) and three ordinary harmonic hinge actions. Ordinary fixed endpoint variations transform accordingly. Thus each fixed \(k\) defines a stationary branch with \(q_i=\dot q_i=0\). Empty records give \(f(0)=\dot f(0)=0\), so the original hinges start flat and stationary for every \(k\). With these same incoming data \(\phi_i=kf\). For any chosen \(0<f_c<1\), the choice \(k=\phi_*/f_c\) closes at that fraction on the first incoming branch, transversally. This uses the action only through first closure in the modeled hinge interval. The examples \(f_c=1/4,1/2,3/4\) share the same oscillator and hinge constants. The derivative coupling cancels on the tracking branch, so there is no inferred mechanical feedback on that trajectory. This is a counterexample to selection from stationarity plus the stated symmetries and initial data. Varying \(k\) means comparing distinct allowed actions. It is not a variational degree of freedom of one fixed action.

A separate potential-only control replaces the hinge terms with \(I\dot\phi_i^2/2-a(\phi_i-kf)^2/2\). Its hinge equation is \(I\ddot\phi_i=-a(\phi_i-kf)\). Exact tracking over an interval would force \(k\ddot f=0\). For empty records, \(\ddot f(0)=2\omega^2\), so the moving potential minimum cannot be tracked exactly from that initial state at finite stiffness. This does not exclude an isolated equality at half transfer under a specified potential, initial data and dynamics.

Both observations leave the native coupling rule open. Smooth incoming dynamics with continuous state and continuous vector field cannot change the derivative of \(f\) instantaneously from positive to zero at closure. The declared v0.25 hard switch can perform that cut with a changed evolution law. Stationarity of the smooth action family alone supplies no such event. Stage 2 remains open.

Run python3 replay_c06_variational_fold.py for exact rational first-branch witnesses with angles measured in closure units and an exact acceleration check at readiness. Stationarity follows from the analytic change of variables.
