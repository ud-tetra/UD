# C06 binary matching fiber as an event clock

**EXACT / CONDITIONAL** for the coordinate-permutation action on the stated binary fiber. **NO-GO** for selecting the two-stage exchange from the fiber and symmetry alone. **Physical Promotion = 0.**

## Event parity and symmetry

Let \(\Theta=\mathbb F_2^3\), one coordinate per opposite-edge matching, with the \(S_4\) relabeling action through \(S_3\) permuting coordinates. The fixed states of this action are \(000\) and \(111\). The only nonzero invariant linear observable \(\Theta\to\mathbb F_2\) is the parity
\[
p(\theta)=\theta_1+\theta_2+\theta_3 .
\]
Indeed, a linear functional invariant under the coordinate swaps must have three equal coefficients. For the closure update supplied in [C06 v0.7](https://github.com/ud-tetra/UD-Physics/pull/410),
\[
\theta'=P_g\theta+\xi,\qquad p(\theta')=p(\theta)+p(\xi),
\]
where \(P_g\) here denotes the permutation of the three matching coordinates and addition is XOR. Consequently parity records the parity of the number of odd-weight flip receipts. A one-coordinate flip toggles it; an even-weight flip and a frame permutation leave it unchanged. This gives a two-phase clock **conditional on receipt of odd-weight events**. It supplies no receipt on its own.

## Autonomous reversible clocks

Under the stated \(S_3\) action there are two fixed points and two three-point orbits, of weights one and two. An equivariant bijection may independently swap the two fixed points and the two three-point orbits. On a three-point orbit the stabilizer of a point fixes just that point within the orbit, so its equivariant self-map is the identity. Complement gives the unique equivariant bijection between the two three-point orbits. Thus exactly four equivariant bijections exist. Their orders are one or two. Among translations \(\theta\mapsto\theta+v\), equivariance requires \(v=000\) or \(111\), making global complement the only nonidentity translation. Symmetry also admits the identity and a reversible update that leaves both fixed states unchanged while swapping the three-point orbits.

Neither an elementary one-coordinate step from a symmetric state nor a two-step stop can be obtained from an autonomous reversible equivariant rule on this fiber alone. A deterministic equivariant map takes a fixed point to a fixed point, and the two fixed points differ in three coordinates. An autonomous reversible orbit is periodic; it cannot reach a distinct absorbing done state. Complement can serve as a toggle if declared, but differs from a supplied single-coordinate flip and repeats indefinitely. Phase initialization and stopping require separate conditions.

## Link to the exchange

A controller can declare that odd-weight transitions out of even parity fire the direct transfer and odd-weight transitions out of odd parity fire the matching transfer, then latch after the second eligible receipt. No such assignment, latch, or quantitative transfer fraction follows from the parity identity. In the [staged exchange](https://github.com/ud-tetra/UD-Physics/pull/408), a direct fraction \(f\) followed by complete transfer of the remaining pair-even amplitude gives record gains \(1,f\) in the even and odd edge sectors. The same binary history is compatible with \(f=1/2\) or \(f=1/4\), giving ratios two or four. Exact shear equalization for complete matching transfer requires \(f=1/2\) from the real record objective. This separates timing eligibility from transfer selection.

The [graph projector](https://github.com/ud-tetra/UD/pull/532) on unsigned edges is outside the span of the signed Hodge cut and cycle projectors, since its disjoint-edge entries are nonzero. This is an algebra-membership claim. It has Hilbert–Schmidt inner product \(3/2\) with each signed Hodge projector in the fixed signed edge basis: only the half-diagonal contributes, and each projector has trace three.

The exact replay enumerates the equivariant reversible maps, checks the receipt identity, and verifies the transfer witnesses and matrix overlaps. It uses the declared coordinate-permutation action and does not assert an endogenous source law for \(\xi\).

**Claim boundary footer:** Physical Promotion = 0.
