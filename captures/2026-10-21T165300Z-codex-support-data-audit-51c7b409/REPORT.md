# Published-data audit against the energy-clock-support contract v0.1

**Result: useful experimental data recovered; no independent UD action anchor admitted. Physical promotion 0.**

This is a scoped content audit, not an exhaustive literature search, a blinded test, or an empirical score of QPB1. Published data can test a declared physical correspondence; they do not replace a mathematical proof. “Not established” below means not established by the specific material inspected, not proof that authors hold no additional records.

## Dataset dispositions

| Dataset | Material actually inspected | Useful role | Action-anchor disposition |
| --- | --- | --- | --- |
| Riechert et al., classical circuit LGT; doi:10.11588/DATA/6MEKHI, v1.0 | One complete raw waveform; acquisition documentation; static analysis of figures notebook, including its energy function | Signed-waveform reconstruction and readout-parity diagnostics | HOLD: absolute UD support map, certified energy/baseline, phase skew and same-carrier correspondence unestablished |
| Datla et al., Rydberg statistical localization; doi:10.5281/zenodo.18012627, v1 | Every CSV member in the released archive, record metadata, 2025 preprint and 2026 publication data-availability section | Correlator, population and localization reanalysis | HOLD: no signed state-quadrature witness or independent UD support/energy map established |
| Yang et al., 71-site optical-lattice simulator; doi:10.7910/DVN/3RXD5F, v1.1 | Current landing page and original-format Fig.4 workbook, four tabs | Population and gauge-violation comparisons | HOLD: reviewed file does not supply an absolute UD support/phase/energy map |
| Mil et al., atomic mixture; doi:10.5061/dryad.8gtht76k2 | Current release listing, one additional figure-4A CSV text response; prior audit of three CSV responses retained separately | Normalized population/imbalance response comparisons | HOLD: reviewed figure data do not establish required amplitude/phase/energy certificates |

The Rydberg record predates the February 2026 journal publication. Its preprint says data are available on request, while the journal publication points to the public Zenodo record. The public release therefore must not be rejected merely because of the older preprint statement. No author was contacted.

## Circuit data: signed information exists before squaring

The 30,941,478-byte waveform matches the published MD5 and the earlier capture's SHA-256. It has 1,000 rows, ten channels, 100 records per channel and 16,384 samples after six metadata fields. Acquisition rate is 1,953,125 Hz. The nominally empty tenth channel is excluded from the nine-channel diagnostic by the published filename; emptiness is not independently certified.

For record index zero of each live channel, discard the first 200 samples, subtract the mean separately from V and V², apply a Hann window, and find the largest FFT peak in fixed bands 10–200 kHz for V and 20–400 kHz for V². All nine squared-signal peak bins lie within one bin of twice the signed-voltage peak bin. The post-crop FFT bin width is 1,953,125/16,184 Hz. This exploratory descriptive check illustrates information loss under squaring; it is not a certified primitive recurrence, a statistical confidence claim, or a Hodge-carrier validation. The fast circuit carrier is not automatically the native update clock. The near-2 frequency ratio has no identification with QPB1's eta_A=2/1.

The verified original figures notebook is parsed as JSON and never executed. Its cell 48 defines capacitor energy from voltage envelopes with default C=20 nF. That is a reproducible analysis choice, not a joint component-calibration and energy-functional certificate. External trigger wiring is documented, but timing equality in metadata does not bound inter-device phase skew. The nonlinear five-site/four-link chain has no established map to the filled-tetrahedron active sector in the reviewed material. Candidate priority is therefore signed readout/simulator diagnostics, not native-action scoring.

## Rydberg data: complete CSV inventory, limited observables

The 18,411-byte Data.zip matches MD5 ba2e952d6a35e79306f90e34d88eac92. Its 27 CSV members parse as finite numeric arrays. The dataset record identifies CC-BY-4.0; creators are Prithvi Raj Datla, Luheng Zhao, Wen Wei Ho, Natalie Klco and Huanqian Loh. A derived source bundle preserves only those 27 scientific CSV members, excluding unrelated archive metadata; each member's original hash is recorded.

File names identify autocorrelations, MeanZ and charge-distribution panels, with experimental/theory variants in figure 4c. Numeric headers are absent; axis roles and uncertainty semantics are not invented from column position. Negative MeanZ values are signed expectations, not signed field quadratures. The reviewed paper describes projection/Z measurements rather than a native amplitude/phase map.

The bottom figure-2a OmegaT array has 42 entries; it consists of two identical copies of the 21-entry top OmegaT vector. Both associated autocorrelation arrays have shape 31×21. This is an intake ambiguity, not a demonstrated scientific error. Retain the original vector; any collapse to a unique 21-entry axis must be explicit and justified before a fit. No fit, energy reconstruction or action estimate is performed.

## Representation and access limits

The Harvard request with `format=original` yields a 19,008-byte OOXML workbook despite the requested filename Fig4.tab. Its original MD5 matches the dataset inventory. The four tabs separate experimental populations, exact-diagonalization populations, experimental gauge violation, and DMRG gauge-violation calculations. The ingested tabular representation and original workbook must not be assigned interchangeable byte counts or parsed by extension alone. The workbook is inspected read-only; no workbook is edited or exported.

The Dryad direct download returned HTTP 403 in this environment; a public text retrieval supplied the figure-4A CSV with 22 numerical rows and a three-column header for normalized imbalance, population mean and its error. This is a text-content audit, not a checksum-verified raw download. The other three figure-4 files remain outside this turn's inspection. Earlier results stay separately scoped rather than being relabeled complete.

An initial circuit notebook transfer failed length/checksum/JSON checks and was rejected. The original-format retry matches the published 7,825,300 bytes and MD5. No conclusion uses the rejected payload. No imported notebook, acquisition script or experiment was executed. Documentation containing device login examples is not republished.

## Gate conclusion and next executable work

The source energy-clock-support theorem requires the actual carrier map M, no-leakage/intertwiner conditions, energy functional G and baseline, an absolute support law or map, a certified readout ratio rho, and joint uncertainties. None of these four scoped reviews closes that complete conjunction. Population normalization or a conventional unit ray does not establish native a=1. No eta_A or hbar estimate is calculated.

Highest-value next reanalysis: freeze a signed-voltage reconstruction contract for the circuit data, separating fast carrier phase, rotating-frame envelope and quadratic energy before any recurrence interpretation. Missing physical amplitude, energy and skew certificates remain explicit OPEN inputs. This can test reconstruction machinery and parity errors without scoring QPB1 or pretending the circuit is the Hodge carrier. Independent review precedes any new empirical bridge score. EXIT-03 remains HOLD.

## Primary sources and provenance

- Circuit data: https://doi.org/10.11588/DATA/6MEKHI ; paper: https://doi.org/10.1103/PhysRevB.105.205141 ; preprint methods: https://arxiv.org/html/2108.01086 .
- Rydberg data: https://doi.org/10.5281/zenodo.18012627 ; publication: https://doi.org/10.1038/s41567-026-03183-w ; earlier preprint: https://arxiv.org/html/2505.18143 .
- Optical-lattice data: https://doi.org/10.7910/DVN/3RXD5F .
- Atomic-mixture data: https://doi.org/10.5061/dryad.8gtht76k2 .
- Prior dataset audit: capture 2026-10-18T141800Z-codex-measurable-audit-a7c392e1. Contract: capture 2026-10-21T162600Z-codex-energy-clock-7b4e0ac2. Current audit code and per-source content receipts accompany this report. Full waveform/notebook remain external hash-pinned source inputs; their complete bytes are not duplicated in this new capture.

**Typed footer:** Development — no registry entry. EMPIRICAL DESCRIPTIVE: waveform spectra and released-array contents only. DERIVED: source-contract eligibility assessment, with unestablished premises recorded OPEN. No experiment, physical correspondence, primitive quantum holonomy or action-ratio score is asserted. Constructor: Codex root. Non-constructor review pending. Physical promotion 0.
