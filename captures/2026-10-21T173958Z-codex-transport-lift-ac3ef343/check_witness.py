from fractions import Fraction as Q
from pathlib import Path
import json
p=Path(__file__).resolve().parent;raw=json.loads((p/'MAP_WITNESSES.json').read_text());w={n:[[Q(x) for x in row] for row in m] for n,m in raw.items()}
def prod(X,Y):
 r=[]
 for i in range(len(X)):
  row=[]
  for j in range(len(Y[0])):
   v=Q(0)
   for k in range(len(Y)):v+=X[i][k]*Y[k][j]
   row.append(v)
  r.append(row)
 return r
def transpose(X):return [[X[i][j] for i in range(len(X))] for j in range(len(X[0]))]
A,D,K,B,G,E,Lsrc=[w[x] for x in ('A','D','K','B','G','E','Fop')]
assert prod(A,D)==prod(D,K)
assert prod(B,D)==[[Q(i==j) for j in range(11)] for i in range(11)]
assert prod(transpose(D),D)==G
assert prod(A,w['Dalt'])==prod(w['Dalt'],K)
assert prod(transpose(w['Dalt']),w['Dalt'])==G and w['Dalt']!=D
AA=prod(A,A);LE=prod([[-x for x in row] for row in AA],E)
assert LE==prod(E,Lsrc)
# Directly check dissipative source T-I and skew target each have the stated symmetry.
assert transpose(A)==[[-x for x in row] for row in A]
assert transpose(w['T'])==w['T']
# Deliberate coordinate corruption must not survive the identities.
bad=[r[:] for r in D];bad[0][0]+=1
assert prod(A,bad)!=prod(bad,K)
badB=[r[:] for r in B];badB[0][0]+=1
assert prod(badB,D)!=[[Q(i==j) for j in range(11)] for i in range(11)]
# Single scale6 matches one branch only; keep native interpolation explicit.
assert LE!=prod(E,[[6*x for x in row] for row in w['H']])
print(json.dumps({'status':'PASS_SCOPED','route':'saved rational matrices; separate product loops','identities':['AD=DK','BD=I','D^T D=G','alternate AD=DK','alternate Gram=G','LE=Ef(H)','A skew','T symmetric'],'negative_controls':['D entry corruption rejected','readout corruption rejected','scalar6 rejected'],'review_status':'same constructor; not non-constructor review','physical_promotion':0},indent=2))
