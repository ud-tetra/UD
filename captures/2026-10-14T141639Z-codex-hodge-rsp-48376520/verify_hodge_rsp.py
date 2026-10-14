"""Exact source-carrier checks and proof-bound parallel evidence, not an experiment."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib,json
from hodge_rsp import k4_generator,transpose,multiply,apply,norm2,quarter_turn_witness,hd_pair_receipt
from rsp1 import State,transition,potential
R=Path(__file__).parent;P=R/'dist/sources/hodge-rsp-v0.1'
A,B=k4_generator();assert all(A[i][j]==-A[j][i] for i in range(15) for j in range(15))
for i in range(2):assert all(v==0 for row in multiply(B[i],B[i+1]) for v in row)
A2=multiply(A,A)
for i in range(15):
 for j in range(15):
  harmonic=Q(1,4) if i<4 and j<4 else Q(0)
  assert A2[i][j]==-4*(int(i==j)-harmonic)
# Four quarter turns act as identity on the whole declared chain, not only the witness plane.
U=[[((Q(1,4) if i<4 and j<4 else Q(0))+A[i][j]/2) for j in range(15)] for i in range(15)]
assert multiply(transpose(U),U)==[[Q(int(i==j)) for j in range(15)] for i in range(15)]
U2=multiply(U,U);assert multiply(U2,U2)==[[Q(int(i==j)) for j in range(15)] for i in range(15)]
w=quarter_turn_witness();assert all([r['intertwines'] for r in rows]==[True,True,True,False] for rows in w['branches'].values())
for x in w['native_states']:
 assert norm2(tuple(Q(a) for a in x['coordinates']))==2
 assert x['L_HD']==[0,0,0] and x['R_HD']==['0','0','0']
# The prepared lookup's first cached latent bit is not the original instantaneous HD witness.
assert w['branches']['C'][1]['decoded_state']['L']==(1,0,0)
assert w['native_states'][1]['L_HD']==[0,0,0]
# A fixed finite preparation defines an invariant bounded register family.
graphs={}
for branch in ['C','H']:
 states=[State((1,1,1),L,q,r,branch=branch) for L,q,r in product(list(product((0,1),repeat=3)),repeat=3) if all(l<=v for l,v in zip(L,q))]
 assert len(states)==216
 index={s:i for i,s in enumerate(states)};successor=[index[transition(s)['state']] for s in states]
 cycles=set();settling=0
 for i,s in enumerate(states):
  path=[];j=i
  while j not in path:path.append(j);j=successor[j]
  cycle=path[path.index(j):];assert len(cycle)==1;cycles.add(j);settling=max(settling,len(path)-1)
  assert successor[i]==i or potential(states[successor[i]])<potential(s)
 graphs[branch]={'states':len(states),'fixed_states':len(cycles),'maximum_settling_updates':settling,'nonfixed_cycles':0}
assert graphs['C']['fixed_states']==1 and graphs['H']['fixed_states']==27
# The unbounded target countermodel proves why the finite-image/uniform qualifier matters.
for n in range(-1000,1001):assert max(-(n+1),0)==max(max(-n,0)-1,0)
parallel=json.loads((P/'HODGE_RSP_PARALLEL_VERIFICATION_v0.1.json').read_text())
assert parallel['status']=='PASS'
for f,h in parallel['input_hashes'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
assert parallel['checker_sha256']==hashlib.sha256((P/'hodge-rsp-parallel-check.py').read_bytes()).hexdigest()
review=(P/'HODGE_RSP_SOURCE_SCOPE_REVIEW_v0.1.md').read_text();assert 'finite' in review.lower() and 'surject' in review.lower() and 'Physical promotion' in review
receipt={'status':'PASS','physical_promotion':0,'chain_dimensions':[4,6,4,1],'exact_arithmetic':'Python Fraction; no floating-point trig in K4 witness',
 'exact_checks':['boundary composition','skewness','A²=−4(I−P_H0)','quarter-turn orthogonality','U^4=I','Av=2u and Au=−2v','norm2=2 on orbit','C/H three matching window edges and wrap mismatch','original HD latent witness zero at all quarter samples; lookup is separately prepared'],
 'root_prepared_graphs':graphs,'unbounded_scope_counterexample_checked_integers':2001,
 'parallel_generic_factor_candidates':parallel['generic_finite_factor_checks']['surjective_permutation_decoder_tests'],
 'parallel_exact_factors_all_fixed':parallel['generic_finite_factor_checks']['exact_factors_all_fixed'],
 'parallel_receipt_sha256':hashlib.sha256((P/'HODGE_RSP_PARALLEL_VERIFICATION_v0.1.json').read_bytes()).hexdigest(),
 'source_scope_review_sha256':hashlib.sha256((P/'HODGE_RSP_SOURCE_SCOPE_REVIEW_v0.1.md').read_bytes()).hexdigest(),
 'theorem_sha256':hashlib.sha256((P/'UD_HODGE_RSP_REALIZATION_OBSTRUCTION_v0.1.md').read_bytes()).hexdigest(),
 'witness_sha256':hashlib.sha256((P/'HODGE_RSP_QUARTER_TURN_WITNESS_v0.1.json').read_bytes()).hexdigest(),
 'scope':'Proofs plus bounded constructor-team AI checks. Generic finite enumeration supports the formal theorem, not every possible native decoder; no physical score or independent human review.'}
(P/'HODGE_RSP_ROOT_VERIFICATION_v0.1.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
