#! /usr/bin/env python2

import sys
import os

TEMPLATE = """\
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=ImageHunter
Comment=Download random images
Exec=%(DIR)s/imagehunter.py
Icon=%(DIR)s/imagehunter.svg
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;
"""

DST = '~/.local/share/applications/imagehunter.desktop'

DIR = os.path.abspath(os.path.dirname(sys.argv[0]))

open(os.path.expanduser(DST), 'w').write(
    TEMPLATE % dict(
	DIR=DIR,
    )
)
