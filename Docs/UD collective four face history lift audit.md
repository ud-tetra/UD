A collective rotation of each tetrahedron's amplitude and its four oriented face amplitudes gives a connected candidate that preserves locality, source-independent event ordering, and the original squared-amplitude norm. It repairs the specific failures of the previous overlapping two-coordinate assignment. Its small-step aggregate recovers the native face-and-tetrahedron generator and its tetrahedron-based acoustic branch, whose leading metric is compatible with the supplied BCC embedding.

This is a conditional construction, not a source-derived law. The current binary event branch does not supply its real amplitude state, rational rotation, step size, launch, or aggregate schedule. The new replay passes **53 exact checks and 730 numerical checks**, including five directions for every one of the 720 six-type schedules. Physical promotion remains 0. Exact algebra and finite sampling have different scopes throughout this report.

## Operator from the oriented four face boundary

For tetrahedron t, let b_t be its column in the oriented boundary matrix B3. Its four entries are signs of unit magnitude, so b_t* b_t=4. Let f contain the face amplitudes and u the tetrahedron amplitudes. Define J_t by coupling only u_t and b_t:

```text
J_t(f,u) = (-b_t u_t, e_t b_t* f)
J_t* = -J_t
J_t³ = -4 J_t
```

Here e_t selects that tetrahedron's coordinate, and star denotes adjoint. For a supplied real step ε, choose the local rational rotation:

```text
U_t(ε) = I + [ε/(1+ε²)] J_t
             + [ε²/(2(1+ε²))] J_t²
```

It is the Cayley transform of J_t. On the normalized pair (b_t/2,u_t), its cosine is (1-ε²)/(1+ε²) and its sine is 2ε/(1+ε²). Therefore U_t*U_t=I for every real ε. There is no stability restriction on this local rotation and no modified norm is needed.

The rational formula is an added choice. The decomposition J_t uses the inspected chain incidence grammar, while choosing Cayley evolution and a common ε does not follow from that grammar. No value is fitted to a physical target. The ε=1/8 exact witness and refinement resolutions are computational controls.

## Locality and chain closure

U_t changes only the four face coordinates in b_t and the cell coordinate u_t. It leaves every other coordinate unchanged, including disconnected spectators. Its face-to-face terms stay within the same tetrahedral star; a stage spans at most two face-cell incidence hops.

The boundary identity B2B3=0 gives B2b_t=0. Hence every update leaves B2f unchanged and preserves the subspace f in the image of B3. Together with arbitrary tetrahedron amplitudes, that subspace is the native top coexact sector. The original full chain generator preserves it as well: the edge update from such f vanishes because B2f=0.

The replay verifies these identities exactly on a connected five-tetrahedron witness and verifies the periodic Laurent boundary and column-norm identities. The periodic columns each use four distinct face types. Thus translates of one tetrahedron type form disjoint update stars and can be grouped into one matching layer.

## Causal history lift

Use the inspected readiness, binary flip, and active recording-buffer rules with **every shared face observed**. Two different tetrahedra that share no face have disjoint amplitude update supports. Their U operators commute exactly. Tetrahedra sharing a face have overlapping operations; the source's full observed-face buffers order their commits and preserve that order in receipt parents.

For a supplied initial amplitude c0 and a complete retained causal event set E, apply the actors' U operators in any linear order consistent with its parent relation. Incomparable events cannot share a face under the full observation contract. Exchanging adjacent incomparable events therefore exchanges commuting operators and leaves the result unchanged. Since any two linear orders of the same finite partial order can be connected by such exchanges, this defines an unambiguous formal amplitude Φ(E).

Appending an enabled commit applies its U_t, preparations leave amplitude unchanged in this proposed lift, and each commit still contributes one source event unit. The real amplitude state or the retained history carries phase information that the recurrent binary state lacks. The previous current-control obstruction remains valid; this construction escapes it by explicitly adding that information.

The proposed amplitude update occurs at commit and publication. An observer can replay only its parent-closed known event set, which may lag published evolution. Readiness and pending buffers still govern source enablement; Φ alone is not a complete source state or a claim of instantaneous global knowledge.

The exact source witness has a central tetrahedron and four neighbors, one across each face. All 24 leaf orders followed by the center give the same retained causal record and the same amplitude, using a dense rational launch. The replay also checks the complete operator commutators, not only this launch. The norm identity applies to every amplitude.

This lift does not turn the binary receipts into measurements of real amplitudes. Given the extra law and launch, actors inferred from receipts can determine a mathematical replay. A physical amplitude measurement, state implementation, precision policy, and receipt accounting interpretation remain open.

## Full observation is a material condition

An arbitrary identifying subgraph is insufficient for this operator family. Three tetrahedra can form a triangle in their full dual graph while the observed graph is only a three-actor path. The path has nonempty, distinct actor signatures and meets the source's component-size condition. Its endpoint actors use disjoint observed buffers, yet their tetrahedra share an unobserved face. Their U operators do not commute.

The replay constructs this triangle and checks the nonzero commutator exactly. A lift that relies on source independence must therefore observe every amplitude-sharing face, introduce separately justified dependencies, or change the operator support. Full observation is an admitted choice here, not an internally selected detector graph. Its buffers retain the source's backpressure; the construction does not claim passive observation.

## Aggregate native generator

Summing the collective generators gives precisely the native top block:

```text
A23 = sum_t J_t = [[0, -B3], [B3*, 0]]
u_double_dot = -B3* B3 u
```

For the periodic six-tetrahedron translation cell, supply a palindromic schedule: the six type layers in order, followed by the reverse order. Each layer uses U_t(δ/2). A full macro update Sδ consequently has:

```text
Sδ = I + δ A23 + δ² A23²/2 + O(δ³)
```

The exact replay checks both coefficients at the zero character and one nontrivial sign character. The general result follows from consistent first-order generators and the symmetric composition: the palindrome makes the quadratic coefficient half the square of their sum. Each factor conserves the original norm, so the complete macro update does too.

The schedule is supplied. On a proper finite periodic carrier with N translation cells, it contains 12 actor-type layers and 12N individually completed commits. The appearance of δ/2 in an amplitude operation does not make a fractional event tick: every commit counts one. Neither 12 layers nor 12N activity units are automatically a native or physical duration. A complete macro layer ordering is an additional contract beyond the source's local readiness and buffer rules.

## Which propagation branch survives

This construction addresses the face-and-tetrahedron sector, not all 26 chain coordinates. Its native top Laplacian has one acoustic branch and five optical pairs at generic nonzero wavevector. At the zero character it has five oscillating pairs and eight stationary coordinates in the full 18-dimensional top block. The aggregate retains the stationary dimension in the exact checked characters, but its stationary cell vector differs from the native one at finite δ.

The prior full-mode audit gives the leading top squared frequency Q/24, where Q=qᵀ(2I+2J)q. Under the previously supplied embedding E=4^(-1/3)(J-2I), the long-wavelength continuum squared speed is κ/24, with κ=2^(5/3). It is 0.132283420997 in the declared units, or speed 0.363707878657. It is slower than the vertex branch by the factor 1/√24. A common shape does not make those speeds equal.

Extending these operators as identity on degree zero and one coordinates leaves a vertex-only amplitude readout unchanged. A state launched solely in this top sector stays invisible to the prior vertex array. Binary face mismatch receipts identify event actors but do not replace a face or cell amplitude readout. This is a concrete observation requirement for using the branch, not evidence for a physical field identification.

## Finite resolution and schedule scan

All 720 permutations of the six type layers were tested at macro δ=1/8, wave magnitude 0.0002, and five Cartesian directions after applying E. The sampled squared speeds range from 0.132282075280 to 0.132282579917. Within any tested schedule, the largest directional spread is about 3.23 times 10^-11. These numerical samples support compatibility with the BCC long-wavelength metric shape; they are not an exact proof of isotropy for arbitrary wavevector or schedule.

Different dependent schedules have different exact macro operators, despite equal total commit counts. Their sampled common speeds also differ slightly. Those schedules correspond to different ordered causal histories, so this is not a failure of the same-history commutation theorem. It shows why counts alone do not specify amplitude evolution and why a schedule cannot be silently imported as a selected clock.

For the displayed order 0,1,2,3,4,5 and its reverse:

| Macro δ | One-step operator error at declared nonzero q | Departure of native normalized cell harmonic vector at q=0 |
| --- | --- | --- |
| 1/8 | 0.000909120416 | 0.000643239026 |
| 1/16 | 0.000114044055 | 0.000080657496 |
| 1/32 | 0.000014268189 | 0.000010090101 |

Both errors decrease by approximately eight when δ halves, as expected for a cubic local error. The native cell harmonic representative is changed, although an eight-dimensional stationary space remains at q=0. Thus a finite-step macro is not exactly the native continuous flow.

## A controlled refinement limit

Each J_t has operator norm 2. Replacing its Cayley half-step by the corresponding exponential costs at most δ³/12, using the angle bound |2 atan(x)-2x|≤2|x|³/3. Twelve factors cost at most δ³ by unitary telescoping. The exponential palindrome and exp(δA23) have equal terms through degree two. Bounding their Taylor tails by the sum of generator norms gives:

```text
||Sδ - exp(δA23)|| ≤ [1 + 576 exp(12|δ|)] |δ|³
```

This bound is intentionally loose; at the displayed larger resolutions it is much larger than the measured error. It is useful for establishing the refinement order and does not estimate an experimental tolerance.

Supply spatial scale a and the same type of refinement clock Δt=aδ used previously. At an integer-step horizon t=n aδ, unitary telescoping gives:

```text
||Sδ^n - exp(nδA23)||
  ≤ [1 + 576 exp(12|δ|)] |t| δ²/a
```

Therefore δ²/a tending to zero is a sufficient joint-refinement condition. The declared example δ=a meets it. This preserves convergence to the native top flow and then its low-wavevector BCC branch under the separately supplied embedding and clock. Neither refinement relation nor its units are derived from the source's commit count.

Every macro update has a strict support bound of at most 24 face-cell incidence hops. Under Δt=aδ, this bound does not provide a uniform physical speed as δ tends to zero. The bound alone does not prove that no sharper cone exists; a uniform cone or appropriate observable-tail statement needs a separate analysis. No Lorentzian or relativistic causal interpretation is established.

## Source selection remains open

Two compatible local laws already demonstrate nonuniqueness: U_t(ε) and U_t(ε/2) squared both conserve the norm, stay in the same star, preserve chain closure, commute for nonadjacent cells, and have the same first derivative J_t. They differ exactly at finite ε. The replay verifies this alternative. Four-face incidence and these compatibility gates do not select the rational law or its scale.

The binary field is also not simply the sign of the new cell amplitude. With cell amplitude 1 and face amplitudes zero, a commit at ε=1/8 gives cell amplitude 63/65, still positive, while the declared source binary bit flips. This exactly rejects that particular sign identification. The source defines x as a binary decoration, so it does not require the rejected sign map in the first place; any alternative readout map needs its own law.

Zero real amplitude remains zero under every rotation while the source can still perform binary commits. Consequently, event counts and a nonzero wave launch are not linked by this construction alone. The source needs an amplitude initialization or resource and readiness relationship before commits can be interpreted as amplitude-driven occurrences.

| Admission requirement | This audit | Remaining obligation |
| --- | --- | --- |
| Connected local operators | Constructed from oriented four-face columns | Justify the operator as a native commit action |
| Common conserved support | Original unit norm conserved exactly | Identify its source meaning and amplitude readout |
| Independent event ordering | Formal lift is well-defined with full shared-face observation | Derive or admit that graph and memory contract |
| Aggregate wave structure | Native top generator recovered to second order | Select event grouping and schedule; audit finite resolution |
| Other branches | Top acoustic branch shares the conditional BCC metric | Full four-branch law and a common physical interpretation remain open |
| State and enablement | Real amplitudes provide the missing phase state | Tie binary decoration and readiness to amplitudes or retained resources |
| Metric and time | Embedding and refinement clock supplied | Independent metric selection and empirical correspondence remain open |

The next bounded source target is the state-and-enablement relationship: whether an inspected support, burden, or resource law ties real face and cell amplitudes to readiness and the binary interface record. If no such map is supplied, retain this as a formal history lift with an explicit new axiom rather than a derived UD mechanism. The global scale and schedule questions remain independent.

## Replay and scope

Run `python verify_ud_collective_face_rotation_v0_1.py --out replay_results` with NumPy and the three unchanged helper files beside it. Their complete prior audits are not rerun. The release preserves source bytes, candidate choices, exact certificates, numerical samples, rejected interpretations, and a SHA256 manifest. The inspected minimum time model v0.11 was checked again against its current retained source, which continues to distinguish the real chain and binary event branches. No canonical source was amended.

The construction and its general algebraic proofs concern internal mathematical compatibility. The 720-schedule scan is finite numerical evidence at a declared wave magnitude, not a proof of all-wavevector symmetry. No independent review, physical experiment, duration calibration, or external physical correspondence is promoted.

## Saved evidence and prior audit

[UD_COLLECTIVE_FOUR_FACE_HISTORY_LIFT_AUDIT_v0.1.md](library-file:file_0000000014b881f68ec2bbe21666588c)

[UD_COLLECTIVE_FACE_ROTATION_RESULTS_v0.1.json](library-file:file_00000000042481f6a464d9a9f72e5959)

[UD_COLLECTIVE_FOUR_FACE_HISTORY_LIFT_CONTRACT_CANDIDATE_v0.1.json](library-file:file_00000000a52c81f684bfdc3145238097)

[UD_EVENT_AMPLITUDE_SOURCE_ADMISSION_STATUS_v0.2.json](library-file:file_00000000df4c81f6976c00313f974de6)

[UD_COLLECTIVE_FOUR_FACE_REJECTED_INTERPRETATIONS_v0.1.json](library-file:file_00000000adf881f6868c2835eefaf58f)

[UD_COLLECTIVE_FOUR_FACE_HISTORY_LIFT_v0.1_RELEASE.zip](library-file:file_00000000f17081f6a70e39bfda4e8ea1)

[UD_COLLECTIVE_FOUR_FACE_HISTORY_LIFT_v0.1.sha256](library-file:file_00000000f42481f699a9cbcf1809ff7d)

[Previous event amplitude audit](https://chatgpt.com/space/page_304006c15fc881918f7b7ee0009d7ff7)