# THM-534 v2.26 — Preparation interval and signed capture certificate

**2 November 2026. EXACT CONDITIONAL.** The certificate applies to the specified continuous native two-mode system. Its proposed selection rule, prepared clock, sticky mode and ideal event detection remain supplied assumptions. Independent review is pending; no physical correspondence is asserted.

## Abstract

We give a concrete, reproducible preparation certificate for the five-amplitude guard introduced in THM-534 v2.25. Every initial field in a full 23-dimensional Euclidean ball of radius $1/10^6$ around a specified private-face input and prepared native clock has exactly one first crossing in a rational interval. Incoming and outgoing normal-speed bounds prove an invertible switch differential throughout that ball. The captured core stock exceeds $1/4$. We bound the nominal peak-capture penalty, certify a noisy inverse on a known observation branch, and enclose signed cell-stock receipts during loading and holding. The state and cell stocks are continuous at the switch. The certificate uses rational outward intervals and exact native incidence identities.

## 1. State space, sources and conventions

Use the oriented cells $[0123]$ and $-[0124]$, their unique real simplex amplitudes, and the original unit Euclidean metric on

$$
\mathcal H=C_0\oplus C_1\oplus C_2\oplus C_3,\qquad
\dim\mathcal H=5+9+7+2=23.
$$

For lexicographically ordered simplices, boundary columns use the alternating deletion sign; the second top-cell orientation is negative. Faces are ordered $012,013,014,023,024,123,124$. The native binary whole-face generator is

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix},\qquad H=\operatorname{diag}(h).
$$

One shared-face gate controls both incident core contacts. Set

$$
A=A_{(1,1,1,1,1,1,1)},\qquad
B=A_{(0,1,0,1,0,1,0)}.
$$

During Load, $\dot x=Ax$. At the first admitted negative crossing of the guard below, switch continuously to Hold, $\dot x=Bx$, and retain that mode. There is no state reset or impulse. Observation is at the known model parameter $T=1$. This generator parameter is dimensionless; it is not physical time.

Let $q$ be the core-$1$ unit vector, and $n$ the second column of $B_3$ embedded in faces. Define

$$
\beta_1=n^{\mathsf T}x,\qquad
\Gamma(x)=\beta_1+v_4=\nu^{\mathsf T}x,\qquad
\nu=n+e_{\mathrm{vertex}\,4}.
$$

The guard reads four boundary faces and private vertex $4$, all within output cell $0124$. Its coefficient one is a declared constitutive choice. It is not a derived universal coupling.

Sources are the coefficient ledger v0.39, Q169–Q179, THM-534 v2.22 §§1–5, and v2.25 §§2–8. Source snapshots accompany this capture. The immutable v2.25 dependency is [commit b7fdf7210560b948e2c10f52b3f49020d2593b67](https://github.com/ud-tetra/UD/tree/b7fdf7210560b948e2c10f52b3f49020d2593b67/captures/2026-11-02T192806Z-codex-thm534-native-clock-b58ac031). This is a development extension, not an amendment of the original exact-peak guard.

## 2. Concrete preparation and closed nominal observables

Let $w$ have vertex amplitudes $w_3=1$, $w_4=-1$, with all others zero. Its vertex–edge image is $d=A_hw$ for every mask. Exact incidence identities give

$$
A_hw=d,\qquad A_hd=-3w,\qquad
\|w\|^2=2,\quad \|d\|^2=6.
$$

Choose

$$
r=\frac1{1000},\qquad
\bar x_0=-e_{\mathrm{face}\,014}+rw,\qquad
x_0=\bar x_0+\eta,\quad \|\eta\|_2\le\epsilon=\frac1{10^6}.
$$

The field error $\eta$ may occupy **any of the 23 coordinates**; it need not remain in the nominal active-plus-clock sector. The nominal norm is

$$
\|\bar x_0\|^2=1+2r^2=\frac{500001}{500000}.
$$

For nominal all-on loading, put $s_3=\sqrt3$, $s_5=\sqrt5$. The core and boundary observables are

$$
c_0(t)=\frac12\left(\frac{\sin(s_3t)}{s_3}
-\frac{\sin(s_5t)}{s_5}\right),
$$

$$
c_1(t)=\frac12\left(\frac{\sin(s_3t)}{s_3}
+\frac{\sin(s_5t)}{s_5}\right),
$$

$$
\beta_1(t)=\frac{\cos(s_3t)+\cos(s_5t)}2,
\qquad
\dot\beta_1(t)=
-\frac{s_3\sin(s_3t)+s_5\sin(s_5t)}2.
$$

The nominal clock is $a(t)w+b(t)d$, where

$$
a(t)=r\cos(s_3t),\qquad
b(t)=\frac r{s_3}\sin(s_3t),\qquad v_4(t)=-a(t).
$$

Consequently the nominal guard is $G(t)=\beta_1(t)-a(t)$.

## 3. First-crossing and perturbation theorem

Define the broad branch and the smaller event interval

$$
J=\left[\frac{79}{100},\frac45\right],\qquad
I=\left[\frac{1979}{2500},\frac{39581}{50000}\right]\subset J.
$$

**Theorem 1 (unique first capture on a full preparation ball).** Every $x_0$ in the preparation ball of §2 has a unique first zero of $\Gamma$ in $I$. This is a negative crossing. No zero occurs earlier. At its crossing, the incoming and outgoing normal speeds satisfy

$$
-2<\dot\Gamma_-<-\frac{19}{10},\qquad
\frac1{625}<\dot\Gamma_+<\frac1{500}.
$$

If $\tau_\eta$ is its event parameter and $\tau_0$ the nominal event parameter, then

$$
|\tau_\eta-\tau_0|
\le\frac{30}{19}\|\eta\|_2
<\frac1{500000}.
$$

The first inequality also holds at $\eta=0$; the final strict bound follows from the declared maximum radius.

*Proof.* Orthogonality of the supplied native loading flow gives

$$
\|e^{tA}\eta\|_2=\|\eta\|_2.
$$

The verifier checks exact row norms

$$
\|\nu\|^2=5,\qquad
\|A^{\mathsf T}\nu\|^2=20,\qquad
\|B^{\mathsf T}\nu\|^2=3.
$$

Therefore, at the same loading parameter, perturbations of the guard and its incoming derivative are bounded respectively by $3\epsilon$ and $5\epsilon$. The outgoing rate is perturbed by at most $2\epsilon$.

Before $79/100$, $\beta_1$ decreases from one: both sine arguments lie in $(0,\pi)$, since $s_5(4/5)<3<\pi$. Its value at $79/100$ exceeds $3/1000$. Since $|a|\le1/1000$,

$$
\Gamma(e^{tA}x_0)>
\frac3{1000}-\frac1{1000}-3\epsilon>0
\quad\left(0\le t\le\frac{79}{100}\right).
$$

The rational interval calculation establishes

$$
G\left(\frac{1979}{2500}\right)>\frac1{100000},
\qquad
G\left(\frac{39581}{50000}\right)<-\frac1{50000}.
$$

These signs survive the preparation ball. Twenty rational subintervals cover $J$. On each, outward sine and cosine enclosures prove the stated speed bounds after adding the full perturbation margins. In particular the incoming guard is strictly decreasing on $J$. Existence follows from the endpoint signs and continuity; monotonicity and the earlier exclusion prove first-hit uniqueness.

For the nominal root and perturbed root, the guard discrepancy is at most $3\|\eta\|$. The mean value theorem with slope magnitude at least $19/10$ gives the time-shift bound. The bounds apply to the unswitched Load flow until its unique event; after crossing the mode is sticky. $\square$

The interval endpoints are a robust certificate, not a fitted event time. A much narrower rational enclosure for $\tau_0$ is recorded in RESULTS.json:

$$
\tau_0\in
\left[
\frac{197901578644588253}{250000000000000000},
\frac{158321262915670603}{200000000000000000}
\right].
$$

## 4. Invertibility, held observables and noisy reconstruction

**Theorem 2 (nondegenerate capture and retained core).** Throughout the preparation ball, the common-$T$ switch differential is invertible on the full carrier. Its saltation determinant satisfies

$$
-\frac1{950}<\det S_\Gamma<-\frac1{1250}.
$$

Both $\beta_1$ and $c_1$ remain exactly constant throughout Hold, and the captured core stock obeys

$$
c_1(\tau_\eta)^2>\frac14.
$$

*Proof.* The event differential is

$$
S_\Gamma=I+
\frac{(Bz-Az)\nu^{\mathsf T}}{\nu^{\mathsf T}Az}.
$$

The rank-one determinant formula gives

$$
\det S_\Gamma=\frac{\nu^{\mathsf T}Bz}{\nu^{\mathsf T}Az}
=\frac{\dot\Gamma_+}{\dot\Gamma_-}.
$$

The speed intervals of Theorem 1 imply the stated nonzero negative interval. The before/after exponentials are invertible, so the full common-$T$ map has rank 23 locally. This establishes local invertibility on the admitted sticky-mode branch, not a global inverse over multiple event branches.

Exact incidence checks give $Bn=Bq=0$ for all eight masks closing the output core's four incident faces. Hence both readouts stay constant. Over $I$, the full-ball core-amplitude interval lies strictly above $1/2$, as verified in RESULTS.json. Squaring proves the lower stock bound. $\square$

This extension does not assume an uncontaminated clock plane for its local inverse. Given a full output $y=x(T)$ and known $T=1$, define

$$
F_y(s)=\nu^{\mathsf T}e^{-(T-s)B}y,\qquad s\in J.
$$

The true event is a root, with positive derivative. After finding it, reconstruct

$$
z=e^{-(T-\tau)B}y,\qquad x_0=e^{-\tau A}z.
$$

**Theorem 3 (bounded-noise inverse on the declared branch).** Let $y$ be an output from the preparation ball. If $\widehat y=y+\xi$ and $\|\xi\|_2\le\sigma=1/10^7$, then $F_{\widehat y}$ has a unique root in $J$, and

$$
|\widehat\tau-\tau|\le3000\|\xi\|_2.
$$

*Proof.* Hold annihilates the face sum, while the entire vertex/gradient sector evolves identically under all face masks. Thus the outgoing derivative bounds used in Theorem 1 extend to the backward-Hold branch over $J$, even when $s$ precedes the actual event. A readout perturbation changes $F$ by at most $3\|\xi\|$ and $F'$ by at most $2\|\xi\|$. Hence

$$
F'_{\widehat y}>\frac1{625}-2\sigma>\frac1{1000}.
$$

At the left branch endpoint the exact-output root has margin at least $(\inf I-\inf J)/625$; the analogous right margin is $(\sup J-\sup I)/625$. Both exceed $3\sigma$. Endpoint signs and monotonicity establish a unique perturbed root. The mean value theorem yields the bound. $\square$

This concerns error in the full output field at a known observation parameter. A scalar face-only readout with unknown contaminated clock preparation is not claimed sufficient. The factor 3000 is a conservative bound, not an optimal condition number.

## 5. Capture penalty relative to the original nominal peak

For the specified nominal active preparation, the original core maximum is at

$$
t_*=\frac{\pi}{\sqrt3+\sqrt5}.
$$

The rational enclosures prove

$$
\frac1{10000}<t_*-\tau_0<\frac{11}{100000}.
$$

Thus nominal capture occurs before the exact peak. On $J$, $-2<\dot\beta_1<0$ and $\dot c_1=\beta_1$. Integrating from the zero of $\beta_1$ gives

$$
0<c_1(t_*)-c_1(\tau_0)
<\left(\frac{11}{100000}\right)^2
=\frac{121}{10000000000}.
$$

Since $c_1(t_*)<51/100$, a conservative squared-core-stock penalty bound is

$$
0<c_1(t_*)^2-c_1(\tau_0)^2
<
\frac{1234200014641}{100000000000000000000}.
$$

This small penalty is a **nominal-preparation statement**. The full perturbation ball has the separate retained-stock bound of Theorem 2. Comparing each perturbed trajectory to its own peak would require an additional error statement and is not silently substituted here.

## 6. Signed cell receipts through load, switch and hold

Use the original equal-top-star weights

$$
w_{\sigma,\tau}=
\begin{cases}
1/n_3(\sigma),&\sigma\subset\tau,\\
0,&\text{otherwise}.
\end{cases}
$$

For cell $\tau=0,1$, let $W_\tau$ be the corresponding diagonal matrix and
$O_\tau(x)=x^{\mathsf T}W_\tau x$. The verifier checks $W_0+W_1=I$.

For every native mask and every real field,

$$
\dot O_\tau=x^{\mathsf T}(W_\tau A_h-A_hW_\tau)x
=2\sum_{i<j}(w_{i,\tau}-w_{j,\tau})(A_h)_{ij}x_ix_j.
$$

The exact polynomial coefficients of both forms are checked independently for all 128 masks and both cells: 256 identities. Integrating separately on Load and Hold defines the **signed** receipts

$$
\Delta O_\tau^{L}=O_\tau(z)-O_\tau(x_0),\qquad
\Delta O_\tau^{H}=O_\tau(y)-O_\tau(z).
$$

These are signed net transfers, not unsigned total variation or a consumable source budget. No quadrature estimate is needed to identify them: the integrated native continuity identity proves the equality with the signed current integral.

**Theorem 4 (certified receipts on the full preparation ball).** At the event and at $T=1$, the verified endpoint enclosures give the following outward-rounded rational bounds:

| Stage | Cell 0 signed receipt | Cell 1 signed receipt |
|---|---:|---:|
| Load | $[147503,147592]/10^6$ | $[-147592,-147503]/10^6$ |
| Hold through $T=1$ | $[6197,6475]/10^6$ | $[-6475,-6197]/10^6$ |
| Entire trajectory | $[153789,153978]/10^6$ | $[-153978,-153789]/10^6$ |

For each actual trajectory the paired receipts are exactly opposite; the interval endpoints are correlated enclosures. The switch itself has

$$
\Delta O_0^{\rm switch}=\Delta O_1^{\rm switch}=0.
$$

*Proof.* A direct spectral decomposition of the entire nominal active input supplies the loading field, including lower grades. For $f_0=-e_{\mathrm{face}\,014}$, define

$$
p_3=\frac{A^2+5I}{2}f_0,\qquad p_5=f_0-p_3.
$$

The verifier checks $A^2p_3=-3p_3$ and $A^2p_5=-5p_5$. Hence the nominal full field is

$$
\bar x(t)=
\cos(s_3t)p_3+\cos(s_5t)p_5+
\frac{\sin(s_3t)}{s_3}Ap_3+
\frac{\sin(s_5t)}{s_5}Ap_5
+r\cos(s_3t)w+\frac r{s_3}\sin(s_3t)d.
$$

Outward intervals evaluate it over $I$. Holding is enclosed by a degree-32 Taylor polynomial for $e^{B(1-\tau)}$, with explicit tail. Since $\|B\|_\infty\le5$ and $5(1-\inf I)<2$, the infinity-norm tail is at most

$$
9\|\bar x(I)\|_\infty
\frac{[5(1-\inf I)]^{33}}{33!}.
$$

Here $\|\bar x(I)\|_\infty$ denotes the maximum absolute endpoint in the interval box. The bound follows from $e^z<9$ for $0\le z<2$.

For each actual event parameter, the perturbed loading and held fields differ from the corresponding nominal fields by at most $\epsilon$ in 2-norm, because both phase flows are orthogonal. With

$$
N=\frac{1000001}{1000000}>\|\bar x_0\|_2,
$$

each owned quadratic stock changes by at most $(2N+\epsilon)\epsilon$. A tighter initial-cell-0 margin is $(2r+\epsilon)\epsilon$. These margins are included in every reported receipt. The continuity polynomial, endpoint enclosures and conservation $W_0+W_1=I$ prove the signed bounds. Field continuity at the switch gives zero instantaneous stock jump. $\square$

The nominal initial allocation is exactly

$$
(O_0,O_1)(\bar x_0)=
\left(\frac1{10^6},\frac{1000001}{10^6}\right).
$$

The total perturbed norm is conserved, but it need not equal the nominal norm. In particular the receipt pairing uses conservation along each individual trajectory, not replacement of its initial norm by the nominal value.

Although $\beta_1$ and the core remain fixed, owned cell stock continues to transfer in Hold. The positive Hold receipt in cell 0 explicitly distinguishes stored readouts from a frozen whole field. No reset, dissipation, energy or physical action law follows from these norm receipts.

## 7. Verification, controls and limitations

Run:

    python verify_preparation.py
    python verify_controls.py

All arithmetic for certification is rational. Square-root bounds use integer square roots; sine and cosine use 14 Taylor terms and analytic remainder bounds, with outward rounding on a grid of denominator $10^{24}$. The peak comparison uses a rational Machin enclosure for $\pi$. Source v2.22 supplies the interval method, which is reproduced in interval_exact.py.

Six full-field loading controls compare the spectral formula with a separately constructed degree-56 native matrix-exponential Taylor enclosure. This is a distinct calculation, not independent peer review. The signed receipts use exact continuity identities and endpoint enclosures; an independent numerical current quadrature is not claimed.

RESULTS.json retains the exact root, slope, determinant, peak-penalty and reconstruction bounds. SIGNED_CELL_RECEIPTS.json retains the finer endpoint stocks, rates and signed integrals. Mutation controls reject a zero clock, an excessive preparation radius and a reopened output-core gate; fresh replay must match both results files byte for byte.

The result closes the **declared preparation-domain certificate** for this proposed continuous capture rule. Clock generation, sticky-mode initialization and persistence, native crossing detection, reset/renewal and a physical clock/action map remain OPEN. It does not establish a global controller or empirical target-blind preregistration.

Development only; independent review pending. Physical promotion: 0.
