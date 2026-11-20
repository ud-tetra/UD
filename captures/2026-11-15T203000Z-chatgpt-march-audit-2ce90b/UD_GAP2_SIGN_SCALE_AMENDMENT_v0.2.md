# UD Gap 2 — Source-to-scale and running-sign audit

**Artifact:** `UD_GAP2_SIGN_SCALE_AMENDMENT_v0.2`  
**Date of this audit:** 2026-11-15  
**Scope:** independent mathematical analysis of recovered historical Distinction Theory v2.1 Gap 2 sources; developmental amendment only  
**Claim bins:** `EXACT_CONDITIONAL`, `NO-GO_SCOPED`, `NUMERICAL_SOURCE_EVALUATION`, `OPEN_GATED`  
**Registry:** not promoted; non-constructor review not obtained  
**Physical promotion:** **0**  
**Status of historical artifacts:** preserved unchanged

## 1. Sources, authority, and chronology

Exact source bytes are tracked in `UD_GAP2_SIGN_SCALE_CHECK_RECEIPT_v0.2.json`. Main historical records:

- `Gap2_REVISED_Omega_Convergence.md`, **§2** (model, spectrum, scale convention and spectral tilt), **§3** (Planck-backsolved genesis level), **§5** (running), **§6** (remaining independent inputs), **§7** (revised equations).
- `Gap2_FINAL_STATUS.md`, **§1** (later 57-level-fit and original formula falsification), **§3** (measurement gate), **§4** (one undetermined pivot level), **§6** (later revised A.19'').
- `v07_Diagnostic_Analysis.md`, **§§1–2** (original inflation analogy ruled out by v0.7), **§§4–6** (reopen and prediction changes).
- `coherence_equation.md`, **§§1–3** (independent fixed-retention route, not the same spectral map).
- `DistinctionTheory_MasterTheory_v1.md`, **§§5,12** (historical retention and cosmology proposals; no proof that they share the same readout as Gap 2).
- `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, **C02/G05/G06** (internal arithmetic vs physical bridge and source-normalization boundaries).

Current repository boundaries were inspected: `ud-tetra/UD` (`README.md`, `INDEX.md`), `ud-tetra/UD-Site` (`README.md`), and the designated research portal homepage. The public site still states **physical promotion 0** and independent review pending. These later sources do not independently certify the March cosmological inference. The historical files' asserted March date is *not* treated as independent confirmation of their contents' creation time.

This v0.2 artifact supersedes **only** the sign/scale conclusion and expands numerical verification in `UD_MARCH_PROVENANCE_GAP_AUDIT_v0.1.md`. It does not amend the original source files or any frozen mainline registry row.

## 2. Typed objects and explicit assumptions

Let **n** be a dimensionless genesis-level index, **k** a *provisional* model wavenumber, **Ω(n)** the dimensionless recursive integration statistic, **Φ(n)** the coherence statistic, and **P_model(k)** the model's proposed scale power. These are not automatically primordial **dimensionless curvature power** \(\mathcal{P}_{\mathcal{R}}(k_{\rm phys})\), physical time, or a CMB measurement.

Assume for a restricted early-growth epoch:

\[
\Omega(n)=\Omega_\infty-D\rho^n,
\qquad n\ge 0,
\quad 0<\rho<1,
\quad 0<D<\Omega_\infty.
\tag{1}
\]

Assume a *chosen readout*, not a native generator-derived theorem:

\[
P_{\rm model}(k)=\frac{C}{\Omega(n(k))\Phi(n(k))},\qquad C>0.
\tag{2}
\]

For the **base historical calculation**, take \(\Phi(n)=\Phi_0>0\), constant. Define exact scale increment

\[
L=\ln\frac{1}{r},\quad r=4^{-1/3},\quad L=\frac{\ln 4}{3}>0.
\tag{3}
\]

The document supplies \(dn/d\ln k=1/L\), equivalent to one **particular orientation** of a log-linear map. Carry both orientations explicitly:

\[
\ln\frac{k}{k_0}=s n L,\qquad\frac{dn}{d\ln k}=\frac{s}{L},\quad s\in\{+1,-1\}.
\tag{4}
\]

- \(s=+1\): length \(\ell_n=\ell_0 r^n\) decreases with n; model wavenumber increases.
- \(s=-1\): length \(\ell_n=\ell_0 r^{-n}\) increases with n; model wavenumber decreases.

**Source conflict:** §2.3 says both “each IFS level creates structure at a progressively larger scale” (\(s=-1\)) and “earlier levels → larger scales; later levels → smaller scales” plus \(dn/d\ln k=+1/L\) (\(s=+1\)). The current historical source does not uniquely select these contradictory orientation statements. Equation (4) isolates the two branches without silently choosing.

## 3. EXACT — running-sign derivation

Write \(\lambda=-\ln\rho>0\) and \(x(n)=D\rho^n/\Omega_\infty\in(0,1)\). Then

\[
\Omega(n)=\Omega_\infty(1-x),\quad
\frac{d\Omega}{dn}=D\lambda\rho^n>0,\quad
\frac{d^2\Omega}{dn^2}=-D\lambda^2\rho^n<0.
\]

For the chosen constant-\(\Phi\) readout, define \(n_s-1:=d\ln P_{\rm model}/d\ln k\). Applying the chain rule gives

\[
\boxed{n_s-1=-\frac{s\lambda}{L}\frac{x}{1-x}}.
\tag{5}
\]

The second derivative is

\[
\boxed{\alpha_s:=\frac{dn_s}{d\ln k}=\frac{\lambda^2}{L^2}\frac{x}{(1-x)^2} = \frac{D\Omega_\infty\lambda^2\rho^n}{L^2(\Omega_\infty-D\rho^n)^2}>0.}
\tag{6}
\]

**EXACT conditional conclusions** under (1)–(4):

1. \(s=+1\) yields a **red tilt** \(n_s<1\) and **positive** running \(\alpha_s>0\).
2. \(s=-1\) yields a **blue tilt** \(n_s>1\) and **positive** running \(\alpha_s>0\).
3. Reversing only the orientation **cannot** obtain simultaneous red tilt and negative running.
4. The historical expression \(\alpha_s=-(n_s-1)\lambda/L\), as printed, is **positive** for its claimed red tilt. The subsequent assignment of \(-0.0082\) is a sign error even at the document's own approximation level.

The exact branch (s=+1) obeys the additional identity

\[
\boxed{\alpha_s=\frac{\lambda}{L}(1-n_s)+(1-n_s)^2.}
\tag{7}
\]

If one *approximates* \(\Omega(n)\) by \(\Omega_\infty\) in (5), the \((1-n_s)^2\) correction is dropped. That is the origin of an additional discrepancy between exact and approximate magnitudes.

**NO-GO_SCOPED:** *Within* assumptions (1)–(4), simultaneous \(n_s<1\) and \(\alpha_s<0\) is impossible. This is **not** a universal no-go for all possible UD genesis dynamics, scale maps, or Φ evolution.

## 4. NUMERICAL — historical source parameter audit (not predictions)

All displayed decimals in this section are source-reported fitted values or measurement-facing calculations, not new native constants. In particular, \(n_s=0.9649\) below was **supplied as a historical comparison target**, not predicted by UD.

| Check | Recovered early-fit stratum \(\rho=0.898,\ \Omega_\infty=1.10,\ D=0.477\) | Later final-status stratum \(\rho=0.891,\ A=0.051\) |
|---|---:|---:|
| Prefactor \(A=D\lambda/(\Omega_\infty L)\) | ≈0.100959 | A≈0.051 supplied; D, Ω∞ not jointly supplied |
| n inferred from \(n_s=0.9649\) under **approximate** \(n_s=1-A\rho^n\) | ≈9.82023 | ≈3.23734 |
| n inferred using **exact** equation (5) | ≈11.12546 | Not identifiable without \(D/\Omega_\infty\) |
| Approximate \(\alpha_s\) at target | **+0.008172** | **+0.008766** |
| Exact \(\alpha_s\) for early source at target | **+0.009404** | Not identifiable from the reported later parameters alone |
| Historical claimed running | \(-0.0082\) | approximately \(-0.008\) to \(-0.010\) |

Two historical numbers previously presented as “9.8 ≈ 11.1” are **not interchangeable rounding results**. The first arises from approximating the denominator by \(\Omega_\infty\); the second arises from retaining \(\Omega(n)\). Their agreement with a supplied target proves neither cosmological generation nor mode freezeout.

Independent symbolic differentiation and high-precision central differences both return \(+0.009403956\) for the exact early-fit branch at its backsolved pivot. They also return positive running after orientation reversal (with blue tilt \(n_s=1.0351\)). The executable receipt contains full values and exact source SHA-256 hashes.

**Additional historical data check:** `Gap2_REVISED_Omega_Convergence.md` §2.1 lists \(\Omega(0)=0.674\) and \(\Omega(1)=0.626\); therefore its accompanying phrase “Ω increases monotonically” is not true over all nine listed levels. Fit-based convergence and raw monotonicity must be assessed separately. `Gap2_FINAL_STATUS.md` is a later fit over 57 levels, not a replacement for these exact raw-table entries.

## 5. Separate fixed-coherence route — keep typed provenance

`coherence_equation.md` §3 defines a *different* model formula:

\[
\eta=\frac{61}{62},\qquad n_s=1+\frac{\ln(61/62)}{L}\approx0.964812.
\]

**EXACT conditional:** If this \(\eta\) is constant with scale, this separate formula gives **\(\alpha_s=0\)**, not negative running. It does not resolve Gap 2 by being numerically close to an observed scalar index. Linking it to the Ω model would require a typed evolution/readout that actually derives \(\eta(k)\) or another scale dependence. It is not valid to combine the \(61/62\) ratio with \(\Omega(n)\) simply because their numerical outputs are close.

## 6. Candidate routes that would change the no-go assumptions (OPEN)

These are **ways to formulate discriminating tests**, not repairs declared successful:

**A. Derived scale-dependent coherence:** retaining \(\Phi(n)>0\) and the log-linear map gives

\[
\alpha_s=-\frac{1}{L^2}\frac{d^2}{dn^2}\ln\big[\Omega(n)\Phi(n)\big].
\]

For negative running, a necessary-and-sufficient pointwise condition under that map is

\[
\boxed{\frac{d^2\ln\Phi}{dn^2}>\frac{\lambda^2x}{(1-x)^2}.}
\tag{8}
\]

For red tilt with \(s=+1\), also require \(d\ln(\Omega\Phi)/dn>0\). No source-derived \(\Phi(n)\) trajectory satisfying both has been supplied.

**B. Derived nonlinear mode-creation map:** let \(t=\ln(k/k_0)\) and take \(n=n(t)\), rather than assuming (4). For constant Φ,

\[
\alpha_s=\frac{\lambda^2x}{(1-x)^2}(n')^2 -\frac{\lambda x}{1-x}\,n'',
\]

where primes now denote derivatives w.r.t. \(t\). Negative running requires

\[
\boxed{n''>\frac{\lambda}{1-x}(n')^2.}
\tag{9}
\]

For red tilt also require \(n'>0\). This is a **test target**; it cannot be introduced as a fitted correction to reproduce an observed sign.

**C. Different source power readout:** deriving a genuine primordial observable from source amplitudes, correlation functions and transfer dynamics may invalidate (2). That would define a new scoped prediction. An arbitrary power-law prefactor inserted to force a desired \(n_s\) or \(\alpha_s\) is prohibited.

## 7. Physical source-to-scale bridge gates (OPEN_GATED)

| Layer | Source object | Missing map/test |
|---|---|---|
| Finite dynamics | \(a_i(t_{\rm step})\), \(\Omega(n)\), \(\Phi(n)\) on 80×80 triangular graph | Reproducible trajectory, initial/boundary conditions, update law and raw traces |
| Mode creation | \(n\mapsto\ell_{\rm graph}\) and \(n\mapsto k_{\rm graph}\) | Dynamical selection of orientation \(s\), mode freeze or other creation/readout rule, not just assumed IFS packing ratio |
| Growth and power | Discrete 2D amplitude Fourier power \(|\widehat{a}(k)|^2\) | Distinguish model 2D PSD from 3D primordial **dimensionless curvature power** and identify required normalization/transfer |
| Physical wave-number | \(k_{\rm graph}\to k_{\rm physical}\) | Grounded scale/unit map, background evolution and pivot identity (Mpc\(^{-1}\) if CMB-facing) |
| Physical time | Genesis-event counts / oscillation cycles | Independent clock calibration; “~51 simulation steps per level” is not an SI clock |
| Independent confirmation | Original model versus null & alternatives | Target-blind or freshly held-out tests, error propagation, independent replay and non-constructor adversarial review |

The historical simulation had a **fixed 2D lattice**, as explicitly acknowledged in `v07_Diagnostic_Analysis.md` §2.2. In particular it had no sourced cosmological horizon-crossing/freezeout mechanism. `Gap2_FINAL_STATUS.md` §1 reports that its direct late-time \(P(k)\) measure had a nonlinear slope near -2.5 and could not resolve the hypothesized primordial tilt; do not silently treat that as \(n_s-1\).

**Physical promotion = 0** for all March cosmological claims, including the original inflationary formula, the revised negative-running claim, and the fixed-retention near-observed number.

## 8. Append-only amendment proposed for current ledger

**Claim ID (new local development label):** `UD-GAP2-SIGN-SCALE-v0.2`  
**Provenance:** recovered historical v2.1 mathematics + independently executed symbolic and finite-difference verification  
**Proof status:** `EXACT_CONDITIONAL / NO-GO_SCOPED`  
**Review:** `SELF_CHECK_ONLY`, independent reviewer not assigned  
**CRL:** development lane, not registry promotion; if submitted as a bridge proposal it is at most `CRL-2a`  
**Dependencies:** the assumptions (1)–(4) and source files listed in §1  
**Obstruction:** red tilt plus negative running impossible under fixed-Φ exponential Ω and affine log-k map  
**Unblocked:** alternate sourced Φ evolution, sourced nonlinear n(k), or different physical readout are not refuted  
**Original negative-running statement:** `AUTO_FREEZE_FOR_CURRENT_REUSE` / retain historical text, correction required before any new manuscript import  
**Reopening:** explicit alternative state/evolution/readout with frozen assumptions, sign calculation, null comparison and independent evidence.

**Suggested non-destructive replacement paragraph for any future manuscript (not yet applied):**

> For the early-epoch exponential Ω convergence \(\Omega(n)=\Omega_\infty-D\rho^n\), a constant-Φ source spectrum \(P\propto1/\Omega(n)\), and log-linear creation map \(k_n=k_0r^{-n}\), the internally implied tilt is red but its running is positive, \(\alpha_s= D\Omega_\infty(\ln\rho)^2\rho^n/[\ln(1/r)^2(\Omega_\infty-D\rho^n)^2]\). The historical negative-running inference is therefore withdrawn under these assumptions. Any revised negative-running candidate must separately derive coherence evolution, a nonlinear scale map or a new physical power readout, and independently qualify a cosmological correspondence.

## 9. Verification and limitations

Run:

```bash
python UD_GAP2_SIGN_SCALE_INDEPENDENT_CHECK_v0.2.py
```

The script uses SymPy differentiation as one method, high-precision mpmath central differences as a second method, and exact identities for orientation invariance. Its JSON receipt gives precise historical evaluations and SHA-256 hashes of the analyzed source bytes. **No original simulator was rerun**, no historical data were invented, no empirical unit map was developed, no independent non-constructor review occurred, and no GitHub or website record was modified in this audit.

## 10. Mission outcome

- **A — CURRENT MISSION TRAJECTORY:** Close conditional mathematics before attempting a calibrated primordial CMB correspondence.
- **B — WHAT WAS DONE:** Verified the running, separated orientation and exact/approximate formulae, and specified admissible source-to-scale alternatives.
- **C — FINDING:** Early-epoch exponential Ω with constant Φ has positive running in either scale orientation; historical negative-running claim is algebraically unsupported.
- **D — UD GAP IMPACT:** Gap 2 mathematical sign ambiguity closed as an exact conditional no-go; the cosmological bridge and independent scale map remain open.

**Recommended next step (priority 97/100):** source-derive a mode-production rule and scale-dependent \(\Phi\), then test (8) against raw linear-regime spectra before allowing a new running prediction.  
**Independent supporting workload (priority 92/100):** retrieve and replay v0.7/v0.7b/v0.7c raw traces, fit with frozen windows and compare against nulls; no cosmological promotion absent the CMB-facing map.
