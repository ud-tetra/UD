# A programmed weighted-path clock for the finite joint carrier

Development v0.1 · 14 October 2026 · public reading edition0.8

**RESULT.** The supplied reversible carrier now has a constant-Hamiltonian finite-word implementation, with complete clock/data/record/reset accounting. For even word length it is exactly a weighted path-graph Hodge generator after a declared phase gauge. An odd word has a full-carrier harmonic-kernel obstruction; one supplied identity gate repairs that representation without changing the terminal payload. Neither construction derives a native tetrahedral source, calibrated time, locality or permanent export.

CANDIDATE ENGINEERED GEOMETRY / EXACT CONDITIONAL OPERATOR THEOREMS / SCOPED NO-GO. Development — no registry entry. Independent human review pending. Physical promotion0. Separate AI reviews are constructor-team checks, not the non-constructor/custodian promotion procedure in the attached CRL-2 subdivision proposal. Historical ledger0.39 remains a dated235-object source, not the current448-row public ledger.

## 1. Owned word and retained joint domain

Use the unchanged joint_carrier.py candidate. Its payload P contains work, N old-state cells and N receipt cells. There are B complete independent donor payloads. Let Z=P⊗D_0⊗…⊗D_(B−1), D=dim P=d^(N+1)m^N and Q=dim Z=D^(B+1). All outgoing blocks and arbitrary spectators Y remain retained.

The original certified window has K=(B+1)N+B payload operations V_0,…,V_(K−1): compute taps and scheduled complete-payload SWAPs. Remove the original cyclic clock shift from these gates; its final idle/wrap operation is not in the word. Each V_j is a total permutation on Z, including dirty configurations. The prepared input and complete source/receipt dictionary stay exactly those of carrier0.1.

Set n=K when K is even. When K is odd, optionally append V_K=I_Z and set n=K+1. The weighted ordinary-path representation below uses this padding. Define prefix permutations Q_0=I and Q_j=V_(j−1)…V_0. Prefixes denote operators, while scalar Q denotes data-bank dimension; their types remain distinct. The final padded word has Q_n=Q_K.

Replace the cyclic clock by a fresh path clock C with n+1 orthonormal addresses0,…,n. The complete domain is J_path=C⊗Z, dimension (n+1)Q. The old clock and this one are alternative implementations, not two clocks silently combined. Equal address counts do not imply equal operators.

## 2. Constant supplied history Hamiltonian

For a supplied internal rate kappa>0, define

    H_C = kappa sum_(j=0)^(n−1) sqrt((j+1)(n−j)) (|j+1><j|+|j><j+1|),
    W = sum_(j=0)^n |j><j|⊗Q_j,
    H_p = W(H_C⊗I_Z)W†.

These are exact definitions. H_p is Hermitian, constant after launch, and has edge blocks V_j and V_j†. It does not require clock-dependent external switching during this ideal propagation. Gate synthesis, launch, bare energies, errors and source acquisition are supplied assumptions.

Take zero comparison work generator. All V_j then commute with it, meeting Paper IV IV.4 exactly. This is a specialization of its established history propagation, not a new perfect-transfer principle. An added nonzero comparison generator needs its own commutation proof; it cannot be imported by merely naming a native Hodge operator.

**Theorem PC.1 (complete history and endpoint).** From clock0 and arbitrary payload/spectator vector psi,

    exp(−it H_p)|0>psi = sum_j c_j(t)|j>Q_j psi,
    c_j(t)=(-i)^j sqrt(binomial(n,j)) sin(kappa t)^j cos(kappa t)^(n−j).

At T=pi/(2 kappa), the complete output is (-i)^n |n>Q_n psi. At 2T the whole operator, on every clock/data input, is (-1)^n I. The spectrum is kappa(n−2j), each repeated Q times, and ||H_p||=kappa n.

*Proof.* Identify clock address j with the normalized symmetric sum of n binary spin strings of weight j. The restriction of kappa sum X_a has the displayed square-root edges; commuting single-spin rotations give c_j, eigenvalues n−2j and the complete projective return. Conjugation by W supplies the prefixes and preserves spectrum, norm and return. Extension by I_Y retains every correlation. □

Intermediate time generally gives coherent prefix branches, not a succession of pure clock addresses at evenly spaced physical times. Conditional on a clock-basis address j, the ideal payload is its corresponding Q_j state. Measuring or monitoring that clock changes the channel. A positive terminal-clock probability alone supplies neither a native detector nor a continuously monitored first-entry probability.

The fixed final response may coexist with changing complete history branches. At 2T all previously outgoing records and donor exchanges are coherently undone in this zero-free-generator model. The path clock does not permanently stop or retain export. Protected output needs a separately owned capture/isolation contact and its supply/error ledger.

## 3. Exact weighted-path Hodge representation

For n=2M, use a path graph with vertices v_r at even addresses2r (r=0,…,M) and edges e_r at odd addresses2r+1 (r=0,…,M−1). Orient e_r from v_r to v_(r+1). Its ordinary incidence B has −1 at the source and +1 at the target. There are no higher-dimensional cells.

Choose positive diagonal unit-rate chain metrics G_0=diag(a_r), G_1=diag(b_r) recursively:

    a_0=1,
    b_r=a_r/[(2r+1)(n−2r)],
    a_(r+1)=b_r (2r+2)(n−2r−1).

All a_r,b_r are positive rational numbers. Their common scale is a metric convention, not a source-derived physical normalization. In normalized chain coordinates,

    D_1=sqrt(G_0) B invsqrt(G_1),
    A_path=[[0,D_1],[-D_1^T,0]].

The left/right magnitudes in edge column r are respectively sqrt((2r+1)(n−2r)) and sqrt((2r+2)(n−2r−1)). Write the operator back in interleaved clock order. For S=diag(i^j),

    S H_C S† = i kappa A_path,
    S H_p S† = W(i kappa A_path⊗I_Z)W†.

**Theorem PC.2.** The even-word supplied clock has this exact weighted graph-Hodge representation. Its full graph comprises Q disjoint path components, each with M+1 vertices and M edges. Its harmonic kernel has dimension Q.

*Proof.* The metric recurrences give a_r/b_r=(2r+1)(n−2r) and a_(r+1)/b_r=(2r+2)(n−2r−1). The phase ratios i^j/i^(j+1)=−i give precisely the skew incidence signs. Positive metrics preserve path rank M and one H0 harmonic mode per component. W commutes with S and preserves chain parity. Current V_j are basis permutations, so W only relabels vertices and edges: each column still has exactly two opposite incidence signs. This gives an ordinary disjoint-path graph with authored metrics. For future arbitrary quantum gates, only unitary-frame conjugacy would follow; literal ordinary incidence would need a separate proof. □

This is an engineered degree0/degree1 graph, not a tetrahedral packet complex. The metrics, prefix frame and graph labels were constructed from the supplied programme. They do not explain why a native source should choose that programme. Address geometry being a path does not prove locality on work or donor registers.

## 4. Parity obstruction, padding and a native spectral limit

**Theorem PC.3 (odd-word full-carrier no-go).** For odd n, H_C has no zero eigenvalue. It cannot be unitarily equivalent on its entire carrier to i times the ordinary full Hodge generator of any nonempty finite simplicial complex with positive metrics and no augmentation or boundary restriction: that generator has at least one H0 harmonic mode per connected component.

*Proof.* n−2j is never0 for odd n. Positive-metric ordinary homology preserves b0≥1. Unitary equivalence preserves kernel dimension. □

This theorem concerns full-carrier equivalence. It does not forbid an embedding into a selected active native subspace, an augmented/reduced complex, grounded boundary conditions or a different operator. Identity padding changes odd K to even n, adds one clock address and one supplied identity edge, and keeps the terminal payload word unchanged. It changes spectrum, norm, initial variance and timing-tolerance dependence; those changes must be counted.

**Theorem PC.4 (unit-metric single-tetrahedron operator limit).** For even n≥4 and kappa>0, no isometric exact operator embedding of this full clock/data generator into the unit-metric filled-tetrahedron generator, or any direct sum of copies of that same generator, exists. The clock has at least two positive frequencies2 kappa and4 kappa. The stated tetrahedral operator has only the positive frequency2 (and0,−2). An exact intertwiner must preserve every source eigenvalue; both2 kappa and4 kappa cannot equal2.

This excludes that declared native class, not every weighted or glued tetrahedral complex, encoded subsystem, time-dependent source or weak finite-window comparison. Paper I's unit-metric identity and spectrum are the source premise. No physical frequency is identified here.

## 5. Complete clock/resource and error ledger

For the default d=3,m=4,N=4,B=1 word, K=9. Unpadded n=9 has10 addresses and no harmonic kernel. Padded n=10 has11 addresses and the same Q=3,869,835,264 data-bank labels. Complete dimension becomes42,568,187,904; the added address costs one additional Q-dimensional clock sector. Separate binary allocation still has four clock bits, so address-dimension cost is not necessarily a larger integer bit count.

| Resource | Padded default | Disposition |
|---|---|---|
| Clock | 11 addresses, n=10 | Terminal at T; complete projective return at2T |
| Word | 8 compute gates,1 payload SWAP,1 identity | Same terminal payload as nine-operation carrier window |
| State/receipt memory | 8 state cells,8 receipt cells | Complete prefix/outgoing history retained |
| Payload donors | 1 fresh independent block | Exchanged at its prefix; not erased or replenished |
| Weighted graph | 6 vertices,5 edges per component | Q engineered disjoint paths, not spatial cells |
| Operator norm |10 kappa | Model generator norm, not measured energy |
| Fresh-clock variance |10 kappa²; mean0 | Nonstationary resource; zero mean does not make preparation free |
| Interaction debit | norm(H_p−H_C⊗I)≤20 kappa | Cannot omit programme dressing without an operator/source justification |

The variance follows from the first clock edge's squared magnitude kappa²n and holds for arbitrary input payload/spectator with fresh clock0. The interaction bound is triangle inequality between two norm-kappa n operators. It is a sufficient upper bound, not a universal lower bound. Exact small witnesses attain2 kappa n; generic words need not. The bare clock H_C⊗I moves the address but leaves Z unchanged, so it fails a nontrivial payload word.

At xi=kappa t/pi, ideal terminal probability is p_n=sin^(2n)(pi xi). The **complete** trace distance to the ideal terminal state |n><n|⊗Q_n rho_ZY Q_n† is exactly sqrt(1−p_n), even for arbitrary mixed rho_ZY.

*Mixed-state proof.* Let L_t and L_T be the two input-to-joint isometries. Their overlap L_t†L_T is c_n(t)*I up to the harmless terminal phase. Diagonalize rho_ZY. For distinct eigenvectors, their pairs of isometric images span orthogonal subspaces because every cross overlap is the same scalar times their original inner product. Each rank-one block contributes its eigenvalue times sqrt(1−|c_n|²) to trace distance. Summing the eigenvalues gives the equality. Degenerate endpoint cases follow by continuity. □

For t=T+s, |s|≤sigma, sqrt(1−p_n)≤sqrt(n) kappa sigma. If the complete supplied input has trace-distance error epsilon_supply (clock, bank and every admitted spectator correlation), and actual propagation differs from H_p by an owned integrated norm r(t), then

    D_tr(actual_t, ideal_terminal) ≤ min(1, epsilon_supply + sqrt(n) kappa sigma + r(t)).

For a constant operator residual eta, r(t)≤(T+sigma)eta. The nonterminal-event probability satisfies epsilon_supply+min(1,[sqrt(n) kappa sigma+r(t)]²), capped at1; supply error is a probability-distance debit, not squared as an amplitude. No success conditioning or omitted failed branch is used. Capture/storage errors belong to further owned operations and are not supplied by this bound.

A declared arithmetic-only example with n=10, kappa sigma=1/100, eta/kappa=1/10000 and epsilon_supply=1/1000 has conservative rational distance bound

    1/1000 + 4/100 + (11/7+1/100)/10000 = 288107/7000000,

using sqrt(10)<4 and pi<22/7. It is a protocol illustration, not a theory constant, measured error certificate or rate calibration. The exact sqrt(10) expression is sharper. These controls stay distinct from the coefficient ledger's physical/action/time gates.

## 6. Native admission gate and next falsifiable target

Supply a finite native joint complex, chain basis, positive metric, full retained environment and declared Hermitian H_nat. Specify an isometry E:J_path→H_native, including clock, work, records and donor registers, and a source-defined decoder/preparation map. An operator residual must be computed from source-authored matrices,

    eta_native = ||H_nat E − E H_p||.

For finite Hermitian operators,

    ||exp(−itH_nat)E − E exp(−itH_p)|| ≤ |t| eta_native.

*Proof.* Differentiate exp(−i(t−u)H_nat) E exp(−iuH_p), integrate from0 to t, and use the isometry/unitary norms. This does not assume the encoded subspace invariant. Exact residual0 does establish invariance and intertwining. □

This provides a concrete falsifiable operator-admission target, not a claim that E or native supply is known. The native basis/metric and E must be fixed before output fitting. Independently admit the complete prepared state, ordinal/SI timing relation if used, output readout and protected retention. Dimension and spectral compatibility are preliminary gates, not substitutes for the residual or source-selected response law. On the declared single-tetrahedron class PC.4 already blocks exact full-clock admission.

## 7. Provenance, review and reproduction

Primary basis: Paper IV development0.1 §§2,4,8,9 and IV.1/IV.4/IV.12/IV.13; Paper I review1.1.1 skew Hodge and unit-metric filled-tetrahedron spectrum; unchanged carrier0.1/RSP0.1. New derivations: rational weighted-path metrics, padding/parity scope, mixed-state terminal equality, explicit resource specialization and native-isometry admission contract. General spin/history transfer is inherited established mathematics, not claimed novel.

programmed_clock.py produces a compressed exact C/H word/metric/witness, never a dense42-billion-dimensional matrix. verify_programmed_clock.py checks exact rational incidence/metrics, determinant polynomials, source word consistency and separately marked numerical timing diagnostics. A separate generated AI checker verifies small complete dressings and spectator-correlated transfers, with exact and numerical counts kept distinct. UI phase curves are model diagnostics, not empirical data.

Disposition: supplied constant-Hamiltonian word CONSTRUCTED CONDITIONALLY; engineered weighted-path Hodge representation EXACT CONDITIONAL; odd-word full-carrier representation and single-tetrahedron full embedding SCOPED NO-GO; native enlarged geometry, metric selection, locality, clock supply, physical calibration and permanent output isolation OPEN. No registry or CRL promotion. Physical promotion0; human review pending.
