# UD two-shell and tetrahedral-readout observability v0.1

2026-10-16 UTC. Development — no registry entry. Constructor verified. Independent non-constructor review pending. Physical promotion: 0.

## Result and scope

On the same regular 600-cell boundary, Euclidean unit simplex metric and unweighted skew generator A(1,1,1), add an orthogonal second vertex-link shell and one tetrahedral coordinate readout. The augmented ideal history rank is **2498**, leaving **142** hidden dimensions, versus **747** for the original single shell. The new tetrahedral readout removes the hidden stationary three-cycle; all remaining hidden dimensions are oscillatory.

A specific finite protocol uses 125 scalar channels at **8192 equally spaced times**, step **1/2**, through internal time **8191/2**. For the sample stack normalized by 1/sqrt(8192), on the observable Euclidean subspace W, the certified bounds are

    sigma_min(F|W) >= sqrt(3)/2048,
    sigma_max(F|W) <= 1,
    kappa_2(F|W) <= 2048/sqrt(3) < 1183.

The full operator on all 2640 coordinates still has a 142-dimensional kernel and no inverse there. Neither physical time nor physical instrument conditioning is certified by this finite-model result.

## 1. Fixed source, state and observations

Use sorted oriented chains X=C0⊕C1⊕C2⊕C3 with dimensions (120,720,1200,600), no augmentation and no additional four-cell. The dynamics is x'=Ax, with block matrix

    A = [[0,-B1,0,0], [B1^T,0,-B2,0],
         [0,B2^T,0,-B3], [0,0,B3^T,0]].

Here Bk are integer signed simplicial boundaries, A^T=-A, and the chain metric is identity. Initial states are unrestricted real vectors. There is no drive, gating, stochastic disturbance, retriangulation or dissipation. Observations are exact signed simplex amplitudes, with calibration gains one and offsets zero in model units. No coframe or finite-field reconstruction rule is added.

The first centre is dataset vertex 0, quaternion (-1,0,0,0). The selected second centre is vertex 45, quaternion (0,-1,0,0), so their dot product is exactly zero. Observe all vertices, edges and faces of both icosahedral links. The links have disjoint simplex-coordinate sets, giving 124 scalar channels. Add source tetrahedron index 0, oriented simplex **(0,33,34,41)**, global chain coordinate **2040**, as channel 125. It lies in the first centre's closed star.

Let R2 be the 124-row coordinate restriction and R the 125-row augmented restriction, with the tetrahedron last. Their exact index lists are in selected_operators.npz and SELECTION.json. All 125 rows are distinct standard coordinate rows: RR^T=I125 and ||R||2=1. Unit normalization is a declared mathematical metric, not a physical amplitude calibration theorem.

## 2. Placement screen, not a universal optimum

The screen considered one lowest-index representative of each of eight distinct exact dot-product levels relative to the first centre, with the same tetrahedral coordinate fixed in every case. The field was F1009. The results below are screen ranks over that field; the selected observer is subsequently certified over Q. They do not prove optimality over all second vertices, all same-level representatives with the fixed port, or all 600 possible tetrahedral ports.

| Second vertex | Dot product with first centre | Two-shell screen rank | With fixed tetrahedral port |
|---|---|---:|---:|
| 1 | 1/2 | 2449 | 2454 |
| 21 | (1-phi)/2 | 2447 | 2450 |
| 33 | phi/2 | 2335 | 2336 |
| **45** | **0** | **2493** | **2498** |
| 75 | -phi/2 | 2335 | 2336 |
| 87 | (phi-1)/2 | 2447 | 2450 |
| 99 | -1/2 | 2449 | 2454 |
| 119 | -1 | 1893 | 1898 |

Selection rule: largest augmented screen rank, then fewer distinct sensors, then lowest index. This is mathematical observer design, not target-blind physical preregistration or a source-selected natural observer. The original triangle–tetrahedron–icosahedral-link motivation is retained; no fractal dimension or packing law is used.

## 3. Theorem TS1 — Exact kernel reduction

For this selected observer,

| Observer | Snapshot rank | Continuous-history rank | Continuous hidden dimension |
|---|---:|---:|---:|
| Original one-shell readout | 62 | 1893 | 747 |
| Two selected shells | 124 | **2493** | **147** |
| Two shells and tetrahedral port | 125 | **2498** | **142** |

The second shell exposes 600 additional dimensions. The tetrahedral port exposes five more: one stationary dimension, two dimensions at frequency sqrt(3), and two at frequency sqrt(5). The count 600 is a rank increment in this observation problem; it does not identify one recovered coordinate per tetrahedron or imply a physical equality of those differently typed objects.

The exact residual subspace is

    N = intersection_(k=0)^104 ker(R A^k), dim_R N=142.

It equals {x: R exp(tA)x=0 for all real t}. Set W=N^perp, dimension 2498. Since A is real skew and N is A-invariant, W is invariant as well. Data identify the orthogonal observable component Pi_W x, not the unknown full x unless a prior restriction x∈W is supplied.

Proof/certificate: use the degree-53 squarefree Laplacian polynomial q from the preceding vertex-link release. For L=-A², exact arbitrary-precision integer multiplication verifies Rq(L)=0 for all 125 rows. Because q=x q1 and A is skew, R A q1(-A²)=0, a degree-105 recurrence, so derivative powers through 104 suffice for the full history. For every irreducible factor f of q form the row block

    V_f = stack_(j=0)^(deg f-1) [R L^j (q/f)(L); R A L^j (q/f)(L)].

Coprime factors give a direct sum of generated row modules. Exact rational ranks of the thirty blocks sum to 2498. Removing the tetrahedral row from each block gives sum 2493. Each augmented component rank agrees independently over F1009 and F1013. EXACT_RANKS.json contains every component; the screen itself is not used as the characteristic-zero proof.

### Residual spectral dimensions

Only the following rational Laplacian components retain hidden dimensions after augmentation. Ambient multiplicities are inherited from the pinned full source spectrum; new observation ranks are checked exactly here.

| Factor f(L) | Hidden dimension |
|---|---:|
| L-14 | 24 |
| L-12 | 12 |
| L-8 | 4 |
| L-7 | 28 |
| L-5 | 2 |
| L-4 | 4 |
| L-3 | 20 |
| L²-11L+29 | 4 |
| L²-10L+23 | 40 |
| L²-8L+11 | 4 |
| **Total** | **142** |

The stationary kernel of A has dimension two: uniform C0 and the oriented fundamental C3 cycle. The two shells already observe the first. The new tetrahedral coordinate evaluates nonzero on the latter, while the uniform C0 mode has zero value at that coordinate. Both stationary modes are therefore independently visible. This does not imply that arbitrary C3 dynamics is observable.

SURVIVING_DARK_WITNESSES.json explicitly gives a full 24-vector basis for the remaining hidden sqrt(14) component, organized as twelve oscillator pairs x,Ax with

    A²x=-14x, Rx=RAx=0.

The component follows from twelve exact graph eigenvectors at eigenvalue 14 that vanish on both link vertex sets; their gradients vanish on the observed link edges, and their entire motion has no C3 amplitude. The tetrahedral port cannot see these vertex/edge oscillators. The full residual N is provided by exact recurrence constraints and component dimensions, not a dense list of 142 basis vectors.

## 4. Theorem TS2 — Finite sampling rank and temporal frame bound

Use

    t_j=j/2, j=0,...,8191,
    F x=(1/sqrt(8192)) (R exp(t_0 A)x, ..., R exp(t_8191 A)x).

This is 8192 simultaneous 125-channel snapshots, or **1,024,000 scalar amplitude samples**. The final sample is at t=8191/2. These are internal units; no seconds or device bandwidth are inferred.

The observed dynamics has 105 distinct signed frequencies: zero and ±sqrt(mu) for the 52 positive roots of q. Exact Sturm intervals enclose all real roots; frequency separation is approximately at least 0.00428816, with the certified interval in FREQUENCY_CERTIFICATE.json. All phases exp(i omega/2) are distinct, so 105 consecutive sample times would already give the full algebraic rank. No useful condition bound for that shorter protocol is claimed here.

For the 8192-sample certificate, define V_(j,ell)=exp(i t_j omega_ell)/sqrt(8192). Its diagonal Gram entries are one and its off-diagonal entries obey the geometric-series bound

    |(V*V)_(ell,m)| <= 1/[8192 |sin((omega_ell-omega_m)/4)|].

Sturm root isolation and 256-bit Arb interval arithmetic certify a maximum reciprocal-sine row sum C less than 1786, with the sharper enclosed value approximately 1785.76545033. Thus

    epsilon_t=C/8192 < 1/4,
    (3/4) I <= V*V <= (5/4) I.

There is no sampled aliasing among the 105 frequencies. Combining this temporal bound with TS3 gives rank F=2498 and ker F=N exactly. Finite sampling therefore introduces no additional kernel for this particular protocol.

## 5. Theorem TS3 — Certified spatial and complete conditioning bounds

For each positive squared frequency mu, let P_mu be the L spectral projector on the observable part. The relevant compressed real matrices are

    G_mu=R P_mu R^T,  J_mu=R A P_mu R^T.

The positive-frequency output Gram matrix is

    H_mu=(G_mu-i J_mu/sqrt(mu))/2.

At zero frequency use H_0=R P_0 R^T without the factor 1/2. The nonzero eigenvalues of these matrices are the squared singular values of the observation restricted to the corresponding frequency eigenspaces, after removing their exact kernels.

Each compressed projector is evaluated from exact moments using

    P_mu = [q(L)/(L-mu I)]/q'(mu)

on the observation-generated subspace. The numerator denotes polynomial synthetic division, not inversion of a singular matrix. Integer moments R L^k R^T and R A L^k R^T for k=0,...,52 are stored as compressed JSON data. The observer identity Rq(L)=0 makes the formula valid even without replaying a full-carrier characteristic polynomial.

Arb interval matrices enclose the projector entries at 256 bits, starting from exact rational Sturm intervals. Numerical Hermitian eigendecompositions supply approximate eigenvalues and vectors only. To certify them, interpret each binary floating coefficient as an exact constant matrix U, then bound both

    E=U* H_mu U-diag(d),   eta=||U*U-I||2

by certified absolute row sums. The exact component rank supplies the number of positive eigenvalues. Weyl's inequality and the congruence bounds give

    lambda_min_positive(H_mu) >= [d_min_positive-||E||2]/(1+eta).

All 53 zero/positive-root components pass with a common rational bound

    alpha² >= 1/1048576 = 2^-20.

The smallest certified lower enclosure is approximately 1.23142109×10^-6, at the smallest root of mu³-11mu²+33mu-28. This identifies a weak spatially observed mode; it is not a physical decay rate or measured uncertainty. The positive modal ranks sum, with the ± multiplicity, to 2498.

For x∈W, orthogonal frequency decomposition and the temporal frame bound now give

    ||F x||² >= (3/4) alpha² ||x||²
               >= 3/4194304 ||x||².

The upper bound is even simpler: each exp(tA) is orthogonal and R is a coordinate restriction, so the average sampled energy is at most ||x||². Consequently

    sqrt(3)/2048 <= sigma_min(F|W) <= sigma_max(F|W) <= 1,
    kappa_2(F|W) <= 2048/sqrt(3) < 1183.

The certificate is sufficient and conservative; it is not the exact condition number or a claim of optimal sampling duration. It refers to the Euclidean norm on simplex amplitudes and the average-time Euclidean norm on measurements.

## 6. Reconstruction and error contract

For measurements y_j=R exp(t_j A)x+e_j, define aggregate RMS vector error

    delta=[(1/8192) sum_j ||e_j||²]^(1/2).

A least-squares reconstruction constrained to W, equivalently the minimum-norm pseudoinverse on W, satisfies

    ||x_hat-Pi_W x|| <= (2048/sqrt(3)) delta < 1183 delta.

No zero-mean, independence or Gaussian noise assumption is required for this deterministic bound. If instead every scalar channel error is bounded by epsilon, then delta<=sqrt(125) epsilon and the corresponding state-error bound is 1183 sqrt(125) epsilon. The hidden component Pi_N x cannot be bounded from these data alone.

For clock errors |Delta t_j|<=tau while the generator and readout remain exact, the observed frequency range has |omega|<=sqrt(9+3sqrt(5))<4. With w=Pi_W x, Duhamel's identity gives the additional aggregate signal-error bound 4 tau ||w||. Therefore the same reconstruction rule has the sufficient timing-plus-measurement bound

    ||x_hat-w|| < 1183 [delta+4 tau ||w||].

This is a mathematical timing budget in internal time units. Sensor gain/offset errors, finite bandwidth, operator/rate mismatch and physical clock calibration are not estimated here. Their values must be supplied before this becomes an apparatus acceptance protocol. Sampling schedule optimization and a noisy hardware implementation remain open.

## 7. Reproduction and evidence status

Run, with bundled inputs:

    python select.py
    python exact.py
    python frequency_certificate.py
    python spatial_certificate.py
    python summarize.py
    python validate.py

requirements.txt pins the versions used. Imported source scripts are not executed. New scripts construct all calculations from preserved JSON simplex/spectrum data and prior operator data. The exact rank work uses arbitrary-precision integer arithmetic; F1009/F1013 checks are separate corroborations. The conditioning certificate uses interval root isolation, interval matrix arithmetic and rational final bounds; unverified eigensolver values do not serve as proof. validate.py checks fifteen families and constructs explicit residual dark modes.

Sources:

- Immediate parent release: UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1, local Git commit e215561fe155927e22d0997729f465b2604172aa, especially §§2–5. Its source JSON files are preserved by hash. Its one-shell result is the baseline; the new observer does not supersede its theorem.
- Public main snapshot: 3b4ccc26a65b5deef0e917fa8bbadf045649695d. Existing AGENTS.md and relevant 600-cell notes remain applicable. Public GitHub publication is still pending authorization after the prior automatic-review block.
- Underlying PR105 head: 40d56f5f8a54b1ed7b6125209903504f66e9a2a4, exact simplex/action data.
- Underlying PR106 head: 2c4e4c89d25817cb0120916e28014c8b77a5527f, exact spectral factors. Prior full characteristic polynomial replays are not repeated; the new observer annihilator and all new rank/certificate computations are executed.
- Project association: REF01 (#136, metric/observer selection) and APP05 (#144, finite acquisition). Neither issue is closed: native selection and apparatus correspondence remain unresolved.

Implementation corrections before release: NumPy integer scalars in the screen's coordinate lists were converted for JSON serialization after the initial arithmetic completed. The final screen was rerun and captured. No scientific rank value changed. A draft timing-error paragraph initially used sqrt(15) for the frequency ceiling; checking the certified roots identified the true largest squared frequency 9+3sqrt(5). The released timing bound uses the safe ceiling four. The rank and conditioning certificates already used the complete root list and are unchanged; CORRECTIONS.json records this pre-release repair. All written conclusions use the completed exact or interval certificates, not partial progress files.

No new experiment, empirical fit, registry promotion, independent review, main-branch merge or site publication is claimed. The uploaded governance/ledger files are not modified or redistributed; the unavailable Genesis PNG was not used.

## Next gate

The weakest spatial mode, rather than a missing temporal frequency separation, now controls this sufficient bound. Test extra or alternative readouts targeted at that mode and shorten the sample window while preserving a certified reconstruction margin. For an experimental contract, first supply amplitude calibration, noise and timing bounds in measured units. A further boundary-only addition cannot be assumed to remove the remaining 142-dimensional kernel; any proposed port set needs its own rank check.
