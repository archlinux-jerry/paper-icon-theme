project('paper-icon-theme',
    version: '1.5',
    meson_version: '>= 0.40',
    license: 'CC-by-SA',
    default_options: ['prefix=/usr']
)

cp_cmd = 'cp -rP ../@0@ $DESTDIR@1@'
mkdir_p = 'mkdir -p $DESTDIR/@0@'
install_dir = join_paths(get_option('prefix'), 'share/icons')

meson.add_install_script('sh', '-c',
    mkdir_p.format(install_dir)
)

meson.add_install_script('sh', '-c',
    cp_cmd.format('Paper', install_dir)
)

meson.add_install_script('sh', '-c',
    cp_cmd.format('Paper-Mono-Dark', install_dir)
)

meson.add_install_script('meson/post_install.py')
