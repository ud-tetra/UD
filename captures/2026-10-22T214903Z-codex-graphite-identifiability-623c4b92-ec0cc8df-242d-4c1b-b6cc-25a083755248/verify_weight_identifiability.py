"""Exact inverse and collision audit of the seven-orbit graphite source."""
from pathlib import Path
from fractions import Fraction as F
import contextlib
import io
import json
import runpy

base=Path(__file__).resolve().parents[2]
source=base/'captures/2026-10-22T214428Z-codex-graphite-harmonic-source-49d5bb28-64263b7c-7b88-4f45-a8a9-e0cb34f52956/verify_harmonic_source.py'
with contextlib.redirect_stdout(io.StringIO()):
    d=runpy.run_path(str(source))
Q=d['Q']; Ks=d['Ks']; rank=d['rank']; mm=d['mm']; trans=d['trans']
Ginv=[[F(4,3),F(-2,3)],[F(-2,3),F(4,3)]]
assert rank(Q)==6 and rank(Q+[[F(1)]*7])==7

def qform(w):
    return sum(w[i]*Q[i][j]*w[j] for i in range(7) for j in range(7))

def gram_readout(i, w):
    K=[[sum(w[j]*Ks[j][a][v] for j in range(7)) for v in range(14)]
       for a in range(2)]
    H=mm(Ks[i],trans(K))
    return sum(Ginv[a][b]*H[b][a] for a in range(2) for b in range(2))/2

for w in [list(map(F,[0,1,0,0,0,0,0])),
          list(map(F,[2,-3,0,5,1,4,-1])),
          [F(1,7),F(2,3),F(-4,5),F(3,2),F(0),F(-1),F(7,4)]]:
    assert [gram_readout(i,w) for i in range(7)] == [
        sum(Q[i][j]*w[j] for j in range(7)) for i in range(7)]
    assert qform([x+F(9,13) for x in w])==qform(w)

u=[F(0),F(1),F(0),F(0),F(0),F(0),F(0)]
v=[F(0),F(0),F(1),F(0),F(0),F(0),F(0)]
assert sum(u)==sum(v)==1
assert sum(x*x for x in u)==sum(x*x for x in v)==1
assert qform(u)==qform(v)==1
# Automorphisms preserve whether a vertex is incident to a double edge.
assert any(-4*Q[1][j]==2 for j in range(7) if j!=1)
assert all(-4*Q[2][j]!=2 for j in range(7) if j!=2)
contrast=[u[i]-v[i] for i in range(7)]
assert qform(contrast)==F(5,2)
# At nonuniform w, derivative 2Qw is nonzero; uniform is stationary.
assert any(sum(Q[i][j]*contrast[j] for j in range(7)) for i in range(7))
assert all(sum(Q[i][j] for j in range(7))==0 for i in range(7))
print(json.dumps({'status':'EXACT_CONDITIONAL_CONSTRUCTOR_CHECK',
                  'observable_rank_for_nonuniform_w':1,
                  'source_contrast_rank':6,
                  'equal_alpha_inequivalent_sources':['e1','e2'],
                  'alpha_each':'1','alpha_e1_minus_e2':'5/2',
                  'inverse_gram':'b=Qw, unique with sum(w)=0 if coupling calibrated',
                  'full_frequency':'depends on w only through alpha under degenerate isotropic bath'},indent=2))
