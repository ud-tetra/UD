# UD — Native Seam-Source Selection and Adversarial Generator Gate v0.3

**Date:** 2026-11-15  **Track:** development / independent reproducible mathematics  **Physical promotion:** **0**

**Claim classification:** **EXACT_CONDITIONAL** (theorems and exhaustive finite calculation), **NO-GO_SCOPED** (source-selection impossibility under named premises), **CANDIDATE** (postulated dynamical laws), **OPEN_GATED** (native selection, G05/G06 and physical bridges). This is an additive successor to the source-captured `UD_NATIVE_ADMISSIBLE_MULTI_FACE_v0.2` and its two draft PRs, not a retroactive amendment to frozen results.

## 1. Source / object contracts

Recovered historical March 2026 sources:
- `triangular_transport_symbol_alphabet.md`, §§2–4: face admissibility `A_[ijk]=1−δ_{b_i b_j}δ_{b_j b_k}` and phase/framing/closure symbols.
- `seam_phase_transport.md`, §§1–4: link transport `U_ij`, loop holonomy and `U(1)`-like reduction `U=e^{iqφ}`; it does **not** select a stochastic transition rate.
- `packet_modulation_layer.md`, §§1–3: `X_i=(ρ_i,θ_i,χ_i)` and generic `F_i` update; stated phase/stock coefficients are not fixed by primitive geometry.
- `packet_field_equation.md`, §4: continuum-limit update ansatz, not microscopic proof.

Versioned current governance check: `ud-tetra/UD-Physics@2ab32f5f28d0461dc4d35a389e814e8415cb58e8`, `state/CURRENT.md` and `experiments/g0506-packet-hodge-sourcegate/README.md`; no unique packet-to-Hodge source map or action unit. Prior developmental source results: `ud-tetra/UD` draft PR #513 and `ud-tetra/UD-Physics` draft PR #387, 2026-11-15. Neither PR had been merged at this audit.

**Carriers (not physical identification):** two filled tetrahedra `[0123] ∪ [0124]`, `V=5`, `E=9`, `F=7`, `T=2`. Binary `b∈(Z2)^5`. Exactly six globally face-admitted `b` configurations, with zero admitted one-bit edges and two disjoint `K3` components of the six admitted minimal Hamming-two edges.

**Candidate dynamical state:** `(b,d,x)` with `d∈Z4` the gauge-compensated seam phase, `x∈N_0^F`, total stock `∑_f x_f=M=2`. These *face stocks* are additional assumed state coordinates, not necessarily historical UD burden or physical mass. Clock `s` is an uncalibrated Markov event parameter. Positive coefficient field `Q`; no continuum metric, Planck unit, spatial wave-number or CMB readout.

Define a permitted face-stock event `f→g` by `χ_L(b)χ_R(b)=1`, `x_f≥1`, and the faces sharing a complete edge; its destination is `x−e_f+e_g`. This is necessary pre-event authorization, **not unique event selection**. The generator's outgoing rate is separately specified.

## 2. Exact source-selection obstruction: even with endpoint forcing

**Hypotheses H:** (H1) the relative seam phase is `d∈Z4` with `U=i^d`; (H2) the interfacial weight is a gauge-invariant scalar `p(d)`; (H3) reversal-even `p(d)=p(−d)`; (H4) `0≤p(d)≤1`; (H5) aligned-phase opening `p(0)=1` and antiphase shutdown `p(2)=0`. H5 is a **stronger candidate boundary condition**, not historically forced, chosen to give uniqueness the best chance.

**THEOREM (EXACT):** Every weight satisfying H has the form

`p(d) = (1,q,0,q)` for `q∈[0,1]`, in `d=0,1,2,3` order.

**Proof:** H3 forces `p(1)=p(3)=q`; H5 fixes the other two; H4 only bounds `q`. Conversely every such vector satisfies H. QED.

Hence even these stricter conditions leave an entire continuum of inequivalent positive-stock generators. In particular:

| Phase law | `p(0),p(1),p(2),p(3)` | Additional construction |
| --- | --- | --- |
| first harmonic | `(1,1/2,0,1/2)` | `p=(1+cos φ)/2` |
| squared harmonic | `(1,1/4,0,1/4)` | `p=((1+cos φ)/2)^2` |
| strict match | `(1,0,0,0)` | `p=1[d=0]` |

All are gauge-compensated, reversal-even, nonnegative and have identical endpoint behavior. They are different at quadrature `φ=π/2`.

**Conditional rescue / necessary new axiom:** If one *additionally imposes* `p(φ)=a+b cos φ` for all phase values (first Fourier harmonic) together with H5, solving `a+b=1`, `a−b=0` gives `a=b=1/2`. This selects the v0.2 `q=1/2` rule **only within the newly assumed first-harmonic constitutive class**. Historic U(1)-like seam transport and binary closure alone do not force the first-harmonic truncation or a Born-intensity readout. An overall event-rate `γ>0` is also entirely unselected; multiplying a generator by `γ` changes the dimensionless clock pace without changing its static constraints.

**Pre-event bit rule:** The admitted Hamming-two edges form two triangles. If one additionally postulates minimal moves, no coupling to phase/stock, permutation-invariant equal-edge rates, and bit-complement symmetry, their rates must agree on each of the six edges, but the common scale is free. Geometry selects this adjacency, not a stochastic clock.

## 3. Second obstruction: equilibrium does not select donor kinetics

For each undirected adjacent face pair `{i,j}`, let the common symmetric stock transfer rate be

`q_{i→j}(b,d,x) = x_i w_ij(d) [1+κ(x_i+x_j−1)]`, `κ≥0` and `x_i≥1`.

Here `w=1` on intra-tetrahedron exclusive-face edges and `w=p(d)` across the glued interface. The donor multiplier depends on the conserved **pair stock** `x_i+x_j`; the reverse event has the same multiplier. Both `κ=0` (linear donor) and `κ=1` (pair-stock enhanced) have nonnegative rates, exact stock conservation and reversible *identical* equilibrium

`π(b,d,x) = (1/24) · (M! / ∏_f x_f!) · F^(−M)`

for each fixed face set of size `F`. The factor `1/24` is uniform on six admitted bit states and four phase states; bit flip and phase diffusion update independently with symmetric rates. **Detailed balance proof:** for `y=x−e_i+e_j`, `π(y)/π(x)=x_i/(x_j+1)`; `y_i+y_j=x_i+x_j`; and `w_ij=w_ji`, so `π(x) x_i w h = π(y)(x_j+1)w h`. Phase and bit transitions separately satisfy symmetry. No external source/sink is hidden.

For any centered zero-sum linear face mode `Z_e=e·x`, stationary correlation's initial slope obeys the exact Dirichlet identity

`R'_e(0)=−[sum_{i<j}w_ij(d)(e_i−e_j)^2 / ||e||²] · [1 + 2κ(M−1)/F]`

when `d` is fixed. Averaging over uniform phase replaces `w(d)` by `E_d w`. This follows because the occupied pair total `m=x_i+x_j` is binomial `(M,2/F)`, and `E[m(1+κ(m−1))]/E[m]=1+2κ(M−1)/F`.

At `M=2`, `F=7`, `κ=1`, the slope is multiplied by `9/7` compared with `κ=0`, while the **second derivative does not scale by `(9/7)^2`**. This excludes equivalence under a single constant clock rescaling. Hence even a fixed symmetric equilibrium law and fixed phase gate leave a genuine dynamical constitutive ambiguity.

## 4. Exhaustive tests, including alternate boundaries

Exact full-state verification covers 672 states for each seven-face model (`6×4×C(8,6)`) and 504 states when the shared-face stock is removed (`6×4×C(7,5)`). Each case was exhaustively checked for nonnegative rates, valid destinations, total face-stock conservation, and detailed balance. Rephasing compensation was exhaustively checked over `4^5` frame/connection choices. Independent standard-library replay performed direct stationary two-step moment calculations on the 112-state stock×phase marginal (binary sector factors out).

Normalized autocorrelations of the intercell difference `v=(0,1,−1,1,−1,1,−1)` start as follows. These are exact rational native-event derivatives, not experimental data:

| Generator | `R'_v(0)` | `R''_v(0)` | Total joint states |
| --- | --- | --- | ---: |
| harmonic first-phase, κ=0, full | `−3/2` | `27/8` | 672 |
| squared harmonic, κ=0, full | `−9/8` | `81/32` | 672 |
| strict match, κ=0, full | `−3/4` | `9/4` | 672 |
| harmonic, κ=1, full | `−27/14` | `351/56` | 672 |
| harmonic, κ=0, shared face reflective | `−1` | `3/2` | 672 |
| harmonic, κ=0, shared-face stock omitted | `−1` | `3/2` | 504 |

**Boundary conditions:**
- Full complex: all seven face stocks active; the shared face `012` mediates six interface connections, with three additional exclusive-face cross-matches.
- Reflective shared-face boundary: the shared-face stock remains a separate **conserved** register and six incident stock transports are switched off; the remaining six-face graph is a triangular prism. There are two zero modes even at `p>0` because the central register is isolated.
- Omitted shared-face stock: the stock space has six face slots (the shared face is not assigned a stock variable), while binary full-closure admission is retained; the exclusive-face graph remains the prism. There is one zero mode for `p>0`.

The exact weighted face-graph Laplacian spectra (`p>0`, multiplicities in parentheses) are

`full: {0(1),3p(1),7p(1),(3+p)(2),(3+3p)(2)}`

`reflective: {0(2),2p(1),3(2),(3+2p)(2)}`

`omitted: {0(1),2p(1),3(2),(3+2p)(2)}`.

At `p=0`, all three geometries have more conserved components; zero multiplicities in the displayed sets must be combined. All three boundary models retain nonnegative stocks and total conservation when their state spaces and flux ports are declared correctly. Altering boundary ownership changes the apparent intercell relaxation rate; no physical selection criterion is supplied by historical files.

## 5. Scientific disposition

**NO-GO_SCOPED:** The source-defined trion gate and U(1)-like seam labels together with gauge covariance, reversal-even attenuation, a positive-stock continuity law, reversible multinomial equilibrium and endpoint-normalized phase response do **not** select a unique pre-event generator. Even with the same phase gate and equilibrium measure, a free pair-invariant donor interaction changes dynamics beyond clock rescaling. Boundary changes independently affect the spectrum.

**Narrow positive result:** We identified the exact additional constitutive assumptions that *would* select a first-harmonic gate conditionally; derived a reversible nonlinear donor family and a measurable-in-model difference in its second temporal derivative; and provided source-budget-preserving controls for alternate topological boundary ownership.

**Reopening gate:** provide a source-derived variational principle, explicit microscopic two-channel amplitude-and-readout law, entropy/cost optimization with a declared unique criterion, or an independently selected native source update. It must determine `q`, `κ`, allowable simultaneous `b/d/x` moves, and event-rate normalizations without empirical target backfitting. Test it with held-out time-domain phase sweeps and changed shared-face boundary conditions. None of these mathematical phase weights is yet a measured electromagnetic coupling or primordial cosmological quantity.

**G05/G06:** untouched. Native packet-to-Hodge map, signed loop source and absolute unit/clock remain **OPEN_GATED**; existing theorem/no-go hypotheses are preserved. **Physical Promotion = 0.**

## 6. Reproduction and provenance

- `python verify.py`: reconstructs two-tetrahedron graph, full finite states and exact transition rates; exhaustive gauge, source-budget, nonnegative and detailed-balance checks; exact SymPy boundary spectra and mode moments.
- `python replay_stdlib.py`: independent implementation using only Python's standard library, `Fraction`, 112-state phase×stock marginal and direct two-step generator moments.
- `results.json`, `run.log`, `replay.log`, and `MANIFEST.json` preserve outputs and source hashes. The source files are bundled in `inputs/` for reproducibility. Constructor-computed exact checks are **not** independent non-constructor review, and code consistency does not prove physical correspondence.
- No historical claims are silently rewritten. This record is submitted as a **draft PR** in UD and UD-Physics, with mainline promotion and manuscript incorporation gated on independent review.
