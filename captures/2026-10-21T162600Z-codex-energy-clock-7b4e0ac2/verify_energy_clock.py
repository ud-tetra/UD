"""Exact carrier, map-rescaling, clock and deterministic-bound controls."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,hashlib

H=Path(__file__).resolve().parent;root=H.parents[1]
def tr(a):return [list(x) for x in zip(*a)]
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def scale(k,a):return [[k*x for x in r] for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def rank(a):
 a=[list(map(F,r)) for r in a];i=0
 for j in range(len(a[0]) if a else 0):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i

source=root/'captures/2026-10-21T151000Z-codex-exit03-recovery-98dc7b12/library_LEDGER_v0.85.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec'
by={r['id']:r for r in json.loads(source.read_text())['rows']}
assert by['Q286']['status'].endswith('NOT SUPPORT QUANTIZATION')
# Build the actual filled-tetrahedron chain boundary from oriented simplices.
simp=[s for k in range(1,5) for s in combinations(range(4),k)];idx={s:i for i,s in enumerate(simp)}
d=[[F(0)]*15 for _ in range(15)]
for s in simp:
 if len(s)==1:continue
 for j in range(len(s)):d[idx[s[:j]+s[j+1:]]][idx[s]]=F((-1)**j)
Z=[[F(0)]*15 for _ in range(15)];assert mul(d,d)==Z
A=add(d,scale(-1,tr(d)));A2=mul(A,A);P=scale(F(-1,4),A2)
assert add(A,tr(A))==Z and mul(P,P)==P and rank(P)==14
assert mul(A,A2)==scale(-4,A)
J=scale(F(1,2),A);assert mul(J,J)==scale(-1,P)
assert sum(P[i][i] for i in range(15))==14
# Exact physical two-plane map fixture; no actual apparatus values.
AA=[[F(0),F(-2)],[F(2),F(0)]];M=[[F(2),F(0)],[F(0),F(7)]]
Mi=[[F(1,2),F(0)],[F(0),F(1,7)]];tau=F(3);A0=F(5)
G=[[F(5,6),F(0)],[F(0),F(10,147)]];K=scale(1/tau,mul(mul(M,AA),Mi))
assert mul(K,M)==scale(1/tau,mul(M,AA))
assert mul(mul(tr(M),G),M)==scale(2*A0/tau,eye(2))
assert add(mul(tr(K),G),mul(G,K))==[[0,0],[0,0]]
C=mul(mul(Mi,K),M);B=mul(mul(tr(M),G),M);gamma=F(1,3);lam=F(10,3)
assert mul(Mi,M)==eye(2) and mul(K,M)==mul(M,C)
assert C==scale(gamma,AA) and B==scale(lam,eye(2))
assert lam/(2*gamma)==A0 and 1/gamma==tau
x=[[F(2)],[F(3)]];a=mul(tr(x),x)[0][0];z=mul(M,x);E=mul(mul(tr(z),G),z)[0][0]/2
assert a==13 and E==F(65,3) and E*tau==A0*a
rescales=[F(1,10),F(1,2),F(3,2),F(2),F(10)]
for c in rescales:
 xn=scale(c,x);Mn=scale(1/c,M);an=c*c*a;An=A0/(c*c)
 assert mul(Mn,xn)==z
 assert mul(K,Mn)==scale(1/tau,mul(Mn,AA))
 assert mul(mul(tr(Mn),G),Mn)==scale(2*An/tau,eye(2))
 assert An*an==A0*a and An*an/tau==E
# Rank obstruction from the previously hidden norm parameter.
W=[[1,-1,1],[0,1,0]];target=[1,0,0];v=[-1,0,1]
assert rank(W)==2 and rank(W+[target])==3
assert all(sum(a*b for a,b in zip(r,v))==0 for r in W)
assert sum(a*b for a,b in zip(target,v))==-1
assert rank(W+[[0,0,1]])==3
# Exact quarter-cycle points: signed readout changes sign at half state cycle;
# quadratic readout repeats there, is nonconstant at quarter state cycle.
orbit=[[1,0],[0,1],[-1,0],[0,-1],[1,0]]
assert orbit[2]!=orbit[0] and orbit[4]==orbit[0]
assert orbit[0][0]**2==orbit[2][0]**2!=orbit[1][0]**2
# Pi-free interval coefficients; final action interval divides these by pi.
EL,EU=F(99,10),F(101,10);TL,TU=F(199,100),F(201,100)
rL,rU=F(1),F(1);aL,aU=F(9,10),F(11,10)
low=EL*TL/(rU*aU);high=EU*TU/(rL*aL)
for e in [EL,EU]:
 for t in [TL,TU]:
  for aa in [aL,aU]:assert low<=e*t/aa<=high
norm=F(1);delta=F(1,10);assert (norm-delta)**2==F(81,100) and (norm+delta)**2==F(121,100)
out={'status':'PASS_SCOPED','carrier_dimension':15,'active_rank':14,'chain_squared_zero':True,'A_cubed_equals_minus_4A':True,
 'exact_rescalings_checked':len(rescales),'physical_fixture':'Synthetic rational two-plane calibration; no hardware evidence',
 'observably_identified':'A0*a = E*T_state/pi','A0_identified_without_support_anchor':False,
 'matrix_calibration_rule':'For independently calibrated absolute M, LM=I, KM=M(LKM), LKM=gamma*A and M^TGM=lambda*I imply tau0=1/gamma, A0=lambda/(2*gamma).',
 'period_control':'Signed orbit period pi; nonconstant quadratic period pi/2; constant energy supplies no period',
 'interval_coefficients_before_division_by_pi':[str(low),str(high)],
 'source_Q286_preserved':'Normalized representative is not support quantization',
 'EXIT03':'HOLD','QPB1':'QUARANTINED','independent_review':'PENDING','physical_promotion':0}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
