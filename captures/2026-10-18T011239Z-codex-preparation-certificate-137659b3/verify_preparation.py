"""Constructor replay of exact finite topology and rational sufficient bounds.
Analytic geodesic estimates and all-time invariance are proved in the manuscript,
not certified by finite numerical examples.
"""
from preparation_certificate import *
from endpoint_robustness_budget import budget
from collections import Counter
from pathlib import Path
import hashlib,copy
P=Path(__file__).resolve().parent
checks={}
def check(name,condition):
 checks[name]=bool(condition)
 if not condition:raise AssertionError(name)
nodes,edges,parent,phase,paths,cycles=carrier()
check('carrier_counts',(len(nodes),len(edges),len(cycles),len(parent))==(15,28,14,14))
check('rooted_tree_depth',max(map(len,paths.values()))==3 and all(i<j for i,j in parent.items()))
check('cycle_sign_counts',Counter(c['sign'] for c in cycles)=={-1:10,1:4})
check('tree_nominal_identity',all(phase[i].conjugate()*(-1j*b)*phase[j]==1 for i,j,b in edges if parent.get(i)==j))
check('word_length_bound',all(len(c['word_edges'])<=7 for c in cycles))
check('word_multiplicity_square_bound',all(sum(v*v for v in Counter(c['word_edges']).values())<=14 for c in cycles))
# Integer diamond cycle: i<-j<-k minus i<-h<-k; R z=0 exactly.
diamonds=[]
for k,s in enumerate(nodes):
 for i,t in enumerate(nodes):
  if len(s)==len(t)+2 and set(t)<set(s):
   mid=[j for j,u in enumerate(nodes) if len(u)==len(t)+1 and set(t)<set(u)<set(s)]
   j,h=mid
   z=[0]*28
   for a,b,sg in [(i,j,1),(j,k,1),(i,h,-1),(h,k,-1)]:
    z[next(n for n,(u,v,w) in enumerate(edges) if (u,v)==(a,b))]=sg
   divergence=[sum(z[e]*((i==n)-(j==n)) for e,(i,j,b) in enumerate(edges)) for n in range(15)]
   check('diamond_divergence_'+str(len(diamonds)),divergence==[0]*15 and sum(v*v for v in z)==4)
   diamonds.append(z)
check('diamond_count',len(diamonds)==18)
check('local_matter_frame_bound',1+3==4)
check('local_projector_bound',2*4*4<=6*6)
check('local_cycle_bound',4+12==16)
check('local_chord_constant',14*16**2+2*6**2==3656)
check('local_score_constant',1+F(121,49)*3656==F(442425,49)<10000)
check('uniform_interval_constant',10*6+4*2+4==72 and 1+F(121,49)*72==F(8761,49)<179<180)
# Long division of x^4(1-x)^4 by 1+x^2: remainder -4, no x term.
p=[F(0)]*9
for k,c in enumerate([1,-4,6,-4,1]):p[k+4]=F(c)
q=[F(0)]*7
for k in range(8,1,-1):
 q[k-2]=p[k];p[k]-=q[k-2];p[k-2]-=q[k-2]
check('pi_integral_remainder',p==[F(-4)]+[F(0)]*8)
check('pi_integral_polynomial',sum(c/F(k+1) for k,c in enumerate(q))==F(22,7))
for n,d in [(0,1),(1,1),(2,3),(1,10**100),(129,13)]:
 a=F(n,d);v=lower_sqrt(a);check('inward_sqrt_'+str(n)+'_'+str(d),v*v<=a<(v+F(1,10**80))**2)
b=budget();delta2=F(b['exact']['delta_eta_squared']);eta=F(b['exact']['eta'])
fixtures={}
for label,record,expected in [('ideal',nominal_record(),True),('bounded_intervals',nominal_record(epsilon=delta2/1000),True),('wide_intervals',nominal_record(epsilon=delta2),False),('hidden_electric',dict(nominal_record(),electric_squared_upper='4'),False)]:
 result=score(record,delta2)
 check('fixture_'+label,(result['status']=='CERTIFIED_SUFFICIENT_PREPARATION')==expected)
 fixtures[label]={'input':record,'result':result}
bad=nominal_record();bad['alpha']=['0','1']
try:score(bad,delta2);zero_rejected=False
except ValueError:zero_rejected=True
check('zero_coherence_rejected',zero_rejected)
bad=nominal_record();bad['cycles'][0]['real_trace']=['100','100']
try:score(bad,delta2);bad_rejected=False
except ValueError:bad_rejected=True
check('inconsistent_residual_rejected',bad_rejected)
check('uniform_precision_budget',F(8761,49)*delta2/180<delta2)
check('endpoint_delta_inside_local_region',delta2<F(1,64))
files=['parity_budget.py','endpoint_robustness_budget.py','FROZEN_ENDPOINT_ROBUSTNESS_CERTIFICATE_v0.1.json']
out={'status':'PASS','exact_check_count':len(checks),'checks':checks,'topology':{'nodes':[list(n) for n in nodes],'edges':edges,'root':14,'parent':parent,'phase':{str(k):[int(v.real),int(v.imag)] for k,v in phase.items()},'non_tree_cycles':cycles,'diamond_cycle_witness':diamonds[0]},'unit_endpoint_budget':b,'uniform_sufficient_epsilon':str(delta2/180),'conditioning_constant':'442425/49','fixtures':fixtures,'dependencies':{f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in files},'verification_scope':'Exact integer topology, rational arithmetic and hostile interval controls; constructor analytic theorem remains review-pending','physical_promotion':0}
(P/'PREPARATION_CERTIFICATE_v0.1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'delta_squared_decimal':float(delta2),'uniform_epsilon_decimal':float(delta2/180)},indent=2))
