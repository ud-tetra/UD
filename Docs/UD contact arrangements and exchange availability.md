Two distinct contact faces are sufficient to reduce the permanently non-transferring central seed space from three dimensions to one, provided both declared candidate exchange channels are nonzero at each contact. The surviving direction is the uniform vertex harmonic. An equal-sign spoke pattern that never recruits an isolated neighbor at one face recruits an isolated neighbor at any other face at quadratic stock order.

These are exact conditional results for supplied contacts and independently stored packets. They establish that exchange availability depends on the contact arrangement as well as the seed pattern. They do not establish a native activation law, persistent binding, topology creation, metric shape preference or physical correspondence.

Date: 3 October 2026. Internal claim bin: CANDIDATE_DEVELOPMENT_MATHEMATICS. Correspondence status: NOT_PROPOSED. Physical promotion: 0. Independent review: PENDING.

## Model and source boundary

Retain the oriented tetrahedral packet with 15 coordinates: four vertices, six edges, four faces and one cell. Ascending simplex orientation defines the boundary matrix D; the one-copy generator is A = transpose(D) minus D, with the supplied identity metric. Direct reconstruction gives D squared = 0 and A cubed = minus 4A.

The central tetrahedron has vertices 0, 1, 2, 3. Its four possible contact faces are 012, 013, 023 and 123. Every tested contact has a separate, pre-existing 15-coordinate neighbor. A signed incidence transport identifies that neighbor's face and opposite apex with the central coordinate frame. The packets retain separate copies of their shared-face amplitudes. This is an exchange model on independent storage, not the quotient that identifies shared simplices into a single glued complex.

For face f, restrict the vertex–edge and edge–face boundary blocks to the full contact triangle. Define their skew extensions as Ba(f) and Bb(f). The candidate exchange operator is:

```text
Bf = af Ba(f) + bf Bb(f)
x' = A x + sum_f Bf yf
yf' = A yf + Bf x
initial state: x(0) = v; all yf(0) = 0
```

The coefficients remain arbitrary fixed real values. An active channel means its coefficient is nonzero; no magnitude, sign or rate is selected. The three classified regimes activate a at every selected face, b at every selected face, or both at every selected face. Mixed per-face regimes and neighbor-to-neighbor interactions are outside this release. The full star generator is skew and preserves the sum of packet norms squared.

The parent seed-readiness release supplies the one-face family and exact observation test. Its archived executable was replayed, including its two upstream replays. This release independently reconstructs the packet and all four channels, compares A to the replayed parent and verifies signed covariance under all 24 tetrahedral vertex permutations.

The current parity-parent source addendum was also read in full. That separate 16-coordinate candidate supplies a reciprocal reservoir and a Jacobi-compatible boundary-face port under its stated nonlinear-feedback ansatz. It explicitly leaves the reservoir preparation and coupling provenance open. It neither supplies these contact coefficients nor licenses identifying its reservoir with a neighboring tetrahedron. Its correspondence tag is not inherited here.

## Exact test for complete absence of recruitment

For a set of supplied contacts, stack their active channel matrices into R. Define O by stacking R and RA. Orthogonality of the two channels at each face gives:

```text
Ba(f)^T Bb(f) = Bb(f)^T Ba(f) = 0
||Bf v||^2 = af^2 ||Ba(f) v||^2 + bf^2 ||Bb(f) v||^2
```

Thus nonzero coefficients cannot cancel the two channels within a contact. Separate neighbors contribute separate nonnegative stocks, so they cannot cancel each other's recruitment either. The coefficient-independent all-time test is:

```text
Every neighbor stays exactly empty for all time
if and only if
R v = 0 and R A v = 0.
```

Necessity follows by differentiating the neighbor amplitudes at zero: the first derivatives are Bf v and the second derivatives are (ABf + Bf A)v. If the neighbors remain empty, both observations vanish.

For sufficiency, A cubed = minus 4A reduces all later native observations to the first three. Direct verification gives R A squared = minus 4R. The space N = kernel(R) intersect kernel(RA) is therefore A-invariant. Starting in N, the trajectory with x(s) = exp(As)v and all neighbors zero satisfies every equation; uniqueness of the fixed linear system makes it the actual trajectory.

This is a joint statement about all neighbors remaining empty. A face classified as permanently silent in an isolated two-packet experiment need not remain silent after other active neighbors change the central state. The isolated route witness below and the joint star test are kept separate.

## Contact atlas

The verifier exhausts every nonempty subset of the four faces in each of the three channel regimes: 45 configurations. The table reports the common result for every subset of the indicated size. All dimensions refer to the 15-dimensional central amplitude space; they are not probabilities, counts of particles or fractions of physical preparations.

| Channels | Contact faces | Immediate observation rank | All-time observation rank | Permanent nullity | Delayed quotient dimension |
| --- | ---: | ---: | ---: | ---: | ---: |
| a only | 1 | 4 | 8 | 7 | 4 |
| a only | 2 | 7 | 12 | 3 | 5 |
| a only | 3 | 9 | 12 | 3 | 3 |
| a only | 4 | 9 | 12 | 3 | 3 |
| b only | 1 | 2 | 4 | 11 | 2 |
| b only | 2 | 4 | 6 | 9 | 2 |
| b only | 3 | 6 | 8 | 7 | 2 |
| b only | 4 | 7 | 8 | 7 | 1 |
| both | 1 | 6 | 12 | 3 | 6 |
| both | 2 | 10 | 14 | 1 | 4 |
| both | 3 | 12 | 14 | 1 | 2 |
| both | 4 | 13 | 14 | 1 | 1 |

The delayed quotient dimension is all-time rank minus immediate rank. It describes kernel(R) modulo N; it is not an extra invariant sector. With no supplied contacts, all 15 seed directions are silent by construction.

Two faces with both channels active expose every central direction except the uniform vertex harmonic to eventual exchange. Adding the third or fourth face changes which preparations exchange immediately, but does not reduce the permanent nullity further. With four faces, one further independent direction is initially silent but becomes available at higher Taylor order.

The exact surviving spaces provide useful controls:

| Contact regime | Permanent seed space |
| --- | --- |
| Both channels on any two or more distinct faces | span(h), where h has vertex entries 1/2 and every other entry zero |
| a only on any two or more distinct faces | span(h, D z, z), where z is the cell basis vector |
| b only on all four faces | All vertex amplitudes plus the three-dimensional space of edge gradients D transpose applied to vertex amplitudes |

The first space is stationary because Ah = 0 and every contact channel annihilates h. The other spaces can contain native internal motion even while every neighbor remains empty. Lack of recruitment is not lack of propagation within the central packet.

## Stages and a concrete route witness

At every empty-neighbor launch, the initial derivative of neighbor stock is zero. It therefore cannot by itself distinguish recruitment from complete silence. For fixed coefficients, define total neighbor stock S as the sum of norms squared:

```text
If at least one Bf v is nonzero:
S(s) = sum_f ||Bf v||^2 s^2 + O(s^3).

If every Bf v = 0, but some Bf A v is nonzero:
S(s) = (1/4) sum_f ||Bf A v||^2 s^4 + O(s^5).

If every Bf v and Bf A v vanishes:
S(s) = 0 for all time.
```

The fourth-order case has no positive waiting interval. A higher Taylor order is not a native waiting threshold, and dimensionless s is not an identified physical time.

Take the equal-sign spoke seed v = e03 + e13 + e23, with central stock 3. Test one isolated neighbor at a time:

| Contact face | Immediate channel observations | Isolated recruitment result |
| --- | --- | --- |
| 012 | Both zero; both second observations also zero | Permanently empty |
| 013 | a observation norm squared 6; b observation zero | S(s) = 6 af squared s squared + higher orders, if af is nonzero |
| 023 | a observation norm squared 6; b observation zero | Same quadratic onset condition |
| 123 | a observation norm squared 6; b observation zero | Same quadratic onset condition |

This is the same central pattern and the same initial stock in all four experiments. Availability changes with the contact face. With all four already supplied neighbors and a common arbitrary a coefficient, the total initial quadratic stock coefficient is 18 a squared. That aggregate assertion does not claim independent isolated trajectories after transfer begins.

The executable also records the stage for all 15 coordinate-basis seeds in each of the 45 configurations: 675 exact records. These basis records are diagnostics, not a complete classification of superpositions. The retained kernel bases classify superpositions, including cancellations inside signed seeds.

## What survives a state dependent activation rule

If a proposed state-dependent law only multiplies these same channels, the intersection of their structural kernels remains a protected no-recruitment space whenever the full ODE is well posed and unique. A central state in that space undergoes native motion and presents zero channel force to every empty neighbor, regardless of coefficient values along that trajectory.

The converse is conditional. A seed outside the structural kernel is available to a channel but need not actually recruit if an activation law sets that channel to zero. Immediate onset requires an actual nonzero channel force. Higher-order onset for a nonlinear rule needs its own regularity and derivative audit; the fixed-coefficient fourth-order formula cannot be imported unchanged.

Consequently, an overlap rule that disables every empty-neighbor contact still prevents recruitment. Adding more potential contacts does not repair that source defect. The all-face harmonic direction also cannot be recruited by changing only scalar activation coefficients within this family.

## Scientific interpretation and next discriminator

The gap analysis now has a concrete answer: a pattern cannot be classified as recruitment-preferring without specifying the permitted contacts and active propagation channels. One-face silence can be removed by another contact, while some seed sectors remain protected under the entire contact family.

This release establishes exchange availability and its initial stages. Fixed skew dynamics preserve distances between full-system trajectories, so they do not supply attraction to a preferred configuration. Norm conservation alone does not establish binding, retained membership or cluster growth. No cubic or skew-cubic carrier has been selected.

The next informative comparison is to derive or declare which contacts can become active and whether exchanged support yields durable shared membership. A source-complete test should compare alternative contact arrangements under the same preparation and activation source, record signed amplitudes and donor receipts, then test retention after the preparation is removed. Geometric preferences require an admitted link between incidence contacts and metric configurations; these exact rank calculations do not provide that link.

## Verification and retained evidence

The exact verifier passes 484 assertions covering boundary reconstruction, signed covariance, all 45 rank and kernel certificates, permanent-space spanning certificates, the isolated spoke witness, a 75-coordinate four-neighbor star and total norm conservation. The parent readiness executable reproduces its mathematical JSON exactly and includes its two upstream source replays. A fresh extraction of this release reproduces its own results byte for byte.

The archive retains the verifier, exact results, source-read receipts, the complete parent release, a risk register, requirements and a SHA-256 manifest. Constructor replay and byte integrity are not independent scientific review. Current source-read scope consists of the readiness report and the parity-parent addendum, not the entire UD corpus.
