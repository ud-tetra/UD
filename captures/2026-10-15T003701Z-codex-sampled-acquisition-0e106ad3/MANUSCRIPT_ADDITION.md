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
