# Whole-ball shift bounds and fixed-basis least-squares obstruction

**A priori residual bounds are proved over the full declared encoded ball, with explicit quality/normal-equation premises. They do not establish universal v2 admission. The directed saved basis cannot pass the old shift gate even with exact least squares. The external review request has been sent; outside acceptance/review remains PENDING.**

## Whole-ball bounds

For every input within the encoded per62-vector2^-48 ball, the following are certified upper bounds on the exact least-squares raw shift residual, conditional on each row's stated SVD quality:

| Basis/quality premise | Uniform exact-LS residual upper |
|---|---:|
| Ideal exact top209 SVD basis |<2.309064e-9|
| Returned basis, abstract operator-only approximation certificate |<6.933911e-9|
| Returned basis, actual parent Frobenius-derived full-factor certificate |<2.629186e-9|

The published v2 shift allowance lower is approximately5.563206409135e-10. These upper bounds exceed it. Therefore THIS sufficient whole-ball admission proof remains HOLD, even at zero normal-equation error. This is not a lower bound on the true worst case and not an exhibited v2 failure. All prior finite v2 PASS results and original v1 HOLDs remain unchanged. No gate or radius was changed to obtain a different verdict.

## Exact and floating least squares

Let A=Uminus, E=Uplus-A*T and N=A^T E for the actual returned finite real shift. Theorem proofs give an exact-LS residual upper J and positive singular lower a_min. Exact projection orthogonality yields

\[
 ||E||_F^2=||E_*||_F^2+||(A^\dagger)^TN||_F^2
 \le J^2+(||N||_F/a_{\min})^2.
\]

Thus a uniform normal-equation ceiling nu would give the returned-output bound sqrt(J^2+(nu/a_min)^2). Such a ceiling is an explicit additional premise, not an unproved global LAPACK/BLAS guarantee. Projection/SVD quality alone cannot bound arbitrary returned T: tI yields unbounded residual on a full-rank basis.

The frozen grid has two illustrative normal ceilings,0 and2^-45. The actual three saved normal residuals are slightly ABOVE2^-45 (approximately2.875e-14 to3.079e-14). They are NOT claimed to satisfy that illustrative ceiling. Their separate certificates use their individually verified exact-dyadic normal residuals.

## Actual saved-output diagnostic

New exact integer Gram/cross-Gram computations re-evaluate the three PR215 saved bases/shifts; no new SVD, fit, raw generation or raw acquisition is executed. All pinned array/package bytes are checked. Exact squared residuals are retained, with no subtraction of uncharged floating matrix products.

| Saved case | Exact-LS minimum residual lower | Raw returned residual upper | Old gate unattainable on this basis? |
|---|---:|---:|---|
| rotating_checker |>5.6554288575e-11|<5.6554296458e-11|Not proved; original PASS remains|
| block128 |>5.3192200106e-11|<5.3192208288e-11|Not proved; original PASS remains|
| directed_period4 |>3.3486132964e-10|<3.3486133114e-10|**YES**|

The old gate is2^-34≈5.82076609135e-11. For directed_period4 every real shift matrix on THAT saved basis violates the old Frobenius gate. The basis is fixed; this does not prohibit another basis, another estimator or v2. It shows that making this shift solve exact cannot repair this specific old-policy HOLD.

The LS residual-component discrepancy from exact minimization is at most3.160e-14 in Frobenius norm for these saved outputs. This is a component bound; the report does not confuse it with the smaller possible improvement in the scalar residual norm.

## Norm semantics and provenance

THEOREMS.md proves that the parent's exact residual/polar formula actually bounds Frobenius approximation error: Gram defects are Frobenius norms and singularvalue polar corrections sum in squares. The stronger row is tied to THAT verified helper; it does not infer equal Frobenius and operator norms. With an abstract operator-only certificate the projected error explicitly pays sqrt209. Baseline r is itself an exact cross-Gram Frobenius residual; the input noise Frobenius bound follows from the pervector model and sketch norm. Source constants and prior factor certificates remain explicit dependencies.

FREEZE.json binds source inputs, code, theorem text and same-team design review before these new bounds/normal calculations; saved case outcomes were already known. There is no blinded preregistration claim. Four exact/refusal controls test two scaled least-squares fixtures, singular-margin refusal and altered-source hash refusal.

## Portable replay

With the repository and requirements.txt available, run

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python replay.py --repo /absolute/path/to/UD --out /absolute/path/to/new-review
```

The wrapper hash-checks the pinned PR215 root manifest and all members, safely extracts its ten archives, checks package/array bytes, recomputes all12 bound rows, all3 normal-equation certificates and four controls. Parent full-factor/eligibility proofs are pinned dependencies; this command does not silently claim a new fullfactor/rawprojection execution. The output directory must be new. The clean replay receipt/logs are included when published. The three large saved witnesses are not duplicated in this capture; use their immutable parent archives.

## Review and governance

The authorized prepared request was sent to Siegfried M. Rump on19October2026. CONTACT_STATUS.json records only public project contact/scope; private sender/mailbox identifiers/headers are excluded. A sent request is not delivery/read confirmation, acceptance or an attributable external review. No favorable verdict or independent execution is invented.

Development — no registry entry. Same-team design/final reviews do not satisfy outside independence. Physical promotion0. Numerical gates/ceilings remain O03 protocol controls. No universal floating solver admission, physical/SI frequency identification, full-Hankel/native1893 claim, apparatus qualification or recovery of the nominal747-dimensional observer kernel is established.

A supplemental direct-data certificate removes source/noise/SVD-quality premises from the fixed-basis old-gate obstruction: exact Gram margin and exact rational LS lower comparison are independently re-expressed and retained in DIRECT_GRAM_CERTIFICATE.json and DIRECT_THEOREM.md. For the full primary-plus-supplement replay, use `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python replay_all.py --repo /absolute/path/to/UD --out /absolute/path/to/new-review`. The primary replay.py remains available with its narrower original scope.
