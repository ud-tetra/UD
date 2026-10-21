# UD phase-aware gate-transition audit v0.1

2026-10-01, America/Chicago (2026-10-02 UTC). Development lane. Constructor: Codex. Independent review: none. Physical promotion: 0.

## Result

A phase-aware current-crossing detector admits an exact isolated-tetrahedron example with explicit readiness reset and reusable-credit accounting. It does not survive unrestricted gluing under an all-four-face completion requirement: a valid active native mode of two face-glued tetrahedra leaves the shared face identically blind.

A cell-native zero-crossing port avoids that particular blind interface. It remains a candidate operational interface. Simultaneous publication, reference conventions, resource eligibility and observer lag still need source admission. No result here selects the cubic/BCC geometry or promotes a physical claim.

This continues the [amplitude/readiness audit](https://chatgpt.com/space/page_16412477c310819189552e1f0821e706) and preserves its findings. Earlier releases and source ledger values are unchanged.

## Source and branch boundary

The current provenance ledger v0.86 Q169–Q173 supplies the real skew generator, support stocks and signed incidence currents. Q173 still names “gate-transition receipt” as its next gate. The full retrieved local-clock audit v0.4 explicitly classifies reusable credits and one-way observation as a separate candidate branch.

Current manuscript version9 also contains:

- SA-TIME-007A/B: declared scalar cell bits and shared XOR comparison, separate from geometric orientation; not a deduction from Q169.

- SA-TIME-010: an exact binary reference/mismatch realization of the full-readiness template. It is explicitly constructed after a binary extension, not derived from the real-amplitude generator.

The binary comparator remains available. This audit tests an additional amplitude-driven mechanism; it does not claim that no readiness constructions already exist. Retrieved source windows and their identities are retained in the release. Their hashes identify the snapshots, not unretrieved full-source bytes.

## 1. The proposed detector must not gate away its own input

Write the directed ungated face-to-cell current as

~~~text
J(f,t) = 2 B3(f,t) f_f u_t.
~~~

Suppose an unready face has R(f,t)=0, the hard mask is h=R, and readiness can be acquired only from an upward crossing of the gated current h J. For that unready face, h J is identically zero until readiness changes. It has no transverse upward crossing that could cause readiness to change. Therefore it cannot acquire a missing flag from this rule alone.

This is a conditional deadlock of the specified self-gated construction, not a claim that UD's declared hard masks must equal readiness. A seed, a distinct probe current, an exogenous mask transition, or a new dynamics law changes the premise and must be stated.

The constructive branch below observes the ungated native current. Its readiness flags do not control the amplitude generator.

## 2. Working isolated example: four faces supply one synchronized port

Use one tetrahedron's oriented boundary column b, whose four entries are ±1. Restrict to the native closed face–cell pair:

~~~text
f = a b,          a' = −u,          u' = 4a
a = A cos(2zeta), u = 2A sin(2zeta)
J(f,t) = 2a u = 2 A² sin(4zeta) on every face.
S = ||f||² + u² = 4 A².
~~~

A is a nonzero preparation amplitude, not a fitted source coefficient. Zeta is the dimensionless native parameter, with no physical-time identification.

All four directed currents are equal. They cross upward simultaneously at zeta=k*pi/2 and downward at zeta=pi/4+k*pi/2. Exclude zeta=0 as initialization.

Declare this candidate observer:

1. Each upward crossing sets all four face-incidence flags.

2. At a fresh upward opportunity, full readiness, one available credit and clear publication buffers permit one commit.

3. The commit reserves one credit, toggles the independent cell bit and resets readiness to empty.

4. The next downward crossing returns the reserved credit. It commits no event.

5. Readiness remains latched while publication is blocked; retry only at the next fresh upward opportunity.

6. Neither readiness updates nor commits jump the amplitudes.

With one initial credit and an unblocked observer, there is one commit per upward opportunity indefinitely. Available plus reserved credits remains one; the bit records event parity. The exact replay covers24 half-crossings and12 commits, including reset receipts, zero-credit WAIT and backpressure.

The four flags are synchronized and redundant in this preparation. This example does not derive four independent accumulation mechanisms. The bit is not the sign of u at the opportunity: u=0 there.

This observational branch differs from the earlier candidate history lift, where each committed event applies a collective Cayley update. Adding that jump changes the sampled orbit and invalidates the unchanged-clock proof unless separately analyzed.

## 3. Gluing falsifier: active cell motion with a blind shared face

Take tetrahedra0123 and0124, using ascending-simplex chain bases. The shared face is012. Their boundary Gram matrix is

~~~text
G = B3ᵀ B3 = [[4,1],[1,4]].
e = (1,−1),  G e = 3e.
~~~

The native solution from f(0)=0 and u(0)=e is

~~~text
u(zeta) = e cos(sqrt(3) zeta)
f(zeta) = −(B3 e)/sqrt(3) sin(sqrt(3) zeta).
~~~

B3 e is zero on the shared face and nonzero on all six private faces. Therefore the shared face amplitude and both directed shared-face currents remain zero for all zeta. The cells oscillate; this is not a zero-support or stationary preparation.

The face state is in im(B3), so B2 f=0 throughout. The two-coordinate mode is invariant under the full native chain generator: lower-sector coupling vanishes. The obstruction is therefore an exact native mode, rather than an artifact of dropping the edge sector.

“Antisymmetric” describes the chosen ascending bases. Reversing the second tetrahedral basis makes the geometric orientations coherent, changes the cell mode to(1,1), and leaves the same physical face vector blind. The obstruction survives that basis change.

An all-four-face crossing latch can acquire private-face flags but never the shared-face flag. It remains WAIT forever on this active mode.

| Completion threshold | Three private flags suffice? |
|---|---|
| At least1,2 or3 faces | Yes |
| All4 faces | No |

All these cardinality rules can be relabeling-covariant. The successful isolated example cannot select the threshold because it acquires all four together. Excluding the glued mode, changing the required face set, or replacing the detector is new admissibility content.

This falsifies a universal gluing claim for the proposed all-four detector. It does not exclude a specified BCC carrier with restricted preparations.

## 4. Shared support flow is not a complete directed record

At the valid instantaneous coexact state f=B3(1,1), u=(1,−1), the two directed shared-face currents are +4 and−4. Their sum is zero.

Consequently a detector observing only the net change of shared-face support can miss the distinct cell-directed currents. The example is instantaneous; it is not asserted to remain in that cancellation pattern throughout its orbit. Unique geometric ownership and separate typed cell-incidence readouts must both be retained.

## 5. Support conservation does not preserve every propagation sector

A hard face mask preserves skewness if the same masked incidence operator appears in both adjoint blocks:

~~~text
A_h = [[0,−h B3],[B3ᵀ h,0]].
~~~

Thus this masked face–cell system preserves its Euclidean support. But B2 h B3 is generally nonzero. A mask retaining only the shared face already breaks the closed top coexact sector.

In the full native chain model, the resulting face state can couple to edges. One cannot use support conservation to assert preservation of the previous face–cell dispersion or clock identities. Whole-cell column gates can preserve B2 B3=0, but their transition and startup laws still require admission.

## 6. Better candidate port: a cell zero crossing with its native slope

Q171 already supplies the cell amplitude u_t and its native slope

~~~text
g_t = (B3ᵀ f)_t,  u_t' = g_t.
F_t = sum_f J(f,t) = 2u_t g_t.
~~~

At a cell root u_t=0 with g_t!=0,

~~~text
F_t' = 2g_t² > 0.
~~~

Every transverse cell-amplitude zero therefore gives an upward crossing of the total cell-support current. The converse need not hold: mixed motion can have nonzero local minima of u_t². A total-current upward crossing alone is not a universal sign-flip detector.

The candidate cell port tests u_t=0 and g_t!=0, admitting both directions. In the glued blind-face mode above, both cells have transverse roots separated by pi/sqrt(3), so this port avoids the particular all-four WAIT obstruction.

Its typed strengths:

- It uses the native cell register and signed contraction, rather than an unrelated threshold or inferred integer support quantum.

- The zero-crossing condition is unchanged by orientation-basis reversal.

- On a declared all-transverse orbit, a retained binary reference can toggle at every root and agree with the sign between roots.

Its remaining obligations:

- Nontransverse zeros, blind/stationary preparations and mixed-mode timing.

- Initial phase/reference and the zero-instant readout convention. Absolute sign of an oriented cell coefficient is not by itself a scalar cell decoration.

- Credits, release, backpressure and successful publication.

- Candidate admission as an actual event interface. Q171 selects the mathematical port quantities, not this event convention.

## 7. Publication obstruction: simultaneous flips can erase a shared trace

The blind-face mode makes the two cell roots simultaneous. If both corresponding bits toggle as one unrecorded update, a shared XOR readout is unchanged:

~~~text
(0,1) -> (1,0): shared XOR 1 -> 1.
Serial publication: XOR 1 -> 0 -> 1.
~~~

With a coherent orientation reference, equally initialized bits likewise give0 -> 0 under a joint flip. More generally, simultaneous global complementation lies in the kernel of the binary graph coboundary. Even a triangle whose individual actor signatures differ loses the net trace of all three bits flipping together.

The two-cell pair is used as a native-amplitude falsifier, not claimed to be a sufficient identifying observer graph. A larger observer may retain external edges and event identities; the shared-only readout obstruction still applies.

Thus detection at a native root, successful publication and retained observation are separate stages. Serial receipts or an explicitly admitted compound-event record are needed before counting the collapsed update as distinct ticks. Buffer delays also separate a published bit from an instantaneous amplitude-sign readout.

## What this adds to the geometry program

The source equations impose useful restrictions beyond geometric resemblance: a moving cell can have a silent interface, and a norm-preserving mask can change its propagation sector. An operational cubic/BCC interpretation must survive both tests.

No internal cubic selection follows. The next bounded target is the cell-native zero-crossing interface under causal publication: preserve root identities through simultaneous roots and backpressure, specify the binary reference, and prove the retained event count survives the permitted ordering. Treat detector occurrence, publication and retained observation as separate records.

## Verification and claim classes

1765 exact constructor checks passed with standard-library Fraction arithmetic. The count includes1296 exhaustive self-gating fixtures,16 isolated orientation choices,128 paired face masks, credit transitions, boundary identities and the explicit glued invariant-mode certificates. It is not a count of independent experiments.

- EXACT / DERIVED: boundary, skewness, conservation, eigenmode, blindness, root-current slope and XOR identities for the fixed native model.

- EXACT CONDITIONAL: isolated observer/reset/reuse behavior under the declared candidate law.

- CANDIDATE: acquisition/reset semantics, credits, binary reference, release and publication interface.

- OPEN: source selection, unrestricted gluing, retained detector correspondence and physical realization.

- Physical promotion:0. No empirical anchor, coefficient value or primitive action is changed.

The mathematical all-time statements follow from the displayed invariant-subspace proofs, not a numerical root grid. Independent review and observations remain absent. Rejected proposals are retained in the risk register with failure modes, repairs and replay conditions.

The command-line workspace is available again. This release preserves the previous audit's saved JavaScript replay alongside the new exact Python replay. Page text is read back for verification; visual layout is unverified.
