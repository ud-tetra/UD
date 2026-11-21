# Release_Gate_Audit · v0.87-preview

**Gate status** · Held for independent review  
**Physical Promotion = 0**

## Dashboard card copy

The PB5 radial sink, shear and holonomy results (#583–#586) and the two-cell exterior settling result (#590) are on main. The coarse-graining architecture (#588), two-cell memory derivation (#589), and release candidate note (#587) remain drafts. GitHub records maintainer and constructor comments. Independent scope-locked review is still outstanding across #583–#590.

| Work item | Repository status | Supported scope |
| --- | --- | --- |
| [#588 · Coarse-graining architecture](https://github.com/ud-tetra/UD/pull/588) | Draft · [CI passed](https://github.com/ud-tetra/UD/actions/runs/44943179328) | Explicit resolved projection and conditional transport and cubic coefficients. The continuum closure and native constitutive parameters remain open. |
| [#589 · Two-cell memory](https://github.com/ud-tetra/UD/pull/589) | Draft · [CI passed](https://github.com/ud-tetra/UD/actions/runs/44943650927) | The specified internal Whitney edge sink gives zero decay in both memory channels. The specified exterior sink yields positive decay in the memory-active blocks. |
| [#590 · Exterior settling](https://github.com/ud-tetra/UD/pull/590) | [Merged at 729e84c](https://github.com/ud-tetra/UD/commit/729e84cc0c356487ca7184827b1827b6cd1d22f7) · [CI passed](https://github.com/ud-tetra/UD/actions/runs/44944127904) | With per-channel normalization and \(T=2\pi/\sqrt{32/7}\approx2.938690840\) carrier time units, \(\gamma_{\rm ext}=2.071267496\ldots\) is the minimum for both kernel tails to stay at or below \(1/62\) for all \(\tau\ge T\). |

The settling calculation uses \(1/62\) as a specified numerical tolerance. Its correspondence to the coherence-law ambiguity and an error-controlled Markov approximation remain open. At the minimum the binding even-channel peak meets the tolerance with equality, after the chosen horizon.

## Release gate evidence

- Record independent post-merge dispositions for #583–#586 and #590, and independent review of the final heads for #587–#589.
- Reconcile the candidate manifest with the final integrated set and verify capture bytes and CI against the release target.
- The candidate remains untagged. The annotated preview tag is gated on the recorded reviews and final release verification.

This snapshot updates status in the original candidate note and the later digest addendum. The captured files themselves are immutable.
