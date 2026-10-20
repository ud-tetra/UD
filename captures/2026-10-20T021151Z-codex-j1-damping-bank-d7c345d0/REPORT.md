# Damping-shifted J₁ state bank and joined certificates

The four-state evaluator passes target 0.1 on

\[
\omega\in[4.4915,4.524125],\qquad \gamma\in[0.1,0.1015].
\]

The uniform continuum-plus-evaluation radius is **<0.099509** under the declared IEEE binary64 round-to-nearest, ties-to-even primitive-operation model. Damping width increases from 1/2000 to 3/2000: exactly **3×**. Frequency coverage is unchanged. This is a new conditional mathematical benchmark result, not a physical calibration or native UD law.

## Actual constructed states and fluxes

Both new states use damping 101/1000 and frequency centers9/2 and289/64. Each is an actual saved two-word P2 solve on the same 12,288 tetrahedra with 18,673 degrees of freedom, including boundary nodes. The state audit removes the exact mean and checks mass/stiffness/source identities and a positive reference-mass LDL bound. Corrected finite-Galerkin algebraic error budgets pass 10⁻¹⁰; those algebraic checks alone are not continuum certificates.

Each state receives its own root/patch RT1 flux, with divergence \(z_c\Pi_1 v_c-F\), followed by a global affine-curl correction. Saved coefficients are reconstructed exactly; the cellwise source projection, divergence, all normal traces, global gradient orthogonality, exact norm decrease and degree-three full-P2-gradient cross moments pass. The nonzero cell-meanfree volume residual is included using the rigorous local Poincaré lift. The flux defect cross identities use projected mass; the corrected output uses full P2 mass. No old-state disk is inherited.

| New state | Frequency center | Corrected J, numerical approximation | Exact defect², decimal approximation | New leaf combined radius, outward rounded |
| --- | --- | --- | --- | --- |
| original | 4.5 | (-4.776188312506015-1.1157746619133981j) | 0.0005268259784235149 | <0.099509 |
| neighbor | 4.515625 | (-4.624166757797436-1.0461986423175407j) | 0.0004924267121131217 | <0.093746 |

For each new state, the final checks include 98,304 affine-divergence conditions and 152,064 face/vertex/component normal-trace conditions. Payload corruption, incompatible divergence, incorrect boundary trace and wrong full-mass cross-term controls pass. The saved state and flux replay runs without regenerating coefficients and matches the exact captured results. Sparse floating solves and LSMR propose coefficients; posterior exact identities establish their stated validity. No global least-squares optimality or all-input solver guarantee is asserted.

## Parameter extension and floating audit

For an exact meanfree frozen trial \(v_c\), set \(z=-\omega^2+2i\gamma\omega\), \(z_c=-\omega_c^2+2i\gamma_c\omega_c\), and \(R_c=\sqrt{d_c^2}+\sqrt{\nu_c^2}\). The inherited continuum Poincaré bound \(C_P\le1/2\) and corrected-output identity give

\[
J_z(v_c)=J_{z_c}(v_c)-(z-z_c)\int v_c^2\,d\mu,
\]
\[
|H_z-J_z(v_c)|\le\sqrt{1+(\omega/2\gamma)^2}
\left(R_c+\tfrac12|z-z_c|\|v_c\|_{L^2}\right)^2.
\]

This holds for arbitrary frozen trials and includes their actual residual. It does not assume an exact Galerkin solve. The output mass integral is bilinear, while the residual perturbation uses the Hermitian L² norm.

The new common damping interval is \([401/4000,203/2000]=[0.10025,0.1015]\), with halfwidth \(\rho=17/2000\) in frequency. The damping center is **inside** this interval. Therefore the previous lower-edge-only imaginary-shift formula is replaced by the general endpoint bound:

\[
|\omega^2-\omega_c^2|\le\rho(2\omega_c+\rho),
\]
\[
2|\gamma\omega-\gamma_c\omega_c|
\le2\max\{|g_-(\omega_c-\rho)-\gamma_c\omega_c|,
|g_+(\omega_c+\rho)-\gamma_c\omega_c|\}.
\]

The component maxima need not occur at the same corner; their squared sum is a conservative uniform upper on \(|z-z_c|^2\). The coercivity factor uses frequency upper and damping lower. Exact rational arithmetic and upward square-root bounds establish both new continuous-parameter leaf certificates.

The actual two-input evaluator uses seven coefficient words and sixteen explicit primitive operations per leaf. Its damping shift is \(2[\gamma(\omega-\omega_c)+\omega_c(\gamma-\gamma_c)]\). Constant quantization, including the nonbinary exact damping center101/1000, and every primitive rounding are propagated. The additive underflow term is2⁻¹⁰⁷⁵; propagated magnitudes less than16 exclude overflow. The source AST, extraction and selector are checked. The proof assumes binary64 RN ties-to-even without FMA/contraction; native/software traces supplement it and do not verify every runtime/platform.

The new evaluator's oracle controls compare4,518 represented input-pair traces and72,288 intermediate nodes against the integer-only RN oracle, and verify the exact closed corrected-estimator identity. The prior evaluator's read-only proof is also replayed. Input parameters denote their exact represented float values; neither `float(0.1)` nor `float(0.101)` is asserted to equal the rational damping center. Decimal parsing, measurement uncertainty and physical Hertz calibration remain outside this contract. The wider test box ending at gamma0.104 fails this same conservative envelope, not an actual-error or physical NO-GO.

## Exact four-state join

The new damping interval overlaps the old \([0.1,0.1005]\) over \([0.10025,0.1005]\), width1/4000. The exact damping selector is

\[
\gamma\le411/4096\ \Rightarrow\ \text{previous two-state evaluator};
\quad\gamma>411/4096\ \Rightarrow\ \text{new two-state evaluator}.
\]

The dyadic switch411/4096 lies strictly inside that overlap. Within either evaluator, the unchanged exact frequency switch is577/128. Both branches receive the same unmodified represented inputs and target the same domain/source/metric/measure continuum transfer. Source forcing AST, exact source norm20, topology hash, state parameters and flux-state hash bindings are checked.

Consecutive exact gamma-word indices partition into old and shifted bands without a hole. Both bands cover the same joined frequency-word interval. Their Cartesian products therefore cover the full accepted rectangle. The proof covers 3,970,281,679,914,860,381,671,476,972 accepted binary64 pairs without enumerating them. There are537 supplemental selector-pair controls including both switches and adjacent words. Selection performs no new output arithmetic, so the global radius is the maximum valid leaf radius. Approximate-output continuity/differentiability and blending are not claimed.

## Provenance correction found during construction

The previous neighbor `UPPER_WITNESS.json.gz` contains a copied literal omega label9/2. Its bound `P2_WITNESS.json`, actual `neighbor_flux.py` arithmetic and `UPPER_RESULTS.json` use289/64. The state SHA binding matches. `PROVENANCE_CORRECTION.json` records this mismatch and corrects the label interpretation to289/64; the legacy label must not be treated as parameter authority. Old bytes and numeric coefficients are preserved.

This is one metadata correction found by constructor source audit. It does not regenerate or re-promote the old numerical result. Both new flux witnesses now assert exact omega/gamma equality with their bound states, and the join audit checks state/result/witness consistency. No independent scientific review is claimed.

## Reproduction and scope

Run `PYTHONDONTWRITEBYTECODE=1 python3 replay.py` in this directory. It replays both saved states and fluxes, both new floating leaves, the previous two-input proof, the metadata correction and the exact four-state join. This capture ran each leaf replay separately, in parallel, and also ran the scalar-only root replay; their receipts record those actual commands. The default wrapper composes the same component checks. Coefficient generation is separate. Each source/payload is pinned by hash and the append-only manifest records all files. The Project receipt and screenshot record the persisted research gate. PR/CI/merge completion is recorded separately on GitHub after publication.

Classification: **DERIVED / EXACT CONDITIONAL**, constructor checked. Scientific overall **OPEN**. Development — no registry entry; independent review absent; **physical promotion=0**. The normalized J₁ scalar-wave benchmark retains its externally declared action/source/damping/metric. No material/horn identification, GR/QFT correspondence or native UD constitutive law follows. Full [0,6]×[0.1,1] precision, quantitative mesh termination and the native bridge remain open.

The coefficient ledger v0.39 remains the attached baseline, not a derivation of these benchmark parameters. CRL2 subdivision remains a governance proposal, not enacted by citation. `Gap2_FINAL_Finite_Genesis.png` was unavailable and not read.

**A. CURRENT MISSION TRAJECTORY —** Widen the certified parameter cover with actual state and flux witnesses.

**B. WHAT WAS DONE —** Constructed two states at gamma0.101, certified their new fluxes, replayed the floating estimators and joined the damping bands; recorded a historical frequency-label correction.

**C. FINDING —** [4.4915,4.524125]×[0.1,0.1015] passes with total radius<0.099509 under declared IEEE RN semantics, tripling damping width.

**D. UD GAP IMPACT —** Conditional benchmark coverage advances; independent review, full-band precision, finite termination and native UD bridge remain OPEN. Physical promotion=0.

**NEXT —** Derive adaptive state placement for wider certified coverage and obtain non-constructor review.
