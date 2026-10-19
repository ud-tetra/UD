# Phase admission through the retained singular equation

Development — no registry entry. Physical Promotion = 0. External nonconstructor review PENDING. Post-known-outcome deterministic mathematical refinement; no new data, fit, or numerical backend success claim.

## Source and units

The source is exclusively the original encoded synthetic baseline with SHA-256 `25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59`, unfolded to 8191 by 2294 and multiplied by the unchanged fixed 2294 by 321 sketch S. Arbitrary additive E satisfies a Euclidean norm bound delta per preparation/sample 62-vector. The inherited exact sketch proof gives ||ES||_2 <= C delta, C <= 597.1110560985338. Let Z = Z0 + ES and let Zbar have rank 209, range W0, and ||Z0-Zbar||_2 <= r. W0 is an exact orthonormal frame. All source approximation, shift and normal-reduction residuals remain explicit inherited premises. Source hashes are pinned in SOURCE_BINDINGS.json. They are not newly independently rederived here.

All phase errors are radians per TWO-step sample, modulo 2 pi. Primitive frequencies remain aliased modulo pi. None of these quantities is an SI time or a six-ratio calibration error.

## Theorem 1 — equation residual controls the retained subspace

Let U in R^(8191 x 209), V in R^(321 x 209), Sigma = diag(s1,...,s209) with every si >= s_* > 0, and

    F = Z V - U Sigma.

Suppose ||F||_2 <= xi, ||U^T U-I||_2 <= etaU < 1, ||V^T V-I||_2 <= etaV < 1. Set R_U = (U^T U)^(1/2), Q = U R_U^-1, e = r + C delta, and P0 = W0 W0^T. Then

    ||(I-P0)Q||_2 <= t = [ e sqrt(1+etaV) + xi ] / [ s_* sqrt(1-etaU) ].

Proof: (I-P0)Zbar=0. Hence (I-P0)U Sigma = (I-P0)(Z-Zbar)V - (I-P0)F. Multiply on the right by Sigma^-1 R_U^-1. The right product need not commute. Its norm is bounded by the product 1/(s_* sqrt(1-etaU)); ||V||_2 <= sqrt(1+etaV). Every matrix product is dimensionally defined. No approximation Z ~= U Sigma V^T, no omitted left singular columns, no right polar correction, and no discarded-tail smallness is needed.

If t<1, equal-dimensional principal-angle theory supplies a right orthogonal O with

    ||Q O-W0||_2 <= d = sqrt(2-2 sqrt(1-t^2)).

This is solely an admission implication. The tuple must actually satisfy the displayed measured premises. The source cutoff alone does not establish the proposed s_* floor, and Weyl's theorem for exact data singular values does not certify arbitrary returned si.

## Theorem 2 — retained lag and eigenpair implication

Retain the PR252 source constants beta, sigma0, M0, eta0, hD, dD, LJ, and source minimum-chord lower bound sep. Define +/- by deleting first/last two rows. For returned T satisfying ||U_+ - U_- T||_2 <= sA, let T_Q = R_U T R_U^-1. Then

    Q_+ - Q_- T_Q = (U_+ - U_- T) R_U^-1,

so its norm is at most sA/sqrt(1-etaU). If beta>d, the aligned shift differs from the saved source comparison by at most

    b = [sigma0 + sA/sqrt(1-etaU) + d(1+M0)] / (beta-d).

The source comparison is not assumed to be the exact least-squares solution. Its sigma0 term remains.

For complex square V_e,H,Lambda with ||V_e H-I||_2 <= rho<1, ||H||_2<=h, ||T V_e-V_e Lambda||_2<=eV, the exact inverse of V_e exists and the correction T -> V_e Lambda V_e^-1 has norm at most Delta=eV h/(1-rho). The polar conjugation costs kappaA=sqrt((1+etaU)/(1-etaU)). The source polar/reference conjugation costs kappa0=sqrt((1+eta0)/(1-eta0)). Thus the proposed eigenvalues are the eigenvalues of a perturbation of the fixed normal target matrix J bounded by

    R = hD LJ + kappa0 hD dD (b + kappaA Delta).

The inherited hD includes the source inverse-residual debit. If R<1 and 2R<sep, homotopy-resolvent counting in disjoint target disks proves exactly one eigenvalue, counting algebraic multiplicity, per target. If emitted angles differ in circular distance by at most a from the arguments of the nonzero proposed eigenvalues, and 2(asin R+a)<sep, their target-label pairing is bijective with error <= asin R+a. Mere nearest-target inclusion is insufficient for the counting assertion. This certifies emitted phase admission, not the exact spectrum of saved T without its own forward proof.

## Protocol caps and finite instantiation

This new protocol uses etaU,etaV <= 2^-43, xi <= 2^-41, sA <= 2^-34, rho <= 2^-40, h <=128, eV <=2^-42, a <=2^-50. The numerical equality xi_cap = the old approximation cap does not identify the residual objects. These are O03 controls, not theory constants.

The independently measured singular-value premise is

    min_i si >= s0 - C delta - 2^-41 > 0.

The subtraction 2^-41 is a conservative protocol debit; no conclusion from a discarded tail is hidden in this requirement. The code records this floor as a required gate, not a guaranteed consequence of exact-cutoff preservation. At delta=3*2^-49 the theorem passes the unchanged phase boundary with strictly positive margin. Exact encoded 62-vector perturbations in this closed ball have integer squared norm at most 2 (zero, one +/-q coordinate, or two distinct +/-q coordinates), q=2^-48. The same local pattern classification extends to delta^2<3q^2. This does not prove a numerical library will return a tuple meeting these caps on every input.

## Theorem 3 — full-factor receipts can qualify this equation without charging the tail

For an already saved complete 321-column tuple Uf,Sigmaf,Vf with residual Rf = Z-Uf Sigmaf Vf^T, write V=Vf[:, :209], U=Uf[:, :209], Sigma=Sigmaf[:209,:209], and let Jr select the first 209 coordinate columns. Exactly,

    Z V-U Sigma = Rf V + Uf Sigmaf (Vf^T V-Jr).

Therefore

    xi <= ||Rf||_2 sqrt(1+etaRf) + sqrt(1+etaLf) smax etaRf.

If Rf was certified against an approximate sketch, add its projection-error upper bound inside the first factor. Principal compressions give the retained Gram bounds from their full-factor counterparts. No sigma210 or discarded-tail norm appears. The supplementary calculation instantiates this implication using the previously certified nonzero one-quantum cyclic record; it reads only small metadata from a pinned archive. It inherits the full-factor receipt rather than rerunning its arithmetic, and does not admit a new output or all input records.

## Why this does not repair a failed reconstruction gate

Take Z=diag(3,1), U=V=(1,0)^T, Sigma=(3). The retained singular-equation residual is zero, while the best rank-one reconstruction error is 1. A larger observed sigma210 can refute an overly strict rank209 approximation gate even when the retained singular equation is perfectly satisfied. This is a difference in theorem premises, not a revised verdict for the old gate. Conversely U=V=(0,1)^T, Sigma=(1) also has zero equation residual but can fail a required source-scale singular floor; equation residual alone is not adequate.

## Frontier

No universal actual floating-solver success, PR233 whole preparation family, PR250 new-output admission, strict-frame success, full old eight-gate success, hidden-state recovery, physical calibration, source-law or physical-identification result is asserted. A reconstruction-gate counterexample does not imply a phase failure. All failed gate verdicts remain append-only. Fresh external calibration/acquisition/model and confirmatory lineage remain HOLD.
