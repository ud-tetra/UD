# Sampled event acquisition and uncertainty receipts

15 October 2026 UTC. Development - no registry entry. Constructor-checked finite mathematics and a declared passive observer; physical promotion 0. No apparatus execution or non-constructor review is claimed.

## What this package closes

The v0.13 hysteresis candidate makes a continuous carrier-to-event rule explicit. It does not automatically make the events readable by finite-rate threshold polling. This package closes a narrower conditional acquisition contract: given bounded stock error, a maximum sample gap and specified transverse/persistent excursions, a conservative observer confirms every address-wise event within a proved delay. It retains uncertainty intervals rather than promoting detection ticks into exact physical event times.

The new guarantees are derived directly. General hysteresis, interval error accounting and sampling are established methods; the contribution here is their exact contract, carrier fixture, counterexample and resource accounting within the existing UD narrative. No broad novelty claim is made.

## Source and governance

The baseline narrative is v0.13, Library version 5, with exact bytes preserved. Its evidence package and GitHub capture commit 92919f243252b1c947660382b333329c8274c2be (PR94, unmerged at creation) are pinned in SOURCE_REGISTER.json. D.15's written stock/dwell bounds are inherited within their fixed-carrier, all-gates-open, passive scope. Selected new computations rebuild the single-cell incidence generator independently; historical source scripts are not executed.

The supplied August ledger v0.39 and proposed CRL2 amendment are preserved as historical source/development governance. The coefficient ledger's G05/G06 action gaps remain open. No claim advances to a registry or physical interpretation. No physical constant is fitted or normalized from a numerical target. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read or used; re-upload it if it should be analyzed. Other historical project files are not newly validated by this package.

## Findings and logical limits

| Finding | Status and qualification |
|---|---|
| A dwell bound alone does not guarantee direct polling capture | EXACT counterexample: a threshold touch between every grid point, on arbitrarily fine odd grids |
| Certified on/off guards | DERIVED wrong-side exclusion from the bounded-error interval; real events may still be withheld |
| Detection delay D=2*epsilon/nu+Delta | DERIVED under explicit reach, persistence, matching-state and coverage conditions |
| Same per-address toggle word | DERIVED when every event satisfies those conditions and D is below the ideal per-address dwell |
| Global event order | CONDITIONAL: requires cross-address separation or nonoverlapping event-time intervals; no uniform native gap is supplied |
| Six-bit, 1/64 cadence fixture | EXACT rational certificate; all guards/bins enclosed without floating-point decisions |
| Bounded-error envelope | EXACT finite overapproximation: twelve per-address words and 1728 joint combinations, with no probability assigned |
| Readout resource formats | EXACT counts for specified logical buffers and encodings, excluding separately supplied metadata and physical implementation |
| Threshold source, sensor, back-action, work and renewal | OPEN |

The counterexample concerns a threshold-polling algorithm. It does not show that exact model-assisted reconstruction from a known state and generator is impossible. The amplitude-only noise cutoff in D.15 applies to its raw noisy guard; the present conservative guard can safely withhold events for larger error. Its principal challenge is completeness, controlled here by excursion margins and sampling coverage.

## The declared observer

At each supplied sample instant, acquire three bounded-error opposite-edge stocks. A zero response bit turns on only when the stock interval's lower endpoint reaches h. A one bit turns off only when its upper endpoint reaches ell. The other cases retain the bit. All confirmed changes at one sample form a detection mask. This finite classical algorithm assumes supplied access to stock values and leaves the carrier unchanged; it is not a quantum instrument or a sensor Hamiltonian.

For an ideal rise, the true stock must reach h+2*epsilon quickly enough and remain there for a full maximum sample gap. For a fall use ell-2*epsilon. The lower slope gives a reach-time bound; the interval of persistence contains a sample. If the resulting delay is shorter than the ideal per-address dwell, induction proves faithful address-wise words. A dwell bound does not itself supply either persistence or a lower crossing slope. Grazing and end-window events remain explicit exclusions unless extra acquisition is supplied.

## Exact fixture and joint error envelope

Use the canonical unit vertex trajectory q_p(s)=sin^2(2s)/4, the ideal thresholds ell=1/16 and h=3/16, six-bit bin-midpoint quantization, zero analog error and sample times s_n=n/64 for n=0,...,128. The quantizer error is at most 1/128. Choose the conservative slope bound nu=3/8. Direct inequalities give D=11/192 < 1/16, below the already proved ideal dwell bound. The required upper/lower confirmation cores each last at least 3/64, exceeding one sample gap. Both events occur well inside the acquisition horizon S=2.

Exact rational sine enclosures at all 129 sample instants certify masks 111 at ticks 34 and 84 for the specified deterministic quantizer. This is a synthetic mathematical trace, not a measured data set. The replay also propagates all allowed bounded-error decisions for each address: onset may occur at tick 34,35 or36, and extinction at84,85,86 or87. Every one of the twelve word combinations has two events within the delay certificate. The Cartesian joint envelope has 1728 combinations and can split the two ideal simultaneous batches into as many as six detection batches. These are allowed uncertainty histories, not a noise distribution or probabilities.

## Resource comparison

| Resource | Count for the horizon S=2 |
|---|---:|
| Scan instants | 129 |
| Scalar stock acquisitions | 387 |
| Current stock buffers | 18 bits |
| Response register | 3 bits |
| Tick counter | 8 bits |
| Detection mask buffer | 3 bits |
| Raw quantized stock archive, if retained | 2322 bits |
| Dense response log, including initialization | 387 bits |
| Sparse response log for the deterministic two-batch trace | 33 bits |
| Same sparse format for the six-batch bounded-error envelope | At most 77 bits |

Sparse records contain an eight-bit tick and a three-bit mask, preceded by the initial three bits and an eight-bit record count. The count field supports the whole 128-interval schedule. These are specified encodings rather than optimal coding theorems. The raw archive and response log serve different purposes and are not substitutes if independent replay of acquisitions is needed. Work buffers and stored records are also distinct.

These figures exclude configuration/reference metadata: scale, thresholds, cadence, quantizer definition, initialization, uncertainty bounds and proof dependencies. Their supply is not treated as physically free. Sensor preparation, transduction, reliable write/retention, processing, clock/reference energy, back-action, bath renewal and exhaustion remain unmodeled. A short response log cannot be compared with boundary area as though it were complete apparatus cost. Nor is its bit capacity a measured entropy: the known deterministic fixture may carry no surprise for a recipient already holding its full preparation.

## Next closure order

1. Keep the native threshold and response semantics problem explicit; this remains an engineered candidate observer.
2. Specify a finite physical acquisition instrument with an input/record channel, back-action, retained distinguishability and a preparation/renewal ledger. The present error budget supplies a target contract for that model.
3. Check whether an application needs a per-address word, a true batch, or a resolved global order. Source the extra timing/reference information before assigning winding or order-dependent costs.
4. Compare resources only after the actual apparatus and boundary map exist. No gravitational entropy density follows from digital buffer counts.

## Reproduction

Run `python verify_sampled_acquisition.py` with SymPy. It produces SAMPLED_CHECKS.json and SAMPLED_TRACE_CERTIFICATE.json. Eighteen check families pass. Sine values are bounded between consecutive alternating rational Taylor sums; Machin's identity and rational arctangent bounds enclose pi for timing checks. The finite guard/envelope enumeration is a certificate for the fixture; universal statements are established by the following written proof. This is constructor verification, not independent review or a replay of all inherited theorems.

## Manuscript proof insertion

## D.16 Sampled acquisition and receipts of uncertain event times

### D.16.1 A dwell bound does not guarantee threshold detection

Keep D.15's passive fixed-carrier model. Its per-address dwell bound concerns the ideal response memory after a guard hit. It does not require the stock to remain above the upper threshold until a sampler reads it. For example, on the canonical vertex trajectory $q_p=\frac14\sin^2(2s)$ choose $h=1/4$ and $\ell=1/8$. The ideal inclusive guard turns on at $\pi/4$ and off at $3\pi/8$. For every odd integer $N$, the grid $s_k=k\pi/(2N)$ misses every maximum: equality would require $2k=(2j+1)N$, impossible by parity. Direct threshold polling therefore remains off even as the grid becomes arbitrarily fine.

This is a limitation of the threshold-polling observer, not an impossibility theorem for model-assisted reconstruction from richer data. Transverse high excursions can also be arbitrarily narrow near grazing; a uniform completeness guarantee needs a quantitative excursion condition rather than a cadence alone. The finite-activity theorem in D.15 remains valid.

### D.16.2 Certified guards and sufficient conditions for faithful acquisition

Let actual sampling times have maximum gap $\Delta>0$ and let $|y_{p,k}-q_p(s_k)|\le\varepsilon$. Initialize the sampled response equal to the ideal one. Use the conservative guards

\[
0\to1\quad\text{if }y_{p,k}-\varepsilon\ge h,
\qquad
1\to0\quad\text{if }y_{p,k}+\varepsilon\le\ell;
\]

otherwise retain the sampled bit. Update all enabled bits in a detection batch, leaving the carrier unchanged. A confirmation implies that the true stock is on the appropriate side of its ideal threshold. Large error can prevent confirmation altogether. Unlike D.15's raw noisy threshold rule, these interval guards need no half-gap condition merely to exclude a wrong-side confirmation; completeness has the additional conditions below [29].

For each ideal rising event at $\tau$, assume the true stock reaches $h+2\varepsilon$ at some $u\le\tau+2\varepsilon/\nu$, and stays at least that high on $[u,u+\Delta]$. A sufficient reach condition is $q'_p\ge\nu>0$ until reaching that level. For a falling event use $\ell-2\varepsilon$ and $-q'_p\ge\nu$. These are supplied event-wise excursion and persistence hypotheses; they are not consequences of skewness alone.

Then the matched sampled event is confirmed with delay

\[
0\le s_{\rm det}-\tau\le D,
\qquad D=2\varepsilon/\nu+\Delta.
\]

**Proof.** A sample occurs in $[u,u+\Delta]$. For a rise, its value satisfies $y\ge q-\varepsilon\ge h+\varepsilon$, so the rising guard fires if it has not already done so. A matched confirmation cannot precede the ideal event, because its true stock must already have reached the ideal threshold. The falling proof is the same with inequalities reversed.

If these hypotheses hold for every event and $D<d_*$, where $d_*$ is D.15's ideal per-address dwell bound, induction gives exactly the same toggle word at each address: every event is confirmed before the next opposite event, and no extra matched event can occur between ideal switches. This claim preserves address-wise words, not necessarily the global order or simultaneity of different addresses. For a finite acquisition window the guarantee covers events at least $D$ before its end; later events require a tail acquisition or an unresolved end-window receipt.

### D.16.3 Time intervals preserve what detection order cannot

With exact detection time $s_i$, retain an event-time interval $I_i=[s_i-D_i,s_i]$. With timestamp error at most $j$, use

\[
I_i=[\widehat s_i-D_i-j,\widehat s_i+j].
\]

Declare event $i$ definitely earlier than $k$ only if $\sup I_i<\inf I_k$. Overlapping intervals do not certify order or simultaneity. A sufficient global ordering condition for ideal times $\tau_i<\tau_k$ is $\tau_k-\tau_i>D_i+2j$, since delays are one-sided. D.15 supplies no uniform gap between different addresses, so no positive fixed cadence guarantees global ordering on that full domain. The bound $\Delta$ refers to actual gaps; if nominal periodic samples have time jitter $j_s$, use at most $\Delta_{\rm nominal}+2j_s$ instead.

Even an ideal simultaneous batch may split into several detection batches under address-wise error. Such a log records acquisition order. It must not be used as a fine carrier-event order without further evidence. If $m!$ different serial orders remain possible and the desired functional distinguishes all of them, recovering a realized order requires at least $\lceil\log_2(m!)\rceil$ additional fixed-length bits, conditional on the known event set. This is a necessary storage condition, not a mechanism for observing the order; guessing those bits adds no evidence. True batches and unresolved order remain valid receipt objects.

### D.16.4 Quantization, an exact fixture and a finite storage ledger

A $b$-bit uniform quantizer on $[0,R^2]$ with bin-midpoint outputs has maximum quantization error $R^2/2^{b+1}$. Clipping an analog reading to that interval cannot increase its error relative to a true stock in the interval. With analog error at most $\varepsilon_a$, use

\[
\varepsilon=\varepsilon_a+R^2/2^{b+1}.
\]

A sufficient design inequality for the delay certificate is

\[
2\varepsilon_a+R^2/2^b<\nu(d_*-\Delta),\qquad\Delta<d_*.
\]

The excursion hypotheses must still be checked. These are logical precision and cadence budgets, not an ADC implementation or a physical energy law.

For the canonical unit vertex trajectory, use $R=1$, $\ell=1/16$, $h=3/16$, $b=6$, $\varepsilon_a=0$ and $\Delta=1/64$. Then $\varepsilon=1/128$. On the required rising/falling bands, the speed is at least $\sqrt{39}/16>3/8$; choose $\nu=3/8$. The confirmation core has length at least $3/64>\Delta$: its stock margin to the peak or trough is $3/64$ and $|q'_p|\le2$. The sinusoidal upper and lower cores are each a single interval. Thus

\[
D=\frac{2(1/128)}{3/8}+\frac1{64}
=\frac{11}{192}<\frac1{16}\le d_*.
\]

Six bits are the minimum for the chosen conservative test $D<1/16$; five give $19/192>1/16$. This uses the linear dwell certificate rather than optimizing the angular one, and is not a globally optimal digitizer lower bound.

On $s_n=n/64$, $0\le n\le128$, the deterministic midpoint-quantized observer records masks $111$ at ticks 34 and 84. Exact rational sine enclosures certify every bin and guard. Allowing arbitrary stock errors within $1/128$ gives per-address onset ticks 34–36 and extinction ticks 84–87, with all twelve combinations permitted by the replay envelope. All are within the proved delay bound. The $12^3=1728$ joint combinations can produce up to six detection batches from the two ideal batches; no probability or independence law is assumed.

There are 129 scans and 387 scalar stock values. The declared current buffers use 18 stock bits, three response bits, an eight-bit tick counter and a three-bit mask buffer. Retaining every quantized stock value separately uses 2322 bits. A dense response-word format uses $3(129)=387$ bits including the initial response. A sparse format with a three-bit initial response, an eight-bit count, and an eight-bit tick plus three-bit mask per record uses 33 bits for the deterministic two-record trace, or at most 77 for the six-record error envelope. These formats encode the observed response log; they do not replace the raw stock archive when that is required. Interval interpretation, scale, thresholds, quantizer, clock and error contracts require separately supplied metadata.

Storage capacity is not automatically information gained; a completely known deterministic preparation may make its trace predictable. Nor is the log the whole apparatus: sensor preparation, back-action, calibration, reference/clock supply, reliable retention, coding/processing and renewal remain uncosted physical resources. This package closes a conditional finite sampling and receipt contract. Native event selection, physical implementation, complete energy cost and entropy per boundary area remain open.
