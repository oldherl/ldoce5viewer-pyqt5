#!/usr/bin/env python

import subprocess
from distutils.core import setup
from ldoce5viewer import __version__


def iter_static():
    import os, os.path

    for root, dirs, files in os.walk("ldoce5viewer/static"):
        for filename in files:
            yield os.path.relpath(os.path.join(root, filename), "ldoce5viewer")

    for root, dirs, files in os.walk("ldoce5viewer/qtgui/resources"):
        for filename in files:
            yield os.path.relpath(os.path.join(root, filename), "ldoce5viewer")

    for root, dirs, files in os.walk("ldoce5viewer/qtgui/ui"):
        for filename in files:
            yield os.path.relpath(os.path.join(root, filename), "ldoce5viewer")


extra_options = {}



#------------
# setup(...)
#------------

if 'name' not in extra_options:
    extra_options['name'] = 'ldoce5viewer'

setup(
    version = __version__,
    description = 'LDOCE5 Viewer fork by oldherl',
    url = 'https://github.com/oldherl/ldoce5viewer-pyqt5',
    license = 'GPLv3+',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Development Status :: 5 - Production/Stable'
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Education',
        ],
    author = 'oldherl',
    author_email = 'oldherl@gmail.com',
    package_dir = {'ldoce5viewer': 'ldoce5viewer'},
    packages = [
        'ldoce5viewer',
        'ldoce5viewer.qtgui',
        'ldoce5viewer.qtgui.ui',
        'ldoce5viewer.qtgui.resources',
        'ldoce5viewer.qtgui.utils',
        'ldoce5viewer.qtgui.utils.mp3play',
        'ldoce5viewer.utils',
        'ldoce5viewer.ldoce5',
        ],
    package_data = {'ldoce5viewer': list(iter_static())},
    scripts = ['scripts/ldoce5viewer'],
    **extra_options
)

