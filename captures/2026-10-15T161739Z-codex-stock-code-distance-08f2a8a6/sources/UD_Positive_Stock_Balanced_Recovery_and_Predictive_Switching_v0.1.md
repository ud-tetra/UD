# UD positive stock, balanced recovery and predictive switching v0.1

15 October 2026 UTC. Development — no registry entry. Constructor verified; independent review pending. Physical promotion 0.

**Result.** A consistent finite-capacity mechanism can be constructed by distinguishing a signed transport amplitude from a positive accumulated load. Dissipation of the transport amplitude supplies a nonnegative source; a separate export reaction removes load into an explicitly counted finite reservoir. A common gate on each balanced vertex star preserves the protected sector. Capacity and a declared control-latency budget then yield a predictive stopping guard. Restoration follows under available contacts and positive rates.

These results derive consequences of a **new, explicitly declared constitutive model**. The supplied UD sources do not uniquely select its kinetic coefficients, capacities, load interpretation or controller. This closes a mathematical construction task, not the native-source or physical-identification gap.

## 1. Sources and declared additions

The attached ledger v0.39(2) supplies the relevant scope: C03 leaves the local admissibility law open; Q153/Q158 distinguish continuity from a predictive source; Q156 defines a hard closure/integrity gate; Q162 is a conditional relaxational lane; Q178 leaves environment and renewal terms open. No use is made of 7/768 as a capacity. The attached CRL-2 amendment is a governance proposal; constructor checking does not provide independent review.

The preceding reports are PR114, commit `a575840cd2e4df93874f0bcac7b621390f83b77f`, and PR115, commit `15759c782a7053c7a80332f46ef17fbc3942f962`. Their safe-port and positivity results are re-used with their stated unit-metric premises. The preserved September normalization repair keeps normalized transport z=N b distinct from the coupling rate. The current repository base is `d833aae`; its newest critical-bifurcation capture concerns a separate candidate gauge-action lane and supplies no load kinetics here.

The finite input is the same 600-cell boundary with chain dimension 2640. `finite_model.py` is the preserved current constructor helper, not code executed from a historical uploaded archive. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not used.

New assumptions are declared before calculation:

1. A signed normalized transport coordinate z_i at each vertex-star port.
2. Positive quadratic-load stock m_i and exported-load receipt w_i, in units declared compatible with the carrier's normalized quadratic storage. These are not yet particle counts, joules or entropy.
3. Positive finite capacities C_i, transport damping d_i, export rates r_i and contact rates gamma_i.
4. A source-complete candidate contact shape F, an availability contract, and a finite response-latency budget Delta.
5. A supplied packet state and write-edge address. Neither the packet source nor the selected fibration is derived here.

## 2. Balanced local contacts

Let A be the restored skew chain generator and

\[
P=\operatorname{diag}(0,P_{\rm cyc},I,I),
\qquad P_{\rm cyc}=I-B_1^T(B_1B_1^T)^+B_1.
\]

The protected space W=ran P has dimension 2401; its complement U has dimension 239. Nilpotence gives PA=AP. For port i at vertex i, take

\[
f_i=\beta_i I_0e_i+\alpha_i I_1B_1^Te_i,
\qquad \beta_i>0,\quad\alpha_i\in\mathbb R,
\qquad F=[f_1\cdots f_{120}].
\]

Each edge output is a full signed star. PF=0 exactly. The preceding local theorem says this is the general safe column confined to that vertex and its edge star. Multiplying a whole column by one state-dependent scalar preserves the property; independent edge masking generally does not.

For an explicit permission contract, suppose all twelve required edge contacts have binary availability a_ie. A binary whole-star permission eta_i must satisfy eta_i<=a_ie for every contact. The unique maximal permission is

\[
\eta_i=\min_e a_{ie}=\prod_e a_{ie}.
\]

This derives the all-or-none permission from the fixed-star requirement. It does not identify those contact flags with an arbitrary historical gate register. A type-correct map from Q156 closure/integrity data to these physical contacts remains a source obligation. A vertex-only fallback is a different permitted architecture and would require its own control contract.

## 3. Positive source/sink mechanism with finite buffers

Define the actual local buffer load

\[
\boxed{b_i=m_i+\tfrac12z_i^2.}
\]

It includes both accumulated load and energy still in transit. Gating only m_i would omit the second contribution and would not establish a finite-capacity invariant.

Declare

\[
g_i(b_i)=\eta_i\gamma_i(1-b_i/C_i)_+,
\qquad G=\operatorname{diag}(g_i),
\]

and the equations

\[
\boxed{\begin{aligned}
c'&=A_hc+FGz,\\
z'&=-GF^Tc-Dz,\\
m_i'&=d_i z_i^2-r_i m_i,\\
w_i'&=r_i m_i,
\end{aligned}}
\qquad D=\operatorname{diag}(d_i).
\]

Here A_h is either the skew cut writer A-E_e or restored A. Damping of a signed transport mode supplies the positive source

\[
\boxed{s_i^+=d_i z_i^2,\qquad s_i^-=r_i m_i.}
\]

These are predictive functions of the present declared state, not a source inferred afterward as a continuity residual. The choice of transport damping and export kinetics is constitutive. The model can be read as normalized storage transfer from transport into a load register, followed by export into w_i. A microscopic reaction or thermal apparatus implementing that transfer has not been derived.

This construction does not contradict the positive-occupancy obstruction: z remains signed. It also does not implement the earlier two-positive-register encoding of z. Instead it proposes that burden is a positive load generated by transport dissipation. Identifying that load with a native UD rho or a physical population requires an additional bridge.

### Positivity and capacity theorem

For m_i,w_i>=0 and b_i<=C_i initially, these inequalities remain invariant. At m_i=0, m_i'=d_i z_i^2>=0. Export is nonnegative. With x_i=f_i^Tc,

\[
\boxed{b_i'=-g_i z_i x_i-r_i m_i.}
\]

At b_i=C_i the contact closes, g_i=0, and b_i'=-r_i m_i<=0. Thus the capacity boundary points inward or tangentially. The vector field is locally Lipschitz; the positive-part continuation makes its boundary definition explicit. The invariant bounded domain and the storage bound below give global forward solutions between controller events.

## 4. Complete normalized storage receipt and finite export reserve

The reciprocal cross terms cancel even though G depends on the state:

\[
\left[\tfrac12\|c\|^2+\tfrac12\|z\|^2\right]'
=-\sum_i d_i z_i^2.
\]

Adding the positive stocks gives

\[
\boxed{\mathcal E=
\tfrac12\|c\|^2+\tfrac12\|z\|^2+
\sum_i(m_i+w_i),\qquad\mathcal E'=0.}
\]

This is the full normalized storage ledger of the declared model. It is not a complete physical resource ledger: sensing, actuation, communication, reservoir preparation and replacement still have no physical cost model. State-dependent skew coupling contributes no term to this declared storage derivative; that identity is not evidence that an implementation's control is free.

Let the collector have total available capacity B, with W_exp=sum w_i. A sufficient admission condition is

\[
\boxed{B-W_{\rm exp}\ge
\tfrac12\|c\|^2+\tfrac12\|z\|^2+\sum_i m_i.}
\]

It reserves room for every remaining normalized storage unit, including the carrier. Conservation then guarantees W_exp<=B under any subsequent skew writer/restoration schedule. This is conservative when protected carrier energy remains retained.

For a new additive packet delta c, admission must charge the actual increase in carrier energy, including c^T delta c; the packet's isolated energy alone can undercount it. A full replacement or orthogonal injection has its own exact receipt. Clearing m does not replenish the collector. Repeated operation needs explicitly renewed reservoir capacity; an exhausted collector yields HOLD, not READY.

## 5. Protection and restoration theorem

During restored operation,

\[
\boxed{(Pc)'=A(Pc).}
\]

Thus the protected component rotates orthogonally and its norm is constant. No tuning of g_i, d_i or r_i is required for this protection; PF=0 is the operative condition. During a cut, P need not commute with A-E_e, and a separate write can populate W.

Assume restored operation continues, eta_i=1 for every port, gamma_i,d_i,r_i>0, and beta_i>0. Put u=(I-P)c and

\[
\mathcal R=\tfrac12\|u\|^2+\tfrac12\|z\|^2+\sum_i m_i.
\]

Then

\[
\boxed{\mathcal R'=-\sum_i r_i m_i.}
\]

To identify the invariant zero-derivative set, m=0 is necessary. Its continued invariance requires m_i'=d_i z_i^2=0, so z=0. Then b=0, G=diag(gamma_i)>0, and z'=0 requires F^Tc=0 throughout the restored A orbit.

There is no undamped orbit in U with that property. Indeed, for a complex A eigenvector with eigenvalue i omega, the vertex equation is -B1 c1=i omega c0. Hence

\[
(F^Tc)_i=(\beta_i-i\alpha_i\omega)(c_0)_i.
\]

Its coefficient is nonzero for every real omega because beta_i>0. Thus c0=0. In U the remaining edge component is an exact gradient; B1 c1=0 then forces c1=0. This includes the zero-frequency case. Finite spectral decomposition of the skew A gives the same conclusion for entire unobserved orbits.

Compactness and this invariant-set argument imply

\[
\boxed{u(s)\to0,\quad z(s)\to0,\quad m(s)\to0.}
\]

The protected rotation may continue; the theorem does not assert convergence of c to a static vector. Every strictly positive readiness tolerance is reached after a finite time. The proof supplies no universal finite deadline and does not establish exact zero in finite time.

The additional export after restoration is predicted exactly:

\[
\boxed{W_{\rm exp}(\infty)-W_{\rm exp}(s_0)=\mathcal R(s_0).}
\]

If required contacts remain unavailable, the protection theorem survives, but restoration can fail through an unobserved U mode. A partial-contact implementation must prove observability of its active port set or remain HOLD; it cannot borrow the full-availability restoration result.

## 6. Predictive switching from state and reserved headroom

The capacity invariant avoids overflow mathematically. A practical controller also needs finite headroom during sensing, communication and actuation. Let E_c<=E_max be a frozen admission bound. Since z_i^2/2<=C_i,

\[
|z_i f_i^Tc|\le2\|f_i\|\sqrt{C_iE_{\max}}.
\]

Choose any certified rational upper bound

\[
Q_i\ge2\gamma_i\|f_i\|\sqrt{C_iE_{\max}}.
\]

Then b_i'<=Q_i(1-b_i/C_i), even during the skew cut writer. Therefore

\[
\boxed{C_i-b_i(s+\Delta)\ge
(C_i-b_i(s))e^{-Q_i\Delta/C_i}.}
\]

To retain headroom h_i>0 throughout the response delay, a sufficient high guard is

\[
b_i\ge b_i^{\rm hi}:=C_i-h_i e^{Q_i\Delta/C_i}.
\]

The controller requests restoration at the first such guard. The delay budget must cover the whole sensing/coordination/actuation path. At actuation, every buffer retains at least its declared h_i, provided it was below its guard before the response interval.

For 0<=x_i=Q_i Delta/C_i<1, the earlier rational guard

\[
\boxed{b_i^{\rm hi}=C_i-\frac{h_i}{1-x_i}}
\]

is sufficient because exp(-x_i)>=1-x_i. This supplies an exact fraction-based control rule without fitting a switching time.

A sampled implementation with bounded stock error e_i can trigger at measured b_hat_i>=b_hi_i-e_i. Every preceding non-triggering sample then certifies true b_i<b_hi_i. If polling plus actuation latency is at most Delta, the same headroom bound applies on each interval. This is a safety guarantee; polling need not reproduce the ideal first-touch event time. Noise bounds, cadence and their costs remain required inputs.

Choose a separate low guard 0<b_lo_i<b_hi_i and a readiness tolerance epsilon_R>0. The candidate hybrid rule is:

| Mode | State-based condition | Action |
|---|---|---|
| HOLD / admission | A supplied pending packet has declared energy/address; capacities, contact permissions and export reserve pass | Admit one write; charge its energy receipt |
| WRITE | First local high guard, combined by an OR with latency <=Delta, or expiry of a declared finite write budget T_write | Restore A within the reserved delay; keep each recovery port balanced; label a budget-only stop TIMEOUT / no certified load event |
| RECOVER | All b_i<=b_lo_i, R<=epsilon_R, contact permissions and next-packet reserve pass | Declare READY and consume the pending request |
| Any mode | Invalid permission, failed sensing bound or insufficient reservoir reserve | HOLD and account for the unresolved condition |

The state remains continuous at switching; no reset deletes load or waste. A physically instantaneous change of the operator is not claimed; Delta is an actuator contract. Exact reciprocal balance also requires matched forward/reverse contacts throughout actuation. Unmatched contacts need a new error receipt.

The rule is predictive and causal under its premises. It is not a uniquely derived native UD law. Capacities, headroom, delay, write budget and readiness tolerance are declared design quantities. A write is not guaranteed to hit a high guard for every input: a null or sufficiently weak drive may never do so. A controller timer, started on admission, therefore requests restoration no later than T_write; a timeout is reported separately from a load event and never certifies a successful record. This makes stopping total for an admitted request without claiming a native clock law. The timer, its reset and its implementation costs are declared controller resources. Together with the restoration theorem, each request reaches a positive readiness tolerance if the stated availability and reserve conditions persist.

Initial admission requires b<=b_lo. Since b_i'<=Q_i, a high-guard event then has a positive minimum dwell min_i[(b_hi_i-b_lo_i)/Q_i]. The positive timeout also has positive dwell. Thus the autonomous handling of one request has no instantaneous repeating write cycle; external packet arrivals still need their own admission contract. The benchmark below demonstrates one actual high-guard event and separately checks a null-packet timeout.

## 7. Frozen 600-cell benchmark

The replay freezes beta=2/3, alpha=1/12, gamma=d=1, r=1/5 and C_i=1/50. All stars are available. Start with unit amplitude at the declared vertex and blank z,m,w; use the previously supplied cut edge. These are controls and charged input choices, not UD constants.

On a degree-12 star, ||f_i||^2=19/36 and E_max=1/2. The rational Q_i=3/20 is a valid upper bound. With Delta=1/100 and h_i=1/200,

\[
x_i=3/40,\qquad
\boxed{b_i^{\rm hi}=27/1850},\qquad
b_i^{\rm lo}=1/200.
\]

The readiness criterion is R<=10^-7 and all low guards satisfied. The finite export reservoir has normalized capacity 2, and the declared maximum write duration is 1. The load guard is reached before that deadline. A separate zero-packet run reaches the deadline with zero load and no false guard event.

| Quantity | Numerical result |
|---|---:|
| High-guard time | 0.46354495 |
| Actual restoration after full permitted delay | 0.47354495 |
| Maximum buffer after delay | 0.014687514 |
| Required ceiling after delay, C-h | 3/200 = 0.015 |
| Protected squared amplitude after write | 0.070258198 |
| Retained protected chain energy | 0.035129099 |
| Ready time at the declared tolerance | 445.57133 |
| Export at readiness | 0.464870801 |
| Remaining recoverable resource | 10^-7 |
| Maximum observed resource-balance error | 5.45 x 10^-11 |

These are dimensionless numerical diagnostics. Retaining a nonzero protected pattern does not establish a decoded information rate or a physical memory record. In particular, the old small-cut exact score-gap certificate is not transferred to this longer, state-coupled write. The write address was supplied, not discovered.

The package contains 21 exact constructor checks and eleven numerical corroborations. The exact algebraic examples corroborate the general identities; universal invariance and restoration are proved above. The numerical path includes the allowed delay, local capacity checks, finite-reservoir accounting, the additional-export prediction and null-packet timeout. A first RK45 run failed the frozen protected-stock drift check; a higher-order DOP853 recovery integration with tighter tolerances passed without loosening that criterion. No physical experiment or independent review is represented by these computations.

## 8. Manuscript consequence and remaining closure order

The manuscript can now present a complete conditional example: geometric isolation protects a retained component; signed transport deposits a positive load; finite capacity attenuates contact; a headroom guard stops writing; a true export sink clears the working state; and the export receipt determines when finite reservoir capacity must be renewed.

The remaining tasks are in logical order: identify the native meaning and normalization of m and C; derive the contact shape/rates and the typed availability interface; source the packet/address and replace or justify the declared timeout clock; implement and account for sensing, matched switching and communication; derive reservoir preparation/renewal and physical costs; then establish retained distinguishability for this changed write dynamics. Physical entropy or an area law cannot be inferred from this normalized storage example.
