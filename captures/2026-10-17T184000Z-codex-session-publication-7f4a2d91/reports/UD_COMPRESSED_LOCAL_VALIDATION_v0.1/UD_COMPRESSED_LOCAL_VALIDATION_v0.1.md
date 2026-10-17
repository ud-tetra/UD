# UD compressed local validation v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; development — no registry entry.**
The declared local fault family admits **260 unit-norm coded preparations**.
Two epochs at three short sample times, with a blank at each epoch, use
**295974 scalar outputs**, over 6900 times fewer than the preceding full-basis
benchmark. The code is injective on all **16175 declared readout coefficients**.
It also supplies a uniform rejection/pass bound for a sparse class of
same-grade metric defects. Physical promotion = 0. Constructor verification
passed; independent review pending. No physical data were used.

The reduction relies on a restricted family and short-time structural bounds.
It does not reproduce unrestricted complete-basis coverage with fewer data.
The number of distinct nonblank preparations falls from2640 to260; most of
the output reduction comes from replacing4096 time samples with three.

## 1. Freeze the local alternative family before data

Retain the 2640-coordinate real chain carrier, 189-coordinate readout R,
frozen grade-metric calibration, fitted Khat, gains and clock reference. All
states, matrices and norms are in those fixed coordinates. The choices below
are **CANDIDATE modeling restrictions**, not a native source law or a claim
that an apparatus already satisfies them.

Let the undirected Hasse graph have one node per chain coordinate and an edge
where the unweighted incidence generator A has a nonzero entry. For each
observed coordinate r, define partners P_r as same-grade coordinates at Hasse
distance two. Add the explicitly named pair (0,4) at observed endpoint4,
because the preceding fault campaign demonstrated this excluded metric
alternative. That pair is an additional declared hypothesis, not implied by
the distance-two rule. Deduplication gives **2574 possible unordered pairs**.

The metric family is

\[
H=H_0+S,
\]

where H0 is scalar on each chain grade, S is symmetric with zero diagonal,
and every nonzero pair lies in the declared list. Active pairs must form a
**matching**: no coordinate belongs to two active pairs. Each pair has at least
one observed endpoint. Assume ||S||<=1/16. Then S has independent 2 by 2
blocks and ||S|| equals the largest absolute pair amplitude. Inverse metric
fill-in stays within each pair. Nonmatching defects can propagate through an
inverse metric and are expressly outside this theorem.

The plant is K=H^(-1)A_w, with constant clock scale included in its effective
reference-time generator. The background H0, rates w and clock are restricted
to the declared calibration uncertainty about the frozen fit. This restriction
is part of the alternative class: it must not be inferred as universally
valid from a calibration whose own model may be false. The amplitude bound,
background bounds and positivity imply H is SPD and ||K||<5 throughout this
family. H is a chain-space metric; no spacetime-metric identity is asserted.

For an observed row r, define

\[
J^K_r=\bigcup_{u\in P_r\cup\{r\}}\operatorname{supp}(A[u,:]),
\qquad J^C_r=J^K_r\cup P_r\cup\{r\}.
\]

Then R(K-Khat) is supported on JKr in row r. The readout family assumes the
gain-normalized error C-R is supported on JCr in each row. It is row sparse
and local: the largest readout stencil has137 entries out of2640, with16175
entries across all189 rows. Observed generator-row stencils total12815 entries,
maximum123 per row. Values inside an allowed stencil are not assumed to have
one common sign or one common amplitude.

**Excluded:** cross-grade metric terms, arbitrary diagonal heterogeneity,
interacting/nonmatching metric pairs, readout outside the listed stencils,
unrestricted nonlinearity and unbounded temporal drift. Passing this protocol
does not establish that these excluded alternatives are absent.

## 2. Deterministic preparation code and exact coverage

Connect two input coordinates in an interference graph when they coexist in
some JCr. A proper coloring assigns distinct colors to every allowed input
of each observed row. Enforce separate color ranges for even and odd chain
degree. Deterministic DSATUR with fully specified tie-breaking produces260
colors on1502 relevant coordinates;1138 coordinates are unprepared because
they occur in no allowed stencil. Full assignments are in PROBE_DESIGN.json.

For color c with nc coordinates, set qc=ceil(sqrt(nc)) and prepare

\[
p_c=\frac1{q_c}\sum_{j:\,\mathrm{color}(j)=c}e_j.
\]

All amplitudes are rational and ||pc||=sqrt(nc)/qc<=1. A class has at most20
coordinates and qc<=5. Realizing every specified address and coefficient with
the required accuracy is an external control requirement. Unit norm does not
establish apparatus feasibility. Colors are a computational design choice,
not a physical symmetry or a source-derived constant.

For a matrix E supported on the declared readout stencils, the coded static
response EP has, in row r and color c, at most one allowed contribution:

\[
(EP)_{r,c}=E_{r,j}/q_c\quad\text{when }j\in J^C_r
\text{ has color }c.
\]

Thus multiplying by qc recovers each allowed coefficient exactly. The
restricted readout map has rank16175. In Frobenius coefficient/data norms,
its minimum singular value is at least1/5, maximum at most1, and condition
number at most5. This is not a statement about the full unrestricted readout
map, which remains underdetermined.

The exact code identities include

\[
\sum_cq_c^2=2073,\qquad
\max_r\sum_{j\in J^K_r}q_{\mathrm{color}(j)}^2=991.
\]

These control the error amplification rather than an unsupported claim of
noise-free compression.

## 3. Static local readout test

Use the preceding total prepared-response error requirement
ecol=1/10^13 in Euclidean output norm, now for every coded unit-norm
preparation at each sample time. It covers normalization, preparation, timing,
noise and blank correction. It is not an empirical instrument performance
claim. Freeze gains and all thresholds before collecting held-out data.

At t=0 subtract the known coded prediction R P and decode only JCr entries.
If each response-column error is <=ecol, the decoded Frobenius error is

\[
\tau_C=\sqrt{2073}\,e_{\rm col}.
\]

Under the null family the remaining diagonal gain error has operator norm
<=gamma= [33/(16 times10^13)]/(15/16), hence Frobenius norm <=sqrt(189)gamma.
Reject the decoded readout residual when

\[
\|\widehat{C-R}\|_F>T_C:=\sqrt{189}\,\gamma+\tau_C.
\]

The enclosed threshold is approximately7.577520934 times10^(-12). Passing
implies, within the local support assumption,

\[
\|C-R\|\le\|C-R\|_F\le\sqrt{189}\gamma+2\tau_C
<13/10^{12}.
\]

There are32965 static row/color cells with no permitted input. Their expected
residual is zero even in the local alternative family. Test their measured
Frobenius norm against sqrt(260)ecol. This supplies an additional locality
syndrome; passing it cannot exclude out-of-family cancellation into allowed
cells or the nullspace below.

## 4. Short-time generator test with parity cancellation

Use reference times 0,h,2h with **h=1/1024**. Both H0 and the allowed S preserve
chain grade, while A_w flips its parity. Every code preparation has one
parity. For an observed row of the opposite parity, all even Taylor powers
vanish in R exp(tK)pc.

With measured coded matrices Y(t), form

\[
L_h(Y)=\frac{8Y(h)-Y(2h)-7Y(0)}{6h}.
\]

The linear term is CKP and the cubic term of the R response cancels. On
opposite-parity rows the remaining R response has uniform bias bounded by

\[
B_h=\frac{\sinh(2z)-8\sinh z+6z}{6h},\qquad z=5h.
\]

This follows by summing the absolute odd Taylor coefficients starting at
degree5, using ||K||<=5 and ||pc||<=1. Numerically Bh is approximately
9.473930034 times10^(-11). The E=C-R contribution need not preserve parity;
bound its full response by

\[
\|E L_h(e^{tK})\|\le\|E\|B_F,
\qquad B_F=\frac53\,5e^{10h}.
\]

This uses 8(exp(hK)-I)-(exp(2hK)-I) and a norm bound on its time integrals.
The instrument-error contribution is <=8ecol/(3h). No statistical averaging
or cancellation of measurement noise is assumed.

Subtract R Khat P and decode the generator-row stencils JKr. Let Dhat be the
decoded observed-generator discrepancy, and use the maximum row Euclidean
norm, max_r||Dhat[r,:]||2. Its error relative to R(K-Khat) is bounded by

\[
\tau_K=\sqrt{991}\left[B_h+E_*B_F+\frac{8e_{\rm col}}{3h}\right],
\quad E_*:=\sqrt{189}\gamma+2\tau_C.
\]

The static readout test must pass first. Using a row norm here avoids an
unnecessary sqrt(189) factor on the background generator uncertainty.

Let epsilon0 be the calibrated effective background-generator uncertainty:

\[
\epsilon_0=\frac{4\Delta_w}{1-\eta}
 +\frac{4(1+b)\Delta_H}{(1-\eta)^2}
 +\frac{4(1+\eta)}{1-\eta}\,\epsilon_{\rm clock},
\]

where eta=3/10^9, b=2/10^9, DeltaH=5/10^10, Deltaw=4/10^10 and
epsilon_clock=(1/10^12)/(15/16), as in the parent contract. Reject when

\[
\max_r\|\widehat D[r,:]\|_2>T_D:=\epsilon_0+\tau_K.
\]

The enclosed TD is approximately1.839634453 times10^(-8). All thresholds are
defined by the exact formulas and interval enclosures, not these rounded
displays. The background uncertainty is a declared restriction on the
alternative class, not an unconditional inference from a possibly misspecified
calibration.

## 5. Uniform metric-fault visibility and pass bound

For every one of2574 permitted pairs (u,v), exact full-carrier calculation
gives the minimum eigenvalue of the two-row Gram matrix
[A[u,:];A[v,:]][A[u,:];A[v,:]]^T at least3. Same-grade rows have common column
weight scalings under A_w, so the minimum singular value of their weighted
row pair is at least(1-eta)sqrt(3).

For a metric block [[a,s],[s,a]], with an observed endpoint v, its row change
is

\[
\Delta K[v,:]=\frac{s^2}{a(a^2-s^2)}A_w[v,:]
             -\frac{s}{a^2-s^2}A_w[u,:].
\]

The Gram bound prevents cancellation between these two row vectors. Including
the clock factor gives the uniform lower bound

\[
\max_r\|(R\Delta K_{\rm metric})[r,:]\|_2
\ge c_S\|S\|,\qquad
c_S=\sqrt3\frac{(1-\epsilon_{\rm clock})(1-\eta)}{(1+\eta)^2}.
\]

The matching restriction makes each observed row belong to at most one block,
and ||S|| equals the maximum block amplitude. At least one endpoint per active
pair is observed, so no allowed block is hidden from this row bound.

If the static and dynamic tests pass,

\[
\boxed{\|S\|\le\frac{2\epsilon_0+2\tau_K}{c_S}
<23/10^9.}
\]

The enclosed expression is approximately2.124226912 times10^(-8). Thus an
allowed metric defect larger than23/10^9 cannot pass both tests under the
instrument/background contracts. The bound allows bounded readout error
and adversarial instrument errors to mask some signal. It is not a statement
that all defects below the bound are invisible.

## 6. Concrete fault and blind-direction checks

**Local cross-talk:** the preceding fault epsilon output_row4 input_column0^T
is in the new readout stencil because pair(0,4) was declared. For
epsilon=1/10^9 the coded data contain epsilon/qcolor(0), and exact decoding
recovers epsilon. It exceeds the certified static rejection margin.

**Local metric:** H=I+rho(e0e4^T+e4e0^T), rho=1/10^6, is one allowed block.
Use the color containing edge coordinate120. No other allowed input in row4
has that color. Exact integer incidence powers and rational Taylor sums at
h and2h give a decoded coefficient magnitude >9/10^7; its noise allowance
still leaves it above TD. This is a synthetic mathematical fault check, not
an apparatus measurement. The uniform Gram proof covers all permitted
matching patterns; one injected example alone would not do so.

**Unrestricted static readout:** the preparation matrix has rank260, so its
nullity is exactly2640-260=**2380 per readout row**. The supplied code constructs
a two-entry alias: two inputs of one color contribute equal and opposite
coefficients to a readout row, giving exactly zero coded static response.
At most one of those inputs lies in that row's allowed stencil, so the alias
is outside the declared local family. Even a two-sparse unrestricted fault
can therefore escape the static test. Sparsity alone is not the coverage rule.

With all three sample times there are at most780 input-response directions
under a fixed nominal plant. At least**1860 unrestricted readout directions
per row** remain possible in their annihilator. Repeating the same schedule
at a stable second epoch adds no new nominal directions. This is a lower bound
on full three-time blindness, not a computed exact rank. It is distinct from
the exact static nullity2380.

The general harmonic metric shadow and rational-grid aliasing obstructions
remain outside this restricted family. Nonmatching or cross-grade metric
faults can violate the inverse-support/parity arguments. They must not be
silently assigned the same pass bound.

## 7. Conditional full-state observation after a compressed pass

The metric pass ceiling23/10^9 is wider than the original grade-only
3/10^9 metric budget. The added fault allowance therefore needs new finite
observation bounds; a compressed pass does not inherit the old condition
numbers unchanged.

Within the selected stable family, use S*=23/10^9 and E*=13/10^12. The total
effective generator distance from the frozen fit is bounded by

\[
\epsilon_{\rm tot}=\epsilon_0+
\frac{(1+\epsilon_{\rm clock})4(1+\eta)S_*}
 {(1-\eta)(1-\eta-S_*)}.
\]

Let GammaA=sqrt[(1+eta+S*)/(1-eta-S*)] and
GammaF=sqrt[(1+b)/(1-b)]. For a later M-snapshot history at tj=j/2 and an
additional per-sample timing jitter ceiling tauA=1/10^6, the finite-map
distance from the frozen fit is at most

\[
\beta_M=E_*\Gamma_A+
 \Gamma_A\Gamma_F\epsilon_{\rm tot}T_{\rm rms}
 +(1+E_*)\Gamma_A\,5\tau_A,
\quad T_{\rm rms}^2=(M-1)(2M-1)/24.
\]

The parent frozen-fit bound is sfit=(97/100)sM. Singular-value perturbation
then certifies the following **if both compressed tests pass and the family,
background, stability and later jitter assumptions hold**:

| Later snapshots | Actual history rank | Kernel | Condition bound |
|---:|---:|---:|---:|
| 2048 | 2640 | 0 | <783 |
| 4096 | 2640 | 0 | <391 |
| 8192 | 2640 | 0 | <328 |

The inequalities use sfit-betaM>0 and sigma_max<=GammaF+betaM. They are
theoretical consequences of the restricted pass contract, not measured
singular values. A compressed pass outside this family does not justify them.
The response-error contract for short probes does not automatically certify
noise, preparation or stability during a later long acquisition.

## 8. Schedule, drift and practical gate

At each of two epochs prepare all260 code vectors and one blank, read all189
outputs at0,1/1024,1/512, and use the same frozen model. Cost is
2 times261 times3 times189=295974 scalar outputs. The exact reduction factor
against the prior2043740160-value benchmark is recorded in the certificate.
No full-basis dataset or physical measurements were generated here.

Paired early/late response differences have null instrument threshold2ecol;
observable coded-response drift above4ecol is guaranteed to reject. This
checks sampled epochs, not arbitrary intervening drift. An external regularity
bound and monitored scale references are still needed for continuous stability
claims. Do not refit on these held-out data. Verified interval statistics
must yield pass, reject or inconclusive when crossing a threshold.

**Remaining gate:** the stencil and matching assumptions must be justified or
challenged with new held-out tests. Added coverage can target interacting
defects, cross-grade terms and out-of-stencil readout, but cannot be claimed
from the present result. Preparation complexity has shifted to260 known
patterns over1502 addresses with up to20 simultaneous amplitudes. A concrete
apparatus, independent error receipts and non-constructor review remain open.

## 9. Reproduction and governance

Run `python certify_compressed.py`; it calls build_design.py. The code verifies
all stencils and color collisions, unit-norm preparation bounds, all2574 row
Gram bounds, exact restricted coefficient injection, interval error/pass/
observer bounds, a local cross-talk fault, an actual-carrier metric fault,
and an exact out-of-family static alias. Fresh-directory replay must reproduce
the design and certificate bytes. Constructor checks are not independent
review and are not physical execution.

Relevant attached ledger entries O03, Q139, Q165 and Q169 remain scoped. The
CRL-2 amendment is self-labeled a proposal; this work stays in the development
distinction and makes no registry promotion. No private attachment is copied
into the deliverable; the unavailable Genesis image was not used. Prior
captures and source versions remain immutable. Provenance and local/public
publication status are recorded separately.
