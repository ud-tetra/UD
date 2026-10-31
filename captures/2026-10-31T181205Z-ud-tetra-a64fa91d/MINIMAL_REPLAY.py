#!/usr/bin/env python3
# Independent concise exact K4 matrix and Bianchi/phase response check.
import sympy as s
B1=s.Matrix([[-1,-1,-1,0,0,0],[1,0,0,-1,-1,0],[0,1,0,1,0,-1],[0,0,1,0,1,1]])
B2=s.Matrix([[1,1,0,0],[-1,0,1,0],[0,-1,-1,0],[1,0,0,1],[0,1,0,-1],[0,0,1,1]])
B3=s.Matrix([[-1],[1],[-1],[1]])
assert B1*B2==s.zeros(4,4) and B2*B3==s.zeros(6,1)
K=B2*B2.T
assert K==4*s.eye(6)-B1.T*B1
assert K.eigenvals()=={s.Integer(0):3,s.Integer(4):3}
phi=s.symbols('phi',real=True);alpha=s.Matrix([phi,0,0,0,0,0])
assert B2.T*alpha==s.Matrix([phi,phi,0,0])
assert B3.T*B2.T*alpha==s.zeros(1,1)
assert B2.T*(alpha+B1.T*s.Matrix([3,5,7,11]))==B2.T*alpha
d=s.symbols('delta',nonnegative=True)
M=B2*s.diag(1+d,1+d,1,1)*B2.T
assert M.eigenvals()=={0:3,4:1,4+2*d:1,4+4*d:1}
assert s.limit((s.sqrt(1+(1-s.cos(phi))/2)-1)/phi**2,phi,0)==s.Rational(1,8)
assert s.limit((s.sqrt(2-s.cos(phi))-1)/phi**2,phi,0)==s.Rational(1,4)
h=s.Rational(1,4);prev=B2[:,0];now=B2[:,1]
Kp=M.subs(d,s.Rational(1,12));Kn=M.subs(d,s.Rational(1,6))
nxt=2*now-prev-h*h*Kn*now
E=lambda x,y,k:((y-x).T*(y-x))[0]/(2*h*h)+(x.T*k*y)[0]/2
assert s.simplify(E(now,nxt,Kn)-E(prev,now,Kp)-(prev.T*(Kn-Kp)*now)[0]/2)==0
print('PASS: exact finite spectral response, no physical promotion')
