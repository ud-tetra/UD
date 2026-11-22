# CYCLE-090 scope and PB3/PB5 memory-pole visibility

**Physical Promotion = 0.** The baseline is the pinned finite-carrier radial and exterior operators of [PR #605](https://github.com/ud-tetra/UD/pull/605) and [PR #606](https://github.com/ud-tetra/UD/pull/606). The PB4 comparison can use [PR #607](https://github.com/ud-tetra/UD/pull/607) after its independent review. Each operator result requires exact replay and independent review.

| Proof obligation | Acceptance criterion | Status |
| --- | --- | --- |
| Radial memory-pole visibility | Every rightmost stable pole of PB3 and PB5 is visible in the full matrix transfer for every radial coupling $g>0$, with zero exterior damping. Include repeated poles and identify any dark stable factors. | Constructor certificate below. Independent review pending. |
| Global PB5/PB3 ratio supremum | Prove or give a certified counterexample to $R(g)\le 5(10-\sqrt5)/57$ for all $g>0$. Account for each leading branch switch and certify the weak and strong tails and the compact interval between them. | Open. |
| Local-in-time resolved trajectory error | Declare the closure, initialization, norm, and horizon. Certify $\sup_{0\le t\le T}\|x(t)-x_{\rm loc}(t)\|$ using the full kernel or a certified multipole remainder. Track initial-slip, pole-truncation, and trajectory-propagation contributions. | Open. |

The approved all-coupling stable-gap comparison from PR #605 supplies $R(g)<1$. For the sharper supremum, the candidate is the exact weak-coupling limit. The ratio has an eventual upturn, as established in [PR #598](https://github.com/ud-tetra/UD/pull/598). Use an overshoot exclusion or sign bounds on certified subintervals. Keep stable-gap comparisons and resolved-trajectory errors distinct.

For the trajectory task, begin with the exterior-only closure at raw coupling 4 and prepared unresolved data $Qy(0)=0$. In unnormalized resolved coordinates, write $x'=A_Px+\int_0^t K(s)x(t-s)\,ds$, and define a candidate local generator $A_P+M_0$ with $M_0=\int_0^\infty K(s)\,ds$. The exact forcing defect of this replacement is
$$
d(t)=\int_0^t K(s)[x(t-s)-x(t)]\,ds-\left(\int_t^\infty K(s)\,ds\right)x(t).
$$
Bound the first term by the weighted kernel moment and a bound on $x'$. Keep the second term all the way to $t=0$, then propagate both by variation of constants. For general data include the unresolved initial forcing. Convert normalized-channel estimates to the norm used for $x$ before propagating them. The collective exterior channel has zero signed integral and a nonzero transient, so a small late-time tail gives no uniform trajectory certificate on its own.

## Exact PB3/PB5 transfer trace certificate

Let $H=Q(A-gS)Q$, with unit simplex coefficient metric and the radial edge projector $S$. Let $V$ contain the cell indicator columns, and $B=QAV$. The normalized or orthonormal-coordinate matrix transfer has the same poles as the unnormalized matrix $B^\mathsf T(zI-H)^{-1}B$ because the PB3/PB5 indicator Gram matrices are invertible. The overall Mori–Zwanzig sign has no effect on pole locations.

For each ring the replay verifies $D(H)B=0$ in exact polynomial arithmetic. The monic annihilators $D$ are $q_{24/5}p_3$ and $q_{40/7}p_5$, respectively, where $q_c=z^2+gz+c$, $p_3$ is the PB3 cubic, and $p_5$ is the PB5 sextic from PR #605. Expanding the matrix resolvent at infinity, the polynomial part of $D(z)\operatorname{tr}[B^\mathsf T(zI-H)^{-1}B]$ gives the scalar numerator up to a constant scaling. The exact annihilator clears the denominator of the full matrix, including at specialized coupling values. If the scalar trace has a pole, at least one transfer entry has that pole. This argument covers repeated roots by their pole order and avoids a choice of individual eigenvector inside a repeated eigenspace.

With numerator scaling 5 for PB3 and 7 for PB5, the exact resultants against the two denominator factors are

| Ring | Against $q_c$ | Against $p_n$ |
| --- | --- | --- |
| PB3 | $576F_3/25$ | $1728g^4F_3$ |
| PB5 | $259200F_5/16807$ | $-256000000g^{10}F_5$ |

Here $F_3=75g^2+4$ and $F_5=213689g^4+769300g^2+9680$. They are strictly positive for $g>0$. Consequently the trace and full transfer have exactly the stated pole denominator for every positive coupling. The remaining stable factors from [PR #597](https://github.com/ud-tetra/UD/pull/597) have no additional poles in the transfer.

For PB3, parameterize the cubic real root as $-r$, so $g=r(r^2+5)/(r^2+2)$ and the complex pair has real part $-3r/[2(r^2+2)]$. The cubic discriminant is strictly negative and the coupling map is strictly increasing. The replay checks that both PB3 quadratics lie strictly left of the complex pair by shifted Hurwitz minors. For PB5, the hidden quartic and $q_7$ are strictly Hurwitz after shifting by the separator $11g/[10(g^2+4)]$. The reviewed PR #605 certificate places a sextic root strictly to the right of that line before translation. Thus the dark stable factors cannot determine either ring's stability gap.

**Constructor result.** For PB3 and PB5 at every $g>0$ with zero exterior damping, every rightmost stable pole is present in the memory transfer. The exponential memory decay rate in each ring equals its stable gap, with pole multiplicities allowed to contribute polynomial time prefactors. The proof certifies pole visibility at the transfer level. It does not assign nonzero overlap to every eigenvector in a repeated eigenspace.

Run `python3 replay_visibility.py` with SymPy and compare stdout with `replay-results.txt`. Independently check the exact matrix annihilators, numerator construction, resultants, and placement of hidden stable factors.
