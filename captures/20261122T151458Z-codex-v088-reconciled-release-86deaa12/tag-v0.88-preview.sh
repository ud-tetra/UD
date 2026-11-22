#!/usr/bin/env bash
# Run from a clone of ud-tetra/UD after the release gate clears.
# Usage: bash tag-v0.88-preview.sh GITHUB_REVIEWER [--push]
set -euo pipefail

repo=ud-tetra/UD
remote="https://github.com/$repo.git"
tag=v0.88-preview
ref="refs/tags/$tag"
reviewer=$(printf '%s' "${1:-}" | tr '[:upper:]' '[:lower:]')
mode="${2:-}"

die() { printf 'Release preflight: %s\n' "$*" >&2; exit 1; }

[[ $# -ge 1 && $# -le 2 && "$reviewer" =~ ^[a-z0-9][a-z0-9-]*$ ]] ||
    die "Usage: bash tag-v0.88-preview.sh GITHUB_REVIEWER [--push]"
[[ -z "$mode" || "$mode" == --push ]] || die "Unknown option: $mode"
command -v gh >/dev/null && command -v jq >/dev/null && command -v python3 >/dev/null || die "Install gh, jq, and Python 3."
git rev-parse --git-dir >/dev/null
gh auth status --hostname github.com >/dev/null 2>&1 ||
    die "Authenticate gh with your GitHub account first."

github_git() {
    git -c credential.helper= -c 'credential.helper=!gh auth git-credential' "$@"
}

technical_merges=()
for pr in 595 596 597 598 599 600 601 602 603; do
    data=$(gh api --hostname github.com "repos/$repo/pulls/$pr")
    merge=$(jq -er '
        select(.merged == true and .base.ref == "main"
               and (.base.repo.full_name | ascii_downcase) == "ud-tetra/ud")
        | .merge_commit_sha | select(test("^[a-f0-9]{40}$"))
    ' <<<"$data") || die "PR #$pr must be merged into $repo:main."
    if (( pr < 602 )); then
        head=$(jq -er '.head.sha | select(test("^[a-f0-9]{40}$"))' <<<"$data")
        author=$(jq -er '.user.login | ascii_downcase' <<<"$data")
        [[ "$reviewer" != "$author" ]] || die "PR #$pr author cannot satisfy independent review."
        gh api --hostname github.com --paginate "repos/$repo/pulls/$pr/reviews?per_page=100" |
            jq -es --arg reviewer "$reviewer" --arg head "$head" '
                add
                | map(select((.user.login // "" | ascii_downcase) == $reviewer
                             and .state != "COMMENTED" and .state != "PENDING"))
                | sort_by(.submitted_at, .id)
                | last
                | .state == "APPROVED" and .commit_id == $head
                  and ((.body // "") | contains("APPROVED_WITH_SCOPE_LOCKS"))
            ' >/dev/null || die "PR #$pr lacks the required approval from @$reviewer on $head."
        technical_merges+=("$merge")
    elif (( pr == 602 )); then
        notes_merge="$merge"
    else
        target="$merge"
    fi
done

github_git fetch --no-tags "$remote" refs/heads/main
main=$(git rev-parse 'FETCH_HEAD^{commit}')
git merge-base --is-ancestor "$target" "$main" ||
    die "PR #603's merge commit is not reachable from GitHub main."
for merge in "${technical_merges[@]}"; do
    git merge-base --is-ancestor "$merge" "$target" ||
        die "PR #603's merge commit does not contain technical merge $merge."
done

git merge-base --is-ancestor "$notes_merge" "$target" ||
    die "PR #603's merge commit does not contain the milestone notes."
manifest="captures/20261122T151458Z-codex-v088-reconciled-release-86deaa12/UD-v0.88-preview-MANIFEST.json"
digest=$(python3 - "$target" "$manifest" <<'PYVERIFY'
import hashlib, json, subprocess, sys
target, path = sys.argv[1:]
def blob(p):
    return subprocess.check_output(["git", "show", f"{target}:{p}"])
raw = blob(path)
data = json.loads(raw)
if data["physical_promotion"] != 0 or [r["pr"] for r in data["technical"]] != list(range(595, 602)):
    raise SystemExit("Invalid release manifest scope")
for entry in data["files"]:
    payload = blob(entry["path"])
    if len(payload) != entry["size_bytes"] or hashlib.sha256(payload).hexdigest() != entry["sha256"]:
        raise SystemExit(f"Manifest mismatch: {entry['path']}")
print(hashlib.sha256(raw).hexdigest())
PYVERIFY
)

if git show-ref --verify --quiet "$ref"; then
    [[ "$(git cat-file -t "$ref")" == tag &&
       "$(git rev-parse "$ref^{commit}")" == "$target" ]] ||
        die "Existing local tag conflicts with verified target $target."
fi
if remote_tag=$(github_git ls-remote --exit-code --refs "$remote" "$ref"); then
    [[ -n "$remote_tag" ]] || die "Remote returned an empty tag record."
    die "Remote tag $tag already exists. No replacement attempted."
else
    status=$?
    [[ "$status" -eq 2 ]] || die "Could not verify whether the remote tag exists."
fi

printf 'Verified target %s (merge of PR #603)\n' "$target"
printf 'Push command: git -c credential.helper= -c '\''credential.helper=!gh auth git-credential'\'' push %s %s:%s\n' "$remote" "$ref" "$ref"
if [[ "$mode" != --push ]]; then
    printf 'Dry run complete. Pass --push to create and push the annotated tag.\n'
    exit 0
fi

if ! git show-ref --verify --quiet "$ref"; then
    git tag -a "$tag" "$target" -F - <<ANNOTATION
Unified Dynamics v0.88-preview

CYCLE-088 PB3/PB5 spectral relaxation milestone
Review scope: APPROVED_WITH_SCOPE_LOCKS on PRs #595–#601 by @$reviewer
Release notes: ud-tetra/UD PR #602
Release reconciliation: ud-tetra/UD PR #603
Release commit: $target
Manifest: $manifest
Manifest SHA-256: $digest
Physical Promotion = 0
ANNOTATION
fi
github_git push "$remote" "$ref:$ref"
pushed=$(github_git ls-remote --exit-code --refs "$remote" "$ref")
[[ "$pushed" == "$(git rev-parse "$ref")"$'\t'"$ref" ]] ||
    die "Remote tag object differs from the local annotated tag."
printf 'Verified remote annotated tag %s at %s\n' "$tag" "$target"
