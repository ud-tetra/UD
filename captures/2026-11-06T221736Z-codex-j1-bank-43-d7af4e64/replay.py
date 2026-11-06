import sys
sys.dont_write_bytecode=True
if __name__=='__main__':
 import planner
 planner.main()
 import audit
 audit.main()
 print('PASS existing-bank cover and actual-evaluator replay',flush=True)
