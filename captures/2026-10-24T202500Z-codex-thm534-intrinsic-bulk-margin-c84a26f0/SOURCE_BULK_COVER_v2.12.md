# THM-534 v2.12: a bounded bulk cover and its cyclic selection obstruction

Development — no registry entry. Exact conditional mathematics and candidate event decomposition. Constructor checked; independent review pending. Physical promotion 0.

## 1. Purpose and assumptions

The v2.11 private-face collective event does nothing on closed complexes. Here a cell-centered cover includes every shared face while retaining complete Q173 face stars. Each local Cayley solve uses at most nine original real coordinates. This closes a bounded-execution construction problem, not the source of a native selection law. A closed-complex symmetry counterexample shows why these are distinct tasks.

Let \(K\) be a finite pure tetrahedral simplicial complex with triangular face valence \(1\le k_f=n_3(f)\le2\). Boundary is permitted. Use the original real face/core carrier with unit metric, incidences \(d_{f\rho}\), separately supplied hard face permissions \(h_f\in\{0,1\}\), and the fixed Q177–Q179 equal-share ownership. Other native grades remain unchanged during the events studied here. The face/core generator is

\[
(G_fx)_f=-\sum_{\rho\supset f}d_{f\rho}x_\rho,
\qquad (G_fx)_\rho=d_{f\rho}x_f,
\qquad G_f^{\mathsf T}=-G_f.
\tag{1}
\]

The full graded Hodge–Dirac operator is not replaced by its face/core restriction as a physical model. The frozen particle operators and metric are unchanged inputs. Q153/Q156/G05 leave constitutive flux, hard readiness, scheduling, renewal and physical action normalization open. The supplied CRL-2 subdivision text is a governance proposal and supplies no new constitutive dynamics.

## 2. A complete cover by bounded local generators

For each tetrahedron \(\tau\), define

\[
H_\tau^h=\sum_{f\subset\tau}\frac{h_f}{k_f}G_f,
\qquad
W_\tau=\{f:f\subset\tau\}\cup
\{\rho:\exists f\subset\tau,\ f\subset\rho\}.
\tag{2}
\]

The second set consists of core coordinates, including \(\tau\). A whole face star is included whenever its face occurs in the central cell; contacts into neighboring cores are retained. Shared-face coefficients are not truncated at the central core. The declared set \(W_\tau\) is a maximal read/write footprint; hard-off faces can reduce the actual footprint.

**Theorem B1 (bounded generator cover).** For fixed permissions,

\[
\boxed{\sum_\tau H_\tau^h=\sum_fh_fG_f=:A_{23}^h,}
\qquad |W_\tau|\le9.
\tag{3}
\]

Each local event

\[
C_\tau^h(t)=
\left(I-\frac t2H_\tau^h\right)^{-1}
\left(I+\frac t2H_\tau^h\right)
\tag{4}
\]

exists for every real finite \(t\), is orthogonal, odd, and an isometry on the original real carrier. Its inverse is \(C_\tau^h(-t)\). The event family is covariant under actual signed carrier automorphisms, with both central cell and permissions transformed. Only a local system of size at most nine must be solved.

**Proof.** Each face is contained in exactly \(k_f\) tetrahedra, so its coefficient in the sum is \(k_fh_f/k_f=h_f\). A tetrahedron has four faces. At valence at most two, each face introduces at most one additional core beyond the central core, giving four faces and at most five cores. Distinct tetrahedra in a simplicial complex cannot share two different triangular faces, so the neighboring cores are distinct when present. Each summand in (2) is skew; the real matrix \(I-tH_\tau^h/2\) is invertible, and the standard Cayley transpose identity gives orthogonality. The operator is zero outside \(W_\tau\). The support, incidence signs, valences and equal allocation transform under relabeling, proving covariance. \(\square\)

The factor \(1/k_f\) is the unique allocation that is constant across a face's cofaces and sums to one. Those two requirements derive this counting partition. They do not derive that the native dynamics should use this particular event decomposition or treat its coefficients as physical conductances. The equality in (3) is a generator identity, not an equality between a sweep of finite events and one Cayley event of the sum.

## 3. Signed support and owned-cell receipts

**Theorem B2 (exact native receipts).** Let \(x'=C_\tau^h(t)x\), \(m=(x+x')/2\), and

\[
\alpha_f=\frac{h_f}{k_f}\mathbf1_{f\subset\tau},
\qquad J_{f\rho}=2t\alpha_fd_{f\rho}m_fm_\rho.
\tag{5}
\]

Then

\[
\Delta x_f^2=-\sum_\rho J_{f\rho},
\qquad \Delta x_\rho^2=\sum_fJ_{f\rho}.
\tag{6}
\]

For native owned face/core stock

\[
O_\eta=x_\eta^2+\sum_{f\subset\eta}\frac{x_f^2}{k_f},
\]

the exact receipt is

\[
\boxed{\Delta O_\eta=
\sum_{f,\rho}\left(
\mathbf1_{\rho=\eta}-\frac{\mathbf1_{f\subset\eta}}{k_f}
\right)J_{f\rho},\qquad \sum_\eta\Delta O_\eta=0.}
\tag{7}
\]

**Proof.** The Cayley midpoint equation is \(x'-x=tH_\tau^hm\). Multiply each coordinate equation by twice its midpoint to obtain (6), then substitute (6) into the definition of \(O_\eta\). Summing the ownership coefficients in (7) gives \(1-k_f/k_f=0\) for each contact. Unchanged lower-grade coordinates add zero to their full native owned-cell receipts. \(\square\)

Unlike the private-face-only construction, an individual bulk event can redistribute owned stock between cells. Zero change in every individual owned stock is not asserted. Transfers remain signed; neither core stock nor a physical energy is required to increase.

## 4. Read/write conflicts and a conditional execution protocol

Let \(T\) be the dual graph of tetrahedra sharing a triangular face. Its degree is at most four. Each \(W_\tau\) contains the four central faces and the closed dual neighborhood's core coordinates.

**Theorem B3 (declared conflict graph).** For distinct central cells,

\[
W_\tau\cap W_\sigma\ne\varnothing
\quad\Longleftrightarrow\quad
\operatorname{dist}_T(\tau,\sigma)\le2.
\tag{8}
\]

Consequently the declared read/write conflict graph is \(T^2\), of maximum degree at most 16. A proper coloring with at most 17 colors exists. For a supplied coloring and supplied color order, each color is a set of disjoint local events that commute, and a sweep of all colors preserves norm and accumulated signed receipts.

**Proof.** Shared face coordinates require dual distance one. The sets of core coordinates intersect precisely when the closed dual neighborhoods intersect, equivalent to distance at most two. If the centers are disconnected or farther apart, neither type of coordinate intersects. The square-degree bound is \(4+4\cdot3=16\); the usual greedy coloring argument gives 17. Disjoint operators commute. Apply B1 and B2 event by event and sum the actual local receipts. \(\square\)

This is a conditional implementation with constant local field footprint. The coloring, ordered sweep, permission consistency and causal record are extra inputs. No native priority is derived by assigning integer color IDs. A current-read implementation may commit disjoint events using a consistent read and permission snapshot, then recompute/read for later colors. It requires a sourced protocol for locks or versions and outgoing records; their existence is not supplied by a matrix identity. Overlapping events need not commute. A full sweep is generally order dependent and is not asserted to be the native finite-time flow.

For frozen permissions, any complete fixed ordering satisfies the small-model-step expansion

\[
\prod_\tau C_\tau^h(t)=I+tA_{23}^h+O(t^2).
\tag{9}
\]

This follows by expanding each finite factor. It is a finite-carrier consistency statement. It supplies neither a physical clock nor a state-dependent selection law, and no carrier-size-uniform error estimate is claimed.

## 5. Closed-complex cyclic counterexample

Take the boundary of the four-simplex on vertices \(0,1,2,3,4\). It has five tetrahedra and ten triangular faces; every face has valence two. List faces and cores lexicographically. Orient core \(\tau_i\), which omits vertex \(i\), by \((-1)^i\) times ascending order. Every block has four faces and all five cores, so \(|W_\tau|=9\), and the declared block-conflict graph is \(K_5\).

Let \(\rho=(0\ 1\ 2\ 3\ 4)\) act by the actual signed simplex action. Define a face-only preparation by summing the signed orbit of the ascending face \([012]\):

\[
x_* = \sum_{r=0}^4\rho^r e_{012}.
\tag{10}
\]

In lexicographic face order \(012,013,014,023,024,034,123,124,134,234\), followed by the five cores, this is

\[
x_*=(1,0,1,0,0,1,1,0,0,1;\ 0,0,0,0,0),
\quad \|x_*\|^2=5.
\tag{11}
\]

All hard permissions are one. The state and permissions are fixed by \(\rho\); the five central-cell blocks form one transitive orbit. Each block is active: its native collective Cayley event at \(t=1\) changes (11). For the block centered on the first lexicographic cell \([0123]\), the exact output is

\[
x'=(15/17,0,1,0,0,1,15/17,0,0,1;\ 0,8/17,0,0,-8/17).
\tag{12}
\]

Its norm remains 5. The five native owned-stock changes, in lexicographic core order, are

\[
\Delta O=(-64,32,0,0,32)/289.
\tag{13}
\]

**Theorem B4 (cyclic block-selection obstruction).** At (11), any deterministic equivariant selector restricted to disjoint blocks from (2) must select the empty batch, although each block separately has nonzero displacement.

**Proof.** Equivariance at a state fixed by \(\rho\) makes the selected block set invariant under its transitive action. Such a set is either empty or all five blocks. All five conflict in \(K_5\), leaving only the empty independent set. Nonzero displacement follows from (12) and covariance under \(\rho\). \(\square\)

There is a second caution: merely summing the blocks does not restore progress at this preparation. Directly from the incidences,

\[
D^{\mathsf T}(x_*)_{\rm face}=0,
\qquad A_{23}^{1}x_*=0.
\tag{14}
\]

Thus the single Cayley map of the sum is the identity on (11), despite every separate block being active. Equation (14) concerns only this face/core sector; it is not a claim that the full graded Hodge–Dirac generator annihilates the preparation. Equation (12), in contrast, requires an actual choice of central block. A serial ordering can move the state but is additional symmetry-breaking scheduling data. The verifier also supplies an exact noncommuting two-block control on a generic rational preparation.

## 6. Source disposition and next frontier

This package supplies a complete bounded cover of the hard-gated face/core generator, a nine-coordinate local event, exact shared-face ownership transfers, and the precise dual-square conflict graph. It also shows that bounded collective granularity alone does not derive liveness or a native choice of event. Conditional coloring and serial consistency do not remove the cyclic obstruction.

Candidate choices remain explicit: coface-neutral event allocation, Cayley discretization, model step, chosen cover, priority/record carrier, admission and renewal. No coefficient is fitted to physical targets; the historically exposed particle and action targets are not reclassified as prospectively blind. No action unit, physical energy, physical clock, quark/lepton map or registry promotion is inferred.

The next source task is to determine whether native causal records, actual asymmetric preparation data, or an admissible alternative joint event supply the missing selection information. Any proposed closure must retain the cyclic closed-complex preparation, all-hard-off states, collective cancellation, signed backflow and serial-order dependence as countercontrols. Adding a record or random choice requires its own carrier, transformation law, cost and renewal receipts. A geometric cover is a prerequisite for that analysis, not evidence those sources already exist.

## 7. Reproducibility

The newly authored `verify_bulk_cover.py` uses exact standard-library `Fraction` arithmetic. It checks all 1,024 face-permission masks for the closed-complex generator partition and one central event's norm/receipts/inverse; 80 additional state/central-block cases; all 120 signed vertex permutations on the five block choices; bounded read dependence; conflict-graph identities on a pair, strip, four-neighbor star and closed boundary; and the cyclic invariant independent batches, explicit output, ownership transfer, cancellation and order countercontrols. These finite constructor checks supplement the proofs. They are not independent review or long-time validation. Source snapshots and hashes are preserved in the companion manifest.
