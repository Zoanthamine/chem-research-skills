"""Tests for the maintenance tooling: manifest, inventory, doctor, installer CLI."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ManifestTests(unittest.TestCase):
    def test_ledger_matches_working_tree(self):
        manifest = load('manifest')
        expected = manifest.load()
        actual = manifest.collect()
        self.assertEqual([row['path'] for row in expected], [row['path'] for row in actual])
        self.assertEqual(manifest.describe_drift(expected, actual), [])

    def test_statistics_cover_every_area(self):
        manifest = load('manifest')
        stats = manifest.statistics(manifest.collect())
        self.assertGreater(stats['verified_files'], 1000)
        self.assertIn('skills/scxrd-refinement', stats['areas'])


class InventoryTests(unittest.TestCase):
    def test_rows_cover_the_manifest(self):
        inventory = load('inventory')
        rows = inventory.build_rows()
        ledger = load('manifest').load()
        self.assertEqual(len(rows), len(ledger))
        self.assertEqual({row['path'] for row in rows}, {row['path'] for row in ledger})

    def test_generation_is_deterministic(self):
        inventory = load('inventory')
        self.assertEqual(inventory.build_rows(), inventory.build_rows())

    def test_committed_documents_are_current(self):
        inventory = load('inventory')
        self.assertEqual(inventory.check_outputs(), [])

    def test_curated_entries_use_real_paths(self):
        inventory = load('inventory')
        missing = [path for path in inventory.CURATED if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])


class DoctorTests(unittest.TestCase):
    def test_report_is_structured_and_read_only(self):
        doctor = load('doctor')
        report = doctor.build_report()
        for key in ('repo', 'os', 'python', 'hosts', 'install', 'external', 'workbench', 'next_steps'):
            self.assertIn(key, report)
        self.assertEqual(report['repo']['manifest'], 'ok')
        self.assertTrue(report['next_steps'])
        self.assertEqual(len(report['external']), len(doctor.EXTERNAL))
        self.assertIn('supported', report['python'])

    def test_render_contains_next_steps(self):
        doctor = load('doctor')
        text = doctor.render(doctor.build_report())
        self.assertIn('下一步', text)
        self.assertIn('chem-research-skills doctor', text)


class InstallerCliTests(unittest.TestCase):
    def test_dry_run_reports_plan_and_writes_nothing(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            target = Path(tmp) / 'skills'
            proc = subprocess.run(
                [sys.executable, str(ROOT / 'install.py'), '--host', 'dsh', '--target', str(target),
                 '--dry-run', '--json'],
                capture_output=True, text=True, encoding='utf-8', timeout=120)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn('"dry_run": true', proc.stdout.replace('"dry_run":  true', '"dry_run": true'))
            self.assertIn('create', proc.stdout)
            self.assertFalse(target.exists())

    def test_check_reports_file_count(self):
        proc = subprocess.run([sys.executable, str(ROOT / 'install.py'), '--check'],
                              capture_output=True, text=True, encoding='utf-8', timeout=120)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn('verified_files', proc.stdout)


if __name__ == '__main__':
    unittest.main()