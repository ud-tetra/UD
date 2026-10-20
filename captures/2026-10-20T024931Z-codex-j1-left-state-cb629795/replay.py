import sys
sys.dont_write_bytecode=True
import argparse,subprocess,os
from pathlib import Path
HERE=Path(__file__).resolve().parent
def main(scalar_only=False):
 if not scalar_only:subprocess.run([sys.executable,'replay.py'],cwd=HERE/'candidate',env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'),check=True)
 import planner,audit
 planner.main();audit.main();print('PASS scalar-only replay' if scalar_only else 'PASS full state flux adaptive replay',flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--scalar-only',action='store_true');a=ap.parse_args();main(a.scalar_only)
