# UD full-state third-shell observability theorem v0.1

2026-10-16 UTC. Development — no registry entry. Constructor verification: exact finite arithmetic and certified interval bounds. Non-constructor independent review: pending. Physical promotion: 0.

## Result and fixed model

For the regular 600-cell boundary, the existing unit simplex metric and unweighted skew Hodge–Dirac generator A(1,1,1), three selected vertex-link shells, the retained tetrahedral port and three additional simplex ports give a **189-channel observer with history rank 2640 and zero dynamical kernel**. The previous observer's 142 hidden dimensions are all exposed.

For 8192 simultaneous snapshots at t_j=j/2, normalized by 1/sqrt(8192), the complete-state sample map satisfies

    sigma_min >= sqrt(3)/512, sigma_max <= 1,
    kappa_2 <= 512/sqrt(3) < 296.

A second sufficient protocol uses only **2048 snapshots** at the same spacing, with complete-state condition number less than **725**. These are mathematical sufficient bounds, not exact measured condition numbers, minimum sample counts or physically calibrated timing.

The carrier remains X=C0⊕C1⊕C2⊕C3 over R, dimensions (120,720,1200,600), total 2640, one sorted oriented simplex per coordinate. The generator has upper adjacent-degree blocks -Bk and lower blocks Bk^T. It is real skew in the identity metric. There is no gate, forcing, dissipation, rate change, retriangulation or change of state convention in this release. All simplex-amplitude readouts have unit gain and zero offset by declaration. The evolution parameter is internal model time.

## 1. Exact observation specification

Retain the two earlier centres 0 and 45 and the tetrahedral amplitude at global coordinate 2040, simplex (0,33,34,41). Add the link of vertex **66**. Exact unit-quaternion centre coordinates are

    v_0=(-1,0,0,0),
    v_45=(0,-1,0,0),
    v_66=(0,(1-phi)/2,-1/2,-phi/2), phi=(1+sqrt(5))/2.

Thus the third centre is orthogonal to the first; its inner product with the second is (phi-1)/2. Its label is a dataset index, not an inferred physical address. All vertices, edges and faces of all three links are observed. Together with the retained tetrahedral coordinate this gives 186 distinct channels.

The following additional readouts are selected in this order:

| Port | Global coordinate | Oriented simplex | Gain in history rank |
|---|---:|---|---:|
| Triangle amplitude, degree 2 | 928 | (2,67,88) | 8 |
| Edge amplitude, degree 1 | 152 | (2,67) | 4 |
| Vertex amplitude, degree 0 | 4 | (4) | 2 |

The complete readout R has **36 vertex, 91 edge, 61 face and 1 tetrahedral channels**, all distinct coordinate rows. Its ordered coordinate list is in RESULTS.json and operators.npz. RR^T=I189. Its snapshot rank is 189 and its snapshot kernel has dimension 2451. Full reconstruction below uses the known evolution and measurement history; no static 189-to-2640 inverse is asserted.

## 2. Selection procedure and exact stage ranks

The finite-field design screen tested all **118 remaining third-centre vertices** against the previous observer's 142-dimensional hidden subspace. All three proposed additional port types were eligible in a subsequent greedy search across the 2640 coordinate readouts. At each step the search maximized the additional history rank; ties used the lowest coordinate. The selected third centre maximized screen rank, then minimized distinct channel count, then minimized index. Sixteen tested centres tied for highest third-shell screen rank; the channel-count/index rules selected 66.

This is an exhaustive third-centre screen for the fixed baseline followed by a greedy port construction. It is not a proof of a globally minimum sensor set or of optimal triples/port combinations. Screening used F1009; the chosen ranks are separately established over characteristic zero.

### Theorem FS1 — Complete observability

| Observer stage | Scalar channels | Exact history rank | Exact hidden dimension |
|---|---:|---:|---:|
| Previous two-shell observer plus tetrahedral port | 125 | 2498 | 142 |
| Add third shell | 186 | 2626 | 14 |
| Add triangle port | 187 | 2634 | 6 |
| Add edge port | 188 | 2638 | 2 |
| Add vertex port | 189 | **2640** | **0** |

The third shell exposes 128 dimensions, followed by increments 8,4,2. Port gains count recoverable state coordinates over histories, not instantaneous output dimensions. A single scalar oscillator readout can distinguish two initial quadratures through time.

There are two independent exact routes to the final rank:

1. Direct finite-field Krylov matrices stack R,RA,...,RA^31 and have full column rank 2640 over both F1009 and F1013. Each full modular rank certifies a nonzero integer minor. Rank over Q, R and C is at least 2640 and cannot exceed the 2640 columns, so it is exactly 2640. No rational upper-rank inference from merely matching deficient modular ranks is used.
2. Rational history-Gram ranks on coprime Laplacian components certify every selected intermediate stage, as detailed below. Their sums are 2626,2634,2638,2640.

Consequently

    intersection_(k=0)^31 ker(RA^k)={0},
    R exp(tA)x=R exp(tA)y for every t iff x=y.

The first identity is a finite derivative certificate, not a requirement to estimate 31 derivatives in the sampling protocol.

### Rational stage proof

Let L=-A² and let q be the same degree-53 squarefree polynomial used in the parent release. Exact integer multiplication verifies Rq(L)=0 on all 189 readouts. Full observability and commutation imply q(L)=0 on the entire carrier: all rows RA^j annihilate q(L), and those rows span the full dual space. This independently certifies the full-carrier annihilator.

For each irreducible factor f of q, use a rational Chinese-remainder projector P_f(L). For history rows R L^j P_f and R A L^j P_f, with j=0,...,deg(f)-1, the Gram blocks are

    [[G_(j+k), -J_(j+k)],
     [J_(j+k),  G_(j+k+1)]],

where G_s=R L^s P_f R^T and J_s=R A L^s P_f R^T. Because A is skew, L is symmetric and P_f is an orthogonal spectral-component projector, this is positive semidefinite and has the same rank as the history rows. A positive common denominator gives an integer matrix; FLINT exact integer rank establishes its rational rank. Selected sensor subsets give the intermediate-stage ranks. Components already fully observed by the parent remain full under inclusion of readouts. STAGE_RANKS.json records these dependencies and every component rank.

After adding the third shell the fourteen remaining hidden dimensions are:

| Squared frequency | Hidden dimension |
|---|---:|
| 14 | 4 |
| 8 | 2 |
| 7 | 4 |
| 4 | 2 |
| 3 | 2 |

The face port removes two dimensions at each of squared frequencies 8,7,4,3. The edge port removes two each at squared frequencies 14 and 7. The vertex port removes the final two at squared frequency 14. This is a typed statement about this generator and observation set, not a universal functional assignment to shapes.

FINAL_PORT_WITNESS.json provides an exact surviving oscillator pair just before the last port: A²x=-14x, all first 188 readouts vanish on x and Ax, but x_4 is nonzero. Thus the final vertex waveform recovers both quadratures of that particular ambiguity. The complete observer has no surviving hidden mode.

## 3. Theorem FS2 — Independent spectral-dimension certificate

The new conditioning computation does not simply assume prior modal multiplicities. The replay evaluates 240 quaternion left/right multiplication maps, with overlaps between the two families; this is an evaluation count, not the symmetry-group order. The replay verifies that each maps every simplex to a simplex and that their generated orbits are transitive separately on vertices, edges, faces and tetrahedra. Signed simplex actions are chain automorphisms by boundary naturality; they are orthogonal in the unit metric and commute with L.

It follows that every diagonal entry of L^k is constant within each chain degree. Since at least one simplex of every degree is observed, the exact observed moment matrices supply

    Tr L^k = 120 (L^k)_(v,v) + 720 (L^k)_(e,e)
             +1200 (L^k)_(f,f)+600 (L^k)_(tau,tau).

For a rational projector P_f(L), its trace equals its ambient dimension. Exact polynomial arithmetic and the stored integer moments compute all thirty dimensions. They sum to 2640 and match the prior characteristic-multiplicity record. The two harmonic dimensions and the signed nonzero-frequency dimensions used below are thereby independently checked. MODAL_DIMENSIONS.json stores the projectors, denominators, exact traces and dimensions.

This trace argument requires the actual unit-incidence model and verified grade transitivity. It is not imported into a nonuniform metric or gated complex without a new check.

## 4. Theorem FS3 — Complete finite-sample conditioning

Define

    F_M x=(1/sqrt(M)) stack_(j=0)^(M-1) R exp(jA/2)x.

All norms here are Euclidean chain-amplitude norms and average-time output norms. The 105 distinct frequencies are zero and the two signs of sqrt(mu) for every positive root of q. Their nodes exp(i omega/2) are distinct. The temporal Gram off-diagonal bound is

    |(V*V)_(a,b)| <= 1/[M |sin((omega_a-omega_b)/4)|].

Exact Sturm intervals and 256-bit Arb arithmetic certify a maximum reciprocal-sine row sum C less than 1786; its enclosed value is approximately 1785.76545033. Therefore temporal frame eigenvalues lie between 1-C/M and 1+C/M whenever the lower bound is positive.

For each squared frequency mu, the compressed positive-frequency spatial Gram is

    H_mu=[R P_mu R^T-i R A P_mu R^T/sqrt(mu)]/2.

At zero use H_0=R P_0 R^T. Synthetic division of q and exact moments evaluate the compressed projectors without singular matrix inversion. The full rank certificate shows that no frequency eigenspace has a hidden vector, so their nonzero dimensions follow from FS2.

Arb interval matrices enclose each H_mu at 256 bits. Approximate numerical eigenvectors U are treated as exact binary constants only to form a test congruence. Certified row-sum bounds on U*H_mu U-diag(d) and U*U-I, together with the exact modal ranks and Weyl/congruence bounds, certify all positive eigenvalues. No unverified numerical eigenvalue is used as proof.

Across all 53 zero/positive-root components,

    alpha² >= 1/65536 = 2^-16.

The smallest certified lower enclosure is approximately 2.32918827112×10^-5, at squared frequency three. The rational common bound is deliberately rounded down. Its power-of-two denominator is bookkeeping for a proved inequality, not a new structural coupling or physical constant.

For every state x and temporal bound epsilon_t<1,

    ||F_M x||² >= (1-epsilon_t) alpha² ||x||².

Also ||F_M x||<=||x|| because each propagator is orthogonal and R is a coordinate restriction. Thus the following sufficient profiles are certified:

| Snapshots M | Last internal time | Scalar samples | Certified sigma_min lower | Certified kappa_2 upper |
|---:|---:|---:|---|---:|
| **2048** | **2047/2** | **387072** | **1/(512 sqrt(2))** | **<725** |
| 4096 | 4095/2 | 774144 | 1/(256 sqrt(2)) | <363 |
| **8192** | **8191/2** | **1548288** | **sqrt(3)/512** | **<296** |

For these rows respectively, C/M is below 7/8, 1/2 and 1/4. The sample count, rational temporal bounds and common spatial bound are recorded in SCHEDULE_CERTIFICATES.json. All three finite sample operators have **rank 2640 and kernel zero**. The upper singular value bound is one.

The shorter 2048-snapshot profile uses one quarter as many scalar samples as the primary 8192-snapshot profile. These are sufficient choices; no globally shortest protocol or exact condition number is claimed. The earlier two-shell bound less than 1183 applied only to its observable subspace, whereas these new bounds apply to all 2640 state coordinates.

## 5. Reconstruction and deterministic error contract

For the selected profile, let measurements be y_j=R exp(jA/2)x+e_j and define

    delta=[(1/M) sum_j ||e_j||²]^(1/2).

Least squares using the normalized sample map now recovers the full initial state, with no hidden-state prior:

    ||x_hat-x|| < K delta,

where K=725,363,296 for M=2048,4096,8192 respectively. No zero-mean, Gaussian or independence assumption is needed. If every scalar error is bounded by epsilon, delta<=sqrt(189) epsilon.

For sampling-time errors bounded by |Delta t_j|<=tau, the full observed frequency band obeys |omega|<=sqrt(9+3sqrt(5))<4. Exact skew propagation gives the additional signal-error budget 4 tau ||x||, hence

    ||x_hat-x|| < K [delta+4 tau ||x||].

These bounds presume the declared generator, chain metric and coordinate gains. They do not estimate physical calibration, gain/offset error, bandwidth, rate/metric mismatch, instrument resources or seconds per internal time unit. Those require separate source and uncertainty contracts before hardware qualification. Recoverability of this finite model does not identify a fundamental physical substrate.

## 6. Provenance, reproducibility and limitations

- Immediate parent: local commit 506b7473cb43ef0aac974aae50936f28fe5aa3de, UD_TWO_SHELL_TETRAHEDRAL_OBSERVABILITY_v0.1. Its 2498-rank observer and exact component record are retained as dependency, not overwritten.
- Earlier baseline: local commit e215561fe155927e22d0997729f465b2604172aa, UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.
- Public main refreshed and unchanged at 3b4ccc26a65b5deef0e917fa8bbadf045649695d. Public source-data heads remain PR105 40d56f5f8a54b1ed7b6125209903504f66e9a2a4 and PR106 2c4e4c89d25817cb0120916e28014c8b77a5527f.
- All imported objects are JSON/matrix source data; no archived executable is run. The historical uploaded ledger and governance proposal are not changed or redistributed. The unavailable Genesis PNG is unread and unused.
- Project association remains REF01 (#136) and APP05 (#144). Native observer selection and measured apparatus correspondence are not closed by this ideal construction. Public GitHub publication remains pending authorization after the earlier approval-review block.

Run the new scripts in this order:

    python select.py
    python verify_rank.py
    python moments.py
    python modal_dimensions.py
    python stage_ranks.py
    python frequency_certificate.py
    python spatial_certificate.py
    python schedule_certificates.py
    python summarize.py
    python validate.py

requirements.txt pins the runtime versions. Exact full-rank checks use two primes, and selected intermediate ranks use rational PSD Gram calculations. Integer moments verify the observer annihilator. Exact quaternion automorphisms and trace projectors independently check modal dimensions. Interval temporal and spatial certificates establish rational final bounds. validate.py checks eighteen families and constructs the exact final-port witness. Clean replay reproduces the certificate pipeline from preserved integer moments; full field-rank and moment-generation runs are separate executed checks.

The full kernel result is scoped to A(1,1,1), the unit chain metric, this 189-coordinate readout and its known evolution. No minimality of sensor count or protocol length, physical calibration, independent review or registry promotion is asserted. Physical promotion remains 0.

## Next gate

Certify tolerances to generator/rate, metric and readout mismatch, using a declared state/noise budget, before turning this ideal full-state protocol into an experimental acceptance contract. A sensor/time-cost optimization can then compare the three sufficient profiles or search for smaller designs while retaining a specified reconstruction margin.
