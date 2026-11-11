# UD polarity pipeline synthetic consistency audit v0.1

**13 October 2026 UTC · development; no registry promotion; physical promotion 0.** Constructor and adversarial self-check: Codex. This is an exact, source-free synthetic audit of the user-supplied polarity pipeline, **not** execution of its frozen blinded multi-model sidecar or an empirical result. Independent non-constructor review remains pending.

## 1. Source binding and unavailable endpoint

The user-supplied statement declares `Theta={0,1}^3`, `q=1-theta`, integrity `T`, latent support `L=1[R>0]`, viable obligation `omega=T L`, a finite continuation index, POC-1 saturation `q=omega`, signed reversible support flux, and a burden address selector. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`), Q165–Q173, supports the typed fixed-complex squared chain support and skew-incidence flux; it does not supply a constitutive parity response. The later Library source `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.65_C3_7_CLOSURE_N1_N2.json`, Q210, explicitly records closed-carrier obligation nonidentifiability; Q271 and O43–O45 record the pretarget multi-model registry and primary firewall. These are source statements, not fresh physical validation.

The already-existing Library theorem `UD_VIABLE_LANE_INDEX_PLUS_IDLE_RESPONSE_INDEX_THEOREM_v0.1.md`, theorem and saturated-prior corollary, proves the idle-response correction and reports 15,625 admissible ordered pairs. This audit independently replays that finite identity and tests how the proposed combined procedure uses it. The versioned `THREE_LAB_SIDECAR_DISTRIBUTION_RECEIPT_v0.1.json` records distribution of `UD_POC1_BLINDED_MULTI_MODEL_RESPONSE_SIDECAR_v0.1_RELEASE.zip` with SHA-256 `531ce192c26dd6962c5838e84b379c2be7cbfa936216320bf0666aae6d47b04a`, but the actual zip, target records, and held-out endpoint data were not found in the supplied workspace, current `ud-tetra/UD` repository, or available Library title search. Its distribution status is later than the v0.58 ledger's O45 pre-distribution status; this is a **versioned status difference**, not evidence of a scored endpoint. No sidecar score is claimed.

Carrier typing: `omega` is a 3-bit obligation receipt; `q` is a 3-bit open-pair response; `theta=1-q` is the closure mask. `T` is a hard-integrity 3-bit input and `L` a pre-gate positivity receipt. All Hamming counts are integers. Chain `c` and burden `b` are separate real vectors; integrated `G^S` is dimensionless squared chain amplitude on the fixed `K4` carrier, not physical time or energy. The index is an algebraic property of two already specified obligation spaces; its predictive content comes from sourcing the *future evaluation-step pre-event* `omega_n`, plus an independent response law.

## 2. EXACT idle-response correction and full-domain enumeration

For each coordinate, admissibility is `omega=T L`, `omega<=q<=T`. There are five `(T,L,q)` states per coordinate and therefore `5^3=125` complete states. Write `h=q-omega`, a nonnegative idle-open bit vector. For **frame-aligned** old receipts and new receipts,

\[
\mu_\Theta=|q^-|-|q^+|
=\bigl(|\omega^-|-|\omega^+|\bigr)+\bigl(|h^-|-|h^+|\bigr)
=\operatorname{ind}F_\omega+\nu_h.
\]

The last equality `ind F=dim L^- - dim L^+` holds for **any** linear map between these finite obligation spaces; it does not identify a causal continuation map or independently force `h=0`. Across all `125^2=15,625` ordered admissible pairs, the code finds index equal to full `mu` in **6,545**. An independent combinatorial check counts states by idle-bit weight `h=0,1,2,3` as `(64,48,12,1)`, so the equality count is `64^2+48^2+12^2+1^2=6,545`. With a saturated old state, there are `64*125=8,000` ordered pairs; index equals full `mu` in exactly `64^2=4,096`, precisely the cases where the new response also saturates. This recovers the existing theorem's scope. **No new theorem promotion is sought.**

## 3. EXACT address-selector inconsistency if POC-1 is binding

Take `T=(1,1,1)`, `L=(1,0,0)`, so `omega=(1,0,0)`. Let old and new obligation receipts agree; the index and target Hamming change are zero. With POC-1, `q=omega` fixes `theta_POC=(0,1,1)` and target weight 2. On one burden snapshot with `b=(0,1,2,3)` and opposite-edge pairs `A=(01,23), B=(02,13), C=(03,12)`, the declared quadratic-gradient construction gives `W=(2,8,10)`.

The posted burden optimizer, restricted **only** to weight 2 and its written integrity condition `q<=T`, gives the unique minimizer `theta=(1,1,0)` with cost 10. POC-1's mask has cost 18. The minimizer closes the required `A` lane (`q_A=0<omega_A=1`) and therefore violates viable completeness. If the admissible set is repaired to require `omega<=q<=T`, its weight-2 shell contains only `theta_POC`; burden minimization is then redundant. **NO-GO under the stated conditions:** POC-1 saturation and a nontrivial, independently address-selecting burden optimizer cannot both be the final response rule on this example. The burden diagnostic may remain a separate test or an explicit alternative response model, without modifying the frozen primary POC-1 verdict.

## 4. EXACT fixed-K counterexample to universal flux-index agreement

Use the sourced filled-tetrahedron skew flow `c'=A_K c` from the unit vertex state `c(0)=e_0`, with all other initial degrees zero. With `m=(1,1,1,1)/4`, the exact solution in the vertex/gradient-edge sector is

\[
c_0(s)=m+\cos(2s)(e_0-m),\quad
c_1(s)=\tfrac12\sin(2s)B_1^Te_0,\quad
E_1(s)=\|c_1(s)\|^2=\tfrac34\sin^2(2s).
\]

Let the previous and current pre-event evaluation instants be `s_a=pi/12`, `s_b=pi/6`, with unchanged integrity `T=(1,0,0)`. Pair A has the active edge 01 and nonzero endpoint vertex amplitudes throughout this interval, so `R_A>0`, `omega_A=1`; B and C are disabled. Thus `omega^- = omega^+ = (1,0,0)`, and the POC-1 response is unchanged: `mu_index=mu_Theta=0`. But by the exact fixed-K edge-support identity,

\[
G_{\Sigma}^{S\pm}=E_1(s_b)-E_1(s_a)=\tfrac38>0,
\qquad G_A^{S\pm}=\tfrac18>0.
\]

The proposed monotone sign rule would assign `mu_flux=-1`. This is a genuine one-viable-pair, pre-event case; hard integrity suppresses B/C obligations while their reversible chain support may still flow. **NO-GO under unchanged T and this native flow:** signed support change alone is not a universal equality constraint on the discrete obligation index. It may be a separately scored directional diagnostic on a more restrictive declared domain. Calling a disagreement an automatic hold is a possible new controller rule, not a prediction from the index equation.

## 5. Frame provenance and corrected execution scope

The cardinal index is unaffected by relabeling, but address-level closures/reopenings are not. If an old A obligation persists as a new B obligation under an A↔B frame permutation, transporting `omega^-` before comparing gives zero toggles. Comparing untransported `omega^-=(1,0,0)` with `omega^+=(0,1,0)` instead reports one false sink and one false source (turnover 2). The source law for `r_n` must therefore act on both `theta^-` **and the old obligation receipt** before computing coordinatewise `c_Theta,o_Theta`; counting dimensions alone does not supply this correspondence.

**Disposition:** **EXACT** finite admissible-state identity, its independent count, a burden-selector counterexample, a fixed-K flux counterexample, and frame-address example. **CANDIDATE** POC-1 as the constitutive no-idle selector, signed flux as a scoped diagnostic, and any repair to burden/address priority. **NO-GO** universal flux-index equality and nontrivial burden selection under binding POC-1 on the stated domains. **OPEN** source-derived response semantics, pre-event frame receipt, distribution package access, frozen sidecar replay, held-out scoring, independent review, and physical correspondence. Physical promotion 0.

Run `python3 verify.py` to regenerate `results.json`; only Python's standard library is used. The synthetic cases were selected to challenge the supplied claims. They are development tests, not a blinded external sidecar score or a post-hoc replacement for any previously frozen protocol. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not used.
