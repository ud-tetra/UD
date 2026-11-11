# Atom-to-chain kinematic map audit v0.1

RESULT: SCOPED_NO_GO for the direct vertex/gradient route into the source's protected sector. Material graph verification PASS on36 configurations. Native600-cell identification and physical bath remain OPEN/HOLD. Physical promotion0.

## 1. Geometry-first definitions

Four original source configurations define two same-layer periodic atom graphs. Each atom selects its3 nearest distinct same-layer neighbors by lateral geometry alone; reciprocal edges, a clear distance gap to neighbor4, degree3 and connectivity are checked before using response data. Images in[-2,2]² cover the local neighbors in these supercells. The neighbor3/neighbor4 distance ratio is about1/sqrt(3), well below the frozen0.8 gap gate. The graph deliberately describes intralayer connectivity, not an interlayer bath-contact model.

| Pattern | Vertices | Edges | Components | Rank B | Cycle dimension |
| --- | ---: | ---: | ---: | ---: | ---: |
| (2,1) | 1008 | 1512 | 2 | 1006 | 506 |
| (3,1) | 1300 | 1950 | 2 | 1298 | 652 |

For oriented incidence B and the existing normalized replication map R_rep, the vertical vertex map is J0=R_rep and the z component of the vector bond-difference map is Jdiff=B^T R_rep. Both are defined without fitting to the response. Physical atom response is u=R_rep Q (Q^T Ksym Q)^-1 Q^T g, with uniform translation removed as before. The sign of equilibrium derivative is minus this quantity, which leaves all squared-norm fractions unchanged.

## 2. Exact gradient obstruction

Under the declared Euclidean edge/vertex metrics,

    Pcyc=I-B^T(BB^T)^+B,
    Pcyc B^T=0.

Proof: B^T annihilates the componentwise constants, which form ker(BB^T). Thus B^T(BB^T)^+(BB^T)=B^T. Equivalently im(B^T) is orthogonal to ker(B). Vertex displacement differences telescope around every graph cycle, including periodic cycles for the single-valued periodic displacements used here. This holds for any finite graph, not only the chosen intralayer graph.

For the source protected projector Pnative=diag(0,Pcyc_native,I,I), a vertex-only map is annihilated by its zero vertex block. Suppose a future dictionary supplies T0,T1 satisfying the exact gradient-intertwining condition

    T1 B_atom^T = B_native^T T0.

Then Pcyc_native T1 B_atom^T=0. A combined vertex/gradient map with no face/cell output therefore has no protected image. It cannot place a nonzero response wholly in that protected space. This is a conditional commuting-map obstruction, not an assertion that such a dictionary has been physically derived.

The result rejects this particular route to automatic geometric protection. It does not show every allowed port couples to the response: a separately sourced lower-rank port might still have another nullspace. It does not prove graphite has nonzero friction or refute all UD mechanisms. Consistent non-Euclidean metrics require their own adjoints/projectors and a metric-compatible dictionary; metric changes are not silently imported.

If an embedding annihilates the material response altogether, that is loss of the observable rather than evidence for protection of a nonzero embedded state.

## 3. Transverse differences and bond extension are different types

The response has only vertical atom components. For relaxed oriented bond r_e and unit vector n_e, Delta u_e=(0,0,(B^Tu)_e).

- Jdiff is the transverse z component of the vector bond-difference cochain. It is orientation-odd and a graph gradient.
- The bond-length rate ell_dot=n_e dot Delta u_e is orientation-even: both n_e and Delta u_e reverse when the edge orientation flips. It is not a signed C1 amplitude without a further representation rule.
- The axial vector a_e=n_e(n_e dot Delta u_e)=n_e n_e^T Delta u_e is orientation-odd. It is a valid3-component edge observable. Its edge-dependent projector generally does not preserve the gradient subspace.

Exactly planar intralayer bonds have n_z=0, so their first-order bond-length response to purely vertical motion is zero. That zero concerns a restricted observable; it is not zero dissipation or topological protection. The relaxed structures have small corrugation, so the axial vector is nonzero.

All36 responses have gradient cycle squared-norm fraction at most2.329560e-30. The axial vector cycle fraction ranges from0.100902330 to0.227517460; its remaining gradient fraction is nonzero throughout. The axial-vector norm is between1.183586e-03 and1.880664e-03 times the unprojected transverse bond-difference norm. These fractions normalize that selected observable only. They are not percentages of friction, thermodynamic energy or native UD protected stock. Result fields named energy_fraction mean Euclidean squared-norm fractions.

The intralayer edge map also annihilates uniform relative-layer breathing, because each layer is a separate graph component. The full vertex map retains it. Missing this signal in an edge-only observable cannot be interpreted as material protection.

## 4. Numerical and source verification

All36 configurations pass the frozen map checks. Four graphs pass degree, reciprocity, gap, component and projector tests. An iterative sparse least-squares projector independently corroborates the constructor's anchored-Laplacian projector. Orientation reversal checks separate signed axial vectors from unsigned length rates. Forty source structure/matrix hashes match. This is constructor verification, not independent review.

IMAGE_BOUND.json additionally certifies the periodic image search geometrically: every omitted image is farther than a constructive two-hop upper bound for the fourth-neighbor distance. This is a completeness verification, without changing the frozen graph rule or outcomes.

The first numerical run completed its MAPS.npz but failed JSON export on a NumPy boolean. The failed script and arrays are preserved under export_failure. Only the exporter changed; all200 saved arrays are exactly equal after regeneration. No numerical rule or threshold changed.

Native source: UD_Protected_Retention_Robustness_and_Port_Condition_v0.1.md, section2, freshly read at main c6b66d68a25b655627d6eb6f1bf6f96a13e2121b. Its port-image theorem remains conditional on its declared600-cell carrier and supplied port. The material graphs here are not that carrier: vertex/edge/cycle counts, representation and dynamics differ. No graph isomorphism, face/cell reconstruction, common metric or physical clock is inferred from this calculation.

## 5. Disposition and next gate

DERIVED: direct vertex/gradient maps do not write the native protected sector under a gradient-preserving dictionary. NUMERICAL: material graph and map decomposition pass on the declared configurations. CANDIDATE: the geometry-derived axial vector has mixed cycle content; whether it corresponds to a dynamically invariant native channel is unproved. OPEN: a source-authored carrier/metric/dictionary, constitutive port and physical bath. Bath identification HOLD; physical promotion0.

Next: test whether the axial-vector observable forms a closed dynamical channel under the qualified material operators and a source-compatible map. Reject any inference from nonzero cycle content alone. A source law must fix the map before independent response/friction tests; previously exposed arrays can only be development data.
