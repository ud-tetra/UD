# Four-pattern angular control from the public fixed-height KC grid

**NUMERICAL CONVENTIONAL ONLY; physical promotion 0.**

Input: Minkin *et al.*, *PRB* **108**, 085411 (2023), arXiv:2308.06302, and CC BY 4.0 data DOI 10.17632/svnpzbjc3t.1 at https://data.mendeley.com/datasets/svnpzbjc3t/1 . Archive SHA-256 b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875. Replay uses only X/Y/Z numeric text in the four `data/pes21`, `pes31`, `pes32`, and `pes51` folders; no embedded code executed. Stored Z differences are converted by ×1000 to μeV as the archive's plotting script does. All four grids have 128×129 samples at 3.46 Å.

A six-term free sine/cosine first-star fit uses $|g|=\sqrt{N_c}4\pi/(\sqrt3a)$ and the common archive-frame 30°, 150°, 270° star. Three fitted wave amplitudes agree within each pattern. Phase-sum closure distinguishes the negative index-seven coefficient from positive controls. Derived ideal periodic static shear uses published shape factors: $16\pi\sqrt{N_c}|U_1|/(\sqrt3a^3)$ for the negative branch and $6.183\sqrt{N_c}U_1/a^3$ for the positive branch, converted to MPa.

| Pattern | $N_c$ | Fitted $U_1$ μeV/atom | Ideal static MPa | Ratio to (2,1) | Same-source Table II MPa |
| --- | ---: | ---: | ---: | ---: | ---: |
| (2,1) | 7 | −20.2475 | 16.741 | 1 | 16.7 |
| (3,1) | 13 | +4.6600 | 1.119 | 0.0668 | 1.12 |
| (3,2) | 19 | +0.43385 | 0.1259 | 0.00752 | 0.126 |
| (5,1) | 31 | +0.0011469 | 0.000425 | 0.0000254 | 0.000425 |

The table is a within-model calculation; comparison with Table II is source-reproduction, not independent validation. Archive folder labels `pes21_10x10`, `pes31_6x6`, `pes32_6x6` differ from Table I simulation-cell sizes 18×18, 18×18, 10×10 respectively. The `(5,1)` 11×11 label matches. The archive's exact processing and relation to Table I remain unresolved. No 2026 experimental detection floor, contact area, rate, or force estimator is available; these ideal strengths are not measured friction. The conventional hierarchy is an explicit competing explanation of why only index seven might be detectable.

Run `python3 fit_angular_controls.py /path/to/archive.zip` with NumPy. `ANGULAR_CONTROL_RESULTS.json` contains all amplitudes, phase closure, range, holdout RMS, source table comparisons and source folder labels.
