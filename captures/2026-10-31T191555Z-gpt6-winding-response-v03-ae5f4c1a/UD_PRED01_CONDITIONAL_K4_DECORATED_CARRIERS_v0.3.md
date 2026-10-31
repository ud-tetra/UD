# UD PRED-01 — Conditional K4-decorated winding carriers, source dynamics and readout obstruction v0.3

**Date:** 2026-10-31  
**Evidence:** EXACT_CONDITIONAL algebra/topology; NUMERICAL discrete relaxation; OPEN native physical correspondence.  
**Status:** D0 development — no registry promotion. Non-constructor review deferred. Physical promotion **0**.

## Source provenance and type boundary

The *specific* source of the proposed event-cost question is `ud-tetra/UD/docs/UD_PREREGISTRATION_PACKET_v1.0.md` Part A §§A.1–A.5, D, E (blob `c5ddbb6f4df4ba3ff5c6b39895b58c6e955fc82b`); its mandatory `UD_PACKET_v1.1_ERRATA.md` §§E.1–E.2 (blob `6961b917f4f1ca470127aa0b7d3c1b59693f4373`); and `UD_EXTERNAL_REVIEW_BRIEF.md` (blob `c1ec2adc2e257e06d9681d1a13c6e11b15b7d750`). The previously generated `UD_PRED01_WINDING_BURDEN_IDENTIFIABILITY_ADDENDUM_v0.2.md` and PR [UD #475](https://github.com/ud-tetra/UD/pull/475) are exploratory antecedents. All claims about the source's missing `n=2` persistence qualification and absent `n=3` endpoint are from the v1.1 errata; this artifact does **not** silently supply an endogenous carrier under those source assumptions.

**New assumptions (A1–A6):**

A1. Attach a **new annular seam topology** to the packet complex. This annulus is an assumed carrier scaffold, not derived from the primitive K4 rule. A filled K4 tetrahedron is contractible, not intrinsically an annulus.

A2. Attach a filled tetrahedron to each annular vertex at *one shared vertex only*. Decorations are topologically contractible and do not create the cycle. The resulting finite simplicial complex is denoted \(X_m\) for integer \(m\ge4\).

A3. Use real lifted link-phase cochains \(a\in C^1(X_m;\mathbb R)\). Declare their integral cycle period \(\oint_\gamma a=n\in\mathbb Z\). This is a **lifted winding/order-parameter convention**, not the gauge-invariant U(1) Wilson loop. Allowed local deformations are exact shifts at fixed integer period; large local-gauge transformations or phase-slip topology changes are not automatically included.

A4. Use the Euclidean unit-edge pairing \(\langle a,b\rangle=\sum_e a_e b_e\) and normalized **model action** \(S_0(a)=\tfrac12\sum_e a_e^2\). All coefficients are declared, not derived UD constants. No units or physical time have been mapped.

A5. Define fixed-sector relaxation and a separately injected three-edge seam-slip source, with explicit source/action receipts. These are stipulated update rules, not recovered native dynamics.

A6. Distinguish **retained equilibrium action increment**, **gross phase-slip input work** and **relaxation remainder** as different typed observables. Do not identify them by a matching number.

## 1. Finite carrier complex and exact topology

For \(i\in\mathbb Z/m\mathbb Z\), define annular vertices \(u_i,v_i\). Use edges
\((u_i,u_{i+1})\), \((v_i,v_{i+1})\), \((u_i,v_i)\), \((u_i,v_{i+1})\), and faces \([u_i,u_{i+1},v_{i+1}]\), \([u_i,v_i,v_{i+1}]\). For each of the \(2m\) annular vertices, attach one full 3-simplex along only that vertex. The complex has

\[
(V,E,F,T)=(8m,16m,10m,2m),\qquad \chi(X_m)=0.
\]

Each filled tetrahedron retracts to its attachment vertex. The undecorated annulus retracts to a circle. Thus \(X_m\simeq S^1\), so over \(\mathbb Z\),

\[
H_0(X_m)\cong\mathbb Z,\quad H_1(X_m)\cong\mathbb Z,\quad H_2(X_m)=H_3(X_m)=0.
\]

At \(m=8\), \((V,E,F,T)=(64,128,80,16)\), the boundary matrix ranks are \((63,64,16)\), and Betti numbers are \((1,1,0,0)\). Independent finite incidence matrices satisfy \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\); exact SymPy rank and independent floating numerical rank calculations agree.

**NO-GO (scope):** A filled single \(\Delta^3\) has \(H_1=0\). Ordinary integer first-cohomology winding therefore cannot be sourced by its *filled-simplex topology alone*. This does **not** prohibit an additional seam fiber, punctured defect, non-Abelian holonomy or ribbon topology; those are distinct branches requiring their own source rules.

## 2. Explicit closed and co-closed lifted winding states

Let \(h=n/m\), and assign oriented link values

\[
\begin{aligned}
a_n(u_i\to u_{i+1})&=h,& a_n(v_i\to v_{i+1})&=h,\\
a_n(u_i\to v_i)&=-h/2,&a_n(u_i\to v_{i+1})&=h/2.
\end{aligned}
\]

Assign zero to all tetrahedral-decoration links. Let \(B_1=\partial_1\) and \(B_2=\partial_2\) in consistently oriented simplex bases. Then **EXACT**

\[
B_2^{\mathsf T}a_n=0,\qquad B_1a_n=0,\qquad \oint_\gamma a_n=n,
\]

and \(\|a_n\|^2=5n^2/(2m)\). Every closed real 1-cochain with this period is \(a_n+B_1^{\mathsf T}\phi\) for some real vertex 0-cochain \(\phi\), modulo constants. Hence

\[
S_0(a_n+B_1^{\mathsf T}\phi)=\frac{5n^2}{4m}+\frac12\|B_1^{\mathsf T}\phi\|^2.
\]

Thus **EXACT_CONDITIONAL:** \(a_n\) is the unique minimum of \(S_0\) as a 1-cochain in its fixed winding class. The constructed \(n=2\) and \(n=3\) carrier states exist mathematically; no native/empirical winding persistence is claimed.

## 3. State evolution and stability

On \(\mathcal Z_n=\{a_n+B_1^{\mathsf T}\phi\}\), choose discrete relaxation

\[
a_{t+1}=a_t-\eta B_1^{\mathsf T}B_1a_t,\qquad 0<\eta<\frac{2}{\lambda_{\max}(B_1B_1^{\mathsf T})}.
\]

Exactness of the correction ensures \(\oint_\gamma a_{t+1}=\oint_\gamma a_t\). The action is nonincreasing, and the exact-cochain component converges to zero by the nonzero spectral gap of the connected graph Laplacian. **The rule cannot change integer winding by itself.**

At \(m=8\), the maximum graph degree is 7, so the declared \(\eta=1/28\) is admissible. Numerical eigensolve returned \(\lambda_2\approx0.16125498724\), \(\lambda_{\max}\approx9.53122961884\). Starting at the externally slipped \(n=2\) state, after 1000 **algorithmic iterations**, the Euclidean error to \(a_3\) was about \(0.0022513921\) (initial \(1.6393596311\)). These iterations are **not calibrated seconds or a physical clock**.

## 4. A local cohomological source and exact receipt

Define the cut cocycle \(z\in C^1(X_m;\mathbb Z)\), supported on the three directed wrap edges \(u_{m-1}\to u_0\), \(v_{m-1}\to v_0\), and \(u_{m-1}\to v_0\), each with value 1 in directed orientation (other entries zero). Explicit incidence calculation gives

\[
B_2^{\mathsf T}z=0,\quad \oint_\gamma z=1,\quad\|z\|^2=3,\quad z-a_1=-B_1^{\mathsf T}\phi_\star
\]

for a declared rational \(\phi_\star\). One externally injected source move \(a_n\mapsto a_n+z\) therefore changes the sector \(n\mapsto n+1\); the subsequent relaxation preserves the new period and converges to \(a_{n+1}\). **There is no unreceipted autonomous winding production.**

Under \(S_0\), the three distinct accounting quantities are

\[
\boxed{W_n^{\rm in}=S_0(a_n+z)-S_0(a_n)=\frac32+\frac{5n}{2m}},
\]
\[
\boxed{\varepsilon_n^{\rm retain}=S_0(a_{n+1})-S_0(a_n)=\frac{5(2n+1)}{4m}},
\]
\[
\boxed{D_n^{\rm relax}=S_0(a_n+z)-S_0(a_{n+1})=\frac32-\frac5{4m}}.
\]

The exact identity \(W_n^{\rm in}=\varepsilon_n^{\rm retain}+D_n^{\rm relax}\) holds for each transition. Here **D is an action decrease under stipulated relaxation**, not demonstrated physical radiation or heat. At \(m=8\), the \(2\to3\) event has input \(17/8\), retained increment \(25/32\), relaxation remainder \(43/32\).

## 5. Observable ambiguity and constitutive-law competition

Two *lawfully distinct* dimensionless two-event ratios are

\[
R_{\rm retain}=\frac{\varepsilon_1^{\rm retain}}{\varepsilon_0^{\rm retain}}=3,
\qquad
R_{\rm gross}=\frac{W_1^{\rm in}}{W_0^{\rm in}}=1+\frac5{3m}.
\]

At \(m=8\), \(R_{\rm gross}=29/24\ne3\). Therefore the selected readout matters even when carrier and update are held fixed. The retained-action increments coincide in shape with the historical HCB1/WBQ1 affine family, \(\varepsilon_k\propto(2k+1)\); the proportionality factor \(5/(4m)\) is a **model normalization dependent on the assumed annulus resolution**, not an inferred physical coefficient.

For a **separately proposed** strictly convex quartic action \(S_\gamma(a)=\tfrac12\|a\|^2+\gamma\sum_ea_e^4\), \(\gamma\ge0\), the same symmetric \(a_n\) minimizes the fixed-period sector; direct edge counting gives

\[
S_\gamma(a_n)=\frac{5n^2}{4m}+\frac{17\gamma n^4}{8m^3}.
\]

With illustrative *chosen* \(\gamma=1,m=8\), the event increments are \((657,2175,4305,7455)/4096\), yielding \(D_2=153/1024\ne0\) and the PRED-01 four-event WBX1 invariant \(H_4=3825/262144\ne0\). This illustrates a third competing non-affine constitutive law. It is **FIT/HYPOTHESIS origin**, not a native selection or a measured effect.

## 6. Boundary and refinement obstruction

**NO-GO under the declared topology:** Capping the annular hole with triangles produces a disk-like complex with \(H_1=0\) (verified \(\beta=(1,0,0)\)). Winding protection is conditional on preserving the hole, the lifted order parameter and allowed transformation class. The Wilson loop of the exponentiated phase is \(\exp(2\pi i n)=1\) in all these integer sectors: **Wilson-loop readout alone cannot distinguish the integer carrier index** without the chosen lift or other structure.

**NO-GO under fixed three-edge cut, quadratic action and nonzero finite retained-gap requirement:** Restore an arbitrary positive edge stiffness \(\lambda_m\) in \(S^{(m)}_0=\lambda_m\|a\|^2/2\). For fixed \(n\) and \(m\to\infty\),

\[
\varepsilon_n^{\rm retain}=\frac{5(2n+1)}4\frac{\lambda_m}{m},\quad
W_n^{\rm in}=\lambda_m\left(\frac32+\frac{5n}{2m}\right).
\]

If the retained gap has a finite positive limit, \(\lambda_m/m\to L>0\), forcing \(\lambda_m\to\infty\), so input work diverges. If input work stays bounded, \(\lambda_m\) is bounded and the retained gap vanishes. Therefore this *specific* fixed-support injection plus stiffness scaling cannot produce **both** a nonzero finite retained continuum gap **and** bounded gross input work. Change the source regularization, geometry or constitutive law to open a new branch; the no-go remains valid under its original hypotheses.

## 7. Source-bound gap classification

| Required gate | Result in this artifact | Meaning |
|---|---|---|
| Finite \(n=2,n=3\) combinatorial construction | **EXACT_CONDITIONAL PASS** | Real cochain sectors on assumed annulus + K4 decorations |
| Chain, topology, flatness, lifted winding | **EXACT_CONDITIONAL PASS** | \((1,1,0,0)\), \(d a_n=0\), \(\oint a_n=n\) |
| Fixed-sector action minimality | **EXACT_CONDITIONAL PASS** | Strict modulo constant vertex gauge |
| Explicit update and source receipt | **EXACT_CONDITIONAL PASS** | External local seam slip + gradient relaxation; no physical clock |
| Boundary robustness | **FAIL for capped hole** | Hole is essential in this model |
| Nondegenerate continuum source+gap | **NO-GO** | Under fixed 3-edge slip and quadratic stiffness family |
| Endogenous native K4 hole/selector | **OPEN_GATED** | Annulus inserted as an assumption, not sourced |
| n=2/n=3 native defect persistence | **OPEN_GATED** | Source's §7.13 standard not passed |
| Physical observables/units/instrument | **OPEN_GATED** | Gross vs retained ambiguity is explicit |
| Independent review/replication | **DEFERRED** | No scientific promotion |

## Reproduction

Run `python3 carrier_and_preparation.py --m 8 --exact-ranks --out RESULTS.json`; `python3 -m unittest discover -v`. Requires pinned NumPy/SymPy; exact algebra is rational; numerical relaxation is documented separately. The scripted controls include capped hole, multiple refinement values, all integer sectors \(n=0,...,4\), exact source receipts and the distinct quartic branch.
