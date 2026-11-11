# UD Hodge-to-RSP realization obstruction v0.1

14 October 2026 UTC. Development — no registry entry. Physical promotion: 0.
Status: EXACT CONDITIONAL NO-GO / PREPARED-WINDOW ENCODING / NATIVE OPEN-SYSTEM REALIZATION OPEN.
Constructor-team mathematical checks and a separate AI reasoning/scope audit are recorded. Independent human/adversarial review remains pending. This result restricts a proposed realization class; it does not retract the conditional RSP-1 recurrence or claim a physical impossibility of irreversible response.

## 1. Exact realization contract

Fix a nonempty source domain D and a native one-attempt map U:D→D. A state-only decoder phi:D→S realizes the complete RSP successor F exactly when

phi(Ux)=F(phi(x)) for every x in D.

The decoder includes stock, cached latent presence, response, bank/cursor and frozen branch. Agreement of Theta alone is a weaker projection and cannot establish this contract. F means the total successor function, including F(s)=s at the programme's terminal model states; the run routine merely stops recording there.

The native source considered here is closed fixed-complex finite-dimensional Hodge flow U_delta=exp(delta A), A^T=−A, at a declared constant dimensionless sample interval delta. This choice is a sampling contract, not a derived event clock or SI duration. D must be stated: a two-sided invariant carrier/sphere, a recurrent prepared orbit, a one-sided initialization domain or a finite window are different contracts.

Source anchors: Paper I v1.1.1 T4.3 and §6; C0579, single-cell spectral/recurrence identity; attached v0.39 ledger Q165/Q169/Q174–Q176; RSP01 §§2–7, prepared carrier and strict potential; E01, deterministic factorization; E03, complete-state projection; C0926 §4.6, typed latent witness. No original source or registry label is replaced.

## 2. Surjective finite-image factor theorem

Assume U is surjective on D, the decoded image M=phi(D) is finite, the exact realization contract holds, and F has a strictly decreasing potential on every nonfixed transition.

Then phi(D) is contained in Fix(F).

Proof: surjectivity gives F(M)=phi(U(D))=phi(D)=M. A surjective map on a finite set is a permutation, so every state in M is on an F cycle. A nonfixed edge on a cycle would strictly decrease potential and return to its old value, a contradiction. Thus every decoded state is fixed.

No continuity, measurement robustness, common recurrence period or native finite-state assumption is needed. The source D can be a real chain carrier; only its decoded image is finite. In particular an exact nontrivial RSP episode on a fixed finite prepared register family cannot be a total autonomous state-only factor of a closed Hodge step on a two-sided invariant domain.

For C, this permits only the exhausted/quiescent terminal state within each fixed prepared family. For H it also permits latched/stranded fixed states. It does not produce a transient from a populated preparation. Trivial constant fixed-state decoders exist and must not be called programme realization of a nonfixed initial state.

## 3. Uniform-settling variant and its necessary limit

Finite image can be replaced by a common finite settling bound N on M: F^(N+1)(s)=F^N(s) for all s in M. Surjectivity yields F^N(M)=M, and every member of that image is fixed. The conclusion is the same, even if M is infinite.

A fixed bounded RSP preparation has such a bound from its integer potential. Arbitrary preparations with unbounded token counts or queue lengths need NOT have a common bound.

Counterexample to the overbroad claim “surjectivity and strict integer descent always forbid a factor”: let U(n)=n+1 on Z, F(k)=max(k−1,0) on nonnegative integers, and phi(n)=max(−n,0). Then phi(n+1)=F(phi(n)) for every integer n, with nonfixed image. The image is unbounded and settling times are not uniform. This is an added unbounded source/clock example, not a Hodge realization or a finite RSP preparation.

## 4. Finite-order sampling theorem

If U^m=id on D for some positive integer m, exact realization gives F^m(phi(x))=phi(x). Strict potential descent forbids any nonfixed periodic target point, so every phi(x) is fixed. This theorem does not require finite image, a uniform settling bound or decoder continuity.

For the unit-metric filled tetrahedron A²=−4(I−P_H0), so exp(pi A)=I. A sample delta/pi=p/q in lowest terms has U_delta^q=I; its order may divide q on a selected state. delta=pi/4 has order four on the active plane used below. Rational sample clocks are declared choices, not native event laws.

## 5. Recurrence and a robust complete-state decoder

Every sampled finite-dimensional closed skew flow has arbitrarily late returns near its initial state. In orthogonal spectral planes the sample is rotation by finitely many angles. Simultaneous phase approximation yields integers n_j→infinity with U_delta^(n_j)→I: if an approximating sequence is bounded, it identifies an exact period and its multiples supply the late returns; otherwise an unbounded subsequence supplies them.

Consequently irrational A/B/C frequency ratios remove an exact common period, not approximate forward recurrence. The prior no-common-period theorem is preserved.

Now fix a recurrent x. Assume phi is return-stable at x: all sufficiently close late orbit returns decode to the SAME complete initial RSP state. Relative local constancy, or continuity into a discrete register space, suffices. If any subsequent F transition changes, potential becomes strictly smaller and can never recover its initial value. But arbitrarily late source returns decode to phi(x), contradicting exact intertwining. Hence the decoded initial state is fixed. This argument requires no uniform bound on the image, but does require complete-state return stability.

Theta-only stability does not forbid hidden stock/cursor descent. The gate L=1[R>0] is generally discontinuous at R=0; conservation and recurrence alone do not prove its return stability.

A one-sided forward orbit with a discontinuous decoder is a genuine mathematical exception to the corresponding assumptions. For an irrational sampled active circle, all U^n x are distinct. Define phi(U^n x)=F^n(s0) for n≥0. This is an exact factor on that forward-only orbit. A nontrivial eventually fixed target labels the initial point differently from arbitrarily late nearby returns, so the decoder is not return-stable and the source restriction is not surjective. This is a prepared orbit-label construction, not a robust native measurement law. Its extension to a total two-sided finite-image factor is forbidden by §2.

## 6. What norm conservation does and does not obstruct

Closed Hodge flow conserves c^T c. If available RSP stock is specifically identified with a function g(c^T c) of that conserved total norm, exact realization requires stock to be constant and forbids a token-consuming inspection. Likewise identifying the strictly descending RSP potential with a conserved invariant forbids every changed transition.

No such identification has been derived. Integer tokens are not chain norm, physical energy, action, burden or hbar. Local support/readouts may decrease while conserved support transfers elsewhere. Norm conservation by itself therefore does NOT exclude every possible stock decoder, larger memory register, finite-window model or open-system realization. The original HD polynomial latent witness can change while total norm stays fixed.

## 7. Exact K4 quarter-turn window and wrap witness

Use the standard oriented boundary matrices and A=d−d^T. Let v have vertex coordinates (1,−1,0,0), with all higher degrees zero. Let u have edge coordinates (1/2)B1^T v, with all other degrees zero. Boundary composition gives B2^T u=0, and the K4 graph Laplacian gives

Av=2u, Au=−2v, ||v||²=||u||²=2.

At delta=pi/4 the native orbit is v→u→−v→−u→v. All displayed coordinates and matrix identities are checked with exact rational arithmetic; no numeric trigonometry enters this witness.

Take the same single-token RSP initial state s0=(T100,L000,q000,r100,empty bank,beta). It reaches s1 after opening and s2 after cache clearing; s2 is fixed for either branch, with different terminal q for C and H. Define the PREPARED lookup on the four native samples by

phi(v)=s0, phi(u)=s1, phi(−v)=s2, phi(−u)=s2.

The first three native transitions intertwine exactly. At the wrap edge, phi(U(−u))=s0 while F(phi(−u))=s2, so the exact factor contract fails. Constant native norm coexists with declining assigned stock in this finite-window lookup; the stock is therefore not that total norm. This is a source-independent encoding of a chosen trajectory, not its derivation or a predictive decoder selected by native physics.

The lookup is also distinct from the original HD latent receipt. At v and −v the edge component vanishes; at u and −u the vertex component vanishes. Hence C0926’s polynomial R_e^(HD)=c1,e²(c0,i²+c0,j²) is zero at all four samples, giving L^(HD)=000. Yet the prepared lookup assigns cached L=100 to s1. No equality between these two differently typed receipts is supplied, even during the matching window.

More generally, any finite RSP trace can be assigned to distinct samples on a frequency-2 plane using a declared period longer than the window. That proves existence of a finite trace encoding, not global realization, controller preparation or a physical clock. A reversible cyclic history embedding similarly needs a separate Hodge incidence/spectrum/metric realization theorem; reversibility alone is insufficient.

## 8. Versioned realization disposition and lawful next routes

The RSP-1 source-interface model remains CANDIDATE with its exact conditional finite properties. Its proposed strict realization as a nontrivial TOTAL finite-image factor of closed Hodge evolution on a two-sided invariant domain is now an EXACT CONDITIONAL NO-GO in this development record. A robust recurrent-orbit realization is also obstructed. This splits the previously open bridge; it does not settle every possible realization class.

OPEN alternatives: a finite prepared window with declared decoder/preparation/error/capture limits; an independently specified open source/reset/export law; a larger sourced history/clock/reservoir carrier with explicit resource bounds; or a weaker preparation-dependent/ensemble correspondence with an actual error contract. A finite closed environment does not automatically yield permanent exact absorbing behavior: its full dynamics remains reversible and recurrent.

Next priority: define a finite-window joint carrier and account explicitly for decoder, clock, memory, outgoing records and reset resources before claiming source realization. Independent adversarial human review remains pending. There is no empirical test, physical promotion, native event-source selection or new absolute time scale in this release.
