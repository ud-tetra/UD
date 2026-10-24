# Source-completeness and full-path calibration witness specification v0.1

24 October 2026 · Development — no registry entry · Proposed requirements only

**Disposition: NOT READY FOR PHYSICAL ADMISSION.** The conditional theorem and exact design arithmetic are complete at constructor level. None of the physical witness reports below has been supplied. Independent adversarial review is pending. Physical Promotion0; EXIT-03 HOLD.

## Apparatus candidate and purpose

Use a **source-controlled, two-component I/Q voltage metrology demonstrator** before attempting an unknown simulator output. Two independently characterized signed voltage channels represent the real and imaginary components of the complex source. The fixture has a primary component with complex spectral TV≤1 V, plus100 stationary complex lines with mode indices100–199 and amplitudes≤2.5 µV each. The nominal cyclic span is1 s. A fixed complex-linear nominal path, bounded image response and bounded nonlinear/remainder terms connect source and target ports. Separate primary acquisition and complex monitor read the same declared residual reference under the same source preparation and epoch.

This is a calibration-fixture candidate, not an autonomous UD realization or a recreation of the historical31 kHz circuit acquisition. Direct baseband testing does not certify an omitted up/downconversion stage. If a later apparatus includes carrier conversion, that entire path must receive its own applicable image, gain, distortion, timing and reference-transfer bounds. No product purchase, apparatus operation or experiment is authorized or performed by this specification.

The monitor has1024 ordered complex samples. The existing acquisition and monitor timing requirements remain separate: original acquisition≤0.2 ns, monitor affine error≤10 ppb and total monitor sample residual≤10 ns. The provisional common coverage is[−1/10⁸,100000001/10⁸] s; both the monitor samples and original acquisition interval[0,16183/1953125] s lie within it. Actual run IDs, ports, loading and intervals must be resolved before review; the historical file6385 run remains unresolved.

## Independent witness package

| Witness | Required content | Proposed acceptance bound |
|---|---|---|
| Source line inventory | Frozen waveform/phase words; port definitions; reconstruction model; frequencies, drift and amplitude uncertainty; original independent source metrology |100 fixed lines, n=100…199, |e_l|≤1/200 Hz, each amplitude≤1/400000 V; summed amplitude≤1/4000 V and coefficient Euclidean norm≤1/40000 V |
| Source primary | Complete primary content and independent amplitude/phase metrology |Complex spectral TV B≤1 V; accounted in image/nonlinear budgets |
| Source impurity | Independent continuous-time source/reconstruction argument covering images, DAC artifacts, modulation and startup; scope covers all unlisted frequencies |R≤1/10⁶ V **spectral TV**, not RMS/PSD |
| Nominal path | Fixed complex-linear transfer model with traceable parameter intervals, loading and entire support coverage |M≤51/50; finite calibration grids need a validated enclosure between and beyond test frequencies |
| Image path | Full-input conjugate/image transfer, including imbalance and cross-coupling |J≤1/10⁶; this is true-output image content, separate from monitor readout error |
| Nonlinear path | Complex mixed-monomial model; parameter uncertainty and validity across the full input range |At V_*=1 V, sums of absolute coefficients β₂,β₃≤1/10⁶ each; not a single fitted coefficient or tail-only distortion |
| Additive remainder | Independent model and bound for true-output additive content |≤1/2000000 V spectral TV |
| Omitted dynamics | All higher orders and memory not in the stated polynomial |≤1/2000000 V spectral TV |
| Initial state and drift | Startup, unsettled state, time variation and temperature/supply effects over the same coverage |≤1/2000000 V spectral TV |
| Primary reference | Difference between the declared ideal H_+b reference and the actual subtraction/transfer reference |≤1/2000000 V spectral TV |
| Monitor readout | Full applicable I/Q path, conditioning/loading/extraction, baseline, digitization and numerical processing |Deterministic sample RMS triangle shares≤10/5/3/2 µV; quadrature matrix norm error≤1/10⁶ at raw vector norm≤5 V |
| Clock and transfer | True sample-event metrology, timestamp words, common-epoch transfer and simultaneous source stationarity |Clock bounds above; same residual complex spectral measure and same preparation across both intervals |

Each witness needs original bytes, units, method, parameter intervals, version/hash, validity interval, exact apparatus/run/port binding, constructor, independent reviewer and explicit exclusions. Source and path facts must not be inferred from the target monitor output they are meant to validate. A separate measurement path can be useful, but an independent path's finite FFT still does not establish an unrestricted spectral-TV bound.

Calibration sweeps and multi-tone measurements can falsify a proposed model and constrain a validated physical parameter family. They cannot alone prove a global model bound or an arbitrary omitted remainder. For a physical model, require an explicit theorem linking independently bounded parameters to the claimed uniform transfer/coefficient/remainder envelope. Pointwise fit residuals are insufficient. If the source has only noise-density or probabilistic specifications, record those honestly and return HOLD under this deterministic contract; any statistical alternative requires a separately reviewed theorem and coverage rule.

## Planned measurement and controls — not executed

1. Resolve the physical apparatus, references, full path, run identity, and source history. Freeze source words, firmware, configuration, port diagram, uncertainty budget and analysis hashes before the blinded run. Obtain nonconstructor adversarial review. This constructor packet alone does not satisfy that gate.
2. Review the source and full-path witness package independently. Require the exact source-to-path inequality and all remainder allocations to close at10 µV. Missing or unsupported roots return HOLD; do not replace them with fitted target values.
3. Acquire the monitor sample words and true-event timing records concurrently with the primary acquisition under the frozen preparation. Retain signed I and Q, raw pre-correction values, reference subtraction, calibration version and diagnostic channels. Apply only frozen corrections; label diagnostic refits separately.
4. Replay the exact digital-RMS/Gram checker using the reviewed records. Require digital RMS≤55 µV, sample error≤20 µV and independent outside-TV≤10 µV. The resulting general monitor bound is≤0.90675 mV. The source-controlled fixture's stronger direct model bound is an additional consistency prediction, not a replacement for missing evidence.
5. Preplan blinded controls: inject a known unlisted tone violating the impurity allocation; enlarge image response; enlarge quadratic distortion; perturb a timestamp; change a source word; and invalidate a calibration interval. Specify expected diagnostic/HOLD behavior before exposing labels. Detecting all physical controls is an experimental question; the current16 controls verify algebra/design rules only.
6. Reconcile evidence into the nine-role graph with independently issued receipts. Any changed preparation, model or calibration expires dependent acceptance. Preserve failures and original bytes. The unsigned tail proposal requires reviewed integration into the acquisition contract; the other eleven acquisition roles remain necessary.

## Exact conditional feasibility and limits

The proposed witness numbers imply outside-model TV≤6.021506252020 µV and sampled RMS≤52.796506252020 µV, including the20 µV readout allocation. The spare margins are approximately3.97849 µV outside TV and2.20349 µV sampled RMS. These are design margins, not measured uncertainties or hardware feasibility demonstrations.

The input-line assumptions also imply direct tail TV≤0.261021506253 mV. Therefore this fixture is a source-controlled **consistency and calibration test**. It cannot establish the mode completeness, stationarity or native normalization of an unknown UD source. No energy/native-support map, action ratio, coupling unification, proton decay or monopole conclusion follows.

**First blocking review item:** identify a defensible physical source/reconstruction model and a method for the1 µV source-impurity and2 µV aggregate remainder TV bounds. If those cannot be supported, the deterministic design stays HOLD even if the sampled waveform looks ideal.
