# UD Provenance Ledger Addendum — Hard Gate + E2 Dry Run 2026-09-14 v0.7

**Physical promotion:** 0

| ID | Object | Exact form | Claim bin | Status | Next gate |
|---|---|---|---|---|---|
| HG01 | hard face mask | \(H=\mathrm{diag}(h_f),\ h_f\in\{0,1\}\) | LOCKED_SOURCE_STRUCTURE | AUTO_LOCK | source actual \(h_f\) |
| HG02 | gated C2 equation | \(\dot c_2=B_2^Tc_1-HB_3c_3\) | EXACT_CONDITIONAL | AUTO_LOCK / declared hard-gate carrier | none |
| HG03 | gated C3 equation | \(\dot c_3=B_3^THc_2-B_4c_4\) | EXACT_CONDITIONAL | AUTO_LOCK / skew pair | none |
| HG04 | gate residual pair | \((I-H)B_3c_3,\ -B_3^T(I-H)c_2\) | EXACT_INTERNAL | AUTO_REPAIR / generator difference | no open-source interpretation |
| HG05 | gate support cancellation | \(2c_2^Tr_2^{(H)}+2c_3^Tr_3^{(H)}=0\) | EXACT_INTERNAL | AUTO_LOCK | none |
| HG06 | hidden-to-contrast operator | \(T_H=B_3^TH(I-P_{23})\) | EXACT_INTERNAL | AUTO_LOCK | source-bound state/mask |
| HG07 | nonuniform-mask theorem | \(T_H\neq0\) for 1022/1022 nonuniform masks | LOCKED_COMPUTATIONAL_THEOREM | AUTO_LOCK / exhaustive \(2^{10}\) audit | none |
| HG08 | rank distribution | \(0:2,1:20,2:110,3:460,4:432\) | EXACT_COMPUTED | AUTO_LOCK | none |
| HG09 | zero-C2 pure-top gate creation | impossible | LOCKED_NO_GO | AUTO_LOCK | pre-existing/context support |
| DRY01 | apparatus binding replay | PASS METHOD | PROTOCOL_CONTROL | AUTO_LOCK / SYNTHETIC ONLY | real lab |
| DRY02 | state qualification | PASS, \(Z_{23}=70.710678...\) synthetic | PROTOCOL_CONTROL | METHOD PASS ONLY | real calibration |
| DRY03 | E2 carrier replay | 12/12 PASS synthetic | PROTOCOL_CONTROL | METHOD PASS ONLY | real acquisition |
| DRY04 | provider merge replay | 12/12 ready synthetic | PROTOCOL_CONTROL | METHOD PASS ONLY | real source returns |
| DRY05 | multi-slip negative | FAIL_E2_CARRIER | PROTOCOL_CONTROL | PASS NEGATIVE CONTROL | none |
| DRY06 | missing leakage negative | NO_SCORE_MISSING_CHANNEL | PROTOCOL_CONTROL | PASS NEGATIVE CONTROL | none |
| DRY07 | state qualification validator | frozen 3-sigma executable | PROTOCOL_CONTROL | APPEND-ONLY REPAIR | real use |
