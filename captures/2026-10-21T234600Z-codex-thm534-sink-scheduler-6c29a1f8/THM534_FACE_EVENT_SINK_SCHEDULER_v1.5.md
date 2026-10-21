# THM-534: conditional sink-reversal scheduler for local face events

## Scope and definitions

This is a new mathematical scheduling candidate for the face-star primitive in the captured v1.4 source. It does not supply a native UD contact-admission rule, initial schedule, action unit, particle identification, or physical clock. All proofs below are conditional on a supplied acyclic orientation of a fixed conservative conflict graph. Constructor verification is not independent peer review. Physical promotion remains 0.

Let a finite pure tetrahedral carrier have one unique coordinate per face and per cell. A face-star event at face \(f\) may change its face amplitude and the amplitudes of incident cells. Its potential footprint is

\[
P_f=\{f\}\cup\{\tau:f\subset\tau\}.
\]

Construct the simple graph \(G\) whose vertices are face events, with \(f\sim g\) exactly when \(P_f\cap P_g\ne\varnothing\). Potential footprints include disabled contacts; the graph remains safe as masks change within this declared family. It may therefore restrict concurrency more than an instantaneous mask requires. Additional interaction families require a new conflict audit.

For \(K_-=[0123]\cup(-[0124])\), ordered faces are \(012,013,014,023,024,123,124\). The conflict graph is two complete graphs on four vertices sharing the vertex \(012\). It has seven vertices, twelve edges, and nine independent pairs. The shared face conflicts with every other face. At most two events can run in a batch.

## Theorem 1: safe batches and persistence of acyclicity

Given an acyclic orientation, take any nonempty subset of its sinks as the next batch. Apply each selected local event, then reverse every edge incident to each selected sink. Attempts reverse edges even when the support map is the identity because its contacts are disabled.

**Proof.** Two adjacent vertices cannot both be sinks, because their edge has a direction. Thus batch footprints are disjoint. Each map reads and writes only its own footprint, so the batch maps commute, including their local mask evaluations when those evaluations depend only on that footprint. Alternatively masks may be fixed before the batch. Arbitrary mask dependence on other events' coordinates is outside this hypothesis. Edge reversals of the selected independent vertices also commute.

A finite acyclic graph has a sink: a directed path that could always be extended would repeat a vertex and create a directed cycle. Reversing one sink makes it a source. A new directed cycle cannot pass through that source; a cycle avoiding it would already have existed. Hence the orientation remains acyclic. An independent batch can be reversed one sink at a time, proving the batch assertion. Therefore every completed batch admits another attempt. This is a scheduling deadlock result, not a contact-opening or support-recovery result. \(\square\)

For reference the local exact map uses \(c_j=D_{fj}h_{fj}\), \(s=\varepsilon/2\), \(m=\sum_jc_j^2\):

\[
f'=\frac{(1-ms^2)f-2s\sum_j c_jt_j}{1+ms^2},\qquad
t_j'=t_j+s c_j(f+f').
\]

With midpoint amplitudes \(\bar f=(f+f')/2\), \(\bar t_j=(t_j+t_j')/2\), its receipts are

\[
J_j=2\varepsilon c_j\bar f\bar t_j,\quad
(f')^2-f^2=-\sum_jJ_j,\quad (t_j')^2-t_j^2=J_j.
\]

Indeed the map satisfies \(f'-f=-\varepsilon\sum_jc_j\bar t_j\) and \(t_j'-t_j=\varepsilon c_j\bar f\); multiply each equation by twice its midpoint. Squaring support and adding the receipts proves norm conservation. Products of disjoint maps preserve these receipts without shared-coordinate collisions. This does not assert that overlapping maps commute; v1.4 supplies their exact order counterexample.

## Theorem 2: bounded attempt fairness

Assume \(G\) is connected, finite, and every scheduling step executes a nonempty subset of sinks. Count individual event attempts, with any serialization of an independent batch. If the initial edge points \(u\to v\), then at every prefix

\[
0\le N_v-N_u\le1.
\]

**Proof.** Vertex \(u\) cannot fire until \(v\) reverses their edge. Thereafter \(v\) cannot fire again until \(u\) reverses it. Firings at other vertices cannot change this edge. Its endpoints therefore alternate, starting with \(v\). Independent simultaneous attempts never share this edge. \(\square\)

Consequently, along a shortest path,

\[
|N_u-N_v|\le d(u,v),\qquad
M=\sum_uN_u\le |V|N_v+\sum_ud(u,v).
\]

If \(N_v=0\), at most \(\sum_ud(u,v)\) individual attempts can have occurred. Thus every vertex receives an attempt within

\[
B_v=1+\sum_ud(u,v)
\]

individual attempts. The argument restarts at every prefix because the current orientation is again acyclic. This bounds subsequent waiting as well. On \(K_-\), \(B_{012}=7\) and \(B_f=10\) for each private face: the shared vertex has six neighbors, whereas a private vertex has three vertices at distance one and three at distance two.

These are bounds in individual scheduling attempts, not physical time, successful transfers, or support-reset counts. A rule that refuses to reverse a sink until its contact becomes ready violates the execution hypothesis. For disconnected graphs the distance bound applies to attempts within a connected component; an arbitrary subset scheduler can neglect another component. Full-sink batches avoid that particular neglect.

## Theorem 3: the initial orientation remains additional information

There are \(24^2=576\) acyclic orientations on this graph. Each complete four-vertex subgraph must have a total order, giving 24 choices. Every simple cycle lies in one clique because the cliques share only one articulation vertex. Hence independently acyclic orientations on the cliques give exactly all acyclic orientations of the union.

No orientation is invariant under the full carrier automorphism group \(S_3\times C_2\). For example, swapping shared vertices 1 and 2 exchanges the adjacent private faces \(013\) and \(023\). Their conflict edge would have to point both ways under an invariant orientation, which is impossible. Therefore a deterministic choice of a complete orientation from carrier geometry and uniform permissions alone cannot be equivariant under all these symmetries. This assertion concerns inputs without additional distinguishing state; it does not exclude choices using asymmetric amplitudes, stored history, or separately supplied orientation data.

A supplied orientation can be transported with a carrier relabeling; sink sets and edge reversal then transform covariantly by their definitions. This is a conditional graph statement, not an exhaustive signed-amplitude covariance test in this verifier. Neither conservation nor the local update formula selects one of the 576 possibilities. The verifier exhibits different first support histories from two supplied acyclic orientations while preserving exact norms and receipts.

The present graph is not bipartite: it contains complete four-vertex subgraphs. In particular all its event vertices cannot initially be sinks. Any earlier vertex–cell bipartite SER carrier, its initialization, and its event-count bounds must be audited separately before transfer. No historical SER source or native scheduling authority is inferred from this new proof. A limited search of consulted tracked docs/captures found no explicit sink-reversal specification; this is not a claim of repository-wide historical absence.

## Exact checks and resulting open obligation

The accompanying fresh standard-library verifier checks all 4,096 orientations and identifies all 576 acyclic ones. Each is replayed for 40 full-sink batches, checking independence, acyclicity, and the endpoint count invariant after every individual attempt. Every face first fires within seven batches in this finite control; the analytic 7/10 individual-attempt bounds hold. The finite seven-batch observation is not substituted for the general proof.

It also checks non-invariance under all 12 induced carrier automorphisms, all nine disjoint event pairs under all 256 incidence masks (2,304 exact rational commutation checks), local midpoint receipts, and seven all-off identity controls. Fixed masks are inputs in these controls, not reconstructed native admission predicates. Fraction arithmetic is exact; no numerical tolerance is used. Only newly authored code is executed.

This closes a conditional conflict-safety and bounded-attempt-fairness gap for the local face-event candidate. To identify it with UD dynamics still requires a source-grounded rule selecting or preparing the auxiliary orientation, an admissible contact law, and evidence connecting attempts to the desired support reset. The all-off identity controls explicitly show that fair attempts alone cannot establish recovery. This capture supplements v1.4 and supersedes no prior result.
