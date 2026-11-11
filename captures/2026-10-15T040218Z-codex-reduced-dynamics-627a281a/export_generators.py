from pathlib import Path
import json
R=Path(__file__).resolve().parent
data=json.load(open(R/'ALL_REDUCED_BLOCKS.json'))
pows=[]
for k in range(10):
 v=[0]*10;v[k]=1
 for d in range(9,3,-1):
  for j,s in enumerate([-1,1,-1,1]):v[d-4+j]+=s*v[d]
 pows.append(v[:4])
def star(co):return [sum(co[k]*pows[-k%10][j] for k in range(4)) for j in range(4)]
cuts=[0,12,84,204,264];out=[]
for block in data['blocks']:
 entries=[]
 for k,B in enumerate(block['B1_B2_B3'],1):
  for i,j,*co in B['entries']:
   entries.append([cuts[k-1]+i,cuts[k]+j,k,*[-v for v in co]])
   entries.append([cuts[k]+j,cuts[k-1]+i,k,*star(co)])
 d={(i,j,k):co for i,j,k,*co in entries}
 assert all(co==[-v for v in star(d[j,i,k])] for (i,j,k),co in d.items())
 out.append({'m':block['m'],'shape':[264,264],'entries':entries})
(R/'TEN_SYMBOLIC_GENERATORS.json').write_text(json.dumps({'field':data['field'],'entry_convention':'[row,column,channel,c0,c1,c2,c3]; value = a_channel * sum_j c_j zeta10^j, with (a1,a2,a3)=(a,b,c). All coefficients exact integers.','blocks':out,'verification':'Exact coefficient-wise skew-Hermitian check passed for all ten.'},separators=(',',':'))+'\n')
print(json.dumps({'symbolic_generators':len(out),'exact_skew_checks':10,'entries':sum(len(b['entries']) for b in out)}))
