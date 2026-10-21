The missing coherence-changing operator can be constructed conditionally, but its admissibility depends on contact access. With fixed native diagonal boundaries, a nonzero pure symmetric cross port confined to the shared face fails boundary-square zero. Allowing exclusive coface incidences yields three one-parameter families under literal simplex-label incidence; each changes the original uniform-vertex mode. Broader access through the packet-coordinate correspondence yields four algebraic branches, including nonzero families that preserve that mode.

One harmonic-preserving completed family has an exact transient-agreement control: special packet preparations can become equal, then immediately leave agreement while the port remains active. This provides a constructive next step beyond the invariant-mismatch baseline. It does not supply native capture, a gate-closing law or geometric preference.

Date: 3 October 2026. Internal claim bin: CANDIDATE_DEVELOPMENT_MATHEMATICS. Correspondence status: NOT_PROPOSED. Physical promotion: 0. Independent review: PENDING. No coefficient value, incidence extension or event law is adopted as native UD.

## Declared boundary ansatz and scope

The carrier retains two independently stored tetrahedral packet states with 15 real amplitudes each and unit metric. Their apex correspondence 3 to 4 identifies packet coordinate frames; it does not identify their geometric apex positions. Each packet has its original ascending boundary D and skew generator A = transpose(D) minus D.

This release classifies a pure symmetric reciprocal cross-port sector through a degree-lowering boundary extension:

```text
Dnew = [[D, E], [-E, D]]
G = transpose(Dnew) - Dnew
  = [[A, -W], [W, A]]
W = E + transpose(E).
```

G is skew for every real E and conserves total packet norm squared. The extra chain requirement is:

```text
Dnew squared = 0
if and only if
D E + E D = 0 and E squared = 0.
```

Unlike the prior skew cross-channel family, the cross operator is symmetric within the matched one-copy frame and can change complete-copy overlap. The extension has an oriented copy link: swapping packet sides reverses E. That side context and any coupling provenance remain unsourced.

The classification keeps the diagonal D fixed, allows only its existing adjacent-grade incidence positions in the matched packet frame, and imposes signed covariance under permutations of contact vertices 0, 1, 2. It excludes diagonal cross ports, non-incidence entries, changed diagonal boundaries, mixed symmetric/skew cross-port families and added state coordinates. It is exhaustive only within this stated ansatz.

The current contact-transition report was read in full and its complete release was hash-checked and replayed, including seven upstream releases. The new boundary and symmetry matrices are independently reconstructed. No current canonical boundary or locked parent release is modified.

## Eight signed incidence orbits

There are 28 nonzero incidence positions in D. Signed contact-permutation covariance leaves an eight-dimensional operator space. At every allowed position, E is the original signed D entry multiplied by the coefficient of its orbit:

| Coefficient | Input simplex | Output simplex |
| --- | --- | --- |
| r0 | Contact edge | Contact vertex |
| r1 | Apex edge | Contact vertex |
| r2 | Apex edge | Apex vertex |
| r3 | Contact face | Contact edge |
| r4 | Mixed face containing the apex | Contact edge |
| r5 | Mixed face containing the apex | Apex edge |
| r6 | Cell | Contact face |
| r7 | Cell | Mixed face containing the apex |

The verifier checks every orbit against all six signed contact permutations. An independent linear commutation system on the 28 individual positions has rank 20, proving that the eight orbit matrices span the entire admitted symmetry space.

Boundary anticommutation has exactly two independent linear conditions:

```text
r0 - r1 + r4 - r5 = 0
r3 - r4 + r6 - r7 = 0.
```

After those conditions are imposed, E squared vanishes exactly when:

```text
(r1-r4)(r4-r5) = 0
(r4-r6)(r6-r7) = 0.
```

These identities are obtained from the complete matrices, not selected examples. They classify a union of four linear branches: choose either factor in the first product and either factor in the second product to vanish. Each branch has dimension four before adding another gate. Branches intersect; their count is not a count of shapes, isomorphisms, preparations or probabilities.

## Access requirements change admissibility

Strict shared-face support retains only r0 and r3. The two anticommutation equations then force both to zero. Thus there is no nonzero face-only port of this type with the native diagonal boundaries unchanged. This is a rejection of this extension ansatz, not a contradiction of the fixed native boundary or a universal prohibition on face-local interactions.

Literal cross-label incidence is a stronger check than matched-frame incidence. For a left output simplex u and right input simplex v, it requires the actual label relation u contained in v after the right apex is relabeled 4. A left simplex containing apex 3 cannot be a face of a right simplex containing apex 4. This removes r2, r5 and r7, leaving five orbits.

The remaining equations yield exactly three one-parameter families. Each row lists the coefficients divided by an arbitrary real k:

| Literal-incidence family | r0 | r1 | r3 | r4 | r6 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Vertex | 1 | 1 | 0 | 0 | 0 |
| Face | 0 | 1 | 1 | 1 | 0 |
| Exclusive to shared | 0 | 1 | 0 | 1 | 1 |

In every row r2, r5 and r7 are zero. Each passes the exact square-zero requirement for every real k. Their shared zero point is not three distinct zero operators. Even these ports exceed strict face-only access: they use exclusive apex-edge, mixed-face or cell inputs.

This extension remains an algebraic chain complex on the doubled packet carrier. It is not automatically the ordinary simplicial boundary of the 23-coordinate glued union: shared simplices are still independently stored, and the new cross incidences and weights need an explicit model interpretation.

## Preserving the original vertex harmonic

Let h be the one-copy unit vector with entry 1/2 on each of the four vertices and zero elsewhere. The original generator satisfies Ah=0. Since E lowers degree, Eh=0, while:

```text
transpose(E) h
  = (r2-r1)/2 times (e03+e13+e23).
```

Keeping this original mode unchanged therefore adds the condition r2=r1. This is an explicit comparison gate; it is not treated here as a newly imposed universal source rule. Moving the original harmonic vector is distinct from changing homology dimension.

Every nonzero literal-incidence family fails this gate because r2=0 and r1=k. Requiring both literal incidence and preservation of the original h leaves only the zero port in this ansatz. Under the broader matched-frame access, the extra harmonic condition leaves four branches of dimension three each. Their complete bases are retained in the results.

| Required access and gates | Exact admitted nonzero family |
| --- | --- |
| Strict face only; fixed native D; square zero | None in this ansatz |
| Literal label incidence with exclusive coface inputs; square zero | Three one-parameter families |
| Same literal incidence plus unchanged original h | None in this ansatz |
| Full matched incidence; square zero | Four intersecting branches of dimension four |
| Full matched incidence plus unchanged original h | Four intersecting branches of dimension three |

This locates a concrete source choice: which exclusive incidences may a contact access, and must it preserve the original harmonic vector? A basis change cannot silently turn broader access into literal face-local geometry.

## A signed seed control for the literal vertex family

For the vertex family write E=k Ev and Wv=Ev+Ev transpose. The initial seeds e0−e01 and e0+e01 have the same coordinate amplitude squares, total stock 2 and an empty neighbor. They differ in relative amplitude sign.

```text
For x' = Ax-k Wv y and y' = Ay+k Wv x:

(x transpose y)' at launch
  = +2k for e0-e01
  = -2k for e0+e01.

For e0-e01:
(||x-y||^2)' at launch = -4k
neighbor stock = 5 k^2 s^2 + O(s^3).
```

For positive k, one declared signed pattern initially increases complete-copy overlap and the other decreases it. Reversing the port orientation reverses that preference. No sign, launch or value of k is selected as native. The negative amplitude carries relative phase in the model; total support is positive norm squared.

The control proves that a conservative square-zero extension can change mismatch. It also retains its failed harmonic gate. Initial mismatch decrease is not global monotonic convergence, attraction or persistent binding.

## Exact completed family with transient agreement

An especially transparent matched-incidence subfamily is E=kD. It obeys both boundary conditions and preserves the original h for every real k. It uses the full matched boundary, including the three orbit types forbidden by literal cross-label incidence. Those additional apex accesses must be declared; this is not a strict face-local mechanism.

Let H=h h transpose, P=I−H and W=D+D transpose. Direct identities give:

```text
W squared = 4P
A squared = -4P
A W + W A = 0
G squared = -4(1+k^2) diag(P,P)
omega = 2 sqrt(1+k^2).
```

For the one-sided launch (v,0), the full exact trajectory is:

```text
x(s) = H v + cos(omega s) P v + sin(omega s) A v / omega
y(s) = k sin(omega s) W v / omega.
```

Its neighbor stock and infinite-time mean are:

```text
S_R(s) = k^2/(1+k^2) sin^2(omega s) ||P v||^2
mean S_R = k^2/[2(1+k^2)] ||P v||^2.
```

These differ from the prior skew cross-channel family's average. The operator changed; its former half-active-stock formula must not be transferred to this new family. Here the mean tends continuously to zero as k tends to zero, and exact empty-neighbor returns occur whenever sin(omega s)=0. Dimensionless frequency is not a physical rate calibration.

Complete-copy agreement requires Hv=0. On that nonharmonic space:

```text
x-y = [cos(phi) I + sin(phi)(A-kW)/omega] v
phi = omega s
(A-kW)^2 = 4(k^2-1)P.
determinant of the difference map on P
  = [cos^2(phi) - (k^2-1)/(k^2+1) sin^2(phi)]^7.
```

If |k| is less than 1, the difference map is invertible at every phase, so no nonzero one-sided seed reaches complete-copy agreement. At |k|=1, agreement is available at cos(phi)=0 for a special seven-dimensional kernel. For |k| greater than 1, the real eigenvalues plus and minus 2 sqrt(k squared minus 1) give two seven-dimensional seed subspaces, each with suitable agreement phases. This is accessibility inside a declared coefficient family, not a native threshold or selected coupling.

At the exceptional algebraic test point k=1, choose the closed contact-edge cycle v=D e012. It has initial stock 3, Dv=0 and Hv=0. At phi=pi/2 the two packet states are exactly equal and each has stock 3/2. This point demonstrates the derived critical branch; it is not an adopted coefficient or chosen physical preparation.

Agreement is transient. When x=y=w, their difference derivative is minus 2kWw. It is nonzero for every nonzero nonharmonic equal state when k is nonzero. Thus the completed port can reach agreement but immediately carries the state out of it. The old invariant 15-dimensional agreement sector is not retained by this changed generator.

Keeping agreement would require another sourced operation, such as a justified port change or a different storage/continuation law. The present calculation does not insert such a switch at the favorable phase.

## Scientific gaps closed and next target

The finite operator search now separates three questions. A conservative port can change agreement; a square-zero realization requires a compatible incidence completion; and momentary agreement still does not establish retained membership. Each has an exact witness or obstruction in the chosen family.

The next source target is the local access and orientation contract for a coherence-changing port, followed by a state-complete rule that retains agreement. That rule must account for port context, donor support, signed interface information, continuation and reversal. It should be tested against the transient-agreement control before any geometric preference is ranked.

No cube, icosahedron or metric shape has been selected. The algebraic branch counts and accessibility subspaces do not supply growth probabilities or physical clustering rates. A broader ansatz with diagonal-boundary changes or auxiliary degrees of freedom remains a separate lawful development option.

## Verification

The executable passes 112 exact assertions. It independently exhausts the signed incidence space, certifies the linear and quadratic square-zero equations and every branch, checks literal-label restrictions and the harmonic gate, and verifies the signed launch and transient equal-copy control. The parent release replays exactly, including seven upstream releases. Fresh extraction of this release reproduces its result bytes exactly.

The archive retains all orbit matrices, branch bases, symbolic certificates, source reads, executable replay and risk records. These are conditional mathematical proofs and constructor checks, not independent scientific review or empirical confirmation. No canonical source, locked parent or public website is changed.
