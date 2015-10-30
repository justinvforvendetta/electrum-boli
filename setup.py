#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-BOLI requires Python version >= 2.7.0...")



data_files = []
if platform.system() in [ 'Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum_boli.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum_boli.png'])
    ]


setup(
    name="Electrum-BOLI",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
    ],
    package_dir={
        'electrum_boli': 'lib',
        'electrum_boli__gui': 'gui',
        'electrum_boli_plugins': 'plugins',
    },
    packages=['electrum_boli','electrum_boli_gui','electrum_boli_gui.qt','electrum_boli_plugins'],
    package_data={
        'electrum_boli': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_boli_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-boli'],
    data_files=data_files,
    description="Lightweight Bolivarcoin Wallet",
    author="mazaclub",
    license="GNU GPLv3",
    url="https://electrum.org",
    long_description="Lightweight Bolivarcoin Wallet"
)
