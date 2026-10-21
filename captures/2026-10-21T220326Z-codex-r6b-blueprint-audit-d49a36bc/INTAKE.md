# Review blueprint010: implementation defects and corrected audit requirements

**BLUEPRINT RECEIVED; CERTIFIED PAYLOAD AUDIT STILL OPEN.** Attribution remains Devin Ramos, user-attested non-constructor, with AI assistance. This is a constructor intake and counterexample run. Physical promotion0; development — no registry entry.

The submission retains the resolved script-hash explanation, retracts the unsupported sample precision claim and keeps C07/C08 OPEN. Those scope repairs remain useful. The proposed new code, however, does not yet implement the corrected audit correctly.

## 1. Manifest loader does not match the evidence

The actual EVIDENCE_INDEX.json has top-level keys base_commit, upstream, source_files, physical_promotion and execution_allowlist_note. File entries are under upstream[].files. `manifest["files"]` raises KeyError on this index.

There are44 inventoried files across six captures, with six upstream manifests and three source files separately pinned. The two array container paths are PR352's INPUTS.npz and NUMERICAL_PAYLOAD.npz. There are no standalone .npy inventory paths. The proposed .npy-only filter therefore cannot return the stored matrices. Verify the container bytes against the declared hashes, load with pickle disabled, inspect the named NPZ arrays and validate their shape, dtype and matrix-hash bindings. Do not interpret a file extension as proof of content or collapse a basename across captures.

## 2. Concrete false enclosure from cancellation

The proposed function computes the explicit residual vector, then discards it when computing variance as `dot(Av,Av)-theta**2`. That subtraction can lose the whole variance.

The supplied function was extracted, inspected and run on

\[
A=\begin{pmatrix}1&10^{-9}\\10^{-9}&2\end{pmatrix},\quad
v=(1,0)^T,\quad\beta=2.
\]

It returns theta=1, variance=0, residual norm=0, scaled residual=0 and interval[1,1]. But the explicit residual is (0,1e-9), so its squared norm is exactly1e-18. The true ground eigenvalue is strictly below1: the characteristic polynomial at1 is -1e-18, with one root on each side of1. The next eigenvalue is above2, so beta2 is valid. The returned point interval therefore excludes the true ground despite satisfying the stated gap precondition.

Use the residual directly, s²=(r^T r)/(v^T v), after theta=(v^TAv)/(v^Tv). Even direct floating residuals need roundoff bounds for a certified tiny interval; exact fractions of stored binary64 values or outward interval arithmetic are appropriate. Clamping a negative variance to zero cannot establish an enclosure, and this code also uses unclamped eta_sq in its interval width.

With a justified **absolute lower bound beta on the next eigenvalue**, the original ground enclosure is [theta-s²/(beta-theta),theta]. The code's symmetric interval can be a looser enclosure under exact valid arithmetic, but doubles its width and does not repair invalid variance. Do not conflate beta with a distance/gap measured from the ground.

## 3. The frozen residual check has changed

The original acceptance rule uses each stored full512-coordinate vector and its stored solver return:

\[
\|Av-\widetilde\lambda v\|/
\max(1,\|A\|_\infty+|\widetilde\lambda|)\le5\times10^{-12}.
\]

The blueprint instead checks a normalized module vector against its Rayleigh quotient and the module norm. That is a useful separate diagnostic, but it does not reproduce the frozen test. Preserve the stored vector and full matrix for that original check. Compute Rayleigh variance separately for the module-specific certificate, accounting for any vector projection and inter-module tails.

The returned `abs(lambda_solver-theta)` measures solver-to-Rayleigh discrepancy, not certified error to the true eigenvalue. Compare the return to the certified interval, or include its discrepancy plus the enclosure radius when giving an error bound.

## 4. Module map, lower bounds and structural zeros

Source first-digit labels are module0 varying depth and modules1,2,3 depth1. The blueprint uses a different numbering without a permutation map. Any alternative order must explicitly map to global coordinate indices.

The trial vector q supplies an **upper** bound lambda2<=v1; it does not prove a positive lower bound. The valid lower bound comes from the codimension-one quadratic-form/min-max argument, followed by the exact perturbation bound. PR358 already records a beta for each full128-coordinate module, including its complement. Positive eigenvalues of a32- or6-coordinate quotient alone do not bound the full complement.

Exact absence of cross-module stored entries is checked directly in PR358. A small row-sum perturbation bound does not imply those entries are exactly zero; it permits small nonzero terms. Confirm the cross-block bytes before using blockwise spectral certificates.

## 5. Reproduction path and disposition

CHECKS.json reproduces the cancellation counterexample and verifies the actual index layout against its pinned snapshot. The checker executes only the manually inspected pure numerical function extracted from this submission. It does not execute the document's runtime instructions or adopt its GR/QFT comparison table as a physical correspondence.

The existing [PR359 review packet](https://github.com/ud-tetra/UD/pull/359) already includes a pinned reproduction harness covering all44 inventoried files, separately pinned sources, and seven explicit constructor verifiers. A non-constructor may run that harness, inspect the underlying proofs and provide attributed output, with any additional independent implementation clearly identified. This supplies a concrete route without requiring a new, incorrectly scoped loader. Running constructor verifiers does not by itself constitute an independent proof review or earn promotion.

This document is an intake of a proposed method, not Receipt004 or a completed independent payload audit. C07/C08 remain OPEN in the review. Original PR358 constructor evidence remains scoped as before. No source edits, reviewer messages, upstream merges, custodian rulings or registry promotions occur. The missing `Gap2_FINAL_Finite_Genesis.png` was not used.
