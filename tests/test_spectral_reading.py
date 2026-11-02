from pathlib import Path
import importlib.util,json,tempfile,unittest,warnings
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'skills/huangjt-spectral-structure-analysis/scripts/read_spectral_file.py'
spec=importlib.util.spec_from_file_location('spectral_reader',P);reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)

@unittest.skipUnless(importlib.util.find_spec('nmrglue'),'NMR profile not installed')
class NmrReadingTests(unittest.TestCase):
    def test_bruker_fid_directory_roundtrip(self):
        import nmrglue as ng,numpy as np
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as temp:
            base=Path(temp);source=base/'bruker';u=ng.fileiobase.create_blank_udic(1)
            u[0].update(size=256,complex=True,sw=5000.0,obs=500.0,car=2500.0,label='1H',time=True,freq=False)
            original=(np.arange(256)+1j*np.arange(256)[::-1]).astype(np.complex128)
            d=ng.bruker.create_dic(u)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore');ng.bruker.write(str(source),d,original,write_prog=False)
                report=reader.run(source,base/'result')
            self.assertEqual(report['format'],'bruker');self.assertTrue(report['complex'])
            np.testing.assert_array_equal(np.load(base/'result/nmr-data.npz')['data'],original)
            self.assertTrue((base/'result/acquisition.json').is_file())
    def test_nmrpipe_complex_roundtrip(self):
        import nmrglue as ng,numpy as np
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as temp:
            base=Path(temp);u=ng.fileiobase.create_blank_udic(1)
            u[0].update(size=128,complex=True,sw=4000.0,obs=400.0,car=1600.0,label='1H',time=True,freq=False)
            original=np.exp(1j*np.arange(128)/10).astype(np.complex64);path=base/'test.pipe'
            ng.pipe.write(str(path),ng.pipe.create_dic(u),original)
            report=reader.run(path,base/'result')
            np.testing.assert_array_equal(np.load(base/'result/nmr-data.npz')['data'],original)
            self.assertEqual(report['processing_applied'],[])
    def test_varian_fid_directory_roundtrip(self):
        import nmrglue as ng,numpy as np
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as temp:
            base=Path(temp);u=ng.fileiobase.create_blank_udic(1)
            u[0].update(size=128,complex=True,sw=4000.0,obs=400.0,car=1600.0,label='1H',time=True,freq=False)
            original=(np.arange(128)+1j*np.arange(128)[::-1]).astype(np.complex64)
            ng.varian.write(str(base/'varian'),ng.varian.create_dic(u),original)
            report=reader.run(base/'varian',base/'result')
            self.assertEqual(report['format'],'varian')
            np.testing.assert_array_equal(np.load(base/'result/nmr-data.npz')['data'],original)

@unittest.skipUnless(importlib.util.find_spec('pyopenms'),'MS profile not installed')
class MsReadingTests(unittest.TestCase):
    def test_mzml_peaks_and_precursors_survive_read(self):
        import pyopenms as ms,numpy as np
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as temp:
            base=Path(temp);exp=ms.MSExperiment()
            for level in [1,2]:
                s=ms.MSSpectrum();s.setMSLevel(level);s.setRT(30.0*level);s.set_peaks((np.array([100.1,201.2]),np.array([3.,7.],dtype=np.float32)))
                if level==2:
                    p=ms.Precursor();p.setMZ(201.2);p.setCharge(1);s.setPrecursors([p])
                exp.addSpectrum(s)
            source=base/'test.mzML';ms.MzMLFile().store(str(source),exp)
            report=reader.run(source,base/'result')
            self.assertEqual(report['spectra'],2);self.assertEqual(report['total_peaks'],4)
            self.assertEqual(report['ms_levels'],{1:1,2:1})
            self.assertIn('201.2',(base/'result/spectra.csv').read_text())
    def test_mgf_is_decoded(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as temp:
            base=Path(temp);source=base/'test.mgf'
            source.write_text('BEGIN IONS\nTITLE=scan=1\nPEPMASS=201.2\nCHARGE=1+\nRTINSECONDS=30\n100.1 3\n150.2 7\nEND IONS\n',encoding='ascii')
            report=reader.run(source,base/'result');self.assertEqual(report['spectra'],1);self.assertEqual(report['total_peaks'],2)

class UnsupportedReadingTests(unittest.TestCase):
    def test_raw_not_misread_as_text(self):
        with self.assertRaisesRegex(ValueError,'Vendor-specific'):reader.identify(Path('sample.raw'),'auto')
    def test_never_writes_into_acquisition_folder(self):
        with tempfile.TemporaryDirectory(dir=ROOT.parent) as temp:
            with self.assertRaises(ValueError):reader.run(Path(temp),Path(temp)/'processed','bruker')

if __name__=='__main__':unittest.main()
