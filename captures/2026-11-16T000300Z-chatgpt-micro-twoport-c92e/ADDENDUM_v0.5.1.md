# Two-port v0.5.1 — face-transfer coefficient correction

**Date:** 2026-11-16 UTC. **Type:** explicit publication erratum; no physical promotion or new theorem. **Supersedes in scope:** only the inconsistent face-transfer notation in v0.5 `REPORT.md` §3. Original version preserved unchanged.

## Replaced statement

`REPORT.md` §3 displayed `q_{f→g}=x_f p_+(dπ/2) w_{fg}` and then described unit internal edge weighting as if the internal rate were `x_f`. Those two statements are inconsistent.

## Correct source-bound candidate rule

For adjacent face pairs `f,g`, define

\[
W_{fg}(d)=\begin{cases}
1,&\text{internal face-pair edge},\\
p_+(d\pi/2),&\text{interfacial face-pair edge},
\end{cases}\qquad
\boxed{q_{f\to g}(b,d,x)=x_f W_{fg}(d)}.
\]

Here `p_+` is **used exactly once** on interfacial moves, while internal transfers use unit weight; no phase multiplier acts on internal transfers. `W` is an assumed face-pair mobility classification, **not** a source-derived native rule. The model and tests `verify.py` and `replay_portable.py` already implemented exactly this corrected expression; no code, stationary measure, count, derivative, or result changed.

This correction is required for faithful transfer of the reported executable model. It does not address the still-open microscopic channel norm allocation, event clock, phase-noise generator, donor source law or physical readout. **G05/G06 OPEN; Physical Promotion = 0.**
