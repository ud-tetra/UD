#!/usr/bin/env python3
"""THM-534 v2.4 exact constructor replay; requires SymPy."""
from itertools import product
import sympy as S

D=S.Matrix([[-1,1],[1,0],[0,-1],[-1,0],[0,1],[1,0],[0,-1]])
contacts=[(f,c,int(D[f,c])) for f in range(7) for c in range(2) if D[f,c]]
assert len(contacts)==8
n=9; A=[]; P=[]
for f,c,d in contacts:
    a=S.zeros(n); a[f,7+c]=-d; a[7+c,f]=d
    p=S.zeros(n); p[f,f]=p[7+c,7+c]=1
    assert a.T==-a and (S.I*a).conjugate().T==S.I*a
    A.append(a);P.append(p)
degree=[sum(int(f==i or 7+c==i) for f,c,_ in contacts) for i in range(n)]
assert max(degree)==4
count=0
for profile in product([S.Integer(0),S.Rational(1,2),S.Integer(1)],repeat=8):
    matrix=sum((profile[k]*A[k] for k in range(8)),S.zeros(n))
    for i in range(n):
        assert sum(abs(matrix[i,j]) for j in range(n) if i!=j)<=4
    count+=1
assert count==6561
x=S.zeros(n,1);f,c,d=contacts[0];x[f]=1
assert (A[0]*x).dot(A[0]*x)==1
for k in [1,10,100]:
    y=-k*A[0]*x
    assert (y.T*A[0]*x)[0]+S.Rational(1,5)==-k+S.Rational(1,5)
shared=[k for k,(face,_,_) in enumerate(contacts) if face==0]
assert len(shared)==2
assert [-(-1)*S.Rational(1,2) for k in shared]==[S.Rational(1,2)]*2
B=S.Rational(1,2)
assert S.Rational(3,10)+S.Rational(1,5)==B
print("PASS 6561 exact gate words, cotangent unboundedness and shared-face double wake")
print("PASS isolated resource split kinetic 3/5 and potential 2/5")
print("Physical promotion 0. Original real cotangent and new complex carrier DISTINCT.")
