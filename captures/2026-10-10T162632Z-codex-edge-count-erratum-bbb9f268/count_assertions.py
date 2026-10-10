#!/usr/bin/env python3
"""Count evaluated assert expressions in the frozen v0.1 verifier."""
import ast
import hashlib
import json
import pathlib
import sys

EXPECTED_SHA256 = "e5a5200c1dbc5817ccebadc3dc81592fb661885752444eb7fbc0eaba6afb902d"


class CountAsserts(ast.NodeTransformer):
    def visit_Assert(self, node):
        return ast.copy_location(
            ast.Expr(value=ast.Call(func=ast.Name(id="_checked", ctx=ast.Load()),
                                    args=[self.visit(node.test)], keywords=[])), node)


def main(path):
    data = pathlib.Path(path).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"Wrong verifier SHA-256: {digest}")
    count = 0

    def checked(value):
        nonlocal count
        count += 1
        if not value:
            raise AssertionError(f"Assertion {count} failed")

    tree = CountAsserts().visit(ast.parse(data, filename=str(path)))
    ast.fix_missing_locations(tree)
    exec(compile(tree, str(path), "exec"), {"__name__": "__main__", "_checked": checked})
    assert count == 1837
    print(json.dumps({"verifier_sha256": digest, "evaluated_assert_expressions": count,
                      "old_manual_checks_field": 1551, "physical_promotion": 0}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: count_assertions.py PATH_TO_FROZEN_VERIFY_PY")
    main(sys.argv[1])
