"""Offline smoke test for a fresh install — no scientific software required.

Runs the checks a new user can run immediately after installing:

1. package integrity (MANIFEST.json)
2. six skill entries present and non-empty
3. the module index answers a query (workbench.py search)
4. the structure CLI exposes its help (no RDKit import needed)

Usage:
    python examples/quickstart_smoke.py
    python examples/quickstart_smoke.py --installed-skills ~/.dsh/skills
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = [
    'scxrd-refinement',
    'huangjt-computational-chemistry',
    'huangjt-spectral-structure-analysis',
    'organic-chemistry-reasoning',
    'huangjt-academic-research',
    'huangjt-academic-writing',
]


def check_manifest() -> tuple[bool, str]:
    try:
        spec = __import__('importlib.util').util.spec_from_file_location('installer', ROOT / 'install.py')
        module = __import__('importlib.util').util.module_from_spec(spec)
        spec.loader.exec_module(module)
        count = module.verify(ROOT)
        return True, f'{count} 个文件通过校验'
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def check_skills(base: Path) -> tuple[bool, str]:
    found = [name for name in NAMES if (base / name / 'SKILL.md').is_file()]
    empty = [name for name in found if (base / name / 'SKILL.md').stat().st_size == 0]
    if empty:
        return False, '空的 SKILL.md: ' + ', '.join(empty)
    return len(found) == 6, f'{len(found)}/6 个入口可读'


def run_json(command: list[str]) -> tuple[bool, str]:
    try:
        proc = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    if proc.returncode != 0:
        return False, (proc.stderr or proc.stdout).strip()[:200]
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return True, proc.stdout.strip()[:120]
    if isinstance(payload, list):
        return True, f'返回 {len(payload)} 条结果'
    return True, '返回 JSON'


def run_help(command: list[str]) -> tuple[bool, str]:
    try:
        proc = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    first = (proc.stdout or proc.stderr).strip().splitlines()
    return proc.returncode == 0, (first[0] if first else 'no output')[:120]


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed-skills', help='also check an installed skills directory')
    args = parser.parse_args(argv)
    python = sys.executable

    checks = [
        ('包完整性', check_manifest()),
        ('技能入口', check_skills(ROOT / 'skills')),
        ('模块索引', run_json([python, str(ROOT / 'tools' / 'workbench.py'), 'search', 'nmr'])),
        ('结构 CLI', run_help([python, str(ROOT / 'skills' / 'organic-chemistry-reasoning' / 'scripts' / 'structure_cli.py'), '--help'])),
    ]
    if args.installed_skills:
        checks.append(('已安装技能', check_skills(Path(args.installed_skills).expanduser())))

    failed = 0
    for label, (ok, detail) in checks:
        print(f"[{'OK' if ok else 'FAIL'}] {label}: {detail}")
        failed += 0 if ok else 1
    if failed:
        print('\n有检查未通过。先运行 python install.py --check 和 python tools/doctor.py。')
        return 1
    print('\n全部通过：这份包可以安装，安装后六个入口可被发现。')
    print('下一步：python install.py --host dsh --dry-run')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())