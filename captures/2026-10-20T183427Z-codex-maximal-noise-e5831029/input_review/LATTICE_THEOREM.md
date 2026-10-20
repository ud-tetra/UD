# Exact alphabet for the frozen quantized noise ball

Development — no registry entry. Physical Promotion=0; external promotion review PENDING.

Let the additive computational perturbation of a single 62-channel observation be `e=q k`, where `q=2^-48` and `k` is an integer vector. The original fixed protocol radius is `δ0=3*2^-49=(3/2)q`. This theorem concerns additive encoded perturbations only; it is not an empirical noise law.

**Theorem.** `||e||2 <= δ0` holds if and only if `k` has zero, one, or two nonzero coordinates, and every nonzero coordinate equals +1 or −1. The full per-vector alphabet contains exactly 7,689 states. Its maximum encoded norm is `sqrt(2) q`, strictly below the continuous ball radius.

**Proof.** The inequality is equivalent to `sum_j k_j² <= 9/4`. The sum is a nonnegative integer, so this is equivalent to `sum_j k_j² <= 2`. Any coordinate with magnitude at least 2 contributes at least 4 and is excluded. All remaining nonzero coordinates have magnitude 1 and contribute one unit each, so at most two can be nonzero. Conversely, all such sparse vectors have squared norm 0, 1, or 2 and satisfy the inequality.

There is one zero vector, `2*62=124` signed one-coordinate vectors, and `4*binomial(62,2)=7,564` signed two-coordinate vectors. Hence the total is `1+124+7,564=7,689`. Two unit coordinates attain squared norm 2. Since `2<9/4`, the maximum squared ratio to the frozen radius is exactly `8/9`. A single coordinate of size 2q and three distinct coordinates of size q are both outside the ball.

The two prospective campaign recipes attain this maximum encoded amplitude in every observation vector. They sample two deterministic histories; they do not enumerate all assignments of the alphabet across a complete record. With independently selectable perturbations at 303,067 vector positions, there are symbolically `7689^303067` assignments. No universal estimator success, whole-trajectory conditioning, floating backend guarantee, physical freshness, or physical accuracy follows from the per-vector classification or from two successful cases.

`review_data.py --lattice-only` independently constructs every canonical sparse alphabet element, checks uniqueness and exact cardinalities by squared norm, checks the rational ball inequality, and exhaustively corroborates the classification in dimension 4 on all 625 integer vectors with coordinates from −2 to 2. The analytic sum-of-squares argument, rather than that smaller cross-check, supplies the dimension-62 proof. Numerical protocol constants are O03 controls and are not promoted to UD theory constants.
