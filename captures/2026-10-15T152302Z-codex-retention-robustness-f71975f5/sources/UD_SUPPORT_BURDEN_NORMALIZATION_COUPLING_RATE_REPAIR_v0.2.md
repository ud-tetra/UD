# UD_SUPPORT_BURDEN_NORMALIZATION_COUPLING_RATE_REPAIR_v0.2

**Date:** 2026-09-18  
**Status:** EXACT REPAIR / SUPERSEDES RAW-TRANSFORMER SHORTHAND  
**Physical promotion:** 0

## 1. Repair target

Previous normalized coupling used

\[
\widehat b = N b
\]

with normalized equations

\[
\dot c
=
\mathcal A c
+
\gamma I_0\widehat b,
\]

\[
\dot{\widehat b}
=
-\gamma I_0^\top c
-
R_{\widehat B}\widehat b.
\]

Here:

- \(N\) is a **state normalization / unit map**;
- \(\gamma\) is a **coupling rate**;
- \(I_0\) is the degree-zero support inclusion.

These are distinct typed objects.

---

## 2. Exact raw-coordinate transformation

Since

\[
\widehat b = Nb
\]

with constant invertible \(N\),

\[
\dot{\widehat b}
=
N\dot b.
\]

Therefore the raw equations are

\[
\boxed{
\dot c
=
\mathcal A c
+
\gamma I_0Nb,
}
\]

\[
\boxed{
\dot b
=
-\gamma N^{-1}I_0^\top c
-
N^{-1}R_{\widehat B}Nb.
}
\]

This is the correct transformed system.

### AUTO_REPAIR

`RAW_SUPPORT_BURDEN_COUPLING_USES_RECIPROCAL_N_AND_N_INVERSE_FACTORS_v0.2`

---

## 3. Scalar-local specialization

For

\[
N=\kappa I,
\qquad
\kappa>0,
\]

the cross-coupling equations become

\[
\boxed{
\dot c
=
\mathcal A c
+
\gamma\kappa I_0 b,
}
\]

\[
\boxed{
\dot b
=
-\frac{\gamma}{\kappa}I_0^\top c
-
R_Bb
}
\]

when \(R_{\widehat B}\) commutes with the scalar normalization.

Thus the raw forward and reverse coefficients are

\[
\boxed{
k_+
=
\gamma\kappa,
}
\]

\[
\boxed{
k_-
=
\frac{\gamma}{\kappa}.
}
\]

A normalization factor cannot be used as a symmetric raw coupling rate.

---

## 4. Exact factor-separation theorem

If a source-complete reciprocal raw process independently supplies both positive coefficients

\[
k_+,
\qquad
k_-,
\]

then

\[
k_+k_-=\gamma^2,
\]

so

\[
\boxed{
\gamma
=
\sqrt{k_+k_-}.
}
\]

Also,

\[
\frac{k_+}{k_-}
=
\kappa^2,
\]

so

\[
\boxed{
\kappa
=
\sqrt{\frac{k_+}{k_-}}.
}
\]

### AUTO_LOCK

`RECIPROCAL_RAW_TRANSFER_SEPARATES_RATE_AND_NORMALIZATION_v0.1`

This is the correct route to identify coupling rate and state normalization separately.

---

## 5. General matrix form

For a positive invertible normalization \(N\), define raw cross maps

\[
F
=
\gamma N,
\]

\[
G
=
\gamma N^{-1}.
\]

Then

\[
\boxed{
FG
=
GF
=
\gamma^2 I.
}
\]

Thus a valid reciprocal raw pair must satisfy the consistency test

\[
\boxed{
FG
\propto I.
}
\]

If \(F\) and \(G\) are independently derived and

\[
FG=\lambda I,
\qquad
\lambda>0,
\]

then

\[
\boxed{
\gamma=\sqrt{\lambda},
}
\]

and

\[
\boxed{
N=\frac{F}{\gamma}
=
\gamma G^{-1}.
}
\]

This generalizes the scalar theorem.

---

## 6. \(S_4\)-sector form

For K4,

\[
N
=
\nu_0P_0+\nu_\perp P_\perp.
\]

If one common coupling rate \(\gamma\) acts on both irreducible sectors, then

\[
F
=
f_0P_0+f_\perp P_\perp,
\]

\[
G
=
g_0P_0+g_\perp P_\perp
\]

must satisfy

\[
\boxed{
f_0g_0
=
f_\perp g_\perp
=
\gamma^2.
}
\]

The normalizations are then

\[
\boxed{
\nu_0
=
\sqrt{\frac{f_0}{g_0}},
}
\]

\[
\boxed{
\nu_\perp
=
\sqrt{\frac{f_\perp}{g_\perp}}.
}
\]

Failure of the equal-product condition falsifies a single-rate reciprocal model.

---

## 7. Storage metric repair

Normalized storage is

\[
H
=
\frac12\|c\|^2
+
\frac12\|\widehat b\|^2.
\]

In raw coordinates,

\[
\boxed{
H
=
\frac12\|c\|^2
+
\frac12 b^\top N^\top N b.
}
\]

Therefore the raw burden metric is

\[
\boxed{
G_B^{raw}
=
N^\top N.
}
\]

The raw cross block

\[
\begin{pmatrix}
0&\gamma I_0N\\
-\gamma N^{-1}I_0^\top&0
\end{pmatrix}
\]

is not generally skew under the ordinary Euclidean raw inner product.

It is power-skew with respect to the pulled-back storage metric.

### Scalar case

For \(N=\kappa I\),

\[
H
=
\frac12\|c\|^2
+
\frac{\kappa^2}{2}\|b\|^2.
\]

Cross terms cancel exactly.

But ordinary raw Euclidean storage

\[
H_E
=
\frac12\|c\|^2
+
\frac12\|b\|^2
\]

has cross derivative

\[
\boxed{
\dot H_E^{cross}
=
\gamma
\left(
\kappa-\frac1\kappa
\right)
c_0^\top b.
}
\]

Thus Euclidean raw storage is cross-conserved only when

\[
\boxed{
\kappa=1.
}
\]

### AUTO_LOCK

`RAW_EUCLIDEAN_STORAGE_IS_NOT_PRESERVED_BY_NONTRIVIAL_NORMALIZATION_v0.1`

---

## 8. Superseded statements

### SUPERSEDED

The shorthand

\[
T_{SB}^{raw}=I_0N
\]

as if it alone were the complete raw Dirac coupling.

Correct statement:

\[
\boxed{
F_{B\to S}
=
\gamma I_0N,
\qquad
F_{S\to B}
=
\gamma N^{-1}I_0^\top.
}
\]

### SUPERSEDED

A symmetric raw law

\[
\dot c\propto\kappa b,
\qquad
\dot b\propto-\kappa c_0
\]

being generated solely by normalization \(N=\kappa I\).

That symmetric law uses \(\kappa\) as a **coupling rate**, not a state normalization.

---

## 9. Updated dependency graph

The raw bridge now has two independent targets:

### NORM-SB
Derive

\[
N.
\]

### RATE-SB
Derive

\[
\gamma.
\]

A source-complete reciprocal raw process can close both simultaneously if it returns both directional maps \(F\) and \(G\).

---

## 10. Governance

### AUTO_LOCK
- reciprocal \(N/N^{-1}\) transformation;
- separation of \(\gamma\) and \(N\);
- exact factor-identification theorem;
- pulled-back raw storage metric.

### AUTO_FREEZE
- absorbing a coupling rate into normalization while retaining the same raw equations;
- treating \(I_0N\) as the complete raw Dirac block;
- claiming raw Euclidean storage conservation for \(N\neq I\).

**Physical promotion:** 0.
