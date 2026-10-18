#!/usr/bin/env python3
"""Reproduce into a fresh location without trusting bundled numerical output."""
import sys,shutil,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
if len(sys.argv)!=2:raise SystemExit('usage: python replay.py NEW_DIRECTORY')
dst=Path(sys.argv[1]).resolve();dst.mkdir(exist_ok=False)
p=dst/'nominal-work';p.mkdir()
for f in (root/'nominal-work').iterdir():
 if f.suffix=='.py' or f.name=='requirements.txt':shutil.copy2(f,p/f.name)
shutil.copytree(root/'nominal-work/sources',p/'sources');shutil.copytree(root/'spectral-work',dst/'spectral-work')
subprocess.run([sys.executable,str(p/'run_all.py')],check=True)
