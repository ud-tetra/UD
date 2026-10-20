# C23 scoped source-applicability and prediction review

The recovered helper source clarifies a separate acquisition routine. It does **not** change the drive1 recipe or establish source-bound physical calibration. The paper's discussed driven comparisons include fitted and measured inputs; the reviewed passages do not establish untouched, pretarget validation for this UD work. These findings do not reject the paper's scientific conclusions.

The three author files were independently fetched through GitHub at commit `265b6671dde799d7c73f32247fa3ee93ae70e0f2`. Their exact UTF-8 bytes were bound by recomputing the Git blob SHA1 and SHA256:

| File | Git blob | SHA256 |
| --- | --- | --- |
| utility.c | 785ebb6c4303fe6060baeed49e96a42cff67022a | 8348e6f79e5c854f4b543e0de586bd0420be457767546523f17b622e3579ec79 |
| u1_drive1.c | 043e2731b643596f566eec0176557e877aaebc7a | 17bfd371ab475cce39acc9c0ad50cd4b856bfe3e60209b7701499890ffc7a1fa |
| utility.h | f20a9a86fd80af20afbf330c02fc0ff7ade7cd98 | a94bdf898508c1787a1f1051e4212e19308eb9496e501f57eccdd6c5661dd4a8 |

| Setting | utility.c helper | u1_drive1.c |
| --- | --- | --- |
| Decimation | best_decimation_factor targets 20 samples/period; acquire_2channels accepts a decimation argument | Direct RP_DEC_64 setting |
| ADC reset | acquire_2channels resets | Direct reset in acquisition loop |
| Trigger | NOW | External negative edge |
| Trigger delay | 8192 | 7992; source comment places trigger at sample 200 |
| Averaging | 1 | 1 |

The displayed drive1 source does not call best_decimation_factor or acquire_2channels. It uses other utility routines for ranges and the TTL waveform. Including utility.h does not apply every helper's configuration. Consequently neither the helper's NOW trigger nor adaptive decimation can replace drive1's direct settings. A 20-sample target is algorithmic intent, not a calibrated anti-alias, clock or joint-error bound; the finite allowed-factor list and fallback also limit any unconditional reading of that intent.

The exact-source acquisition block is in drive1 lines 139–148; data retrieval and default `%f` printing are in lines 181–199. This is a conditional source recipe. It does not prove which binary/configuration produced a selected archive, its board identity/calibration, sample-clock stability, cross-device skew, analogue anti-alias response or a deterministic waveform-error enclosure. A trigger chain or source latency comment cannot establish a shared calibrated ADC timebase. Source and metadata identity are distinct from runtime and metrological evidence.

The version-specific [paper](https://arxiv.org/html/2108.01086v1) was read through Firecrawl. Appendix A's simulation paragraph explicitly treats dissipation strength k=0.0045 as adjusted to the observations in Fig. 8; the preceding paragraph limits that empirical term to the driven simulations. This must not be generalized into a claim that all nondriven predictions were fitted. Appendix F motivates a reduced back-action hierarchy from observed amplitude decay and uses measured Fig. 7 amplitudes in its Fig. 4 frequency-shift calculation. Those are measurement-conditioned comparisons, not automatically a pretarget test.

Conditioning on separately measured covariates is not inherently circular. A later independent validation could use separately calibrated parameters/amplitudes and a frozen predictor against held-out outcomes. The enumerated paper/code/metadata sources do not supply the required chronology, exposure/custody separation and target-specific receipts for this UD qualification. No actual independent replicate is established, and no exhaustive absence claim is made. The HTML render date is not an acquisition or preregistration timestamp.

The retained evidence inventory records release 1.0 with 32 gzip archives. Its distinct 05-28 candidate was already labelled metadata-only HOLD and differs from exposed 05-21 in declared last-two-channel roles and drive amplitude. File/date/checksum differences alone cannot establish new acquisition independence or silently repoint an exact-source request. The parent's current 71-file/32-gzip reconciliation was not independently repeated in this review; no conclusion here relies on treating that reconciliation as reviewer-performed work.

Recovery of utility.c closes the earlier retrieval-availability gap only. It does not close a calibration or fresh-validation qualification gate, replace request metadata, change numerical gates or create physical authority. Public capture of this review should contain **only REVIEW.md and REVIEW.json**; local source copies are excluded.

Development — no registry entry. Limited enumerated primary-source review; no raw archive opened, notebook/source executed, fit, estimator, new numerical wrapper, new acquisition or gate change. Provenance HOLD. Independent acquisition/fresh preparation NOT_ESTABLISHED. External promotion review PENDING. Physical Promotion = 0.
