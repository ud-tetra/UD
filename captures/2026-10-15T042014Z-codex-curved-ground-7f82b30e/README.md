# Stable nonzero curved matter orbit v0.1

The unchanged candidate action admits U_e=-i b_e, E=0, psi=chi=sqrt(N)v, where v is the normalized strictly positive eigenvector of the unsigned Hasse adjacency T with rho=sqrt(8+2sqrt(10)). Every diamond holonomy is -1. The branch evolves only by the common phase rate mu-rho.

For scalar rank r=1, constrained energy proves nonlinear orbital stability for a>0 and 0<=kappa<N*rho*(10-sqrt(10))/(120*(6+sqrt(2))). At zero stiffness this is the unique constrained global minimizing orbit. This is a sufficient interval, not a sharp transition.

Separately, for every finite rank the fixed-norm Gauss-admissible global minimizing set is nonempty, compact, invariant and stable as a set. It contains no flat state when kappa/(r*N)<(rho-2)/18. This does not identify individual minimizers or prove higher-rank stability of the scalar embedding.

Read `UD_CURVED_GROUND_STABILITY_THEOREM_v0.1.pdf`; TeX supplies the proof. Run `python3 verify_curved_ground.py` with SymPy, NumPy and SciPy to reproduce 40 exact checks and two separately typed full nonlinear numerical campaigns. The graph constructor is inherited unchanged. Candidate action, independent review pending, no experimental data, physical promotion 0.
