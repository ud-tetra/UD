import subprocess,pathlib,os
p=pathlib.Path(__file__).parent; jobs=[]
for i in range(4):
 f=(p/f'case_{i}.log').open('w');jobs.append((subprocess.Popen(['python3','-u',str(p/'calculate_reduced.py'),str(i)],stdout=f,stderr=subprocess.STDOUT),f))
for j,f in jobs:
 code=j.wait();f.close();print('case_exit',code,flush=True)
