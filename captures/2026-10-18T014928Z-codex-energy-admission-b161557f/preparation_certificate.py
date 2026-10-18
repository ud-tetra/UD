"""Exact rational sufficient preparation score; enclosures are assumed certified inputs.
No data realizability, acquisition calibration or model admissibility is inferred.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json,argparse

def carrier():
 nodes=[s for k in range(1,5) for s in combinations(range(4),k)]
 edges=[]
 for j,s in enumerate(nodes):
  if len(s)>1:
   for h in range(len(s)):
    i=nodes.index(s[:h]+s[h+1:]);edges.append((i,j,(-1)**h))
 parent={i:nodes.index(tuple(sorted(s+(min(set(range(4))-set(s)),)))) for i,s in enumerate(nodes) if i!=14}
 tree={(i,j) for i,j in parent.items()};phase={14:1+0j};paths={14:[]}
 for i in range(13,-1,-1):
  j=parent[i];e=next(k for k,(a,b,c) in enumerate(edges) if (a,b)==(i,j))
  phase[i]=-1j*edges[e][2]*phase[j];paths[i]=[e]+paths[j]
 cycles=[]
 for k,(i,j,b) in enumerate(edges):
  if (i,j) not in tree:
   z=phase[i].conjugate()*(-1j*b)*phase[j]
   assert z.imag==0 and z.real in [-1,1]
   cycles.append({'edge':k,'i':i,'j':j,'sign':int(z.real),'word_edges':paths[i]+[k]+paths[j]})
 return nodes,edges,parent,phase,paths,cycles

def lower_sqrt(q,digits=80):
 q=F(q)
 if q<0:raise ValueError('negative square root')
 scale=10**digits
 return F(isqrt(q.numerator*scale*scale//q.denominator),scale)

def pair(x,name):
 if not isinstance(x,list) or len(x)!=2:raise ValueError(name+': expected two endpoints')
 lo,hi=map(F,x)
 if lo>hi:raise ValueError(name+': reversed endpoints')
 return lo,hi

def score(record,target_squared,digits=80):
 target_squared=F(target_squared)
 if target_squared<=0:raise ValueError('positive target required')
 r=record['rank']
 if type(r)!=int or r<1:raise ValueError('positive finite integer rank required')
 aL,aU=pair(record['alpha'],'alpha');gL,gU=pair(record['gamma'],'gamma')
 if not (0<aL<=aU<=1 and 0<=gL<=gU<=1):raise ValueError('coherence intervals outside contract or alpha not positive')
 eU=F(record['electric_squared_upper'])
 if eU<0:raise ValueError('negative electric upper bound')
 cycles=carrier()[-1]
 if len(record['cycles'])!=14:raise ValueError('fourteen ordered non-tree cycles required')
 hs=[]
 for c,x in zip(cycles,record['cycles']):
  if x['edge']!=c['edge']:raise ValueError('cycle order/edge mismatch')
  tL,tU=pair(x['real_trace'],'real_trace')
  h=2*r-2*tL
  if c['sign']==-1:
   mL,mU=pair(x['active_moment'],'active_moment')
   h+=4*max(m/a for m in [mL,mU] for a in [aL,aU])
  if h<0:raise ValueError('negative squared-residual upper bound: inconsistent enclosures')
  hs.append(h)
 sL=lower_sqrt(aL,digits);uL=lower_sqrt(gL/aU,digits)
 C=sum(hs,F(0))+2*(1-sL)+2*(1-uL)
 P=eU+F(121,49)*C
 return {'status':'CERTIFIED_SUFFICIENT_PREPARATION' if P<=target_squared else 'NOT_CERTIFIED_BY_THIS_BOUND','score_upper':str(P),'target_squared':str(target_squared),'cycle_residual_squared_upper':[str(x) for x in hs],'matter_chord_squared_upper':str(2*(1-sL)+2*(1-uL)),'scope':'Conditional on certified enclosures, fixed norms, frozen representation and carrier; no model admissibility or physical preparation inferred','physical_promotion':0}

def nominal_record(rank=2,epsilon=F(0)):
 eps=F(epsilon)
 if not 0<=eps<1:raise ValueError('epsilon in [0,1) required')
 out={'rank':rank,'alpha':[str(1-eps),'1'],'gamma':[str(1-eps),'1'],'electric_squared_upper':str(eps),'cycles':[]}
 for c in carrier()[-1]:
  t=rank-2 if c['sign']==-1 else rank
  x={'edge':c['edge'],'real_trace':[str(t-eps),str(t+eps)]}
  if c['sign']==-1:x['active_moment']=['-1',str(-1+eps)]
  out['cycles'].append(x)
 return out

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('record');p.add_argument('--target-squared',required=True);p.add_argument('--digits',type=int,default=80)
 x=p.parse_args()
 if not 1<=x.digits<=10000:raise ValueError('digits outside [1,10000]')
 with open(x.record) as f:r=json.load(f)
 print(json.dumps(score(r,F(x.target_squared),x.digits),indent=2))
