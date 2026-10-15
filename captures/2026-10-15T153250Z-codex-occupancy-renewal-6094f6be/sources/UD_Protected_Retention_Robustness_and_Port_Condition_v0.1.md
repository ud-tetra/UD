# UD protected retention: port condition, finite robustness and eventual leakage v0.1

15 October 2026 UTC. Development addendum; no registry entry. Constructor verification only. Physical promotion 0.

**Result.** The preceding protected-selection theorem survives arbitrary reciprocal recovery ports whose carrier image lies in vertices plus exact edge gradients. This is a necessary and sufficient linear port condition for protecting the entire 2401-dimensional subspace. A balanced local star satisfies it. A single unpaired edge contact violates it, even while preserving the storage balance. When that small erroneous contact uses the written edge, the entire 42-dimensional cyclic component populated by that cut eventually decays. Finite retention remains certifiable. A six-template real-amplitude code gives a stronger bounded-noise certificate than the six quadratic-score decoder, at the cost of a more demanding readout contract.

The purpose is to identify what a recovery mechanism must preserve geometrically, and what its imperfections cost. This does not derive a native gate trigger, lawful burden occupancy, physical drain or recorder.

## 1. Source disposition

The current attached coefficient ledger v0.39(2), C03, Q153/Q158/Q162 and G05, still scopes absolute capacity, predictive source/sink, time normalization and open-system receipts. The attached CRL-2 subdivision is a governance proposal; constructor checks are not independent review. `SOURCE_REGISTER.json` preserves exact paths, hashes and source representations.

The preceding source is `UD_Reciprocal_Recovery_and_Protected_Selection_v0.1.md`, freshly retrieved and locally preserved, PR112 commit `f90a29063636e7cae8412036bc7e8d39331aa12a`. Its recovered `UD_SUPPORT_BURDEN_NORMALIZATION_COUPLING_RATE_REPAIR_v0.2.md` supplies a conditional reciprocal storage model with distinct normalization and rate. The finite complex is the preserved PR110/PR112 input, not a newly inferred physical lattice. Repository base inspected: `69b2f3dfc5fdd18b0b97690b43fb1178bdec8976`.

Additional source audit:

| Exact source | What was recovered | What remains open |
|---|---|---|
| `PREDICTIVE_PRE_EVENT_BURDEN_SOURCE_NONIDENTIFIABILITY_THEOREM_v0.1.md`, 6 September, §§1–4,6 | For the declared isolated symmetric K4 winding event, source direction is uniform; continuity permits any otherwise admitted scalar constitutive amplitude | The pre-event amplitude law; this K4 source is not automatically a global uniform 600-cell source |
| `WINDING_TO_BURDEN_SOURCE_LAW_ADMISSION_v0.1.md`, §§Source variables–Automatic tests | Required sign/null, normalization and composition tests for a future winding-burden law | No completed amplitude or drain law |
| `M11_LINEAR_BURDEN_SOURCE_IMAGE_AND_UNSOURCED_EDGE_SECTOR_THEOREM_v0.1.json` | Historical four-dimensional vertex-source image on a separate nine-dimensional projective carrier | Its five-dimensional complement is not identified with the 600-cell protected space |

These documents narrow the source obligations; they do not supply a native recovery rate. No archived program was executed. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read.

## 2. Which port geometry protects the pattern?

Let A be the restored unit-weight skew chain generator. Write

\[
L=B_1B_1^T,\quad
P_{\rm cyc}=I-B_1^TL^+B_1,\quad
P=\operatorname{diag}(0,P_{\rm cyc},I,I).
\]

Its range W has dimension 2401. Its orthogonal complement U consists of vertex amplitudes and exact edge gradients, of dimension 239. Boundary nilpotence gives PA=AP.

For a normalized burden coordinate z and any constant real reciprocal port F, consider

\[
c'=Ac+Fz,
\qquad z'=-F^Tc-Rz,
\qquad R=R^T\succeq0.
\]

The storage law is independent of the port shape:

\[
H=\tfrac12(\|c\|^2+\|z\|^2),\qquad H'=-z^TRz.
\]

**Port condition theorem.** The protected component obeys y'=Ay for every initial state if and only if PF=0. Sufficiency follows by projecting the c equation. Necessity follows by setting c=0 and choosing z with PFz nonzero. Therefore

\[
\boxed{\operatorname{ran}F\subseteq C_0\oplus\operatorname{im}B_1^T.}
\]

Equivalently every such linear port can be written

\[
F=I_0F_0+I_1B_1^TF_1,
\]

with appropriately typed burden-to-vertex maps F0,F1; its face and cell output blocks vanish. For the edge block, Pcyc Fedge=0 is equivalent to its image being a gradient. Global right-action equivariance is not necessary: arbitrary spatial variation in F0,F1 preserves W. It may still mix the ten Fourier sectors within U.

This is stronger than requiring a coefficient to be exactly zero by tuning. The port can vary throughout a declared geometrically constrained class. A vertex-local potential mapped through B1 transpose produces a full signed star of edge contacts. Its cycle component vanishes exactly. A unit edge basis vector has a cycle component of squared norm 601/720, so an individual edge contact does not have this protection.

The range condition is independent of an invertible burden normalization: PFN=0 if and only if PF=0. Its geometric meaning can therefore be derived before the absolute burden unit is fixed. The ledger's gradient within burden transport does not, by itself, derive this support–burden cross-port or its coefficient; that typed bridge remains a source obligation.

| Recovery port image | W protected? | Additional requirement |
|---|---|---|
| Vertices only | Yes | Drain and burden semantics remain separately sourced |
| Vertices plus exact edge gradients | Yes | Realize the signed gradient port, including its full contact pattern |
| A single unpaired edge | Generally no | Finite error tolerance or a redesigned port |
| Arbitrary face/cell coordinates | No universal W guarantee | A smaller invariant code would require its own proof |

**Write obstruction.** Starting with Pc=0, arbitrary vertex-only or exact-gradient forcing cannot create a protected component. Thus the same safe recovery port is not, by itself, a write mechanism for W. The previous contact cut is a separate actuator that leaves this port class. A source law must explain why that actuator is admitted and when it stops.

## 3. A local passive error that eventually erases the written component

Take the reference F=gamma I0 and R positive definite, with gamma nonzero. Add a local reciprocal contact between burden at vertex u and carrier edge e:

\[
F_\epsilon=\gamma I_0+\epsilon I_1e_e e_u^T.
\]

The added joint block is skew. It introduces no positive term in H'. Nonetheless PF_epsilon is nonzero for epsilon nonzero. Storage passivity alone therefore does not certify retention.

Let w=I1 Pcyc e_e and

\[
\mathcal C_e=\operatorname{span}\{w,Aw,A^2w,\ldots\}\subset W.
\]

**Exact finite result.** On the packaged 600-cell, dim C_e=42. The replay computes the degree-21 minimal polynomial of Q=B2 B2 transpose on Qe_e, verifies the polynomial annihilation exactly and a nonzero exact Hankel determinant. Because Q is invertible on the cycle space, Qe_e and Pcyc e_e have the same cyclic span under Q. Applying A adds the paired face components, doubling the dimension. The complete integer polynomial is exported in `ROBUST_RETENTION_DATA.json`; no numerical eigenvalue fit is used for this dimension.

**Same-edge erasure theorem.** Suppose epsilon is nonzero and R is positive definite. Any undamped joint eigenvector has z=0 by the storage identity. It must then satisfy

\[
Ac=i\omega c,\qquad
\gamma c_0+\epsilon e_u(c_1)_e=0.
\]

The second condition makes c0 proportional to the site vector e_u. Squaring the A eigen-equation on C0 gives Lc0=omega squared c0. But e_u is not an eigenvector of L: its Laplacian image has nonzero neighbor entries. Therefore c0=0 and (c1)e=0. The remaining undamped subspace is precisely

\[
\mathcal D=W\cap\mathcal C_e^\perp,
\qquad \dim\mathcal D=2359.
\]

D is reducing for the joint generator, and its orthogonal complement is strictly stable. The full contraction excludes imaginary-axis Jordan growth.

The supplied cut c'= (A-E_e)c starting at e_u lives in U plus C_e. Indeed its projected drive is always a scalar multiple of w. It has no D component. Consequently, after restoration with the same-edge erroneous recovery port,

\[
\boxed{(c(s),z(s))\longrightarrow0\quad\text{for every fixed }\epsilon\ne0.}
\]

The 401-dimensional relevant joint space consists of U (239), the written cyclic component (42), and burden (120). At epsilon=0, 359 directions decay and 42 persist. At epsilon nonzero, all 401 decay under the stated hypotheses. This is an infinite-time singular limit: making epsilon small can prolong retention but does not establish permanent protection.

The theorem concerns the pattern written by that same edge. It does not prove that all six codewords coincide under one fixed faulty port, that every protected state decays, or that an unmodelled microscopic reservoir loses the exported information.

## 4. Finite retention from the complete storage budget

Let the cut duration be tau=1/1000, with unit initial carrier norm and blank burden. The post-cut recovery starts with H0=1/2. Let R be at least r I, r>0. For y=Pc and the ideal protected evolution yref=exp(As)y0,

\[
y-y_{\rm ref}
=\epsilon\int_0^s e^{A(s-v)}w z_u(v)\,dv.
\]

With rho squared=601/720 and Qexport=integral z transpose Rz,

\[
\int_0^s\|z(v)\|^2dv\le H_0/r,
\qquad
\boxed{\|y-y_{\rm ref}\|\le |\epsilon|\rho\sqrt{sH_0/r}.}
\]

This is a general sufficient finite-time bound, not a fitted decay rate. It remains valid while the erroneous port feeds energy back between burden and carrier, because the complete reciprocal storage balance was retained. A bounded additional error nu in the measured protected amplitude adds nu to the right side. Normalization/rate uncertainties are not silently absorbed into epsilon.

### Six quadratic-score decoder

The preceding exact lower score gap is

\[
\Delta_*={6551\over375000000000}.
\]

The protected starting norm has the bound

\[
\|y_0\|\le r_*:=\rho\tau(1+\tfrac92\tau).
\]

To derive it, write the projected cut as an integral of the rotated w. The scalar vertex drive starts with magnitude one and changes by at most 6 sqrt(2) v; integrating and using sqrt(2)<3/2 gives the displayed bound. This uses norm(A-E_e)<6 and the unit norm maintained during the skew cut.

For a difference of the two orthoprojector scores, operator norm is at most one. A protected amplitude error d changes a gap by at most

\[
2r_*d+d^2.
\]

Hence a sufficient condition for the original winner is 2r*d+d squared < Delta*. At the declared recovery horizon s=600, r=1/5 and with no separate readout error, the rational choice

\[
\boxed{|\epsilon|\le1/4000000}
\]

passes exactly. Using sqrt(1500)<39, the worst gap-error bound is 7885721/480000000000000; the remaining certified gap is 499559/480000000000000. These are derived tolerance receipts for this benchmark, not fundamental UD constants or source-selected couplings.

### Six-template amplitude decoder

Declare a classical six-symbol input whose controller chooses one frozen incident edge per fibration. This is a candidate real-amplitude encoding contract, not an endogenous source law. The selected edges and all twelve incident alternatives are exported. Each branch uses the same supplied cut duration and vertex input.

Let g_i be the outward signed edge basis vector and w_i=Pcyc g_i. Their exact Gram matrix is

\[
G_{ij}=\delta_{ij}-(B_1g_i)^TL^+(B_1g_j).
\]

All diagonal entries are 601/720. Across the twelve words the off-diagonal values are

\[
-119/1440,\qquad-10697/151200,\qquad-205/3024.
\]

The twelve words sum to zero. For the frozen six representatives, the minimum leading squared distance is exactly 136907/75600, greater than (5/4) squared. Taylor's theorem bounds each finite cut's deviation from tau w_i by 18 tau squared. The finite six-word distance therefore satisfies

\[
\boxed{d_{\min}\ge(5/4)\tau-36\tau^2=607/500000.}
\]

A nearest-template decoder is correct whenever total protected amplitude error is below half this distance, namely 607/1000000. Orthogonal restored evolution preserves the distances; use templates advanced to the readout phase, or an explicitly calibrated co-rotating readout.

At s=600 and r=1/5, the sufficient local-contact tolerance

\[
\boxed{|\epsilon|\le1/100000}
\]

gives amplitude error below 39/100000, safely inside that decision radius. The two epsilon bounds compare conservative certificates. They do not prove failure of the score decoder above its sufficient bound, or a forty-fold measured hardware advantage. The template decoder presumes much richer access: calibrated signed amplitudes, a known frame/phase and stored templates. Neither an implementation nor its readout cost is derived.

Under an exact discrete six-label source and the stated noiseless or bounded-noise decoder contract, the mathematical labels are distinguishable. No quantum discrimination, Born-rule measurement, source acquisition or thermodynamic record claim follows. The gate controller was given the label; its address and preparation are charged inputs.

## 5. Storage removal and normalization do not disappear

For the ideal safe port, stable recovery removes the U/burden part and leaves protected stock p. The benchmark gives numerically

\[
p\approx8.3471874491\times10^{-7},
\qquad Q_{\rm export}(\infty)=\tfrac12(1-p)
\approx0.4999995826406.
\]

For the same-edge faulty port with epsilon nonzero, all of that branch's state eventually decays and Qexport tends to 1/2. These are normalized quadratic-storage quantities, not joules, heat or Landauer cost. Reservoir state, correlations, entropy, reset, controller reuse and physical units remain unmodelled.

Normalizing the surviving pattern can make its relative contrast appear healthy: its leading normalized score gap is

\[
{11/600\over601/720}=66/3005.
\]

But the surviving amplitude is of order tau and stock of order tau squared. Normalization does not restore the lost absolute signal or improve a fixed absolute readout-noise floor for free. A complete information-per-area/resource comparison still requires a recorder, noise model, local implementation, physical area and energy calibration.

## 6. Verification, scope and manuscript use

The replay contains 17 exact checks and seven labelled numerical corroborations. It checks rational code geometry, finite decision radii, storage-based tolerances, exact port cancellation, a 42-dimensional cyclic-write certificate and finite 600-cell constructions. Numerical checks compare the finite six-word distance, corroborate the 401-state stable/undamped split, and test one small local error at the declared horizon. General finite-time and asymptotic theorems are proved above; numerical spectra are corroborations rather than universal proof.

For epsilon=0.1 and 0.01, the largest real parts in the relevant numerical generator are approximately -7.44093e-6 and -7.40318e-8. These illustrate long weak-error tails in dimensionless s, not physical lifetimes or a derived universal epsilon-squared law. At epsilon=1e-5 and s=600, the numerical protected amplitude error is about 1.024e-6, inside the analytic bound about 3.53848e-4. No claim rests on extrapolating that single diagnostic.

The primary next closure target is a source-authored port rule enforcing the gradient/vertex range condition, coupled to an independently normalized burden observable and an active drain/export law. Native trigger, repair of actual closure/integrity data and timing remain open. If the source instead admits an unpaired edge port, finite retention and its whole resource ledger must replace indefinite protection.

This note is a separate manuscript development addendum. Its narrative point is precise: persistence depends on which geometric components recovery can reach. Conservation alone does not protect a selected pattern; the operator's image matters. A proposed physical implementation must demonstrate that image, its errors and its costs.
