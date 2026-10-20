import sys
sys.dont_write_bytecode=True
import planner
planner.main()
import audit
audit.main()
print('PASS saved scalar existing-bank replay',flush=True)
