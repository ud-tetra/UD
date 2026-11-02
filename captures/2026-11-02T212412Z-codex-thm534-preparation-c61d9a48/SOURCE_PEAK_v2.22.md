# THM-534 v2.22 — A local peak guard and conditional native capture

**27 October 2026.** Exact native observable identities; a candidate first-peak capture objective; separate continuous-event and discrete-Cayley constructions.

## Abstract

For a chosen output core on the original two-cell carrier, we derive a six-amplitude guard for a strict local maximum of its stock. The lower edge contributions cancel exactly in the aggregate face derivative. With all gates initially open and a private-face feed, the first peak is explicit and transverse, and a relative preparation ball preserves a unique nearby event. A supplied binary mode can then close the four isolation gates and retain the output. Separately, a single all-on Cayley step has a unique parameter maximizing capture for this preparation family; its square is the positive root of a cubic. An exact rational implementation and signed native receipts are supplied.

**The objective here is first-peak capture.** It does not certify completion of the v2.21 full-feed transfer or restoration of its worker. Choosing this objective, the output role, initial gates and a persistent load/hold record remains a constitutive candidate. No empirical target-blindness, physical clock or action normalization is claimed.

## 1. Carrier, metric and observables

Use oriented filled cells $[0123]$, $-[0124]$, one real amplitude per unique simplex, and the original unit metric. The grades have dimensions $5,9,7,2$. Write $c=(c_0,c_1)^{\mathsf T}$ for the two core amplitudes and $f\in C_2$ for the seven face amplitudes in order

$$
012,\ 013,\ 014,\ 023,\ 024,\ 123,\ 124.
$$

The full native generator is

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix},\qquad H=\operatorname{diag}(h).
$$

All gates are binary and whole-face: the shared face gate acts on both cores. Lower incidence couplings remain present. In this basis,

$$
K:=B_3^{\mathsf T}B_3=
\begin{pmatrix}4&-1\\-1&4\end{pmatrix},
\qquad B_2B_3=0.
$$

Define the two signed face aggregates

$$
\beta=B_3^{\mathsf T}f.
$$

These observables do not eliminate any face reservoir or replace the full 23-dimensional dynamics.

## 2. Local stock-peak condition

**Theorem 1 (six-amplitude peak guard).** While all four faces of output core $1$ are open,

$$
\dot c_1=\beta_1,\qquad
\dot\beta_1=c_0-4c_1,
$$

regardless of the other three gate values. Thus its stock $S_1=c_1^2$ obeys

$$
\dot S_1=2c_1\beta_1,\qquad
\ddot S_1=2\beta_1^2+2c_1(c_0-4c_1).
$$

The state condition

$$
\boxed{\beta_1=0,\qquad c_1(4c_1-c_0)>0}
$$

is sufficient for a strict local stock maximum along the loading vector field. It reads four incident face amplitudes and two core amplitudes.

*Proof.* Let $b_1$ be column $1$ of $B_3$. Its support is exactly the four incident faces. The open gates give $\dot c_1=b_1^{\mathsf T}f$. Moreover,

$$
\dot\beta_1
=b_1^{\mathsf T}B_2^{\mathsf T}e
-b_1^{\mathsf T}HB_3c
=-(Kc)_1=c_0-4c_1.
$$

The first term vanishes because $B_2b_1=0$, and $b_1^{\mathsf T}H=b_1^{\mathsf T}$. Differentiate the stock twice and apply the strict second-derivative test. $\square$

The covariant form of the second condition is $c_1(Kc)_1>0$; signs above use the stated oriented basis. Uniform amplitude rescaling, including sign reversal, preserves the guard. No target amplitude, fitted threshold or prescribed event time appears in it.

The condition detects a local maximum, not delivery of a specified stock or completion of a worker-restoration task. A dark trajectory or a degenerate maximum can fail to meet this strict guard.

For an initially empty core, the strict curvature inequality is false. The guard therefore avoids treating the initially zero stock current as completion. Within the admitted loading family below, no separate occupancy threshold or arming record is needed.

## 3. A loading family with an explicit first event

Assume all seven gates remain open during loading. The four observables $(c,\beta)$ close:

$$
\frac{d}{dt}\begin{pmatrix}c\\\beta\end{pmatrix}
=L\begin{pmatrix}c\\\beta\end{pmatrix},
\qquad
L=\begin{pmatrix}0&I\\-K&0\end{pmatrix}.
$$

The observable map need not be an isometry. Its inherited invariant metric is

$$
G=\operatorname{diag}(I_2,K^{-1}),\qquad
K^{-1}=\frac1{15}\begin{pmatrix}4&1\\1&4\end{pmatrix}.
$$

Indeed, $L^{\mathsf T}G+GL=0$, and
$P=B_3K^{-1}B_3^{\mathsf T}$ is the orthogonal face projector onto
$\operatorname{im}B_3$. Thus

$$
\mathcal E_{\rm core}=\|c\|^2+\beta^{\mathsf T}K^{-1}\beta
=\|c\|^2+\|Pf\|^2
$$

is a conserved component of the original field norm during all-on loading. This is an inherited projection metric, not a replacement for the original unit metric.

Prepare

$$
c(0)=0,\qquad \beta(0)=(0,v)^{\mathsf T},\qquad v\ne0.
$$

One realization is face amplitude $-v$ on the private face $014$, with other faces zero. Vertex and edge amplitudes may be arbitrary; they do not drive these core observables under the all-on mask. In particular, an edge-only preparation with $v=0$ does not load either core in this uniform-gate model.

The available core-loading component of this face feed is exactly

$$
\mathcal E_{\rm core}(0)=\frac4{15}v^2,
$$

leaving $11v^2/15$ in the complementary face sector initially. Hence a uniform-gate loading trajectory or single uniform Cayley step cannot place the entire face-feed stock $v^2$ in the output core. The fractions are internal projection receipts, not physical action coefficients.

**Theorem 2 (first continuous peak).** Put $a=\sqrt3$, $b=\sqrt5$. Then

$$
\begin{aligned}
c_0(t)&=\frac v2\left(\frac{\sin at}{a}-\frac{\sin bt}{b}\right),\\
c_1(t)&=\frac v2\left(\frac{\sin at}{a}+\frac{\sin bt}{b}\right),\\
\beta_1(t)&=\frac v2(\cos at+\cos bt).
\end{aligned}
$$

The first positive strict stock maximum occurs at

$$
t_*=\frac{\pi}{a+b}.
$$

Its retained stock, if isolated at that event, is $v^2R_{\rm flow}$, where

$$
R_{\rm flow}
=\frac14\sin^2\left(\frac{\pi a}{a+b}\right)
\left(\frac1a+\frac1b\right)^2.
$$

*Proof.* Diagonalize $K$, with eigenvectors $(1,1)$, $(1,-1)$ and eigenvalues $3,5$. The displayed solution follows from the initial core velocities. Also,

$$
\frac{\beta_1(t)}v
=\cos\frac{(a+b)t}{2}\cos\frac{(b-a)t}{2}.
$$

Both factors are positive before $t_*$; the first crosses zero there and the second remains positive. The normalized core amplitude is positive up to this point. Hence the stock rises from zero and reaches its first strict maximum. At $t_*$, $\sin(at_*)=\sin(bt_*)>0$, giving the stock formula and a negative second derivative. $\square$

The analytic $t_*$ establishes the event; the proposed guard does not consult this time. Admitting continuous flow and ideal event detection is itself a model assumption, separate from an update index or a physical clock.

## 4. Quantified preparation robustness

**Theorem 3 (a nondegenerate local event).** Let $x_{\rm ref}$ be a preparation in Theorem 2 and perturb it by

$$
\|x(0)-x_{\rm ref}(0)\|_2\le\rho|v|,
\qquad \rho=\frac1{10000}.
$$

Under the same all-on flow, the first zero of $\beta_1$ remains unique in

$$
\left(\frac{79}{100},\frac45\right).
$$

It satisfies the strict peak guard, and its parameter $\tau$ obeys

$$
|\tau-t_*|\le\frac{20}{19}\rho=\frac1{9500}.
$$

*Proof.* Normalize $v=1$; sign reversal handles $v<0$. The exact interval checker establishes

$$
\begin{aligned}
\beta_{1,\rm ref}(79/100)&>3/1000,\\
\beta_{1,\rm ref}(4/5)&<-3/200,\\
c_{1,\rm ref}(t)&>49/100,\\
-2<\dot\beta_{1,\rm ref}(t)&<-193/100
\end{aligned}
$$

throughout the bracket for the last two statements. The all-on flow is orthogonal, so perturbation norm stays at most $\rho$. The row defining $\beta_1$ has norm $2$, and the row defining $\dot\beta_1=c_0-4c_1$ has norm $\sqrt{17}<5$. The endpoint signs therefore persist, and the perturbed derivative remains below $-19/10$ throughout the bracket. This proves existence and uniqueness there.

Before the bracket, the reference $\beta_1$ is decreasing and at least its positive value at $79/100$. The same perturbation bound prevents an earlier zero. At the root, $c_1>49/100-\rho>0$ and $\dot\beta_1<0$, giving the strict guard. At $t_*$, the perturbed aggregate has magnitude at most $2\rho$; the mean value theorem gives the root-shift bound. $\square$

For a nominal trajectory latched at $t_*+\sigma$, with the entire intervening interval inside the certified bracket, Taylor's theorem gives

$$
|c_1(t_*+\sigma)-c_1(t_*)|\le |v|\sigma^2,
$$

$$
|S_1(t_*+\sigma)-S_1(t_*)|
\le v^2\left(\frac{51}{50}+\sigma^2\right)\sigma^2.
$$

For perturbed preparation, the captured amplitude differs from the reference peak by at most

$$
|v|\left(\rho+\left(\frac{20\rho}{19}\right)^2\right).
$$

These are preparation and event-parameter bounds. They do not specify a sensor, sampling protocol, or a guarantee against arbitrary measurement noise.

## 5. Holding requires an explicit mode

A candidate hybrid controller has one supplied binary mode:

| Mode | Mask | Transition |
|---|---|---|
| Load | All seven gates open | At the first strict peak guard, enter Hold |
| Hold | $h=(0,1,0,1,0,1,0)$ | Remain in Hold |

The four zero entries isolate core $0124$. The shared face closes on both cores. The field is continuous at the switch, both generators are skew, and the core amplitude is then exactly constant while the remaining field evolves.

The binary mode is an additional record; its initialization, persistence and reset are not derived from the original 23 field coordinates. The mask state may carry that record in an implementation, but its source and cost still require accounting. Resetting the mode to Load can release the stored output. No reset or fresh-feed cycle is supplied.

Selecting a chosen core's first local maximum as “completion” is a new objective. This controller does not claim that its event completes the previously specified full-feed transfer.

## 6. A separate finite Cayley construction

Define

$$
C_A(s)=\left(I-\frac s2A\right)^{-1}
       \left(I+\frac s2A\right).
$$

For all-on $A$, the observable projection $\mathcal R x=(c,\beta)$ satisfies $\mathcal RA=L\mathcal R$. Hence its Cayley update closes exactly as well. For the preparation in Theorem 2, put $z=s^2$ and

$$
D(z)=1+2z+\frac{15}{16}z^2.
$$

Direct solution of the four-dimensional midpoint equations gives

$$
\frac{c_1^+}{v}=F(s)=\frac{s(1+s^2)}{D(s^2)},
\qquad
\frac{\beta_1^+}{v}=\frac{1-15s^4/16}{D(s^2)}.
$$

**Theorem 4 (single-step peak parameter).** The stock $v^2F(s)^2$ has a unique global maximum for $s>0$. Its parameter $s_*=\sqrt{z_*}$ is determined by the unique positive root

$$
\boxed{16+16z_*-13z_*^2-15z_*^3=0.}
$$

*Proof.* $F>0$, $F\to0$ as $s\to0$ or $s\to\infty$, and

$$
F'(s)=\frac{16+16z-13z^2-15z^3}{16D(z)^2}.
$$

The cubic is positive on $0\le z\le1$, by concavity and its positive endpoint values $16,4$. Its derivative is strictly negative for $z\ge1$, and it tends to minus infinity. There is exactly one positive critical point, with derivative changing from positive to negative. $\square$

This is an optimum only within the one-step all-on Cayley family and this preparation class. Choosing the maximization objective and Cayley convention remains explicit. It is not a unique physical gate law.

At this optimum, $\beta_1^+/v<-1/100$: the continuous peak guard does **not** characterize this parameter maximum. A Cayley-parameter curve is not a continuous-flow trajectory.

| Quantity | Continuous first peak | One-step Cayley maximum |
|---|---:|---:|
| Model parameter, approximate | $0.791708319169036$ | $1.033341848074233$ |
| Stored stock divided by $v^2$, approximate | $0.252123961320045$ | $0.258268315499635$ |
| Peak condition | Local $\beta_1=0$, strict curvature | Positive cubic root for the admitted preparation |

Exact rational enclosures, rather than these display decimals, are recorded in RESULTS.json.

An executable rational witness uses

$$
\widehat s=\frac{516670924037}{500000000000},
\qquad |\widehat s-s_*|<10^{-12}.
$$

ONE_STEP_RECEIPT.json gives the exact 23-coordinate result of that all-on step from the earlier preparation $x_{\rm w}+(24/37)e_{014}$, followed by the isolating mask. It checks norm $4683/1369$, signed equal-top-star cell-stock receipts, and three subsequent hold steps. For this input, the state error relative to the ideal algebraic-parameter step is below $10^{-11}$, using $\|dC_A/ds\|_2\le\|A\|_2\le5$ and input norm below $2$. The rational precision is an implementation convention, not a new native physical constant.

The resulting retained stock is approximately $0.108665120327093$, compared with initial face-feed stock $576/1369$. The remaining support remains in the native field; the worker is not restored. No full-load success or improvement over the earlier transfer task is asserted.

## 7. Exact checks and open source questions

Run from the capture directory:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_local_peak.py

The checker uses only standard-library rational arithmetic. It reconstructs the native boundaries, proves observable intertwining by exact matrix identities, checks all eight local-load variants and eight isolation masks, and compares twelve full native rational Cayley updates to the reduced formulas. It encloses square roots by integer bounds, $\pi$ by alternating arctangent series and the Machin identity, and trigonometric functions by Taylor intervals with explicit remainders. Twenty rational time subintervals certify the uniform transversality bounds. Eighty rational bisections isolate the cubic root. The final full-state loading and holding checks are exact.

For reproduction of the analytic enclosures, the identity

$$
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}
$$

follows from the tangent addition formula and its angle lying between $0$ and $4/5<\pi/2$. Alternating arctangent sums are bounded by consecutive partial sums. Fourteen sine and cosine terms have remainders at most $|z|^{29}/29!$ and $|z|^{28}/28!$, respectively. Every interval operation rounds outward on a rational grid of denominator $10^{24}$. The interval tests do not rely on floating trigonometric evaluations.

The progress is a local strict-peak detector, a robust admitted event family, and a finite conditional capture construction. Source questions remain: why choose this objective and output role; how initialize and implement the mode and gate changes; how detect an event in a native clock model; how restore the worker, reset records and renew supply; and how obtain a physical action-unit map.

The protocol contains no empirical amplitude target, but it was developed after historical data exposure and is not a retrospective target-blind registration. Independent review is pending. Physical promotion remains zero.
