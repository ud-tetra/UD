# UD gluing review candidate 0.7

Read the top-level narrative manuscript 0.7 and `UD_Gluing_Memory_Theorems_v0.1.md`. The latter states the precise contracts, proof, excluded controls and literature boundary. Earlier manuscript versions remain preserved separately; 0.7 supersedes 0.6 for development.

## Replay

Run `python3 verify_gluing.py` with SymPy. It regenerates `GLUING_CHECKS.json` and the exact certificates for five carriers. Three heterogeneous nonzero-weight examples, a symbolic private-block Gram identity, zero-weight controls and a decoupled hidden-oscillator control are included. The five-cell closed-boundary case has a certified 20-dimensional invariant unobservable basis.

The proof, not fixture count, establishes the whole stacked family. These checks do not establish novelty, independent review, acquisition accuracy or a physical memory cost.

Four companion sources are in `sources/`. Previous, unchanged replays are organized in `prior_replays/carriers/`, `prior_replays/apparatus/` and `prior_replays/symmetry/`. Run them in disposable copies if needed; they regenerate their own output files. Their inclusion does not claim a fresh execution in this turn. Source-only covariance, radial and historical apparatus audits remain within their original stated scopes.

`ENVIRONMENT.json` records the constructor environment. `SOURCE_HASHES.json` pins the inspected baseline; `SHA256SUMS.json` inventories the release except itself. Physical promotion: 0. This is a constructor-checked review candidate, not an accepted submission.

## Next publication gates

Assess the specialized gluing theorem against nearby model-reduction and simplicial literature. Challenge the reverse-attachment argument and linear initialization contract independently. Then develop conditioning/noise bounds and execute a fresh-environment replay. Complete author and venue declarations before submitting.
