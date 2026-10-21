"""Exact action-unit and monomial-anchor checks; standard-library rational arithmetic."""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SOURCE=ROOT/'captures/2026-10-21T151000Z-codex-exit03-recovery-98dc7b12/library_LEDGER_v0.85.json'
ZERO=(F(0),)*3

def rref(rows):
 a=[list(map(F,r)) for r in rows];piv=[];i=0
 for j in range(3):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
  piv.append(j);i+=1
  if i==len(a):break
 return a,piv

def rank(rows):return len(rref(rows)[1])
def nullspace(rows):
 a,piv=rref(rows);basis=[]
 for j in set(range(3))-set(piv):
  v=[F(0)]*3;v[j]=F(1)
  for i,k in enumerate(piv):v[k]=-a[i][j]
  basis.append(v)
 return basis
def dot(a,b):return sum(x*y for x,y in zip(a,b))

def dim(e,units):
 if isinstance(e,(int,float)):return ZERO
 if isinstance(e,str):return tuple(map(F,units[e]))
 op,*args=e
 if op in ['mul','div']:
  a,b=(dim(v,units) for v in args);s=1 if op=='mul' else -1
  return tuple(x+s*y for x,y in zip(a,b))
 if op=='pow':return tuple(F(args[1])*x for x in dim(args[0],units))
 if op=='add':
  a,b=(dim(v,units) for v in args)
  if a!=b:raise ValueError('inhomogeneous addition')
  return a
 if op in ['sin','exp','log']:
  if dim(args[0],units)!=ZERO:raise ValueError('dimensional transcendental argument')
  return ZERO
 raise ValueError('unsupported operator')

def main():
 raw=SOURCE.read_bytes();assert hashlib.sha256(raw).hexdigest()=='8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec'
 rows=json.loads(raw)['rows'];by={r['id']:r for r in rows}
 units={'B0':[1,0,0],'a0':[0,1,0],'tau0':[0,0,1],'A0':[1,2,-1],'hbar':[1,2,-1],
 'eta':[0,0,0],'xi_np':[0,0,0],'xi_pn':[0,0,0],'a':[0,0,0],'phi':[0,0,0],
 'n':[0,0,0],'pi':[0,0,0],'I':[0,0,0],'S':[1,2,-1],'alpha':[1,2,-1],
 'H':[0,0,0],'E':[1,2,-2],'omega':[0,0,-1],'G':[ -1,3,-2],'gammaG':[0,0,0]}
 eqs=[('O09','I',['mul',['mul',0.5,'a'],'phi']),('O09','I',['mul',['mul','pi','n'],'a']),
 ('O10','A0',['div',['mul','B0',['pow','a0',2]],'tau0']),('O11','S',['mul','pi','A0']),
 ('O12','xi_pn',['div','hbar','A0']),('O13','xi_np',['div','A0','hbar']),
 ('O13','xi_np',['div',1,'xi_pn']),('O13','A0',['mul','xi_np','hbar']),
 ('O14','eta',['div','A0','hbar']),('O15','G',['div',['mul','gammaG',['pow','a0',3]],['mul','B0',['pow','tau0',2]]]),
 ('Q282','alpha',['div','S',['mul','a','phi']]),('Q282','alpha',['div','A0',2]),
 ('Q283','H','a'),('Q284','omega',['div',2,'tau0']),('Q285',['div','E',['mul','a','omega']],['div','A0',2]),
 ('Q286','S',['mul','pi','A0']),('Q287','hbar',['div','A0',2]),('Q288','eta',2)]
 typed=[]
 for row,lhs,rhs in eqs:
  assert dim(lhs,units)==dim(rhs,units)
  typed.append({'source_row':row,'lhs':lhs,'rhs':rhs,'dimension':list(map(str,dim(lhs,units))),
   'bridge_status':'CANDIDATE_ONLY' if row in ['Q287','Q288'] else 'DECLARED_CONDITIONAL_SCOPE',
   'physical_identity_established':False})
 # Known source error must fail; a different dimension-compatible reciprocal is not algebraically sufficient.
 assert dim('A0',units)!=dim(['div',1,'xi_pn'],units)
 rejections=['O13 literal final equality']
 for expr in [['add','E','S'],['sin','A0']]:
  try:dim(expr,units)
  except ValueError:rejections.append(expr[0])
  else:raise AssertionError('negative control accepted')
 wrong=dict(units);wrong['B0']=[1,2,-2]
 assert dim('A0',wrong)!=dim(eqs[2][2],wrong);rejections.append('energy-typed B0 branch')
 for A,h in [(F(3,7),F(5,11)),(F(7),F(2))]:
  eta=A/h;assert eta*h==A and (h/A)*eta==1
 assert F(1,2)*2==1
 # Every tested rational anchor bank satisfies the row-space / kernel equivalence.
 target=(F(1),F(2),F(-1));vectors=[v for v in product([-1,0,1],repeat=3) if any(v)];checks=0
 for size in range(4):
  for W in combinations(vectors,size):
   identified=rank(W)==rank([*W,target]);basis=nullspace(W)
   assert all(all(dot(r,v)==0 for r in W) for v in basis)
   assert identified==all(dot(target,v)==0 for v in basis)
   if not identified:
    witness=next(v for v in basis if dot(target,v)!=0)
    assert all(dot(r,witness)==0 for r in W) and dot(target,witness)!=0
   checks+=1
 banks={'none':[], 'length_time':[(0,1,0),(0,0,1)],'energy_time':[(1,2,-2),(0,0,1)],
 'direct_action':[(1,2,-1)],'mass_length_time':[(1,0,0),(0,1,0),(0,0,1)],
 'length_frequency':[(0,1,0),(0,0,-1)]}
 examples={}
 for name,W in banks.items():
  yes=rank(W)==rank([*W,target]);examples[name]={'W':W,'action_identified':yes,'rank':rank(W),
   'ambiguity_witness':None if yes else [str(x) for x in next(v for v in nullspace(W) if dot(target,v)!=0)]}
 assert examples['energy_time']['action_identified']
 assert not examples['length_time']['action_identified']
 for name,c in [('energy_time',[1,1]),('direct_action',[1]),('mass_length_time',[1,2,-1])]:
  W=banks[name]
  assert tuple(sum(F(c[i])*W[i][j] for i in range(len(W))) for j in range(3))==target
  examples[name]['row_span_certificate_c']=c
 assert F(1,1000)+F(1,2000)==F(3,2000)
 selected=['G06',*[f'O{i:02}' for i in range(9,16)],*[f'Q{i}' for i in range(282,289)],'O54','O55']
 bindings=[{'id':i,'source_row_sha256':hashlib.sha256(json.dumps(by[i],sort_keys=True,separators=(',',':')).encode()).hexdigest(),'source_claim_bin':by[i]['claim_bin']} for i in selected]
 contract={'version':'0.1','scope':'Action subsystem only; manual source-to-AST transcription, not automatic prose parsing. O13 uses explicit correction proposal.',
 'dimension_basis':['M','L','T'],'unit_declarations':units,'declaration_limit':'a0 length, tau0 time, support and phase dimensionless are explicit hypotheses; O15 supplies B0 mass type. Energy, action and clock physical correspondences remain gated.',
 'source_bindings':bindings,'typed_equalities':typed,'full_ledger_objects':len(rows),'subsystem_source_rows':len(selected),'remaining_outside_this_contract':len(rows)-len(selected),'physical_promotion':0}
 (HERE/'ACTION_UNIT_CONTRACT.json').write_text(json.dumps(contract,indent=2)+'\n')
 result={'status':'PASS_SCOPED','typed_equalities_passed':len(typed),'source_rows_bound':len(selected),'negative_controls_rejected':rejections,'anchor_banks_checked':checks,'examples':examples,'O13_original':'REJECTED_LITERAL_DIMENSIONAL_CHAIN','O13_overlay':'DIMENSIONALLY_VALID; source amendment not approved','QPB1':'DIMENSIONALLY_VALID_CANDIDATE_ONLY','EXIT03':'HOLD; specification and global typing unresolved','physical_promotion':0}
 (HERE/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='examples'}))

if __name__=='__main__':main()
