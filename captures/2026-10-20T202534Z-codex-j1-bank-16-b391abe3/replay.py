import sys
sys.dont_write_bytecode=True
import diagnostic,refinement_diagnostic,scout,gap_witness
for module in [diagnostic,refinement_diagnostic,scout,gap_witness]:module.main()
print('PASS saved unresolved-cover and formula-gap replay; no uniform extension',flush=True)
