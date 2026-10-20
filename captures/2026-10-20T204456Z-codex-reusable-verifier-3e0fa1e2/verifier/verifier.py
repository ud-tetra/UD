"""Manifest-driven exact certificate for a supplied projected matrix and SVD factors.

No estimator, model constructor, prior certificate, or source repository is read.
The finite input profile and scalar acceptance contract are in PROTOCOL.json.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import argparse
import ast
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import platform
import re
import resource
import struct
import time
import zipfile
import numpy as np
from flint import fmpz_mat

HERE = Path(__file__).resolve().parent


class IntakeError(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise IntakeError(reason)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def read_json(path, limit=65536):
    require(path.stat().st_size <= limit, 'JSON resource limit')
    return json.loads(path.read_text(), object_pairs_hook=unique_object,
                      parse_constant=lambda x: (_ for _ in ()).throw(IntakeError('JSON nonfinite')))


def keys(value, wanted):
    require(type(value) is dict and set(value) == set(wanted), 'schema keys')


def integer(value, lo, hi, name):
    require(type(value) is int and lo <= value <= hi, name)
    return value


def clean_path(path):
    absolute = Path(os.path.abspath(path))
    for component in (absolute, *absolute.parents):
        require(not component.is_symlink(), 'symlink path component')
    return absolute


def resolve_input(root, value):
    require(type(value) is str and value and '\\' not in value and '\x00' not in value,
            'invalid relative path')
    path = Path(value)
    require(not path.is_absolute() and '..' not in path.parts, 'path escape')
    out = clean_path(root / path)
    require(out.is_relative_to(root) and out.is_file(), 'input file missing or escaped')
    return out


def checked_digest(value):
    require(type(value) is str and re.fullmatch('[0-9a-f]{64}', value), 'SHA256 syntax')
    return value


def header(stream, size, dtype, profile):
    require(stream.read(6) == b'\x93NUMPY', 'NPY magic')
    version = stream.read(2)
    require(version in (b'\x01\x00', b'\x02\x00', b'\x03\x00'), 'NPY version')
    width = 2 if version == b'\x01\x00' else 4
    raw = stream.read(width)
    require(len(raw) == width, 'truncated NPY header length')
    length = int.from_bytes(raw, 'little')
    require(length <= profile['max_header_bytes'], 'NPY header limit')
    raw = stream.read(length)
    require(len(raw) == length, 'truncated NPY header')
    try:
        meta = ast.literal_eval(raw.decode('utf8' if version == b'\x03\x00' else 'latin1'))
    except (ValueError, SyntaxError, UnicodeError, RecursionError) as exc:
        raise IntakeError('invalid NPY metadata') from exc
    keys(meta, ('descr', 'fortran_order', 'shape'))
    require(meta['descr'] == dtype and type(meta['fortran_order']) is bool, 'NPY dtype/order')
    shape = meta['shape']
    require(type(shape) is tuple and 1 <= len(shape) <= 2, 'NPY dimensions')
    require(all(type(x) is int and 0 < x <= profile['max_m'] for x in shape), 'NPY shape limit')
    payload = math.prod(shape) * 8
    require(payload <= profile['max_entry_bytes'], 'NPY payload limit')
    require(stream.tell() + payload == size, 'NPY payload length/trailing bytes')
    return shape


def preflight_npz(path, expected, profile):
    try:
        with zipfile.ZipFile(path) as z:
            entries = z.infolist()
            require(len(entries) == len(expected) and {x.filename for x in entries} == set(expected),
                    'NPZ exact member set')
            require(sum(x.file_size for x in entries) <= profile['max_file_bytes'], 'NPZ expanded limit')
            result = {}
            for entry in entries:
                require(not (entry.flag_bits & 1) and entry.compress_type in (0, 8), 'NPZ encoding')
                require(entry.file_size <= profile['max_entry_bytes'], 'NPZ entry limit')
                with z.open(entry) as stream:
                    result[entry.filename] = header(stream, entry.file_size, expected[entry.filename], profile)
            return result
    except (zipfile.BadZipFile, NotImplementedError, RuntimeError, EOFError) as exc:
        raise IntakeError('invalid NPZ archive') from exc


def intake(manifest, out, protocol):
    profile = protocol['profile']
    manifest = clean_path(manifest)
    require(manifest.is_file(), 'manifest missing')
    manifest_hash = sha(manifest)
    spec = read_json(manifest)
    keys(spec, ('schema_version', 'record', 'svd', 'left_chunks'))
    require(spec['schema_version'] == '1.0', 'schema version')
    keys(spec['record'], ('path', 'sha256', 'payload_sha256', 'dyadic_exponent'))
    keys(spec['svd'], ('path', 'sha256'))
    integer(spec['record']['dyadic_exponent'], 0, profile['max_denominator_bits'], 'record exponent')
    checked_digest(spec['record']['payload_sha256'])
    chunks = spec['left_chunks']
    require(type(chunks) is list and 1 <= len(chunks) <= profile['max_m'], 'chunk list')
    for chunk in chunks:
        keys(chunk, ('path', 'sha256', 'start', 'stop'))
        integer(chunk['start'], 0, profile['max_m'], 'chunk start')
        integer(chunk['stop'], 1, profile['max_m'], 'chunk stop')
    rows = [spec['record'], spec['svd'], *chunks]
    files = []
    total = 0
    for row in rows:
        path = resolve_input(manifest.parent, row['path'])
        expected_hash = checked_digest(row['sha256'])
        size = path.stat().st_size
        require(size <= profile['max_file_bytes'], 'input file resource limit')
        total += size
        require(total <= profile['max_total_bytes'], 'total input resource limit')
        require(sha(path) == expected_hash, 'input SHA256 mismatch')
        files.append(path)
    require(len(set(files)) == len(files) and manifest not in files, 'duplicate input identity')
    out = clean_path(out)
    require(not out.exists(), 'output already exists')
    require(not HERE.is_relative_to(out) and not out.is_relative_to(HERE), 'output overlaps package')
    for path in [manifest, *files]:
        require(path != out and not path.is_relative_to(out), 'output overlaps input')
    with files[0].open('rb') as stream:
        record_shape = header(stream, files[0].stat().st_size, '<i8', profile)
    require(len(record_shape) == 2, 'record must be matrix')
    m, n = record_shape
    require(2 <= n <= min(m, profile['max_n']), 'record dimension profile')
    sh = preflight_npz(files[1], {'singular.npy': '<f8', 'right_transpose.npy': '<f8'}, profile)
    require(sh == {'singular.npy': (n,), 'right_transpose.npy': (n, n)}, 'SVD dimensions')
    # Every ZIP/NPY header and chunk interval is checked before any array materialization.
    previous = 0
    left_shapes = []
    for row, path in zip(chunks, files[2:]):
        require(row['start'] == previous and row['stop'] > row['start'] and row['stop'] <= m,
                'chunk intervals must cover rows exactly in order')
        csh = preflight_npz(path, {'basis.npy': '<f8'}, profile)['basis.npy']
        require(len(csh) == 2 and csh[0] == row['stop'] - row['start'] and csh[1] < n,
                'left chunk dimensions')
        previous = row['stop']
        left_shapes.append(csh)
    require(previous == m, 'incomplete left row coverage')
    N = np.load(files[0], mmap_mode='r', allow_pickle=False)
    require(N.dtype == np.dtype('<i8') and N.shape == (m, n), 'loaded record mismatch')
    payload_hash = hashlib.sha256(np.asarray(N, dtype='<i8').tobytes(order='C')).hexdigest()
    require(payload_hash == spec['record']['payload_sha256'], 'record payload SHA256 mismatch')
    with np.load(files[1], allow_pickle=False) as archive:
        singular = archive['singular'].copy()
        vt = archive['right_transpose'].copy()
    require(singular.dtype == vt.dtype == np.dtype('<f8') and np.isfinite(singular).all()
            and np.isfinite(vt).all(), 'nonfinite or wrong SVD dtype')
    require(np.all(singular >= 0) and np.all(singular[:-1] >= singular[1:]), 'singular order/sign')
    s = [F(*float(value).as_integer_ratio()) for value in singular]
    cutoff = F(1, 1 << protocol['cutoff_denominator_bits'])
    require(cutoff not in s, 'singular value equals strict cutoff')
    q = sum(value > cutoff for value in s)
    require(1 <= q < n and all(shape[1] == q for shape in left_shapes), 'retained order profile')
    U = np.empty((m, q), dtype='<f8')
    for row, path in zip(chunks, files[2:]):
        with np.load(path, allow_pickle=False) as archive:
            block = archive['basis']
            require(block.dtype == np.dtype('<f8') and np.isfinite(block).all(), 'left factor values')
            U[row['start']:row['stop']] = block
    # Exact encodings are resource-checked before numerical output creation.
    Ui, bU = encode(U, profile)
    Vi, bV = encode(vt[:q].T, profile)
    Di, bD = encode(vt[q:].T, profile)
    si, bS = encode(singular[:q], profile)
    require(sha(manifest) == manifest_hash and all(sha(p) == row['sha256'] for p, row in zip(files, rows)),
            'input changed during intake')
    return {'manifest': manifest, 'manifest_hash': manifest_hash, 'spec': spec, 'files': files,
            'file_rows': rows, 'out': out, 'N': N, 'm': m, 'n': n, 'q': q, 's': s,
            'Ui': Ui, 'Vi': Vi, 'Di': Di, 'si': si, 'bN': spec['record']['dyadic_exponent'],
            'bU': bU, 'bV': bV, 'bD': bD, 'bS': bS, 'payload_hash': payload_hash}


def encode(values, profile):
    ratios = [float(x).as_integer_ratio() for x in values.flat]
    bits = max(d.bit_length() - 1 for _, d in ratios)
    require(bits <= profile['max_denominator_bits'], 'encoded denominator profile')
    data = [numerator << (bits - denominator.bit_length() + 1) for numerator, denominator in ratios]
    require(all(abs(value).bit_length() <= profile['max_encoded_integer_bits'] for value in data),
            'encoded integer profile')
    return np.array(data, dtype=object).reshape(values.shape), bits


def root_upper(value, power, bits):
    if value < 0:
        raise ArithmeticError('negative exact squared norm')
    top = value.numerator << (power * bits)
    bottom = value.denominator
    k = math.isqrt(top // bottom)
    if power == 4:
        k = math.isqrt(k)
    if k ** power * bottom < top:
        k += 1
    answer = F(k, 1 << bits)
    if not (answer ** power >= value and (k == 0 or F(k - 1, 1 << bits) ** power < value)):
        raise ArithmeticError('root enclosure check')
    return answer


def pair(value):
    return [str(value.numerator), str(value.denominator)]


def matrix_rows(value):
    return [[int(x) for x in row] for row in value.tolist()]


def pack(rows, symmetric):
    r, c = len(rows), len(rows[0])
    return {'shape': [r, c], 'storage': 'upper' if symmetric else 'full',
            'values': [str(rows[i][j]) for i in range(r) for j in range(i if symmetric else 0, c)]}


def frobenius_square(rows, denominator_bits):
    return F(sum(value * value for row in rows for value in row), 1 << (2 * denominator_bits))


def calculate(data, protocol):
    N, Ui, Vi, Di, si = (data[k] for k in ('N', 'Ui', 'Vi', 'Di', 'si'))
    m, n, q = (data[k] for k in ('m', 'n', 'q'))
    bN, bU, bV, bD, bS = (data[k] for k in ('bN', 'bU', 'bV', 'bD', 'bS'))
    vm, dm = fmpz_mat(Vi.tolist()), fmpz_mat(Di.tolist())
    M, K, A = fmpz_mat(n, n), fmpz_mat(n, q), fmpz_mat(q, q)
    for start in range(0, m, protocol['block_rows']):
        stop = min(m, start + protocol['block_rows'])
        nm = fmpz_mat(N[start:stop].astype(object).tolist())
        um = fmpz_mat(Ui[start:stop].tolist())
        M += nm.transpose() * nm
        K += nm.transpose() * um
        A += um.transpose() * um
    B = vm.transpose() * vm
    E = dm.transpose() * dm
    for j in range(n - q):
        E[j, j] -= 1 << (2 * bD)
    H = dm.transpose() * M * dm
    rows = {name: matrix_rows(value) for name, value in [('M', M), ('K', K), ('A', A), ('B', B), ('E', E), ('H', H)]}
    ad = [row[:] for row in rows['A']]
    bd = [row[:] for row in rows['B']]
    for j in range(q):
        ad[j][j] -= 1 << (2 * bU)
        bd[j][j] -= 1 << (2 * bV)
    a2 = frobenius_square(ad, 2 * bU)
    b2 = frobenius_square(bd, 2 * bV)
    eta2 = frobenius_square(rows['E'], 2 * bD)
    r4 = frobenius_square(rows['H'], 2 * (bN + bD))
    singular_int = [int(x) for x in si]
    cross = sum(rows['K'][i][j] * int(Vi[i, j]) * singular_int[j] for i in range(n) for j in range(q))
    mv = M * vm
    trace = sum(int(Vi[i, j]) * int(mv[i, j]) for i in range(n) for j in range(q))
    udiag = sum(singular_int[j] ** 2 * rows['A'][j][j] for j in range(q))
    vdiag = sum(singular_int[j] ** 2 * rows['B'][j][j] for j in range(q))
    ksquare = sum(value ** 2 for row in rows['K'] for value in row)
    kF = max(bN + bV, bU + bS)
    alphaF, betaF = 1 << (kF - bN - bV), 1 << (kF - bU - bS)
    kG = max(bN + bU, bV + bS)
    alphaG, betaG = 1 << (kG - bN - bU), 1 << (kG - bV - bS)
    f2 = F(alphaF ** 2 * trace - 2 * alphaF * betaF * cross + betaF ** 2 * udiag, 1 << (2 * kF))
    g2 = F(alphaG ** 2 * ksquare - 2 * alphaG * betaG * cross + betaG ** 2 * vdiag, 1 << (2 * kG))
    exact = {'a_squared': a2, 'b_squared': b2, 'eta_squared': eta2, 'r_fourth': r4,
             'f_squared': f2, 'g_squared': g2}
    bits = protocol['root_ceiling_bits']
    metrics = {name: root_upper(exact[key], power, bits) for name, key, power in
               [('a', 'a_squared', 2), ('b', 'b_squared', 2), ('eta', 'eta_squared', 2),
                ('r', 'r_fourth', 4), ('f', 'f_squared', 2), ('g', 'g_squared', 2)]}
    witness = {'schema_version': '1.0', 'dimensions': {'m': m, 'n': n, 'q': q},
               'exponents': {key: data[key] for key in ('bN', 'bU', 'bV', 'bD', 'bS')},
               'singular_integers': [str(x) for x in singular_int],
               'matrices': {name: pack(value, name != 'K') for name, value in rows.items()},
               'trace_terms': {key: str(value) for key, value in [('cross', cross), ('trace', trace), ('udiag', udiag), ('vdiag', vdiag), ('ksquare', ksquare)]},
               'exact': {key: pair(value) for key, value in exact.items()},
               'metrics': {key: pair(value) for key, value in metrics.items()}}
    return metrics, witness


def derive(metrics, s, q, protocol):
    a, b, eta, r, f, g = (metrics[key] for key in ('a', 'b', 'eta', 'r', 'f', 'g'))
    gates = {'left_Gram_full_rank': a < 1, 'retained_right_Gram_full_rank': b < 1,
             'discarded_right_Gram_full_rank': eta < 1}
    bounds = {}
    if all(gates.values()):
        tail = r / (1 - eta)
        compression = (s[0] * (a / (2 - a) + b / (2 - b)) + f) / (1 - b)
        offdiagonal = max(f / (1 - b), g / (1 - a))
        epsilon = compression + offdiagonal
        gap = s[q - 1] - compression - tail - offdiagonal
        full = max(epsilon, tail, s[q])
        lower = s[q - 1] - epsilon
        bounds = {'direct_tail_upper': tail, 'compression_upper': compression,
                  'offdiagonal_upper': offdiagonal, 'retained_abs_error_upper': epsilon,
                  'discarded_abs_error_upper': max(tail, s[q]), 'full_abs_error_upper': full,
                  'matching_gap': gap, 'ambient_sigma_q_lower': lower}
        if lower > 0:
            bounds['ambient_leading_condition_upper'] = (s[0] + epsilon) / lower
        cutoff = F(1, 1 << protocol['cutoff_denominator_bits'])
        gates.update({'strict_leading_block_matching': gap > 0,
                      'tail_below_cutoff': tail < cutoff, 'retained_lower_above_cutoff': lower > cutoff,
                      'full_abs_error_below_gate': full < F(1, 1 << protocol['accuracy_denominator_bits'])})
    return gates, bounds


def dump(path, value):
    with path.open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


def run(manifest, output):
    start = time.perf_counter()
    protocol = read_json(HERE / 'PROTOCOL.json')
    seal = read_json(HERE / 'SEAL.json')
    for name, digest in seal['files'].items():
        require(sha(HERE / name) == digest, 'package source seal mismatch')
    data = intake(manifest, output, protocol)
    out = data['out']
    out.mkdir(parents=True, exist_ok=False)
    metrics, witness = calculate(data, protocol)
    gates, bounds = derive(metrics, data['s'], data['q'], protocol)
    payload = json.dumps(witness, sort_keys=True, separators=(',', ':')).encode()
    with (out / 'WITNESS.json.gz').open('xb') as stream:
        stream.write(gzip.compress(payload, mtime=0))
    unchanged = sha(data['manifest']) == data['manifest_hash'] and all(
        sha(path) == row['sha256'] for path, row in zip(data['files'], data['file_rows']))
    gates['input_bytes_unchanged'] = unchanged
    passed = all(gates.values())
    cert = {'schema_version': '1.0', 'status': 'CERTIFIED_FINITE_SUPPLIED_RECORD' if passed else 'HOLD_NUMERICAL',
            'dimensions': {'m': data['m'], 'n': data['n'], 'q': data['q']}, 'gates': gates,
            'metrics': {key: pair(value) for key, value in metrics.items()},
            'bounds': {key: pair(value) for key, value in bounds.items()},
            'readable': {key: float(value) for key, value in bounds.items()},
            'manifest_sha256': data['manifest_hash'], 'record_payload_sha256': data['payload_hash'],
            'protocol_sha256': sha(HERE / 'PROTOCOL.json'), 'seal_sha256': sha(HERE / 'SEAL.json'),
            'witness_sha256': sha(out / 'WITNESS.json.gz'),
            'new_estimator_calls': 0, 'prior_certificate_inputs': 0,
            'input_authenticity': 'SUPPLIED_BYTES_ONLY; acquisition and projection lineage are separate',
            'all_input_backend_conformance': 'OPEN', 'algebraic_rank_q_claimed': False,
            'full_matrix_condition_claimed': False, 'external_promotion_review': 'PENDING', 'physical_promotion': 0}
    dump(out / 'CERTIFICATE.json', cert)
    dump(out / 'RESOURCE.json', {'elapsed_seconds': time.perf_counter() - start,
         'process_peak_RSS_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'python': platform.python_version(), 'numpy': np.__version__,
         'scope': 'Supplied projected record and saved factors; not full Hankel pipeline benchmark'})
    print(json.dumps({'status': cert['status'], 'dimensions': cert['dimensions'], 'readable': cert['readable']}), flush=True)
    return 0 if passed else 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    try:
        return run(Path(args.manifest), Path(args.out))
    except (IntakeError, OSError, ValueError, EOFError, struct.error, OverflowError, zipfile.BadZipFile) as exc:
        print(json.dumps({'status': 'HOLD_INTAKE_OR_INPUT_IO', 'reason': str(exc)}), flush=True)
        return 2
    except Exception as exc:
        print(json.dumps({'status': 'HOLD_EXECUTION', 'reason': type(exc).__name__ + ': ' + str(exc)}), flush=True)
        return 3


if __name__ == '__main__':
    raise SystemExit(main())
