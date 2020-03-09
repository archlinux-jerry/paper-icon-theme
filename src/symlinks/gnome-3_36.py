#!/usr/bin/env python
from pathlib import Path
import shutil

ad_dir = Path('/usr/share/icons/Adwaita')
pp_dir = Path('.')

ad_subdir = [f for f in ad_dir.iterdir() if f.is_dir() and (f / 'actions').is_dir()]

dir_map = {ad: (pp_dir / ad.name) for ad in ad_subdir if (pp_dir / ad.name).exists() or print('!! bad', ad)}


def match_icon(fpath):
    n = fpath.name
    try:
        assert n.endswith(('.png', 'svg'))
        iconfull = n[:-4]
        if iconfull.endswith('.symbolic'):
            iconfull = iconfull[:-len('.symbolic')]
        if iconfull.endswith('-symbolic'):
            t = 'sym'
            n = iconfull[:-len('-symbolic')]
        elif iconfull.endswith('-symbolic-rtl'):
            t = 'sym_rtl'
            n = iconfull[:-len('-symbolic-rtl')]
        else:
            t = None
            n = iconfull
        return {'n': n, 't': t}
    except AssertionError:
        print('match icon: bad', fpath)
        return None

for sd, dd in dir_map.items():
    sd = (sd / 'actions')
    si = [f for f in sd.iterdir() if f.is_file() and (lambda n: True if n[-4:] in ('.png', '.svg') else (print('bad', f) or False))(f.name)]
    dd = (dd / 'actions')
    di = [f for f in dd.iterdir() if f.is_file() and (lambda n: True if n[-4:] in ('.png', '.svg') else (print('bad', f) or False))(f.name)]
    pdi = {(a := match_icon(f))['n']: {'t': a['t'], 'f': f} for f in di}
    for f in si:
        m = match_icon(f)
        p = pdi.get(m['n'], None)
        if p:
            if m['t'] == 'sym' and p['t'] != 'sym':
                print(f'warn: {p} in paper is not sym')
                try:
                    (dd / f.name).symlink_to(p['f'].name)
                except:
                    print('error debug:', p['f'].name, 'link to', (dd / f.name))
#                    input()
        else:
            print(f'err: no {f} {m} in paper')
            shutil.copyfile(f, Path(dd / f.name))
