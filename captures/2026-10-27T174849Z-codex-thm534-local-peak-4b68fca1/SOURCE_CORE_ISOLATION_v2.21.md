# THM-534 v2.21 — Native core isolation and the stopping problem

**26 October 2026.** Exact conditional statements on the original real carrier. A local isolation condition and a certified loading witness are distinguished from a mechanism that generates the switching decisions.

## Abstract

The finite transfer in v2.20 does not supply an autonomous stopping rule. Its face-output endpoint is not stationary for any permitted mask, including the all-off mask. We derive a necessary and sufficient local condition for universal retention of an existing cell-core amplitude: all four whole-face gates incident to that core must be closed. The condition protects the core under arbitrary subsequent native Cayley steps without stopping the remaining field. A 64-step extension of the previous sequence loads that core with a rational final-state error bound below $5.500\times10^{-11}$. Endpoint observation aliasing and a failed occupancy trigger identify the remaining decision problem.

## 1. Native model

Use the oriented filled cells $[0123]$, $-[0124]$, with one real amplitude per unique simplex and the original unit metric:

$$
\mathcal H=C_0\oplus C_1\oplus C_2\oplus C_3,
\qquad \dim\mathcal H=5+9+7+2=23.
$$

Faces are ordered $012,013,014,023,024,123,124$. For the signed boundaries $B_k$, a binary mask $h$, and $H=\operatorname{diag}(h)$, set

$$
A_h=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-HB_3\\
0&0&B_3^{\mathsf T}H&0
\end{pmatrix},
\quad
C_h(t)=\left(I-\frac t2 A_h\right)^{-1}
       \left(I+\frac t2 A_h\right).
$$

Each gate acts on its entire face–core star, including both shared-face contacts. Both lower incidence couplings remain when all top gates are off. A positive $t$ is a dimensionless Cayley parameter, without an identified physical clock. A finite Cayley step is not identified with the continuous flow.

Let $x_{\rm w}$ have edge amplitudes $(-1,1,-1)$ on $01,02,12$, respectively, and zero elsewhere. Set $c=24/37$. The old final target and new parking target are

$$
X_{\rm face}=x_{\rm w}+ce_{024},
\qquad X_{\rm core}=x_{\rm w}+ce_{0124},
\qquad \|X_{\rm face}\|^2=\|X_{\rm core}\|^2
=N=\frac{4683}{1369}<4.
$$

Assigning an output role to the second core is supplied boundary information. No field coordinate, metric weight or reservoir is added.

## 2. Why the old endpoint does not stop

**Theorem 1.** Every binary mask satisfies

$$
\|A_hX_{\rm face}\|_2^2
=\frac{22263}{1369}+h_{024}\frac{576}{1369}>16,
\qquad (A_hX_{\rm face})_{024}=1.
$$

Consequently no permitted continuous vector field is stationary there, and no single positive Cayley step fixes the entire state.

*Proof.* Both cores vanish. The edge component is $-cB_2e_{024}$, of squared norm $3c^2$. The face component is $B_2^{\mathsf T}x_{\rm w}$, with entries

$$
(-3,-1,-1,1,1,-1,-1)
$$

and squared norm $15$. The only top component is the second-core contribution of the populated face $024$, with squared norm $h_{024}c^2$. Orthogonality of grades gives the formula. For $t>0$, multiplying the Cayley fixed-point equation by its invertible denominator gives

$$
C_h(t)x=x\quad\Longleftrightarrow\quad tA_hx=0.
$$

$\square$

The continuous derivative and discrete fixed-point statements have separate meanings. A unit all-off Cayley step also changes the old output face from $24/37$ to $1444/2331$, exactly. No returning-product or tiny-step slowing obstruction is asserted.

For the actual v2.20 endpoint, whose error is $b<10^{-10}$, the native bound $\|A_h\|_2\le\|A_h\|_\infty=5$ gives

$$
\|A_hx\|_2>4-5b>3.99,
\qquad (A_hx)_{024}\ge1-5b>0.
$$

Even a convex mixture of the permitted continuous generators cannot freeze the ideal target: the nonzero lower-grade components are independent of the mask.

## 3. Two kernel statements

**Theorem 2.** The all-off kernel and common kernel are, respectively,

$$
\ker A_0=
\mathbb R\,\mathbf1_{C_0}
\operatorname{im}B_3\big|_{C_2}
C_3,\qquad \dim\ker A_0=5,
$$

$$
\bigcap_h\ker A_h=\mathbb R\,\mathbf1_{C_0}.
$$

*Proof.* The boundary ranks are $4,5,2$, with consecutive products zero. For an all-off null vector, $B_1e=B_2^{\mathsf T}e=0$. Exactness $\ker B_1=\operatorname{im}B_2$ forces $e=0$. The edge equation $B_1^{\mathsf T}v-B_2f=0$ is a sum of orthogonal terms, so both vanish. Thus $v$ is constant, $f\in\ker B_2=\operatorname{im}B_3$, and the cores are free.

For the common kernel, subtract $A_0$ from each singleton-mask generator. Each face-star difference forces its face amplitude to vanish, and the private faces force both cores to vanish. The lower equations then leave only the constant vertex vector. $\square$

The active subspace

$$
\mathcal A=\ker B_1\big|_{C_1}\oplus C_2\oplus C_3
$$

has dimension $14$, is invariant under every mask, and contains the preparations and targets. It is orthogonal to the common kernel. A nonzero active preparation therefore cannot be stationary independently of every future mask. Storage under a restricted mask family is possible and is the construction below.

## 4. A local native isolation rule

Choose output core $o=0124$. Its incident faces are

$$
\partial o=\{012,014,024,124\}.
$$

**Theorem 3 (universal isolation).** For a fixed mask $h$, these conditions are equivalent:

1. All four gates on $\partial o$ are zero.
2. $A_he_o=0$.
3. For any fixed $t>0$, every field satisfies $(C_h(t)x)_o=x_o$.
4. Its continuous flow preserves $x_o$ for every field and every time.

Condition 3 need only hold on a nonempty open field neighborhood to imply condition 1.

*Proof.* The $o$-column consists precisely of the four signed incident face contacts. It vanishes exactly when their gates vanish. Skew symmetry gives the zero row, hence preservation in both models.

Conversely, a linear functional vanishing on an open neighborhood vanishes everywhere. If $e_o^{\mathsf T}C_h(t)=e_o^{\mathsf T}$, multiply on the right by $I-tA_h/2$, which commutes with the Cayley matrix. This gives $te_o^{\mathsf T}A_h=0$. Skew symmetry gives condition 2. Differentiation at zero proves the continuous converse. $\square$

The parameter-free **conditional isolation prescription** is

$$
\boxed{h_f=0\quad\text{for every }f\subset o.}
$$

It fixes four local gates and leaves $013,023,123$ free, so exactly eight masks qualify. The shared face $012$ closes on both sides. Any subsequent sequence of these masks preserves output amplitude and stock exactly for arbitrary positive Cayley parameters and arbitrary other field amplitudes. The remaining field need not stop.

This is necessary for universal amplitude retention under a fixed mask, not for a cancellation at one field. It is covariant when the chosen core and incidences are relabeled together. It does not select the core or determine loading completion.

**Corollary (retention and gate-error exposure).** If the loaded core obeys $|x_o-c|\le b$, isolating masks retain this same error forever, without accumulation or correction. At norm squared $N$, mistaken opening of $m_n$ incident faces in later steps gives

$$
|\Delta x_o|\le\sqrt N\sum_n t_n\sqrt{m_n}
\le2\sum_n t_nm_n.
$$

*Proof.* With midpoint $\bar x_n=(x_n+x_{n-1})/2$, the exact Cayley receipt is

$$
x_{n,o}-x_{n-1,o}
=t_n\sum_{f\subset o}h_{n,f}(B_3)_{f,o}\bar x_{n,f}.
$$

The midpoint norm is at most $\sqrt N$. Cauchy–Schwarz bounds the sum by $\sqrt{m_n}\sqrt N$. Sum absolute bounds, use $\sqrt N<2$, and use $\sqrt m\le m$ for integer $m\ge0$. Closed steps contribute exactly zero. $\square$

The exposure is measured in Cayley parameters, not physical time.

## 5. Certified native loading

The full certificate appends 64 positive rational steps to the 192-step v2.20 word. Every prefix mask, parameter and rational trace vector is unchanged. There is no reset at pulse 192. The checker binds the canonical prefix to SHA-256

    27adf805ce5732ebeda11a7881686cd9b2e934f1d75d5a75e1d4a4459189dd1d

The appended target is $X_{\rm core}$.

**Theorem 4.** From the original preparation $X_0=x_{\rm w}+ce_{014}$, the 256-step certificate reaches

$$
\|x_{256}-X_{\rm core}\|_2
\le b=\frac{406991704088902063}
{7400000000000000000000000000}
<5.500\times10^{-11}.
$$

Norm remains exactly $4683/1369$, and the first three checkpoint bounds are unchanged. The worker is restored within $b$; the old face ports and first core are empty within $b$; the second-core stock satisfies

$$
|x_{256,o}^2-c^2|\le b(2c+b).
$$

Closing the four incident gates thereafter preserves this actual core amplitude and stock exactly.

*Proof.* For saved rational trace vectors, with $q_0=X_0$, define

$$
r_n=q_n-q_{n-1}
-t_nA_{h_n}\frac{q_n+q_{n-1}}2,\qquad
E_n=\sum_{j\le n}\|r_j\|_1.
$$

For skew $A$, its Cayley map is orthogonal and
$\|(I-tA/2)^{-1}\|_2\le1$. Induction gives
$\|x_n-q_n\|_2\le E_n$ without checkpoint resets. The exact rational checker computes

$$
E_{256}+\|q_{256}-X_{\rm core}\|_1
=\frac{406991704088902063}
{7400000000000000000000000000}.
$$

It checks all mask bits and positive parameters, prefix binding, 128 native skew generators and 512 signed cell-ownership cut-defect identities. The stock bound follows from $|x_o-c|\le b$; retention follows from Theorem 3. $\square$

The certificate is an approximate transfer for one supplied preparation, not a universal operator transformation. Masks and parameters were constructed using the target. Their sum is approximately $210.902415$, without a physical-time or optimality claim. The implicit whole-carrier Cayley inverse is supplied; a bounded-radius implementation has not been derived.

Original equal-top-star ownership gives the same ideal initial and final cell stocks,

$$
(O_{0123},O_{0124})
=\left(\frac32,\frac32+\frac{576}{1369}\right).
$$

The feed and stored core belong to the second cell. Signed receipts certify internal transfer, not fresh source production. The receipt file provides rational trace changes, exact midpoint-cut defects and rigorous bounds for actual receipts. Trace defects are not physical sources. Gate hardware, readout and renewed supply are not costed by these field receipts.

## 6. The missing trigger

The restriction to all 15 simplex coordinates of the first tetrahedron is identical at the ideal original preparation, old final target and parked target:

$$
P_{0123}X_0=P_{0123}X_{\rm face}
=P_{0123}X_{\rm core}=x_{\rm w}.
$$

A deterministic memoryless controller reading only those coordinates must issue the same command at those ideal states. It cannot issue different start/completion commands from that observation alone. The actual parked observation lies within $b$ of the initial observation; a controller constant on a ball of radius greater than $b$ cannot robustly exploit the small numerical discrepancy. Additional boundary observations or a distinct phase record are required for that task. This does not obstruct a controller in the second cell, where the output core changes.

The candidate trigger “close the output gates when its core becomes nonzero” also fails to identify completion. Exact residual bounds after the **first** prefix step give

$$
0.1<x_{1,o}<0.13<c=\frac{24}{37}.
$$

Latching then would preserve that early value, rather than the completed output. A current or occupancy becoming nonzero therefore does not identify completion of this sequence. A target-amplitude threshold would add a constitutive target and need its own source and robustness justification.

The result supplies the local gate pattern necessary and sufficient for universal core retention, and a finite native loading witness. It leaves generation of the output role, completion event and latched pattern open, along with their clock and preparation.

## 7. Reproduction

From the capture directory, run:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_parking.py
    PYTHONDONTWRITEBYTECODE=1 python3 verify_native_latch.py

Both use standard-library rational arithmetic. Numerical search and trace-construction files are separate. The latch audit checks 128 mask patterns, eight isolating masks, 72 exact finite-step retention controls, kernel ranks, endpoint observation aliasing and the premature trigger.

Continuous-flow loading compilation, geometric gate realization, autonomous completion detection, controller/record reset, repeated fresh supply and the physical action-unit map remain open. Independent review is pending; no physical identification is claimed.
