2026-10-02, America/Chicago. Development lane. Constructor: Codex. Independent review: pending. Internal claim bin: CANDIDATE_DEVELOPMENT_MATHEMATICS. Correspondence status: NOT_PROPOSED. Physical promotion: 0.

A direct counterexample on a cube subdivision rules out an unrestricted map from every native real-cell crossing to a discrete SA-TIME-014/015 commit while preserving cell identities and cumulative counts at every corresponding prefix. Three cells cross twice while three others never cross in the same interval. The discrete source requires cells sharing a vertex to differ by at most one commit.

This narrows the proposed bridge. It does not rule out cubic geometry, the discrete source itself, selected preparations or a separately declared event filter. It shows that a geometric carrier and a compatible event law must be admitted separately.

## Source contract and observation scope

The current returned version9 of UD_SPACETIME_PROOF_MANUSCRIPT.tex was read at the SA-TIME-014 preparation/commit guards and Proposition 77, the compatible count profiles and Proposition 78, and SA-TIME-015's request/acknowledgment implementation and Proposition 81. Exact excerpt text, line ranges and returned versions are retained in the source packets.

The native real-amplitude equations use the already inspected collective-closure note in the October2 gap-inventory release: u'=B3^T f, f'=-B3 u in the closed face–cell sector, with B2 B3=0. Its complete note and original archive identity are retained. These are unit simplex norms; they do not use physical lengths, Euclidean volume weights or SI time.

The target map tested here starts counts at zero at the beginning of the chosen interval. It must associate each completed native cell crossing with one commit of that same cell, introduce no extra commits, and preserve per-cell cumulative counts at every corresponding prefix. Arbitrary vertex preparations and implementation coordination may occur between commits. Those silent operations cannot evade the source count invariant.

## A supplied cube carrier

Label the eight vertices by their binary coordinates, with label x+2y+4z and x,y,z in {0,1}. This labeling is newly declared for this test and does not infer labels from the user's sketch. Take these six tetrahedra:

| Cell | Vertex labels | Alternating mode sign | Crossings in the test interval |
|---|---|---|---|
| C0 | 0 1 3 7 | +1 | 2 |
| C1 | 0 1 5 7 | -1 | 0 |
| C2 | 0 2 3 7 | -1 | 0 |
| C3 | 0 2 6 7 | +1 | 2 |
| C4 | 0 4 5 7 | +1 | 2 |
| C5 | 0 4 6 7 | -1 | 0 |

Each tetrahedron is the coordinate-order region associated with one permutation of the three axes. These six regions partition the unit cube, meeting on common boundaries. Coordinate permutations make them congruent. Each has geometric volume1/6 and squared edge lengths 1,1,1,2,2,3. They are not regular tetrahedra. This is one exact cube subdivision, not a minimum-count or uniqueness theorem, and it does not confirm seven congruent regular tetrahedra.

Orient each tetrahedron coherently in the cube. The exact boundary matrices have 18 faces and 19 edges and satisfy B2 B3=0. With unit simplex norms, the cell Gram matrix is:

```text
G = B3^T B3 = 4I - Adj(C6).
```

Here C6 is the cycle of face-sharing tetrahedra, in cyclic order C0,C1,C4,C5,C3,C2. Its Gram eigenvalues are 2 once, 3 twice, 5 twice and 6 once. Thus its native cell frequencies are sqrt2, sqrt3, sqrt5 and sqrt6, with those multiplicities. These are mathematical source values, not laboratory frequencies.

The discrete source's overlap graph is different: it includes vertex sharing. Every tetrahedron contains vertices0 and7, so that graph is K6. The counterexample also violates the count bound on a face-sharing pair; it does not depend only on the broader overlap definition.

## Exact native trajectory

Let e=(1,1,1,1,1,1) and v=(1,-1,-1,1,1,-1). Exact incidence calculation gives Ge=2e and Gv=6v. The following is a valid closed-sector native solution:

```text
u(s) = e cos(sqrt2 s) - 2v cos(sqrt6 s)
f(s) = -B3 e/sqrt2 sin(sqrt2 s)
       +2 B3 v/sqrt6 sin(sqrt6 s).
```

It satisfies both native equations, and its lower-degree coordinates can remain zero because B2 f=0. At s=0, f=0 and u=e-2v; its conserved support is30. It uses two nonzero modes and no static top mode. The coefficient2 is a declared preparation, not a fitted source-law coefficient.

Set T=pi/(2sqrt6) and observe from s=-T to s=T. At both endpoints, every cell is strictly positive, because the high-frequency cosine is zero and the low-frequency phase is pi/(2sqrt3), strictly between zero and pi/2. Thus the observation starts away from a root, with a common incoming sign reference.

For cells with v=+1:

```text
u_minus(s) = cos(sqrt2 s) - 2cos(sqrt6 s).
```

This even function is negative at zero and positive at both endpoints. On (0,T), its derivative is -sqrt2 sin(sqrt2 s)+2sqrt6 sin(sqrt6 s)>0: both angles lie in (0,pi/2), the higher angle has the larger sine, and its positive coefficient is larger. There is exactly one transverse root on (0,T), and evenness gives exactly one on (-T,0).

For cells with v=-1, u_plus=cos(sqrt2 s)+2cos(sqrt6 s) stays strictly positive throughout the interval. Its first term is strictly positive and its second is nonnegative. It has no roots.

The completed crossing counts are therefore exactly (2,0,0,2,2,0). They follow from analytic inequalities, not a sampled root search. The exported plot illustrates these equations; its curve samples and numerical marker positions are not the proof.

## Why the discrete source cannot match

Proposition77 gives the initialized history invariant:

```text
0 <= M_i - N_c <= 1 whenever vertex i belongs to cell c.
```

M_i counts vertex preparations and N_c counts cell commits. Sharing a vertex forces |N_c-N_d|<=1. SA-TIME-015 implements the same source guards through local certificates, so coordination and extra acknowledgment steps do not weaken this constraint.

After the first native root batch, counts are (1,0,0,1,1,0), which is compatible. After the second they are (2,0,0,2,2,0), which is not. For shared vertex0, a twice-committed cell requires M_0>=2 while a zero-committed cell requires M_0<=1. No vertex preparation count satisfies both. This contradiction is independent of scheduling, recorder width and recording speed.

The exact replay additionally enumerates the initialized source's bounded count lift through coordinate counts2: 1372 states and 4976 transitions. The incompatible target is unreachable. The integers in this enumeration are history bookkeeping whose parities project to the binary source; they are not extra protocol registers. The analytic invariant provides the unrestricted impossibility argument, beyond this finite enumeration.

## What can change the conclusion

Restricting the admitted preparations or selecting fewer crossings can give a different target. Delaying or reordering publications can preserve some event associations while losing equality with native counts at the original prefixes. A scalar pause of the whole native flow preserves its orbit and root order, so it cannot remove this incompatible count prefix by time reparameterization alone.

Local amplitude feedback can alter crossing order and count differences, but then conservation, closure and the cell spectrum need a new audit. Changing the discrete preparation guard also changes the source contract. Adding commits to cells with no crossings violates the tested one-to-one target. None of these choices is selected by this counterexample.

The result leaves open maps with different targets, selected preparations, nonzero history offsets or independently sourced feedback. It does not establish a universal obstruction to combining continuous and discrete dynamics. It excludes the explicitly stated zero-origin, cellwise, prefix-count-preserving interpretation for all real preparations on this cube carrier.

## Verification and next target

1408 exact constructor assertions pass, including coherent incidence, simplex geometry, the complete cell Gram spectrum, native mode identities, count compatibility and the bounded source enumeration. The independent plotting script requires matplotlib; the exact verifier uses only the Python standard library. The PNG was visually inspected for labels, curves and layout.

The next bounded question is which preparation or event-selection law UD actually admits. A possible diagnostic branch retains a single coherent mode and tests its simultaneous crossing batches against the source guards; that would be a selected-state candidate, not a repair for arbitrary real preparations. Any claimed internal selection must be sourced rather than inferred from the cube drawing.

Earlier releases and source claims are unchanged. Physical promotion remains0. Page content is checked by readback; Page layout is unverified.
