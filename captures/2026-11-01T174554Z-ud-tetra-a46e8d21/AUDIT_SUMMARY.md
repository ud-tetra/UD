# UD Rolling-Circle/Hodge Readout - Exact Research Capture v0.1

Date: 2026-11-01
Status: EXACT_INTERNAL / CANDIDATE_OBSERVER / NO_GO_LINEAR_READOUT / PHYSICAL_PROMOTION_0

## Source and carrier
The user-supplied image shows rolling-circle parametric curves, not a native packet action. Current UD Paper I, section 4.3 (public mathematics page) supplies the real 15D filled-tetrahedron unit-simplex skew generator A=B^T-B, satisfying A^2=-4(I-P0) and spectrum lambda*(lambda^2+4)^7. Its evolution parameter s has no SI clock. The recovered ledger v0.85 (inherited scientific revision v0.43) O09 is a positive-frequency loop-history action and Q76-Q84 include conditional context-phase readouts. None selects the observer below.

## Exact one-source-mode trace
Take unit oriented edge e1=[0,1] in the 15D carrier, e2=Ae1/2. Then Ae1=2e2, Ae2=-2e1. Exact closed skew flow:
X(s)=cos(2s)e1+sin(2s)e2, ||X||^2=1.
The selected complex modal coordinate is u=<e1,X>+i<e2,X>=exp(2is).
Choose a NEW quadratic observation map F(u)=2u-u^2. Then
z(s)=2exp(2is)-exp(4is) is precisely the screenshot cardioid after t=2s.
Only one native Hodge oscillator is involved; the second harmonic is observer-generated.

## Readout versus dynamics
Native ||X'||^2=4 is constant, whereas |z|^2=5-4cos(2s) and |z'|^2=64 sin^2(s). At a cusp z'=0 but native ||X'||=2. The pullback angle metric is |dz/dtheta|^2=8-8cos(theta), which vanishes at theta=0. Local series z=1+theta^2+i theta^3+O(theta^4).
Therefore a finite-resolution observer can be insensitive near a cusp without source slowdown. This is NOT evidence of physical measurement error or a UD mass/alpha/CMB correction.

## Exact velocity-balance and cusp test
For z=A exp(i p t)+B exp(i q t), z'=0 iff |pA|=|qB| and exp(i(p-q)t)=-qB/(pA).
When the signed integer frequencies have gcd g, the number of stationary events per primitive period is |p-q|/g. A genuine semicubical cusp additionally needs p+q !=0.
Image cases: cardioid 1 cusp, nephroid 2, deltoid 3, astroid 4, ranunculoid 5; the given epitr/hypotrochoids lack stationary cusps.
The cycloid moves by translation (2pi,0) per rotation; it is not globally closed as a planar trace.

## Scoped no-go and independent control
Any affine readout of the unmodified K4 real skew flow is c0+a cos(2s)+b sin(2s), hence an ellipse/line/point, not a genuine cardioid/deltoid cusp.
Glued K_minus/K_plus linear spectra have irrational sqrt(5/3) and sqrt(5/2) ratios, so generic two-frequency linear traces do not close at finite time. Their temporal incommensurability is not a derivation of Penrose spatial quasicrystals.
4096-point independent FFT of the quadratic cardioid has coefficients at frequencies 1,2 only, 2 and -1. A weak observer u+eps*u^2 with eps=1/1000 adds second harmonic of amplitude ratio 1/1000, without a cusp or new native frequency. Eps is a chosen illustrative parameter, not a fitted or source-selected physical coefficient.

## Release boundaries
The complete user download UD_ROLLING_CIRCLE_HODGE_READOUT_v0.1.zip (SHA256 6ec31e7efa5a22c4133549e61fdb06b26660ebf74f6c36526b461082e35a1975) contains exact_replay.py, independent_numeric.py, JSON receipts, full TECHNICAL_NOTE.md, review protocol and full SHA256 manifest. This GitHub branch contains only a smaller text capture. No PNG screenshots redistributed.
No unreviewed source changes, no observable choice adopted, no physical promotion, no website edit. Independent scientific review and full repository integrity CI pending.

Next: derive an S4/locality-compatible source law selecting the modal complex phase plane and polynomial observer from accepted UD measurement dynamics; test a frozen linear-vs-quadratic observer control with independent apparatus covariance before making physics-facing claims.
