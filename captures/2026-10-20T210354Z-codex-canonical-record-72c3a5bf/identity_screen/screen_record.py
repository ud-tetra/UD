"""Canonical identity of a supplied dyadic projected matrix, not acquisition proof."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import struct
import time
import numpy as np

HERE = Path(__file__).resolve().parent
DOMAIN = b'UD_DYADIC_MATRIX_V1\0'


class IntakeError(Exception):
    pass


def need(value, reason):
    if not value:
        raise IntakeError(reason)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def unique(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def load_json(path):
    need(path.stat().st_size <= 65536, 'JSON resource limit')
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda x: (_ for _ in ()).throw(IntakeError('nonfinite JSON')))


def keys(value, fields):
    need(type(value) is dict and set(value) == set(fields), 'schema keys')


def path_checked(value):
    path = Path(value).absolute()
    for part in (path, *path.parents):
        need(not part.is_symlink(), 'symlink path')
    return path.resolve()


def output_checked(value, inputs):
    out = path_checked(value)
    protected = [HERE]
    # Append-only capture ancestors are protected when the source is archived.
    protected.extend(p for p in HERE.parents if (p / 'MANIFEST.json').is_file())
    need(not out.exists(), 'existing output')
    for part in protected:
        need(not out.is_relative_to(part) and not part.is_relative_to(out), 'protected source/capture output')
    for part in inputs:
        need(out != part and not part.is_relative_to(out), 'output overlaps input')
    return out


def record_header(path, profile):
    need(path.is_file() and path.stat().st_size <= profile['max_file_bytes'], 'record file limit/missing')
    with path.open('rb') as stream:
        need(stream.read(6) == b'\x93NUMPY', 'NPY magic')
        version = stream.read(2)
        need(version in (b'\x01\x00', b'\x02\x00', b'\x03\x00'), 'NPY version')
        width = 2 if version == b'\x01\x00' else 4
        raw = stream.read(width)
        need(len(raw) == width, 'NPY length')
        length = int.from_bytes(raw, 'little')
        need(length <= profile['max_header_bytes'], 'NPY header resource limit')
        raw = stream.read(length)
        need(len(raw) == length, 'NPY truncated header')
        try:
            meta = ast.literal_eval(raw.decode('utf8' if version == b'\x03\x00' else 'latin1'))
        except (SyntaxError, ValueError, UnicodeError, RecursionError) as exc:
            raise IntakeError('invalid NPY header') from exc
        keys(meta, ('descr', 'shape', 'fortran_order'))
        need(meta['descr'] == '<i8' and type(meta['fortran_order']) is bool, 'record dtype/order')
        shape = meta['shape']
        need(type(shape) is tuple and len(shape) == 2 and all(type(x) is int for x in shape), 'matrix shape')
        m, n = shape
        need(1 <= m <= profile['max_m'] and 1 <= n <= profile['max_n'], 'matrix dimension profile')
        need(stream.tell() + 8 * m * n == path.stat().st_size, 'payload size/trailing bytes')
    return m, n


def catalog_read(path):
    obj = load_json(path)
    keys(obj, ('schema_version', 'identity_format', 'coverage', 'records'))
    need(obj['schema_version'] == '1.0' and obj['identity_format'] == DOMAIN[:-1].decode(), 'catalog format')
    need(type(obj['coverage']) is str and 1 <= len(obj['coverage']) <= 2048, 'catalog coverage')
    need(type(obj['records']) is list and len(obj['records']) <= 256, 'catalog size')
    ids = set()
    for row in obj['records']:
        keys(row, ('record_id', 'fingerprint_sha256', 'source_reference'))
        need(type(row['record_id']) is str and re.fullmatch('[A-Za-z0-9_.-]{1,128}', row['record_id']), 'record id')
        need(row['record_id'] not in ids, 'duplicate record id')
        ids.add(row['record_id'])
        need(type(row['fingerprint_sha256']) is str and re.fullmatch('[0-9a-f]{64}', row['fingerprint_sha256']), 'fingerprint syntax')
        need(type(row['source_reference']) is str and 1 <= len(row['source_reference']) <= 2048, 'source reference')
    return obj


def canonical(N, bits, block_rows=512):
    """Signed OR finds the common 2-adic valuation without abs(INT64_MIN)."""
    aggregate = 0
    for start in range(0, N.shape[0], block_rows):
        aggregate |= int(np.bitwise_or.reduce(N[start:start + block_rows], axis=None))
    shift = bits if aggregate == 0 else min(bits, (aggregate & -aggregate).bit_length() - 1)
    normalized_bits = 0 if aggregate == 0 else bits - shift
    # For a nonzero signed-int64 matrix shift<=63. Zero is handled separately.
    digest = hashlib.sha256(DOMAIN + struct.pack('<IIH', *N.shape, normalized_bits))
    payload = hashlib.sha256()
    for start in range(0, N.shape[0], block_rows):
        block = np.asarray(N[start:start + block_rows], dtype='<i8')
        payload.update(block.tobytes(order='C'))
        normalized = np.zeros_like(block) if aggregate == 0 else np.right_shift(block, shift)
        digest.update(np.asarray(normalized, dtype='<i8').tobytes(order='C'))
    return {'fingerprint_sha256': digest.hexdigest(), 'canonical_denominator_bits': normalized_bits,
            'removed_power_of_two': shift, 'all_zero': aggregate == 0,
            'input_C_order_int64_payload_sha256': payload.hexdigest()}


def run(record, bits, known, output):
    start = time.perf_counter()
    protocol = load_json(HERE / 'PROTOCOL.json')
    seal = load_json(HERE / 'SEAL.json')
    for name, digest in seal['files'].items():
        need(sha(HERE / name) == digest, 'source seal changed')
    need(type(bits) is int and 0 <= bits <= protocol['max_denominator_bits'], 'denominator profile')
    record, known = path_checked(record), path_checked(known)
    need(record != known, 'record/catalog identity overlap')
    out = output_checked(output, (record, known))
    shape = record_header(record, protocol)
    catalog = catalog_read(known)
    record_hash, catalog_hash = sha(record), sha(known)
    N = np.load(record, mmap_mode='r', allow_pickle=False)
    need(N.shape == shape and N.dtype == np.dtype('<i8'), 'loaded record mismatch')
    answer = canonical(N, bits, protocol['block_rows'])
    matches = [row['record_id'] for row in catalog['records'] if row['fingerprint_sha256'] == answer['fingerprint_sha256']]
    need(sha(record) == record_hash and sha(known) == catalog_hash, 'input changed at endpoint hash check')
    for name, digest in seal['files'].items():
        need(sha(HERE / name) == digest, 'source changed during screen')
    result = {'schema_version': '1.0', 'identity_relation': 'LISTED_FINGERPRINT' if matches else 'UNLISTED_FINGERPRINT',
              'canonical': answer, 'shape': list(shape), 'input_denominator_bits': bits,
              'matching_record_ids': matches, 'catalog_coverage': catalog['coverage'],
              'record_npy_sha256': record_hash, 'catalog_sha256': catalog_hash,
              'protocol_sha256': sha(HERE / 'PROTOCOL.json'), 'seal_sha256': sha(HERE / 'SEAL.json'),
              'input_bytes_unchanged_at_endpoint_checks': True,
              'provenance_status': 'HOLD_PROVENANCE_NOT_ESTABLISHED',
              'independent_acquisition': 'NOT_ESTABLISHED', 'fresh_preparation': 'NOT_ESTABLISHED',
              'numerical_spectral_certificate': 'NOT_EVALUATED', 'hash_injectivity_claimed': False,
              'new_estimator_calls': 0, 'all_input_backend_conformance': 'OPEN',
              'external_promotion_review': 'PENDING', 'physical_promotion': 0}
    out.mkdir(parents=True, exist_ok=False)
    with (out / 'SCREEN.json').open('x') as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True) + '\n')
    with (out / 'RESOURCE.json').open('x') as stream:
        stream.write(json.dumps({'elapsed_seconds': time.perf_counter() - start,
                                'scope': 'Projected matrix identity screen only'}, indent=2) + '\n')
    print(json.dumps({'identity_relation': result['identity_relation'], 'matches': matches,
                      'provenance_status': result['provenance_status']}), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', required=True)
    parser.add_argument('--denominator-bits', type=int, required=True)
    parser.add_argument('--known', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    try:
        return run(Path(args.record), args.denominator_bits, Path(args.known), Path(args.out))
    except (IntakeError, OSError, ValueError, EOFError, struct.error, OverflowError) as exc:
        print(json.dumps({'status': 'HOLD_INTAKE_OR_IO', 'reason': str(exc)}), flush=True)
        return 2
    except Exception as exc:
        print(json.dumps({'status': 'HOLD_EXECUTION', 'reason': type(exc).__name__ + ': ' + str(exc)}), flush=True)
        return 3


if __name__ == '__main__':
    raise SystemExit(main())
