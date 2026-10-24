# THM-534: native execution, event cost and the bootstrap frontier

Development — no registry entry. Exact deductions and countercontrols for the v2.8 native-carrier prototype. Constructor checked; independent review pending. Physical promotion 0.

## 1. Fixed source boundary

Retain the original real face/core amplitudes, signed incidence matrix, metric and equal-share ownership. Q171–Q173 provide signed currents and hard face multiplication; Q153/Q156 do not uniquely specify the response or hard-permission changes. No new physical carrier or action unit is introduced here.

For a face f, let W_f be its face-plus-incident-core write set, and G the face conflict graph: f and g are adjacent exactly when W_f intersects W_g. The v2.8 prototype reads

\[
R_f=\bigcup_{g\in N_G[f]}W_g
\]

and uses the score, margin and locally normalized weight

\[
s_f=[2x_f\sum_\tau d_{f\tau}x_\tau]_+,
\quad r_f=[s_f-\max(0,s_g:g\sim f)]_+,
\quad w_f=r_f/(k_f E_f),\quad E_f=\sum_{i\in R_f}x_i^2,
\tag{1}
\]

with zero weight at zero read stock and a separately supplied frozen hard permission. A local event T_f reads the current R_f atomically and applies the star Cayley map with that frozen weight, writing only W_f. Equations (1) and the step convention remain candidate response choices. The results below preserve the earlier conservation and locality theorems; they do not promote selection to a native law.

## 2. The correct execution-conflict graph is G squared

Write-disjoint events can still read one another's writes. Define the declared read/write conflict graph H by an edge when either

\[
W_f\cap R_g\ne\varnothing\quad\text{or}\quad W_g\cap R_f\ne\varnothing.
\tag{2}
\]

**Theorem X1.** H is the graph square G squared: distinct faces conflict in H exactly when their distance in G is at most two.

**Proof.** W_f intersects R_g exactly when it intersects W_a for some a in N_G[g]. Intersecting write sets means f=a or f adjacent to a. This is equivalent to a G-path from f to g of length at most two. The same argument applies in the other direction. \(\square\)

On \(K_-\), G consists of two four-cliques sharing the shared-face vertex. It has 12 edges and diameter two. Hence H is the complete seven-vertex graph with 21 edges. Under this conservative declared-footprint protocol, the largest universally read/write-independent batch has size one. This does not assert that all particular event maps fail to commute at every state; it states which pairs are safe without additional data-specific proof or coordination.

For tetrahedral pseudomanifolds with face valence at most two, G has degree at most six, so H has degree at most 36. The v2.8 bounds of at most 15 real reads and three field writes per event remain valid. Execution conflicts remain bounded-neighborhood conditions on this geometric class, rather than a whole-carrier dependency. This class assumption is not extended to unbounded-valence nonmanifolds.

**Theorem X2.** If f and g have distance at least three in G, their current-read local event maps commute, even when each weight is evaluated afresh at its execution. Any finite sequence of valid current-read events conserves original support norm and the exact Q177–Q179 owned receipts. Every executed event with positive weight has positive aggregate core-stock gain for the stated step range.

**Proof.** Distance at least three gives both read/write intersections in (2) empty, including write/write intersections. Neither event changes the other's read values or local input amplitudes. Both use identical coefficients and input coordinates in either order; their writes are disjoint, so they commute. Each individual event has the skew-star Cayley and midpoint receipts proved in v2.8. Summing these receipts in actual execution order gives the sequence result. \(\square\)

This gives a sufficient *computational execution contract* without one global field snapshot: obtain a consistent local read, exclude conflicting writes until commit, evaluate the weight, apply the event, then release. Shared reads and exclusive writes, version validation, or a causal read certificate could implement it. Such lock/version/record registers and their costs are not native-source derived here. Choosing who acquires a conflicting event, fairness, retries and a physical clock remain OPEN. Changing hard permissions concurrently requires its own read/write account.

An exact countercontrol uses \(x_0=-1/2,\ x_1=x_2=2,\ x_7=1,\ x_8=-1\) and other coordinates zero. Faces 013 and 014 initially have disjoint writes and weights 8/25. Frozen maps commute, but maps with intermediate weight recomputation do not. Thus the original snapshot dependence cannot be removed merely by saying the active stars have disjoint support.

## 3. Aggregate versus mean is an event-cost question

Let the signed instantaneous gain of total incident core stock be

\[
j_f=2x_f\sum_\tau d_{f\tau}x_\tau.
\tag{3}
\]

For a declared finite comparison set and positive costs c_f, consider the *additional allocation model*

\[
\max_{a_f\ge0}\sum_fj_fa_f
\quad\text{subject to}\quad\sum_fc_fa_f\le1.
\tag{4}
\]

**Theorem X3.** The optimal value is \(\max(0,\max_f j_f/c_f)\). When that value is positive, allocating to a maximizing face is optimal; uniqueness requires a unique maximizing density.

**Proof.** Let M be the stated nonnegative maximum. Then sum j_f a_f is at most M sum c_f a_f, which is at most M. If M>0, choose a_f=1/c_f at a maximizing face and zero elsewhere. If no density is positive, a=0 attains zero. \(\square\)

A cost of one per face event produces the aggregate-current ranking. A cost \(c_f=k_f\) per incidence channel produces the mean-current ranking. At the v2.8 symmetric state, the shared face has j=4,k=2 and private faces have j=2,k=1: face-unit cost gives a unique shared-face optimum, while incidence cost gives a seven-way density tie. The v2.8 mean-margin rule abstains at that tie; optimization (4) itself does not require abstention.

The optimization is a conditional local comparison model, not a derivation of a global scheduler or of v2.8's precise margin and normalization. The missing assumption is the objective and resource cost of an event. Native counts of faces and incidences do not identify which cost should govern a physical action allocation. No numerical fit or physical action constant is supplied. This sharpens the source target rather than selecting aggregate flow by convention and calling it derived.

## 4. A new bootstrap counterexample with hard permission already open

Prepare one private face amplitude \(x_{013}=1\) and every core amplitude zero, with all other amplitudes zero. Permit that face geometrically. Every instantaneous j_f is zero, hence all margins and weights in (1) vanish. The v2.8 prototype stays fixed despite nonzero available face stock and open hard permission.

The original permitted private-face Cayley event with model step one is instead

\[
(x_f,x_\tau)=(1,0)\longmapsto(3/5,4d_{f\tau}/5),
\quad \Delta x_\tau^2=16/25.
\tag{5}
\]

It preserves norm and owned-cell stock exactly. Thus the native transport operator is capable of filling an empty core; the candidate instantaneous-current predicate blocks the event. This is stronger than the all-hard-permissions-off obstruction, and does not invalidate v2.8's scoped positive-margin proofs, which never guaranteed universal reopening.

**Theorem X4 (continuous monotone bootstrap obstruction).** Let \(x=(y,z)\) be signed real face/core coordinates. Suppose a locally Lipschitz, memoryless vector field F is defined on a full neighborhood of the zero-core slice, and at every point in that neighborhood

\[
\frac{d}{ds}\|z\|^2=2z^{\mathsf T}F_z(y,z)\ge0.
\tag{6}
\]

Then \(F_z(y,0)=0\) on that slice, and its unique local flow cannot bootstrap from all cores zero.

**Proof.** If v=F_z(y,0) were nonzero, choose z=-t v for positive t tending to zero. Continuity gives

\[
z^{\mathsf T}F_z(y,z)=-t\|v\|^2+o(t)<0,
\]

contradicting (6). Thus F_z vanishes at every zero-core point. Restricting the field to z=0 gives a solution on that submanifold; local uniqueness keeps the full solution there. \(\square\)

The theorem uses signed real amplitudes and monotonicity at every nearby state, not just on one chosen trajectory. It does not exclude finite events, fields allowed to reduce core stock temporarily, extra memory/source registers, or a different restricted state domain. It does not forbid ordinary skew transport: its core stock derivative has both signs near z=0. The native step (5) shows why event-endpoint gain and everywhere-monotone continuous gain must not be conflated.

For the v2.8 inward-only finite event rule, total core stock is also a Lyapunov account. Along any sequence of its valid events, aggregate gains are nonnegative and

\[
\sum_n\Delta C_n=C_\infty-C_0\le\|x_0\|^2-C_0,
\quad C=\sum_\tau x_\tau^2.
\tag{7}
\]

If infinitely many events execute, their aggregate gains tend to zero. This rules out a uniform positive gain per event forever in this closed inward-only programme; it is not a no-go for circulation, reverse contacts or an open source/renewal mechanism.

## 5. Concrete next source test

The next readiness object should distinguish an instantaneous derivative from an actual permitted event receipt. For a declared event convention epsilon, the local prospective quantity

\[
g_f^{\rm event}(x;\varepsilon)
=C(\operatorname{Cayley}(\varepsilon G_f)x)-C(x)
\tag{8}
\]

is computable on the native write star and detects (5). This is a typed diagnostic, not yet a replacement gate law. Before using it in competition, derive the event cost and step convention, show the response is continuous at ties, and verify the *executed* gain after any margin-dependent rescaling. Positive gain at one proposed step does not automatically establish gain at a different scaled step. Preserve fixed hard permission and local read/commit semantics.

The priority is now specific: source an event-cost/clock convention and a causal local read/commit account, then test finite-event readiness on empty cores, competing ties, asymmetric incident cores and resource renewal. Do not promote a numerical scheduler or a receipt identity into a native source law. Independent review pending. Physical promotion 0.
