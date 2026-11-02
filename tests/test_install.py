from pathlib import Path
from types import SimpleNamespace
import contextlib,hashlib,importlib.util,json,os,tempfile,unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('installer',ROOT/'install.py');installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)

class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.base=Path(self.tmp.name);self.source=self.base/'package'
        for name in installer.NAMES:
            p=self.source/'skills'/name/'SKILL.md';p.parent.mkdir(parents=True);p.write_text('---\nname: '+name+'\ndescription: test fixture\n---\nExample\n',encoding='utf-8')
        (self.source/'routing').mkdir();(self.source/'routing/global-defaults.md').write_text('# Chemistry\nRoot: {{SKILL_ROOT}}\n',encoding='utf-8')
        self.rehash();self.args=SimpleNamespace(replace=False,no_defaults=False,target=None,codex_home=None,dsh_home=None)
    def tearDown(self):self.tmp.cleanup()
    def rehash(self):
        files=[{'path':p.relative_to(self.source).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in self.source.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
        (self.source/'MANIFEST.json').write_text(json.dumps(files),encoding='utf-8')
    def target(self,host='codex'):return self.base/host/'skills',self.base/host/'AGENTS.md'
    def test_clean_install_and_managed_global_rules(self):
        target,guide=self.target();guide.parent.mkdir();guide.write_text('Keep my project preferences.\n',encoding='utf-8')
        installer.install(self.source,[('codex',(target,guide))],self.args)
        self.assertEqual(len(list(target.glob('*/SKILL.md'))),6)
        self.assertIn('Keep my project preferences.',guide.read_text(encoding='utf-8'))
        self.assertIn(installer.BEGIN,guide.read_text(encoding='utf-8'))
    def test_repeat_install_does_not_duplicate_global_block(self):
        target,guide=self.target();pairs=[('codex',(target,guide))]
        installer.install(self.source,pairs,self.args);installer.install(self.source,pairs,self.args)
        self.assertEqual(guide.read_text(encoding='utf-8').count(installer.BEGIN),1)
    def test_collision_refuses_before_writing_any_skill(self):
        target,guide=self.target();old=target/installer.NAMES[-1]/'SKILL.md';old.parent.mkdir(parents=True);old.write_text('local edits',encoding='utf-8')
        with self.assertRaises(FileExistsError):installer.install(self.source,[('codex',(target,guide))],self.args)
        self.assertFalse((target/installer.NAMES[0]).exists());self.assertEqual(old.read_text(),'local edits')
    def test_replace_preserves_old_file_in_backup(self):
        target,guide=self.target();old=target/installer.NAMES[0]/'SKILL.md';old.parent.mkdir(parents=True);old.write_text('local edits',encoding='utf-8');self.args.replace=True
        installer.install(self.source,[('codex',(target,guide))],self.args)
        backups=list((target.parent/'chemistry-skill-backups').rglob('SKILL.md'))
        self.assertEqual(len(backups),1);self.assertEqual(backups[0].read_text(),'local edits')
    def test_two_hosts_have_independent_global_paths(self):
        pairs=[(h,self.target(h)) for h in ['codex','dsh']];installer.install(self.source,pairs,self.args)
        for _,(target,guide) in pairs:self.assertTrue(guide.exists());self.assertEqual(len(list(target.glob('*/SKILL.md'))),6)
    def test_no_defaults_preserves_instruction_file(self):
        target,guide=self.target();guide.parent.mkdir();guide.write_text('Original',encoding='utf-8');self.args.no_defaults=True
        installer.install(self.source,[('dsh',(target,guide))],self.args);self.assertEqual(guide.read_text(),'Original')
    def test_changed_source_is_rejected(self):
        (self.source/'skills'/installer.NAMES[0]/'SKILL.md').write_text('tampered',encoding='utf-8')
        with self.assertRaises(ValueError):installer.verify(self.source)
    def test_manifest_path_traversal_is_rejected(self):
        outside=self.base/'outside.txt';outside.write_text('outside',encoding='utf-8')
        (self.source/'MANIFEST.json').write_text(json.dumps([{'path':'../outside.txt','sha256':hashlib.sha256(outside.read_bytes()).hexdigest()}]),encoding='utf-8')
        with self.assertRaises(ValueError):installer.verify(self.source)
    def test_untracked_file_is_rejected(self):
        (self.source/'unexpected.txt').write_text('not in manifest',encoding='utf-8')
        with self.assertRaises(ValueError):installer.verify(self.source)
    def test_nested_skill_is_rejected(self):
        p=self.source/'skills'/installer.NAMES[0]/'modules/unwanted/SKILL.md';p.parent.mkdir(parents=True);p.write_text('nested');self.rehash()
        with self.assertRaises(ValueError):installer.verify(self.source)

if __name__=='__main__':unittest.main()
