# UD-PM-PRED05-SCALE-002 v1.0 — Logarithmic harmonic norm and mandatory running stiffness

**Kind:** THEOREM + scoped NO-GO (source-bound mathematical continuation).  
**Proof status:** VERIFIED_SCOPED / EXACT_CONDITIONAL; independent non-constructor review DEFERRED.  
**Physical promotion:** 0.  
**Source:** UD PR #479, `UD_PRED01_LOCAL_DEFECT_SELECTION_AND_BOUNDED_SOURCE_v0.4.md` §4, commit `b5c8146ae4b956279e6f399553e02cffbc42c7ea`; PR #484 `UD-PM-PRED04-WORK-002_v1.0.md`. Distinct external coefficient provenance: supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, 2026-08-22, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, especially G05, G06, Q13 and O03. This ledger is a dated source snapshot, not proof that no newer coefficient exists elsewhere.

## 1. Objects, metric and hypotheses

Let even \(N=2m\ge4\). Let \(K_N\) be the **fully cut** 3-dimensional Freudenthal tetrahedralization constructed in PRED05-EVOL-001, with exactly three vertex levels \(z\in\{0,1,2\}\). Use real simplicial 1-cochains with the **unweighted Euclidean counting norm** \(\|a\|^2=\sum_{e\in E(K_N)}a_e^2\). Fix the oriented generator \(\gamma\) of \(H_1(K_N;\mathbb Z)\cong\mathbb Z\).

Let \(h_N\) be the unique harmonic (closed and co-closed) real 1-cochain with period \(\oint_\gamma h_N=1\). Define \(P_N:=\|h_N\|^2>0\) and harmonic numbers \(\mathcal H_m=\sum_{r=1}^m 1/r\). The action assumption from PR #479 is
\[
\mathcal A_N(a)=\frac{\lambda_N}{2}\|a\|^2+\frac{\mu_N}{2}\|da\|^2,\quad \lambda_N>0,\quad \mu_N\ge0,
\]
with endpoints \(a_2=2h_N\) and \(a_3=3h_N\). These are **model-action** terms, not SI energy or physical time, and the choice of metric is an active hypothesis.

## 2. Theorem: harmonic norm has logarithmic two-sided bounds

For all even \(N\ge4\),
\[
\boxed{\frac38\mathcal H_m\ \le\ P_N\ \le\ 336\mathcal H_m.}
\]
In particular \(P_N=\Theta(\log N)\) within this exact lattice family and unweighted cochain metric.

### Lower-bound proof

For each horizontal level \(z=0,1,2\) and each square radius \(r=1,\ldots,m\), take the oriented perimeter \(L_{r,z}\) of the grid square centered on the puncture with Chebyshev radius \(r\). This is a supported cycle with exactly \(8r\) grid edges. All \(3m\) cycles wind once around the defect and are homologous to \(\gamma\); each has \(\oint h_N=1\). Distinct pairs \((r,z)\) use **disjoint edges**. By Cauchy–Schwarz,
\[
1=\left(\sum_{e\in L_{r,z}}\pm h_e\right)^2\le (8r)\sum_{e\in L_{r,z}}h_e^2,
\]
so summing disjoint contributions over all radii and three levels gives
\(P_N\ge 3\sum_{r=1}^{m}(8r)^{-1}=\frac38\mathcal H_m\).

### Upper-bound proof

Construct a real closed 1-cochain \(\omega_N\) by integrating the normalized planar angular form \(d\arg(x+iy)/(2\pi)\) along the planar projection of every oriented 3D edge (vertical projections contribute zero). Each triangle projects into a base triangle, segment or point avoiding the removed center, so the angular 1-form is exact locally on each projected triangle and \(d\omega_N=0\). It has period one on every square ring and therefore represents the same cohomology class as \(h_N\). Since \(h_N\) minimizes the Euclidean norm in its cohomology class, \(P_N\le\|\omega_N\|^2\).

Every projected edge has coordinate displacement of magnitude at most one in each planar coordinate. Let \(r\ge1\) be the minimum Chebyshev distance of its endpoints from the puncture. For \(r=1\), its normalized angular change has magnitude at most \(1/2\), hence at most \(1/r\). For \(r\ge2\), the straight segment stays at Euclidean distance at least \(r-1\) from the puncture and has length at most \(\sqrt2\); integration gives
\[
|\omega_e|\le\frac{\sqrt2}{2\pi(r-1)}\le\frac{\sqrt2}{\pi r}<\frac1r.
\]
There are exactly \(8r\) planar vertices on the Chebyshev radius-\(r\) ring, three horizontal levels, and at most 14 incident edges per 3D Freudenthal vertex (seven forward plus seven backward). Each edge of minimum radius \(r\) has an endpoint on that ring; thus at most \(24r\cdot14=336r\) such edges. Consequently,
\[
\|\omega_N\|^2\le \sum_{r=1}^m(336r)r^{-2}=336\mathcal H_m,
\]
proving the upper bound and logarithmic growth. QED.

## 3. Corollary: exact stiffness-running constraint and fixed-coefficient NO-GO

The curvature term vanishes at both harmonic endpoints, so for the \(n=2\to3\) event,
\[
\Delta_N=\mathcal A_N(3h_N)-\mathcal A_N(2h_N)=\frac52\lambda_N P_N.
\]
For a fixed native stiffness \(\lambda_N=\lambda_0>0\),
\[
\Delta_N\ge \frac{15}{16}\lambda_0\mathcal H_m\longrightarrow +\infty.
\]
Hence a single scale-independent positive local coefficient cannot produce a bounded retained gap as the puncture-to-boundary scale ratio grows in this **unweighted** family. This is a scoped, exact NO-GO independent of the numerical values in PR #479.

More generally, if constants \(0<\delta_-\le\delta_+<\infty\) satisfy \(\delta_-\le\Delta_N\le\delta_+\) uniformly, the two-sided norm bounds force
\[
\boxed{\frac{\delta_-}{840\mathcal H_m}\le \lambda_N\le\frac{16\delta_+}{15\mathcal H_m}.}
\]
Thus \(\lambda_N=\Theta(1/\log N)\) is **necessary** for a finite nonzero retained-action gap under the declared metric and generator. Conversely, choosing a running coefficient in this asymptotic interval is sufficient to make the retained gap bounded away from zero and infinity for this family, but **does not derive that coefficient from K4 primitives**.

When \(\mu_N=\lambda_N\) and every edge is updated once, the independently proved PRED04-WORK-002 theorem gives
\[
\Delta_N\le W_N^+\le\frac95\Delta_N.
\]
Therefore a constant \(\lambda_0\) also forces \(W_N^+\to\infty\). Bounded action input is possible in the distributed-source branch only if the stiffness, metric, update rule or other assumptions run appropriately.

## 4. Typed normalization audit and reopening conditions

- The prior rule \(\lambda_N P_N=2/5\), which sets \(\Delta_N=1\), is an **inverse normalization** selected to meet a target native gap; it does not follow from packet multiplicities, incidence counts, \(K_4\) symmetry or the transport state alone.
- The symbol \(\lambda\) appearing in a packet **burden-stabilization** term and the partial-spectrum coupling \(\lambda_{\mathrm{partial}}\) in ledger v0.39 are **not** the present 1-cochain stiffness \(\lambda_N\). Likewise the master loop action weight G05 remains source-blocked in that dated ledger; a dimensionally correct bridge must map one of those typed action coefficients into this cochain quadratic form.
- The logarithm is a statement about the **unweighted cochain norm** on this specific expanding radial scale ratio. A changed edge measure/metric, a growing lattice-scale defect radius, a changed three-layer depth, a finite outer/core ratio, or an action with additional native stock/loop terms is a **new branch**, not a refutation of this scoped NO-GO.
- Neither \(\mathcal H_m\) nor a discrete event count constitutes a physical renormalization-group trajectory, SI energy, or elapsed time without a calibrated bridge.
- A running \(\lambda_N\) may be *modeled* by new microscopic assumptions, but no such source rule has been proven from the currently inspected action sources. Physical promotion remains 0.

## 5. Verification

A separate exact rational script generated \(\mathcal H_m\), the lower/upper bounds, and coefficient inequalities for \(N=4,6,8,16,32,64,128\). A second, separately implemented angular-cochain evaluator checked closure, all 3m unit periods and the pointwise edge estimate at \(N=4,6,8,10\). The analytic argument, not those finite checks, proves the all-\(N\) theorem. No independent non-constructor review was performed.
