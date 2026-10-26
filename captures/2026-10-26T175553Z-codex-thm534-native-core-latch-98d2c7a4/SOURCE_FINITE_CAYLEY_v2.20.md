# THM-534 v2.20 — A finite native Cayley checkpoint certificate

**Date:** 26 October 2026. **Mathematical scope:** an explicitly supplied switched discrete model on the original real simplicial carrier. Exact rational certification of an approximate, known-preparation transfer. No physical correspondence is asserted.

## Abstract

We give a finite sequence of 192 positive rational Cayley steps on the original two-tetrahedron carrier. Every generator retains the native vertex–edge and edge–face incidence terms and uses one binary multiplier per whole face–core star. Starting from a specified edge-cycle state and a prepared native feed face, the sequence passes within $10^{-10}$ of three specified checkpoints, ending with the worker restored, the feed nearly empty and its initial stock transferred to a native output face. An exact rational residual argument certifies the full 23-dimensional trajectory without large-denominator exact iteration. It also certifies signed cell-stock receipts and sensitivity to step-size errors. The result supplies a finite witness for the Cayley model; it does not derive autonomous selection, a continuous-flow schedule, a physical clock or renewed boundary preparation.

## 1. Carrier and permitted steps

Use the oriented filled tetrahedra $[0123]$ and $-[0124]$, with each underlying simplex represented once. In increasing vertex order within each grade, the real space is

$$
\mathcal H=C_0\oplus C_1\oplus C_2\oplus C_3,
\qquad (\dim C_0,\dim C_1,\dim C_2,\dim C_3)=(5,9,7,2).
$$

The metric is the original Euclidean sum of squared real simplex amplitudes. Let $B_k:C_k\to C_{k-1}$ be the signed simplicial boundaries. The face ordering is

$$
(012,013,014,023,024,123,124).
$$

For a supplied binary mask $h\in\{0,1\}^7$, let $H=\operatorname{diag}(h)$ and

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix}.
$$

In particular, a gate on the shared face $012$ acts on **both** incident cores with their original incidence signs. No independently addressed shared-face contact or drift-free face generator is executed. Define

$$
C_h(t)=\left(I-\frac t2A_h\right)^{-1}
        \left(I+\frac t2A_h\right),\qquad t>0.
$$

All $t$ in the certificate are positive rationals no larger than $4$. They are dimensionless **Cayley parameters**. A finite $C_h(t)$ is not identified with the continuous flow $e^{tA_h}$. Executing the implicit full-carrier Cayley map is an explicit model assumption; an incidence-local generator alone does not make its inverse a bounded-radius local hardware operation.

## 2. Fixed input and checkpoints

Let $e_0$ have edge entries $-1,+1,-1$ on $01,02,12$, respectively, and zero elsewhere. Thus $B_1e_0=0$ and $|e_0|^2=3$. Embed this as $x_0\in\mathcal H$, with all other grades zero. Set $c=24/37$. Let $y$ have edges $(3/37)e_0$, faces

$$
(y_{012},y_{013},y_{023},y_{123})
=\frac1{37}(-48,-20,20,-20),
$$

first core amplitude $c$, and every other coordinate zero. Let $z=y-ce_{0123}$. With feed coordinate $r=014$ and output coordinate $o=024$, define

$$
\begin{aligned}
X_0&=x_0+ce_r,\\
X_1&=y+ce_r,\\
X_2&=z+ce_r+ce_o,\\
X_3&=x_0+ce_o.
\end{aligned}
$$

Every vector has squared norm

$$
N=3+c^2=\frac{4683}{1369}<4.
$$

These are prescribed target vectors. In particular, $X_1$ is not claimed to arise from a single isolated-tetrahedron step zero-padded into the glued carrier. The certificate uses the full glued generators throughout. Feed/output roles and the initial preparation are supplied boundary information.

## 3. A finite, certified witness

`SCHEDULE_CERTIFICATE.json` contains the complete ordered list of 192 masks and rational step sizes. The first 64 steps target $X_1$, the next 64 target $X_2$, and the last 64 target $X_3$. There is **no reset at either intermediate checkpoint**. Define the exact, mathematically specified trajectory by

$$
x_n=C_{h_n}(t_n)x_{n-1},\qquad x_0=X_0.
$$

The file also supplies rational trace vectors $q_n$ with denominator $10^{14}$. These vectors are witnesses for certification, not a second state update law. Set $q_0=X_0$.

**Theorem 1 (residual enclosure).** Write

$$
m_n=\frac{q_n+q_{n-1}}2,\qquad
r_n=q_n-q_{n-1}-t_nA_{h_n}m_n,\qquad
E_n=\sum_{j=1}^{n}\|r_j\|_1.
$$

Then $\|x_n-q_n\|_2\le E_n$. Consequently, at checkpoint $k$,

$$
\|x_{64k}-X_k\|_2
\le E_{64k}+\|q_{64k}-X_k\|_1=:b_k.
$$

*Proof.* For a real skew matrix $A$, $M=I-tA/2$ obeys

$$
\|Mv\|_2^2=\|v\|_2^2+\frac{t^2}4\|Av\|_2^2,
$$

so $M$ is invertible and $\|M^{-1}\|_2\le1$. Its Cayley transform is orthogonal. The residual equation gives

$$
q_n=C_{h_n}(t_n)q_{n-1}+M_n^{-1}r_n.
$$

Subtract the exact update, apply the triangle inequality and orthogonality, and use $\|r_n\|_2\le\|r_n\|_1$. Induction starts with zero error. The checkpoint inequality follows by another triangle inequality. All residuals and displayed bounds are rational expressions. $\square$

`verify_schedule.py` reconstructs the boundaries and every native matrix using Python's standard-library rational arithmetic. It computes the following exact bounds; decimal entries below are rounded **upward** for display.

| Checkpoint | Steps applied | Certified state error, upper bound | Sum of Cayley parameters, approximate display |
|---|---:|---:|---:|
| $X_1$ | 64 | $2.015\times10^{-11}$ | 49.309886 |
| $X_2$ | 128 | $4.267\times10^{-11}$ | 99.561709 |
| $X_3$ | 192 | $5.039\times10^{-11}$ | 155.727559 |

The exact rational $b_k$, parameter sums, masks and trace are in `RESULTS.json` and the certificate. In particular $b_k<10^{-10}$ for every checkpoint. Parameter sums are descriptive model quantities; they are not physical elapsed times or continuous-flow execution times.

**Theorem 2 (finite witness).** Under the stated availability of the full masked Cayley maps, the ordered certificate is a finite native-generator sequence satisfying the three checkpoint bounds above. It preserves $\|x_n\|_2^2=N$ exactly.

*Proof.* The verifier checks positivity/rationality of each parameter, all seven binary mask entries, all 128 reconstructed mask generators for skew symmetry, and the three residual inequalities using Theorem 1. Every factor is orthogonal. The ordered composition therefore gives the asserted finite witness and exact norm conservation. This proof uses no controllability closure argument or Lie-bracket pulse implementation. $\square$

This is a certified approximate state transfer for **one known preparation**. It does not certify equality to the three full target rotation operators from v2.19 on arbitrary inputs. The schedule was constructed using the checkpoint targets; it is not a target-blind selection law or an empirical blind test.

## 4. Signed native receipts

For each cell $\tau$, assign simplex weight

$$
w_{\sigma,\tau}
=\frac{\mathbf1_{\{\sigma\subseteq\tau\}}}{n_3(\sigma)},
\qquad W_\tau=\operatorname{diag}(w_{\sigma,\tau}),
\qquad O_\tau(x)=x^{\mathsf T}W_\tau x.
$$

Here $n_3(\sigma)$ is the number of incident top-dimensional cells, and $W_0+W_1=I$. This is the original equal-top-star ownership; the three populated shared edges initially contribute $3/2$ to each cell. Both ideal endpoints have

$$
(O_0,O_1)=\left(\frac32,\frac32+\frac{576}{1369}\right).
$$

Equal endpoint ownership does not imply zero intermediate transport. The native feed and output lie in the second cell, so feed-to-output transfer is compatible with zero net endpoint cell-stock change.

**Theorem 3 (exact signed discrete continuity).** For an exact step $x^+=C_h(t)x$ and $\bar x=(x^++x)/2$,

$$
O_\tau(x^+)-O_\tau(x)
=t\bar x^{\mathsf T}(W_\tau A_h-A_hW_\tau)\bar x
=2t\sum_{i<j}(w_i-w_j)(A_h)_{ij}\bar x_i\bar x_j.
$$

For the rational trace, let $\Delta O_\tau(q)=O_\tau(q_n)-O_\tau(q_{n-1})$, and let $F_\tau(q)$ be the same incidence-cut sum evaluated at $m_n$. Then

$$
\Delta O_\tau(q)-F_\tau(q)=2m_n^{\mathsf T}W_\tau r_n.
$$

Moreover,

$$
\begin{aligned}
|O_\tau(q_n)-O_\tau(x_n)|&\le E_n(4+E_n),\\
|\Delta O_\tau(q)-\Delta O_\tau(x)|
&\le E_{n-1}(4+E_{n-1})+E_n(4+E_n).
\end{aligned}
$$

*Proof.* Expand a quadratic difference as $2\bar x^{\mathsf T}W_\tau(x^+-x)$, insert the midpoint update and use skew symmetry. For the trace, insert $q_n-q_{n-1}=tA_hm_n+r_n$. Finally, $\|W_\tau\|_2\le1$, $\|x_n\|_2=\sqrt N<2$ and $\|q_n-x_n\|_2\le E_n$, giving the quadratic-error bound and its two-endpoint difference bound. $\square$

`SIGNED_RECEIPTS.json` supplies 192 pairs of rational signed trace stock changes, their exact cut defects, and certified error bounds for the actual trajectory's stock changes. These are **signed transfers**. No sum of absolute circulating fluxes is identified with a fresh consumable source. The verifier checks all 384 cut-defect identities and telescoping endpoint balances exactly. Actual receipts obey exact continuity; trace defects measure numerical witness error and are not physical sources.

For the final target error $b_3$, the worker's vector restoration error is at most $b_3$, the final feed stock is at most $b_3^2$, and

$$
|x_{192,o}^2-c^2|\le b_3(2c+b_3).
$$

Thus the prepared feed is debited and the output receives approximately $c^2=576/1369$ within explicit bounds. Both final core amplitudes have magnitude at most $b_3$. No output isolation, repeated fresh feed or record reset is inferred from this one-cycle calculation.

## 5. Robustness with a fixed mask word

**Theorem 4 (initial-state and step-parameter errors).** Keep the ordered masks fixed. Let the implemented parameters be $t_n+\delta_n$, and the initial state differ from $X_0$ by at most $\eta$ in Euclidean norm. At checkpoint $k$, the error relative to $X_k$ is bounded by

$$
b_k+\eta+2\sum_{n=1}^{64k}\|A_{h_n}\|_\infty|\delta_n|.
$$

For this certificate every generator has maximum absolute row sum $5$. If $|\delta_n|\le\delta$, the coefficients multiplying $\delta$ are $640,1280,1920$ at the three checkpoints.

*Proof.* Put $M(t)=I-tA/2$. Since $C_A(t)=2M(t)^{-1}-I$ and $A$ commutes with $M(t)$,

$$
\frac{dC_A(t)}{dt}=M(t)^{-1}A M(t)^{-1},\qquad
\left\|\frac{dC_A(t)}{dt}\right\|_2\le\|A\|_2\le\|A\|_\infty.
$$

The last inequality holds here because a skew matrix has equal maximum absolute row and column sums. Integrate this bound between the two real step parameters. Telescope the product difference, using orthogonality of every factor and $\|X_0\|_2<2$; the separately propagated initial error remains at most $\eta$. Add the nominal checkpoint bound. The verifier computes the row sums and cumulative coefficients. $\square$

For example, a uniform step-parameter error of at most $10^{-6}$ and exact initial preparation imply a final state error below $0.001921$. If execution requires positive parameters, perturbations must also preserve positivity. This is a stability estimate, not an optimized tolerance, and gives no protection against an arbitrary mask change.

## 6. Reproduction and remaining question

Run `python3 verify_schedule.py` in the capture directory. This requires only the standard library and the saved certificate. It regenerates `RESULTS.json` and `SIGNED_RECEIPTS.json`. Numerical search is not needed to verify the witness. Separate construction files record a NumPy/SciPy search with fixed seeds and rationalized parameters; optimizer termination alone is not the evidence for the theorem.

The checker rejected three fixed-trace corruptions: a face-mask bit flip, replacement of the first step by $1$, and a $10^{-4}$ perturbation of a saved face amplitude. These are constructor checks; independent review remains outstanding.

The concrete gap reduced here is **finite, quantitatively certified Cayley-model state transfer**. The next selection question is whether an admissible local state/record rule can generate the required mask changes and stopping conditions, including its own clock and boundary preparation, without being handed this target-dependent schedule. Continuous-flow compilation, geometric mask realizability, repeated supply/renewal and the action-unit map remain separate open problems.
