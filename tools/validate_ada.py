#!/usr/bin/env python3
"""Check that .ada archives conform to format v0.1 (see spec/ada-v0.1.md, section 7).

Usage: python3 tools/validate_ada.py FILE.ada [FILE.ada ...]
Requires: jsonschema
"""
import json
import pathlib
import sys
import zipfile

import jsonschema

SCHEMA = json.loads(
    (pathlib.Path(__file__).resolve().parent.parent / "spec" / "manifest-v0.1.schema.json").read_text()
)
REQUIRED = ["manifest.json", "ada-usage.md"]


def check(path):
    errors, notes = [], []
    if not str(path).endswith((".ada", ".ada.zip")):
        errors.append("extension is neither .ada nor .ada.zip")
    try:
        z = zipfile.ZipFile(path)
    except (zipfile.BadZipFile, FileNotFoundError) as e:
        return report(path, [f"not a readable zip archive ({e})"], notes)
    names = set(z.namelist())
    errors += [f"missing {n} at the archive root" for n in REQUIRED if n not in names]
    mode = None
    if "manifest.json" in names:
        try:
            mode = json.loads(z.read("manifest.json").decode("utf-8")).get("mode")
        except Exception:
            pass
    has_deposits = any(n.startswith("deposits/") and not n.endswith("/") for n in names)
    if "prompt.md" not in names:
        if mode == "grown_from_deposits" and has_deposits:
            notes.append("no prompt.md yet: growing file, not ready for readers")
        elif mode == "grown_from_deposits":
            errors.append("grown_from_deposits mode needs prompt.md or a non-empty deposits/")
        else:
            errors.append("missing prompt.md at the archive root")
    if "open_questions.md" not in names:
        notes.append("no open_questions.md (optional)")
    if mode != "grown_from_deposits" and not any(n.startswith("source/") and not n.endswith("/") for n in names):
        notes.append("no original text in source/ (recommended, see spec section 5.1)")
    if "manifest.json" in names:
        try:
            manifest = json.loads(z.read("manifest.json").decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            errors.append(f"manifest.json is not valid UTF-8 JSON ({e})")
        else:
            for e in jsonschema.Draft202012Validator(SCHEMA).iter_errors(manifest):
                where = "/".join(map(str, e.path)) or "(root)"
                errors.append(f"manifest.json {where}: {e.message}")
            ids = {c.get("id") for c in manifest.get("citations", []) if isinstance(c, dict)}
            for c in manifest.get("claims", []) or []:
                for ref in c.get("citations", []) if isinstance(c, dict) else []:
                    if ref not in ids:
                        errors.append(f"claim {c.get('id', c.get('text', '?'))!r} cites unknown id {ref!r}")
    for n in sorted(names):
        if n.endswith((".md", ".json", ".yaml", ".txt")):
            try:
                z.read(n).decode("utf-8")
            except UnicodeDecodeError:
                errors.append(f"{n} is not UTF-8")
    return report(path, errors, notes)


def report(path, errors, notes):
    print(("OK   " if not errors else "FAIL ") + str(path))
    for e in errors:
        print("     error: " + e)
    for n in notes:
        print("     note:  " + n)
    return not errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
