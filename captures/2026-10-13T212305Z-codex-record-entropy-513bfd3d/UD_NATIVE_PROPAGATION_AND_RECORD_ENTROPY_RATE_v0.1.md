# Native propagation and a declared record-entropy rate

2026-10-12, America/Chicago. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Outcome

The independent-bit boundary assumption is replaced by an explicitly derived **correlated record process**. Under a declared fresh-memory projective recording interaction, native tetrahedral propagation fixes a Markov transition kernel and its information-entropy rate. The sampling interval and record observable remain candidate source choices. No physical heat, universal area normalization, metric horizon or G has been derived.

The sharp new distinction is that the stationary carrier-label chain has positive record-history entropy rate but zero path-reversal entropy production. Record-information accumulation is therefore not interchangeable with thermodynamic entropy production.

## 1. Exact native generator and candidate recording operation

Use the filled tetrahedron, unit metric, fifteen oriented simplex coordinates, and B=D^T−D. Let P0 project onto the uniform four-vertex zero mode. The exact checker verifies

D²=0, B^T=−B, B P0=0, B²=−4(I−P0).

Hence the native propagator at sampling gap Delta is exactly

U_Delta=P0+cos(2 Delta)(I−P0)+(sin(2 Delta)/2)B.

Delta is measured in the declared dimensionless native evolution parameter. A physical clock calibration or a preferred sampling gap is not assumed.

Declare the recording instrument on carrier and a fresh blank record:

R(rho)=sum_j Pj rho Pj tensor |j><j|.

One cycle first applies U_Delta to the carrier, then applies this instrument and retains the new record. This is a mathematical CPTP projection-and-write channel. It may be implemented by coherent copying plus an additional record dephasing/environment operation. Neither that dephasing nor the supply of fresh memory is supplied by the closed skew native generator. This is a declared candidate **open-system interaction**, not a reclassification of native reversible dynamics as irreversible.

The conditional carrier state after a rank-one readout is the indicated basis state. Thus outcome probabilities over repeated cycles are derived from the generator and the instrument, rather than inserted as independent Bernoulli occupations.

## 2. Degree recording in the top-cell/face oscillator

Let e be the unit top-cell vector, f=Be/2. The native invariant plane has B e=2f and B f=−2e. With e labelled 0 and coherent face vector f labelled 1, the propagator is a rotation by 2 Delta. Chain-degree recording restricted to this plane distinguishes these two labels and retains the coherent face superposition.

The recorded transition kernel is

P_degree=[[1−q,q],[q,1−q]], q=sin²(2 Delta).

Starting at e, the final label probability after n cycles is

Pr(Rn=1)=[1−(1−2q)^n]/2.

The history is generally correlated. Nonetheless its Markov conditional entropy is constant:

H(Rn|R1,...,Rn−1)=h(q),
H(R1,...,Rn)=n h(q),

with deterministic R0=0 and h(q)=−q ln q−(1−q)ln(1−q). Thus q and the information-entropy rate are now derived **conditional on the specified native propagator, observable and sampling gap**.

| Gap Delta | q | Information entropy per record, in nats |
|---|---|---|
| pi/12 | 1/4 | 2 ln 2−(3/4)ln 3 |
| pi/8 | 1/2 | ln 2 |
| pi/4 | 1 | 0 |
| pi/2 | 0 | 0 |

The full-transfer clock at pi/4 produces a deterministic alternating sequence and zero history entropy. The return clock at pi/2 also produces zero. The quarter-ray-period sampling pi/8 gives independent fair records. The native oscillation frequency does not by itself select the entropy-maximizing clock.

As Delta→0, q=4 Delta²+O(Delta⁴) and h(q)=q[1−ln q]+O(q²). Therefore h(q)/Delta→0. Arbitrarily frequent recording does not yield an unbounded information-entropy rate in this candidate interaction; the repeated projection suppresses transitions. This is a scoped recording-backaction result, not a physical time law.

## 3. Resolving individual simplices changes the recorded dynamics

Now take rank-one projectors onto all fifteen simplex coordinates. The conditional state after a record is a simplex basis vector, and

P_ij=|(U_Delta)_ji|².

These projectors destroy coherence between the four face coordinates. Unlike degree recording, the conditioned carrier is no longer restricted to the two-dimensional top-cell/face plane. Future propagation explores the full fifteen-dimensional register. The change in entropy rate is an intervention effect, not merely a passive renaming of the same recorded history.

Put c=cos(2 Delta), s²=1−c². The transition probabilities have a simple native form:

- For a vertex, its own probability is (1+3c)²/16; each of the other three vertices has probability (1−c)²/16; each of its three incident edges has probability s²/4.
- For a nonvertex simplex, its own probability is c²; each of its four incident adjacent-degree simplices has probability s²/4.
- All other entries vanish.

The matrix is symmetric and doubly stochastic. When sin(2 Delta) is nonzero, the incidence edges give an irreducible chain; vertex self-loops give aperiodicity for the tested gaps. The unique stationary label distribution is uniform 1/15. This equilibrium is selected by the **candidate unital recording channel**; it is not a derived thermal Gibbs state.

Let Hv be the vertex-row entropy and Hnv the common nonvertex-row entropy. The stationary record-information entropy rate is

h_star=(4 Hv+11 Hnv)/15.

For Delta=pi/4 the row entropies are Hv=(5/2)ln 2 and Hnv=2 ln 2, so

h_star=(32/15)ln 2.

For Delta=pi/6, exact rational probabilities give

h_star=(58/15)ln 2−(7/10)ln 3−(5/24)ln 5.

Both kernels, every row and column sum, the exact entropy log coefficients and finite-history chain-rule calculations are checked. At the same gap pi/4, degree recording has zero rate while simplex recording has a positive rate. A source law choosing the record observable is indispensable.

## 4. Controlled stationary limit from a fixed native initial state

Start from the top-cell basis state rather than assume a stationary ensemble. For the tested simplex kernels, the exact sixth power P^6 has strictly positive entries. Its minimum m gives a Doeblin coefficient alpha=15m, because P^6_ij≥alpha/15 for all i,j.

Total variation distance to uniform contracts by at least 1−alpha every six steps. Therefore, with Hn the n-record history entropy,

|Hn−n h_star|≤(6/alpha) ln 15.

The bound follows by summing deviations of the expected row entropy; each row entropy lies between 0 and ln 15. It is conservative but explicit and does not assume independent records.

For Delta=pi/4, alpha=135/1024, and the transient bound is (2048/45)ln 15. For Delta=pi/6, alpha=24324705/33554432. This proves the limiting information-entropy rate from a declared native pure initial state under the recording intervention.

If the initial label is stationary and included as the first of N records, the exact joint entropy is ln 15+(N−1)h_star. These conventions differ only by initial/transient terms; they must not be mixed when assigning an exact finite-area intercept.

## 5. Positive record entropy does not establish irreversible carrier thermodynamics

At the stationary distribution pi_i=1/15, symmetry gives pi_i P_ij=pi_j P_ji. Consequently the stationary Markov path-reversal relative-entropy rate

sigma_path=k_B sum_ij pi_i P_ij ln[(pi_i P_ij)/(pi_j P_ji)]

is exactly zero; zero-probability terms are omitted. Yet h_star is strictly positive for both tested simplex channels. The current label entropy stays fixed at ln 15 while the retained history entropy grows.

Thus history randomness, storage growth and the stationary label chain's time-reversal irreversibility are distinct quantities. The result does **not** say that the complete measurement, dephasing, memory preparation or erasure apparatus dissipates no energy. Its energetic/environmental bookkeeping is not present in the candidate channel and remains OPEN. Neither sigma_path nor Hn has been identified with a physical horizon Clausius entropy.

For classically dephased records with consistent retained histories, each cycle raises the carrier-plus-retained-record information entropy by the relevant conditional record entropy. A unitary dilation including the omitted environment can instead preserve total von Neumann entropy. The statistical increase cannot be used as a heat law without deriving that environment and its energy exchange.

## 6. Conditional area coefficient with derived correlations

If a source independently assigns one distinct retained record slot to each equal-area boundary tile, and N tiles have A=N a0, then the derived correlated process gives

S_rec(A)=k_B h_star A/a0+O(1), eta_phys=k_B h_star/a0.

For stationary label initialization, the O(1) term is explicitly k_B(ln 15−h_star). For the deterministic top-cell start, it is bounded by k_B(6/alpha)ln 15.

This advances the previous product-bit example: h_star is computed from native propagation and a recording interaction, and correlations are retained. The one-slot-per-tile placement, record sampling gap, observable, physical a0 and identification of the boundary with a causal horizon remain candidate inputs. Recording repeatedly on one fixed patch produces a temporal history, not automatically additional spatial horizon area.

At Delta=pi/4 and equilateral triangular patch area a0=sqrt(3)ell²/4,

eta_phys=128 k_B ln 2/(15 sqrt(3)ell²).

No G or Planck scale entered this expression. It is a conditional coefficient for a specified interaction and metric area, not a universal gravitational normalization.

## 7. Refinement and memory budgets

Geometric subdivision does not automatically create new independent record capacity. If one parent tile with record R is split into m equal-area children and each child carries a redundant copy of R, the child joint entropy is H(R), and their total area remains the parent area. The checker verifies this for biased binary records and m=2,4,8.

Declaring instead m fresh independent children changes the physical/statistical state and multiplies its information entropy. That is not a refinement of the same record state. The exact entropy-rate limit must be compatible with the chosen coarse-to-fine record map.

There is also a finite memory requirement. For degree recording with 0<q<1, every one of 2^n histories has nonzero probability, so exact lossless orthogonal retention requires memory dimension at least 2^n. Deterministic endpoint q=0 or 1 has only one possible history. For simplex recording, the checker counts positive-probability histories recursively and provides the corresponding exact lossless memory lower bounds.

A fixed finite closed memory cannot retain an unlimited complete history. Continuing the process needs additional memory, export, reset or permitted lossy compression, each with an explicit resource/source rule. Those resources are not supplied free by the native incidence generator.

## Disposition and next gate

CHECKED under declared mathematics: native propagator; recording kernels; conditional and stationary information-entropy rates; explicit stationary-limit bound; stationary path-reversal rate zero; redundant subdivision and memory-capacity bounds.

CANDIDATE: the projection/dephasing/write interaction, fresh-memory supply, record observable and clock, tile placement and physical patch metric.

OPEN: a UD-derived recording interaction with energy/environment accounting; source selection of the clock and observable; consistent multi-tetrahedron boundary placement; causal-horizon identification; heat/temperature/entropy bridge; independent physical normalization.

Next, derive an energetically specified carrier–memory–environment interaction and calculate its recorded currents and entropy balance, while deriving a coarse-to-fine boundary placement rule. These are source questions; the positive entropy rate above cannot close them by numerical matching. The ledger, registry and website are unchanged. Physical promotion remains 0; independent review OPEN. The unavailable Genesis image was unused.
