#!/usr/bin/env python3
# Minimal exact checked subcase. Full scripts are in LOCAL ZIP only.
import sympy as S
b1=S.Matrix([[-1,-1,-1,0,0,0],[1,0,0,-1,-1,0],[0,1,0,1,0,-1],[0,0,1,0,1,1]])
b2=S.Matrix([[1,1,0,0],[-1,0,1,0],[0,-1,-1,0],[1,0,0,1],[0,1,0,-1],[0,0,1,1]])
b3=S.Matrix([1,-1,1,-1])
assert b1*b2==S.zeros(4,4) and b2*b3==S.zeros(6,1)
p=S.symbols('p',real=True)
alpha=S.Matrix([p,0,0,0,0,0])
F=b2.T*alpha
assert F==S.Matrix([p,p,0,0]) and b3.T*F==S.zeros(1,1)
H=b2*S.diag(S.cos(p),S.cos(p),1,1)*b2.T
x=S.Symbol('x')
target=x**3*(x-4)*(x-2-2*S.cos(p))*(x-4*S.cos(p))
assert S.simplify(H.charpoly(x).as_expr()-target)==0
gradient=b2*S.Matrix([S.sin(v) for v in F])
assert gradient==S.sin(p)*S.Matrix([2,-1,-1,1,1,0])
assert b1*gradient==S.zeros(4,1)
for u,z in [(S.pi/3,{0:3,2:1,3:1,4:1}),(S.pi/2,{0:4,2:1,4:1}),(2*S.pi/3,{0:3,-2:1,1:1,4:1})]:
    assert H.subs(p,u).eigenvals()=={S.Integer(k):v for k,v in z.items()}
w=S.Symbol('w')
K=b2*S.diag(w,w,1,1)*b2.T
assert S.simplify(K.charpoly(x).as_expr()-x**3*(x-4)*(x-2-2*w)*(x-4*w))==0
assert S.simplify((4*w-4)/(2+2*w-4))==2
print('PASS: K4 Wilson face response conditional and Bianchi/no-source constraints; promotion 0')
