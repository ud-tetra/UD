# THM-534 v2.14: intrinsic bulk activity margins and their execution radius

Development — no registry entry. Exact conditional response on original native coordinates; constitutive policy remains candidate. Constructor checked; independent review pending. Physical promotion 0.

## 1. Scope

The v2.13 record theorem does not forbid selection from an already asymmetric native field. Here the v2.12 bulk cover supplies a finite-event activity diagnostic. Strict local activity margins give a continuous field update on the original real face/core carrier, without added mark registers. The construction moves an explicit open set of asymmetric preparations but still stalls at the cyclic symmetric preparation. Its choice of objective is not derived from native conservation alone.

Let \(K\) be a finite pure tetrahedral simplicial complex, with triangular face valence \(1\le k_f\le2\). Retain the unit support metric, signed face generators \(G_f\), fixed hard face permissions \(h_f\), and Q177–Q179 ownership. Other grades remain unchanged during these events. No frozen particle operator or metric is revised. The candidate bulk block centered at cell \(\tau\) is

\[
H_\tau^h=\sum_{f\subset\tau}\frac{h_f}{k_f}G_f,
\qquad C_\tau^h(t)=\operatorname{Cayley}(tH_\tau^h).
\tag{1}
\]

Its declared write/read footprint \(W_\tau\) consists of the four central faces and cores incident to those faces, at most nine real coordinates. The dual cell graph \(T\) has degree at most four. Distinct block footprints intersect exactly at dual distance at most two, so the primitive block-conflict graph is \(T^2\). Each (1) retains whole Q173 face stars, including neighboring-core contacts. The coface-neutral decomposition, Cayley convention and model step are still supplied choices.

## 2. An intrinsic finite-activity response

Fix a dimensionless reference step \(0<\varepsilon\le1\). Define

\[
s_\tau(x,h)=\|(C_\tau^h(\varepsilon)-I)x\|^2,
\quad
r_\tau=\left[s_\tau-\max\bigl(0,s_\sigma:
0<\operatorname{dist}_T(\tau,\sigma)\le2\bigr)\right]_+.
\tag{2}
\]

The score is the exact metric displacement of a supplied reference native block event, with hard permissions included. It is not an inward-stock score or a physical action. Set

\[
R_\tau=\bigcup_{\sigma\in B_T(\tau,2)}W_\sigma,
\quad E_\tau=\sum_{i\in R_\tau}x_i^2,
\quad
w_\tau=\begin{cases}r_\tau/(4E_\tau),&E_\tau>0,\\0,&E_\tau=0.\end{cases}
\tag{3}
\]

Use weights computed from one consistent pre-event snapshot, and execute the positive-weight blocks at actual steps \(t_\tau=\varepsilon w_\tau\):

\[
\boxed{\Phi_\varepsilon^h(x)=
x+\sum_\tau(C_\tau^h(\varepsilon w_\tau(x,h))-I)x.}
\tag{4}
\]

No mark is generated or stored. Existing field asymmetry is read directly. Hard permission is not newly predicted by this response.

**Theorem I1 (disjoint events and exact receipts).** The weights satisfy \(0\le w_\tau\le1\). Positive weights have disjoint write footprints, so (4) is equivalently their commuting product. It preserves the original support norm, is odd and homogeneous in the field, and is covariant under actual signed carrier automorphisms with transformed permissions. Every positive-weight block executes a nonzero metric displacement. If all cores are initially zero and some block has positive weight, the update creates positive core stock. The original signed midpoint and owned-cell receipts hold with actual step \(\varepsilon w_\tau\).

**Proof.** Write the block as a skew off-diagonal incidence matrix with rectangular part \(M_\tau\). Its squared Frobenius norm is

\[
\|M_\tau\|_F^2=
\sum_{f\subset\tau}\sum_{\rho\supset f}
\left(\frac{h_fd_{f\rho}}{k_f}\right)^2
=\sum_{f\subset\tau}\frac{h_f}{k_f}\le4.
\tag{5}
\]

Hence \(\|H_\tau^h\|\le2\). The Cayley resolvent of a real skew matrix has norm at most one, giving \(\|C_\tau^h(\varepsilon)-I\|\le2\varepsilon\). Thus \(s_\tau\le4E_\tau\) and \(w_\tau\le1\). Conflicting positive margins would require both \(s_\tau>s_\sigma\) and \(s_\sigma>s_\tau\). Consequently active footprints are disjoint, and their orthogonal events preserve norm. Moreover

\[
C_\tau^h(t)-I=t(I-tH_\tau^h/2)^{-1}H_\tau^h.
\tag{6}
\]

A positive score implies \(H_\tau^hx\ne0\), so (6) gives positive executed displacement at the positive actual step. For a zero initial core vector and face vector \(a\), the core output satisfies \((I+t^2M_\tau M_\tau^{\mathsf T}/4)b'=tM_\tau a\). An active block has \(M_\tau a\ne0\), so the invertible left factor gives \(b'\ne0\). Disjoint active blocks cannot cancel these outputs. The scores and read stocks are even quadratic forms; the weights are invariant under nonzero common field scaling. This proves oddness and homogeneity, including the zero extension. Signed covariance follows from the native incidence/metric action and the geometric read sets.

For an actual active event with midpoint \(m\), put

\[
J_{f\rho}=2\varepsilon w_\tau\frac{h_f}{k_f}
\mathbf1_{f\subset\tau}d_{f\rho}m_fm_\rho.
\tag{7}
\]

The midpoint equation gives \(\Delta x_f^2=-\sum_\rho J_{f\rho}\), \(\Delta x_\rho^2=\sum_fJ_{f\rho}\). For \(O_\eta=x_\eta^2+\sum_{f\subset\eta}x_f^2/k_f\),

\[
\Delta O_\eta=\sum_{f,\rho}
\left(\mathbf1_{\rho=\eta}-\frac{\mathbf1_{f\subset\eta}}{k_f}\right)J_{f\rho}.
\tag{8}
\]

Summing the owned receipts gives zero. These are signed transfers, not guaranteed core growth or a physical energy law. \(\square\)

The nonlinear state map in (4) is not asserted to be an isometry between distinct inputs, invertible or time reversible. Orthogonality holds for the operator frozen at each input. These distinctions matter when weights are recomputed.

## 3. Bounded reads and robust state response

**Theorem I2 (locality and global Lipschitz bound).** Each block decision reads at most 105 real field coordinates and 52 hard face bits; each executed block writes at most nine real coordinates. For fixed permissions, the state map is globally Lipschitz, including score ties and vacuum. A sufficient bound independent of total carrier size is

\[
\|\Phi_\varepsilon^h(x)-\Phi_\varepsilon^h(y)\|
\le(1+14\sqrt{265}\,\varepsilon)\|x-y\|.
\tag{9}
\]

**Proof of locality.** The dual ball of radius two has at most \(1+4+12=17\) cells. It is connected. If it has \(n\) cells, its distinct triangular faces number \(4n-e\), where \(e\ge n-1\) counts its internal shared faces; face valence is at most two. Hence there are at most \(3n+1\le52\) distinct face coordinates and face permission bits. The core part of \(R_\tau\) is exactly the dual ball of radius three, at most \(1+4+12+36=53\) cores. The total is at most 105. The write bound is inherited from (1).

**Proof of regularity.** Let \(R=\sqrt{E_\tau}\). On this read set each score is a positive quadratic form of operator norm at most four, so \(\|\nabla s_\sigma\|\le8R\). At differentiability points the max/positive-part margin satisfies \(\|\nabla r_\tau\|\le16R\). Consequently

\[
\|\nabla w_\tau\|\le\frac6R\quad(R>0).
\tag{10}
\]

For the increment \(\delta_\tau(x)=(C_\tau^h(\varepsilon w_\tau)-I)x\), the direct field derivative is at most \(2\varepsilon\), and the weight derivative contributes at most \((2\varepsilon R)(6/R)=12\varepsilon\). Thus its derivative norm is at most \(14\varepsilon\). Also \(\|\delta_\tau\|\le2\varepsilon R\), so the increment extends continuously by zero at empty read stock. Max/positive-part pieces and this extension yield a globally \(14\varepsilon\)-Lipschitz increment on its read coordinates, by integrating along lines through the smooth pieces and vacuum boundaries.

A core coordinate belongs to at most 53 read sets, since the center must lie within dual distance three. A face belongs to read sets centered within distance two of one of its at most two cofaces, at most 34 centers, also bounded by 53. A core is written by at most five centers and a face by at most two, hence write multiplicity is at most five. Therefore

\[
\left\|\sum_\tau[\delta_\tau(x)-\delta_\tau(y)]\right\|^2
\le5(14\varepsilon)^2\sum_\tau\|(x-y)_{R_\tau}\|^2
\le265(14\varepsilon)^2\|x-y\|^2.
\tag{11}
\]

Adding the identity proves (9). \(\square\)

Weights themselves can have direction-dependent limits at vacuum; the state increments remain continuous. Binary changes of hard permission are not covered by the fixed-mask bound. A local diagnostic does not by itself produce an outgoing record or its storage/reset receipts.

## 4. Execution radius: disjoint writes do not suffice for recomputation

**Theorem I3 (declared read/write conflicts).** For distinct centers,

\[
W_\tau\cap R_\sigma\ne\varnothing
\quad\Longleftrightarrow\quad
\operatorname{dist}_T(\tau,\sigma)\le4.
\tag{12}
\]

Thus the declared execution conflict graph for fresh weight recomputation is \(T^4\), with degree at most \(4+12+36+108=160\). These bounds are attainable on a stacked tetrahedral ball whose dual is a degree-four tree.

**Proof.** Core coordinates in \(W_\tau\) form \(B_T(\tau,1)\), while core coordinates in \(R_\sigma\) form \(B_T(\sigma,3)\). These intersect exactly when the centers have distance at most four. A shared face coordinate in the two sets already puts the centers at distance at most three, so it introduces no additional conflicts. The degree bound counts vertices at distances one through four. A degree-four tree through depth four has 161 cells, realizes 160 neighbors of the central center in \(T^4\), and realizes the 105-coordinate read set. \(\square\)

One frozen-snapshot update (4) can run its disjoint selected writes in parallel. Fresh recomputation requires a stronger consistency account. Events at distance at least five neither write another's decision reads and commute with recomputation. A supplied proper coloring of \(T^4\) with at most 161 colors gives a conditional safe batch protocol, but its coloring/order and consistent permissions are not native-sourced. Its sweep is not the frozen map (4).

The verifier supplies an exact race on the seven-cell strip with cells \([i,i+1,i+2,i+3]\), \(0\le i\le6\), in ascending orientation. Prepare the first lexicographic private face in cell 0 and in cell 3 with amplitude one, all other coordinates zero. Both cells win their local comparisons and have disjoint writes. Cell 3 initially has weight \(17/110\). Executing cell 0 first changes cell 3's recomputed weight to

\[
\frac{416157819610735772897}{2761493311383258036750}
\ne\frac{17}{110}.
\tag{13}
\]

The frozen-snapshot update on this face-only strip preparation creates strictly positive core stock from zero, with all hard permissions supplied open and no mark registers. The two recomputed serial orders give different exact outputs; both preserve norm. This separates conservation from confluence and from causal scheduling.

## 5. Explicit intrinsic asymmetry and the retained symmetric stall

On the closed four-simplex boundary, use the v2.12/v2.13 cyclic preparation

\[
x_*=(1,0,1,0,0,1,1,0,0,1;0,0,0,0,0).
\tag{14}
\]

With all permissions on and \(\varepsilon=1\), every block score is \(8/17\); every margin is zero, so \(\Phi_1^1(x_*)=x_*\). No symmetric record or choice is manufactured.

Instead consider the already asymmetric native preparation \(x_\delta=x_*+\delta e_{\tau_0}\), where \(\tau_0=[0123]\) is the first lexicographic core. Exact evaluation gives

\[
s_{\tau_0}=\frac8{17}+\frac{16}{21}\delta^2,
\qquad
s_\sigma=\frac8{17}+\frac{80}{357}\delta^2
\quad(\sigma\ne\tau_0).
\tag{15}
\]

The block conflict graph is complete, so for every \(\delta\ne0\),

\[
w_{\tau_0}=\frac{16\delta^2}{119(5+\delta^2)}>0,
\qquad w_\sigma=0\quad(\sigma\ne\tau_0).
\tag{16}
\]

At \(\delta=1\), the weight is \(8/357\). This is a nonzero native event chosen from current field data without an added mark. It does not explain the origin of that initial asymmetry, and it is not an empty-core genesis result.

The choice persists on an explicit open neighborhood. At \(x_1\), the initial score gap is \(64/119\) and \(\|x_1\|=\sqrt6\). For \(\|u\|\le\eta=1/100\), each quadratic score changes by at most \(4(2\sqrt6\eta+\eta^2)\). Using \(2\sqrt6<5\), the worst difference of two score changes is at most \(501/1250\). Thus every competing gap stays at least

\[
\frac{64}{119}-\frac{501}{1250}
=\frac{20381}{148750}>0.
\tag{17}
\]

This certifies a robust strict-margin sector at fixed permissions. As \(\delta\to0\), the selected weight in (16) tends to zero quadratically. There is no positive uniform progress bound through the symmetric limit, consistent with the earlier symmetry and record theorems.

## 6. Disposition and next test

This package provides a continuous bounded-locality bulk response using native coordinates only, an explicit robust asymmetric sector, and its true recomputation radius. It does not derive a unique native selector. Finite metric activity, strict comparison, division by four times read stock, the bulk cover and the model step are constitutive choices. The factor four is a sufficient spectral normalization from (5), not a physical coupling or an optimization theorem. All-hard-off and zero stock remain absorbing. Ties, dark blocks, signed backflow, unfair repeated local winners and closed-system renewal remain unresolved.

The next source test is to compare this intrinsic response with an actual native event-cost/renewal principle, or to supply the missing asymmetric record/preparation through an explicit covariant carrier. Any asynchronous proposal must respect the \(T^4\) decision footprint. No physical action, clock, particle/quark/lepton map, native randomness or registry promotion follows. Historical physical targets remain exposed; exact algebra is not retrospectively empirical preregistration.

## 7. Reproducibility

The freshly authored `verify_intrinsic_bulk_margin.py` uses standard-library exact `Fraction` arithmetic. It checks all 1,024 face masks for norm and native receipts, all 120 signed vertex permutations, the asymmetric preparations (15)–(16), zero/hard-off controls, exact scaling/oddness, the saturating 161-cell geometry and all 25,760 distinct-center read/write relations, read multiplicity and locality, and the fresh-recomputation race. The uniform neighborhood bound (17) is an analytic quadratic-form certificate. Finite controls supplement the proofs; they are constructor work, not independent replication, endurance testing or physical validation. No archived scripts are executed.
