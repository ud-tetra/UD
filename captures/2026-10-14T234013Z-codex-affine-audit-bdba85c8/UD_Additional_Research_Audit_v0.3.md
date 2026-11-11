# Additional research audit: affine control closure, phase extensions and conditional transport

14 October 2026. Constructor-checked development; no independent review, registry promotion or physical promotion. Companion to narrative manuscript v0.12. Imported partner-LLM statements are claims to check, not sources of established physics.

## Inputs and recovery

This batch contains `1, 2, and 3(9).docx` (S9), `1, 2, and 3(10).docx` (S10), and `1, 2, and 3(11).docx` (S11). Original bytes, hashes, paragraph text, and original Office Math XML are preserved. Paragraph anchors below are zero-based body-paragraph indices, including empty paragraphs. Plain-text extraction flattens equation layout; use the preserved originals and XML when interpreting an equation. No imported code was executed. The supplied coefficient ledger v0.39 and CRL2 governance proposal are historical inputs with explicit development scope. They do not supersede the October manuscript evidence. The unavailable `Gap2_FINAL_Finite_Genesis.png` is excluded.

The baseline is the narrative manuscript v0.11, Library version 3, and its fine-history package. The current batch supplies no native physical carrier map, action calibration, bath implementation, entropy-area normalization or gravitational correspondence. In particular, the ledger's orientation sign is not an integer winding counter; its legacy `13*pi^2` entry does not derive a new physical phase sector.

## Dispositions

| Source and anchors | Claim | Finding and destination |
|---|---|---|
| S9 P79–109 | Four-terminal cyclic scattering has quantized Hall resistance and zero longitudinal resistance | Correct for the declared permutation network and reservoir/probe convention. Keep as conditional audit example; not a derivation from UD or Weyl chirality. |
| S9 P110–140 | 144 FO comparisons give a uniform winding/burden step | Counts correct; winding inference unsupported. Only 72 pairs admit either weight-compatible ordering in the all-open receipt graph, 36 in each specified direction. |
| S9 P141–176 | Order-104 semidirect group and finite-field decomposition | Group order and 29 complex irreducibles correct for the declared nontrivial action; the stated F7 algebra has dimension 56, not 104. Corrected below. |
| S10 P37–68 | Boolean affine group, central C13 extension and modular representations | Affine action follows from composition of the existing controls: integrate into D.14. Optional C13 extension and its algebra are conditional constructions, not native winding. |
| S10 P69–101 | 144 FE comparisons imply a fixed deactivation cost | Counting correct; direction, starting winding, and work interpretation require separate declarations. |
| S10 P102–136 | Ideal chiral scattering is noiseless | Zero-temperature, zero-frequency partition noise vanishes for a permutation scattering matrix. This does not remove finite-temperature noise, contact dissipation or apparatus resources. |
| S11 P79–106 | An eight-terminal unitary interpolation preserves a Hall ratio and predicts a universal noise peak | Exact DC solution verified for this network on 0<z<1. Endpoints need qualifications; noise formula mixes current normalizations and omits fluctuating voltage-probe conditions. Keep in audit. |
| S11 P107–132 | OO/EE partitions give invariant physical sectors and modulus 5/12 | Combinatorial partition correct. A label partition is not an invariant operator sector without an operator-preservation proof; the ratio is not a derived modulus. |
| S11 P133–156 | Affine extension has vanishing Schur multiplier and therefore no anomalies | False vanishing claim: explicit nontrivial U(1) projective cocycle below. A selected ordinary representation remains ordinary on pullback, but does not classify all projective representations or physical anomalies. Integrate the limited counterexample into D.14. |

## 1. Composition is the useful new bridge

For Theta=F2^3, primitive controls are theta -> P_g theta xor xi, with g in S3 and xi either zero or one of three unit vectors. There are 24 distinct primitive transformations. They generate all 48 affine transformations, because unit translations generate F2^3. The action is faithful. This closes an algebraic composition question for the reference graph already used in v0.11; it does not close native source formation or admission.

Centering the Boolean cube identifies this signed-permutation group with C2 x S4 using determinant sign and the permutation of its four body-diagonal lines. The kernel of the latter permutation is {I,-I}; determinant separates those two. The replay checks the bijection and all 2,304 multiplication pairs. The manuscript provides a proof independent of the replay.

Primitive words carry more information than endpoint actions. The empty word and a double flip both act as the identity but have lengths zero and two. Any elapsed-time, supplied-control, work or retained-winding claim must declare which history data it needs. The central C13 extension does not solve this problem: its characters provide phase residues, not an integer lift.

## 2. The missing finite-field block

Declare G=(V4 x C13) semidirect C2, where the involution swaps the two coordinates of V4 and inverts C13. This group has order 104; rotation acts trivially on V4. It is not the direct product with a trivial reflection action. An explicit enumeration gives conjugacy-class sizes: two classes of size 1, two of size 26 and 25 of size 2. Hence there are 29 complex irreducibles: four linear and 25 of dimension two. There is no quotient S3 because 6 does not divide 104.

For F7, use the characters (k,chi) of the normal abelian subgroup C13 x V4. Reflection sends (k,chi) to (-k,swap(chi)). Two fixed characters at k=0 each extend with either involution sign, giving four linear representations. All other reflection orbits have size two and induce two-dimensional complex representations. Frobenius multiplies k by 7 and fixes the V4 characters. On the 25 induced representations its orbit lengths are 1,6,6,12. The size-12 orbit occurs for the pair of nonfixed V4 characters and is absent from the source's decomposition. Thus

\[
\mathbb F_7[G]\cong 4\mathbb F_7\oplus M_2(\mathbb F_7)
\oplus 2M_2(\mathbb F_{7^6})\oplus M_2(\mathbb F_{7^{12}}).
\]

The dimensions are 4+4+48+48=104. The source's expression totals only 56. Simple-module dimensions over F7 are 1 (four times), 2 (once), 12 (twice), and 24 (once); regular multiplicities are the matrix sizes 1 or 2, not these extension-field dimensions. Independent orbit enumeration is in the replay.

For G_aff the isomorphism C2 x S4 gives the split algebra 4F7 + 2M2(F7) + 4M3(F7), dimension 48: the standard rational S4 irreducible dimensions are 1,1,2,3,3, duplicated by C2. Tensoring with F7[C13]=F7 + F(7^12) gives the conditional order-624 algebra, dimension 48+576. Dimension consistency alone is not a physical realization or phase-selection law. The replay checks the orbit calculation and dimensions; it does not construct every irreducible matrix for the order-624 group.

## 3. A decisive projective counterexample

Write G_aff as C2 x S4 and set delta=the C2 coordinate, p=the permutation parity in S4. With Pauli X,Z define R(g)=X^delta(g) Z^p(g). Then

\[
R(g)R(h)=(-1)^{p(g)\delta(h)}R(gh).
\]

Both exponents are additive mod 2, proving the normalized cocycle identity. A central inversion (delta=1,p=0) and an odd permutation with delta=0 commute as group elements; their lifts X and Z anticommute. A change of projective phase cannot alter the commutator of lifts of commuting elements. Therefore this U(1) cocycle is not a coboundary. The same witness extends across C13 by letting that factor act trivially.

This is sufficient to refute the source's zero-projective-class premise without relying on a table of Schur multipliers or asserting a full classification. The replay checks every 48^3 triple and the exact matrix witness. Semisimplicity in characteristic 7 does not imply vanishing projective cohomology. A physical gauge anomaly is a separate question requiring physical fields and an action. None is calculated here. Ordinary representation pullback remains an ordinary representation; that limited statement does not justify the source's broader conclusion.

## 4. Conditional DC transport survives; its physical interpretation does not follow

With I=(e^2/h)(I-T)V, T_ij=|S_ij|^2, take terminals 1 and 3 as source/drain, V3=0 and all other DC currents zero. For the four-terminal cycle S with nonzero entries S12=S23=S34=S41=1, the solution is (V1,V2,V3,V4)=(1,0,0,1) I h/e^2. Thus Rxy=(V2-V4)/I=-h/e^2 and R14=0 under that sign convention. The source assumes this network; it does not derive it from the UD carrier. Zero longitudinal drop does not imply zero source power: I(V1-V3)=I^2 h/e^2 is supplied and dissipated by the full reservoir/contact system.

For S11 define z=t^2, u=sqrt(1-z), v=i sqrt(z). The nonzero entries of S are

\[
S_{12}=S_{23}=S_{34}=S_{41}=S_{58}=S_{65}=S_{76}=S_{87}=u,
\]
\[
S_{15}=S_{26}=S_{37}=S_{48}=S_{51}=S_{62}=S_{73}=S_{84}=v.
\]

The matrix is unitary on 0<=z<=1: each column has norm one, and overlapping columns have inner product uv*+vu*=0. The replay verifies the exact identity before imposing u^2+t^2=1. Solving the stated DC probe problem for 0<z<1 gives the potentials in units I h/e^2:

\[
V=\left(\frac1{1-z},\frac z{2(1-z)},0,\frac{2-z}{2(1-z)},
\frac{1+z}{2(1-z)},\frac1{2(1-z)},\frac12,\frac1{2(1-z)}\right).
\]

Consequently Rxy=-h/e^2, G_two=(e^2/h)(1-z), and R14=(h/e^2)z/[2(1-z)]. The Hall relation is exact for this constructed family, not a theorem for arbitrary unitary perturbations. At z=0 the right-hand contacts disconnect and their absolute voltages are undetermined; the displayed values there are limits. At z=1 source and drain lie in disconnected components, so the nonzero imposed source current has no stationary solution. Fixed-current power is I^2(h/e^2)/(1-z); it grows rather than vanishes.

The replay verifies the symbolic DC solution, unitarity and endpoint ranks. It does not derive this scattering network from the tetrahedral generator, specify a microscopic contact apparatus or establish a universal Hall law.

## 5. Correct noise normalization and the remaining probe problem

For a declared coherent single-channel, two-terminal, zero-temperature, zero-frequency binomial benchmark, let Gamma be the incident attempt rate and T its transmission probability. Independent transmitted counts have variance Gamma*tau*T(1-T) over time tau. With the conventional spectral normalization S=2 lim Var(Q)/tau,

\[
I_0=e\Gamma,\quad I=I_0T,\quad
S=2eI_0T(1-T)=2e|I|(1-T).
\]

For T=1-z, fixed incident current I0 gives S=2e I0 z(1-z), peaking at z=1/2. Fixed transmitted current I instead gives S=2e|I|z, with no interior maximum in this idealized parametrization. Maintaining that fixed current as z approaches one requires unbounded voltage; the benchmark does not justify that physical extrapolation. The source uses I as the transmitted DC current in its voltage solution and as incident current in its noise formula. These conventions cannot be interchanged.

The two-terminal benchmark is not automatically the eight-terminal answer. Floating voltage probes require their own fluctuation constraints, noise correlations and measurement bandwidth; their effective DC conductance is not generally a coherent transmission eigenvalue. Full eight-terminal probe-noise closure remains OPEN. Deterministic permutation scattering has no zero-temperature partition randomness, but this does not remove thermal or apparatus noise. For technical context: M. Büttiker, “Scattering theory of current and intensity noise correlations in conductors and wave guides,” Phys. Rev. B 46, 12485 (1992), DOI 10.1103/PhysRevB.46.12485. The binomial calculation above is independently specified and derived, not an extraction of a UD correspondence.

## 6. Counting, winding and resource accounting

FO and FE each have 144 Cartesian label comparisons. At a prescribed ordering F then O (or F then E), weight compatibility leaves 36; reversing the order gives another disjoint 36. Hence 72 allow either ordering in the declared reference graph. Counting all 144 does not establish admissible native two-event histories.

For either OO or EE there are 153 unordered distinct-label pairs. Partition by address and parity: (same,same)=18, (same,cross)=27, (cross,same)=54, (cross,cross)=54. Address totals are 45 and 108; parity totals are 72 and 81. Thus 45/108=5/12 is an address-count ratio. It is not a parity ratio, a physical modulus, or an invariant quantum sector. Such sectors would require a declared linear realization and preservation by its interaction operator.

An activation label changes Boolean weight, not a derived integer winding. If a separate counter n has quadratic burden B=kappa*n^2, steps +1 and -1 cost kappa(2n+1) and kappa(1-2n), respectively. The imported constants +kappa and -kappa use particular starting values n=0 and n=1. Even then, a burden decrease is not identified with recoverable work; controls, reservoirs, readout, retained correlations and renewal must enter a complete apparatus ledger. The receipt-fiber criterion and record-size bounds of v0.11 remain in force.

## 7. Integration and next closure order

The manuscript gains D.14: affine closure, its C2 x S4 identification, endpoint/history distinction, the limited status of C13, and the explicit projective counterexample. Transport, extra finite-field details and repeated counts stay in this audit to preserve the manuscript's narrative scope. No sqrt(10) significance emerges: the already repaired, model-derived sqrt(3) example remains appropriate.

Priority remains: (1) derive native control eligibility and its source from the carrier interaction; (2) declare an actual connection and test its history/receipt observability, rather than naming a finite phase winding; (3) specify and calibrate the full control/readout/renewal apparatus before comparing retained information with total cost; (4) derive a boundary-counting limit and entropy normalization without importing G. If transport is pursued separately, derive the scattering/contact map and solve the floating-probe noise before claiming robustness or a noise peak. The present 19 check families close finite algebra and conditional example calculations only.

## Reproduction and provenance

Run `python verify_research_batch3.py` with SymPy. It writes `RESEARCH_BATCH3_CHECKS.json`. The input DOCX files are preserved inside `SOURCE_DOCUMENTS.tar.xz`; extracted equation XML is included separately. `SOURCE_REGISTER.json` pins original hashes and the v0.11 baseline; `SHA256SUMS.json` hashes package members. The archived earlier evidence package is identified by its exact hash and prior GitHub commit rather than reinterpreted or promoted. Code and constructor checks are new work; imported working notes remain unreviewed source data.
