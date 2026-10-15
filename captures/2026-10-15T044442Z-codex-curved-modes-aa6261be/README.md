# Curved scalar reduced modes and sharp stability boundary v0.1

The unchanged negative-holonomy branch has 84 physical real dimensions at fixed equal species norms and after gauge/common-phase reduction. Its linear dynamics splits into 14 neutral matter oscillator pairs and 28 link-charge pairs. Exact 3-, 5-, 2- and 2-dimensional symmetry-section pencils, with irrep multiplicities, specify every charged frequency.

The sharp scalar boundary is kappa_star=4N*w0/Lambda_plus, w0=rho*(10-sqrt(10))/480, rho=sqrt(8+2sqrt(10)), Lambda_plus=(28+17sqrt(10)+sqrt(866-128sqrt(10)))/18. The orbit is nonlinearly stable for 0<=kappa<=kappa_star, and unstable above it, for each a>0,N>0. kappa_star/N is about 0.03760248457, strengthening the old conservative 0.02908745325.

At equality, three length-two zero Jordan chains do not imply nonlinear instability. The energy minimized over matter shape has a positive critical quartic. Its two symmetric coefficients satisfy exact integer interval bounds 11<A4<12 and 12<B4<13. Full derivation is in `UD_CURVED_REDUCED_MODES_THEOREM_v0.1.pdf` and TeX.

Run `python3 verify_curved_modes.py` with SymPy, NumPy and SciPy. It performs 47 exact checks including the exact integer interval certificate, four separately typed numerical linear benchmarks, and three full nonlinear trajectory campaigns. `MODE_BLOCKS_v0.1.json` stores all exact mode matrices and reconstruction bases. No hardware or experimental data, no physical promotion, no independent review. Additional color modes at r>1 remain open.
