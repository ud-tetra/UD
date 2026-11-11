# THM-534 v0.9 append-only claim and dependency ledger — autonomous positive-stock candidate

**Date:** 2026-10-21 | **Parent:** [v0.8 gate nonidentifiability and finite-circulation no-go](THM534_GATE_SELECTION_AND_CIRCULATION_BUDGET_v0.8.md) | **New theorem:** [v0.9](THM534_AUTONOMOUS_GATE_RESERVOIR_v0.9.md) | **Source:** UD coefficient provenance v0.39, Q153/Q155/Q156/Q158/Q161/Q162 and Q169–Q173 | **Lane:** development, no registry promotion | **Physical promotion:** 0.

| ID | Claim | Mathematical status | Source dependencies | Qualification / next gate |
|---|---|---|---|---|
| S29 | state-generated stock-availability \(\chi_v^{avail}=1_{r_v>0}\), candidate \(h_{uv}=\chi_u\chi_v\beta_u\beta_v\tau_{uv}\); positive reciprocal reservoir update preserves total stock | EXACT CONDITIONAL / CANDIDATE selection | Q156 factorization, Q162 vertex relaxation, new \(r_v\) state | nonnegative stock is not native packet closure; derive \(\chi,b,\tau\) gate predicate |
| S30 | typed source \(s=(r-p)/4\), \(\Delta\rho=B_1j+s\), \(\Delta r=-s\) | EXACT CONDITIONAL | new paired vertex reservoir, Q153/Q155 source ledger | reservoir-to-vertex physical mechanism, units, contacts and clock OPEN |
| S31 | combined 8-stock variance decreases by at least \(\|F\|^2+(3/8)\|p-r\|^2\), hence \(\sum\|F_n\|^2<\infty\) | EXACT / NO-GO within passive update | S25 plus positive symmetric exchange | does not extend to active/reversible current or an external source |
| S32 | autonomous initial stock \(r_0=(1,1,1,0)\), \(\rho_0=e_0\) generates persistent nonuniform gate, transient nonzero face circulation, exact rates \((15\pm\sqrt{97})/32\) | EXACT CONDITIONAL | S29–S31, \(\beta=\tau=1\) | initialized nonuniform reservoir is explicit initial asymmetry, not spontaneous S4 breaking |
| S33 | availability flags can only change 0→1, never 1→0 under passive exchange; complete-cell alternative selector remains valid | EXACT / NO-GO full-closure identification | \(r'=(p+3r)/4,\ p\ge0\) and S23 | derive geometric closure/fracture/recovery, transport/boundary dynamics |
| S34 | externally oriented 3-cycle routing permutation produces perpetual face circulation while conserving nonnegative total vertex stock | EXACT CONDITIONAL / NO-GO on overbroad persistence obstruction | declared signed \(\sigma=(u,v,w)\), route \(k_{uv}=\rho_u\), etc. | this is **not Q162**; independently source rotor orientation, cycle timing and admissibility |

## Source/normalization conflict firewall

1. **S29 stock bit \(\chi^{avail}\) is NOT the frozen intrinsic closure state \(\chi\).** The current v0.39 Q156 only specifies a product of unspecified hard gate predicates. S29 supplies one explicit *candidate* predicate to test consistency, not a recovery of the omitted closure mechanism.
2. **\(r\) is a new 4-vector vertex reservoir** and is not Q172's face-interface reservoir \(S_f^{iface}\), nor Q170's Hasse support control volume, nor physical vacuum/radiation. Equal dimensional counts do not identify carriers.
3. **\(1/4\) appears twice for different operations:** the sourced Q162 relaxational flux and the *new* chosen reservoir exchange. Q161's \(1/4\) is an internal dimensionless attempt clock, **not a theorem that these two rates must coincide**. No parameter-free completed UD dynamics is claimed.
4. **The strong S31 no-go is about dissipative mixing**, not about universal finite closed-source conservation. S34 is the necessary adversarial control: directed transport with a signed cycle register can conserve total burden and sustain circulation, but its rotor is extra specified structure.
5. **Stored stock is not physical energy.** There is no calibrated proper time, metric-action choice, conserved physical stress-energy tensor, Holonomy/U(1) map, six-edge Markov probability/renewal mechanism or confirmed particle-sector bridge.
6. Historical THM-534 target matrix \((1/2,1/6,1/12)\) was known before the new construction; all v0.9 model selection is **target-exposed exploratory**, not preregistered target-blind.

## Evidence and verification

- Full local constructor script [verify_thm534_autonomous_reservoir_v0_9.py](verify_thm534_autonomous_reservoir_v0_9.py) (local release package) checks exact first stocks/source/circulation, exact eigenvalues, exact Lyapunov budget, exact 24 S4 relabelings, 4,096 exact boundary/support/integrity input cases, nine rotor steps and 8,192 numerical reservoir-update steps. Local output: PASS_SCOPED, 4,096 nonuniform mask steps and 1,574 transient nonzero face circulations, max total-stock drift \(1.7763568394002505\times10^{-15}\); max numerical deficit of an exact nonnegative Lyapunov remainder \(1.1401454618356886\times10^{-16}\); max oriented face-closure residual 0.
- [Published compact exact verification](verify_thm534_autonomous_reservoir_v0_9.py): an independent file transcription, not asserted byte-equal to the local full script.
- [Independently coded Fraction verification](verify_thm534_reservoir_fraction_v0_9.py): pure Python stdlib, 64 exact controls, 24 nonzero face witnesses, exact conservation, signed face closure and Lyapunov inequality. Different implementation from full SymPy code, **same constructor**, not independent non-constructor review.
- **Review status:** constructor checks and source reasoning complete; independent adversarial review and separate external replication OPEN. No CRL status promotion.
- **GitHub status:** research branch only; draft PR #346; main unmerged. Direct Project board membership not verified.

## Decision / reopening conditions

**AUTO_LOCK scoped mathematics** S29–S34 conditional proofs, with assumptions preserved. **AUTO_FREEZE** identification of stock-availability bit with native closure, indefinite circulation from passive reservoir replenishment, uniqueness/necessity of the \(1/4\) reservoir exchange, intrinsic rotor-source selection and historical THM-534 physical correspondence.  
**OPEN_GATED:** an admitted cell-closure and boundary-state evolution \(U_{\chi,b,\tau}\); reservoir location/ownership and true positive-stock creation/consumption; oriented reversible transport work/entropy and event-time rules; unique edge route/holonomy; non-constructor review. No physical promotion.
