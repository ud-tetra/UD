# C06 boundary impedance and hard drive constraint v0.25

**EXACT / CONDITIONAL** for the declared static positive loading model and hard projection. **CANDIDATE** for a face-saturation law that changes the drive constraint at balance. **Physical Promotion = 0.**

## Finite positive loading

On the mean-zero carrier \(X=E\oplus T_2\), use the v0.23 unsigned face sum \(H\), so \(H^\mathsf TH=2P_-\). The v0.24 face complement makes no difference on \(HX\subset\mathbf1^\perp\). Test the declared quasistatic series loading law with eliminated drive \(d\):
\[
x=(I_X+H^\mathsf T W H)d,\qquad G_Wx=Gd.
\]
Here \(W\) is any bounded positive semidefinite face weight. The chosen law represents an algebraic model of passive positive loading. It supplies no constitutive rule for \(W\) or a physical impedance scale. Keep the declared Whitney port metrics and set carrier and record velocities by \((-G_W^\dagger y,G_W x)\).

The loading matrix is positive definite, identity on \(E\), and preserves \(T_2\). Its inverse has odd eigenvalues at least \(1/(1+2\|W\|)>0\). Since the original \(G\) is injective on \(X\), finite weights cannot produce odd blockade. In the uniform case \(W=\lambda I\), \(G_W=G(P_++P_-/(1+2\lambda))\). The odd exchange rate becomes \(\omega_-/(1+2\lambda)\). Switching to this law at half stock leaves normalized balance growing at rate \(2\omega_-/(1+2\lambda)\) immediately after the switch. If the uniform loading varies, the remaining odd phase increment is \(\int \omega_-/(1+2\lambda(t))\,dt\). This result is scoped to the specified positive, memoryless series loading. Dynamic or resonant constitutive laws require separate tests.

## Hard constraint on the drive

Instead choose \(d\) to minimize \(\tfrac12\|d-x\|^2\) subject to \(Hd=0\). The unique drive is
\[
d=P_+x,\qquad G_{\rm hold}x=GP_+x.
\]
With a Lagrange multiplier in the mean-zero face space, \(d=x-H^\mathsf T\eta\), \(HH^\mathsf T\eta=Hx\), and \(\eta=Hx/2\). This uses the complementary face channel and the exact incidence eigenvalue. Imposing any three face constraints already forces \(Hd=0\) by the sum-zero relation. Two or fewer leave a nonzero odd drive direction. This projection is also the limit of the uniform positive loading as \(\lambda\to+\infty\).

The constraint acts on the *drive* rather than projecting the stored state at balance. Keep an identity amplitude reset and use the adjoint of \(GP_+\). Under the previous orthogonal record-range condition this freezes both odd registers, leaves even exchange active, and conserves total stock. A candidate transition is a shared Ready-to-Hold event initiated by the first qualifying face receipt under the common-phase preparation. It activates the full independent constraint set at that instant. The incidence identities establish the response of a prescribed hard constraint. They do not derive why the face crossing activates it. The ledger Q156 audit conditions hard gating on closure receipts and transport integrity, and supplies no such face-saturation rule. Native same-event authority, the trigger interface, and Stage 2 remain open.

## Scope corrections to v0.24 discussion

On all six ordinary edges \(H^\mathsf TQH=\mathbf1_6\mathbf1_6^\mathsf T\) for \(Q=\mathbf1_4\mathbf1_4^\mathsf T/4\). The coefficient on that outer product is one. Its orthogonal compression to \(X\) vanishes. The prior no-go concerns scalar mediation and this common-face channel, leaving room for a cell that directly accesses independent face channels.

Run python3 replay_c06_impedance.py for exact positive-weight bounds in the uniform case, odd-drive residuals, all face subsets and the hard projector.
