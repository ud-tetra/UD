import sys
sys.dont_write_bytecode=True
import argparse,subprocess,os
from pathlib import Path
HERE=Path(__file__).resolve().parent
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--scalar-only',action='store_true');a=ap.parse_args()
 if not a.scalar_only:subprocess.run([sys.executable,'replay.py'],cwd=HERE/'candidate',env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'),check=True)
 import diagnostic,scout,planner
 diagnostic.main()
 scout.main()
 planner.main()
 import audit
 audit.main()
 print('PASS refined scalar replay',flush=True)
