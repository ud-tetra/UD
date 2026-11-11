# Intake of submitted R6b review

**REVIEW SUBMITTED; TECHNICAL REVISION REQUIRED; NON-CONSTRUCTOR PROVENANCE UNVERIFIED.** Development — no registry entry. Physical promotion: 0. This is the constructor's response to a supplied review, not another independent review. The supplied bytes are preserved in SUBMITTED_REVIEW.txt. Nothing in an uploaded receipt automatically authenticates its claims, reviewer separation or promotion authority.

## Findings

The submission correctly reproduces the three positive Theta64 eigenvalues as exact fractions, their ranks, and the approximate low roots, channel weight and source profile departure. Its conclusion that physical promotion remains0 is consistent with the packet. However, several purported independent verifications contradict the source equations and evidence.

| ID | Submitted statement | Intake finding and correction |
|---|---|---|
| R01 | N/64 component scaling breaks away from L=4 unless a level congruence holds | **FALSE.** For every L>=3, the implemented Theta edges preserve the first L-3 base4 digits. Every fixed-prefix64-site block is connected by the positive second-cousin edges between its four16-site groups. Therefore there are exactly 4^(L-3)=N/64 components. Fresh enumerations give L=3:1, L=4:4, L=5:16. No mod4 condition occurs. |
| R02 | The displayed unscaled IPR formula gives the frozen F with uniform value1 | **NORMALIZATION MISMATCH.** The displayed formula gives1/64 on64 uniformly occupied sites. The frozen component diagnostic includes the factor64. Thus F_c=64 sum_c |v|^4/(sum_c |v|^2)^2; empty occupied-channel normalization remains undefined. |
| R03 | The complement and stored lambda2 are bounded below by approximately48.75 | **FALSE FOR THE COUPLED MATRIX.** The Theta-only gap cannot be transferred to low-energy rho directions. In any depth1 module q=(ones64/8,0) is unit and orthogonal to both columns of the two-coordinate invariant sector. Its exact energy is v1=49/36864, approximately0.00132921, far below48. Because the negative eigenvector lies in that invariant sector, q is also orthogonal to it; min-max gives coupled lambda2<=v1. The two-column orthogonal complement has codimension2, not1. The valid lower bound used in PR358 is v_min/2 minus the assembly row-sum bound, about0.000664605 in depth1 modules, not48.75. The original proof retains a small positive bound and does not require the stronger false bound. |
| R04 | Positive shift sigma excludes negative eigenvalues; PR352 supplies no negative ground-mode coverage | **FALSE AS A GENERAL RULE AND INCOMPLETE AS A REPLAY DESCRIPTION.** Shift-invert maps lambda to1/(lambda-sigma); the sign of sigma does not exclude negative lambda. For diag(-1,10) and sigma=1/10, the negative root has the larger transformed magnitude. The stored sigma=.00133 probe returned no negative modes, but the separate sigma=1e-8 probe, also positive, returned all4. Both dense outputs also cover all4. The .00133 probe's lack of coverage was explicitly reported, not hidden as a solver defect. |
| R05 | A weighted pairwise variance equals one-half the weighted variance about the mean | **FALSE AS WRITTEN.** For unnormalized weights n_i with total N, sum_(i<j) n_i n_j(x_i-x_j)^2 = N sum_i n_i(x_i-mean)^2. Here N=16. A rational control with n=(1,3,12), x=(0,1,2) gives pair sum87 and weighted variance87/16, not half that variance. For normalized weights the factor is1, not1/2. PR356 uses the correct pairwise identity. |
| R06 | Original acceptance was an absolute residual norm<=5e-12 | **WRONG CRITERION.** The frozen condition is scaled: ||Av-lambda v||/max(1,||A||_infinity+abs(lambda))<=5e-12. PR358 checks that exact squared inequality for all12 low-mode returns over all512 coordinates. The submission conflates residual norms, eigenvalue errors and the scaled threshold. |
| R07 | The assembly operator-norm bound is4.4e-14, and the stored gap exceeds48.75 unconditionally | **UNSUPPORTED SUBSTITUTION.** Approximately4.39648e-14 is the measured ground-eigenvalue shift. PR358 instead uses a certified maximum absolute row-sum perturbation bound of approximately5.818e-14. An eigenvalue shift does not supply an upper bound on the matrix perturbation norm. The stored gap claim is already contradicted by R03; it cannot support an independent Temple calculation as written. |
| R08 | A role declaration establishes independent reviewer separation and reproduced checks | **PROVENANCE NOT ESTABLISHED.** The JSON has a role and self-declaration but no reviewer identity, run artifacts, independent implementation, commands, or output hashes. The quoted schema URI is a declaration, not authentication. Preserve the submitted assertion without treating it as verified independence. |

## Exact counterexample for the coupled gap

Let p=parity/8 and u=ones/8 in a depth1 module. The ground sector is span{(p,0),(0,u)}. Because parity sums to zero within each sibling group, (u,0) is orthogonal to that whole sector. The rho sibling Laplacian annihilates u, and the Theta coordinate is zero, so its cross-term energy vanishes. Therefore

\[
\|(u,0)\|^2=1,\quad (u,0)\perp\operatorname{range}B_2,\quad
\langle(u,0),H(u,0)\rangle=\frac{49}{36864}<0.002.
\]

The complement's minimum Rayleigh quotient is at most this value. This disproves the review's lower bound above48, while leaving the original small-positive-gap proof intact. Since q is orthogonal to the unique negative ground vector, the full module's second eigenvalue is at most the same Rayleigh quotient. A perturbation of order1e-13 cannot raise that coupled gap to48.75.

## What the intake check does and does not establish

`check_objections.py` independently enumerates the declared Theta address relation for L=3,4,5, checks the exact spectrum fractions, constructs the rho Rayleigh counterexample, tests the normalization and weighted-variance identities, and reads pinned PR352/PR358 JSON to verify probe coverage and the actual bounds. It uses standard-library arithmetic and git object reads; no recovered program or eigensolver is executed. CHECKS.json records the source hashes and outputs.

The arbitrary-L component statement above follows by the prefix/connectivity proof, not finite enumeration alone. The general shift-invert objection follows from its rational spectral transformation, not an assertion about an unexecuted solver. The row-sum observation in R07 does not itself prove the exact perturbation norm exceeds4.4e-14; it identifies the certified bound actually available and the invalid inference from one eigenvalue shift to an operator-norm upper bound.

Additional review wording also requires repair: the nonuniformity proof uses positivity of the ground eigenvector of the Schur-reduced L-V(lambda), not just the uncoupled uniform Theta vector. PR355 verifies rational inequalities rather than the PR356 root bisection. The stored depth1 equivalence is established by a rho sign gauge, not by an unspecified hypercubic rotation. Sparse numerical vectors are approximate members of a degenerate spectral family; the evidence does not justify describing them as strictly exact subspace members.

## Disposition and next gate

The uploaded document is retained as a submitted review with revision required. Its all-PASS receipt is not adopted as a verified successful non-constructor review. This intake does not prove the reviewer was involved in construction; it records that separation is not yet substantiated. No custodian decision or CRL promotion is inferred from the uploaded JSON, and no prior source theorem is demoted merely because the review's attempted justification is wrong.

Request a corrected receipt from its reviewer, with identity or stable attribution, non-constructor provenance, per-claim independent methods and reproducible outputs tied to the pinned commits. The reviewer should address R01–R08 explicitly, using the coupled small-gap bound and both sparse probes. Retain correct spectrum/profile calculations and the physical-promotion boundary. A later corrected review must be a new append-only submission, preserving this original.

Review now cannot retroactively blind an already exposed replay. CRL subrungs must be evaluated against their actual requirements; absent physical units or particle correspondence does not by itself bar writing a proposed bridge at2a. This packet has requested no registry promotion. Target-blind pre-exposure registration, action units and particle correspondence remain separate open work.

The unavailable `Gap2_FINAL_Finite_Genesis.png` was not used. Physical promotion remains0.
