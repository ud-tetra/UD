#!/usr/bin/env python3
"""Exact checks for scoped source corrections. Never execute imported code."""
import argparse
import ast
import hashlib
import itertools
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def z(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]

def eye(n):
    a = z(n, n)
    for i in range(n): a[i][i] = F(1)
    return a

def tr(a): return [list(c) for c in zip(*a)]
def add(a, b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a, c): return [[F(c)*x for x in r] for r in a]
def sub(a, b): return add(a, scale(b, -1))
def mul(a, b):
    assert len(a[0]) == len(b), 'matrix dimension mismatch'
    bt = tr(b)
    return [[sum((x*y for x,y in zip(r,c)), F(0)) for c in bt] for r in a]
def trace(a): return sum((a[i][i] for i in range(len(a))), F(0))
def iszero(a): return all(x == 0 for r in a for x in r)

def rank(a):
    a = [[F(x) for x in r] for r in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None: continue
        a[row], a[pivot] = a[pivot], a[row]
        q = a[row][col]; a[row] = [x/q for x in a[row]]
        for i in range(len(a)):
            if i != row:
                q = a[i][col]
                a[i] = [x-q*y for x,y in zip(a[i],a[row])]
        row += 1
        if row == len(a): break
    return row

def complex_from_cells(cells):
    basis = [sorted({s for cell in cells for s in itertools.combinations(cell,k+1)})
             for k in range(4)]
    bs = []
    for k in range(1,4):
        b = z(len(basis[k-1]), len(basis[k])); idx = {s:i for i,s in enumerate(basis[k-1])}
        for j,s in enumerate(basis[k]):
            for i in range(k+1): b[idx[s[:i]+s[i+1:]]][j] = F((-1)**i)
        bs.append(b)
    assert iszero(mul(bs[0],bs[1])) and iszero(mul(bs[1],bs[2]))
    sizes = list(map(len,basis)); n = sum(sizes); offsets = [0]
    for size in sizes: offsets.append(offsets[-1]+size)
    a = z(n,n)
    for k,b in enumerate(bs):
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[offsets[k]+i][offsets[k+1]+j] = -b[i][j]
                a[offsets[k+1]+j][offsets[k]+i] = b[i][j]
    l1 = add(mul(tr(bs[0]),bs[0]),mul(bs[1],tr(bs[1])))
    return basis, bs, a, l1

def spectral_check(l, values):
    n = len(l); product = eye(n)
    for value in values: product = mul(product,sub(l,scale(eye(n),value)))
    assert iszero(product)
    multiplicities = {str(value): n-rank(sub(l,scale(eye(n),value))) for value in values}
    assert sum(multiplicities.values()) == n
    return multiplicities

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x

def run(source):
    source_bytes = source.read_bytes(); text = source_bytes.decode('utf-8')
    match = re.search(r'H_base = np\.array\((\[.*?\])\)',text,re.S)
    assert match, 'printed matrix missing'
    literal = ast.literal_eval(match.group(1))  # data only; no imported script execution
    printed = [[F(str(x)) for x in r] for r in literal]
    assert len(printed)==10 and all(len(r)==10 for r in printed)
    assert printed == tr(printed)
    native = {}
    specs = {}
    for name,cells,values in [
        ('Delta3',[(0,1,2,3)],[4]),
        ('K_minus',[(0,1,2,3),(0,1,2,4)],[3,5]),
        ('K_plus',[(0,1,2,3),(0,1,2,4),(0,1,3,4)],[2,5])]:
        basis,bs,a,l1 = complex_from_cells(cells)
        assert iszero(add(a,tr(a)))
        specs[name] = spectral_check(l1,values)
        native[name] = {'cells':cells,'simplex_basis':basis,'boundaries':bs,'A':a,'L1':l1}
    frozen = json.loads((ROOT/'sources/NATIVE_DELTA3_OPERATORS.json').read_text())
    assert native['Delta3']['A'] == [[F(x) for x in r] for r in frozen['A']]
    a = native['Delta3']['A']; n = len(a); h0 = z(n,n)
    for i in range(4):
        for j in range(4): h0[i][j] = F(1,4)
    assert mul(a,a)==scale(sub(eye(n),h0),-4)
    assert iszero(mul(a,h0))
    u = add(add(h0,scale(sub(eye(n),h0),F(3,5))),scale(a,F(2,5)))
    assert mul(tr(u),u)==eye(n)  # independently declared cosine/sine fixture

    t = [[F(1,2),F(0)],[F(0),F(3,4)]]
    g = sub(mul(tr(t),t),eye(2)); loss = scale(g,-1)
    assert g==[[F(-3,4),F(0)],[F(0),F(-7,16)]]
    assert loss==[[F(3,4),F(0)],[F(0),F(7,16)]]
    # Negative row signs cannot change a positive Gram matrix's inertia.
    row_flip = [[F(-1),F(0)],[F(0),F(1)]]
    assert mul(tr(row_flip),row_flip)==eye(2)
    # Pullback of H=R^T R is (RM)^T(RM), hence positive semidefinite.
    m = z(4,15)
    for i in range(4): m[i][i] = F(1)
    assert rank(m)==4 and 15-rank(m)==11
    assert trace(mul(tr(m),m))==4
    # Symmetric loss and skew order may have zero commutator: no selected time axis.
    assert iszero(sub(mul(eye(2),[[F(0),F(1)],[F(-1),F(0)]]),
                      mul([[F(0),F(1)],[F(-1),F(0)]],eye(2))))
    # Input is an eigenvector of P, yet polar V changes its original ray.
    p = [[F(1,2),F(0)],[F(0),F(1)]]
    v = [[F(0),F(-1)],[F(1),F(0)]]
    tx = mul(mul(v,p),[[F(1)],[F(0)]])
    assert tx==[[F(0)],[F(1,2)]]
    assert tx[0][0]**2==0 and sum(r[0]**2 for r in tx)==F(1,4)

    plus = native['K_plus']; b1,b2,_ = plus['boundaries']; l1 = plus['L1']
    assert specs=={'Delta3':{'4':6},'K_minus':{'3':3,'5':6},'K_plus':{'2':1,'5':9}}
    assert rank(b2)==6 and len(b2[0])-rank(b2)==3
    assert rank(plus['boundaries'][2])==3
    assert rank(mul(tr(native['Delta3']['boundaries'][0]),native['Delta3']['boundaries'][0]))==3
    gradient = scale(mul(tr(b1),b1),F(1,5))
    curl = sub(eye(10),gradient)
    assert mul(gradient,gradient)==gradient and rank(gradient)==4
    assert rank(curl)==6 and mul(curl,curl)==curl
    assert iszero(mul(gradient,curl))
    assert iszero(mul(tr(b2),tr(b1)))
    assert mul(l1,gradient)==scale(gradient,5)
    p2 = scale(sub(scale(eye(10),5),l1),F(1,3))
    p5 = sub(eye(10),p2)
    assert rank(p2)==1 and rank(p5)==9 and mul(p2,p2)==p2
    assert mul(p2,curl)==p2
    tr_printed = trace(printed); tr_printed2 = trace(mul(printed,printed))
    assert tr_printed==47 and tr_printed != 1+2+8*5
    assert tr_printed2 != trace(mul(l1,l1))
    assert not iszero(mul(sub(printed,scale(eye(10),2)),sub(printed,scale(eye(10),5))))
    # Extract the broken code only to parse it; explicitly reject its missing mask.
    start=text.index('import numpy as np',text.index('H_base')-500)
    stop=text.index('Use code with caution.',start)
    try:
        ast.parse(text[start:stop]); broken_syntax=False
    except SyntaxError:
        broken_syntax=True
    assert broken_syntax
    # Exact scalar resonant transport fixture, Gamma_L=Gamma_R=1.
    eta=F(1,100)
    isolated_transmission = F(1)/(eta*eta)
    dressed_transmission = F(1)/(1+eta)**2
    assert isolated_transmission==10000 and dressed_transmission==F(10000,10201)

    results = {
        'status':'PASS','arithmetic':'Fraction, exact','source_sha256':hashlib.sha256(source_bytes).hexdigest(),
        'physical_promotion':0,'independent_review':'pending',
        'scope':'four named corrections and immediate dependent claims; not a complete audit of all 2721 source lines',
        'generator':{'skew_adjoint':True,'frozen_operator_match':True,'rational_propagator_orthogonal':True},
        'loss':{'G_T':g,'positive_loss':loss},
        'reconstruction':{'declared_map_rank':4,'nullity':11,'row_sign_gram_unchanged':True,'commutator_no_selection_counterexample':True},
        'polar_ray_counterexample':{'same_ray_receipt':0,'retained_norm_squared':F(1,4)},
        'edge_spectra':specs,
        'printed_matrix':{'trace':tr_printed,'trace_of_square':tr_printed2,'claimed_trace':43,
                          'native_K_plus_trace':trace(l1),'native_K_plus_trace_of_square':trace(mul(l1,l1)),
                          'claimed_spectrum_rejected':True,'native_spectrum_rejected_for_printed_matrix':True},
        'K_plus_hodge':{'gradient_rank':rank(gradient),'curl_rank':rank(curl),'gradient_eigenvalue':5,
                        'eigenvalue_2_multiplicity':1,'eigenvalue_2_sector':'curl',
                        'B2_kernel_dimension':3,'B3_image_dimension':3},
        'broken_scattering_script':{'syntax_rejected':True,'imported_code_executed':False,'mask_recovered':False},
        'transport_fixture':{'isolated_resolvent_quantity':isolated_transmission,'dressed_transmission':dressed_transmission,
                              'units':'independent dimensionless illustration; not a UD physical model'},
        'numerical_target_evaluated':False
    }
    native['K_plus']['gradient_projector']=gradient
    native['K_plus']['curl_projector']=curl
    native['K_plus']['P2']=p2
    native['K_plus']['P5']=p5
    return encode(results), encode(native)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    results,operators=run(ROOT/'sources/PASTED_TEXT_ORIGINAL.txt')
    if args.check:
        assert json.loads((ROOT/'RESULTS.json').read_text())==results
        assert json.loads((ROOT/'CORRECTED_OPERATORS.json').read_text())==operators
    else:
        (ROOT/'RESULTS.json').write_text(json.dumps(results,indent=2)+'\n')
        (ROOT/'CORRECTED_OPERATORS.json').write_text(json.dumps(operators,indent=2)+'\n')
    print(json.dumps(results,indent=2))
