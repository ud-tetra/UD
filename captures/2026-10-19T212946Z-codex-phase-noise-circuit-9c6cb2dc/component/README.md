# Executed frozen ten-channel circuit component analysis

Development — no registry entry; external non-constructor review PENDING; Physical Promotion=0.

The unchanged PR244 component reference checker was executed on the exact author-deposited Riechert acquisition identified by SHA2567966700a6208e2bd2b5829a32b38cce7016f0c3460ace2708c85bac8577c282c,30,941,478 compressed bytes, gitblob2dc5ace1c7d79b01bb0aba96577861a9eeae6acc at author commit265b6671dde799d7c73f32247fa3ee93ae70e0f2. The Git partial fetch retrieved pinned raw data only; author acquisition/analysis code was not executed. The earlier GitHub connector file route returned no binary content and its blob route refused UTF8 decoding; neither response was parsed as a waveform or substituted for data.

The1000 records form100 groups containing all10channels. The previously frozen group split is60train/20validation/20test. The post-trigger crop has16184 samples. All80 fixed channel-feature/partition comparison rows completed descriptively; no feature was undefined. No row, channel or group was dropped or imputed. COMPONENT_RESULT.json retains every feature and paired held-out error; COMPARISON_TABLE.md exhaustively displays all80 comparisons.

Interpolation has lower test MAE in9of40 pairs, median in27, and4ties. On validation these counts are11,25,4. These are dependent descriptive comparisons, not hypothesis tests or evidence selecting a physical model. Both methods remain reported; no winner is installed. Some dominant-bin errors are exactlyzero because the discrete returned bin labels agree; this does not prove underlying continuous frequencies are identical. Fifty-eight of1000 records change dominant bins between the fixed rectangular and symmetric-Hann windows, at most one nominal bin (about120.682464Hz). Window disagreement and bin spacing are not confidence bounds. Channel10 remains an acquisition channel with an unverified filename label, not a certified noise-only reference.

The contract and code were frozen in the prior turn. EXECUTION_FREEZE.json binds their unchanged bytes, raw identity and current runtime before the primary raw run. Previous full-record summaries were already known; this is not blinded external preregistration. The historical scope flags and deferred-execution docstrings in the byte-identical copied prior files describe their original contract-only turn; this separate execution receipt authorizes and records the present raw run. REPORTING_PLAN.json was written after primary execution completed but before result-feature inspection; it specifies exhaustive reporting without changing any frozen scientific extraction or comparator.

One primary run and one post-known-outcome portable replay were executed. The replay returned byte-identical scientific JSON. Separate same-team streamed review is counted separately; it uses the same raw bytes and independent reduction/comparator code with disclosed floating FFT backend overlap. None of these is independent experimental replication, an interval FFT proof or physical calibration. No native floating-estimator/SVD/eigenvalue/inverse/alignment proposal was run, and no gauge/phase/coupling/nonlinear model was fitted. The two simple descriptive baselines do use the frozen training groups, as declared.

## Replay

Supply the exact compressed file from https://github.com/tychon/U1CircuitsData at the immutable commit above, path05-21/set2_CH1-site1_CH2-link1_CH3-site2_CH4-link2_CH5-site3_CH6-link3_CH7-site4_CH8-link4_CH9-site5_CH10-empty.gz. Related deposited dataset DOI:10.11588/DATA/6MEKHI; fileDOI10.11588/DATA/6MEKHI/4PV8ZU. Original measurements and dataset credit belong to Riechert and collaborators. The inherited dataset inventory identifies CC-BY-4.0 data; source bytes are referenced externally rather than duplicated here. The related paper is Physical Review B105,205141(2022), DOI10.1103/PhysRevB.105.205141.

Use the full UD repository and a new external output directory:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python replay.py --repo /absolute/UD --raw /absolute/pinned.gz --out /absolute/new-component-replay
```

The replay never downloads data, changes contract/code, repairs a HOLD or selects a model. The exact result checksum also depends on the recorded software versions; no universal cross-platform bit-reproducibility is asserted. A mismatch is refused and retained, not silently repaired.

Recorded nominal volts and metadata hertz remain uncalibrated conditional units. There is no actual independent gain/offset/time-grid/anti-alias/uncertainty or oscillator-to-UD state/action bridge. Native62-channel admission, calibrated nonlinear circuit comparison, phase/Gauss conservation significance and physical correspondence remain HOLD. No2^-49residualgate or2^-38shape reassignment is used. The modelq=2^-48 is unrelated to a measured SI tolerance.
