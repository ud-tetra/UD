"""Run the exact Python blocks embedded in the five preserved C06 proofs."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("evidence", type=Path)
args = parser.parse_args()
reports = sorted(args.evidence.glob("*UD_C06_*_v0.*.md"),
                 key=lambda report: report.stem.rsplit("_v", 1)[1])
assert [report.stem.rsplit("_v", 1)[1] for report in reports] == [
    "0.1", "0.2", "0.3", "0.4", "0.5"
]
results = []
with tempfile.TemporaryDirectory() as temp:
    for report in reports:
        block, = re.findall(r"^```python\n(.*?)^```$", report.read_text(), re.M | re.S)
        script = Path(temp) / "replay.py"
        script.write_text(block)
        replay = subprocess.run([sys.executable, str(script)], text=True,
                                capture_output=True, check=True)
        assert replay.stdout.startswith("PASS"), replay.stdout
        results.append({
            "file": report.name[4:] if re.match(r"^\d{3}-", report.name) else report.name,
            "sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
            "result": replay.stdout.strip(),
        })
print(json.dumps({"status": "PASS_EXACT", "relationship": "constructor replay",
                  "physical_promotion": 0, "results": results}, indent=2))
