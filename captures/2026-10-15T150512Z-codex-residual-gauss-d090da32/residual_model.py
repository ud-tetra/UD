"""Residual U(s) moment map on the frozen curved-branch symplectic slice.

Canonical one-form: 2 Re sum e^dagger dX + sum tr(Pi dA).
The functions accept either SymPy matrices (exact) or NumPy arrays (diagnostic).
"""
import sympy as sp

def comm(a,b): return a*b-b*a

def moment_raw(X,E,A=(),Pi=()):
    return sp.I*(X*E.H-E*X.H)+sum((sp.I*comm(a,p) for a,p in zip(A,Pi)),sp.zeros(X.rows))

def moment_modes(plus,minus,vacuum=()):
    return plus*plus.H-minus*minus.H+sum((comm(z,z.H) for z in vacuum),sp.zeros(plus.rows))

def hermitian_basis(s):
    out=[]
    for i in range(s):
        z=sp.zeros(s);z[i,i]=1;out.append(z)
    for i in range(s):
        for j in range(i+1,s):
            z=sp.zeros(s);z[i,j]=z[j,i]=1;out.append(z)
            z=sp.zeros(s);z[i,j]=sp.I;z[j,i]=-sp.I;out.append(z)
    return out

def hermitian_vector(z):
    s=z.rows
    return sp.Matrix([sp.re(z[i,i]) for i in range(s)]+[v for i in range(s) for j in range(i+1,s) for v in (sp.re(z[i,j]),sp.im(z[i,j]))])

def shift_completion(eigenvalues):
    """Descending real trace-zero eigenvalues of the desired vacuum charge.

    Return a weighted shift whose self-commutator is diag(eigenvalues).
    Ordering/positivity of partial sums is a caller/theorem precondition.
    """
    s=len(eigenvalues);z=sp.zeros(s);partial=sp.Integer(0)
    for i in range(s-1):
        partial+=eigenvalues[i];z[i,i+1]=sp.sqrt(partial)
    return z

def dimensions(s):
    return {'rank':s+1,'slice_real':84+112*s+28*s*s,
            'free_reduced_real':84+112*s+26*s*s,
            'maximal_stabilizer_real':112 if s else 84}

def principal_witness(s):
    plus=sp.zeros(s,1);plus[0]=1;minus=plus.copy()
    z1=sp.diag(*range(1,s+1));z2=sp.zeros(s)
    for i in range(s-1):z2[i,i+1]=z2[i+1,i]=1
    return plus,minus,[z1,z2]
