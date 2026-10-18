#!/usr/bin/env python3
"""Conditional perturbation-radius theorem from certified record extrema; no metrology claim."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from flint import arb,fmpq,ctx
from proof_math import up,down
ctx.prec=512
def aq(v):return arb(fmpq(v.numerator,v.denominator))
def run(certificate,contract,output):
 cert=json.loads(Path(certificate).read_text());c=json.loads(Path(contract).read_text());assert cert['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
 lo,hi,tail=[F(*cert[k]) for k in ['sigma_r_lower','sigma_1_upper','projection_tail_frobenius_upper']];T=F(*cert['selection_threshold']);cap=c['spectral_rule']['retained_condition_number_strict_upper']
 radius=min(T-tail,lo-T,(cap*lo-hi)/(cap+1));B=F(*c['spectral_rule']['data_Hankel_operator_error_ceiling']);assert B<radius
 condition=(hi+B)/(lo-B);assert hi+B>0 and lo-B>T and tail+B<T and condition<cap
 d=F(*c['history_vector_error_ceiling']);deltaF=arb(37).sqrt()*aq(d);lv=aq(lo)-deltaF;hv=aq(hi)+deltaF;tv=aq(tail)+deltaF;assert lv>aq(T) and tv<aq(T) and hv/lv<cap
 result={'status':'DERIVED_CONDITIONAL','physical_promotion':0,'independent_review':'pending','premise_receipts_validated':False,'radius_strict_operator_norm':[radius.numerator,radius.denominator],'source_operator_error_ceiling':[B.numerator,B.denominator],'at_source_operator_error_ceiling':{'sigma_r_lower':[ (lo-B).numerator,(lo-B).denominator],'sigma_1_upper':[(hi+B).numerator,(hi+B).denominator],'sigma_r_plus1_upper':[(tail+B).numerator,(tail+B).denominator],'condition_upper':[condition.numerator,condition.denominator],'projection_frobenius_tail_claimed':False,'readable_condition_upper':float(condition)},'uniform_vector_error_case':{'each_vector_l2_error_ceiling':[d.numerator,d.denominator],'hankel_frobenius_error_upper':up(deltaF),'sigma_r_lower':down(lv),'sigma_r_plus1_upper':up(tv),'condition_upper':up(hv/lv),'projection_frobenius_tail_upper':up(tv)},'scope':'Numeric signature is stable conditional on the stated perturbation norm. Does not establish acquisition/calibration receipts or physical model membership.'}
 Path(output).write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('contract');p.add_argument('output');a=p.parse_args();run(a.certificate,a.contract,a.output)
