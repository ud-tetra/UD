# UD PRED-01 — Winding-burden identifiability and leakage-control addendum v0.2

**Created:** 2026-10-31  
**Lane:** D0 DEVELOPMENT — NO REGISTRY PROMOTION  
**Evidence:** EXACT_CONDITIONAL algebra, exact finite-grid verification, NUMERICAL_SYNTHETIC Gaussian mean-noise audit  
**Physical promotion:** 0  
**Scope:** an explicitly assumed finite event model; does *not* certify physical carriers, a transport action, a laboratory protocol, mass, energy or calibrated time.

## 1. Typed sources and hypotheses

- `ud-tetra/UD/docs/UD_PREREGISTRATION_PACKET_v1.0.md`, Part A §§A.1–A.5, D, E, source blob `c5ddbb6f4df4ba3ff5c6b39895b58c6e955fc82b` (checked 2026-10-31).
- `ud-tetra/UD/docs/UD_PACKET_v1.1_ERRATA.md`, §§E.1–E.2, source blob `6961b917f4f1ca470127aa0b7d3c1b59693f4373`.
- `ud-tetra/UD/docs/UD_EXTERNAL_REVIEW_BRIEF.md`, §§"load-bearing claim", "known weaknesses", source blob `c1ec2adc2e257e06d9681d1a13c6e11b15b7d750`.
- `ud-tetra/UD/docs/UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, §4, still a *proposal* when checked; the development lane permits analysis without an evidentiary promotion.
- New program policy PR `ud-tetra/UD#473` is not assumed merged. No existing frozen claim is silently amended.

**Assumption A1 (formal carriers).** Symbols \(C_0,\ldots,C_4\) are ordered formal states with event transitions \(E_k:C_k\to C_{k+1}\). They are *not* physically constructed UD carriers. The cited source records that the \(n=2\) candidate lacks full persistence tests and the \(n=3\) endpoint is not constructed. Event numbers are indices, not physical time.

**Assumption A2 (WBX1 recurrence).** Let \(A>0\), \(C,\kappa\in\mathbb R\), \(f(0)=0\), and \(\varepsilon_k=A+Ck+\kappa f(k)\) with \(f(k+1)=f(k)+\varepsilon_k\). Here \(f,\varepsilon,A,C\) are native *cost/readout* scalars of the same declared units; \(\kappa\) is dimensionless. The measurement bridge, independent leakage values \(\Lambda_k\), and calibration to SI units are OPEN.

**Assumption A3 (admissibility branches).** Broad physical-cone proxy: \(\varepsilon_k\ge 0\) for tested \(k\). A *stronger and separately labeled* optional branch imposes \(C\ge0,\kappa\ge0\). Do not replace one by the other without an amendment.

## 2. Exact recurrence theorem

From the assumed update,

\[
\begin{aligned}
\varepsilon_{k+1}-\varepsilon_k
 &=C+\kappa[f(k+1)-f(k)]\\
 &=C+\kappa\varepsilon_k,\\
\boxed{\varepsilon_{k+1}&=(1+\kappa)\varepsilon_k+C.}
\end{aligned}
\]

Set \(\delta_k=\varepsilon_{k+1}-\varepsilon_k\). Then \(\delta_{k+1}=(1+\kappa)\delta_k\), with \(\delta_0=C+\kappa A\). Consequently

\[
\begin{aligned}
\varepsilon_0&=A,\\
\varepsilon_1&=A+C+\kappa A,\\
D_2&:=\varepsilon_2-2\varepsilon_1+\varepsilon_0
=\kappa(C+\kappa A),\\
T_3&:=\varepsilon_3-3\varepsilon_2+3\varepsilon_1-\varepsilon_0
=\kappa D_2.
\end{aligned}
\]

These equations agree with the source's \(D_2/A=\kappa(c+\kappa)\), \(c=C/A\), and the source's fourth-event formula

\[
\varepsilon_3=A(1+\kappa)^3+C(\kappa^2+3\kappa+3).
\]

**EXACT four-event necessary invariant.** All WBX1 event quartets satisfy

\[
\boxed{H_4:=(\varepsilon_1-\varepsilon_0)(\varepsilon_3-\varepsilon_2)
-(\varepsilon_2-\varepsilon_1)^2=0.}
\]

Equivalently \((\varepsilon_1-\varepsilon_0)T_3=D_2^2\). This is a parameter-free *model falsifier*, not an independent physical prediction. It is **not sufficient** on the singular branch: \([1,1,1,9]\) has \(H_4=0\) but violates the WBX1 recurrence. There the additional requirement is \(\varepsilon_3=\varepsilon_0\).

## 3. Exact identifiability partition and source repair

If \(\varepsilon_1\ne\varepsilon_0\), the first three increments give

\[
\boxed{\kappa=\frac{\varepsilon_2-2\varepsilon_1+\varepsilon_0}{\varepsilon_1-\varepsilon_0}},\qquad
\boxed{C=(\varepsilon_1-\varepsilon_0)-\kappa\varepsilon_0}.
\]

If \(\varepsilon_1=\varepsilon_0\) and \(\varepsilon_2\ne\varepsilon_0\), WBX1 is rejected. If \(\varepsilon_0=\varepsilon_1=\varepsilon_2=A\), the recurrence forces **all** \(\varepsilon_k=A\) and every \(\kappa\) combined with \(C=-\kappa A\) gives the same observable sequence. Thus source §A.5's unqualified statement "Three events fix (A,c,kappa) exactly" is **false on the singular line**. This addendum is a *proposed narrowed repair*; it does not overwrite v1.0.

The wider \(\varepsilon_k\ge0\) cone **does not remove** the singular line: \((A,C,\kappa)=(1,-2,2)\) gives \(\varepsilon_k=1\) for every \(k\). Within the extra assumptions \(C,\kappa\ge0\), the singular branch instead forces \(C=\kappa=0\). State which branch is tested.

## 4. Positive-cone false-positive result

Fix \(A=1\), \(C,\kappa\in\{0,\tfrac12,1,\tfrac32,2\}\). All 25 models have nonnegative tested increments. Five models have \(\varepsilon_0=1,\varepsilon_1=3\), hence the frozen two-event ratio \(R_B=3\); **four have \(\kappa>0\)** and are distinct from HCB1/WBQ1 \(\varepsilon_k=1+2k\). Example:

| Model | \(A\) | \(C\) | \(\kappa\) | \(\varepsilon_{0..3}\) | \(D_2\) |
|---|---:|---:|---:|---|---:|
| HCB1/WBQ1 | 1 | 2 | 0 | 1, 3, 5, 7 | 0 |
| WBX1 mixed | 1 | 1 | 1 | 1, 3, 7, 15 | 2 |
| WBX1 autocatalytic | 1 | 0 | 2 | 1, 3, 9, 27 | 4 |

**NO-GO under these assumptions:** a ratio extracted only from \(E_0,E_1\) cannot identify WBX1 \(\kappa\) or distinguish nonlinear formation from this affine null. This mathematical counterexample remains even in the stronger \(A>0,C\ge0,\kappa\ge0\) cone.

## 5. Leakage-identification obstruction

The source's v1.1 errata correctly requires a separately returned leakage triple \(\Lambda_0,\Lambda_1,\Lambda_2\). Under the PLB1 model \(\varepsilon_k=p\Lambda_k\), exact compatibility is tested by a single nonnegative \(p\) satisfying all event coordinates; for any nonzero pair this is equivalent to zero cross-products \(\varepsilon_i\Lambda_j-\varepsilon_j\Lambda_i=0\).

**EXACT conditional no-go:** if the leakage sequence is unconstrained and not independently measured, any positive \(\varepsilon\) can be explained by PLB1 after choosing \(\Lambda_k=\varepsilon_k/p\), for arbitrary \(p>0\). Even with independent leakage data, a proportional leakage sequence makes WBX1 and PLB1 observationally indistinguishable on the measured events. A successful D2 or H4 alone never establishes autocatalysis. Distinguishing such a case requires additional independent constraints or an intervention that changes leakage without mechanically determining the burden response.

**Operational readout:** return \(\varepsilon\) and \(\Lambda\) from independent providers, preserve blinding/custody, calculate both \(D_2(\varepsilon)\) and \(D_2(\Lambda)\), test PLB1 proportionality, then test WBX1 fourth-event holdout. Label the result AMBIGUOUS if both families survive.

## 6. Precision and synthetic results

Assume *only for synthetic development* that each event cost mean has independent Gaussian noise, coefficient of variation \(r=\tfrac1{10}\), and \(n=12\) repeated observations per event. For the HCB1 baseline \((A,3A,5A)\),

\[
\operatorname{Var}(D_2/A)=\frac{r^2}{n}(1+4\cdot3^2+5^2)=\frac{31}{600},\quad
\sigma_{D_2/A}=\sqrt{\frac{31}{600}}\approx0.227303.
\]

A nominal \(3\sigma\) two-sided threshold is \(3\sqrt{31/600}\approx0.681909\). Along \(c+\kappa=2\), where \(D_2/A=2\kappa\), **the mean signal reaches this fixed null threshold at**

\[
\kappa_{3\sigma,\mathrm{mean}}=\frac32\sqrt{\frac{31}{600}}\approx0.340955.
\]

This is **not** a statistical-power requirement and is not a laboratory threshold. Source Part E described \(\kappa\approx0.30\) as a rough detectable value; the present specific null/CV assumption produces the above sharper boundary. Do not silently replace the source's acquisition protocol.

Under 10,000 seeded *synthetic* noise draws (`seed=20261031`, fixed null threshold, Gaussian class means) detection frequencies were: HCB1 0.0027; WBX1 \(\kappa=\tfrac12\) 0.9042; \(\kappa=1\) 1.0000; \(\kappa=2\) 1.0000. These are computer-generated frequencies, **not** observed statistical power, since apparatus noise, source occupancy, carrier validity and nuisance covariance are unresolved.

## 7. Open gates / next discriminate

**OPEN_GATED:** construct and qualify physical \(n=2,n=3\) carriers, establish native burden/leakage readouts, independent leakage-provider custody, units/calibration, noise covariance, event selection and null distribution. The formal \(C_0\to C_4\) chain is only a test harness.

**Recommended next action:** publish an assumption-scoped experimental *contract* with alternatives WBX1, affine HCB1/WBQ1, nonstationary PLB1, and polynomial-degree-2 controls; specify E3 holdout and independent leakage, then commission carrier validation. Until then the theorem is EXACT_CONDITIONAL and the computations NUMERICAL_SYNTHETIC. Physical promotion = 0; non-constructor review deferred.

## 8. Reproduction

```
python3 pred01_engine.py --out results.json --draws 10000 --seed 20261031
python3 -m unittest discover -v
```

No network, hardware or non-stdlib Python packages are required for the captured scripts. A separate SymPy 1.14 check (not a dependency) independently expanded the recurrence, confirmed \(D_2=\kappa(C+\kappa A)\), \(T_3=\kappa^2(C+\kappa A)\), \(H_4=0\), and confirmed the source fourth-event formula.
