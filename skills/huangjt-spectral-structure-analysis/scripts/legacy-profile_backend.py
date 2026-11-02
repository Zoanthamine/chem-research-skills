"""Bounded local 1D profile/peak-list analysis. No chemical assignments inferred."""
from pathlib import Path
import csv
import hashlib
import json
import re
import numpy as np
from scipy.signal import find_peaks

TYPES = {'1H-NMR', '13C-NMR', '19F-NMR', '31P-NMR', 'MS-LowRes',
         'MS-HighRes', 'IR', 'UV-Vis', 'CD', 'HPLC', 'GC'}


def normalize_type(value):
    aliases = {'nmr': '1H-NMR', '1h': '1H-NMR', '13c': '13C-NMR',
               'ms': 'MS-LowRes', 'hrms': 'MS-HighRes', 'uv': 'UV-Vis'}
    if value in TYPES:
        return value
    candidate = aliases.get(str(value).lower())
    if candidate:
        return candidate
    for item in TYPES:
        if item.lower() == str(value).lower():
            return item
    raise ValueError('Unsupported spectrum type; specify one of: ' + ', '.join(sorted(TYPES)))


def read_xy(path):
    text = path.read_text(encoding='utf-8-sig')
    rows, headers, skipped = [], [], 0
    for number, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith(('#', '//', ';')):
            continue
        parts = re.split(r'[,;\t\s]+', line)
        try:
            pair = [float(p) for p in parts]
        except ValueError:
            if rows:
                raise ValueError(f'Non-numeric row {number}; refusing to silently drop data')
            headers.append(line)
            skipped += 1
            continue
        if len(pair) != 2:
            raise ValueError(f'Row {number}: exactly two numeric columns required')
        rows.append(pair)
    if not rows:
        raise ValueError('No two-column numeric data found')
    data = np.asarray(rows, dtype=float)
    if not np.isfinite(data).all():
        raise ValueError('NaN or infinite values found')
    return data[:, 0], data[:, 1], {'headers': headers, 'header_rows': skipped}


def read_jcamp(path):
    from nmrglue.fileio import jcampdx
    # nmrglue handles row-start coordinates and compressed JCAMP numeric encodings.
    dic, data = jcampdx.read(str(path))
    if data is None or isinstance(data, list) or np.iscomplexobj(data):
        raise ValueError('A single real 1D processed JCAMP spectrum is required; raw FID/complex data need NMR processing first')
    y = np.asarray(data, dtype=float)
    if y.ndim != 1 or len(y) < 2:
        raise ValueError('JCAMP does not contain a usable single 1D spectrum')
    def field(key, default=None):
        item = dic.get(key, [default])
        return item[0] if isinstance(item, list) else item
    datatype = str(field('DATATYPE', '')).upper()
    if 'FID' in datatype:
        raise ValueError('FID is time-domain data; phase/calibrate/transform it first')
    first, last = float(field('FIRSTX')), float(field('LASTX'))
    count = int(field('NPOINTS', len(y)))
    if count != len(y):
        raise ValueError('JCAMP point count does not match decoded data')
    x = np.linspace(first, last, len(y))
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError('JCAMP contains nonfinite values')
    return x, y, {'x_units': field('XUNITS'), 'y_units': field('YUNITS'),
                  'data_type': datatype, 'decoder': 'nmrglue.jcampdx'}


def analyze_profile(filepath, output_dir, spectrum_type, input_kind='profile',
                    signal_kind=None, prominence_fraction=0.02):
    path, out = Path(filepath), Path(output_dir)
    kind = normalize_type(spectrum_type)
    result = dict(success=False, spectrum_type=kind, file_path=str(path), confidence=1.0,
                  raw_data={}, peaks=[], structural_info={}, functional_groups=[],
                  molecular_formula=None, molecular_weight=None, notes=[], output_files={}, errors=[])
    try:
        if input_kind not in {'profile', 'peaks'}:
            raise ValueError('input_kind must be profile or peaks')
        if not 0 < prominence_fraction < 1:
            raise ValueError('prominence_fraction must be between zero and one')
        reader = read_jcamp if path.suffix.lower() in {'.jdx', '.dx', '.jcm'} else read_xy
        x, y, metadata = reader(path)
        nmr = kind.endswith('-NMR')
        expected_x = 'ppm' if nmr else ('cm-1' if kind == 'IR' else ('nm' if kind in {'UV-Vis', 'CD'} else ('m/z' if kind.startswith('MS-') else 'source retention-time unit')))
        x_units = str(metadata.get('x_units') or '').strip().lower()
        allowed_units = {'ppm'} if nmr else ({'1/cm', 'cm-1', 'cm^-1'} if kind == 'IR' else ({'nm', 'nanometers'} if kind in {'UV-Vis', 'CD'} else set()))
        if x_units and allowed_units and x_units not in allowed_units:
            raise ValueError(f'X unit {x_units!r} is incompatible with {kind}; convert/calibrate explicitly')
        if kind == 'IR':
            if signal_kind is None:
                unit = str(metadata.get('y_units') or '').upper()
                if 'TRANSMIT' in unit:
                    signal_kind = 'transmittance'
                elif 'ABSORB' in unit:
                    signal_kind = 'absorbance'
                else:
                    raise ValueError('IR requires signal_kind=absorbance or transmittance; cannot infer polarity from numeric values')
            if signal_kind not in {'absorbance', 'transmittance'}:
                raise ValueError('IR signal_kind must be absorbance or transmittance')
        notes = ['Numerical peak candidates only; no automatic chemical assignment or purity claim.',
                 f'X-axis expected: {expected_x}. Text files must already use this unit.']
        if input_kind == 'profile':
            if len(x) < 3:
                raise ValueError('A profile requires at least three samples; use input_kind=peaks for peak lists')
            delta = np.diff(x)
            if not ((delta > 0).all() or (delta < 0).all()):
                raise ValueError('Profile X must be strictly monotonic; repeated scans/coordinates need separate processing')
            if x[0] > x[-1]:
                x, y = x[::-1], y[::-1]
            prominence = float(np.ptp(y)) * prominence_fraction
            if prominence == 0:
                indices, props = np.array([], dtype=int), {'prominences': []}
            else:
                target = -y if signal_kind == 'transmittance' else y
                indices, props = find_peaks(target, prominence=prominence)
                if kind == 'CD':
                    minus, minus_props = find_peaks(-y, prominence=prominence)
                    indices = np.concatenate([indices, minus])
                    props['prominences'] = np.concatenate([props['prominences'], minus_props['prominences']])
            notes.append('Endpoints are not treated as peaks; no smoothing, baseline correction or concentration calibration applied.')
            candidates = [dict(x=float(x[i]), y=float(y[i]), prominence=float(p)) for i, p in zip(indices, props['prominences'])]
        else:
            candidates = [dict(x=float(a), y=float(b)) for a, b in zip(x, y)]
            notes.append('Input was explicitly declared a peak list; no peak picking applied.')
        result['peaks'] = sorted(candidates, key=lambda p: p['x'])
        result['raw_data'] = dict(points=len(x), input_kind=input_kind, signal_kind=signal_kind,
                                  x_unit=expected_x, metadata=metadata,
                                  source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                                  prominence_fraction=prominence_fraction)
        result['notes'] = notes
        out.mkdir(parents=True, exist_ok=True)
        for name, rows, headers in [('spectrum-data.csv', zip(x, y), ['x', 'signal']),
                                    ('peak-candidates.csv', ((p['x'], p['y']) for p in result['peaks']), ['x', 'signal'])]:
            dest = out / name
            with dest.open('w', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f); writer.writerow(headers); writer.writerows(rows)
            result['output_files'][name] = str(dest)
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, y, lw=0.9)
        ax.scatter([p['x'] for p in result['peaks']], [p['y'] for p in result['peaks']], s=14, color='red')
        ax.set(xlabel=expected_x, ylabel=signal_kind or 'source signal unit', title=kind)
        if nmr or kind == 'IR':
            ax.invert_xaxis()
        fig.tight_layout()
        for suffix in ['svg', 'png']:
            dest = out / f'spectrum.{suffix}'
            fig.savefig(dest, dpi=160); result['output_files'][suffix] = str(dest)
        plt.close(fig)
        result['success'] = True
    except Exception as exc:
        result['errors'].append(str(exc))
    out.mkdir(parents=True, exist_ok=True)
    result['output_files']['profile-analysis'] = str(out / 'profile-analysis.json')
    (out / 'profile-analysis.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('--type', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--input-kind', choices=['profile', 'peaks'], default='profile')
    p.add_argument('--signal-kind', choices=['absorbance', 'transmittance'])
    a = p.parse_args()
    r = analyze_profile(a.input, a.output, a.type, a.input_kind, a.signal_kind)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['success'] else 1)
