# Apparatus-facing contract design review

Development — no registry entry. Physical Promotion=0. This is a same-team mathematical and protocol design review; no physical acquisition, independent non-constructor review, or new estimator run is represented.

## Boundary of the claim

The current anchor is a pinned synthetic209-clock temporal family and a321-column projected sketch. The37 preparations and62 channel coordinates have a declared order and model-coordinate normalization. The current temporal record uses nominal index step1 and clocks t_a,k=o_a+(1+eps_parity)*k+jitter_parity*(-1)^k. Historical h=1/32 belongs to the separate six-ratio calibration lane; it is not the current history sampling interval. The older native1893 history contract has its own normalized-step1/2 and candidate raw16/33 conventions, which must remain distinct. None of these model parameters is an apparatus time interval until separately calibrated. The2^-48 encoded-vector radius is a model-coordinate input contract, not an SI measurement tolerance. A separately derived larger raw-input noise budget for source-family excitation/tail separation, if certified, remains a separate order-only lane; it does not extend measured-frame/phase admission. The unchanged retained-Gram, normal, measured-frame and shift caps remain finite saved-output gates. Neither a missing apparatus calibration nor model mismatch may be hidden by changing these caps. No2^-49 residual gate is reinstated; the2^-38 shape gate is not repurposed as a shear or acquisition norm.

## Mandatory frozen evidence and fail-closed admission

A proposed apparatus record must name and hash the raw bytes, acquisition identity, source-model/anchor version, decoder and channel map, calibration receipts, preparation and validation partition, units and frozen decision rules. A complete string or checked boolean is not itself calibration evidence.

The decoder must specify all62 source coordinates, raw channel identifiers/order/signs, gain and offset maps, crosstalk/nonlinearity allowance, saturation/dropout rules, ADC quantization, sensor bandwidth, signal ranges and coordinate units. Gain/offset uncertainties must be valid over that same amplitude and temperature/range domain. Unmapped/duplicated channels, saturation, missing finite uncertainties, negative budgets, inconsistent units or uncertain calibration domains are HOLD before numerical acceptance.

The timebase must identify oscillator/reference calibration, physical unit, model-to-apparatus conversion, sample interval, preparation-specific origin/rate errors and bounded residual jitter, synchronization conventions, timestamp resolution and valid duration. Anti-alias evidence must include the independently specified input band, sampling/filter transfer and uncertainty, and injectivity/separation of the admitted two-step targets. Unknown stopband energy is an unbounded acquisition error, not a zero entry. Missing time/anti-alias evidence gives HOLD even if a synthetic phase matcher passes.

The preparation ledger must identify intended preparation operator, measured implementation relative to an independently pinned anchor, uncertainty domain, every raw source dependency and acquisition run. Preparation identity/provenance must not be inferred solely from successful fitting. The noise ledger must distinguish deterministic uniform bounds from confidence intervals, identify confidence level and simultaneous coverage if probabilistic, and retain possible bias/correlation. Independent channel or preparation noise is not assumed.

## Deterministic acquisition budget

Let Yhat denote decoded measured coordinates and Ytrue the unknown noiseless apparatus coordinates in the same declared model-coordinate system, with Nvec finite62-vectors. A valid per-vector deterministic bound ||Yhat_v−Ytrue_v||2<=delta_v gives

alpha_raw=sqrt(sum_v delta_v^2), and alpha_Z<=kA*alpha_raw,

where kA is a validated upper bound for the actual fully normalized sketch operator norm. Under a uniform delta, alpha_Z<=kA*sqrt(Nvec)*delta. For the existing real sketch Aint/128, its raw-input quantum normalization must be applied exactly once; using Aint without its denominator would change the bound. Channel/preparation unfolding is a permutation and preserves Frobenius norm. Sketch errors are Frobenius bounds; they are not guaranteed209-dimensional coordinates or new physical information.

A safe decoder component bound for yhat=Ghat*zobs+bhat and ytrue=G*ztrue+b, with ||G−Ghat||2<=dg, ||b−bhat||2<=db and ||zobs−ztrue||2<=dz, is

decode_error<=dg*||zobs||2+(||Ghat||2+dg)*dz+db.

The gain units convert code units to the explicitly stated coordinate unit. Add separately justified saturation/nonlinearity/crosstalk/filter-tail errors. Deterministic terms add by the triangle inequality; quadrature is not justified solely because the terms have different names.

For an intended preparation operator That and true T relative to fixed anchor Yanchor, an independently justified ||T−That||2<=dp implies ||(T−That)Yanchor||F<=dp*||Yanchor||F, with orientation adjusted to the saved convention. Same-clock-parity support must be part of the declared source family. Do not infer a preparation norm or fixed-sketch conditioning from orthogonality alone. Uncertain or unmeasured anchor amplitude makes this bound unavailable.

For a declared source waveform y_a(t)=b_a+sum_j[A_ja*cos(theta_j*t)+B_ja*sin(theta_j*t)], one valid finite derivative bound is L_a=sum_j|theta_j|*sqrt(||A_ja||2^2+||B_ja||2^2). Then timing error contributes at most L_a*|dt_ak| per vector. Under dt_ak=do_a+k*de_a+u_ak, use |do_a|+k*|de_a|+|u_ak| with a frozen finite horizon. Physical seconds may enter only after converting them through a calibrated model-time scale. The spectral/Lipschitz bound is conditional on this declared source model; it is not a theorem for an arbitrary apparatus signal.

These components can enter one conservative budget only when they bound disjoint terms of a displayed record-error decomposition. Preparation/clock deviations deliberately being tested as model mismatch must not also be subtracted as acquisition uncertainty. Large uncertainty can produce HOLD; it cannot create falsification evidence.

## Model-mismatch decision rule

Freeze a prediction Ymodel independently of the scored record. In raw or projected coordinates, let r=||Yhat−Ymodel||F and let alpha rigorously bound ||Yhat−Ytrue||F in that same space. The unobserved mismatch m=||Ytrue−Ymodel||F satisfies

max(0,r−alpha)<=m<=r+alpha.

Given a nonnegative predata mismatch cap c with the same units: PASS only if the validated upper r+alpha<=c; FALSIFY_FROZEN_CONTRACT only if the validated lower max(0,r−alpha)>c; otherwise HOLD. Missing provenance/calibration is HOLD before this test. An inconclusive interval comparison is HOLD. Falsification applies to the stated frozen model/protocol under its admitted calibration assumptions, not to every UD construction. A diagnostic cap cannot be selected using validation outcomes.

## Honest held-out validation

Disjoint filenames, seeds or indices do not establish independent preparations. Signed or rational rotations of the same37 synthetic anchor series are finite adversarial fixtures with shared lineage. Genuine held-out validation requires preparations/acquisitions excluded from calibration and model selection, an auditable preparation lineage, and a partition frozen before scored outcomes. Freeze coefficients, model order rule, preprocessing/decoder, normalization, cap, horizon, stopping rules and all planned outcomes. Do not manufacture truth as prediction plus small random noise.

If initial validation states require measurements, freeze an independent initialization protocol and propagate its uncertainty. Fitting those states or amplitudes to the same future readings being scored is not held-out prediction. Shared gain/time calibration may be used only with explicit common uncertainty; its error is not reduced by counting more preparations. A predetermined separate apparatus calibration set is distinct from validation data. Data-dependent postvalidation calibration is a new disclosed experiment/version, never silent repair.

## Two-step alias refusal

The observed source multiplier exp(2i*omega) determines omega modulo pi in sample/model coordinates. Omega and omega+pi are exactly indistinguishable under lag2. A calibrated sample period converts units but alone does not choose an alias. A frozen external frequency band and acquisition/filter model must make the two-step map injective over all admitted possibilities with the required separation. Without those premises, retain a modulo-pi phase result and HOLD unaliased/SI identification. A good condition number cannot fix nonidentifiability.

## Prospective finite synthetic controls

Use these to test schema/decision behavior, not to claim physical validation or209-mode excitation. A constant-in-time rational perturbation of the stationary clock channel remains in the source family's linear span. Toy units and cap are fixture-local, frozen before evaluation, and cannot replace the old numerical gates.

Take a four-sample toy record with nominal stationary channel1/4 and all other channels zero. Add r/2 to that same channel at each of the four samples, so its exact Frobenius residual is r. Use toy acquisition bound alpha=1/128 and toy mismatch cap c=1/16. This small-shape arithmetic fixture is not a full37x8191x62 record or an excitation/cutoff test.

| Fixture | Frozen evidence/change | Exact decision |
|---|---|---|
| valid calibrated synthetic | Complete synthetic receipts, r=1/32 | upper5/128<=8/128: PASS_SYNTHETIC_CONTRACT |
| mismatch | Same receipts, r=1/4 | lower31/128>8/128: FALSIFY_SYNTHETIC_CONTRACT |
| uncertainty overlap | Same receipts, r=1/16 | [7/128,9/128] straddles cap: HOLD |
| missing gain provenance | Remove gain receipt/hash from otherwise valid fixture | HOLD_MISSING_CALIBRATION before residual arithmetic |
| missing time/preparation/noise/channel/unit provenance | One missing or inconsistent mandatory field per frozen control | HOLD with explicit reason, never zero-filled uncertainty |
| alias ambiguity | Two candidate frequencies omega and omega+pi, same two-step multiplier, no independent band | HOLD_UNALIASED_IDENTIFICATION; modulo-pi match may remain valid |
| validation contamination | A validation preparation inherits calibration raw dependency | HOLD_HELDOUT_LINEAGE; no independent-validation claim |
| cap boundary | alpha=0,r=c | PASS on exact upper<=cap; outward/inconclusive interval comparison HOLD |

A coefficient/sign/channel permutation with a correctly updated map should be a covariance control; leaving the decoder map unchanged should be a map-mismatch or model-mismatch control. Include wrong units, negative uncertainty, duplicated channel, saturation and unsupported statistical confidence as fail-closed controls. All control IDs, expected outcomes and bytes should freeze before verifier execution. No control outcome promotes physical status.
