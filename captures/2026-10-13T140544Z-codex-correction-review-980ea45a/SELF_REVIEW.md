# Corrected source edition — constructor review

**Scope:** v0.1 corrections in PR #57, not every claim in the original pasted
conversation. **Review kind:** constructor self-review, not independent review.
**Lane:** development — no registry entry. **Physical promotion:** 0.

## Findings and revisions

**R10 — labeled move gap.** The v0.1 table used two valid carrier representatives
with the correct individual spectra, but their outer face sets were unequal.
It therefore did not identify a single labeled 2↔3 move. This was found during
constructor review, after publication of PR #57. v0.2 fixes the pair:

| Side | Cells | Interior simplex |
|---|---|---|
| \(K_-\) | \(0234,1234\) | shared face \(234\) |
| \(K_+\) | \(0123,0124,0134\) | common edge \(01\) |

The oriented cell chains
\[
[0234]-[1234]\quad\text{and}\quad[0123]-[0124]+[0134]
\]
have equal boundaries. Both have the six outer faces
\(023,024,034,123,124,134\). The old cell table fails this check as a
negative control. A signed vertex relabeling maps the old two-cell representative
to the new one and intertwines its boundary-derived generator and edge
Laplacian. The individual edge spectra remain unchanged.

Embedding the revised pair in the unique-simplex register of
\(U=\partial\Delta^4\), with dimensions \((5,10,10,5)\), reproduces
\(\operatorname{rank}(A_+^U-A_-^U)=18\) and nullity 12 by exact rational
elimination. This is consistent with the frozen UD result. These inclusions
compare operators; they do not choose a transfer law between the two states.

**R11 — line versus signed ray.** A rank-one projector cannot distinguish
\(x\) and \(-x\). The positive projective representative reconstructed by
real PSR retains the component-root signs. v0.2 explicitly distinguishes
preservation of the projector line, \(Vx=\pm x\), from preservation of the
positive signed ray, \(Vx=x\), for nonzero input in the polar eigenvector
example. This is a terminology clarification; the prior rotated-ray
counterexample remains valid.

## Checks and retained boundaries

The new checks verify cell-boundary equality with orientation, covariance under
signed relabeling, ambient dimensions, exact overlap rank and the line/ray sign
counterexample. The corrected source replay still verifies the generator,
contraction signs, spectral polynomial/rank certificates, Hodge sectors and
the script's syntax rejection. The script remains unexecuted as source code.

An additional independently declared scalar transport fixture with broadenings
\(\Gamma_L=1,\Gamma_R=2\) gives resonant transmission \(8/9\), from
\(4\Gamma_L\Gamma_R/(\Gamma_L+\Gamma_R)^2\). Thus even the corrected
coherent transport contract does not imply generic unit transmission. This
algebraic illustration is not a recovered UD disorder experiment.

No new error was found in the four scoped mathematical correction families
apart from the labeling and terminology revisions above. This statement is a
record of this review, not a proof of completeness or an independent verdict.
The proposed governance amendment remains a proposal. No CRL rung, registry
status or physical identification is promoted.

## Remaining gate

The corrected edition is ready for a non-constructor review of its defined
scope. Separately, any development beyond it must declare the state, operator,
sampling interval, transfer/reset law and observables it uses. The native memory
result from PR #51 is not extended to glued carriers or variable clocks by this
review. The numerical target 238.14 remains unevaluated. Other original source
passages remain unaudited; the missing Genesis image is not evidence.
