# UD_SUPPORT_BURDEN_NORMALIZATION_MAP_AUDIT_v0.1

**Date:** 2026-09-18  
**Status:** EXACT REPRESENTATION FORM + UNIFORM-SECTOR NORMALIZATION NO-GO  
**Physical promotion:** 0

---

## 1. Target

Derive the support↔burden normalization map

\[
\mathcal N_{SB}
\]

and determine whether it constrains the saturation ratio

\[
\kappa_{SB}
\]

in

\[
H_{\widehat B}
\le
\kappa_{SB}H_S.
\]

---

## 2. Common vertex carrier

Current burden transport uses a vertex burden field

\[
b\in C_0(K).
\]

Current support state contains a vertex component

\[
c_0\in C_0(K)
\]

inside

\[
c=(c_0,c_1,c_2,c_3).
\]

Thus a support↔burden normalization can at minimum be studied on the common \(C_0(K)\) representation.

This is a structural carrier correspondence, not yet an identity of units or physical meaning.

---

## 3. K4 representation decomposition

For one K4 vertex space,

\[
C_0(K4)
\cong
\mathbf 1
\oplus
V_3,
\]

where:

- \(\mathbf1\) is the one-dimensional uniform/trivial sector;
- \(V_3\) is the three-dimensional zero-sum standard sector.

Define projectors

\[
\boxed{
P_0
=
\frac14\mathbf1\mathbf1^\top
}
\]

and

\[
\boxed{
P_\perp
=
I-P_0.
}
\]

Factor structure:

\[
4=2^2.
\]

---

## 4. Most general S4-equivariant linear normalization

Any linear map

\[
\mathcal N_{SB}:C_0^B\to C_0^S
\]

that commutes with the K4 vertex-permutation action of \(S_4\) must act as a scalar on each irreducible sector.

Therefore:

\[
\boxed{
\mathcal N_{SB}
=
\nu_0P_0
+
\nu_\perp P_\perp,
}
\]

with

\[
\nu_0,\nu_\perp>0
\]

for a positive normalization.

### AUTO_LOCK

`S4_EQUIVARIANT_SUPPORT_BURDEN_VERTEX_NORMALIZATION_HAS_TWO_SCALAR_SECTORS_v0.1`

This is exact representation theory.

---

## 5. Why Q162 cannot fix \(\nu_0\)

Q162 depends only on

\[
B_1^\top b.
\]

Because

\[
B_1^\top P_0b=0,
\]

the entire burden transport law is blind to the uniform sector.

Therefore any transformation

\[
b
\mapsto
\nu_0P_0b
+
\nu_\perp P_\perp b
\]

changes the uniform normalization without changing the structural zero-sum transport after \(\nu_\perp\) is separately accounted for.

Thus:

\[
\boxed{
\text{Q162 cannot determine }\nu_0.
}
\]

### AUTO_LOCK

`BURDEN_TRANSPORT_CANNOT_FIX_UNIFORM_SUPPORT_BURDEN_NORMALIZATION_v0.1`

This is the normalization form of the earlier uniform-burden-shift no-go.

---

## 6. Contrast normalization

The contrast sector

\[
P_\perp b
\]

does enter Q162 and Q163.

In principle a future typed intertwiner between burden contrast and support \(C_0\) contrast could determine

\[
\nu_\perp.
\]

Current source does not provide that intertwiner.

Therefore:

\[
\nu_\perp
\]

also remains open, although unlike \(\nu_0\) it is dynamically visible.

---

## 7. Normalized burden storage

Define

\[
\widehat b
=
\mathcal N_{SB}b.
\]

Then

\[
H_{\widehat B}
=
\frac12
\|\widehat b\|^2
\]

becomes

\[
\boxed{
H_{\widehat B}
=
\frac12
\left[
\nu_0^2\|P_0b\|^2
+
\nu_\perp^2\|P_\perp b\|^2
\right].
}
\]

For a pure uniform burden state

\[
b=\bar b\,\mathbf1,
\]

\[
P_\perp b=0
\]

and therefore

\[
\boxed{
H_{\widehat B}
=
\frac12
\nu_0^2N_S\bar b^2.
}
\]

The stock is

\[
B_S=N_S\bar b.
\]

Thus any stock-capacity theorem depends directly on \(\nu_0\).

---

## 8. Saturation ratio degeneracy

Suppose the normalized saturation law is

\[
H_{\widehat B}
\le
\kappa_{SB}H_S.
\]

For uniform burden,

\[
\frac12
\nu_0^2
\frac{B_S^2}{N_S}
\le
\kappa_{SB}H_S.
\]

Hence

\[
\boxed{
B_S
\le
\sqrt{
\frac{2\kappa_{SB}N_SH_S}{\nu_0^2}
}.
}
\]

Since

\[
2H_S=S_\mu^{rev},
\]

\[
\boxed{
B_\star
=
\sqrt{
\frac{\kappa_{SB}}{\nu_0^2}
N_SS_\mu^{rev}
}.
}
\]

Therefore current data identify only the combination

\[
\boxed{
\chi_{SB}
:=
\frac{\kappa_{SB}}{\nu_0^2}.
}
\]

The pair

\[
(\nu_0,\kappa_{SB})
\]

is not separately identifiable from a capacity statement alone.

### AUTO_LOCK

`SUPPORT_BURDEN_CAPACITY_DEPENDS_ONLY_ON_KAPPA_OVER_UNIFORM_NORMALIZATION_SQUARED_v0.1`

---

## 9. Normalization gauge

Under

\[
\nu_0
\mapsto
a\nu_0,
\]

and

\[
\kappa_{SB}
\mapsto
a^2\kappa_{SB},
\]

the combination

\[
\chi_{SB}
=
\kappa_{SB}/\nu_0^2
\]

is unchanged.

Thus the storage-capacity law has a normalization-gauge freedom until an independent cross-sector scale fixes \(\nu_0\).

### AUTO_LOCK

`SUPPORT_BURDEN_STORAGE_HAS_NORMALIZATION_GAUGE_v0.1`

This is an internal identifiability statement, not physical gauge theory.

---

## 10. Action-unit audit

Current source preserves a common action-dimension scaffold of the historical form

\[
\mathcal A_0
=
\frac{B_0a_0^2}{\tau_0},
\]

but the reproducible current \(\xi_\hbar\) normalization/convention is unresolved.

More importantly, an action unit fixes dimensions of action-valued objects.

It does not automatically fix the relative norm of:

\[
b\in C_0^B
\]

and

\[
c_0\in C_0^S.
\]

Therefore current action-unit work does not close

\[
\nu_0
\]

or

\[
\nu_\perp.
\]

### AUTO_LOCK

`COMMON_ACTION_DIMENSION_DOES_NOT_FIX_SUPPORT_BURDEN_STATE_NORMALIZATION_v0.1`

---

## 11. Strongest current normalization map

The source-honest current form is

\[
\boxed{
\mathcal N_{SB}
=
\nu_0P_0+\nu_\perp P_\perp,
}
\]

with both coefficients open.

For burden-capacity purposes, the decisive object is

\[
\boxed{
\chi_{SB}
=
\kappa_{SB}/\nu_0^2.
}
\]

The exact conditional capacity is

\[
\boxed{
B_\star
=
\sqrt{
\chi_{SB}
N_SS_\mu^{rev}
}.
}
\]

This is more precise than leaving \(\kappa_{SB}\) alone open.

---

## 12. What would close the map

### Gate A — uniform-sector bridge

Derive one independently normalized state pair

\[
b_{\rm ref},
\qquad
c_{0,\rm ref}
\]

with a theorem stating their common stored-unit equivalence.

This fixes

\[
\nu_0.
\]

### Gate B — contrast intertwiner

Derive a typed relation between

\[
P_\perp b
\]

and

\[
P_\perp c_0.
\]

This fixes or constrains

\[
\nu_\perp.
\]

### Gate C — saturation law

Independently determine

\[
\kappa_{SB}.
\]

Only after A+C can \(B_\star\) be numerically source-closed.

---

## 13. Governance

### AUTO_LOCK

- exact two-sector form of \(\mathcal N_{SB}\);
- Q162 blindness to the uniform normalization;
- normalization-gauge degeneracy;
- capacity depends on \(\chi_{SB}=\kappa_{SB}/\nu_0^2\);
- common action dimension does not fix the state normalization.

### AUTO_FREEZE

- \(\nu_0=1\) by convenience;
- \(\nu_\perp=1\) by convenience;
- \(\nu_0=\nu_\perp\) without a theorem;
- \(\kappa_{SB}=1\) from coordinate normalization;
- interpreting normalization-gauge freedom as physical gauge symmetry.

**Physical promotion:** 0.
