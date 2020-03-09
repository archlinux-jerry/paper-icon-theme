#!/usr/bin/env python
from pathlib import Path

ad_dir = Path('/usr/share/icons/Adwaita')
pp_dir = Path('.')

ad_subdir = [f for f in ad_dir.iterdir() if f.is_dir() and (f / 'actions').is_dir() and f.name != 'scalable']
pp_subdir = [f for f in pp_dir.iterdir() if f.is_dir() and (f / 'actions').is_dir() and f.name != 'scalable']

# link actions
icons_found = list()
for d in ad_subdir:
    d = d / 'actions'
    print('ad_subdir found', d)
    i = [f.name for f in d.iterdir() if f.is_file() and (lambda n: True if n[-4:] in ('.png', '.svg') else (print('bad', f) or False))(f.name)]
    icons_found.extend([_ii for _i in i if (_ii := _i.split('.')[0])])

print('icons_found:', len(icons_found))
ad_si = [i for i in icons_found if i.endswith('-symbolic')]
ad_rtli = [i for i in icons_found if i.endswith('-symbolic-rtl')]
print('symbolic_icons_found:', len(ad_si))
print('symbolic-rtl_icons_found:', len(ad_rtli))
print('sum:', len(ad_rtli) + len(ad_si))

findex=list()
icons_found = list()
for d in pp_subdir:
    d = d / 'actions'
    print('pp_subdir found', d)
    i = [f.name for f in d.iterdir() if f.is_file() and (lambda n: True if n[-4:] in ('.png', '.svg') else (print('bad', f) or False))(f.name)]
    findex.extend([f for f in d.iterdir() if f.is_file() and (lambda n: True if n[-4:] in ('.png', '.svg') else (print('bad', f) or False))(f.name)])
    icons_found.extend([_ii for _i in i if (_ii := _i.split('.')[0])])
print('icons_found:', len(icons_found))
pp_si = [i for i in icons_found if i.endswith('-symbolic')]
pp_rtli = [i for i in icons_found if i.endswith('-symbolic-rtl')]
print('symbolic_icons_found:', len(pp_si))
print('symbolic-rtl_icons_found:', len(pp_rtli))
print('sum:', len(pp_rtli) + len(pp_si))

ttl_processed = 0
for i in ad_si:
    if i in pp_si:
        pass
        #print('good', i, 'is found in paper')
    elif i[:-len('-symbolic.xxx')+1] in [i[:-4] for i in icons_found]:
        #print('warn', i, 'is found in paper but not symbolic')
        processed = 0
        for f in findex:
            if f.name.startswith(i[:-len('-symbolic.xxx')+1]) and 'symbolic' not in f.name:
                nname = f"{f.name[:-4]}-symbolic.symbolic.{f.name[-3:]}"
                np = Path(f.parent / nname)
                if not np.exists():
                    np.symlink_to(f.name)
                    processed += 1
        if processed:
            ttl_processed += processed
        else:
            print('!!!', i, 'unexpected')
    else:
        pass
        #print('err', i, 'is not found in paper')
print('processed:', ttl_processed)
