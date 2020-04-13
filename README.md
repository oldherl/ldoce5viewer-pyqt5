# LDOCE5 Viewer (PyQt5, Python3)

This project is ported to PyQt5 which supports retina (HiDPI) display.

The LDOCE5 Viewer is an alternative dictionary viewer for the Longman Dictionary of Contemporary English 5th Edition (LDOCE 5).

Website: http://hakidame.net/ldoce5viewer/

It runs on Linux, Mac OS X and Microsoft Windows.

This software is free and open source software licensed under the terms of GPLv3.


## Requirement packages (in ubuntu)

- `pyqt5-dev-tools`
- `python3-pyqt5.qtwebkit`
- `python3-pyqt5.qtmultimedia`
- `libqt5multimedia5-plugins`
- `python3-whoosh`
- `python3-lxml`
- `python3-distutils`

## Installation

``` bash
$ sudo apt install pyqt5-dev-tools python3-pyqt5.qtwebkit python3-pyqt5.qtmultimedia libqt5multimedia5-plugins
$ sudo apt install python3-whoosh python3-lxml python3-distutils
$ make
$ sudo make install
```
