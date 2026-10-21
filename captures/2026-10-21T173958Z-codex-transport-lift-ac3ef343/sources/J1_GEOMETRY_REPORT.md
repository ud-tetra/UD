# J1 square pyramid: UD geometry investigation v0.1

Development — no registry entry. EXACT INTERNAL results below are constructor-checked mathematical statements; operator and horn models are explicitly conditional. No independent review or physical promotion (0). Refs #218, #136, #157.

## Result

The strongest UD role is a metric/incidence discrimination fixture and a square-port triangular shell, with an exact half-octahedron completion. A native law selecting the shape, a physical amplifier, and persistent clustering are not established.

## 1. Geometry audit

For a>0 the supplied Cartesian coordinates, height a/sqrt2, slant height sqrt3 a/2, internal dihedrals arccos(1/sqrt3) and arccos(-1/3), total area (1+sqrt3)a² and volume sqrt2 a³/6 are correct. Equal-edge convex J1 is the intended embedded realization, up to rigid motion/reflection and scale; connectivity alone would not fix an arbitrary folded assembly.

The net-fold wording needs convention discipline. From the flat outward net, rotate each triangular panel upward by pi-arccos(1/sqrt3), about125.264 degrees. Its final interior angle to the base is arccos(1/sqrt3), about54.736 degrees. Thus the supplied125.26 value is a fold rotation, not the final interior angle.

Solid uniform-density centroid is h/4. This does not apply to a fabricated hollow shell: the four side faces alone have centroid h/3; a uniform thin closed shell including the base has z=h sqrt3/[3(1+sqrt3)]. Material thickness and seam mass require their own model. The0.5-degree apex-drift statement supplies no tolerance theorem, and a universal thickness/kerf prescription is not established by the geometry.

The supplied STL facets have the intended orientation for positive finite a. Its edge-count function checks two facets per undirected edge; it does not check directed cancellation, connected vertex links, connectivity, self-intersection, degeneracy, Euler characteristic or the float32 serialization. Therefore its printed 'Chi=2 verified' and complete manifold certification overstate what that function computes. Add finite a>0 validation and validate the serialized mesh before fabrication. No submitted/archived script was executed in this investigation.

## 2. Half an octahedron, with a four-triangle port

Reflect the apex (0,0,h) to (0,0,-h). The convex union across the square is a regular octahedron: six vertices, twelve edges of length a, eight equilateral faces. The square is an equatorial section/internal gluing interface, not one octahedral boundary face. A square mouth distinguishes this object from tetrahedral triangular-face gluing. The symmetry is D4v for the embedded pyramid, versus tetrahedral Td; an equal second moment cannot identify their symmetry actions.

Removing the base leaves S=apex*C4, a triangulated disk with f=(5,8,4), Euler characteristic1, four mouth edges and apex link C4. A standard3-horn is three faces of one tetrahedron, f=(4,6,3), apex links according to that tetrahedral incidence. J1's shell is not that simplicial object; both being contractible does not supply a horn-filling theorem. 'Polyhedral horn' is a possible geometric/model description; retain this distinction.

## 3. The normal-frame identity and its limits

Order lateral outward unit normals north, west, south, east:

    n1=(0,sqrt(2/3),1/sqrt3), n2=(-sqrt(2/3),0,1/sqrt3),
    n3=(0,-sqrt(2/3),1/sqrt3), n4=(sqrt(2/3),0,1/sqrt3).

Their unweighted dyads satisfy sum_i n_i n_i^T=(4/3)I. This is the same second moment as the tetrahedral normal frame (ledger F03), but adjacent dot products are+1/3 and opposite dot products-1/3. Their oriented sum is(0,0,4/sqrt3), not zero. Alternating sign changes (+,-,+,-) give a regular tetrahedral Gram matrix; those changed vectors are not all outward normals of J1. This explains the shared unoriented frame geometry without identifying outward fluxes or face incidence.

Including the base outward normal -ez restores area-weighted vector closure. The area-weighted dyad of the complete boundary is

    sum_faces Area(f) n_f n_f^T = a²[(sqrt3/3)I + ez ez^T],

which is anisotropic. The exact4/3 lateral frame identity does not fix a full-boundary metric, coupling or action. F03 is a provenance comparison, not a new physical alias.

## 4. Filled J1 recovers Kminus incidence but changes geometric cells

Choose base diagonal V1V3. The two cells [apex,V1,V2,V3] and [apex,V1,V3,V4] share [apex,V1,V3], giving f=(5,9,7,2) and chain dimension23: the abstract two-tetrahedron Kminus complex. Each tetrahedron has five edges a and the diagonal sqrt2 a. Each volume is sqrt2 a³/12, equal to the volume of a regular edge-a tetrahedron, despite the differing shape. Neither cell is regular. Equal volume does not repair the metric discrepancy.

No choice of one diagonal is invariant under a quarter-turn: it exchanges V1V3 and V2V4. A geometric D4 symmetry does not act simplicially on that single triangulation. An invariant alternative adds the square center and four tetrahedra, changing the complex to f=(6,13,12,4). Comparing refinements needs a declared transfer/metric/observable contract, not merely equal outer shape.

## 5. Exact chain-operator comparison

Use the UD unweighted real skew Hodge-Dirac convention with off-diagonal blocks B_k,-B_k^T and the identity metric on every simplex register. The exact integer characteristic polynomial calculations give:

| Object | f vector | Characteristic polynomial | Frequencies, multiplicity per sign |
|---|---|---|---|
| Open four-face shell | (5,8,4) | lambda(lambda²+1)(lambda²+3)^4(lambda²+5)^3 | 1 once; sqrt3 four; sqrt5 three |
| Filled diagonal J1 | (5,9,7,2) | lambda(lambda²+3)^4(lambda²+5)^7 | sqrt3 four; sqrt5 seven |

Both have one zero mode and no nonzero global recurrence period, because their active irrational frequency ratios cannot share a finite period. These are chain-parameter frequencies, not Hz. The filled result reproduces ledger Q174 by incidence and the explicitly selected unit chain metric. It is insensitive to the long Euclidean diagonal under this convention. A metric-sensitive realization may differ. Geometry does not itself justify using identity metric or identify the physical field.

## 6. Conditional horn transport test

An open, hard-walled hollow pyramid could be investigated as a duct only after declaring medium, wall/throat/mouth boundary conditions, losses and readout. With z measured from the square base toward the apex, its cross-sectional area is A(z)=a²(1-z/h)². Under an ASSUMED lossless one-dimensional Webster model, p''+(A'/A)p'+k²p=0 becomes, for r=h-z,

    p_rr + (2/r)p_r + k²p=0,
    p(r)=[C sin(kr)+D cos(kr)]/r, k>0.

Bounded pressure at a closed sharp apex forces D=0. Then A times axial pressure gradient tends to0, so the regular solution carries no finite through-flow through a point throat. The sharp-tip shape is not a finite-throughput two-port horn. Truncating at r=r0>0 gives a finite throat and an area ratio(h/r0)²; actual transmission, gain or mode selection still requires the declared boundary/source model. This is a conditional derivation, not a claim that a one-dimensional approximation describes this broad pyramid accurately.

## 7. Next decisive work

1. Freeze a metric-sensitive operator, state and square-port observable, then compare J1, regular Kminus and the center refinement under explicit transfer maps.
2. If horn behavior is the target, choose a finite throat and a passive medium/boundary model; compare against equal-length/equal-volume controls before interpreting concentration as amplification.
3. Test persistence or clustering only after a source/contact/energy law predicts it. Shape catalog membership, the common4/3 identity and equal cell volumes do not select that law.

## Sources and replay

The geometry is derived from the user-supplied coordinates; verify_j1.py independently constructs boundaries and computes characteristic polynomials over integers, with exact rational metric checks. Run `python3 verify_j1.py` outside mutable output paths; RESULTS.json records23 constructor assertions. The spectral statement is a finite exact algebraic check, not an independently reviewed result. No archived program executed.

Read attached UD Coefficient Provenance Ledger v0.39 (F03, Q169-Q179) and the attached CRL2 amendment. The latter explicitly labels itself a governance proposal; this turn does not enact it or create a registry promotion. The supplied packet_modulation_layer.md and seam_phase_transport.md contain placeholder text, so they cannot support a transport-law claim.

External checks: https://mathworld.wolfram.com/SquarePyramid.html (J1 and geometry); Bastiaan Cnossen, Stable homotopy theory and higher algebra, section1.6 definition1.6.5: https://bastiaancnossen.com/notes/stable-homotopy-higher-algebra/section/introduction-to-infinity-categories/simplicial-objects-and-quasicategories/index.html (standard horn definition). No external transport formula is treated as an established UD source law.
