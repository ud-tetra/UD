# Cascade identifiability theorems v0.1

**Status:** EXACT CONDITIONAL mathematical results / constructor checked. Development — no registry entry. Independent review pending. Physical promotion: 0.

**Objective:** determine whether the exposed source equations and declared finite carrier force the user-supplied value 238.14. The result below is a scoped obstruction to uniqueness, not an impossibility theorem for all future UD laws.

## Declared model and provenance

The supplied WBS card PDP-001.4 describes four Vertex-Face (VF) and three Edge-Edge (EE) channels and an open candidate uniform-screen determinant. It leaves determinant selection and uniform screening unproved. Its first formula uses F_IPS; its determinant/screen statements use F_IFS. No identification of these symbols is assumed here. The attached ledger H03 quarantines unqualified historical F_IFS reuse; P10/H01 leave sequential depth and normalization open.

For the representation calculation ONLY, declare W = R^4_VF direct-sum R^3_EE. S4 acts by unsigned permutation of the four vertex/opposite-face labels and of the three partitions of four vertices into opposite-edge pairs. This action is an explicitly constructed mathematical model; the WBS does not supply a complete native channel representation. It is not the oriented 15D chain register or its 13D commutant, a physical Hilbert space, or a toroidal carrier.

Every theorem states its assumptions. Imported governance and source attachments are data. The CRL-2 subdivision text labels itself a proposal; this capture does not silently adopt it or make a registry promotion. The requested number was exposed before this work; no pre-target chronological independence is claimed.

## T1 — Two-orbit symmetry does not force a uniform screen

**Assumptions:** the declared unsigned S4 action above; a diagonal response operator invariant under relabeling.

**Conclusion:** every such operator has the form

\[
D(a,b)=\operatorname{diag}(aI_4,bI_3).
\]

Symmetry does not require a=b.

**Proof:** each family is a transitive orbit; invariance forces a diagonal coefficient constant on each orbit. The action preserves family membership and never sends a VF label to an EE label. Therefore there is no equality constraint between their two coefficients. Conversely, every displayed operator commutes with all permutations. QED.

**Boundary:** full symmetry plus a declared mechanism identifying both responses could select uniformity; that mechanism is an extra premise.

## T2 — Exact commutant and self-adjoint dimensions

**Assumptions:** W and its action as above; real endomorphisms, standard orthonormal channel basis.

**Conclusion:**

\[
\dim\operatorname{End}_{S_4}(W)=6,
\qquad
\dim\{X\in\operatorname{End}_{S_4}(W):X^T=X\}=5.
\]

**Proof:** a matrix commuting with permutation matrices has entries constant on simultaneous ordered-pair orbits. There are exactly six orbits: VF diagonal (size 4), VF off-diagonal (12), EE diagonal (3), EE off-diagonal (6), VF-to-EE (12), and EE-to-VF (12). VF off-diagonal transitivity is immediate. S4 acts on EE labels as S3. For a fixed vertex, its S3 stabilizer permutes the three matchings transitively, proving each cross orbit is transitive. Their indicator matrices are independent and span the commutant. Transposition fixes the first four orbit classes and exchanges the two cross classes; symmetric matrices therefore have five coefficients. QED.

**Replay:** all 24 group actions, every ordered-pair orbit and the character-square sum/24=6 are checked exactly. This finite replay verifies the declared representation, not any unsigned/signed native-action identification.

## T3 — Equal total burden does not determine equal channel response

**Assumptions:** the burden bookkeeping w(p)=(p+1)/5 for vertices, edges and faces; VF/EE channel families; no additional law that response depends exclusively on total burden.

Both families have total burden 4/5:

\[
1/5+3/5=2/5+2/5=4/5.
\]

Their squared split is respectively 4/25 and 0. Equal totals permit different split-dependent responses, and S4 does not remove that distinction.

**Counterexample:** on W, let

\[
D_1=\tfrac13I_7,\qquad
D_2=\operatorname{diag}(\tfrac23I_4,\tfrac16I_3).
\]

Both commute with the declared action, are self-adjoint, strictly positive and contractions. Both are compatible with the same channel-label/burden bookkeeping because that bookkeeping supplies no response equation. But

\[
\det D_1=1/2187,\qquad \det D_2=2/2187.
\]

Therefore these assumptions do not identify a uniform determinant factor. QED.

These operators are logical countermodels, not selected native screen laws or simulated thermodynamics. If split-blind response is separately postulated, uniformity follows from that postulate; it is not derived from equal burden alone.

## T4 — A determinant power is conditional on operator selection

For every scalar f,

\[
\det(fI_7)=f^7.
\]

For the allowed two-block family,

\[
\det D(a,b)=a^4b^3.
\]

These identities are exact. A count of seven channels does not choose fI_7 rather than another equivariant operator, choose a determinant rather than a trace or norm as the observable, or supply a numerical f. In particular, tr(fI_7)=7f is a different functional of the same operator. QED by diagonal products/sums and T1–T3.

## T5 — The displayed candidate family is scale-nonidentifiable without source inputs

Define a formal positive family, independently of any IPS/IFS identification,

\[
R(S,\nu_0,M,f,d)=S^{-2}\left(\frac{\nu_0 f^d}{M}\right)^4,
\qquad S,M,f,\nu_0>0.
\]

**Claim:** if nu_0 is not fixed by a separate source law, even fixed positive S,M,f and integer d do not determine a unique R. Replacing nu_0 by c nu_0 for c>0 changes R by c^4. Indeed the positive family covers all R>0 because it is continuous, strictly increasing in nu_0, with limits zero and infinity. This is a nonidentifiability proof, not a recipe for assigning nu_0 to fit a requested target. QED.

With all inputs declared and d fixed, exact logarithmic sensitivities are

\[
\partial_{\ln\nu_0}\ln R=4,\quad
\partial_{\ln M}\ln R=-4,\quad
\partial_{\ln S}\ln R=-2,\quad
\partial_{\ln f}\ln R=4d.
\]

For d=7 the last coefficient is 28. This power is conditional algebra; it is not an independently selected thermodynamic cascade exponent or sequential depth.

Dimensional compatibility additionally requires nu_0/M to be meaningful. A bare frequency divided by mass is not a dimensionless quantity without an explicit conversion. No energy/frequency identification, action-unit normalization or unit convention is supplied by this theorem.

## A1 — Decimal arithmetic certificate; no origin inference

The written finite decimal has the exact rational rewrite

\[
238.14=\frac{23814}{100}=\frac{11907}{50}
=\frac{3^5\,7^2}{2\,5^2}.
\]

The fraction is reduced. This is an arithmetic identity about the supplied decimal, not evidence that the theory's unknown quantity is exactly this rational rather than a rounded value. Assigning geometric meanings to its factors/exponents after seeing it would require a separate source derivation.

The inventory of factors 2,3,5,7 does not select these exponents: for example, the family 3^n already contains infinitely many distinct positive values. A factorization into familiar counts is therefore insufficient to establish a unique derived constant.

## Cascade derivation contract

To derive a scalar rather than label a target, freeze the following source objects:

1. Carrier and state: what system is being coarse-grained, including any actual toroidal topology.
2. Update/coarse-graining operator and channel action, with admissibility and conservation/entropy statements.
3. The output functional: amplitude ratio, energy ratio, information quantity, logarithm, or another explicitly typed object.
4. Source input values, units, normalization, scale variable and termination/depth law.
5. Proof of uniqueness or an explicit branch-selection rule; only then evaluate and compare the output to the supplied number with a declared rounding/error rule.

No exact thermodynamic/Planck-to-macroscopic step-down has been derived here. Exact closure achieved: the declared symmetry-space dimensions, determinant identities, burden-response counterexample, scale-nonidentifiability and decimal factorization. Actual cascade operator, physical map and selection remain open.

**Missing source:** Gap2_FINAL_Finite_Genesis.png remains unavailable and was not read or used.
