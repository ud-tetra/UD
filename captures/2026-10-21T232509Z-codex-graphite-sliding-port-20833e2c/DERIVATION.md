# Relative-layer sliding port and conservative memory

Development — no registry entry. Physical promotion 0. Constructor: Codex. Non-constructor reviewers: none. This is conventional harmonic elimination, not a native UD identification.

## Coordinates and force units

For N equal-mass atoms with equal layer populations, let sigma=+1 for type 2 and -1 for type 1. T_x=(sigma/sqrt(N),0,0), T_y=(0,sigma/sqrt(N),0). The qualified internal orthonormal basis B has zero mean x/y separately in each layer and zero global mean z. E=[B,T] is orthonormal and removes only the three global translations from the primitive-periodic coordinate family. It does not span every supercell fluctuation.

Write atom displacement Bq+Tr. The relative layer displacement is delta=2r/sqrt(N). Virtual work gives F_delta=sqrt(N) F_r/2; stiffness and memory in delta coordinates are N/4 times their r-coordinate counterparts. The corresponding kinetic mass is N*m_C/4 for delta, m_C for normalized r. Force signs here are external forces required to hold/drive, opposite the potential force.

Expand potential at the held registry: U=U0-b_q^T q-b_r^T r+(q^T H q+2q^T C r+r^T P r)/2. The measured b_r need not vanish. The harmonic perturbation equations subtract baseline forces; the external clamp supplies -b_r. Residual b_q is reported, and the numerical linear model centers it to zero. Internal H is SPD; the extended matrix and relaxed port stiffness S need not be SPD.

## Exact conditional elimination

Normalize H,C,P by h*=lambda_max(H), calling them A,D,V. Time tau absorbs a common mass and h*; no native UD clock is identified. For prescribed r(tau), the internal equation is q''+Aq+Dr=0. Define S=V-D^T A^-1 D and K(t)=D^T A^-1 cos(sqrt(A)t)D. Then the required baseline-subtracted drive is

F(t)=r''(t)+S r(t)+integral_0^t K(t-s)r'(s)ds+j(t),

j(t)=D^T cos(sqrt(A)t)[q0+A^-1 D r0]+D^T A^-1/2 sin(sqrt(A)t)v0.

Unlike the internal-coordinate equation's right-hand source, j has a plus sign because this is required external force. The formula retains the initial-slip contribution +K(t)r0. Baseline physical drive is -b_r+h*F; multiply by sqrt(N)/2 for force conjugate to delta. The r'' term assumes the same common atomic mass used in tau. For a massless imposed clamp, report only F-r'' as potential reaction.

If A=U diag(alpha) U^T and G=U^T D, K=sum_j g_j g_j^T cos(sqrt(alpha_j)t)/alpha_j. Spectral weights are PSD, but K(t) need not be pointwise PSD. The finite kernel is reversible and oscillatory. It does not supply a steady friction coefficient or a thermal reservoir.

Memory realization: a'=G r'-sqrt(alpha)b, b'=sqrt(alpha)a, a(0)=b(0)=0; convolution=G^T(a/alpha). Initial source is evaluated separately. Full reference integrates q,q' directly under the prescribed path. Both methods use the same frozen harmonic coefficients; this is a consistency check, not independent replication or a test against nonlinear driven atomistic motion.

## Numerical scope

Two new port columns plus nine internal directional reciprocity probes per case. All stencils use the prior every-stencil branch/roundoff guard. The nine probes do not independently remeasure every internal-to-port entry. Previous internal H is reused with hashed provenance. No response-adaptive step choice. The prescribed path has r0=0; nonzero-r0 initial-slip behavior is derived here but not covered by these driven numerical tests.

No UD-specific mechanism, clock, bath, experimental friction or promotion is inferred. A distinguishing UD hypothesis still requires a source-derived correspondence and a prediction beyond conventional harmonic response.
