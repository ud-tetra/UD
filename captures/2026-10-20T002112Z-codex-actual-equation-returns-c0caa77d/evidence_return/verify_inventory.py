#!/usr/bin/env python3
"""Read-only inventory check of this requirements packet, never evidence admission.
Uses only packet files and ten explicitly bound repository files. No returned
claims, URLs, raw data, notebooks, fitting code or other external files are opened.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads(path.read_text())


def null_count(value):
    if isinstance(value, dict):
        return sum(null_count(v) for v in value.values())
    if isinstance(value, list):
        return sum(null_count(v) for v in value)
    return int(value is None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    repo = args.repo.resolve()
    freeze = read_json(packet / 'FREEZE.json')
    for item in freeze['frozen_files']:
        path = packet / item['path']
        require(path.parent == packet, 'packet inventory must be flat')
        require(digest(path) == {k: item[k] for k in ('bytes', 'sha256')}, item['path'] + ': frozen bytes differ')
    binding = read_json(packet / 'SOURCE_BINDINGS.json')
    sources = {}
    require(len(binding['inputs']) == 10, 'expected ten pinned sources')
    for item in binding['inputs']:
        rel = Path(item['repository_path'])
        require(not rel.is_absolute() and '..' not in rel.parts, 'unsafe source path')
        path = repo / rel
        require(digest(path) == {k: item[k] for k in ('bytes', 'sha256')}, str(rel) + ': source pin differs')
        sources[item['role']] = path
    original = read_json(sources['blocker_map'])['entries']
    preflight = read_json(sources['original_preflight'])
    cross = read_json(packet / 'BLOCKER_RETURN_CROSSWALK.json')
    entries = cross['entries']
    require(len(entries) == len(original) == 128, 'expected 128 original paths')
    require(len({e['original_path'] for e in entries}) == 128, 'duplicate original path')
    require([(e['original_path'], e['original_blocker']) for e in entries] ==
            [(e['path'], e['original_blocker']) for e in original], 'crosswalk differs from source')
    require([e['original_blocker'] for e in entries] == preflight['blocking_metadata'], 'preflight list differs')
    profile = read_json(packet / 'RETURN_PROFILE.json')
    artifacts = {a['id']: a for a in profile['artifacts']}
    require(list(artifacts) == [f'R{i:02}' for i in range(1, 15)], 'fourteen ordered artifact roles required')
    require(len({a['requested_path'] for a in artifacts.values()}) == 14, 'duplicate return path')
    for artifact in artifacts.values():
        require(artifact['received'] is False and artifact['content_verified'] is False and
                artifact['actual_return_sha256'] is None, 'requirements cannot claim received evidence')
    for entry in entries:
        artifact = artifacts[entry['requested_artifact_id']]
        require(entry['requested_path'] == artifact['requested_path'], 'return path mismatch')
        require(entry['requested_section'] in artifact['required_sections'], 'unknown section')
        for ref in entry['additional_requested_sections']:
            require(ref['section'] in artifacts[ref['artifact_id']]['required_sections'], 'unknown secondary section')
        require(entry['qualification_closed'] is False, 'crosswalk cannot close qualification')
        match = re.search(r'amplitude_channels\[(\d+)\]', entry['original_path'])
        require(entry['actual_channel_if_applicable'] == (int(match.group(1)) + 1 if match else None), 'channel identity mismatch')
    require(Counter(e['actual_channel_if_applicable'] for e in entries if e['actual_channel_if_applicable']) == Counter({i: 8 for i in range(1, 11)}), 'ten channels, eight fields each required')
    require(Counter(e['route_applicability'] for e in entries) == Counter({
        'COMMON_OR_OTHER_EVIDENCE': 120, 'BOTH_JOINT_ROUTES': 4,
        'JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE_ONLY': 3,
        'DETERMINISTIC_SIMULTANEOUS_ENCLOSURE_ONLY': 1}), 'joint-route applicability differs')
    candidate_nulls = null_count(read_json(sources['candidate_request']))
    require(candidate_nulls == cross['candidate_v0_2_null_leaf_count'] == 170, 'candidate field count differs')
    require(cross['null_leaves_are_independent_blockers'] is False and
            cross['original_128_paths_are_independent_gates'] is False and
            profile['original_128_paths_are_independent_gates'] is False, 'field counts are not independent gates')
    receipt = read_json(packet / 'EXTERNAL_RETURN_RECEIPT_TEMPLATE.json')
    require(receipt['status'] == 'BLANK_NOT_A_REVIEW', 'blank template status required')
    require([a['id'] for a in receipt['reviewed_artifacts']] == [f'R{i:02}' for i in range(1, 14)], 'R14 must not self-review')
    for item in receipt['reviewed_artifacts']:
        require(all(value is None for key, value in item.items() if key != 'id'), 'actual external review fields must stay blank')
    require(receipt['review_return_artifact']['id'] == 'R14' and
            receipt['review_return_artifact']['self_hash_required'] is False and
            receipt['review_return_artifact']['reviewer_independent_review_of_own_statement_required'] is False,
            'receipt must avoid self-hash/self-review')
    for key in ('source_identity', 'analysis_lane', 'reviewer_identity', 'reviewer_independence_and_conflicts',
                'calibration_authority_acceptance', 'review_date_UTC', 'review_commands_versions_logs',
                'all_outcomes_and_HOLDs_retained', 'limitations', 'attributable_verdict', 'custodian_ruling'):
        require(receipt[key] is None, 'blank external field required: ' + key)
    examples = read_json(packet / 'EXAMPLES.json')
    require(len(examples['examples']) == 12 and examples['examples_are_actual_evidence'] is False, 'hypothetical examples only')
    require(all(e['physical_promotion'] == 0 and e['raw_access_authorized'] is False for e in examples['examples']), 'examples confer no authority')
    require(profile['qualification_blockers_closed'] == cross['qualification_blockers_closed'] == receipt['qualification_blockers_closed'] == 0, 'no qualification closure')
    require(profile['raw_access_authorized'] is False and profile['hardware_operation_authorized'] is False and profile['outreach_sent'] is False, 'no authority/outreach')
    require(profile['physical_promotion'] == cross['physical_promotion'] == receipt['physical_promotion'] == 0, 'physical promotion remains zero')
    print(json.dumps({
        'status': 'PASS_STRUCTURAL_RETURN_INVENTORY_NOT_EVIDENCE_ADMISSION',
        'frozen_files_checked': len(freeze['frozen_files']), 'repository_source_pins_checked': len(sources),
        'original_paths_crosswalked': len(entries), 'requested_return_artifact_roles': len(artifacts),
        'candidate_null_leaf_count_not_independent_gates': candidate_nulls,
        'qualification_blockers_closed': 0, 'raw_records_opened': False, 'external_evidence_opened': False,
        'external_review': 'PENDING', 'outreach_sent': False, 'physical_promotion': 0,
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
