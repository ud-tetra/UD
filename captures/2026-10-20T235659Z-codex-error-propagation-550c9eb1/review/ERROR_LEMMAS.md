# Deterministic observation and reconstruction bounds

Let F be the fixed PR307 normalized sample map, with K skew, ||K||<5, coordinate readout ||R||=1, and t_j=j/2, j0..4095. Let P project onto its1999-dimensional observable subspace and C=27648/61. The inherited certificate gives F-dagger F=P and ||F-dagger||<C.

Take a constant real skew K'=K+Delta, ||Delta||<=xi. Write U_j=exp(t_j K) and U'_j=exp((t_j+theta_j)K'). Assume ||E_j||<=rho_j, |theta_j|<=eta_j, ||x||<=X and ||pvec||<=p. Define actual samples as

    y_j=(R+E_j)U'_j(x+pvec)+n_j+codec_j.

All aggregate sample vectors below have normalization1/sqrt4096. Their norm is the RMS of the per-sample Euclidean norms. If the normalized n and codec vectors have norms at most nu and enc, no independence assumption is needed.

Orthogonality and Duhamel give

    ||U'_j-U_j||<=t_j xi+(5+xi)eta_j.

For example split the difference into exp(theta_j K')exp(t_j K')-exp(t_j K') and exp(t_j K')-exp(t_j K). The first term is bounded by |theta_j| ||K'||; the second by t_j||Delta||. This remains valid for negative clock offsets, since the skew propagators are isometries for all real times. Also ||U'_j-U_j||<=2. Put

    b_j=rho_j+min(2,t_j xi+(5+xi)eta_j),
    b=(mean_j b_j²)^(1/2).

The readout mismatch operator is R(U'_j-U_j)+E_j U'_j, whose norm is at most b_j. Since

    y-Fx=F pvec + stack_j [R(U'_j-U_j)+E_jU'_j](x+pvec)/sqrt4096 +n+codec,

we obtain the deterministic bound

    ||y-Fx||<=delta_y=p+(X+p)b+nu+enc.

A simpler conservative envelope is

    b<=rho_rms+T_rms xi+(5+xi)eta_rms,
    T_rms²=11180715/8<2048².

The clipping is optional. Preparation is multiplied by the mismatch too: replacing X+p by X would omit a genuine mixed term. Errors may add coherently, so an independence-free proof uses triangle/Minkowski bounds, not an unjustified root-sum-square across different sources.

The ideal nominal reconstruction obeys

    ||F-dagger y-Px||<=C delta_y.

This inequality is safe also when delta_y=0. A strict less-than follows from ||F-dagger||<C only if delta_y>0. It does not recover (I-P)x. Perturbed hidden dynamics can contribute to y and therefore to a nominal model mismatch.

For a specified implemented linear estimator B with ||B||<=beta and ||BF-P||<=alpha on the complete state space, and an arithmetic/implementation output bound eps_alg, one has

    ||computed_estimate-Px||<=alpha X+beta delta_y+eps_alg.

Conditioning of F alone gives neither alpha nor beta nor eps_alg for a floating implementation. These must be independently verified for its actual coefficients, input convention and arithmetic path. A test on a finite set of preparations is not a full operator defect bound.

## Clock decomposition

If theta_j=b0+a t_j+zeta_j, then

    eta_rms<=|b0|+|a|T_rms+zeta_rms.

For the affine component alone the exact RMS squared is b0²+2b0*a*mu+a²T_rms², with mu=4095/4. In centered form put bc=b0+a*mu; then its squared RMS is bc²+a²v, where v=(4096²-1)/48. Thus an often tighter valid bound is sqrt(bc²+a²v)+zeta_rms. Arbitrary jitter need not be orthogonal to the affine clock component. Relative drift a is dimensionless; its timing contribution grows across the grid and is not simply |a|.

## Stable nominal quotient, without hidden quarantine

Let Ftilde be the actual noiseless map before preparation error, and assume ||Ftilde-F||<=b. On the fixed nominal observable subspace,

    sigma_min(Ftilde restricted to range(P))>s-b,
    ||Ftilde restricted to range(P)||<=1+b,
    s=61/27648.

For b<s this proves injectivity on that subspace and a condition upper (1+b)/(s-b). It does not prove the perturbed complete map still has rank1999 or the same kernel. Weyl supplies sigma_1999(Ftilde)>s-b and every new singular value beyond1999 at most b, but any of those values may become positive. An arbitrarily weak coupling can expose nominal hidden directions. A bound on generator perturbation alone is not a proof of preserved hidden-space invariance.

All quantities are typed mathematical error inputs in the declared model units. No actual error sizes, acquisition, physical clock, physical constitutive law or floating estimator are supplied here. Development — no registry entry. Same-team review, external review PENDING, Physical Promotion=0.
