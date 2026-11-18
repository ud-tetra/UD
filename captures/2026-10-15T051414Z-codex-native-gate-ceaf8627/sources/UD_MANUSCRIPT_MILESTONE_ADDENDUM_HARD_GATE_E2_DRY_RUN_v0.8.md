# Unified Dynamics — Manuscript Milestone Addendum: Hard-Gate Contrast Transduction and E2 Full Dry Run v0.8

**Date:** 2026-09-14  
**Status:** `INSERT_READY_MILESTONE_ADDENDUM`  
**Physical promotion:** `0`

## 1. Hard face gates are generator changes, not open sources

The locked support carrier permits binary hard face gates

\[
h_f\in\{0,1\}.
\]

Let

\[
H=\operatorname{diag}(h_f).
\]

The gated \(C_2\leftrightarrow C_3\) skew pair is

\[
\dot c_2
=
B_2^{\mathsf T}c_1-HB_3c_3,
\]

\[
\dot c_3
=
B_3^{\mathsf T}Hc_2-B_4c_4.
\]

Relative to the ungated carrier,

\[
r_2^{(H)}
=
(I-H)B_3c_3,
\]

\[
r_3^{(H)}
=
-B_3^{\mathsf T}(I-H)c_2.
\]

These satisfy

\[
2c_2^{\mathsf T}r_2^{(H)}
+
2c_3^{\mathsf T}r_3^{(H)}
=
0.
\]

Therefore the gate changes the skew generator and redistributes support; it is not an exogenous open-system source.

## 2. Hidden-to-visible facet-contrast transduction

With

\[
P_{23}
=
\frac15B_3B_3^{\mathsf T},
\]

the ungated facet-contrast lane is blind to

\[
(I-P_{23})c_2.
\]

Under hard gating, the new contribution is

\[
T_H
=
B_3^{\mathsf T}H(I-P_{23}).
\]

A complete enumeration of all

\[
2^{10}=1024
\]

binary face masks gives only two masks with

\[
T_H=0:
\]

the all-open and all-closed masks.

Thus all

\[
1022=2\cdot7\cdot73
\]

nonuniform masks possess at least one hidden-to-visible transduction direction.

The rank distribution is

\[
0:2,\quad
1:20,\quad
2:110,\quad
3:460,\quad
4:432.
\]

Hence a source-bound nonuniform closure pattern can convert previously facet-invisible \(C_2\) support into visible \(C_3\) contrast with no fitted continuous parameter.

## 3. Gate no-go

Hard gating does not create contrast from mathematical nothing.

If

\[
c_2=0
\]

and

\[
c_3\propto B_4,
\]

then no hard mask produces a facet-contrast drive.

The gate therefore requires pre-existing/source-bound support or context structure.

## 4. E2 full synthetic workflow replay

The apparatus-specific E2 workflow has now been replayed end-to-end on synthetic data.

The run executed:

- apparatus binding;
- calibration and state-label freeze;
- 36-trial state qualification;
- SHA-256 qualification freeze;
- 36-slot balanced \(E_0/E_1/E_2\) acquisition;
- SHA-256 primary freeze;
- 12/12 E2 carrier validations;
- independent burden-provider returns;
- independent leakage-provider returns;
- provider freeze;
- joint merge readiness;
- deliberate multi-slip rejection;
- deliberate missing-channel no-score;
- final full-directory custody freeze.

No synthetic fixture was permitted to generate a scientific bridge verdict.

## 5. Dry-run repair

The replay found one executable workflow omission:

the frozen \(n=2/n=3\) separation rule lacked a standalone validator.

An append-only validator was added using the already-frozen

\[
3\sigma
\]

threshold.

No scientific threshold or interpretation rule changed.

## 6. Current closure state

### AUTO_LOCK

- hard gate residuals are generator-difference terms, not open sources;
- nonuniform hard gating can transduce hidden \(C_2\) support into facet contrast;
- every nonuniform binary Delta4 hard-face mask has nonzero hidden-to-contrast transduction;
- zero-\(C_2\)/pure-top state remains a no-go for gate-generated contrast;
- full synthetic E2 apparatus/custody workflow passes;
- multi-slip fails rather than relabels;
- missing leakage produces no-score;
- standalone state-qualification validation is now executable.

### OPEN

- source law producing the actual pre-gate \(C_2\) state and hard-gate pattern;
- real laboratory binding;
- real E2 data;
- physical bridge.

**Physical promotion remains 0.**
