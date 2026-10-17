# Continuous finite-word lift: constructor-team source and scope audit

14 October 2026. Development lane; no registry entry. This is an AI constructor-team audit, not independent human review or a CRL promotion. Physical promotion remains 0.

## Disposition

The proposed prefix-dressed engineered spin clock is a valid exact conditional continuous implementation of the **supplied finite payload word**. It provides coherent prefix histories and deterministic complete-word output at one prepared endpoint. It does not identify the original cyclic permutation with its Hamiltonian, execute deterministic basis-clock ticks at equal physical intervals, or supply permanent capture, an exhaustion latch, native geometry, physical units, or a fresh complete restart.

## Primary local source anchors

The inspected primary snapshot is `dist/sources/joint-carrier-v0.1/PIV.txt` in capture `captures/2026-10-14T144416Z-codex-joint-carrier-28082f98`.

| Source | Support and limit |
|---|---|
| Paper IV §4, lines 105–132, IV.4 | Supplied gate word, prefixes, dressed spin clock, exact transfer amplitudes, spectrum/norm, terminal time and actual/comparator bound. Gates commute with comparison work generator. Zero comparison generator satisfies the condition. |
| Paper IV §4, lines 134–148, IV.5 | Projective return, finite completion window, clock tail and complete target debit. Whole propagation mismatch is charged once. Arbitrary gate word is not automatically a packet producer. |
| Paper IV §2, lines 31–50, IV.1 | Finite complex Hilbert spaces, mathematical hbar=1, complete joint domain with spectator, Duhamel channel bound, separate amplitude-squared diagnostic and initial state distance. |
| Paper IV §6, lines 202–214 | Closed finite stationary exact permanent first-entry capture obstruction; finite approximate horizon or supplied switching are different contracts. |
| Paper IV §8, lines 278–313, IV.12–IV.13 | Full matched-module exchange exports correlations; fresh donor independence is a hypothesis; full-bank error and unconditional telescoping, with no postselection or double charging. |
| Paper IV §9, lines 321–350 | Conserved constant-generator mean energy, interaction debit, zero initial mean does not make preparation free; native supply, local coupling, launch, trigger and export remain acquisition gates. |
| JC v0.1 §§3–7 | Entire-domain reversible compute maps; fixed finite compute/reset word; outgoing records and full matched donors; master clock is additional state; wrap does not refill resources. |
| Hodge/RSP obstruction v0.1 §§2–8 | Finite-window preparation and a larger sourced history carrier are admissible development directions; total finite-image nontrivial absorbing factor is excluded under stated surjective-domain assumptions. |

No archived imported source code was executed. Prior source novelty acknowledgements are preserved: engineered perfect transfer and prefix-history Hamiltonians are established ingredients, not new priority claims.

## Exact mathematical checks

Write K=(B+1)N+B, retain Z=P tensor D_0 tensor ... tensor D_(B−1), and take V_0,...,V_(K−1) to be the compute/reset payload blocks at old addresses 0,...,K−1. Exclude the cyclic clock shift and the final identity/wrap block. Q_0=I and Q_j=V_(j−1)...V_0. The dressed unitary W=sum_j |j><j| tensor Q_j conjugates the bare spin clock into

    H_p = kappa sum_(j=0)^(K−1) sqrt((j+1)(K−j))
          [|j+1><j| tensor V_j + |j><j+1| tensor V_j^dagger].

It is Hermitian on the full declared joint carrier, even with dirty payloads/donors. Its spectrum is kappa(K−2r), r=0,...,K, each repeated dim Z times. Its norm is kappa K and the interaction relative to bare clock obeys ||H_p−H_C tensor I|| <= 2 kappa K. These are supplied-operator quantities.

From a fresh clock, arbitrary payload/spectator input is mapped by the isometry

    A_t psi = sum_j c_j(t) |j> Q_j psi,
    c_j(t)=(-i)^j sqrt(binomial(K,j)) sin(kappa t)^j cos(kappa t)^(K−j).

Clock address probability is |c_j|² independently of the payload or spectator. Conditional on an address with nonzero probability, the payload/spectator is Q_j rho Q_j^dagger. At T=pi/(2 kappa), only the terminal address survives and the entire word Q_K is applied, with common phase (-i)^K. At 2T, the **entire propagator** is (-1)^K I, under the declared zero-free-generator comparison. A nonzero commuting free comparator retains its free evolution and need not return the full state.

### Mixed-state terminal distance refinement

The exact full-joint terminal target is B rho B^dagger, where B psi=|K>Q_K psi, and actual comparison is A_t rho A_t^dagger. A_t^dagger B=c_K(t)^* I. Consequently

    D_tr(A_t rho A_t^dagger, B rho B^dagger)
       = sqrt(1−|c_K(t)|²)

for **every** normalized mixed rho, including arbitrary retained spectator correlations. Proof: diagonalize rho=sum_a lambda_a |a><a|. Distinct a induce mutually orthogonal spans of A_t|a> and B|a>, since cross-inner-products are zero. In each span the pure-state difference has eigenvalues ±lambda_a sqrt(1−|c_K|²); summing its trace norm yields the equality. This is stronger than merely quoting a purification upper bound; include this short proof if equality is claimed for mixed inputs.

Near T, t=T+s, the distance is sqrt(1−cos(kappa s)^(2K)) <= min(1,sqrt(K) kappa |s|). For general dimensionless xi=kappa t/pi, terminal probability is sin(pi xi)^(2K); the distance is sqrt(1−sin(pi xi)^(2K)). It is zero at xi=1/2 and one at xi=0,1 for K>=1. At the latter addresses old records, swaps, and payload changes have coherently reversed; permanent retained outputs have not been protected.

From fresh clock address 0, every payload/spectator state has mean H_p equal to 0 and second moment kappa²K. Thus variance is kappa²K. A global energy-origin change alters mean but not variance. None of these facts gives physical clock acquisition or energy units.

## Required scope corrections and negative controls

1. Equal address dimension K+1=L does not equate the spin-path generator with the old cyclic shift U. Their evolution and recurrence differ.
2. At generic continuous times the clock coherently superposes prefixes, including pre-reset and post-reset donor roles. Allocated resource capacities are fixed, but usage is address-conditional. Do not describe the evolution as a definite classical consumption schedule without an explicitly supplied measurement channel.
3. A bare spin clock H_C tensor I retains the input payload and fails a nontrivial word. It cannot stand in for the gate-dependent hopping blocks.
4. A payload reset is one of the supplied reversible word gates. It exchanges a whole payload and preserves outgoing correlations. It does not reset the production clock. A fresh clock by itself does not replenish the full payload/donor bank.
5. Adjacency on the clock path is not two-locality on work/memory/record registers. V_j can be a large modular lookup or complete-payload exchange. No native Hodge incidence realization is supplied by the dressing identity.
6. The endpoint guarantee is complete joint, including clock and all outgoing donors. A reduced output error cannot replace it when records or donors are retained or reused.
7. Clock preparation and kappa are declared inputs. T is a model-unit time, not a derived native event cadence, SI duration, proper time, or hbar normalization.
8. Correlated fresh-bank failure controls remain necessary. Checking each donor marginal does not certify the full joint preparation.

## Complete actual/comparator admission

Supply a complete actual generator H_a(t) on the same clock+Z domain (with the same spectator extension) and a uniform mismatch certificate delta(t)=||H_a(t)−H_p||. Let Gamma(t)=integral_0^t delta(u)du. If the actual complete supply differs from the independent ideal supply by epsilon_bank, then

    D_tr(actual_t, terminal_target) <=
       min(1,epsilon_bank+Gamma(t)+sqrt(1−|c_K(t)|²)).

At |t−T|<=sigma, this is bounded by min(1,epsilon_bank+Gamma(T+sigma)+sqrt(K) kappa sigma), when Gamma is nondecreasing. Charge the same integrated interval once. Additional gate-error sums should not also charge a mismatch already covered by Gamma. For the nonterminal clock event, with ideal supply, operator error gives an amplitude bound and hence probability <= min(1,(sqrt(1−|c_K|²)+Gamma)²). Initial state discrepancy epsilon_bank enters diagnostic probabilities linearly, not through an unjustified amplitude square.

## Next native admission contract

Before naming this a UD-native realization, identify all of the following on one declared source domain:

- Source-selected joint carrier and named finite preparation family, including an actual clock state, blank history/record supply, each whole donor, and retained spectator/outputs. If scope is only one known trace, declare that restriction rather than claiming the universal full register carrier.
- Explicit isometry E from the claimed ideal carrier into a sourced native carrier, with named metric, oriented incidences, generator and dimensions. A single unextended tetrahedral chain register is not automatically the large clock+payload+bank space.
- Actual native generator H_nat and an independently source-bound residual certificate ||H_nat E−E H_p||<=delta. This accounts for dynamics mismatch and leakage together. Duhamel gives ||exp(−itH_nat)E−E exp(−itH_p)||<=t delta on the full admitted family; arbitrary spectators extend by identity.
- A sourced complete readout/receipt channel agreeing with the declared ideal labels and retaining outgoing correlations; an instant HD latent polynomial is not an identified historical cache or stock decoder.
- A physical time/action convention, acquisition/reset/export supply, local implementation and retained-output perturbation bounds. Include the source of each certificate; equality of numbers is not identification of objects.

No source provided here closes those native, empirical or physical gates. Exact conditional algebra is established by direct re-derivation; importing more conditional citations must not raise registry status. Independent non-constructor review and a custodian ruling remain promotion requirements under the attached CRL-2 governance proposal.

## Addendum: exact weighted-path Hodge representation and parity obstruction

The parent's proposed weighted-path representation passes a separate algebraic check, with a rate normalization correction noted below. Define the **unit-rate** adjacent magnitudes b_j=sqrt((j+1)(n−j)) and gauge T=diag(i^j). Then T H_C T^dagger has row (j,j+1) equal to −i kappa b_j and row (j+1,j) equal to +i kappa b_j.

For even n=2M, use a path with vertices v_r at clock addresses 2r (r=0,...,M), edges a_r at addresses 2r+1 (r=0,...,M−1), and orient edge r from vertex r to r+1. Set positive diagonal metric entries

    g_v,0=1,
    g_e,r=g_v,r/[(2r+1)(n−2r)],
    g_v,r+1=g_e,r (2r+2)(n−2r−1).

Every displayed metric entry is rational and strictly positive. With ordinary incidence B_(r,r)=−1 and B_(r+1,r)=+1, normalized boundary D=sqrt(G_0) B inverse_sqrt(G_1) has entries −b_(2r) and +b_(2r+1). In grouped vertex/edge coordinates A_path=[[0,D],[−D^T,0]]. Therefore, after the explicit permutation from grouped to interleaved addresses,

    T H_C T^dagger = i kappa A_path.

The rate kappa must be factored out in this rational-metric statement. If equality with i A_path without the external rate is desired, take g_e,r=g_v,r/[kappa²(2r+1)(n−2r)] and g_v,r+1=g_e,r kappa²(2r+2)(n−2r−1). Those entries remain positive for kappa>0, but rationality then requires kappa² rational. The choice kappa=1 retains all claims without qualification.

The prefix frame W commutes with the clock-only gauge T, so dressed propagation is W(i kappa A_path tensor I_Z)W^dagger. For arbitrary unitary prefixes, this is a unitary-frame Hodge representation, not automatically an ordinary scalar simplicial incidence matrix in the original register basis. **For this carrier specifically**, every prefix is a basis permutation. It separately permutes even-address vertex labels and odd-address edge labels, so the transformed boundary still has exactly two oppositely signed nonzeros per edge column. It is an ordinary weighted incidence matrix for dim Z disjoint paths with authored register-dependent endpoint labels. Its metrics and incidence are compiled from the supplied word, rather than recovered from native tetrahedral geometry. This distinction should be explicit.

For odd n, spin eigenvalues kappa(n−2r) exclude 0. The full chain Hodge generator of every ordinary nonempty finite simplicial complex with positive definite metric has nontrivial degree-zero homology and hence a zero mode (one for each connected component). Thus an odd-word spin generator cannot be unitarily conjugate to that **entire** simplicial Hodge carrier. This obstruction does not cover reduced chains, active subspaces with harmonic modes excluded, augmentation by extra modes, nonordinary complexes, or general operator compressions. Scope must remain full-carrier unitary equivalence.

Appending one terminal identity gate when original K is odd gives even n=K+1, preserves final payload Q_n=Q_K, and adds exactly one address factor. For K=9 this changes dimension 10 to 11; endpoint time remains pi/(2 kappa), while norm increases from 9 kappa to 10 kappa and initial variance from 9 kappa² to 10 kappa². The extra address is charged even though no extra payload record or reset donor is consumed. The default dressed carrier dimension changes accordingly. Identity padding is an engineered representation choice, not a source-selected physical clock repair.

This yields a valid exact conditional weighted one-dimensional Hodge-form carrier. It closes a narrowly stated algebraic representation question and leaves native unit-metric tetrahedral selection, native metric/coupling acquisition, source stock/readout mapping, physical units, local register architecture and protected irreversible export open.

## Final implementation audit

Reviewed the actual `programmed_clock.py` and `UD_PROGRAMMED_WEIGHTED_PATH_CLOCK_v0.1.md` on the Site checkout after implementation. The mathematical disposition is **PASS within the declared conditional scope**. No Site files were edited by this reviewer.

- PC.1 agrees with the inherited spin-history formula and exact projective whole-operator return.
- PC.2 uses the corrected external kappa rate, positive rational unit-rate metrics, and restricts literal disjoint-path incidence to present permutation prefixes.
- PC.3 states the odd-word kernel obstruction on the full ordinary simplicial carrier and names the excluded restriction/augmentation alternatives.
- PC.4 is valid for even n>=4: exact isometric intertwining preserves source eigenvalues, while source positive eigenvalues 2 kappa and 4 kappa cannot both lie in the target positive spectrum {2}. Identical direct sums change multiplicity, not the allowed target eigenvalues. No exact isometric full-carrier embedding into that declared single-tetrahedron class exists. This is not a general prohibition on enlarged/weighted native complexes or approximate finite-window matching.
- Coherent reset branches, retained outgoing donor records, complete mixed-state terminal distance and the no-permanent-export return are explicitly accounted for.
- The mixed-state equality proof is correct: scalar overlap of the two isometries produces orthogonal rank-one comparison blocks for each eigenvector of the arbitrary input density matrix.
- The native residual inequality follows Duhamel for finite Hermitian generators without requiring prior subspace invariance. Residual zero establishes exact intertwining/invariance; nonzero residual counts leakage and within-image mismatch together.
- The declared arithmetic bound evaluates exactly to 288107/7000000. Its sqrt(10)<4 and pi<22/7 replacements are conservative, and the example remains an authored protocol illustration.

Additional narrow consistency checks executed: exact determinant roots for even n=4,6,...,20; exact default C/H padding preservation and complete dimension42,568,187,904; and exact rational arithmetic for the reported tolerance bound. These are not substitutes for the general proofs. The general source-free operator embedding contradiction was checked by reasoning, not promoted by finite enumeration.

One cosmetic correction was sent to the primary constructor: the resource table's interaction-norm row used unescaped vertical norm bars, which split Markdown columns. The constructor replaced those bars with `norm(...)`; this correction was re-read and is **RESOLVED**. It preserves all mathematics, and the refreshed proof hash is bound below.

Final audited file hashes after the resolved typographic correction:

| File | Bytes | SHA-256 |
|---|---:|---|
| programmed_clock.py | 3633 | ab4dfcee24da59bb9d8f22e46411963a77dc30428d2338698a0b735caa06f7d6 |
| UD_PROGRAMMED_WEIGHTED_PATH_CLOCK_v0.1.md | 15333 | 45b69deefe6f370ece8dc7e010e9df21796ffa7f9beee34217d8d708334627a3 |

Final status: conditional engineered carrier PASS; native tetrahedral/source acquisition OPEN; full specified single-tetrahedron embedding SCOPED NO-GO; independent human review PENDING; no registry promotion; physical promotion0.
