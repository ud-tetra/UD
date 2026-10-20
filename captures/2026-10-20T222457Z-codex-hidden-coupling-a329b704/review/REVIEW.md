# C24 independent hidden/visible coupling review

The proposed results are sound with the explicit sampled-nullspace argument and the clarified distinction S=mean(sine squared), B=S/10. They concern a declared skew perturbation of a mathematical generator. They do not establish a native physical coupling law, a universal estimator guarantee or an acquisition result.

## General transfer and exact invisibility

Let X=V orthogonal-sum N, K be real skew, and ||P_V K P_N||<=epsilon. For a unit n in N, write exp(tK)n=v(t)+w(t), with r=||v||. Norm conservation gives ||w||=sqrt(1-r^2). The visible diagonal skew block contributes zero to the derivative of r^2, so wherever 0<r<1,

    r' <= epsilon sqrt(1-r^2).

Integrating the arcsine inequality up to first saturation, with the right-derivative/comparison interpretation at r=0, gives r<=sin(epsilon t) for 0<=epsilon t<=pi/2. Afterwards r<=1. Apply the same argument to -K for negative time, and rescale n. This proves the stated sin(min(epsilon|t|,pi/2)) bound, independent of diagonal-block magnitudes. The epsilon=0 case is exact invariance. A two-plane rotation attains the bound before saturation. Skewness is essential: a growing hidden diagonal block in a non-skew triangular matrix can amplify an arbitrarily small off-diagonal forcing beyond this bound.

Because the nominal A is skew, its invariant N is reducing. Any skew D supported on N leaves the visible block and all nominal R exp(t(A+D))x outputs unchanged, for every initial x. This allows 747*746/2=278631 hidden-block skew parameters without altering these outputs. It is an observation nonidentifiability result, not a claim that these parameters are allowed native chain laws. For the coordinate readout ||R||=1 and a readout perturbation E_t of norm at most eta, the hidden-initial-state output bound is (sinclip+eta)||n||. An arbitrary initial state or non-skew generator requires a different statement.

## Source-bound rank change and symmetry

The inherited source gives nominal history rank1893, hidden dimension747, stationary dark dimension1, and harmonic dimension2. Those ranks were not recomputed. This review reads only JSON from the pinned source archive and independently checks the fundamental oriented C3 cycle is closed, its 600 coefficients have unit magnitude, the signed action fixes it, and the uniform C0 vector is fixed. There are12 observed vertices and no C3 readout: ||Ru||^2=1/10 and Rh=0.

With E=epsilon(u h^T-h u^T), Ku=-epsilon h and Kh=epsilon u. On their plane, exp(tK)h=cos(epsilon t)h+sin(epsilon t)u; all other nominal modes are unchanged. If epsilon>0 and q(epsilon^2) is nonzero, the new signed frequencies do not coincide with any old observed frequency. Their two independent sine/cosine coefficients replace the one visible stationary coefficient. Thus the ideal history rank is1894 and the hidden space is the old N intersect h-perpendicular, dimension746. Arbitrarily weak admissible epsilon therefore changes exact rank; no positive uniform robustness margin follows from this rank change.

The signed C10 action fixes both u and h, so this particular E commutes with that action. The isolated m0 rank becomes256 and its hidden dimension8; other isolated ranks remain inherited. Their sum becomes2524, the individually dark sum116, and the mixed-sector dark quotient remains630. No generic cross-sector invariance follows for arbitrary K. E is odd under chain parity (it anticommutes with the parity involution); it does not preserve the even and odd state subspaces separately. Its dense C0-to-C3 coupling violates the native adjacent-degree Hodge–Dirac structure and supplies no locality, incidence/Pachner provenance or physical source law.

## Sampling and conditioning

A small ||Fh|| alone does not bound the smallest positive singular value unless h lies perpendicular to the sampled kernel. The missing condition is discharged here: this review independently rebuilds the displayed q factors against the authoritative JSON coefficients, verifies their pairwise coprimality and exact Sturm counts, and finds all52 distinct nonzero q roots strictly in (0,16). The104 old signed observed frequencies lie in(-4,4). For 0<epsilon<=2^-20 with q(epsilon^2) nonzero, adding the two signed epsilon frequencies gives106 distinct phases at spacing1/2, without aliasing. The first106 samples form a Vandermonde system separating frequency coefficients. Hence M>=106 yields the same kernel746 as the continuous history. Merely having enough samples without nonaliasing would not suffice: a two-plane rotation sampled at integer half-periods can hide its sine coordinate exactly.

For M4096, t_j=j/2, center c=4095/4, set h_e=cos(epsilon c)h-sin(epsilon c)u and u_e=cos(epsilon c)u+sin(epsilon c)h. Their output sines and cosines are centered; grid reflection makes the compressed two-plane Gram diagonal with entries S_c/10 and (1-S_c)/10. Both trial vectors lie perpendicular to the sampled kernel. Therefore

    sigma_min_positive(F_M) <= sqrt(S_c/10),
    kappa_positive(F_M) >= sqrt((1-S_c)/S_c).

These are full-map upper/lower inequalities respectively. A lower enclosure for the plane's weak singular value is not a lower enclosure for the full map's smallest positive singular value: other columns can couple in the full Gram matrix. The full2640-domain condition number is infinite because746 directions remain invisible.

Direct exact sums give v=5592405/16 and w=56294984157321/256. Taylor inequalities on the small centered arguments give epsilon^2 v-epsilon^4 w/3 <= S_c <= epsilon^2 v. Independent rational calculations and directed root endpoints agree with all three root cases:

| epsilon | Full-map sigma_min_positive upper, rounded display | Full-map kappa_positive lower, rounded display |
| --- | --- | --- |
| 2^-20 | 1.78295098040938e-4 | 1773.61979789920 |
| 2^-30 | 1.74116306680604e-7 | 1816186.96172366 |
| 2^-40 | 1.70035455742777e-10 | 1859775448.80531 |

Exact rational pairs and directed binary enclosures are authoritative; decimal entries are displays. This normalized62-channel state-observation map is distinct from a Hankel matrix, the321-column projected-record estimator and its2029 conditioning gate. No threshold is transferred between these operators.

The earlier S-versus-B normalization and parity wording were clarified before a frozen theorem was issued. No frozen mathematical retraction is needed. Development — no registry entry. No raw acquisition, archived script, SVD/fit or estimator execution. Source ranks remain inherited; no external physical review authority is claimed. External review PENDING. Physical Promotion = 0.
