from pathlib import Path
import os,subprocess,sys,unittest

SCRIPTS=Path(__file__).resolve().parents[1]/"skills/scxrd-refinement/scripts"

class Utf8OutputTests(unittest.TestCase):
    def test_cli_help_with_western_windows_pipe_encoding(self):
        env={**os.environ,"PYTHONUTF8":"0","PYTHONIOENCODING":"cp1252"}
        for name in ["03_run.py","09_checkcif.py","10_delivery.py"]:
            with self.subTest(script=name):
                result=subprocess.run([sys.executable,str(SCRIPTS/name),"--help"],env=env,capture_output=True)
                self.assertEqual(result.returncode,0,result.stderr.decode("utf-8",errors="replace"))
                output=result.stdout.decode("utf-8")
                self.assertIn("usage:",output)
    def test_unicode_text_survives_redirected_output(self):
        env={**os.environ,"PYTHONUTF8":"0","PYTHONIOENCODING":"cp1252"}
        code="import sys;sys.path.insert(0,sys.argv[1]);from utf8_console import configure_utf8;configure_utf8();print('单晶精修与结构验证')"
        result=subprocess.run([sys.executable,"-c",code,str(SCRIPTS)],env=env,capture_output=True)
        self.assertEqual(result.returncode,0)
        self.assertIn("单晶精修与结构验证",result.stdout.decode("utf-8"))
