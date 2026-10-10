# UD candidate flip-provider interoperability and null audit v0.1

**10 October 2026 UTC · development — no registry entry · physical promotion 0.**

## Source and declared object

The admitted `UD_THETA_FLIP_DIRECT_EVENT_INPUT_SOURCE_ADDENDUM_v0.1.md` (26 August 2026; Library `libfile_6145629eb8c081919302d99d60df1c82`, “Transition,” “Local source protocol,” “Missing source”) maps a **provided** provenance-bound `EXTERNAL_QUARANTINED` pair mask to \(\Theta^+=P_g\Theta^-\oplus\xi\) on \(\mathbb F_2^3\). Its `theta_flip_event_quarantine_contract_v0_1.py` (Phase 23 package `libfile_5c9aeab36a448191bf27669bf18f1099`, extracted source SHA-256 `49ce70c77f80dfa0bede388b4fc2f000b473ad9ab48e5268e54305a0158d512b`) validates such receipts; it does not generate them. The package itself has SHA-256 `b6037a5610d19937178801de3078371b017c16b08fa0f29d78f6e2d0b25f50a0`.

The historical `UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md` (30 August 2026; Library `libfile_8b9461fba6248191bb6d58dcf977a977`, §7 v0.3/v0.4) proposes a **conditional** one-pair signed-source/burden selector \(F\) on \((\Theta,I,G^{S\pm},W^{B2})\). The source, assumptions, and 46,656 synthetic input check are documented in [the historical selector capture](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T164302Z-codex-historical-pair-5b327476). The exact copied implementation has SHA-256 `44fe5049e14099ff111296726a36b4db7fe1f748cd4307b7c314cc148fb893c9`. Its minimal-capacity alignment and event eligibility are not native theorems. Neither source gives a physical clock, event rate, endogenous \(\xi\), or edge-local transport-map update.

## Exact conditional bridge and frame convention

Domain: one labeled K4 opposite-pair state \(\Theta\in\mathbb F_2^3\), a declared pair permutation \(\pi\in S_3\), pair-integrity bits \(I\), signed rational source vector \(G\), and nonnegative rational burden vector \(W\). The historical code writes `y[pi[i]]=x[i]`, whereas Phase 23 writes `y[j]=x[p[j]]`. **Use \(p=\pi^{-1}\)**. With every input relabeled in the same frame, let

\[
Y=P_{\pi^{-1}}\Theta,\quad
Z=F(Y,\pi I,\pi G,\pi W),\quad
\xi_{\rm cand}=Y\oplus Z.
\]

Then the admitted direct-update *algebra*, **if an independently valid receipt for that same \(\xi\) exists**, gives \(P_{\pi^{-1}}\Theta\oplus\xi_{\rm cand}=Z\). This is a composition identity, not a derivation of the receipt or its event cause. The selector outputs Hamming weight 1 for close/reopen, 2 for its zero-total swap, and 0 for holds. The proof is coordinatewise XOR; the inverse permutation equates the two source implementations. The candidate's source window, eligibility, budget polarity and address choice remain conditional. Fabricating an `EXTERNAL_QUARANTINED` receipt from the candidate output would launder a prediction into an apparent external observation.

`verify.py` exhausts \(8\) pair states, \(8\) integrity masks, \(27\) signed triples, \(27\) burden triples, and \(6\) pair permutations: **279,936 synthetic frame cases**, with **36** branch-by-frame probes against the Phase 23 receipt code. It explicitly checks a 3-cycle, on which passing the historical tuple unchanged to Phase 23 relabels the wrong pair. The branch counts and the mismatch witness are in `results.json`. The finite domain tests the declared selector's compatibility, not source reachability or predictive accuracy.

## Hold, no event, and the fixed-structure control

The Phase 23 API treats `None` as **THETA_UPDATE_DEFERRED** with local \(\Theta\) preserved; a valid zero-mask receipt is **APPLIED** and returns \(P_g\Theta\). They are operationally distinct, even though neither changes pair bits in its own comparison frame. Across the synthetic frame domain, **93,360** hold cases have \(P_g\Theta\ne\Theta\). A hold must not be silently turned into a zero-flip *event* receipt. A frame relabeling on a hold must be stored or applied separately under an explicit frame convention; deferral is not evidence that no event happened physically. This is an interface distinction, not 93,360 observed events.

The exact [native static K4 null](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T164734Z-codex-native-static-null-b71cb9e8) supplies \(G=(-1,-\tfrac12,-\tfrac12)\), \(\Theta=(0,0,0)\), integrity all one and \(W=0\). The unqualified historical selector emits a closure of A; fixed closure requirements/receipts and local edge maps leave the structural mask unchanged. The script reproduces this disagreeing fixture using exact fractions. **NO-GO under an unqualified universal interpretation:** source loss by itself is no event trigger. The historical selector's additional source-addressable-event and capacity-alignment hypotheses are absent on this null; this does not falsify its scoped conditional branch.

## Acquisition and decision

No independently produced same-carrier event corpus was in the recovered Phase 23 package, supplied local attachment set, [previous eligibility audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T165456Z-codex-event-eligibility-d4d33a75), or [OP03 two-stage intake](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T165944Z-codex-op03-intake-ed488bce). The latter's input schema requires pre-event raw cochains or auditable \(G\), eligibility independent of the target, null windows, independent post-event \(\Theta\) receipts, hashes and chronology. The `Gap2_FINAL_Finite_Genesis.png` attachment remained unavailable and was not used. No held-out outcome was scored.

**Disposition:** EXACT source-convention bridge and finite compatibility audit; CANDIDATE \(\xi_{\rm cand}\) provider; NO-GO for unqualified support-loss triggering; OPEN endogenous event-ready predicate, independent \(\xi\) cause, local \(U_e\) update and physical correspondence. The supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` (Library `libfile_93b66da4fd448191a2b04ca03b93e58c`, §§1–4) is a governance proposal. This constructor check is development work, with non-constructor review pending; physical promotion remains 0.
