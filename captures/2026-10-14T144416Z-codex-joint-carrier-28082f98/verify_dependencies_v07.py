"""Fresh constructor checks of the scoped graph and its mathematical boundaries."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,math
R=Path(__file__).parent;D=R/'dist';g=json.loads((D/'assets/dependencies-v0.7.json').read_text())
nodes={n['id']:n for n in g['nodes']};assert len(nodes)==len(g['nodes'])
assert g['physical_promotion']==0 and 'GLOBAL_PROOF_DAG_OPEN' in g['status']
sources={s['id']:s for s in g['sources']}
for s in sources.values():assert hashlib.sha256((D/s['path'].lstrip('/')).read_bytes()).hexdigest()==s['sha256']
for n in nodes.values():
 assert n['citations'] and len(n['dependencies'])==len(set(n['dependencies']))
 for c in n['citations']:
  s=sources[c['source_id']];assert c['snapshot_sha256']==s['sha256']
  assert c['anchor_text'] in (D/s['path'].lstrip('/')).read_text() and c['section']
 assert set(n['dependencies'])=={e['from'] for e in g['edges'] if e['to']==n['id']}
assert len({(e['from'],e['to']) for e in g['edges']})==len(g['edges'])
for e in g['edges']:
 assert e['from'] in nodes and e['to'] in nodes
 assert e['kind'] in ['proof_premise','constitutive_assumption','evaluation_requirement'] and e['reason'] and e['citations']
visiting=set();visited=set()
def walk(id):
 assert id not in visiting,('cycle',id)
 if id in visited:return
 visiting.add(id)
 for p in nodes[id]['dependencies']:walk(p)
 visiting.remove(id);visited.add(id)
for id in nodes:walk(id)
targets={x['target']:x for x in g['target_closure']}
assert set(targets)=={n['id'] for n in nodes.values() if n['status'] in ['EXACT_CONDITIONAL','EXACT_NO_GO']}
for id,t in targets.items():assert t['direct_premises']==nodes[id]['dependencies']
edge_pairs={(e['from'],e['to']) for e in g['edges']}
for x in g['excluded_inferences']:assert (x['from'],x['to']) not in edge_pairs
def descendants(ids):
 reached=set();todo=list(ids)
 while todo:
  id=todo.pop()
  for e in g['edges']:
   if e['from']==id and e['to'] not in reached:
    reached.add(e['to']);todo.append(e['to'])
 return reached-set(ids)
scenario_results=[]
for s in g['scenarios']:
 affected=descendants(s['changes'])
 assert set(s['must_affect'])<=affected,s['id']
 assert not set(s['must_preserve'])&affected,s['id']
 scenario_results.append({'id':s['id'],'affected':sorted(affected),'preserved_checks':s['must_preserve'],'status':'PASS'})
# Independently enumerate the admitted binary domain, including nonsaturated equal-idle cases.
seats=[(t,l,q) for t,l,q in product([0,1],repeat=3) if t*l<=q<=t]
assert len(seats)==5
states=[]
for triples in product(seats,repeat=3):
 t,l,q=zip(*triples);omega=tuple(a*b for a,b in zip(t,l));h=tuple(a-b for a,b in zip(q,omega));states.append((t,l,q,omega,h))
assert len(states)==125
eq=0;saturated_old=0;saturated_equal=0;nonsat_equal=0
for old,new in product(states,repeat=2):
 mu=(3-sum(new[2]))-(3-sum(old[2]));index=sum(old[3])-sum(new[3]);idle=sum(old[4])-sum(new[4])
 assert mu==index+idle
 assert (mu==index)==(sum(old[4])==sum(new[4]))
 eq+=mu==index;nonsat_equal+=(mu==index and sum(old[4])>0)
 if sum(old[4])==0:
  saturated_old+=1;assert mu==index-sum(new[4]);assert (mu==index)==(sum(new[4])==0);saturated_equal+=mu==index
assert (eq,saturated_old,saturated_equal)==(6545,8000,4096) and nonsat_equal>0
# Concrete burden conflict: integrity-only optimum differs from viable/no-idle response.
omega=(1,0,0);W=(2,8,10);shell=[t for t in product([0,1],repeat=3) if sum(t)==2]
cost=lambda t:sum(a*b for a,b in zip(t,W))
assert min(shell,key=cost)==(1,1,0) and cost((0,1,1))==18 and cost((1,1,0))==10
viable=[t for t in shell if all(o<=1-v for o,v in zip(omega,t))];assert viable==[(0,1,1)]
# Signed support witness: sin²(pi/3)-sin²(pi/6)=1/2, times 3/4.
flux=Q(3,4)*(Q(3,4)-Q(1,4));assert flux==Q(3,8) and flux/3==Q(1,8)
# Direct rational scale-gauge checks, including the physical frequency and gravity scaling.
for a,t,b,lam in product([Q(1,2),Q(2),Q(7,3)],repeat=4):
 c=a/t;action=b*a*a/t;aa,tt,bb=lam*a,lam*t,b/lam
 assert aa/tt==c and bb*aa*aa/tt==action
 assert Q(2)/tt==(Q(2)/t)/lam
 assert aa**3/(bb*tt**2)==lam**2*a**3/(b*t**2)
# Native action intensive ratio and local Genesis product; no physical hbar identification.
for a,phi,unit in product([Q(1,3),Q(2),Q(5,2)],repeat=3):assert (unit*a*phi/2)/(a*phi)==unit/2
for omega,delta2 in product([Q(1,3),Q(2),Q(7,2)],repeat=2):
 action_ratio=3*omega/(4*delta2);clock_ratio=2/omega
 assert action_ratio*clock_ratio==3/(2*delta2)
# Same endpoint is compatible with different winding/action. Use real phase only in this witness.
for a in [.25,1,3]:
 assert math.isclose(math.cos(0),math.cos(2*math.pi),abs_tol=1e-14)
 assert math.isclose(math.sin(0),math.sin(2*math.pi),abs_tol=1e-14)
 assert a*2*math.pi/2>0
assert 2/Q(1)!=2/Q(2) # A varying omega cannot share one constant local clock ratio.
receipt={'status':'PASS','edition':'0.7','physical_promotion':0,'nodes':len(nodes),'edges':len(g['edges']),
 'source_snapshots_verified':len(sources),'scoped_target_declarations':len(targets),'acyclic':True,
 'edge_kinds_distinguished':True,'forbidden_edges_absent':True,'ordered_polarity_pairs':len(states)**2,
 'index_equal_pairs':eq,'equal_idle_nonsaturated_examples':nonsat_equal,'saturated_prior_pairs':saturated_old,
 'saturated_prior_index_equal_pairs':saturated_equal,'scenario_results':scenario_results,
 'checks':['source text hashes and locators','explicit target premises','DAG acyclicity','eighteen change audits',
 'full binary response enumeration','selector conflict and flux witness','rational action/clock gauge',
 'intensive native action ratio','conditional Genesis product','same-endpoint winding distinction'],
 'scope':'Constructor verification; imported spectral identities are source premises; no independent proof review or empirical score.',
 'graph_sha256':hashlib.sha256((D/'assets/dependencies-v0.7.json').read_bytes()).hexdigest()}
(D/'sources/UD_DEPENDENCY_VERIFICATION_v0.7.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='scenario_results'}))
