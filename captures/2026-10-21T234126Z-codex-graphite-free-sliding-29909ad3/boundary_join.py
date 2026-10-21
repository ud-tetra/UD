from pathlib import Path
from fractions import Fraction as F
import json,hashlib
p=Path(__file__).resolve().parent;src=p.parent/'lammps-runtime/lammps/share/lammps/potentials/CH.rebo';tokens=src.read_text().split('# gC1 and gC2',1)[1].split('# gH',1)[0].split();n=int(tokens[0]);coeff=[[F(x) for x in tokens[1+n+6*i:1+n+6*(i+1)]] for i in range(8)];records=[]
for name,offset in [('gC1',0),('gC2',4)]:
 for k in range(4):
  vals=[]
  for idx in [offset+1,offset+2]:
   cc=coeff[idx]
   for _ in range(k):cc=[i*v for i,v in enumerate(cc)][1:]
   vals.append(sum(v*F(-1,2)**i for i,v in enumerate(cc)))
  if k<=2:assert vals[0]==vals[1]
  records.append(dict(family=name,order=k,left=str(vals[0]),right=str(vals[1]),jump=str(vals[1]-vals[0])))
(p/'BOUNDARY_JOIN.json').write_text(json.dumps({'source':str(src.relative_to(p.parent)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'arithmetic':'Exact rational interpretation of stored decimal coefficients; does not model every binary floating-point operation.','records':records,'status':'C2_SCALAR_JOINS_VERIFIED','physical_promotion':0},indent=2)+'\n');print(records)
