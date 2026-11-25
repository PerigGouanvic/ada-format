#!/usr/bin/env python3
"""Validate .ada files against the v0.1 schema and check internal references.

Usage: python3 tools/validate.py FILE.ada [FILE.ada ...]
Requires: pyyaml, jsonschema
"""
import json, sys, pathlib
import yaml, jsonschema

SCHEMA = json.loads((pathlib.Path(__file__).parent.parent / "spec" / "ada-v0.1.schema.json").read_text())

def refs(doc):
    ids = {s["id"] for s in doc.get("sections", [])}
    cids = {c["id"] for c in doc.get("concepts", [])}
    out = []
    for c in doc.get("concepts", []):
        out += [("concept " + c["id"] + ".requires", r, cids) for r in c.get("requires", [])]
    for s in doc.get("sections", []):
        out += [("section " + s["id"] + ".uses", r, cids) for r in s.get("uses", [])]
        out += [("section " + s["id"] + ".links", l["to"], ids) for l in s.get("links", [])]
    for a in doc.get("intent", {}).get("audiences", []):
        out += [("audience " + a["id"] + ".start_with", r, ids) for r in a.get("start_with", [])]
    for i, q in enumerate(doc.get("questions", [])):
        out += [(f"questions[{i}].see", r, ids) for r in q.get("see", [])]
    de = doc.get("decoder", {}).get("default_entry")
    if de:
        out.append(("decoder.default_entry", de, ids))
    return [f"{where}: unknown id '{r}'" for where, r, pool in out if r not in pool]

def check(path):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    errs = [e.message + " at " + "/".join(map(str, e.path)) for e in jsonschema.Draft202012Validator(SCHEMA).iter_errors(doc)]
    if not errs:
        errs = refs(doc)
    print(("OK   " if not errs else "FAIL ") + str(path))
    for e in errs:
        print("     " + e)
    return not errs

if __name__ == "__main__":
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
