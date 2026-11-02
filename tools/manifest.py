"""Regenerate or verify the package integrity ledger (root MANIFEST.json).

The ledger is what ``install.py --check`` trusts: one record per shipped file with
its LF-normalised byte count and SHA-256. It proves the release archive is the
tree that was tested and packaged; it does not prove that any scientific module
was validated.

Usage:
    python tools/manifest.py --check    # CI: exit 1 when the ledger is stale
    python tools/manifest.py --write    # maintainer: rewrite MANIFEST.json
    python tools/manifest.py --list     # print area statistics only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = 'MANIFEST.json'
# install.py treats these as package metadata, not shipped content.
EXCLUDED_DIRS = {'.git', '__pycache__', '.venv'}


def _excluded(rel_parts: tuple[str, ...]) -> bool:
    return any(part in EXCLUDED_DIRS for part in rel_parts)


def _is_text(raw: bytes) -> bool:
    if b'\x00' in raw:
        return False
    try:
        raw.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True


def record(path: Path, rel: str) -> dict:
    raw = path.read_bytes()
    text = _is_text(raw)
    canonical = raw.replace(b'\r\n', b'\n') if text else raw
    row = {
        'path': rel,
        'bytes': len(canonical),
        'sha256': hashlib.sha256(canonical).hexdigest(),
    }
    if text:
        # Lets a Windows checkout with CRLF produce the same digest.
        row['normalize_lf'] = True
    return row


def collect(root: Path = ROOT) -> list[dict]:
    rows = []
    for path in sorted(root.rglob('*')):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.as_posix() == LEDGER or _excluded(rel.parts):
            continue
        rows.append(record(path, rel.as_posix()))
    rows.sort(key=lambda item: item['path'])
    return rows


def load(path: Path = ROOT / LEDGER) -> list[dict]:
    return json.loads(path.read_text(encoding='utf-8'))


def describe_drift(expected: list[dict], actual: list[dict]) -> list[str]:
    by_path = {row['path']: row for row in actual}
    exp = {row['path']: row for row in expected}
    problems = []
    for rel in sorted(set(exp) - set(by_path)):
        problems.append('missing on disk: ' + rel)
    for rel in sorted(set(by_path) - set(exp)):
        problems.append('not in ledger: ' + rel)
    for rel in sorted(set(exp) & set(by_path)):
        left, right = exp[rel], by_path[rel]
        if left.get('sha256') != right.get('sha256'):
            problems.append('checksum drift: ' + rel)
        elif left.get('bytes') != right.get('bytes'):
            problems.append('size drift: ' + rel)
    return problems


def statistics(rows: list[dict]) -> dict:
    areas: dict[str, int] = {}
    for row in rows:
        parts = row['path'].split('/')
        area = parts[0] if len(parts) > 1 else '(root)'
        if area == 'skills' and len(parts) > 1:
            area = 'skills/' + parts[1]
        areas[area] = areas.get(area, 0) + 1
    return {
        'verified_files': len(rows),
        'total_bytes': sum(row['bytes'] for row in rows),
        'areas': dict(sorted(areas.items())),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='rewrite MANIFEST.json')
    parser.add_argument('--check', action='store_true', help='verify the ledger against the working tree')
    parser.add_argument('--list', action='store_true', help='print per-area statistics')
    parser.add_argument('--json', action='store_true', help='machine-readable output')
    args = parser.parse_args(argv)

    if args.write:
        rows = collect()
        (ROOT / LEDGER).write_text(
            json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(statistics(rows), ensure_ascii=False, indent=2))
        return 0

    expected = load()
    actual = collect()
    stats = statistics(actual)
    problems = describe_drift(expected, actual)

    if args.check:
        if problems:
            for line in problems[:20]:
                print('DRIFT: ' + line, file=sys.stderr)
            print(f'MANIFEST.json is stale ({len(problems)} problems). '
                  'Run: python tools/manifest.py --write', file=sys.stderr)
            return 1
        print(f'manifest OK: {stats["verified_files"]} files, '
              f'{stats["total_bytes"]} bytes')
        return 0

    if args.list:
        if args.json:
            print(json.dumps(stats, ensure_ascii=False, indent=2))
        else:
            for area, count in stats['areas'].items():
                print(f'{count:6d}  {area}')
            print(f'{stats["verified_files"]:6d}  TOTAL')
        return 0

    parser.print_help()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())