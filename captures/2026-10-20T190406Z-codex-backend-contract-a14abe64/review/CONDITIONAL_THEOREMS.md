# Conditional backend obligations after finite output certification

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

This is a mathematical distinction between accepted-output soundness and universal backend success. It is not a new estimator run, a proof that the fixed SciPy implementation fails, or a change to any old campaign verdict.

## Definitions and inherited premises

The input family consists of encoded records relative to the original nominal with SHA-256 `25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59`. Each of its 303,067 observation vectors has 62 channels, scalar quantum `q0=2^-48`, and additive perturbation norm at most the unchanged `δ0=3*2^-49`. The exact integer alphabet is 7,689 pointwise vectors. Its cardinality does not imply output quality.

The resulting exact projected matrix is `Z∈R^(8191×321)`. Let `r=209`, threshold `τ=2^-24`, and original exact nominal projection `Z0`. The source receipts supply lower `s0≤σ_r(Z0)`, upper `u0≥σ_(r+1)(Z0)`, and multiplier `C` satisfying `||Z−Z0||2≤Cδ0`. These source facts are inherited and hash-bound here, not independently rederived. Define

`L=s0−Cδ0`, `U=u0+Cδ0`, `μ=min(L−τ, τ−U)`, and floor debit `d=2^-41`.

The exact checker obtains `0<U<τ<L`, `0<d<μ`, and `μ≈5.9498083072701636×10^-8`. The approximation is informational; exact rational margins in CERTIFICATE.json are authoritative. Tolerances and recipe integers are O03 protocol controls.

## Theorem 1: a sufficient universal rank contract

Suppose that, for every admissible record, a backend terminates and emits a finite, nonnegative, sorted 321-entry array `ŝ`, and suppose the uniform error bound

`max_i |ŝ_i−σ_i(Z)| ≤ ε`, with `0≤ε<μ`,

has been proved for that backend/environment/input family. Then exactly 209 returned entries are above `τ`, and no returned entry equals `τ`.

Proof. Weyl's singular-value inequality gives `σ_r(Z)≥L` and `σ_(r+1)(Z)≤U`. For `i≤r`, sorting gives `ŝ_i≥L−ε>τ`; for `i≥r+1`, `ŝ_i≤U+ε<τ`. These inequalities prove both the count and the absence of equality. They do not say that a returned vector basis or any phase calculation is correct.

The largest sufficient dyadic error budget is `ε=2^-25`: it is strictly below `μ`, whereas `2^-24` is not. This budget is a sufficient conditional threshold, not a measured error bound for the actual backend. Equality at the upper margin can preserve the strict count while placing the first tail entry exactly on the cutoff; the current saved-rank policy correctly returns HOLD in that case. Thus an equality-HOLD must not be reported as an incorrect rank count.

## Theorem 2: the proposed singular floor is a stronger obligation

Under the same matched singular-error premise, the condition `ε≤d` implies

`ŝ_r ≥ L−d >0`,

which is the frozen proposed singular-floor requirement. The sufficient dyadic floor budget `2^-41` is 65,536 times smaller than the sufficient dyadic rank budget `2^-25`.

Proof. `ŝ_r≥σ_r(Z)−ε≥L−ε≥L−d`. Rank correctness alone does not supply this inequality. A scalar countermodel sets the first 209 exact singulars to `L`, their returned values to `L−2^-25`, and all tail values to zero. The returned array has rank count 209 but fails `ŝ_r≥L−d`. This countermodel concerns the stated scalar-bound premises; it is not an exhibited raw input in the frozen family or an output of the actual SciPy implementation.

## Theorem 3: one route from complete-factor error to singular accuracy

Suppose a complete 321-column factorization is available:

`Z = Uf Σ Vf^T + F`, `||F||2≤f`,

where `Uf∈R^(8191×321)`, `Vf∈R^(321×321)`, and `Σ` is diagonal with nonnegative sorted entries, largest value `m`. Suppose full Gram defects obey

`||Uf^T Uf−I||2≤ηL<1`, `||Vf^T Vf−I||2≤ηR<1`.

Define `a(η)=1−sqrt(1−η)`. Then the returned diagonal singular values have uniform absolute error at most

`εeff = f + m[a(ηL) sqrt(1+ηR) + a(ηR)]`.

Proof. Use full polar factors `Uf=QL RL`, `Vf=QR RR`, where QL has orthonormal columns and QR is square orthogonal. Their polar corrections satisfy `||RL−I||2≤a(ηL)`, `||RR−I||2≤a(ηR)`, and `||RR||2≤sqrt(1+ηR)`. The exact matrix `QL Σ QR^T` has singular values equal to the diagonal entries of Σ. Also

`RL Σ RR−Σ=(RL−I)Σ RR + Σ(RR−I)`.

The triangle/submultiplicative norm bounds give the displayed distance from Z to this exact orthogonal factorization. Weyl then proves the singular-error bound. Comparing `εeff` to Theorem 1 or 2 supplies sufficient rank or floor obligations.

These are COMPLETE-factor premises. Current PR279 preserves only the 209 retained left columns, even though it preserves all singular values and the right factor. A retained equation certificate is not a complete reconstruction certificate and does not fill these premises. No full-factor proof was newly computed here, and no uniform actual library bound has been established.

## Theorem 4: accepted-output soundness has different quantifiers

Let `P` denote all explicit, correctly typed inherited source premises. Let `Q(x,w)` be the actual mathematical quality conditions for a particular raw record x and exact decoded saved tuple w, including rank, input membership, both retained Gram defects, equation residual, measured singular floor, lag bound, LS positive floor, inverse/eigen residual bounds, actual emitted argument enclosure, source phase implication and strict disks, and finite target bijection. Let `V(x,w)=ACCEPT` mean those conditions have actually been established by the pinned exact checker and independent audit, not merely that a JSON Boolean says true. Subject to correctness and binding of that checking arithmetic,

`P ∧ V(x,w)=ACCEPT  =>  finite emitted-phase conclusion for that (x,w)`.

This statement quantifies over ANY producer: the producer's brand or implementation need not be trusted once the actual tuple and premises have been independently checked. It does not imply

`for every x, backend B terminates and returns w with V(x,w)=ACCEPT`.

The latter is completeness/success of a particular numerical backend over the specified family. It needs proof of all required numerical and operational obligations. Rank and singular-floor proofs alone do not imply the Gram, equation, lag, eigenpair or argument conditions. For example, exact singular values accompanied by a zero proposed left basis violate the left Gram condition.

A wrapper can treat missing files, crashes, inconclusive interval comparisons, broken hashes, or failed premises as HOLD. This is an operational fail-closed rule. It does not prove checker termination, numerical backend termination, or successful extraction for every input. A successful source theorem does not make an unverified returned tuple admissible.

## Theorem 5: finite tests do not entail universal backend success

For any proper tested subset S of an input domain D and a point `x*∈D\S`, two otherwise unrestricted blackbox functions can agree on every point in S and differ at x*. Construct B2 to equal B1 on S and return HOLD at x*. Hence agreement on finitely tested histories alone does not imply all-input success.

The exact toy control uses `D={0,1,2,3}`, `S={0,1}`, and counterpoint 2. This is a countermodel to an inference rule, not an implementation counterexample against the unchanged SciPy source. It neither proves the actual backend fails on an untested record nor proves that universal success is impossible. A verified whole-program/numerical proof, suitable covering argument, or exhaustive finite verification could supply additional evidence. None is replaced by finite tests or by counting the pointwise alphabet.

## Remaining obligations

A successful all-input extractor claim requires an explicit implementation/environment/failure model and a uniform theorem or complete verification for every promised condition: termination and complete output custody; singular accuracy adequate for rank and the proposed floor; retained/full-factor Gram and equation errors as appropriate; shifted least-squares and lag errors under all admissible conditioning; eigenpair/inverse and argument/encoding errors; strict target margins; and exact checker/source binding. Acquisition calibration and physical fresh lineage are additional, separate evidence obligations. No SI, six-ratio physical accuracy, native 1893/747 recovery, new-case full reconstruction, or exact spectrum(T) conclusion follows from these conditional backend contracts.
