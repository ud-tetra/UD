# THM-534 v2.24 — Finite controlled writer operator certificates

**28 October 2026.** Certified approximate operators from positive rational native Cayley steps. Clock generation, adaptive writing and autonomous programme realization are separate source questions.

## Abstract

The v2.23 pure record-plane writer is outside the instantaneous span of native whole-face generators. We supply two finite compositions that approximate this writer and its inverse on the complete 14-dimensional active sector. Each composition has 160 positive rational Cayley steps. Exact rational residual bounds certify active-sector operator errors below $4.465\times10^{-10}$ and $2.461\times10^{-10}$, respectively. Their composition is within $6.926\times10^{-10}$ of identity on that sector.

The construction uses supplied masks and step parameters. It does not generate the event-time signal to be written. Both programmes temporarily move more than $99/100$ of a unit record input's stock outside the protected plane, and both rotate the uncontrolled gradient sector. These are full two-cell controlled operations, not continuously isolated five-coordinate primitives.

## 1. Fixed carrier and target

Use the original oriented cells $[0123]$, $-[0124]$, unique real simplex amplitudes and unit metric on

$$
\mathcal H=C_0\oplus C_1\oplus C_2\oplus C_3,\qquad
\dim\mathcal H=5+9+7+2=23.
$$

For binary face mask $h$, with $H=\operatorname{diag}(h)$, retain all native lower incidence contacts:

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix},
\qquad
C_h(t)=\left(I-\frac t2A_h\right)^{-1}
       \left(I+\frac t2A_h\right).
$$

The face order is $012,013,014,023,024,123,124$. One shared-face gate always controls both of its core contacts. The programmes use only $t>0$, rational and no larger than $4$. A finite Cayley map is a supplied implicit update on this full carrier; it is not identified with $e^{tA_h}$, a physical duration, or a bounded-radius implementation.

Let

$$
q=e_{\mathrm{core}\,1},\qquad
p=\frac12 B_3e_{\mathrm{core}\,1}\quad\text{embedded in the face grade}.
$$

They are orthonormal. Define $P_{\rm rec}=pp^{\mathsf T}+qq^{\mathsf T}$ and

$$
J=pq^{\mathsf T}-qp^{\mathsf T}.
$$

The exact target family is

$$
R(u)=I+\left(\frac{1-u^2}{1+u^2}-1\right)P_{\rm rec}
       +\frac{2u}{1+u^2}J.
$$

It rotates the record plane and fixes its orthogonal complement. The two targets here are $u=1/2$ and $u=-1/2$, so their cosine is $3/5$ and sine is respectively $4/5$ or $-4/5$. In particular,

$$
R(1/2)q=\frac35q+\frac45p,\qquad
R(-1/2)=R(1/2)^{-1}.
$$

These are fixed constructed benchmarks. They do not establish an arbitrary-angle writer or an empirical target-blind registration.

## 2. Certified sector and exact basis

The active sector is

$$
\mathcal A=\ker B_1\big|_{C_1}\oplus C_2\oplus C_3,
\qquad \dim\mathcal A=5+7+2=14.
$$

Every $A_h$ preserves it: $B_1B_2=0$ ensures that an edge cycle stays in the cycle sector, and no vertex component is generated. Every Cayley factor therefore preserves it as well.

For an exact basis matrix $V$, take the first five independent columns of $B_2$, in face order, as edge-cycle vectors. Append the seven unit face vectors and two unit core vectors. Thus $V$ is $23\times14$, and its Gram matrix $G=V^{\mathsf T}V$ is invertible. The verifier checks

$$
\|G^{-1}\|_\infty=\frac75.
$$

For $x=Va\in\mathcal A$,

$$
\|a\|_2
\le\sqrt{\|G^{-1}\|_2}\|x\|_2
\le\sqrt{\frac75}\|x\|_2
\le\frac75\|x\|_2.
$$

All certification is performed in the original full metric. The rational basis is not declared orthonormal and no metric is replaced. The exact orthogonal projector
$P_{\mathcal A}=VG^{-1}V^{\mathsf T}$ is checked for idempotence and commutation with all 128 native masked generators.

## 3. From constructed proposals to rigorous operator bounds

For a saved programme, let

$$
T_n=C_{h_n}(t_n)\cdots C_{h_1}(t_1),\qquad T_0=I.
$$

The verifier constructs rational proposal matrices $Q_n\in\mathbb Q^{23\times14}$, with $Q_0=V$. Deterministic integer elimination proposes entries at precision $10^{-30}$, which are rounded onto a grid of denominator $10^{15}$. Its accuracy is not assumed; the residual inequalities establish the bounds.

Define exact rational residual matrices

$$
D_n=\left(I-\frac{t_n}2A_{h_n}\right)Q_n
    -\left(I+\frac{t_n}2A_{h_n}\right)Q_{n-1},
\qquad
E_n=\sum_{j=1}^n\sum_{i,k}|(D_j)_{ik}|.
$$

**Theorem 1 (validated operator residual bound).** For every proposal sequence,

$$
\|T_nV-Q_n\|_F\le E_n.
$$

If $L=\sum_{i,k}|(Q_N-RV)_{ik}|$, then

$$
\boxed{\|(T_N-R)|_{\mathcal A}\|_2
\le\frac75(E_N+L).}
$$

*Proof.* For a real skew matrix $A$,

$$
\left\|\left(I-\frac t2 A\right)v\right\|_2^2
=\|v\|_2^2+\frac{t^2}4\|Av\|_2^2.
$$

Thus the inverse denominator exists with norm at most $1$, and its Cayley transform is orthogonal. The proposal equation is

$$
Q_n=C_{h_n}(t_n)Q_{n-1}
    +\left(I-\frac{t_n}2A_{h_n}\right)^{-1}D_n.
$$

Left orthogonal multiplication preserves Frobenius norm. Induction, the triangle inequality and the entrywise bound $\|D_n\|_F\le\sum|(D_n)_{ik}|$ give the first result. Next,
$\|(T_N-R)V\|_F\le E_N+L$. Apply this matrix to $a$, use the basis bound above, and take the supremum over unit $x=Va$. $\square$

Every residual, threshold comparison, basis metric and final bound is evaluated with exact rational arithmetic. The proposal arithmetic uses exact integer operations and an explicit rounding rule. Inaccurate proposals would fail the residual inequalities; there is no trusted solver tolerance or floating-point solve in verification. No intermediate checkpoint is reset to a target.

## 4. Two finite controlled writers

WRITER_SCHEDULES.json gives both complete ordered programmes. Numerical construction used fixed mask seeds and optimized positive step parameters. The parameters were then rationalized and accepted only through Theorem 1.

**Theorem 2 (certified fixed-angle writers).** The saved programmes $T_+$, $T_-$ each use 160 permitted positive rational Cayley steps and obey

$$
\|(T_+-R(1/2))|_{\mathcal A}\|_2\le\varepsilon_+,
\qquad
\|(T_--R(-1/2))|_{\mathcal A}\|_2\le\varepsilon_-,
$$

with the following exact certificate bounds shown as upward-rounded decimal displays:

| Programme | Certified operator-error upper display | Sum of Cayley parameters, approximate display |
|---|---:|---:|
| Write $u=1/2$ | $4.465\times10^{-10}$ | $136.213206$ |
| Unwrite $u=-1/2$ | $2.461\times10^{-10}$ | $130.891145$ |

The exact rational bounds and parameter sums are in RESULTS.json. Every factor preserves total native norm exactly. Moreover,

$$
\|(T_-T_+-I)|_{\mathcal A}\|_2
\le\varepsilon_-+\varepsilon_+
<6.926\times10^{-10}.
$$

*Proof.* The verifier reconstructs the full native matrices, validates every mask and rational parameter, and checks the residual inequalities of Theorem 1 against each exact rational target. The round-trip estimate follows by writing

$$
T_-T_+-R_-R_+
=(T_--R_-)T_++R_-(T_+-R_+)
$$

and using active-sector invariance and orthogonality. Since $R_-R_+=I$, the result follows. $\square$

The operator certificate covers every active-sector input, including every vector orthogonal to the record plane that should remain unchanged at completion. It is stronger than checking one prepared vector.

These compositions resolve the instantaneous-span obstruction for the two stated controlled benchmarks. They do not refute the primitive-generator obstruction: a product of noncommuting allowed updates need not lie in their instantaneous linear span.

For fixed masks and perturbed step parameters, orthogonality and

$$
\frac{dC_A(t)}{dt}
=\left(I-\frac t2A\right)^{-1}
A\left(I-\frac t2A\right)^{-1},
\qquad
\left\|\frac{dC_A(t)}{dt}\right\|_2\le5
$$

give the additional operator-error bound $5\sum_j|\delta t_j|$. For 160 steps with uniform error at most $\delta$, each writer's error is at most $\varepsilon_\pm+800\delta$, provided perturbed steps stay admissible. This is a fixed-mask stability bound, not a source for precise gate timings or protection against mask errors.

Applying a known inverse write is not erasing an unknown receipt. An arbitrary unknown phase cannot be mapped to a fixed blank while preserving all its other information without a transfer or inverse record.

## 5. Intermediate stock and signed ownership

The programmes do not preserve isolation during writing. For the exact unit input $q$, each has a certified intermediate event at which more than $99/100$ of the stock is outside the record plane:

| Programme | Witness pulse | Certified outside-plane stock lower display |
|---|---:|---:|
| Write | 72 | $0.9965$ |
| Unwrite | 47 | $0.9990$ |

The displays are rounded downward; exact rational lower bounds are in RESULTS.json.

To certify them, let $z_n=T_nq$ and let $\widehat z_n$ be the corresponding proposal column. Since $\|z_n\|=1$ and $\|z_n-\widehat z_n\|\le E_n$,

$$
\|(I-P_{\rm rec})z_n\|^2
\ge \|(I-P_{\rm rec})\widehat z_n\|^2-E_n(2+E_n).
$$

The two-cell surrounding field therefore participates materially in these writers. No claim of a continuously protected five-coordinate operation is made.

For signed cell receipts, use the original equal-top-star diagonal ownership weights $W_\tau$. For each proposal step and its exact residual column $r_n$, with midpoint $\widehat m_n$, the checker verifies

$$
\Delta O_\tau(\widehat z)
-t_n\widehat m_n^{\mathsf T}
(W_\tau A_{h_n}-A_{h_n}W_\tau)\widehat m_n
=2\widehat m_n^{\mathsf T}W_\tau r_n.
$$

It checks 640 such trace cut-defect identities and telescoping balances. For the actual unit-input path,

$$
|O_\tau(\widehat z_n)-O_\tau(z_n)|\le E_n(2+E_n).
$$

SIGNED_RECEIPT_SUMMARY.json records the signed unit-core witness totals and actual-path error bounds. Proposal defects are numerical witness residuals, not physical sources.

For the ideal target applied to the pure input $q$, the final cell stocks are exactly

$$
(O_0,O_1)=\left(\frac2{25},\frac{23}{25}\right),
$$

compared with initial $(0,1)$. The shared-face component accounts for the neighboring cell's share. This witness is not a universal ownership split for arbitrary superposed fields. The original scalar core stock becomes $9/25$; the retained record quantity is the projected-plane norm, not scalar core stock or a new physical action quantity.

## 6. The uncontrolled sector is not fixed

The orthogonal vertex/edge-gradient sector is invariant under every mask and sees the same lower generator $D$, with squared frequencies $3$ and $5$. A pure record-plane rotation would leave this sector unchanged, but the two saved native programmes do not.

For a unit vector $w$ in one such modal plane, with $D^2w=-\lambda^2w$, the product acts as

$$
Tw=\alpha w+\beta Dw,\qquad
\alpha^2+\lambda^2\beta^2=1.
$$

Each rational Cayley step has coefficients

$$
a(t)=\frac{1-\lambda^2t^2/4}{1+\lambda^2t^2/4},
\qquad
b(t)=\frac{t}{1+\lambda^2t^2/4},
$$

and the exact recurrence is

$$
\alpha'=\alpha a-\lambda^2\beta b,\qquad
\beta'=\alpha b+\beta a.
$$

Therefore

$$
\|Tw-w\|^2=2(1-\alpha).
$$

The verifier computes these values by exact rational recurrence. For example, a squared-frequency-$5$ unit witness has identity error squared above $11/100$ under the write programme. A squared-frequency-$3$ witness has error squared above $73/100$ under the unwrite programme. Full 23-dimensional identity-on-complement is therefore excluded for these published programmes.

This is not a universal impossibility theorem for every finite Cayley word. It is a certified scope limit of these two witnesses. A clock stored in that uncontrolled sector would need its evolution tracked, rather than being presumed untouched.

## 7. Retention after writing and remaining clock source

All eight masks that close the four faces incident to core $1$ annihilate both $p$ and $q$. After a compiled write, any sequence of these masks retains its **actual** two recorded coordinates exactly. The finite write error does not accumulate in those coordinates during hold.

For active input $x$, the written plane coordinates differ from the ideal rotation by at most $\varepsilon_\pm\|x\|$; the corresponding projected-stock error is at most $2\varepsilon_\pm\|x\|^2$. This retention does not correct the initial write error.

The missing event time cannot be recovered merely by composing a writer after an information-losing peak map: equal peak outputs remain equal under the same fixed writer. A real receipt requires clock information generated and retained before that loss, plus a rule selecting the write programme from it.

Only two fixed angles are certified here. The 160 masks and their parameters are supplied controls. No state-local rule generates them, no arbitrary clock-conditioned family is established, and no programme clock, gate hardware or mode-reset cost is hidden in the field-norm receipt. Physical time and action-unit correspondences remain open.

## 8. Reproduction

Run on a working copy of this capture:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_writer.py
    PYTHONDONTWRITEBYTECODE=1 python3 verify_certificate_controls.py

Verification uses the Python standard library. Deterministic integer elimination proposes rational-grid matrices; exact Fraction residuals certify them. The second checker rejects a changed parameter, changed mask and wrong target sign. Search construction is separately recorded in search_writer.py and requires NumPy/SciPy; it is not needed for verification.

The original real metric and full native contacts remain unchanged. The result is finite controlled approximate actuation for two active-sector writer operators, with explicit leakage and gradient-sector limits. Native clock generation, adaptive writing, source-derived selection, record reset/renewal and physical correspondence remain open. Independent review is pending; physical promotion remains zero.
