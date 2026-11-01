# UD-PM-PRED06-SEL-001 v1.0 — Symmetric K4 cannot deterministically select one seed or port

**Kind:** NO-GO (equivariance obstruction). **Status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0.

## Source and typed objects

Source: UD coefficient ledger v0.39 (2026-08-22), P01–P04 (`K4`, `S4`, eight opposite-edge parity states), Q153, Q156, Q162; `UD_Local_Source_Selection_v0.1.md` (2026-10-15), §3, supplied local edge/vertex gate; `UD_Native_Gate_Trigger_and_Recovery_v0.1.md`, §§1–2, source-gate nonidentifiability. Earlier PRED05-EVOL-001 (open UD PR #487) assumes a source vertex and a +z port; it does not derive them.

Let the labelled K4 be the simple graph on vertices \(V=\{0,1,2,3\}\) and edges \(E=\binom V2\). The automorphism group \(G=S_4\) acts on vertices, edges, permitted vertex burden vectors, typed gate masks and parity states. Let \(x_*\) denote a fully invariant input state: \(g\cdot x_*=x_*\) for all \(g\in G\). An admissible deterministic native selector \(F\) is assumed **equivariant**: \(F(gx)=gF(x)\). Equivariance formalizes the absence of a hidden vertex-address or geometric-direction choice. The state may include any fixed scalar or group-invariant readout.

## Theorem — no unique symmetry-respecting selection

There is **no** equivariant map selecting exactly one vertex \(F:X\to V\) at the fully symmetric state \(x_*\). There is likewise no equivariant unique edge or oriented port at \(x_*\). Even if a vertex \(v\) is externally seeded, an equivariant selector using only data invariant under its stabilizer \(G_v\cong S_3\) cannot select exactly one of the three incident edges.

**Proof.** Equivariance and invariance give \(F(x_*)=F(gx_*)=gF(x_*)\) for all \(g\in G\). Thus the selected vertex would have to be fixed by every permutation in \(S_4\), but no such vertex exists. The six undirected edges are also a single orbit without a globally fixed edge; neither does any oriented edge remain fixed. After seeding \(v\), the stabilizer of \(v\) permutes its other three vertices transitively, and hence permutes its incident edges transitively. No edge is fixed by all elements of \(G_v\). QED.

## Source-bound strengthening: diffusion cannot create contrast from a uniform state

**Additional hypotheses:** fix a K4 incidence matrix \(\partial_1\), all hard gates \(h_e=1\), no constitutive source \(s_B=0\), and use only the conditional Q162 relaxational current
\[
 j_e=-\tfrac14(\partial_1^\mathsf T b)_e,
 \qquad \dot b=\partial_1j=-\tfrac14\partial_1\partial_1^\mathsf T b.
\]
Since \(\partial_1^\mathsf T\mathbf1=0\), the uniform state \(b(0)=b_0\mathbf1\) has \(\dot b=0\), and uniqueness of this finite linear ODE implies \(b(\tau)=b_0\mathbf1\) for all model times. More generally, with \(\bar b=\frac14\mathbf1^\mathsf Tb\),
\[
\frac{d}{d\tau}\frac12\|b-\bar b\mathbf1\|^2
=-\frac14\|\partial_1^\mathsf Tb\|^2\le0.
\]
Thus this restricted conservative diffusion does not spontaneously generate a local burden maximum from exact uniform preparation.

## Counterexamples, scope, and dependency

The no-go applies **only** to invariant input data and equivariant deterministic rules. A nonuniform burden, asymmetric boundary condition, initial local parity defect, stochastic event, symmetry-breaking instability with a perturbation, or explicit control field can select an orbit representative. The proof does not exclude such branches. It does show that a unique source and +z contact cannot be deduced from symmetric K4 counts, Q162 mixing, and invariant reference data alone.

**Exact check:** all 24 vertex permutations were enumerated; no common fixed vertex/edge, and the vertex stabilizer has six elements permuting its three outgoing neighbors. A separate rational K4 Laplacian calculation gives spectrum \(\{0,4,4,4\}\) and dissipative contrast derivative \(-35/4\) for \(b=(4,3,2,0)\). These checks corroborate the general group/energy proofs.

**OPEN_GATED:** source law for a symmetry-breaking burden state; physical/local evolution and stochasticity; native seed/port selectability; SI clock and measurable readout. No physical claim promoted.
