# THM-534 v2.18: conditional feed/output completion and its native coupling gap

Development — no registry entry. Exact kinematic completion with two explicitly added abstract ports. The port and restoration operators are not derived native incidence couplings. Constructor checked; independent review pending. Physical promotion 0.

## 1. Purpose and retained native stage

The v2.17 tetrahedral donor channel transfers existing edge support into an empty core under a supplied nonuniform face mask. It does not retain an output while restoring its donor. This note derives the necessary support balance, constructs one fully accounted conditional port cycle, and audits its nonnative couplings. The construction settles a feasibility question under an extended metric; it is not a native autonomous renewal law.

Retain the original 15-coordinate real tetrahedral worker, unit metric, signed incidences and whole-face permission mask \(h\). Write its native generator \(A_h\) and supplied unit model-step map

\[
C_h=(I-A_h/2)^{-1}(I+A_h/2).
\tag{1}
\]

For a nonuniform mask, use the prepared native edge cycle

\[
x_0=(0,u_h,0,0),\qquad u_h=B_2\operatorname{diag}(h)B_3.
\]

Let \(y=C_hx_0\), \(c=y_{\rm core}\ne0\), \(p=c^2\), and \(N=\|x_0\|^2=\|y\|^2\). The previous exact formula gives \(c=8k(4-k)/(k^2+4k+32)\) for \(k\) open faces. No particle operator or original metric is changed.

Q169–Q173 and Q177–Q179 govern this native stage and its receipts. Q153/Q156/G05 do not supply the port geometry, event cost, mask controller, reserve renewal or physical action scale used below. The supplied governance amendment remains a proposal.

## 2. Necessary support balance for a restored worker

**Theorem O1 (restoration with retained support output).** Partition a norm-conserving enlarged model into worker \(W\), feed \(F\), output \(O\) and other environment \(E\), with additive nonnegative squared-amplitude support. If worker support and other environmental support are restored, then

\[
\Delta S_O=-\Delta S_F.
\tag{2}
\]

If the feed is also restored and output starts empty, no positive output support can be retained. With a finite feed pool and no replenishment, accumulated output support is at most its initial feed support.

**Proof.** Subtract the initial and final total support identities and impose \(\Delta S_W=\Delta S_E=0\). This gives (2). Nonnegativity of final feed support gives the finite-pool bound. Exact restoration of worker amplitudes is a stronger condition than the support restoration used in the argument. \(\square\)

This is a support balance, not a bound on all information processing or a physical work/entropy theorem. A record can require a separate account even when some support stocks are unchanged.

## 3. Explicit conditional completion with two abstract ports

Add real amplitudes \(r\) and \(o\), called feed and output. They have no assigned native simplex grade. Declare the enlarged product support

\[
S_{\rm ext}=\|x\|^2+r^2+o^2.
\tag{3}
\]

This metric extension is a candidate interface model. Its two new coordinates are not covered automatically by native unique-simplex ownership. The native 15-coordinate metric remains unchanged.

Prepare \((x,r,o)=(x_0,c,0)\), with \(h\), model step and all three phase operators fixed from this known template. No feedback controller or autonomous phase clock is derived.

### Native conversion

Apply (1) to the worker only, giving \((y,c,0)\). Its native coordinate and grade receipts are those of v2.17.

### Candidate output extraction

Apply the proper quarter-turn \((x_{\rm core},o)\mapsto(-o,x_{\rm core})\). This empties the worker core and retains amplitude \(c\) in the output. If \(z\) is \(y\) with its core set to zero, then

\[
(y,c,0)\longmapsto(z,c,c),\qquad \|z\|^2=N-p.
\tag{4}
\]

This extraction contact is an added abstract coupling. It has not been embedded into a native glued complex. Its two-coordinate midpoint support receipt is exactly \(p\) from core to output.

### Candidate worker restoration

In the 16-coordinate worker/feed space, put

\[
v=(z,c),\qquad w=(x_0,0),\qquad
K=wv^{\mathsf T}-vw^{\mathsf T},\qquad d=v^{\mathsf T}w.
\tag{5}
\]

Both vectors have squared norm \(N\). Since \(c\ne0\), they cannot be antipodal, so \(N+d>0\). Define

\[
S=\frac{2K}{N+d},\qquad
R=\operatorname{Cayley}(S)
=I+\frac KN+\frac{K^2}{N(N+d)}.
\tag{6}
\]

**Theorem O2 (matched-template completion).** The fixed operator \(R\) is a real orthogonal plane rotation and \(Rv=w\). The complete three-phase sequence therefore gives

\[
\boxed{(x_0,c,0)\longmapsto(x_0,0,c).}
\tag{7}
\]

The worker is restored exactly, feed support decreases by \(p\), and output support increases by \(p\).

**Proof.** The matrix \(S\) is skew, hence its Cayley map is orthogonal. On the span of \(v,w\), \(Kv=Nw-dv\) and \(K^2v=-(N^2-d^2)v\). Substitution in (6) yields \(Rv=w\). On the orthogonal complement, \(K=0\), so \(R=I\). Formula (6) is the Cayley plane rotation and can also be obtained by direct multiplication with \(I-S/2\). All phases preserve (3); (4) and \(Rv=w\) establish (7). \(\square\)

For rational native preparation and model step, all these vectors and matrices are rational. No square-root feed amplitude is hidden: the prepared feed is the signed native output amplitude \(c\), with support \(c^2\).

The conditional phase map is linear and orthogonal once the template is fixed, so it preserves the extended norm on arbitrary inputs. Its exact restoration property (7) is for the stated matched input. It is not a universal reset of an unknown worker state.

## 4. Explicit accounting and finite-resource tests

The restoration obeys the generic skew-midpoint identity

\[
w-v=S\bar v,\qquad \bar v=(v+w)/2.
\]

For every pair \(i<j\), define \(J^{\rm reset}_{i\to j}=2S_{ji}\bar v_i\bar v_j\). These receipts account for each squared-coordinate change. They are generic added-coupling receipts, not claimed native Hasse-incidence receipts. Summing over the feed boundary gives a feed debit \(p\), and the worker gains \(p\). The output is untouched during restoration.

For the one-open-face preparation \(h=(1,0,0,0)\),

\[
N=3,\qquad c=24/37,\qquad p=576/1369.
\tag{8}
\]

Each exact cycle retains \(576/1369\) support in its fresh output and empties a feed of that same support. After \(m\) cycles with \(m\) freshly prepared feeds and empty outputs, the worker is \(x_0\), total retained output is \(mp\), and all spent feeds are zero. The external resource pool has changed, so this is not a closed catalyst producing new support.

Replacing the feed by \(c+\delta\) while keeping the fixed template rotation gives

\[
\|R(z,c+\delta)-(x_0,0)\|=|\delta|.
\tag{9}
\]

This follows from orthogonality. In particular, omitting the feed makes exact worker restoration impossible: the worker/feed input support is only \(N-p\), while the desired worker has support \(N\). Preparing fresh feeds is an explicit external obligation, not a passive bookkeeping operation.

An empty output slot is also an input condition. Reusing a charged output changes the extraction step's input and does not satisfy (7). Retaining outputs indefinitely requires outgoing capacity or a further specified transfer. No record label, record erasure or reset reservoir is supplied by the two amplitude ports.

## 5. Native coupling audit

**Theorem O3 (this explicit restoration is not a native incidence generator).** The generator \(S\) in (6) generally has worker-coordinate couplings absent from the original all-open tetrahedral Hodge–Dirac incidence graph. The one-open-face example already supplies an exact counterentry:

\[
S_{[01],[023]}=-1/3,
\qquad (B_2)_{[01],[023]}=0.
\tag{10}
\]

**Verification.** In this preparation, \(u_h\) has edge components \((-1,1,0,-1,0,0)\), the native output edges are \((3/37)u_h\), and its face vector is \((-48,-20,20,-20)/37\). Thus \(d=9/37\), \(N+d=120/37\). Substituting in (5)–(6) gives (10). The edge \([01]\) is not contained in face \([023]\). Six such nonincident worker pairs occur in this example; the verifier finds at least six across all 14 matched nonuniform masks. \(\square\)

This is a concrete implementation gap, not a proof that a sequence of native controlled events could never synthesize the same finite map. Such a compilation would require an actual glued complex, admissible whole-face controls, a derived sequence, and all ownership/record receipts. Neither (6) nor a dense orthogonal matrix supplies that compilation. The two abstract ports themselves also lack native incidence geometry.

## 6. What has and has not closed

The construction supplies a consistent conditional answer to a support question: a native donor-conversion stage can be embedded into an ideal extended cycle that restores its worker and retains output, with output paid exactly by fresh feed. It also makes the missing implementation explicit. The new extraction and restoration couplings, product metric, feed preparation, empty output preparation and ordered phase program are candidate inputs.

The face mask is held externally fixed. No native law opens, restores or selects it; no phase clock, fair scheduler, controller-memory reset or physical action cost is included. The port construction is not an autonomous native engine and does not establish a physical source/sink mechanism. Amplitude scaling changes \(p\), and different masks/model steps change it, so (8) is not a universal event or action unit.

The strongest next target is a native compilation or obstruction: realize the feed and output through actual unique simplices and cofaces, preserve Q173 whole-face contacts and Q177–Q179 ownership, and derive a local consistent gate/phase rule. The nonincident reset entry (10), the zero-feed failure and the finite-feed balance are required countercontrols. Independent review and any physical action/clock/particle bridge remain open.

## 7. Reproducibility

The fresh `verify_feed_output.py` uses exact standard-library `Fraction` arithmetic. It constructs the full native worker stage; checks all 14 matched nonuniform masks; 56 finite matched-cycle-length controls; 336 signed prepared-cycle covariance controls; 42 wrong-feed/error controls; 56 global norm controls on generic inputs; every restoration coordinate's skew-midpoint receipts; and the nonnative coupling audit. No archived script is executed. These are constructor controls, not independent replication, physical feed preparation, native compilation or empirical validation.
