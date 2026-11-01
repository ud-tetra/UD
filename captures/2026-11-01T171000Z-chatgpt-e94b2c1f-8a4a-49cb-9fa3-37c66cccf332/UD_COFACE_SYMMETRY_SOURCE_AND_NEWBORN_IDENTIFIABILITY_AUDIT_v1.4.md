# Unified Dynamics — Coface Symmetry-Breaking, Signed-Source and Newborn Resource Identifiability Audit v1.4

**Date:** 2026-11-01  
**Lane:** `DEVELOPMENT_NO_REGISTRY_ENTRY` · **Physical promotion:** `0`  
**Verdict:** `EXACT_PREBIRTH_DIAGNOSTICS / NO_SOURCE_OWNED_FACET_SELECTOR / NEWBORN_AND_COST_NOT_IDENTIFIABLE`  
**Scope:** two authorized workloads: (1) source-derived symmetry breaking before tetrahedral coface birth; (2) independent newborn-state, seam and positive-formation-debit identifiability.

## 1. Typed source and precedence

The initial spatial carrier is a **filled** tetrahedron \(\tau=[0123]\) with vertices \(V=\{0,1,2,3\}\), edges \(E=\binom V2\), faces \(F=\binom V3\), binary graph labels \(b=(0,0,1,1)\), source parameter \(s\) (not physical seconds), inherited burden \(\rho\), group-valued seam transports \(U_e\), and retained event history \(\mathcal E\). A possible new tetrahedron is \(\tau_f=f*[w_f]\), with a **new** vertex and exactly three new edges. It is NOT the filled 4-simplex. The pre-birth selection domain is the set of the four exposed triangles.

**Source hierarchy.** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22), Q140, Q153–Q158, Q162, Q165–Q173, G05, and recovered source documents: `GRAPH_FIRST_LOCAL_ADMISSIBLE_COFACE_EXTENSION_PRIMITIVE_INDE.md` (Aug 9 v0.1), `UD native coface growth and cluster selection audit.md` (Oct 2, SHA `9ac884d727e65ddd4ed1c277d2ed4a7b91135d73`), `UD_COFACE_RESOURCE_INHERITANCE_EXACT_THEOREMS_v0.1.md` (Aug source), `UD_COFACE_NEWBORN_PACKET_INHERITANCE_MATRIX_v0.1.md` (Aug source), `UD event admission and interface memory.md` (Oct source SHA `6719d0f77622eac59c5c88fc163b49adda664e6`), and v1.3 proof `UD_NATIVE_COFACE_EVENT_RESOURCE_CONTRACT_AUDIT_v1.3.md` (local file SHA256 `994bcf2072342703431ce42ff9b1b2049d614103a128a61faed17251d848beb6`). The designated portal currently advertises Papers I–III 1.1.1 / IV 0.1 and physical promotion 0; those papers do not elevate this candidate. Newer archived audits reference a v0.86 coefficient ledger; it was not substituted for the directly audited v0.39 baseline.

**Historical target exposure:** binary \(q=2\), maximum 2 vertices per label, and a desired tetrahedral dimension were previously supplied. Their consequences are EXACT *conditional on the premises*, not a target-blind physical derivation of 3D space.

## 2. Exact structural and group constraints

Legal first facets: \(012,013,023,123\). Each facet contains one deficient binary label. Each attachment increments \((f_0,f_1,f_2,f_3)\) by \((1,3,3,1)\) and \(\chi\) by zero. The label-preserving isotropy group of the stated fully symmetric seed is \(H=S_{\{0,1\}}\times S_{\{2,3\}}\), order 4. It acts on candidate facets with two orbits \(\{012,013\}\), \(\{023,123\}\), and fixes no singleton facet.

**NO-GO (equivariant singleton theorem).** Let \(\Gamma(X)\) be an equivariant deterministic selector returning exactly one face, \(\Gamma(gX)=g\Gamma(X)\). If \(gX=X\) for every \(g\in H\), then the selected face must be fixed by all \(H\), which no candidate is. Therefore no such \(\Gamma\) exists on this symmetric input. This does not prevent stochastic symmetry-equivariant selection with a separately derived probability measure, a source-owned history tag, or selection from an asymmetric prestate.

**CANDIDATE / NOT NATIVE:** For any proposed permutation-covariant score \(D_f(X)\), a *unique strict maximum* would provide a mathematical equivariant selection on its nondegenerate domain; at ties this rule must be left UNKNOWN or assigned a separately specified tie policy. The frozen equations do **not** say to maximize either diagnostic below.

## 3. Workload 1a — exact source-current diagnostics from Q162

For the **conditional relaxational burden lane**, pass all hard gates \(h_e=1\), use the edge orientation \(i<j\), and read the frozen Q162 formula:

\[
 j_{ij}^{B,\mathrm{mix}}=-\frac14(\rho_j-\rho_i).
\]

Construct a candidate face-local squared-current diagnostic

\[
 D_f^{B}(\rho):=\sum_{\{i,j\}\subset f}(j_{ij}^{B,\mathrm{mix}})^2.
\]

**DERIVED diagnostic (not source-selected objective):** With \(\rho=(0,0,1,1)\), each face has \(D_f^B=1/8\). No face is distinguished. With \(\rho=(0,1,2,4)\), the exact values in face order 012, 013, 023, 123 are

\[
 (D_{012},D_{013},D_{023},D_{123})
 =\left(\frac38,\frac{13}{8},\frac32,\frac78\right).
\]

The unique largest diagnostic is face **013**. Its uniqueness is a mathematical *if-maximized* inference: Q162 supplies the edge currents, but neither Q162 nor Q153 supplies a source-owned facet competition objective, event clock or growth authorization. Under all 24 vertex relabelings, the diagnostic transforms covariantly. Its units are the square of the burden-current unit (under the declared source-parameter normalization), NOT formation energy or action.

## 4. Workload 1b — seam/twist discriminants

Take old U(1) seam link angles \(a\in (\mathbb R/2\pi\mathbb Z)^6\). With oriented edge-to-triangle matrix \(B_2\), the four triangular holonomy angles are \(\phi=B_2^Ta\). Because the oriented tetrahedron satisfies \(B_2u=0\) for \(u=(-1,1,-1,1)^T\), every permitted set of face angles obeys the exact boundary identity \(u^T\phi=0\pmod{2\pi}\). In the continuous U(1) comparator, the explicit integral edge-phase coefficients

\[
 a/(\pi/6)=(-1,1,0,-1,0,0)
\]

for edge order \((01,02,03,12,13,23)\) produce

\[
 \phi/(\pi/6)=(-3,-1,1,-1).
\]

The gauge-invariant candidate triangle mismatch \(D_f^{U}=1-\cos\phi_f\) therefore has one unique maximum \(D_{012}^U=1\) while each of the other three equals \(1-\sqrt3/2\). Every old link remains unitary and the input was specified **prior to birth**. The group phase and mismatch, however, do not determine that growth must maximize it. The edge-phase values are exact *test preparations*, not native coefficients. \(D^U\) is distinct from the ledger's \(\delta_U\) on its originally typed operator unless a holonomy readout map is explicitly supplied (the scalar functional can be evaluated on an admitted group element).

**Stronger NO-GO under binary central twists:** for \(\mathbb Z_2\) link signs on all six old edges, every edge participates in exactly two tetrahedral faces; hence the product of the four face holonomies equals \(+1\). The number of negative face loops is even. Exhaustively enumerating all \(2^6=64\) edge-sign assignments gives 8 with zero defects, 48 with two, and 8 with four. Therefore **a binary face-defect magnitude alone can never have a unique strict maximum** on the old tetrahedron. Continuous twists (or supplementary signed history data) can break this tie, as the preceding exact U(1) witness shows. These are two different transporter types; a U(1) witness cannot be silently imported as an SU(2)/Spin(3) law.

**Causal history:** a legitimate retained face-specific receipt can lower the isotropy group and make a singleton selector *possible*; the archive does not supply a universal prediction that such a receipt is produced or that its marked face must grow. A lexicographic vertex-ID tie break is external, not native.

## 5. Workload 2a — newborn seam identifiability

Let a child \(w*012\) share old face 012. Old face vertices, edges, links, and opposite induced face orientation are inherited by identity. The **three** new edges \(w0,w1,w2\) require new group-valued link data. For fixed old U(1) face links, a newborn-vertex gauge change removes one common phase but leaves **two independent relative phases** and the new triangle holonomies. For example, `(0,0,0)` and `(0,π/3,0)` in new-edge angles agree on all original edges but are not gauge equivalent under a gauge transformation that fixes the original boundary data. The new triangle holonomy differs. This proves **nonuniqueness from boundary inheritance alone**.

The analogous source record explicitly leaves newborn \(\rho_w,\theta_w,\sigma_w,b_w\), decorated seams and geometric normal/preframe OPEN. Setting all new loops flat would eliminate these distinctions only under an additional flatness premise; it can be incompatible with already nonflat old boundary holonomy. Gauge freedom is not additional *physical* energy stock.

## 6. Workload 2b — burden/formation-cost identifiability

With initial old scalar burdens \((1,1,1,1)\), the same total burden \(4\) and nonnegative demand permit a one-parameter family of newborn allocations, \(0\le x\le1\):

\[
 \rho'_{\rm uniform}=(1-x/4,1-x/4,1-x/4,1-x/4,x)
\]

or, with the same initial state and same newborn amount,

\[
 \rho'_{\rm concentrated}=(1-x,1,1,1,x).
\]

Each conserves the same aggregate scalar burden but they are distinct for \(x>0\). Neither is claimed as the native Q162/Q153 next-step solution: they are alternative *post-birth distributions satisfying accounting*, demonstrating that stock conservation alone does not determine the donor allocation or amount. The remaining event law must also balance actual edge fluxes and source receipts.

Separately, if free abstract formation stock is \(3\) and bound stock is \(4\), both a debit of \(1\) and a debit of \(2\) (or HOLD) preserve \(R_{\rm free}+R_{\rm bound}=7\). These are only dimensionless exact witnesses. In original newborn suite, \(M_{\rm form}\) is explicitly a **viability threshold**, not an additive cost; \(C_{\rm form}>0\) and available donor stock are OPEN. Q153 defines an incidence-plus-source balance; the residual Q158 cannot be reverse-read as a predictive source. Q165–Q173 conserve quadratic amplitudes on already admitted chain coordinates; neither abstract formation stock nor burden nor that quadratic support has an established map to physical joules. G05 master loop-action normalization is OPEN.

**NO-GO under the inspected interface:** graph-label and shared-edge inheritance, hard-gate status, burden continuity as a balance identity, seam group membership, and support conservation do not uniquely determine all newborn variables or a positive debit. A fresh constitutive law (or additional recovered source) is necessary. This is not a no-go for all possible UD extensions.

## 7. Criteria for a genuinely autonomous next step

A future candidate must specify *before the event* (i) the full typed prestate and history, (ii) a source-authorized functional for facet competition with a tie/collision and causal policy, (iii) a newborn scalar/framing/seam/normal preparation map, (iv) a positive formation debit with donor and units, (v) a closed support/burden receipt and a precise geometric/retraction update. It must make at least one advance prediction on held-out asymmetric preparations and pass the equal-stock and pure Z2-twist degeneracy controls. A candidate pass in one arrangement cannot be called physical time, energy, geometry selection or spontaneous packet birth.

**AUTO_LOCK scope recommendation:** exact algebra of the two burden fixtures, U(1)/Z2 seam fixtures, stabilizer obstruction and conservation nonidentifiability (constructor verification). **AUTO_FREEZE:** any assertion that maximizing the burden/current/holonomy mismatch is already an admitted source-owned scheduler, or that seam parameters/resource debit have been derived from graph-only birth. No frozen ledger change, registry promotion, or physical correspondence.

## 8. Reproducibility, review and provenance

- `verify_v1_4.py`: primary exact SymPy/Fraction implementation: 232 assertions.
- `independent_check_v1_4.py`: separate stdlib/Fraction implementation: 270 assertions; all 64 binary edge twist assignments exhausted.
- v1.3 precursor `verify_v1_3.py` / `independent_check_v1_3.py` rerun unchanged: 6,842 / 82 assertions passed.

Total 7,426 scoped exact assertion groups passed across four scripts, of which 502 are new v1.4 checks. Both new scripts were written by the same constructor; neither constitutes external scientific review. No physical units, measurement dataset, event-time calibration or native source parameter fit was used. Site update not authorized by this analysis. This report and code constitute a development capture only.
