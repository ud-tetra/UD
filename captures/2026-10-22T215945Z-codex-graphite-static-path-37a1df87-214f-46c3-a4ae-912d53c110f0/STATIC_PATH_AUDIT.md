# Conventional two-shell static path audit

Source: Minkin *et al.*, *PRB* **108**, 085411 (2023), arXiv:2308.06302; raw public Mendeley Data DOI 10.17632/svnpzbjc3t.1, CC BY 4.0, exact archive SHA-256 b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875. Its `data/pes21_10x10_Rc=16_lz=3.46` folder label differs from the article Table I `(2,1)` 18×18 simulation-cell entry. We cannot resolve this provenance detail; report fitted *archive-grid* results, not guaranteed Table I's exact computation.

At z=3.46 Å, fit a constant and separate sine/cosine terms at all three index-seven reciprocal vectors. Then optionally add the next allowed common norm-three reciprocal shell (three more wavevectors). Solve for the stationary minimum and nearby index-one saddles in the three nearest translation directions. The Hessian eigenvalues have opposing signs at each saddle. Evaluate maximum tangential derivative on each *straight* minimum-to-minimum segment; divide force per carbon atom by area per atom $\sqrt3 a^2/4$. The script never executes archived plotting code.

- First shell: nearby saddle barrier 80.954–81.032 μeV/atom; straight-path maximum shear 16.734–16.750 MPa.
- First plus norm-three shell: 78.212–78.243 μeV/atom; straight-path maximum shear 16.224–16.230 MPa.
- The difference (~2.8 μeV/atom barrier; ~0.51 MPa straight-path peak) is entirely an ordinary conventional second-shell correction for this *fixed-height* KC simulation. It is not a UD prediction, and no global MEP proof for the two-shell surface or dynamic contact-force calculation is claimed.

Replay: `python3 derive_kc_barrier_replay.py /path/to/archive.zip`, with NumPy and SciPy. JSON contains all three directions and their Hessian signs. No 2026 force data, vertical PES family, contact area calibration or bath source. Physical promotion 0.
