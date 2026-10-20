"""Pinned identity -> exact numerical verifier -> distinct product-audit handoff.

Successful numerical completion always retains acquisition provenance HOLD.
No externally supplied certificate/status is an executable input to this runner.
"""
import argparse
import gc
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import zipfile

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
NUMERIC_PASS = 'CERTIFIED_FINITE_SUPPLIED_RECORD'
AUDIT_PASS = 'PASS_ALL_SIX_EXACT_CRT_AND_FRESH_SCALAR_CERTIFICATE'
GATES = {'left_Gram_full_rank', 'retained_right_Gram_full_rank', 'discarded_right_Gram_full_rank',
         'strict_leading_block_matching', 'tail_below_cutoff', 'retained_lower_above_cutoff',
         'full_abs_error_below_gate', 'input_bytes_unchanged'}
PROVENANCE = {'provenance_status': 'HOLD_PROVENANCE_NOT_ESTABLISHED',
              'independent_acquisition': 'NOT_ESTABLISHED', 'fresh_preparation': 'NOT_ESTABLISHED',
              'external_promotion_review': 'PENDING', 'physical_promotion': 0,
              'all_input_backend_conformance': 'OPEN'}


class HandoffError(Exception):
    pass


def need(ok, reason):
    if not ok:
        raise HandoffError(reason)


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


def load(path, limit=1048576):
    need(path.is_file() and path.stat().st_size <= limit, 'missing/oversize JSON: ' + path.name)
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda x: (_ for _ in ()).throw(HandoffError('nonfinite JSON')))


def keys(value, wanted):
    need(type(value) is dict and set(value) == set(wanted), 'schema keys')


def clean(path):
    p = Path(os.path.abspath(path))
    for part in (p, *p.parents):
        need(not part.is_symlink(), 'symlink path component')
    return p


def guard_output(path, repo, inputs=()):
    out = clean(path)
    need(not out.exists(), 'output exists')
    protected = [repo, HERE, *(p for p in HERE.parents if (p / 'MANIFEST.json').is_file())]
    for p in protected:
        need(not out.is_relative_to(p) and not p.is_relative_to(out), 'output overlaps source/repository')
    for p in inputs:
        need(out != p and not p.is_relative_to(out), 'output overlaps input')
    return out


def source_check(repo):
    seal = load(HERE / 'SEAL.json')
    for name, digest in seal['files'].items():
        need(sha(HERE / name) == digest, 'runner source seal changed')
    config = load(HERE / 'DEPENDENCIES.json')
    keys(config, ('version', 'roles'))
    keys(config['roles'], ('identity', 'numerical', 'audit'))
    paths = {}
    for role, spec in config['roles'].items():
        keys(spec, ('entry', 'files'))
        for relative, digest in spec['files'].items():
            need(type(relative) is str and not Path(relative).is_absolute() and '..' not in Path(relative).parts,
                 'dependency relative path')
            p = clean(repo / relative)
            need(p.is_relative_to(repo) and p.is_file(), 'dependency missing/escaped')
            need(type(digest) is str and re.fullmatch('[0-9a-f]{64}', digest) and sha(p) == digest,
                 'dependency bytes changed: ' + relative)
        need(spec['entry'] in spec['files'], 'unbound entry script')
        paths[role] = repo / spec['entry']
    return config, paths


def same_inputs(expected):
    return all(p.is_file() and sha(p) == digest for p, digest in expected['input_hashes'].items())


def dimensions_equal(value, expected):
    keys(value, ('m', 'n', 'q'))
    return all(type(value[key]) is int and value[key] == expected[key] for key in expected)


def zero_integer(value):
    return type(value) is int and value == 0


def validate_identity(report, expected):
    need(report['identity_relation'] in ('LISTED_FINGERPRINT', 'UNLISTED_FINGERPRINT'), 'identity class')
    fingerprint = report['canonical']['fingerprint_sha256']
    need(type(fingerprint) is str and re.fullmatch('[0-9a-f]{64}', fingerprint), 'identity fingerprint syntax')
    ids = expected['catalog_fingerprint_ids'].get(fingerprint, [])
    need(report['matching_record_ids'] == ids and type(report['matching_record_ids']) is list and
         report['identity_relation'] == ('LISTED_FINGERPRINT' if ids else 'UNLISTED_FINGERPRINT') and
         report['catalog_coverage'] == expected['catalog_coverage'], 'identity catalog/class consistency')
    need(report['record_npy_sha256'] == expected['record_npy_sha256'] and
         report['canonical']['input_C_order_int64_payload_sha256'] == expected['payload_sha256'], 'identity input binding')
    need(type(report['shape']) is list and all(type(x) is int for x in report['shape']) and
         report['shape'] == [expected['dimensions']['m'], expected['dimensions']['n']] and
         type(report['input_denominator_bits']) is int and
         report['input_denominator_bits'] == expected['denominator_bits'], 'identity dimensions/exponent')
    need(report['seal_sha256'] == expected['identity_seal_sha256'] and
         report['protocol_sha256'] == expected['identity_protocol_sha256'] and
         report['catalog_sha256'] == expected['catalog_sha256'], 'identity source/catalog binding')
    need(report['input_bytes_unchanged_at_endpoint_checks'] is True and
         report['hash_injectivity_claimed'] is False and report['numerical_spectral_certificate'] == 'NOT_EVALUATED',
         'identity scope/endpoint flags')
    need(zero_integer(report['new_estimator_calls']), 'identity estimator count')
    for key in PROVENANCE:
        need(type(report[key]) is type(PROVENANCE[key]) and report[key] == PROVENANCE[key], 'identity provenance escalation')


def validate_numerical(cert, expected):
    need(cert['status'] == NUMERIC_PASS, 'numerical result is not certified')
    need(cert['manifest_sha256'] == expected['manifest_sha256'] and
         cert['record_payload_sha256'] == expected['payload_sha256'] and
         dimensions_equal(cert['dimensions'], expected['dimensions']), 'numerical input binding')
    need(cert['seal_sha256'] == expected['numerical_seal_sha256'] and
         cert['protocol_sha256'] == expected['numerical_protocol_sha256'], 'numerical source binding')
    keys(cert['gates'], GATES)
    need(all(type(value) is bool and value for value in cert['gates'].values()), 'numerical gates')
    need(type(cert['physical_promotion']) is int and cert['physical_promotion'] == 0 and
         cert['algebraic_rank_q_claimed'] is False and cert['full_matrix_condition_claimed'] is False and
         cert['all_input_backend_conformance'] == 'OPEN' and cert['external_promotion_review'] == 'PENDING' and
         zero_integer(cert['prior_certificate_inputs']) and zero_integer(cert['new_estimator_calls']), 'numerical scope')


def validate_audit(report, expected, cert, witness_sha256, certificate_sha256):
    need(report['status'] == AUDIT_PASS, 'distinct audit did not pass')
    need(report['manifest_sha256'] == expected['manifest_sha256'] and
         report['record_payload_sha256'] == expected['payload_sha256'] and
         dimensions_equal(report['dimensions'], expected['dimensions']), 'audit input binding')
    need(report['witness_sha256'] == witness_sha256 and
         report['producer_certificate_sha256'] == certificate_sha256 and
         report['audit_freeze_sha256'] == expected['audit_freeze_sha256'], 'audit artifact/source binding')
    keys(report['matrix_checks'], ('M', 'K', 'A', 'B', 'E', 'H'))
    n, q = expected['dimensions']['n'], expected['dimensions']['q']
    sizes = {'M': n*n, 'K': n*q, 'A': q*q, 'B': q*q, 'E': (n-q)**2, 'H': (n-q)**2}
    for name, row in report['matrix_checks'].items():
        need(row['status'] == 'PASS_EXACT_ALL_ENTRY_CRT' and row['primes'] and
             len(row['checks']) == len(row['primes']), 'audit matrix proof incomplete')
        need(type(row['primes']) is list and all(type(p) is int and 2 <= p < 1 << 24 for p in row['primes']) and
             len(set(row['primes'])) == len(row['primes']), 'audit prime list')
        need(int(row['difference_bound']) >= 0 and math.prod(row['primes']) == int(row['CRT_product']) and
             int(row['CRT_product']) > 2 * int(row['difference_bound']), 'audit CRT bound')
        for prime, check in zip(row['primes'], row['checks']):
            need(check['all_entries_match'] is True and type(check['entries']) is int and
                 check['entries'] == sizes[name] and type(check['matching_entries']) is int and
                 check['matching_entries'] == check['entries'] and check['prime'] == prime and
                 check['trial_division_prime_proved'] is True and
                 all(0 <= int(x) < 1 << 63 for x in check['maximum_int64_dot_sums']), 'audit entry mismatch')
    scalar = report['scalar_checks']
    keys(scalar['gates'], GATES)
    need(all(type(value) is bool and value for value in scalar['gates'].values()), 'audit scalar gate types')
    need(scalar['independently_derived_status'] == NUMERIC_PASS and scalar['gates'] == cert['gates'] and
         scalar['metrics'] == cert['metrics'] and scalar['bounds'] == cert['bounds'], 'audit scalar/result mismatch')
    need(type(report['physical_promotion']) is int and report['physical_promotion'] == 0 and
         zero_integer(report['prior_certificate_mathematical_premises']) and zero_integer(report['new_estimator_calls']) and
         report['external_review'] == 'PENDING',
         'audit scope')


def dump(path, value):
    with path.open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


def child(role, command, out, timeout):
    env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}
    started = time.perf_counter()
    try:
        r = subprocess.run(command, env=env, capture_output=True, text=True, timeout=timeout)
        entry = {'role': role, 'returncode': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr,
                 'timed_out': False}
    except subprocess.TimeoutExpired as exc:
        entry = {'role': role, 'returncode': None, 'stdout': str(exc.stdout or ''),
                 'stderr': str(exc.stderr or ''), 'timed_out': True}
    dump(out / (role + '_PROCESS.json'), {**entry, 'elapsed_seconds': time.perf_counter() - started})
    return entry


def run(repo, manifest, output):
    started = time.perf_counter()
    repo, manifest = clean(repo), clean(manifest)
    config, paths = source_check(repo)
    protocol = load(HERE / 'PROTOCOL.json')
    out = guard_output(output, repo, (manifest,))
    # Reuse the pinned intake before creating any output; no fit/SVD occurs here.
    module_spec = importlib.util.spec_from_file_location('pinned_submission_preflight', paths['numerical'])
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    numeric_protocol = module.read_json(paths['numerical'].parent / 'PROTOCOL.json')
    prepared = module.intake(manifest, out / 'numerical', numeric_protocol)
    out = guard_output(out, repo, (manifest, *prepared['files']))
    expected = {'manifest_sha256': prepared['manifest_hash'], 'payload_sha256': prepared['payload_hash'],
                'dimensions': {key: prepared[key] for key in ('m', 'n', 'q')},
                'denominator_bits': prepared['bN'], 'record_npy_sha256': prepared['spec']['record']['sha256'],
                'input_hashes': {manifest: prepared['manifest_hash'],
                                 **{p: row['sha256'] for p, row in zip(prepared['files'], prepared['file_rows'])}},
                'identity_seal_sha256': sha(paths['identity'].parent / 'SEAL.json'),
                'identity_protocol_sha256': sha(paths['identity'].parent / 'PROTOCOL.json'),
                'catalog_sha256': sha(paths['identity'].parent / 'KNOWN_RECORDS.json'),
                'numerical_seal_sha256': sha(paths['numerical'].parent / 'SEAL.json'),
                'numerical_protocol_sha256': sha(paths['numerical'].parent / 'PROTOCOL.json'),
                'audit_freeze_sha256': sha(paths['audit'].parent / 'FREEZE.json')}
    catalog = load(paths['identity'].parent / 'KNOWN_RECORDS.json')
    expected['catalog_fingerprint_ids'] = {}
    for row in catalog['records']:
        expected['catalog_fingerprint_ids'].setdefault(row['fingerprint_sha256'], []).append(row['record_id'])
    expected['catalog_coverage'] = catalog['coverage']
    record = prepared['files'][0]
    del prepared
    gc.collect()
    need(same_inputs(expected), 'input changed after preflight')
    source_check(repo)
    out.mkdir(parents=True, exist_ok=False)
    steps = []
    status = 'HOLD_PIPELINE'
    stage = 'identity'
    reason = None
    artifacts = {}
    try:
        commands = {
            'identity': [sys.executable, str(paths['identity']), '--record', str(record), '--denominator-bits',
                         str(expected['denominator_bits']), '--known', str(paths['identity'].parent / 'KNOWN_RECORDS.json'),
                         '--out', str(out / 'identity')],
            'numerical': [sys.executable, str(paths['numerical']), '--manifest', str(manifest), '--out', str(out / 'numerical')],
            'audit': [sys.executable, str(paths['audit']), '--manifest', str(manifest),
                      '--witness', str(out / 'numerical/WITNESS.json.gz'),
                      '--certificate', str(out / 'numerical/CERTIFICATE.json'), '--out', str(out / 'audit')]}
        for stage in ('identity', 'numerical', 'audit'):
            source_check(repo)
            need(same_inputs(expected), 'input changed before ' + stage)
            step = child(stage, commands[stage], out, protocol['child_timeout_seconds'])
            steps.append({key: step[key] for key in ('role', 'returncode', 'timed_out')})
            need(not step['timed_out'] and step['returncode'] == 0, stage + ' child failed or held')
            if stage == 'identity':
                identity = load(out / 'identity/SCREEN.json')
                validate_identity(identity, expected)
                artifacts['identity/SCREEN.json'] = sha(out / 'identity/SCREEN.json')
            elif stage == 'numerical':
                cert = load(out / 'numerical/CERTIFICATE.json')
                validate_numerical(cert, expected)
                witness_hash = sha(out / 'numerical/WITNESS.json.gz')
                certificate_hash = sha(out / 'numerical/CERTIFICATE.json')
                need(cert['witness_sha256'] == witness_hash, 'numerical witness hash')
                artifacts.update({'numerical/CERTIFICATE.json': certificate_hash,
                                  'numerical/WITNESS.json.gz': witness_hash})
            else:
                audit = load(out / 'audit/CERTIFICATE.json')
                validate_audit(audit, expected, cert, witness_hash, certificate_hash)
                artifacts['audit/CERTIFICATE.json'] = sha(out / 'audit/CERTIFICATE.json')
        status = 'NUMERICAL_PASS_PROVENANCE_HOLD'
    except Exception as exc:
        status = 'HOLD_' + stage.upper() + '_STEP'
        reason = type(exc).__name__ + ': ' + str(exc)
    try:
        source_check(repo)
        need(same_inputs(expected), 'input changed at endpoint')
        need(all(sha(out / name) == digest for name, digest in artifacts.items()), 'stage artifact changed at endpoint')
    except Exception as exc:
        status, reason = 'HOLD_BINDING_CHANGE', type(exc).__name__ + ': ' + str(exc)
    passed = status == 'NUMERICAL_PASS_PROVENANCE_HOLD'
    rollup = {**PROVENANCE, 'schema_version': '1.0', 'workflow_status': status, 'reason': reason,
              'numerical_status': 'CERTIFIED_WITH_DISTINCT_PRODUCT_AUDIT' if passed else 'NOT_ACCEPTED_BY_HANDOFF',
              'identity_relation': identity['identity_relation'] if 'identity' in locals() else 'NOT_COMPLETED',
              'manifest_sha256': expected['manifest_sha256'], 'record_payload_sha256': expected['payload_sha256'],
              'dimensions': expected['dimensions'], 'stages_invoked': steps, 'artifacts_sha256': artifacts,
              'runner_seal_sha256': sha(HERE / 'SEAL.json'), 'dependencies_sha256': sha(HERE / 'DEPENDENCIES.json'),
              'new_estimator_calls': 0, 'input_stability_premise': 'Stable supplied inputs and stage artifacts during execution; endpoint hashes are not atomic snapshots',
              'scope': 'Finite supplied-record numerical handoff only; no acquisition/preparation/unit/physical correspondence established'}
    dump(out / 'ROLLUP.json', rollup)
    dump(out / 'RESOURCE.json', {'elapsed_seconds': time.perf_counter() - started,
                               'scope': 'Pinned identity, precomputed-factor numerical verification and distinct audit; no end-to-end acquisition/Hankel benchmark'})
    print(json.dumps({'workflow_status': status, 'provenance_status': rollup['provenance_status'],
                      'stages_invoked': [step['role'] for step in steps], 'reason': reason}), flush=True)
    return 0 if passed else 2


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--repo', required=True)
    p.add_argument('--manifest', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    try:
        return run(Path(args.repo), Path(args.manifest), Path(args.out))
    except Exception as exc:
        print(json.dumps({**PROVENANCE, 'workflow_status': 'HOLD_INTAKE_OR_SETUP',
                          'reason': type(exc).__name__ + ': ' + str(exc)}), flush=True)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
