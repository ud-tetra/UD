# THM-534 v2.25 — Local native clock and phase-retaining capture

**2 November 2026.** EXACT under the stated finite carrier, metric, preparation and continuous evolution assumptions. A revised clock-assisted capture rule is CANDIDATE; its scoped local invertibility is proved. Clock preparation and autonomous mode realization remain OPEN. No physical time or action unit is identified.

## Abstract

The original two-tetrahedron carrier contains a native two-dimensional oscillatory mode with frequency $\sqrt3$ in the supplied generator parameter. Every whole-face mask acts identically on this mode. On a specified preparation sector, its two coordinates can be read from one private vertex and its three incident edges. The readout cancels arbitrary active cycle/face/core fields, and its scaled error is at most the full field error. The clock contributes a constant, exactly allocated stock to each cell.

This supplies a local phase signal, not an event-time memory. With the same prepared clock and common observation parameter, the clock evolves independently of the peak time. The unchanged peak-and-hold protocol still has an explicit continuum of identical final fields. Face masks cannot generate an initially absent clock or freeze its nonzero phase. Event-indexed clock sampling restores the missing direction locally, but the event sample itself must be retained. Continuous and finite Cayley clock parameters are distinguished.

A revised five-amplitude guard compares the output face sum with a private-vertex clock amplitude. The same native hold mask then retains that event-phase value in the existing protected face coordinate. A nonzero switch determinant and an explicit local inverse establish that this modified capture avoids the original phase collapse on its declared branch. Its clock preparation, mode initialization and ideal event execution are supplied assumptions.

## 1. Objects, sources and scope

Use oriented cells $[0123]$ and $-[0124]$, unique simplex grades of sizes $(5,9,7,2)$, and the original real unit metric. The state is

$$
x=(v,e,f,c)\in\mathcal H=C_0\oplus C_1\oplus C_2\oplus C_3.
$$

For the signed incidence matrices $B_1,B_2,B_3$, $B_1B_2=B_2B_3=0$. With one binary whole-face gate per face,

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix},\qquad H=\operatorname{diag}(h).
$$

Faces are ordered $012,013,014,023,024,123,124$. The continuous evolution is $\dot x=A_{h(t)}x$, with supplied, piecewise constant masks and no state reset. State-dependent switching is allowed where its trajectory is well defined. The model parameter is $t$; no map to seconds is supplied. The orthogonal active sector is

$$
\mathcal A=\ker B_1\big|_{C_1}\oplus C_2\oplus C_3,\qquad \dim\mathcal A=14.
$$

Sources: coefficient ledger v0.39, Q169–Q179; v2.23 §§1–4 for the transverse peak protocol and event-time loss; v2.24 §§1–2 and its gradient-sector discussion for controlled writers and invariant sectors. Exact source snapshots accompany this proof. Immutable sources: [v2.23/v2.24 capture](https://github.com/ud-tetra/UD/tree/d233a82d13010bae262f1d297cf43bfaef81e8a9/captures/2026-10-28T151619Z-codex-thm534-writer-compile-5e7c109a). The [project portal](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/) currently states independent review pending and physical promotion 0; it does not supply a native clock preparation law. The present contribution is the private-star readout, its preparation/robustness contract, clock ownership receipts and the prepared-clock collision audit.

The source ledger's full all-on spectrum is not being reassigned to this two-coordinate mode: its $\sqrt3$ frequency is proved directly below. No fitted experimental target enters this calculation.

## 2. A gate-independent native oscillator

Let $w$ have vertex amplitudes $w_3=1$, $w_4=-1$, all other amplitudes zero. Define $d$ by its edge grade

$$
d=B_1^{\mathsf T}w,\qquad d\in C_1\subset\mathcal H.
$$

The nonzero edge entries are $d_{03}=d_{13}=d_{23}=1$ and $d_{04}=d_{14}=d_{24}=-1$. Direct incidence calculation gives

$$
B_1B_1^{\mathsf T}w=3w,\qquad
\|w\|^2=2,\quad \|d\|^2=6,\quad w^{\mathsf T}d=0.
$$

**Theorem 1 (native clock plane).** Every admissible mask satisfies

$$
A_hw=d,\qquad A_hd=-3w.
$$

Thus $\mathcal C=\operatorname{span}\{w,d\}$ is invariant and orthogonal to $\mathcal A$. For $g=aw+bd$,

$$
\dot a=-3b,\qquad \dot b=a,\qquad
\|g\|^2=2a^2+6b^2.
$$

With the supplied preparation $g(0)=rw$, $r>0$,

$$
g(t)=r\cos(\sqrt3t)\,w+
\frac r{\sqrt3}\sin(\sqrt3t)\,d.
$$

*Proof.* The first identity uses only the vertex–edge block. For the second, the vertex block is $-B_1d=-3w$, and the face block is $B_2^{\mathsf T}d=(B_1B_2)^{\mathsf T}w=0$. Neither expression involves a face gate. An active edge cycle is orthogonal to $d$, and its vertex grade is zero. The oscillator equations and norm follow by substitution. They hold on every switching interval and extend across continuous switch states. $\square$

The mode is an existing native carrier, rather than an added record coordinate. Its initial radius, polarity and phase origin are preparation data. The frequency follows the chosen native generator normalization; it is not a physical clock calibration.

## 3. A four-amplitude local readout and its limits

**Preparation contract.** Restrict the nominal field to

$$
x=a_{\rm act}+aw+bd,\qquad a_{\rm act}\in\mathcal A.
$$

The other seven gradient/uniform coordinates are nominally absent. All native masks preserve this sixteen-dimensional sector.

Define the linear local readout

$$
\mathscr R(x)=
\left(
v_3,\frac{(B_1e)_3}{3}
\right)=
\left(
v_3,\frac{e_{03}+e_{13}+e_{23}}3
\right)\in\mathbb R^2.
$$

Its support consists of vertex $3$ and the three edges incident to it, all in cell $0123$.

**Theorem 2 (active-field rejection and robustness).** Under the preparation contract,

$$
\mathscr R(x)=(a,b).
$$

For an arbitrary additive full-field error $\eta$ at readout, define $Y(x)=(\mathscr R_1(x),\sqrt3\mathscr R_2(x))$. Then

$$
\|Y(x+\eta)-Y(x)\|_2\le\|\eta\|_2.
$$

For the nominal radius-$r$ clock, an error $\|\eta\|_2\le\epsilon<r$ changes its phase by at most

$$
|\delta\theta|_{\rm circular}\le\arcsin(\epsilon/r).
$$

On a known unwrap branch with sufficient distance from its cut, the corresponding parameter estimate obeys

$$
|\delta t|\le\frac1{\sqrt3}\arcsin(\epsilon/r).
$$

*Proof.* Active vertices vanish, while $B_1e_{\rm act}=0$. At vertex $3$, $w_3=1$ and $(B_1d)_3=3$. The two rows of $Y$ have disjoint supports and unit Euclidean row norms, hence its operator norm is one. The angular estimate is the tangent-angle bound for a radius-$\epsilon$ disk about a vector of length $r$. Division by the nominal angular speed yields the time-parameter bound. $\square$

The branch inverse is

$$
t=\frac{\operatorname{atan2}(\sqrt3b,a)+2\pi k}{\sqrt3}.
$$

The integer $k$ must be specified by a bounded observation window or a retained lap count. One clock cycle alone does not encode unbounded elapsed parameter. The error statement is about readout error on a declared branch, not a general adaptive-controller stability theorem.

The preparation restriction is material. The field with only vertex $0$ equal to one has $\mathscr R(x)=(0,0)$ but

$$
\mathscr R(A_hx)=(0,-1/3).
$$

Consequently this local readout does not close as a clock on the unrestricted carrier. Other prepared gradient modes require separation or an amended readout.

## 4. Exact stock receipts

Let $W_\tau$ be the original diagonal equal-top-star ownership metric for cell $\tau$:
$w_{\sigma,\tau}=1/n_3(\sigma)$ on its simplices. This is the Q177 ownership map, not a new normalization.

**Theorem 3 (clock stock allocation).** For $g=aw+bd$ and each of the two cells,

$$
g^{\mathsf T}W_\tau g=a^2+3b^2,\qquad
a_{\rm act}^{\mathsf T}W_\tau g=0\quad(a_{\rm act}\in\mathcal A).
$$

Thus with preparation $g(0)=rw$, the clock has total stock $2r^2$ and contributes exactly $r^2$ to each cell at every continuous clock phase.

*Proof.* Each cell contains one nonzero private clock vertex and three nonzero private clock edges, each with ownership one. There are no clock amplitudes on shared simplices. The only possible cross term with the active field is the sum of active cycle edges incident to the private vertex. It vanishes because $B_1e_{\rm act}=0$. Finally $a^2+3b^2$ is conserved by Theorem 1. $\square$

This proves an additive cell stock decomposition on the stated sector even though ownership metrics need not respect arbitrary orthogonal decompositions. It supplies no fresh stock, source law, physical energy or action quantum.

## 5. Why this clock does not retain the peak time

Let $A=A_{\mathbf1}$ load the active field, and $B=A_{(0,1,0,1,0,1,0)}$ hold it. Put $q=e_{\mathrm{core}\,1}$ and let $n$ be column $1$ of $B_3$ embedded in faces. The strict peak guard is

$$
n^{\mathsf T}z=0,\qquad c_1(4c_1-c_0)>0.
$$

The hold mask satisfies $Bn=Bq=0$. The incoming normal speed at $q$ is $n^{\mathsf T}Aq=-4$.

**Theorem 4 (fixed-clock common-time collision).** Prepare the same clock $g_0=rw$ at parameter zero for every active input. In the unchanged peak-and-hold protocol, observing both active field and native clock at a known common parameter $T$ does not recover the event time.

*Proof.* Choose a sufficiently small $\tau_0>0$ and $s$ near zero so that $\tau_0-s>0$. Define active inputs

$$
a_s=e^{-(\tau_0-s)A}q.
$$

In a sufficiently short incoming neighborhood of the strict peak, their first guard hit is $q$ at $\tau_s=\tau_0-s$. These inputs are distinct, of equal norm, since $Aq\ne0$. After the hit, $Bq=0$. For any fixed $T$ beyond all these hits, the complete output is

$$
x_s(T)=q+e^{TD|_{\mathcal C}}g_0,
$$

independent of $s$, where $D|_{\mathcal C}$ denotes the common clock generator from Theorem 1. Both clock and active output therefore coincide while the event times differ. $\square$

This is a fixed-clock-preparation collision, not merely a comparison that permits different initial clock phases. It lies in the active input norm sphere. A specially restricted preparation family can remove the ambiguous direction; the claim concerns admitted phase perturbations around the peak protocol.

At a strict transverse event, the active switch differential is

$$
S_{\mathcal A}=I_{\mathcal A}
+\frac{(Bz-Az)n^{\mathsf T}|_{\mathcal A}}{n^{\mathsf T}Az},
\qquad \operatorname{rank}S_{\mathcal A}=13.
$$

At $z=q$, it is $I_{\mathcal A}-nn^{\mathsf T}/4$. Appending the common-$T$ clock does not increase rank: its derivative with respect to active preparation is zero.

By contrast, the event-indexed output

$$
a\longmapsto\big(e^{\tau(a)A}a,\ e^{\tau(a)D|_{\mathcal C}}g_0\big)
$$

has rank $14$ locally. Indeed, the missing active direction changes $\tau$, and the clock tangent $D|_{\mathcal C}g(\tau)$ is nonzero. On a known clock branch the event phase determines $\tau$, and the inverse active preparation is $a=e^{-\tau A}z$.

The event-indexed clock value is available at the event. It is not automatically retained at a later common parameter. Sampling, a retained event time, an event-sensitive write, or a changed capture law would constitute additional operations whose dynamics and receipts must be supplied.

## 6. No generation or clock parking by face gates

**Theorem 5 (scoped no-go).** Under the continuous native generator family, with face gating only and no resets or additional terms:

1. An initially absent clock remains absent, including under state-dependent mask choices.
2. A nonzero clock in $\mathcal C$ cannot be parked by any face mask or mask sequence.
3. Two trajectories with the same prepared clock have the same clock at every common parameter, irrespective of their face-mask histories.

*Proof.* The clock always satisfies the same homogeneous two-dimensional equation of Theorem 1. Its zero solution is invariant, its common-parameter solution depends only on its initial clock, and

$$
\|A_hg\|^2=3\|g\|^2>0
$$

for a nonzero clock. In particular the phase continues during every core-isolating hold mask. $\square$

This is not a no-go against clock-to-active control: a supplied state-dependent mask rule can read clock phase and affect the active field. It is not a no-go against an active record written before phase loss. It does exclude calling a passive face-gate-independent oscillator an event-sensitive stored receipt.

## 7. Cayley clock: exact recurrence, different parameter semantics

For a supplied positive Cayley step

$$
C_h(t)=\left(I-\frac t2A_h\right)^{-1}
\left(I+\frac t2A_h\right),
$$

the clock recurrence is mask independent:

$$
\begin{pmatrix}a^+\\b^+\end{pmatrix}
=\begin{pmatrix}\alpha(t)&-3\beta(t)\\
\beta(t)&\alpha(t)\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix},
\quad
\alpha(t)=\frac{1-3t^2/4}{1+3t^2/4},\quad
\beta(t)=\frac{t}{1+3t^2/4}.
$$

It preserves $a^2+3b^2$. Its phase increment is

$$
\vartheta(t)=2\arctan(\sqrt3t/2).
$$

For a sequence, the unwrapped clock phase is $\sum_n\vartheta(t_n)$, not $\sqrt3\sum_nt_n$. For example, from $(a,b)=(1,0)$, a step $t=1$ gives

$$
(a,b)=(1/7,4/7),
$$

whereas two steps $t=1/2$ give

$$
(a,b)=(-23/361,208/361).
$$

Both parameter sums are one, but the clock states differ exactly. Fixed identical Cayley parameter lists give identical clock states regardless of masks. If event-dependent step counts or parameters change that list, the clock may depend on those programme choices; that requires an explicit schedule and receipt analysis. The continuous common-$T$ collision theorem cannot silently be transferred to such altered schedules.

## 8. A local clock-assisted capture that retains event phase

This section changes the guard, not the native generators, metric or hold mask. It is a new CANDIDATE selection branch, not a reinterpretation of the exact-peak rule.

On the preparation sector of §3, the clock can equally be read from the private vertex of output cell $0124$:

$$
a=-v_4,\qquad b=-\frac{e_{04}+e_{14}+e_{24}}3.
$$

These relations follow from $w_4=-1$ and $B_1e_{\rm act}=0$. Define the revised guard

$$
\Gamma(x)=\beta_1+v_4=\beta_1-a=0.
$$

It reads vertex $4$ and faces $012,014,024,124$, all contained in the output tetrahedron. The coefficient one is a declared constitutive choice in the original amplitude units, not a uniquely derived physical coupling. The guard is homogeneous under a common amplitude scaling. Its clock amplitude relative to the active preparation remains a resource parameter.

**Candidate rule.** Start in Load with all faces open. At the first admitted negative crossing of $\Gamma$, switch to the original sticky Hold mask. Limit the branch to a known clock interval where $b\ne0$, and require incoming transversality. Mode initialization, persistence and ideal crossing detection are supplied, as in the earlier peak candidate.

Let $d_-=c_0-4c_1$ be the incoming derivative of $\beta_1$. At a prepared event,

$$
\dot\Gamma_-=d_-+3b,\qquad
\dot\Gamma_+=3b.
$$

The second equality holds because Hold freezes $\beta_1$ while the clock continues.

**Theorem 6 (conditional local reversible capture).** At any such event with $b\ne0$ and $d_-+3b\ne0$, the full $23$-dimensional common-parameter switch differential is invertible:

$$
S_\Gamma=I+
\frac{(A_{\rm hold}z-A_{\rm load}z)\nu^{\mathsf T}}
{\nu^{\mathsf T}A_{\rm load}z},
\qquad \nu=n+e_{\mathrm{vertex}\,4},
$$

$$
\boxed{\det S_\Gamma=\frac{3b}{d_-+3b}\ne0.}
$$

On the stated prepared-clock sector and a known monotone clock branch, the unchanged Hold phase retains an event-time receipt in the existing face observable:

$$
\beta_1(T)=\beta_1(\tau)=a(\tau),\qquad T\ge\tau.
$$

*Proof.* The guard is a fixed linear functional on the original carrier. The rank-one determinant identity gives the ratio of outgoing and incoming normal speeds. Their values above follow from the native clock and hold equations; neither uses a reset. Multiplication by invertible before/after flow matrices preserves rank. The hold generator annihilates $n$, so its stored face sum remains equal to its event value. By the guard, this value is $a(\tau)$. Since $a'(\tau)=-3b(\tau)\ne0$, the inverse function theorem determines $\tau$ locally. For a known clock preparation and known $T$, recover the active field at the event and its initial value by

$$
z_{\rm act}=e^{-(T-\tau)B}y_{\rm act},\qquad
a_{\rm act}(0)=e^{-\tau A}z_{\rm act}.
$$

This is an explicit inverse on the preparation sector. Full-carrier local invertibility also follows directly from the nonzero switch determinant. $\square$

An exact rational event witness is

$$
z=q+\frac13d,\qquad a=0,\quad b=\frac13.
$$

Here $\Gamma=0$, $\dot\Gamma_-=-3$, $\dot\Gamma_+=1$, and $\det S_\Gamma=-1/3$. This is a local event witness, not a claimed full preparation protocol. A fixed earlier clock state and active input realizing it can be defined by their backward native loading flows on a sufficiently short first-event interval.

This rule retains $p^{\mathsf T}x=\beta_1/2$, along with the core amplitude. It therefore uses the existing protected plane without the separate 160-step writer. It does not preserve the same exact-peak output for every input: in general $\beta_1(\tau)=a(\tau)\ne0$, so stopping occurs before or after the core maximum. This changed stopping condition is precisely the extra information channel; the §5 no-go remains valid for its original guard.

**Conditional near-peak bound.** Suppose the loading trajectory has an isolated peak at $t_*$, and on a bracket containing both $t_*$ and the revised crossing,

$$
-M\le\dot\beta_1\le-m<0,\qquad |a(t)|\le r,\qquad
|\dot a(t)|\le\sqrt3r<m.
$$

If the bracket endpoints have $\beta_1>r$ and $\beta_1<-r$, respectively, $\Gamma$ has exactly one crossing there. Moreover

$$
|\tau-t_*|\le\frac r m,\qquad
|c_1(\tau)-c_1(t_*)|\le\frac M2\left(\frac r m\right)^2.
$$

*Proof.* The endpoint signs imply existence; $\dot\Gamma\le-m+\sqrt3r<0$ gives uniqueness. At the crossing, $|\beta_1(\tau)|=|a(\tau)|\le r$. Integrating the lower slope bound from $\beta_1(t_*)=0$ bounds the time shift. Since $\dot c_1=\beta_1$ and $|\beta_1(t)|\le M|t-t_*|$, integration gives the amplitude bound. $\square$

For squared core stock the resulting error is bounded by $2|c_1(t_*)|\Delta+\Delta^2$, where $\Delta$ is the amplitude bound. These hypotheses must be checked for the selected preparation; they are not asserted uniformly over the full carrier.

There is a real precision tradeoff. On a clock branch with $|b|\ge b_{\min}>0$, an ideal stored-face-sum error $\delta\beta$ gives

$$
|\delta\tau|\le\frac{|\delta\beta|}{3b_{\min}}.
$$

Reducing the clock radius improves proximity to the peak but weakens time discrimination. The limit of zero clock stock recovers the original singular capture. The locally retained continuous record also cannot be replaced by a two-valued mode bit for exact recovery.

No extra norm is created at the switch: the state is continuous, each generator is skew, and the original ownership stocks are continuous. Only their current laws change with the mask. The protected face sum is a linear readout of existing amplitudes, not a new additive cell stock or a physical action observable.

## 9. Verification and dependency disposition

Run the supplied standard-library verifier:

    python verify_clock.py

It reconstructs the original carrier and verifies: 128 mask/mode/readout controls; 512 rational Cayley clock residuals and norm identities; all eight core-holding masks failing to park the clock; 56 cell-ownership cross-term controls; the rank-13 common-time and rank-14 event-augmented active differentials at the original rational peak; the revised guard's full rank 23 and determinant $-1/3$; 72 revised event/hold controls; the unrestricted-preparation counterexample; and the equal-parameter-sum partition counterexample. Analytic neighborhood, inverse, near-peak and phase-error arguments are supplied in the proofs, rather than inferred from finite cases. A separate control script rejects altered clock preparation and a spurious core–clock contact, and verifies fresh deterministic replay.

| Dependency | Result in this version |
|---|---|
| Existing native oscillatory carrier | EXACT: two-coordinate mode derived directly |
| Local readout immune to active fields | EXACT under the stated preparation; four amplitudes |
| Finite readout error | DERIVED bound with nonzero prepared radius and branch margin |
| Clock stock and cell ownership | EXACT: total $2r^2$, each cell $r^2$ |
| Clock preparation and phase origin | OPEN; cannot be generated from active-only input by these gates |
| Event phase available at event | EXACT locally under a declared unwrap branch |
| Later stored event time from passive clock alone | NO-GO for the unchanged continuous capture protocol |
| Revised local event-phase capture | CANDIDATE rule; EXACT conditional local inverse and error tradeoff |
| Clock-conditioned native writer programme | OPEN; revised guard bypasses a separate compiled writer for this receipt |
| Clock-driven robust selection, reset and renewal | OPEN |
| Physical time, action unit, quark/lepton correspondence | OPEN; physical promotion $0$ |

The highest-value next test is a concrete preparation interval for the revised guard, verifying unique first crossing, peak-stock penalty, inverse conditioning and signed cell receipts under perturbations. It should compare exact-peak capture and the zero-clock limit. Autonomous mode generation and renewal remain separate dependencies. An identically applied fixed-angle writer after the original collision cannot distinguish already equal fields.

Development — no registry entry. Constructor verification only; independent review pending.
