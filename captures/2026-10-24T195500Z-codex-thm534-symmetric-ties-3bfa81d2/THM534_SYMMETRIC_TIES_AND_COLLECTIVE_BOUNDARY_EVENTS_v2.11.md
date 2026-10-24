# THM-534 v2.11: symmetric stalls and bounded collective boundary events

Development — no registry entry. Exact conditional mathematics on the original real carrier. Constructor verification only; independent review pending. Physical promotion 0.

## 1. Question and retained source

The v2.10 metric-activity rule can bootstrap a permitted empty core and is continuous across ties, but does it guarantee progress whenever some permitted native event moves the state? No. This note identifies a symmetric stall and proves that every deterministic equivariant selector restricted to disjoint whole-face stars must also stall there. A bounded collective event escapes that particular restriction without a new field register. Its use as a selection policy is an additional constitutive choice.

Retain Q169–Q173 real incidence transport, the unit support metric and Q177–Q179 fixed equal-share ownership. The other native grades remain unchanged during these face/core events. No frozen particle operator is revised. Q153, Q156 and G05 still do not supply an event objective, hard-permission dynamics, cost, renewal or physical action scale. The supplied CRL-2 subdivision document remains a governance proposal, not new scientific evidence.

Use the two-cell carrier with oriented cores \(\tau_0=[0123]\), \(\tau_1=-[0124]\). Order faces as \(012,013,014,023,024,123,124\), followed by the two core coordinates. Its face/core incidence is

\[
D=\begin{pmatrix}-1&1\\1&0\\0&-1\\-1&0\\0&1\\1&0\\0&-1\end{pmatrix}.
\tag{1}
\]

The native face generator satisfies \((G_fx)_f=-B_f\), \((G_fx)_\tau=d_{f\tau}x_f\), where \(B_f=\sum_\tau d_{f\tau}x_\tau\). Let \(W_f\) be that face and its incident cores. The conflict graph \(G\) has an edge precisely when two distinct \(W_f\) intersect. It consists of two four-vertex cliques sharing face 0. Each primitive event here means a whole Q173 face star, not a single incidence contact.

## 2. Exact stall criterion for the inherited activity rule

For fixed reference step \(0<\varepsilon\le1\), define

\[
s_f=\frac{\varepsilon^2(B_f^2+k_fx_f^2)}{1+k_f\varepsilon^2/4},\quad
r_f=[s_f-\max(0,s_g:g\sim f)]_+,\quad
w_f=\frac{r_f}{k_fE_f},
\tag{2}
\]

with \(k_f=n_3(f)\), \(E_f=\sum_{i\in R_f}x_i^2\), \(R_f=\bigcup_{g\in N[f]}W_g\), and \(w_f=0\) at \(E_f=0\). Hard face permissions \(h_f\) are supplied separately. The v2.10 map applies the disjoint positive-weight stars with steps \(\varepsilon h_fw_f\).

**Theorem T1 (all-permitted stall criterion).** With every \(h_f=1\), this map fixes \(x\) if and only if every face with positive score has a neighbor of at least that score:

\[
\Phi_\varepsilon(x)=x
\quad\Longleftrightarrow\quad
\forall f:\ s_f=0\ \text{or}\ \exists g\sim f:\ s_g\ge s_f.
\tag{3}
\]

**Proof.** A positive margin implies positive score and positive read stock. Conversely positive read stock cannot turn a positive margin into zero weight. Positive weights have disjoint write supports, and each executes a nonzero displacement, since its score is positive. Therefore the full map is the identity exactly when every margin vanishes. Expanding that condition gives (3). \(\square\)

This is a graph-local criterion, not a statement that any one tied maximum suffices to stall the entire carrier. Every positive singleton score plateau must lack a strict local maximum; equal-score neighboring faces can suppress one another regardless of whether higher scores exist elsewhere. For masked permissions, only permitted positive margins matter; the inherited competition still reads blocked neighbors.

At \(\varepsilon=1\), take the face-only state

\[
x_*=(0,1,-1,-1,1,1,-1,0,0),\qquad \|x_*\|^2=6.
\tag{4}
\]

Every private face has score \(4/5\); the shared face has score zero. Each private face is tied with the other two private faces of its core. All margins vanish, so \(\Phi_1(x_*)=x_*\), although each of the six permitted private-face unit Cayley events separately has positive displacement. The all-core state \((0,0,0,0,0,0,0,1,1)\) is a second exact stall with nonzero private-star activity. These are competition stalls, distinct from the condition \(G_fx=0\) for every face.

Continuity does not provide uniform progress near a stall. From the v2.10 Lipschitz increment bound, on this carrier

\[
\|\Phi_1(x_*+u)-(x_*+u)\|\le112\|u\|.
\tag{5}
\]

Hence any proposed positive lower throughput bound throughout a neighborhood of (4) fails. This does not preclude progress at asymmetric nearby preparations.

## 3. Symmetry obstruction beyond this particular score

**Theorem T2 (disjoint-star selection obstruction).** Suppose a deterministic selector assigns an independent set \(S(x,h)\) of whole-face stars and is equivariant under the actual signed carrier automorphisms. With all permissions on, at (4) it can select only the empty set or the shared face alone. Either choice produces no native motion at that state. The result does not assume the activity objective, the strict margin or continuity.

**Proof.** The even vertex cycle \(\rho=(0\ 1\ 2)\), fixing vertices 3 and 4, induces a signed carrier automorphism fixing \(x_*\) and the all-on permission vector. It fixes the shared face and has two three-face orbits: \(\{013,023,123\}\) and \(\{014,024,124\}\). The signs in (4) are precisely the incidences into their respective cores, so the signed action fixes the amplitudes. Equivariance requires \(S(x_*,1)\) to be a union of these face orbits. Each three-face orbit is a clique in the conflict graph and thus cannot lie in an independent set. Only the shared singleton remains, and \(G_0x_*=0\). \(\square\)

The theorem concerns a selector of disjoint whole-face stars followed by their native events. It does not cover an arbitrary direct state map, collective overlapping blocks, stochastic choices with sourced randomness, stateful priorities, asymmetric boundary data or a physically derived symmetry-breaking preparation. An unrecorded ordering of face IDs would abandon the specified equivariance. An extra register would need its own native source and transformation rule.

## 4. A local collective event that escapes the disjoint-star restriction

The obstruction points to event granularity as an explicit choice. For each core \(\tau\), let

\[
P_\tau=\{f\subset\tau:n_3(f)=1\},\qquad
H_\tau=\sum_{f\in P_\tau}h_fG_f.
\tag{6}
\]

These use only topologically private faces, with the original face-level hard permissions. Different cores' sets \(P_\tau\cup\{\tau\}\) are disjoint. Within one block, several native face stars overlap on the core and are solved together:

\[
\Psi_t(x)=\prod_\tau\operatorname{Cayley}(tH_\tau)x.
\tag{7}
\]

This is a boundary-only partial transport construction, not a derived universal selection law. Choosing to use private-face blocks and choosing \(t\) remain supplied policies. All shared-face amplitudes are unchanged by (7).

**Theorem T3 (bounded collective boundary map).** For fixed hard permissions and fixed finite \(t\), (7) is an orthogonal linear map, odd, equivariant with transformed permissions, and exactly inverted by \(t\mapsto-t\). On a tetrahedral simplicial complex each block reads and writes at most five real coordinates. It preserves the original signed midpoint and equal-share owned-cell receipts, and moves the symmetric state (4) without a symmetry-breaking priority.

**Proof.** Every \(H_\tau\) is a sum of original skew generators, hence skew; its Cayley transform is orthogonal and defined for real \(t\). Distinct blocks have disjoint coordinates and commute. Their partition is defined by face valence, so it is covariant under signed relabeling. The mask transforms alongside faces. Each tetrahedron has at most four private faces and one core, establishing the five-coordinate bound independently of total carrier size. Fixed-mask orthogonality gives Lipschitz constant 1 for the map. Reversing \(t\) inverts each fixed operator. These claims do not imply reversibility for a later state-dependent scheduler or permission law.

For an explicit local solve, let \(A_\tau=\{f\in P_\tau:h_f=1\}\), \(m=|A_\tau|\), \(b=x_\tau\), \(z=\sum_{f\in A_\tau}d_{f\tau}x_f\), and \(c=t/2\). When \(m>0\),

\[
b'=\frac{(1-mc^2)b+2cz}{1+mc^2},\qquad
x_f'=x_f-\frac{2cd_{f\tau}(b+cz)}{1+mc^2}
\quad(f\in A_\tau).
\tag{8}
\]

Other faces are unchanged. This follows by eliminating the leaf amplitudes from the Cayley midpoint equation. No global inverse is needed. With \(\bar x=(x+x')/2\), that equation yields

\[
J_{f\tau}=2t h_fd_{f\tau}\bar x_f\bar x_\tau,\quad
\Delta x_f^2=-J_{f\tau},\quad
\Delta x_\tau^2=\sum_{f\in P_\tau}J_{f\tau}.
\tag{9}
\]

Each private face has native ownership weight 1 in its core. Shared faces are fixed, so their equal shares are fixed. Thus every owned cell stock is unchanged, with exact signed internal receipts (9). \(\square\)

For (4), all permissions on and the declared model step \(t=1\), each block has \(m=z=3\) and \(b=0\). Equations (8) give

\[
\Psi_1(x_*)=(0,1/7,-1/7,-1/7,1/7,1/7,-1/7,12/7,12/7).
\tag{10}
\]

Each private contact receipt is \(48/49\); each core gains \(144/49\), for aggregate gain \(288/49\). Norm stays 6, and each owned cell stock stays 3. Both cell blocks run simultaneously on disjoint coordinates while the overlapping primitive face generators inside each block are treated jointly. This does not contradict T2, whose event alphabet excludes those joint blocks.

## 5. Limits and next source obligation

The boundary construction is deliberately limited. It never transports across a shared face; on a complex with no private faces it is the identity. The boundary of a four-simplex supplies an exact closed countercontrol: all ten triangular faces have valence two, so every private-face block is empty. Destructive cancellation within a collective block can also leave nonzero face stock dark: on the two-cell carrier, take only \(x_{013}=x_{023}=1\); their opposite incidence signs give \(z=0\), with \(b=0\), so (8) is the identity. Neither example guarantees progress on every nonzero preparation.

Signed backflow is explicit: applying (7) with \(t=1\) a second time to (10) sends both core amplitudes from \(12/7\) to \(24/49\), decreasing aggregate core stock. This is a deterministic fixed-mask linear control, not an endurance or reset-cycle result. The construction provides no reset, fairness, record carrier or open-system renewal. Fixed-permission linear isometry does not establish regularity for state-dependent hard admissions. A unit model step is not an action quantum or physical clock.

The new conclusion is therefore precise: permitted bootstrap plus continuous local response does not imply liveness; deterministic symmetry and disjoint whole-face selection can themselves force a stall; bounded collective boundary blocks remove that specific obstruction using original operators and metric. Boundary-only blocks cannot close the native bulk selection problem.

The strongest next source task is to specify an admissible collective-event cover for shared-face/bulk complexes, with bounded reads and writes, exact native receipts, transformed permissions and a causal commit rule. Test it on closed complexes with no private faces and symmetric ties before claiming general progress. Which cover, cost, objective, scheduling and renewal law the native source selects remains OPEN. No particle identification or physical action coefficient follows.

## 6. Reproducibility

The companion fresh `verify_symmetric_ties.py` uses only the Python standard library and exact `Fraction` arithmetic. It checks the stall criterion, both explicit stalls, all 128 independent-set candidates under the actual signed vertex cycle, the collective output (10), all 128 hard masks on 64 distinct rational states, exact norm/midpoint/ownership/inverse/odd identities, all twelve signed carrier symmetries, bounded read dependence and small asymmetric tie perturbations. These are finite constructor controls supplementing the proofs, not independent review or endurance validation. Imported historical scripts are not executed. Source versions and byte hashes are in the manifest and provenance record.
