# UD Coefficient Provenance Ledger v0.39R1 — Reconciled Export

**Reconciliation date:** 2026-08-30  
**Canonical source baseline:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39` (2026-08-22)  
**Reconciliation type:** `EDITORIAL/PROVENANCE_RECONCILIATION_ONLY`  
**Typed objects:** **235**  
**Physical promotion:** **0**

This export does **not** replace v0.39 with a new scientific coefficient set. It preserves all 235 source rows and adds current-use classes, notation normalization for display, collision guards, and a glossary.

## Authority rule

The v0.39 source remains the coefficient source of record for this package. Historical/source-stratum telemetry or earlier operational PASS language does not supersede a later v0.39 OPEN, QUARANTINED, SOURCE_STRATUM, or EXPELLED status unless a newer canonical ledger explicitly does so.

## Claim-bin distribution

- `EXACT_CONDITIONAL`: **68**
- `EXACT_INTERNAL`: **44**
- `DERIVED_STRUCTURAL`: **36**
- `LOCKED_INTERNAL_MATHEMATICS`: **22**
- `QUARANTINED_CANDIDATE`: **14**
- `SOURCE_STRATUM`: **10**
- `LOCKED_MATHEMATICAL_GEOMETRY`: **9**
- `NOT_A_COEFFICIENT`: **7**
- `COMPUTED_BRIDGE`: **4**
- `LOCKED_NO_GO`: **4**
- `SIMULATION_CALIBRATED`: **4**
- `PROTOCOL_CONTROL`: **3**
- `EXACT_PROXY`: **2**
- `EXPELLED`: **2**
- `LOCKED_SOURCE_STRUCTURE`: **2**
- `LOCKED_STATUS`: **2**
- `OPEN_GAP`: **2**

## Reconciled canonical ledger

| ID | Display symbol | Source symbol | Exact form | Claim bin | Current-use class | Status | Next gate | Reconciliation notes |
|---|---|---|---|---|---|---|---|---|
| P01 | V(K_4) | V(K4) | 4 | EXACT_INTERNAL | CURRENT_EXACT | ACTIVE ROOT GENERATOR | none for count; physical dimension interpretations remain downstream |  |
| P02 | E(K_4) | E(K4) | 6 | EXACT_INTERNAL | CURRENT_EXACT | ACTIVE ROOT GENERATOR | none for count |  |
| P03 | \\|Aut(K_4)\\| = \\|S_4\\| | \\|Aut(K4)\\| = \\|S4\\| | 24 | EXACT_INTERNAL | CURRENT_EXACT | ACTIVE ROOT GENERATOR | none for group order |  |
| P04 | \\|\Theta\\| | \\|Theta\\| | 2^3 = 8 | EXACT_INTERNAL | CURRENT_EXACT | ACTIVE ROOT GENERATOR | closure/admissibility rule must justify the unique reference state |  |
| P05 | N_1 | N1 | 24 * 8 = 192 | EXACT_INTERNAL | CURRENT_EXACT | ACTIVE / SECTION-7 DEPENDENCY | any observable interpretation must be derived separately |  |
| P06 | \Delta_\theta | Delta_theta | 8 - 1 = 7 | EXACT_INTERNAL | CURRENT_EXACT | ACTIVE / SECTION-7 DEPENDENCY | continue to preserve the closure-rule proof independently of downstream matches |  |
| P07 | G_{1,default} | G1_default | 4 | COMPUTED_BRIDGE | BRIDGE | DEFAULT NATIVE SELECTOR WITH TESTED-SCOPE GUARD | general branch grammar / larger-scope recurrence |  |
| P08 | G_{1,dense} | G1_dense | 12 | COMPUTED_BRIDGE | BRIDGE | ADMISSIBLE DENSE ALTERNATE | global consistency / dense-branch recurrence |  |
| P09 | N_{2,default} / N_{2,dense} | N2_default / N2_dense | 768 / 2304 | DERIVED_STRUCTURAL | CURRENT_DERIVED | BRANCH-SPLIT LADDER CANDIDATES | branch selector generalization |  |
| P10 | N_{layer} | N_layer | 4 * 8 = 32 | QUARANTINED_CANDIDATE | QUARANTINED | STRONG NATIVE LAYER-DEPTH CANDIDATE; CURRENT BANACH ATTENUATION OVER-SUPPRESSES; TERMINATION/NORMALIZATION OPEN | prove the 32-layer termination and per-layer attenuation normalization independently of the hierarchy target | quarantined; blocked from settled mainline use; 32 is native-count supported but sequential depth/termination remains unproved |
| F01 | R_d | R_d | (d+1)/d, d>=1 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / DIMENSION-TYPED FRAME FAMILY | none for frame identity; any dynamics using a special R_d needs an independent source law |  |
| F02 | C_d | C_d | d/(d+1), d>=0 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / DIMENSION-TYPED RECIPROCAL FAMILY | none for frame/norm identity |  |
| F03 | R_3^(tet-face) | R_3^(tet-face) | 4/3 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT COFRAME-SHAPE FACTOR UNDER DECLARED DYAD DEFINITION | physical coframe interpretation requires independent continuum/transport bridge | COLLISION-02: same rational value, different types |
| F04 | C_3^(tet-center) | C_3^(tet-center) | 3/4 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT GEOMETRIC LOCATION; OLD9 DYNAMICAL REUSE FROZEN | any dynamical use must be independently source-derived | COLLISION-03: repeated 3/4 value on different carriers |
| F05 | R_4^(5-state address) | R_4^(5-state address) | 5/4 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT ADDRESS-FRAME IDENTITY | none for address-frame identity |  |
| F06 | dim Sym^2_0(3) | dim Sym^2_0(3) | 5 = 2 + 3 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT OPERATOR-SPACE DIMENSION | deficit-allocation/interface map if used as divisor in alpha_struct | COLLISION-08: repeated dimension/value 5 |
| C01 | r_\Delta | r_Delta | 7/192 | EXACT_INTERNAL | CURRENT_EXACT | LOCKED INTERNAL STRUCTURAL RATIO | none for arithmetic; each physical alias needs its own gate |  |
| C02 | r_{retain} | r_retain | 185/192 | EXACT_INTERNAL | CURRENT_EXACT | LOCKED INTERNAL STRUCTURAL RATIO | physical spectral-index interpretation requires its own cosmology proof |  |
| C03 | C_vertex | C_vertex | 7/768 | DERIVED_STRUCTURAL | CURRENT_DERIVED | ACTIVE STRUCTURAL RATIO; PHYSICAL CAPACITY LANGUAGE SCOPED | derive the local admissibility law independently of physical cutoff claims |  |
| C04 | \beta_{UD} | beta_UD | ln(192/185) | DERIVED_STRUCTURAL | CURRENT_DERIVED | ACTIVE STRUCTURAL FLOW COEFFICIENT; RG INTERPRETATION NOT PRIMITIVE | derive the dynamics that make this logarithm the actual coarse-scale flow rate |  |
| C05 | d_seat | d_seat | 5 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT NATIVE FIVE-DIMENSIONAL RESPONSE SPACE | none for dimension; any deficit-to-response allocation law is separate | COLLISION-08: repeated dimension/value 5 |
| C06 | \alpha_{struct}^{(0)} | alpha_struct^(0) | 7/960 | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK EXACT INTERNAL NORMALIZED RATIO / AUTO_FREEZE AS CURRENT q-PAIRING HAMILTONIAN COEFFICIENT | derive an independent S4-invariant source functional before any physical coupling interpretation | 7/960 is an exact internal normalized ratio; physical coupling interpretation is frozen |
| C07 | S0 | S0 | 43/7 | DERIVED_STRUCTURAL | CURRENT_DERIVED | B1-D DERIVED FORMAL / ACTIVE INTERNAL SUPPORT | maintain consistency between the two support derivations and current packet grammar |  |
| C08 | H | H | 101/6 | DERIVED_STRUCTURAL | CURRENT_DERIVED | B1-D DERIVED FORMAL; PHYSICAL IDENTITY GAP OPEN | continue reconciliation of parity doubling, identity increment, coherence rebate, and C3_7 burden ledger | 101/6 is structural H/heavy-lift quantity; physical identity/B_e equality remains open |
| C09 | C_star | C_star | 7/8 | SOURCE_STRATUM | SOURCE_STRATUM | SOURCE-STRATUM / NEEDS CURRENT REBASE | re-derive under current finite-register admissibility grammar | historical/source-layer; not current physical canon |
| C10 | Q_agree / Q_Koide | Q_agree / Q_Koide | 2/3 | SOURCE_STRATUM | SOURCE_STRATUM | NOTATION COLLISION / CONTEXT QUALIFICATION REQUIRED | split symbols by mechanism and re-audit each route | historical/source-layer; not current physical canon; COLLISION-04: 2/3 notation/value collision |
| Q01 | Q_A,Q_B,Q_C coefficients | Q_A,Q_B,Q_C coefficients | permutations of (-2/3, 1/3, 1/3) | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXPLICIT PAIRING 2-IRREP REALIZATION | source dynamics must supply a nonzero weight contrast to activate energy in this channel |  |
| Q02 | \\|\\|Q_i\\|\\|_F^2 | \\|\\|Q_i\\|\\|_F^2 | 2/3 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT OPERATOR NORM | none for norm | COLLISION-04: 2/3 notation/value collision |
| Q03 | R_pair-op | R_pair-op | 3/2 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT PAIRING-OPERATOR FRAME CONSTANT | none for frame identity; source amplitude remains separate |  |
| Q04 | a_star = K_q^star/G | a_star = K_q^star/G | 3/2 | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK / CURRENT SOURCE-COMPLETE q-SCALAR BLOCK | non-scalar q activation requires independently derived edge-class contrast or other lawful source asymmetry |  |
| Q05 | b_star = K_m^star/G | b_star = K_m^star/G | 11/4 | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK / CURRENT SOURCE-COMPLETE m-SCALAR BLOCK | boundary/source corrections may split modes but physical units remain downstream |  |
| Q06 | kappa_q,pair^current | kappa_q,pair^current | 0 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / CURRENT SOURCE-SELECTED PAIRING q AMPLITUDE IS ZERO | derive unequal edge-class source weights or another lawful source if a nonzero q quadrupole is proposed | COLLISION-07: zero-valued source amplitudes with distinct provenance |
| Q07 | mu_partial | mu_partial | {0, 1/9, 1/3} | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK / BASIS-INDEPENDENT BOUNDARY SPECTRUM | recover retained m representation/intertwiner for S4 channel alignment |  |
| Q08 | mu_bar | mu_bar | 4/27 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT ISOTROPIC BOUNDARY SHIFT | none for mean; source amplitude lambda_partial remains separate |  |
| Q09 | spec(T_partial) | spec(T_partial) | {-4/27, -1/27, 5/27} | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT TRACELESS BOUNDARY ANISOTROPY | recover rho_m(g) or an explicit intertwiner U |  |
| Q10 | Tr(T_partial^2) | Tr(T_partial^2) | 14/243 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT BOUNDARY ANISOTROPY INVARIANT | representation alignment for channel-specific meaning |  |
| Q11 | omega_0^2 | omega_0^2 | 33/8 | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK / EXACT MODE BASELINE WITHIN CURRENT RETAINED HAMILTONIAN | physical mapping and broader source generality downstream |  |
| Q12 | r_0^2 | r_0^2 | 11/6 | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK / EXACT MODE RESPONSE FACTOR | same as Q11 |  |
| Q13 | lambda_partial(zeta) | lambda_partial(zeta) | beta_F^2/(zeta-Delta_F); positivity requires lambda_partial > -33/4 | EXACT_CONDITIONAL | CURRENT_CONDITIONAL | AUTO_LOCK CONDITIONAL FAMILY FORM / PRIMITIVE AMPLITUDE AND GAP SOURCE-BLOCKED | recover explicit radial vertical Hamiltonian D_F and coupling block B_F from source data |  |
| Q14 | kappa_pair^(uniaxial contrast coordinate) | kappa_pair^(uniaxial contrast coordinate) | kappa = W_A-W_B = W_A-W_C on W_B=W_C; -9/2 < kappa < 9/4 | EXACT_CONDITIONAL | CURRENT_CONDITIONAL | AUTO_LOCK / UNIAXIAL EDGE-CLASS CONTRAST COORDINATE; CURRENT VALUE 0 UNDER EQUAL WEIGHTS | derive actual W_A,W_B,W_C from packet source dynamics; no target backsolve |  |
| Q15 | c_partial,2 / c_partial,3 | c_partial,2 / c_partial,3 | UNRESOLVED | QUARANTINED_CANDIDATE | QUARANTINED | AUTO_FREEZE / NOT CANONICALLY COMPUTABLE FROM SPECTRUM ALONE | BOUNDARY_PAIRING_ALIGNMENT_SOURCE_RECOVERY_GATE: recover rho_m(g) or U in the same basis as S_partial | quarantined; blocked from settled mainline use |
| Q16 | E_5(T_partial) | E_5(T_partial) | 14/1215 | EXACT_INTERNAL | CURRENT_EXACT | AUTO_LOCK / EXACT SCALAR RESPONSE DENSITY | none for invariant; physical source interpretation separate |  |
| Q17 | beta_F | beta_F | OPEN | QUARANTINED_CANDIDATE | QUARANTINED | AUTO_FREEZE AGAINST HISTORICAL SYMBOL REUSE / SOURCE-BLOCKED | recover B_F and derive B_F B_F^T normalization | quarantined; blocked from settled mainline use |
| Q18 | Delta_F | Delta_F | OPEN | QUARANTINED_CANDIDATE | QUARANTINED | AUTO_FREEZE AGAINST HISTORICAL Delta REUSE / SOURCE-BLOCKED | recover D_F and derive its spectrum | quarantined; blocked from settled mainline use |
| Q19 | zeta_F (operative spectral point) | zeta_F (operative spectral point) | OPEN | QUARANTINED_CANDIDATE | QUARANTINED | SOURCE-BLOCKED / NO TARGET-BACKSOLVE | derive state/energy selection rule from fine Hamiltonian | quarantined; blocked from settled mainline use |
| Q20 | delta_pair = (delta_A,delta_B,delta_C) | delta_pair = (delta_A,delta_B,delta_C) | delta_i=W_i-(W_A+W_B+W_C)/3; delta_A+delta_B+delta_C=0 | NOT_A_COEFFICIENT | NON_COEFFICIENT | AUTO_LOCK / EXACT SOURCE VARIABLE FAMILY; CURRENT EQUAL-CELL STAR HAS delta_pair=0 | derive W_A,W_B,W_C from lawful defect, boundary, burden-current, or transport-cost dynamics | not a tunable coefficient |
| Q21 | A_pair^2 = \\|\\|Q_src\\|\\|_F^2 | A_pair^2 = \\|\\|Q_src\\|\\|_F^2 | delta_A^2+delta_B^2+delta_C^2 = [(W_A-W_B)^2+(W_B-W_C)^2+(W_C-W_A)^2]/3 | DERIVED_STRUCTURAL | CURRENT_DERIVED | AUTO_LOCK / EXACT DYNAMIC SOURCE INVARIANT; CURRENT VALUE 0 UNDER EQUAL WEIGHTS | test source histories that generate nonzero class-weight contrast without fitting |  |
| G01 | g_G^lat = G_eff^lattice | g_G^lat = G_eff^lattice | 3/(4*pi) | SIMULATION_CALIBRATED | PROTOCOL_CALIBRATED | PASS_LOCKED WITHIN TESTED PROTOCOLS | physical scale mapping and broader observable/general-topology validation | COLLISION-01: same numerical form, distinct provenance |
| G02 | beta_A | beta_A | 1/12 | SIMULATION_CALIBRATED | PROTOCOL_CALIBRATED | PASS_LOCKED WITHIN R10a | replication across additional source classes/topologies |  |
| G03 | kappa_C^(legacy) | kappa_C^(legacy) | 3/(4*pi) | SOURCE_STRATUM | SOURCE_STRATUM | SOURCE-STRATUM / NUMERICALLY COLLIDES WITH G01 BUT PROVENANCE REMAINS DISTINCT | prove equivalence or keep symbols permanently distinct | historical/source-layer; not current physical canon; COLLISION-01: same numerical form, distinct provenance |
| G04 | epsilon_G | epsilon_G | 1/1000 | PROTOCOL_CONTROL | PROTOCOL_CONTROL | CONTROL ONLY | sensitivity/robustness study if promoted as a methodological standard | method control only |
| B01 | sin^2(theta_W)^(legacy) | sin^2(theta_W)^(legacy) | 3/13 | SOURCE_STRATUM | SOURCE_STRATUM | REBUILD/REBASE REQUIRED BEFORE CURRENT CANON | target-blind current gauge derivation with normalization proof | historical/source-layer; not current physical canon |
