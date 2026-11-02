"""Read-only readiness check for a machine that wants to use these skills.

Answers "can this computer run the library, and what should I do next?" without
installing anything, without launching scientific software, and without network
access. Safe to run before and after ``install.py``.

Usage:
    python tools/doctor.py              # human table
    python tools/doctor.py --json       # machine-readable
    python tools/doctor.py --skills-dir D:/skills   # check a specific install
    python tools/doctor.py --strict     # exit 1 when a core check fails
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import platform
import shutil
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
PROFILE_MODULES = {
    'foundation': ['rdkit', 'PIL'],
    'spectra': ['numpy', 'scipy', 'matplotlib', 'nmrglue', 'pyopenms'],
    'thermo-raw': ['pyopenms'],
    'crystal': ['gemmi', 'numpy', 'requests'],
    'documents': ['docx', 'pptx', 'pypdf', 'PIL'],
    'ocsr': ['rdkit', 'PIL'],
}
# (key, label, env vars, executables, why it matters)
EXTERNAL = [
    ('dials', 'DIALS', ['DIALS_BIN'], ['dials'], '单晶：原始帧还原/积分/标度'),
    ('shelx', 'SHELXL/SHELXT', ['SHELXL_EXE', 'SHELXT_EXE'], ['shelxl', 'shelxt'], '单晶：解结构与精修'),
    ('platon', 'PLATON', ['PLATON_EXE'], ['platon'], '单晶：checkCIF 辅助与孪晶检查'),
    ('gaussian', 'Gaussian', ['GAUSSIAN_EXE', 'G16_EXE'], ['g16', 'g09'], '计算：DFT 优化/频率/GIAO'),
    ('orca', 'ORCA', ['ORCA_EXE'], ['orca'], '计算：DFT 备选、耦合常数、ECD'),
    ('xtb', 'xTB', ['CODEX_CHEM_XTB_PATH', 'XTBPATH'], ['xtb'], '计算：半经验采样/预优化'),
    ('gromacs', 'GROMACS', ['GMX_BIN'], ['gmx', 'gmx_mpi'], '计算：MD 构象采样'),
    ('molclus', 'Molclus', ['MOLCLUS_EXE'], ['molclus'], '计算：构象去重与排序'),
    ('multiwfn', 'Multiwfn', ['MULTIWFN_EXE'], ['Multiwfn'], '计算：波函数/轨道分析'),
    ('obabel', 'Open Babel', ['CODEX_CHEM_OBABEL_PATH'], ['obabel'], '结构：格式转换、SMILES'),
    ('thermo', 'ThermoRawFileParser', ['THERMO_RAW_FILE_PARSER'], ['ThermoRawFileParser'], '解谱：Thermo RAW 转 mzML'),
    ('java', 'Java', ['JAVA_HOME'], ['java'], '结构：MolVec 离线识图'),
]


def _short(text: str, limit: int = 70) -> str:
    text = ' '.join(str(text).split())
    return text if len(text) <= limit else text[: limit - 1] + '…'


def find_repo_file(*parts: str) -> Path | None:
    path = ROOT.joinpath(*parts)
    return path if path.exists() else None


def load_installer():
    """Reuse install.py's verifier instead of copying its rules."""
    spec = importlib.util.spec_from_file_location('chem_installer', ROOT / 'install.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def repo_state() -> dict:
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip() if (ROOT / 'VERSION').exists() else 'unknown'
    result = {'root': str(ROOT), 'version': version, 'manifest': 'missing', 'verified_files': 0}
    try:
        installer = load_installer()
        count = installer.verify(ROOT)
        result.update({'manifest': 'ok', 'verified_files': count})
    except Exception as exc:  # noqa: BLE001 - any manifest problem is a finding
        result.update({'manifest': 'error', 'error': _short(exc)})
    return result


def hosts() -> list[dict]:
    found = []
    candidates = [
        ('dsh', Path(os.environ.get('DSH_HOME', Path.home() / '.dsh')), 'AGENTS.md'),
        ('codex', Path(os.environ.get('AGENTS_HOME', Path.home() / '.agents')), None),
    ]
    for host, base, guide in candidates:
        target = base / 'skills'
        found.append({
            'host': host,
            'base': str(base.expanduser()),
            'skills_dir': str(target.expanduser()),
            'detected': base.expanduser().is_dir() or target.expanduser().is_dir(),
            'global_instructions': str((base / guide).expanduser()) if guide else str((Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'AGENTS.md')),
        })
    return found


def installed_state(skills_dir: Path) -> dict:
    marker = skills_dir / '.huangjt-chemistry-install.json'
    info = {'skills_dir': str(skills_dir), 'exists': skills_dir.is_dir(), 'marker': None,
            'found': [], 'missing': [], 'different': []}
    if marker.is_file():
        try:
            info['marker'] = json.loads(marker.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            info['marker'] = {'error': 'unreadable marker'}
    try:
        installer = load_installer()
        fingerprint = installer.fingerprint
    except Exception:  # noqa: BLE001
        fingerprint = None
    for name in NAMES:
        source = ROOT / 'skills' / name
        target = skills_dir / name
        if not target.is_dir():
            info['missing'].append(name)
            continue
        info['found'].append(name)
        if fingerprint and source.is_dir():
            try:
                if fingerprint(target) != fingerprint(source):
                    info['different'].append(name)
            except OSError:
                pass
    block = None
    for candidate in [skills_dir.parent / 'AGENTS.md']:
        if candidate.is_file():
            text = candidate.read_text(encoding='utf-8-sig', errors='replace')
            block = text.count('<!-- huangjt-chemistry-defaults:begin -->')
            break
    info['global_block'] = block
    return info


def python_state() -> dict:
    modules = {}
    for name in sorted({mod for mods in PROFILE_MODULES.values() for mod in mods}):
        try:
            modules[name] = importlib.util.find_spec(name) is not None
        except (ImportError, ValueError):
            modules[name] = False
    return {
        'executable': sys.executable,
        'version': platform.python_version(),
        'supported': sys.version_info >= (3, 11),
        'modules': modules,
        'profiles': {
            profile: {'ready': all(modules.get(mod, False) for mod in mods),
                      'missing': [mod for mod in mods if not modules.get(mod, False)]}
            for profile, mods in PROFILE_MODULES.items()
        },
    }


def external_state() -> list[dict]:
    rows = []
    for key, label, env_names, executables, why in EXTERNAL:
        from_env = next((os.environ[name] for name in env_names if os.environ.get(name)), None)
        found = Path(from_env).exists() if from_env else None
        if found is None:
            for exe in executables:
                located = shutil.which(exe)
                if located:
                    found, from_env = True, located
                    break
        rows.append({'key': key, 'label': label, 'why': why,
                     'available': bool(found), 'path': from_env if found else None})
    return rows


def workbench_state() -> dict:
    candidates = []
    if os.environ.get('CHEM_WORKBENCH_HOME'):
        candidates.append(Path(os.environ['CHEM_WORKBENCH_HOME']))
    for env in ('DSH_HOME', 'CODEX_HOME'):
        if os.environ.get(env):
            candidates.append(Path(os.environ[env]) / 'dependencies' / 'chem-workbench')
    candidates.append(Path.home() / '.local' / 'share' / 'chem-workbench')
    for base in candidates:
        config = base / 'workbench.json'
        if config.is_file():
            try:
                data = json.loads(config.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                return {'config': str(config), 'error': 'unreadable'}
            return {'config': str(config), 'profiles': data.get('profiles', {}),
                    'python': data.get('python')}
    return {'config': None, 'profiles': {}}


def next_steps(report: dict) -> list[str]:
    steps = []
    if report['repo']['manifest'] != 'ok':
        steps.append('在干净目录重新解压发布包：MANIFEST 校验失败，不要继续安装。')
        return steps
    if not report['python']['supported']:
        steps.append('安装 Python 3.11+（3.12 或 3.13 更稳），再运行本检查。')
    if not any(item['detected'] for item in report['hosts']):
        steps.append('未发现 DSH/Codex 目录：先确认宿主，或显式传 --target 到自选技能目录。')
    host = next((item for item in report['hosts'] if item['detected']), report['hosts'][0])
    installed = report['install']
    if installed['missing'] or not installed['exists']:
        steps.append(f"安装六技能：python install.py --host {host['host']} --dry-run 先看计划，再运行同一命令去掉 --dry-run。")
    elif installed['different']:
        steps.append('已安装内容与发布包不同：先比较，确认后再用 --replace（会自动备份）。')
    if installed.get('global_block') in (0, None) and installed['exists']:
        steps.append('全局默认规则未写入：去掉 --no-defaults 重新运行安装器，或手动合并 routing/global-defaults.md。')
    foundation = report['python']['profiles']['foundation']
    if not foundation['ready']:
        steps.append('python tools/workbench.py setup --profile foundation --apply   # 结构式识别/绘制/转换的最小依赖')
    spectra = report['python']['profiles']['spectra']
    if not spectra['ready']:
        steps.append('python tools/workbench.py setup --profile spectra --apply      # NMR/MS 读取与绘图依赖')
    missing = [row['label'] for row in report['external'] if not row['available']]
    if missing:
        steps.append('自备专业软件（按需，未随包分发）：' + '、'.join(missing[:6])
                     + ('…' if len(missing) > 6 else ''))
    if not steps:
        steps.append('检查通过：可以直接开始任务（说“修单晶 / 算核磁 / 解谱 / 有机 / 找文献 / 写作”）。')
    return steps


def build_report(skills_dir: Path | None = None) -> dict:
    host_list = hosts()
    chosen = skills_dir or Path(next((item['skills_dir'] for item in host_list if item['detected']),
                                      host_list[0]['skills_dir']))
    report = {
        'tool': 'chem-research-skills doctor',
        'repo': repo_state(),
        'os': {'platform': platform.platform(), 'machine': platform.machine()},
        'python': python_state(),
        'hosts': host_list,
        'install': installed_state(Path(chosen)),
        'external': external_state(),
        'workbench': workbench_state(),
    }
    report['next_steps'] = next_steps(report)
    return report


def render(report: dict) -> str:
    repo = report['repo']
    mark = lambda ok: '✅' if ok else '❌'  # noqa: E731
    lines = [
        f"chem-research-skills doctor   版本 {repo['version']}",
        f"仓库   {repo['root']}",
        f"完整性 {mark(repo['manifest'] == 'ok')} MANIFEST {repo['manifest']}"
        + (f"（{repo['verified_files']} 文件）" if repo['verified_files'] else ''),
        f"系统   {report['os']['platform']}",
        f"Python {mark(report['python']['supported'])} {report['python']['version']}  {report['python']['executable']}",
    ]
    host = next((item for item in report['hosts'] if item['detected']), None)
    lines.append('宿主   ' + (f"✅ {host['host']}  {host['base']}" if host else '⚠️ 未发现 DSH/Codex 目录'))
    install = report['install']
    if install['exists']:
        state = '完整' if not install['missing'] and not install['different'] else '需处理'
        marker = install.get('marker') or {}
        version = marker.get('version', '无安装标记') if isinstance(marker, dict) else '无安装标记'
        lines.append(f"技能   {state} {install['skills_dir']}  已装 {len(install['found'])}/6  标记 {version}")
        if install['missing']:
            lines.append('       缺少: ' + ', '.join(install['missing']))
        if install['different']:
            lines.append('       与发布包内容不同: ' + ', '.join(install['different']))
        if install.get('global_block') is not None:
            lines.append(f"       全局默认规则块: {install['global_block']} 处")
    else:
        lines.append(f"技能   ⚠️ 目标目录不存在 {install['skills_dir']}")
    lines.append('依赖   ' + '  '.join(
        f"{name}{'✅' if info['ready'] else '⚠️'}" for name, info in report['python']['profiles'].items()))
    external = report['external']
    lines.append('外部软件 ' + '  '.join(f"{row['label']}{'✅' if row['available'] else '—'}" for row in external))
    if report['workbench'].get('config'):
        lines.append('工作台   ' + report['workbench']['config'])
    lines.append('')
    lines.append('下一步：')
    for index, step in enumerate(report['next_steps'], 1):
        lines.append(f'  {index}. {step}')
    return '\n'.join(lines)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='machine-readable report')
    parser.add_argument('--skills-dir', help='installed skills directory to inspect')
    parser.add_argument('--strict', action='store_true', help='exit 1 when manifest or Python check fails')
    args = parser.parse_args(argv)

    report = build_report(Path(args.skills_dir).expanduser() if args.skills_dir else None)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render(report))
    if args.strict and (report['repo']['manifest'] != 'ok' or not report['python']['supported']):
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())