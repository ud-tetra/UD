import sys
sys.dont_write_bytecode=True
import planner,audit
planner.main();audit.main()
print('PASS saved adaptive cover and placement replay',flush=True)
