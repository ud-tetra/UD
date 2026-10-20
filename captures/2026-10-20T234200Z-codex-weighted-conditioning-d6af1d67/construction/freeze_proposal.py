from pathlib import Path
import json,gzip,hashlib
import numpy as np
P=Path('/workspace/scratch/f3d1c2f040c9');O=P/'c27_work';z=np.load(O/'FULL_SCREEN.npz',allow_pickle=False);Q=z['Q'].copy();Q[:,1000:]*=-1
Qint=np.rint(Q*2**40).astype('<i8');raw=Qint.tobytes(order='C');(O/'Q_DYADIC.bin.gz').write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
w=z['frequencies'];order=np.argsort(w);groups=[]
for i in order:
 if not groups or abs(w[i]-w[groups[-1][0]])>1e-7:groups.append([int(i)])
 else:groups[-1].append(int(i))
wi=np.zeros(len(w),dtype=np.int64);labels=np.zeros(len(w),dtype=np.int64);centers=[]
for g,ids in enumerate(groups):
 n=int(round(float(np.mean(w[ids]))*2**40));wi[ids]=n;labels[ids]=g;centers.append(n)
meta={'status':'DYADIC_TRIAL_WITNESS_FROZEN_BEFORE_VALIDATED_ARITHMETIC','model':'PR305 unchanged','rank_inherited':1999,'shape':[2640,1999],'integer_dtype':'little_endian_signed_int64','coordinate_scale_denominator_power2':40,'frequency_scale_denominator_power2':40,'frequency_integers':wi.tolist(),'distinct_frequency_integers':centers,'frequency_group_indices':labels.tolist(),'column_order':'zero;999lower-grade oscillator vectors;999negative upper-grade partners','source_convention':'K upper−B, lower+Btranspose; trialJ upper+omega, lower−omega','Q_gzip_sha256':hashlib.sha256((O/'Q_DYADIC.bin.gz').read_bytes()).hexdigest(),'Q_decoded_sha256':hashlib.sha256(raw).hexdigest(),'numerical_search_disclosed':'Trial columns selected after numerical fullGram screen≈180. Group tolerance1e-7 and dyadic rounding only choose J; exact E covers all approximation. No model/gate tuning or blinded acquisition claim.','certificate_target':'positive quotient kappa<512 via fixed conservative exact residual inequalities, not claiming numerical≈180 certified','budgets':{'eta_Q_frobenius':'<1/16','E_frobenius':'<2^-24','eta_eigenproposal_frobenius':'<1/16','eigenproposal_residual_frobenius':'<2^-22','proposal_diagonal_min':'>9*2^-20','Gram_operator_error':'<2^-44'},'physical_promotion':0,'external_promotion_review':'PENDING'}
(O/'PROPOSAL_FREEZE.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n');print({'Q_gzip_bytes':(O/'Q_DYADIC.bin.gz').stat().st_size,'frequency_groups':len(centers),'sha256':meta['Q_gzip_sha256']})
