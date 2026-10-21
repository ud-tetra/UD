This audit tests whether the previously identified BCC propagation geometry can coexist with strict local propagation and UD event counting. A proposed local update achieves a finite step cone and preserves the leading BCC geometry of all four acoustic branches. It changes the conserved support. The inspected UD sources do not select this update or connect its steps to their cell commits. Physical promotion remains 0.

The new replay passes **69 exact checks and 109 numerical checks**. These establish conditional mathematical properties, not a source-derived mechanism or empirical validation. The retained prior release was recovered and every file checked against its archived SHA256 manifest; unchanged prior tests were not rerun.

## Comparison of the three update laws

| Update | Original squared amplitude norm | Strict graph cone | Leading BCC geometry | Source status |
| --- | --- | --- | --- | --- |
| Native continuous flow exp(s A) | Conserved | No exact cone; distant response tails persist | Yes, for the declared carrier | Inspected continuous comparison branch |
| Proposed local kick and drift Tδ | Changes; a different quadratic form is conserved | Yes in step count | Yes; all four acoustic branches retain their speed ratios | New computational comparison candidate |
| Cayley update Qδ | Conserved | No; one step has arbitrarily distant tails | Same leading geometry | Mathematical comparison candidate |

This comparison is not a theorem that locality and the original norm are incompatible for every possible discrete update. Other schedules and local orthogonal products require their own symmetry, sector, and source audits.

## Carrier and scalar update

Retain the prior periodic tetrahedral complex with one vertex, seven edge types, twelve face types, and six tetrahedra per translation cell. These are six congruent nonregular tetrahedra; no regular tetrahedron tiling or seven-tetrahedron partition is being asserted. Let β=B1(q), with star denoting conjugate transpose in Fourier space and transpose plus inversion of Laurent powers in the exact replay.

The native scalar sector is u_dot=-βp and p_dot=β* u. The candidate replaces continuous evolution by two explicit stages:

```text
p_next = p + δ β* u
u_next = u - δ β p_next

Tδ = [[I - δ² ββ*, -δβ],
      [δβ*,          I ]]

L0 = ββ* = 14I - adjacency
u_(n+1) - 2u_n + u_(n-1) = -δ² L0 u_n
```

The adjacency uses the fourteen displacements ±d, where d runs over the seven nonzero binary triples. One full scalar step expands support by at most one vertex graph hop. For an impulse with zero staggered velocity, use u0 at the origin and u1=(I-δ²L0/2)u0. This startup requires p at the preceding half step to equal -δβ*u0/2. It is an added preparation choice, not the native instantaneous state p=0.

For every integer n the recurrence is a degree n polynomial in adjacency, so its support lies within graph distance n. The exact coefficient at site (n,0,0) is δ^(2n)/2 for n≥1. The replay certifies support and this nonzero front for n=1 through 6 at δ=1/4, 1/8, and 1/16. The general conclusion follows from polynomial degree and the unique length n path to that axial site. No amplitude threshold creates this cone.

## Conservation and stability

The candidate exactly conserves the following modified form:

```text
Hδ = [[I,      δβ/2],
      [δβ*/2,  I   ]]
Tδ* Hδ Tδ = Hδ

Supportδ(u,p) = ||u||² + ||p||² + δ Re(u* βp)
Hδ > 0 when δ² λ_max < 4
```

The positivity condition follows from the Schur complement I-δ²L0/4. The scalar bound λ_max≤28 supplies the sufficient condition δ<1/√7. The three rational δ values are resolution controls, not inferred UD constants.

The original unit norm is not conserved. At the real sign character q=(π,0,0), λ=16. Starting with u=1 and p=0, one δ=1/8 step changes ||u||²+||p||² from 1 to **13/16**, while Supportδ remains exactly 1. This witness uses a different preparation from the zero-velocity impulse experiment above; conservation applies to both.

The cross term changes the interpretation of independent squared amplitude stocks and therefore requires a corresponding accounting and receipt contract. Conservation of Hδ is not conservation of the original support under a new name.

## All propagation modes

Split the 26 chain coordinates into even degrees (0 and 2) and odd degrees (1 and 3). Each side has thirteen coordinates. In this ordering the native generator has the same bipartite form:

```text
A = [[0, -C], [C*, 0]]
C = [[B1,    0],
     [-B2*, B3]]
```

Apply the same kick and drift with C in place of β. The Laurent identity Tδ*HδTδ=Hδ holds exactly for the full 26-coordinate system. Nilpotency B1B2=0 and B2B3=0 makes the squared generator block diagonal in chain degree and retains the scalar lane. The full update is local in the incidence network: each stage crosses one incidence, and a full step crosses at most two. The one-vertex-hop cone above is the more specific scalar result.

An entrywise Fourier bound gives ||C||²≤112 from row bound 14 and column bound 8. The full replay therefore uses δ=1/8, for which 112δ²<4. The less restrictive scalar δ=1/4 is not admitted for the full branch on the strength of this bound.

Every native singular frequency σ becomes a discrete eigenphase ±θ, where θ=2 asin(δσ/2). Thus:

```text
ωδ(σ) = 2 asin(δσ/2) / δ
```

At generic nonzero q there remain thirteen oscillating pairs. At q=0 there are nine optical pairs and eight stationary coordinates. All four acoustic branches keep their leading squared frequencies Q, Q/8, Q/8, Q/24, where Q=qᵀ(2I+2J)q. The replay checks the complete eigenphase map at three nonzero wavevectors and the four small-q ratios at two resolutions. A shared metric shape does not make their speeds equal. The optical frequencies remain finite in native units; under the scalar continuum clock below they scale as 1/a, so no finite physical optical interpretation is supplied.

## Continuum clock and error

Retain the supplied unit-covolume embedding E=4^(-1/3)(J-2I). Its leading scalar inverse propagation tensor is E(2I+2J)Eᵀ=κI, with κ=2^(5/3). Let the spatial refinement scale be a, take q=aEᵀk, and **supply** the clock increment Δt=aδ. This is a refinement contract, not a derivation from commits or a calibration to seconds.

```text
Ω_(a,δ)(k) = 2 asin(δ sqrt(λ(aEᵀk))/2) / (aδ)
Ω_(a,δ)(k) → sqrt(κ) |k| as a → 0 at fixed stable δ
```

For the scalar lane this clock also gives a strict envelope in the propagation metric G=(2I+2J)^(-1). Here x=a times the lattice site, before applying E. The largest squared neighbor length in G is 1/2. Hence d_G(x)≤a n/√2 at step n and the envelope speed is at most 1/(√2δ). This is a sufficient support bound, not the long-wavelength wave speed. The embedding and metric units are supplied conventions.

The change from the native scalar frequency is bounded pointwise by:

```text
0 ≤ ωδ - sqrt(λ)
  ≤ δ² λ^(3/2) / [24 (1-δ²λ/4)^(3/2)]
```

Divide this bound by a for Ω versus the native refined frequency. It follows by integrating an upper bound on the derivative of asin, and is valid when δ²λ<4. It gives order δ²a² error at fixed k. For a matched zero-velocity scalar Fourier component and a common horizon t, the cosine response error is at most |t| times this physical-frequency bound. This is a scalar response bound, not a bound on arbitrary full-state detector readouts.

At δ=1/4, along a Cartesian axis with |k|=1:

| Mesh a | Steps to t=1 | Candidate frequency | Absolute continuum error |
| --- | --- | --- | --- |
| 1/8 | 32 | 1.780876796 | 0.000920640 |
| 1/16 | 64 | 1.781567263 | 0.000230174 |
| 1/32 | 128 | 1.781739892 | 0.000057544 |

The continuum value is 1.781797436. The machine result contains the unrounded values. Tests cover three directions, three mesh scales, and three δ values; all show second-order convergence and satisfy the analytic native-frequency error bound.

Finite-wavelength anisotropy remains. Write λ(aEᵀk)/a²=κ|k|²+a²C4(k)+O(a⁴). The time update changes the quartic term to C4(k)+δ²κ²|k|⁴/12. Its addition is isotropic. For unit axis and diagonal directions, C4 is respectively -5r⁴/3 and -11r⁴/9, where r=4^(-1/3). Their difference -4r⁴/9 is unchanged. Local time discretization does not select the embedding or erase its lattice anisotropy.

## The norm preserving comparison retains tails

For the native skew-adjoint A, define Qδ=(I-δA/2)^(-1)(I+δA/2). Algebra gives Qδ*Qδ=I. On the scalar impulse its vertex block is 2R-I, with R=(I+zL0)^(-1) and z=δ²/4.

```text
R = 1/(1+14z) sum_(m≥0) [z/(1+14z)]^m adjacency^m
```

All coefficients are nonnegative and the series converges because 14z/(1+14z)<1. For site (d,0,0), d≥1, a length d path gives a strict one-step response lower bound 2[z/(1+14z)]^d/(1+14z)>0. The replay retains rational lower bounds for d=1 through 6; the argument covers every d. Numerical checks also verify the original norm identity on the full branch. This preserves norm through an inverse operator that spreads response to arbitrary graph distance.

## What the inspected UD sources admit

The source baseline is the recovered manuscript version 9, the minimum time model v0.11, and the two event-generator audits listed in the source index. These are inspected files, not a claim that every canonical source has been exhausted.

| Required bridge | Source finding | Admission status |
| --- | --- | --- |
| State correspondence | The chosen finite branch has binary decorations on tetrahedral cells and four readiness predicates per cell. The continuous branch has real amplitudes on chains. | No map supplied; primal vertex and dual cell variables differ |
| Update correspondence | Four face preparations enable one cell flip and reset; preparations count zero and the commit counts one. | Does not select kick and drift or one stencil step per commit |
| Conserved support and receipts | The continuous branch uses the unit chain metric; the retained event apparatus has active buffers and backpressure. | Hδ and its cross-term accounting need independent provenance |
| Clock and refinement | Event granularity and admissible history equivalence are supplied; readiness erasure is only a scoped abstraction. | Δt=aδ is an added contract; no physical duration selected |
| Metric selection | Incidence supplies no length, inverse metric, or preferred coordinates. | BCC embedding remains conditional |
| Generator normalization | Symplectic/permutation geometry permits frequency freedom; the natural cotangent lift remains a candidate with kinetic and potential maps open. | No event-frequency value may be imported as δ |

These findings agree with the minimum time model Sections 2, 3, 5, and 7; manuscript Sections 1A and the four-face refinement discussion; the event pushforward audit; and the S5 neutral lift audit. The bundle pins the full source bytes and their SHA256 values.

There is also a specific encoding obstruction. At q=(π,0,0) and δ=1/8, a nonzero scalar oscillating mode has 2cos(θ)=7/4. If its rotation had a finite orbit, its eigenvalue would be a root of unity, making 2cos(θ) an algebraic integer. A rational algebraic integer must be an integer, whereas 7/4 is not. Therefore this mode has no nonzero finite orbit.

Consequently, no encoding depending only on a finite control state can represent this nonzero mode for an unbounded sequence of fixed candidate steps: some control state must recur while the amplitude orbit does not. This conclusion assumes one fixed candidate step for each modeled update and an encoding of current finite control alone. It does not exclude history-dependent encodings, growing counters or records, different schedules, bounded horizons, approximations, or other dynamics. The instrumented event source already includes potentially unbounded records, so this is not a no-go theorem for UD as a whole.

## Next source test

The next target is an explicit state and history map Φ plus an admitted event grouping for which advancing the chosen event group makes Φ advance by the candidate update. A complete test must specify how preparation, commits, retained receipts, and backpressure enter Φ, and prove conservation and causal continuation under that map. If Φ depends on history, its memory carrier and capacity must be stated. A current-boundary match is insufficient.

Two concrete outcomes are admissible: a source-derived map and law, or a separately justified new axiom with a narrower claim. Until then the result is that causal local updates can support the BCC interpretation conditionally; UD has not internally selected the geometry, amplitude update, common physical speed, or elapsed duration.

## Replay and limitations

Run `python verify_ud_bcc_causal_update_v0_1.py --out replay_results` with Python and NumPy. The two unchanged helper scripts must be beside the verifier. The release includes the source snapshots, prior audit and results, candidate contract, current results, and a SHA256 manifest. Exact checks use rational Laurent algebra and finite support arithmetic. Numerical tolerances test dispersion and convergence on the declared samples; they do not prove uniform continuum convergence for arbitrary fields, boundaries, or observations. No independent mathematical review or empirical test occurred.

## Saved audit files

[UD_BCC_CAUSAL_UPDATE_AND_EVENT_BRIDGE_AUDIT_v0.1.md](library-file:file_00000000f05881f6a8ef268ec327763d)

[UD_BCC_CAUSAL_UPDATE_RESULTS_v0.1.json](library-file:file_0000000023c481f6a7e2c785896b69ca)

[UD_BCC_CAUSAL_UPDATE_CONTRACT_CANDIDATE_v0.1.json](library-file:file_000000002d1c81f6b9cc08d882e91ada)

[UD_BCC_CAUSAL_UPDATE_v0.1_RELEASE.zip](library-file:file_0000000009d481f6a5d0b3cade3efd18)

[UD_BCC_CAUSAL_UPDATE_v0.1.sha256](library-file:file_0000000017a481f6ab342a63eab315b8)