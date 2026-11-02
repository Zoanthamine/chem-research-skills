from pathlib import Path
import importlib.util,json,os,subprocess,sys,tempfile,unittest,zipfile

ROOT=Path(__file__).resolve().parents[1]
ORGANIC=ROOT/'skills/organic-chemistry-reasoning'
spec=importlib.util.spec_from_file_location('workbench',ORGANIC/'scripts/workbench.py')
workbench=importlib.util.module_from_spec(spec);spec.loader.exec_module(workbench)

class LibraryPortabilityTests(unittest.TestCase):
    def test_catalog_resolves_every_bundled_resource(self):
        rows=json.loads((ROOT/'catalog/modules.json').read_text(encoding='utf-8'))
        self.assertEqual(len(rows),47)
        for row in rows:
            for name in [row['workflow'],*row['scripts'],*row['references'],*row['templates']]:
                self.assertTrue((ROOT/name).is_file(),name)
            self.assertTrue(row['keywords'],row['module'])
        self.assertEqual(len([r for r in rows if r['owner']=='huangjt-academic-writing']),7)

    def test_plain_chinese_search_finds_relevant_modules(self):
        result=subprocess.check_output([sys.executable,str(ROOT/'tools/workbench.py'),'search','构象'],encoding='utf-8')
        self.assertIn('rdkit-conf',{r['module'] for r in json.loads(result)})

    def test_installed_organic_skill_keeps_setup_and_catalog(self):
        # Copy just this skill: no repository-level files or siblings are available.
        import shutil
        with tempfile.TemporaryDirectory(dir=ROOT.parent,prefix='portable skill ') as t:
            dst=Path(t)/'isolated-skills/organic-chemistry-reasoning';shutil.copytree(ORGANIC,dst,ignore=shutil.ignore_patterns('__pycache__'))
            result=subprocess.check_output([sys.executable,str(dst/'scripts/workbench.py'),'search','核磁'],cwd=t,encoding='utf-8')
            self.assertTrue(json.loads(result))
            plan=subprocess.check_output([sys.executable,str(dst/'scripts/workbench.py'),'setup','--data-dir',str(Path(t)/'data')],cwd=t,encoding='utf-8')
            self.assertFalse(json.loads(plan)['will_install'])
            self.assertFalse((Path(t)/'data').exists())

    def test_download_archive_cannot_escape_destination(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as t:
            base=Path(t);archive=base/'bad.zip'
            with zipfile.ZipFile(archive,'w') as z:z.writestr('../escaped.txt','bad')
            with self.assertRaises(ValueError):workbench.safe_extract(archive,base/'destination')
            self.assertFalse((base/'escaped.txt').exists())

    def test_download_archive_cannot_follow_symlink(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as t:
            base=Path(t);archive=base/'link.zip';entry=zipfile.ZipInfo('link');entry.create_system=3;entry.external_attr=(0o120777<<16)
            with zipfile.ZipFile(archive,'w') as z:z.writestr(entry,'../outside')
            with self.assertRaises(ValueError):workbench.safe_extract(archive,base/'destination')

@unittest.skipUnless(importlib.util.find_spec('rdkit'),'RDKit profile not installed')
class StructurePortabilityTests(unittest.TestCase):
    def test_conversion_keeps_stereo_and_charge(self):
        from rdkit import Chem
        cli=ORGANIC/'scripts/structure_cli.py'
        with tempfile.TemporaryDirectory(dir=ROOT.parent,prefix='structure test ') as t:
            out=Path(t)/'structure.mol';smiles='C[C@H](O)C(=O)[O-]'
            subprocess.run([sys.executable,str(cli),'convert',smiles,'--output',str(out)],check=True,capture_output=True)
            result=json.loads(subprocess.check_output([sys.executable,str(cli),'info',str(out)],encoding='utf-8'))
            self.assertEqual(Chem.MolToSmiles(Chem.MolFromSmiles(smiles)),result['smiles'])
            self.assertEqual(result['formal_charge'],-1)
            self.assertEqual(result['formula'],'C3H5O3-')
    def test_structure_drawing_creates_svg(self):
        cli=ORGANIC/'scripts/structure_cli.py'
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as t:
            out=Path(t)/'benzene.svg'
            subprocess.run([sys.executable,str(cli),'draw','c1ccccc1','--output',str(out)],check=True,capture_output=True)
            self.assertIn('<svg',out.read_text())

if __name__=='__main__':unittest.main()
