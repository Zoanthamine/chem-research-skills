"""Install the six chemistry/research skills for Codex or DeepSeek Harness.

What it does, in order: verify the release against MANIFEST.json, copy the six
skill folders, write an install marker, and add one managed block of default
routing rules to the host's AGENTS.md (backing up that file first). Nothing else
is modified and no scientific software is downloaded.

Typical use::

    python install.py --check                  # integrity only, writes nothing
    python install.py --host dsh --dry-run     # show the plan
    python install.py --host dsh               # install
    python install.py --host both --smoke      # Codex + DSH, then self-check
    python install.py --host auto              # install into detected hosts

Existing skills whose content differs are never overwritten without --replace;
--replace first moves them into chemistry-skill-backups/<timestamp>/.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys

NAMES = [
    'scxrd-refinement',
    'huangjt-computational-chemistry',
    'huangjt-spectral-structure-analysis',
    'organic-chemistry-reasoning',
    'huangjt-academic-research',
    'huangjt-academic-writing',
]
BEGIN = '<!-- huangjt-chemistry-defaults:begin -->'
END = '<!-- huangjt-chemistry-defaults:end -->'


def fingerprint(root):
    h = hashlib.sha256()
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts:
            h.update(p.relative_to(root).as_posix().encode())
            h.update(hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()


def verify(root):
    records = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
    expected = set()
    for row in records:
        p = (root / row['path']).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file():
            raise ValueError('Missing/unsafe file: ' + row['path'])
        content = p.read_bytes()
        if row.get('normalize_lf'):
            content = content.replace(b'\r\n', b'\n')
        if hashlib.sha256(content).hexdigest() != row['sha256']:
            raise ValueError('Checksum mismatch: ' + row['path'])
        expected.add(p)
    excluded = {'.git', '__pycache__', '.venv'}
    actual = {
        p.resolve() for p in root.rglob('*')
        if p.is_file()
        and p != root / 'MANIFEST.json'
        and not any(part in excluded for part in p.relative_to(root).parts)
    }
    if actual != expected:
        raise ValueError('Unexpected package files; use a clean checkout or release extraction')
    for name in NAMES:
        if not (root / 'skills' / name / 'SKILL.md').is_file():
            raise ValueError('Missing skill: ' + name)
    nested = list((root / 'skills').rglob('SKILL.md'))
    if len(nested) != 6:
        raise ValueError('Expected exactly six registered skills')
    return len(records)


def _arg(args, name, default=None):
    return getattr(args, name, default)


def profile(host, args):
    if host == 'codex':
        # Codex's standard user skill directory is AGENTS_HOME/skills.
        agent_home = Path(os.environ.get('AGENTS_HOME', str(Path.home() / '.agents'))).expanduser()
        codex_home = Path(_arg(args, 'codex_home') or os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))).expanduser()
        target = Path(args.target).expanduser() if _arg(args, 'target') else agent_home / 'skills'
        return target, codex_home / 'AGENTS.md'
    dsh_home = Path(_arg(args, 'dsh_home') or os.environ.get('DSH_HOME', str(Path.home() / '.dsh'))).expanduser()
    target = Path(args.target).expanduser() if _arg(args, 'target') else dsh_home / 'skills'
    return target, dsh_home / 'AGENTS.md'


def detect_hosts(args):
    """Return hosts whose home directory already exists, DSH first."""
    found = []
    for host in ('dsh', 'codex'):
        target, instructions = profile(host, args)
        home = instructions.parent
        if home.is_dir() or target.is_dir():
            found.append(host)
    return found


def route_block(root, template):
    return BEGIN + '\n' + template.replace('{{SKILL_ROOT}}', root.resolve().as_posix()).strip() + '\n' + END + '\n'


def write_defaults(p, root, template, backup):
    existing = p.read_text(encoding='utf-8-sig') if p.exists() else ''
    block = route_block(root, template)
    if BEGIN in existing:
        if END not in existing:
            raise ValueError('Incomplete managed global block: ' + str(p))
        updated = re.sub(re.escape(BEGIN) + r'[\s\S]*?' + re.escape(END) + r'\n?', lambda _: block, existing, count=1)
    else:
        updated = block + '\n' + existing
    if updated == existing:
        return False
    if p.exists():
        target = backup / 'instructions' / p.parent.name / p.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(updated, encoding='utf-8')
    return True


def plan(root, targets, args):
    """Describe what install() would do, without writing anything."""
    actions = []
    for host, (target, instructions) in targets:
        target = target.resolve()
        for name in NAMES:
            dst = target / name
            status = 'create'
            if dst.exists():
                same = fingerprint(dst) == fingerprint(root / 'skills' / name)
                if same:
                    status = 'identical'
                elif not _arg(args, 'replace'):
                    raise FileExistsError(
                        'Existing different skill; compare first, or use --replace to back it up: ' + str(dst))
                else:
                    status = 'replace'
            actions.append({'host': host, 'skills': str(target), 'skill': name, 'status': status})
        if instructions.exists():
            text = instructions.read_text(encoding='utf-8-sig')
            if BEGIN in text and END not in text:
                raise ValueError('Incomplete managed instruction block: ' + str(instructions))
    return actions


def install(root, targets, args):
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    actions = []
    for host, (target, instructions) in targets:
        target = target.resolve()
        marker = target / '.huangjt-chemistry-install.json'
        if marker.exists():  # reading the marker is not required, but proves the format stays valid
            json.loads(marker.read_text(encoding='utf-8'))
        for name in NAMES:
            dst = target / name
            if dst.exists():
                same = fingerprint(dst) == fingerprint(root / 'skills' / name)
                if not same and not _arg(args, 'replace'):
                    raise FileExistsError(
                        'Existing different skill; compare first, or use --replace to back it up: ' + str(dst))
            actions.append((host, target, instructions, name))
        if instructions.exists():
            text = instructions.read_text(encoding='utf-8-sig')
            if BEGIN in text and END not in text:
                raise ValueError('Incomplete managed instruction block: ' + str(instructions))
    backups = {}
    for host, target, instructions, name in actions:
        backup = backups.setdefault(str(target), target.parent / 'chemistry-skill-backups' / stamp)
        if not backup.resolve().is_relative_to(target.parent.resolve()):
            raise ValueError('Backup escapes the selected installation parent')
        dst = target / name
        src = root / 'skills' / name
        if dst.exists() and fingerprint(dst) == fingerprint(src):
            continue
        target.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            if dst.parent.resolve() != target:
                raise ValueError('Unsafe target parent')
            archived = backup / 'skills' / name
            if not archived.resolve().is_relative_to(backup.resolve()):
                raise ValueError('Unsafe backup target')
            archived.parent.mkdir(parents=True, exist_ok=True)
            dst.rename(archived)
        shutil.copytree(src, dst)
    for host, (target, instructions) in targets:
        target = target.resolve()
        backup = backups[str(target)]
        marker = {
            'package': 'huangjt-chemistry-skills',
            'version': (root / 'VERSION').read_text(encoding='utf-8').strip() if (root / 'VERSION').exists() else 'unversioned',
            'host': host,
            'fingerprints': {n: fingerprint(target / n) for n in NAMES},
        }
        (target / '.huangjt-chemistry-install.json').write_text(
            json.dumps(marker, ensure_ascii=False, indent=2), encoding='utf-8')
        if not _arg(args, 'no_defaults'):
            write_defaults(instructions, target, (root / 'routing/global-defaults.md').read_text(encoding='utf-8'), backup)
    return [{'host': host, 'skills': str(target.resolve()), 'global_instructions': str(instructions),
             'defaults_installed': not _arg(args, 'no_defaults')} for host, (target, instructions) in targets]


def smoke(root, targets, no_defaults=False):
    """Post-install checks that need no scientific software."""
    checks = []
    for host, (target, instructions) in targets:
        target = target.resolve()
        skill_files = [p for p in target.glob('*/SKILL.md')]
        checks.append({'host': host, 'check': 'six skill entries', 'ok': len(skill_files) == 6,
                       'detail': f'{len(skill_files)}/6'})
        marker = target / '.huangjt-chemistry-install.json'
        version = None
        if marker.is_file():
            version = json.loads(marker.read_text(encoding='utf-8')).get('version')
        expected = (root / 'VERSION').read_text(encoding='utf-8').strip() if (root / 'VERSION').exists() else None
        checks.append({'host': host, 'check': 'install marker version', 'ok': version == expected,
                       'detail': f'{version} vs {expected}'})
        if no_defaults:
            checks.append({'host': host, 'check': 'managed defaults block', 'ok': True,
                           'detail': 'skipped (--no-defaults)'})
        else:
            count = None
            if instructions.is_file():
                count = instructions.read_text(encoding='utf-8-sig').count(BEGIN)
            checks.append({'host': host, 'check': 'managed defaults block', 'ok': count == 1,
                           'detail': f'{count} block(s)'})
    return checks


def print_summary(results, checks):
    print('已安装：')
    for row in results:
        print(f"  {row['host']:6s} {row['skills']}")
        print(f"         全局规则 {row['global_instructions']} "
              f"({'已写入' if row['defaults_installed'] else '未写入'})")
    if checks:
        print('自检：')
        for check in checks:
            print(f"  [{'OK' if check['ok'] else 'FAIL'}] {check['host']} {check['check']} ({check['detail']})")
    print('下一步：')
    print('  python tools/doctor.py            # 环境与后端自检（只读）')
    print('  python tools/workbench.py setup --profile foundation --apply')
    print('  新开一个会话，然后直接说：修单晶 / 算核磁 / 解谱 / 有机 / 找文献 / 写作')


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    root = Path(__file__).resolve().parent
    version_file = root / 'VERSION'
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--host', choices=['codex', 'dsh', 'both', 'auto'], default='codex',
                        help='target host; auto = installed-looking hosts, DSH first (default: codex)')
    parser.add_argument('--target', help='explicit skill directory; use with a single host')
    parser.add_argument('--codex-home')
    parser.add_argument('--dsh-home')
    parser.add_argument('--check', action='store_true', help='verify the package only; print JSON; install nothing')
    parser.add_argument('--dry-run', action='store_true', help='show the plan; write nothing')
    parser.add_argument('--smoke', action='store_true', help='run post-install checks that need no science software')
    parser.add_argument('--replace', action='store_true', help='back up different existing skills, then replace them')
    parser.add_argument('--no-defaults', action='store_true', help='install skills without the managed AGENTS.md block')
    parser.add_argument('--json', action='store_true', help='machine-readable output')
    parser.add_argument('--version', action='version',
                        version=version_file.read_text(encoding='utf-8').strip() if version_file.exists() else 'unversioned')
    args = parser.parse_args(argv)

    count = verify(root)
    if args.check:
        print(json.dumps({'verified_files': count, 'skills': NAMES, 'installed': False}))
        return 0

    if args.host == 'both' and args.target:
        parser.error('--target requires a single host')
    if args.host == 'auto':
        hosts = detect_hosts(args)
        if not hosts:
            parser.error('no DSH/Codex home detected; pass --host dsh|codex with --target')
    else:
        hosts = ['codex', 'dsh'] if args.host == 'both' else [args.host]
    targets = [(h, profile(h, args)) for h in hosts]
    for _, (target, _) in targets:
        if target.resolve() == root:
            parser.error('refusing to install into the package directory itself')

    if args.dry_run:
        actions = plan(root, targets, args)
        payload = {'verified_files': count, 'dry_run': True,
                   'targets': [{'host': h, 'skills': str(t.resolve())} for h, (t, _) in targets],
                   'actions': actions}
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f'包校验通过：{count} 个文件')
            for row in actions:
                print(f"  {row['status']:9s} {row['host']:6s} {row['skill']}")
            print('（未写入任何文件）')
        return 0

    results = install(root, targets, args)
    checks = smoke(root, targets, _arg(args, 'no_defaults')) if args.smoke else []
    if args.json:
        print(json.dumps({'verified_files': count, 'installation': results, 'checks': checks},
                         ensure_ascii=False, indent=2))
    else:
        print_summary(results, checks)
    return 0


if __name__ == '__main__':
    main()