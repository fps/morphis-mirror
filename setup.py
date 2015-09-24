# Copyright (c) 2014-2015  Sam Maloney.
# License: GPL v2.

from distutils.core import setup
from Cython.Build import cythonize

import os
import glob

modules = [
    "asymkey",
    "base58",
    "bittrie",
    "brute",
    "chordexception",
    "chord_packet",
    "chord",
    "chord_tasks",
    "client_engine",
    "client",
    "consts",
    "db",
    "dhgroup14",
    "dmail",
    "dsskey",
    "enc",
    "hashbench",
    "kexdhgroup14sha1",
    "kex",
    "llog",
    "mbase32",
    "mcc",
    "mn1",
    "multipart",
    "mutil",
    "packet",
    "peer",
    "putil",
    "rsakey",
    "shell",
    "node",
    "sshexception",
    "sshtype"
]

#setup(
#    name = 'morphis',
#    ext_modules = cythonize(\
#        [x + ".py" for x in modules]),
#    scripts = [ "node.py" ]
#)

setup( name='morphis', 
    py_modules = modules, 
    entry_points={'console_scripts': [ 'morphis_node=node:main'] }, 
    packages = [ "maalstroom" ],
    data_files = [ 
        (
            os.path.join('share', 'morphis', 'bitmaps'), 
            [ 'bitmaps/favicon.ico' ] 
        ), 

        (
            os.path.join('share', 'morphis', 'maalstroom' ,'resources', 'images', 'dmail'), 
            glob.glob(os.path.join('maalstroom', 'resources', 'images', 'dmail', '*')) 
        ), 

        (
            os.path.join('share', 'morphis', 'maalstroom' ,'templates' ,'main'), 
            glob.glob(os.path.join('maalstroom', 'templates', 'main', '*')) 
        ), 

        (
            os.path.join('share', 'morphis', 'maalstroom' ,'templates' ,'dmail'),
            glob.glob(os.path.join('maalstroom', 'templates', 'dmail', '*')) 
        ) 
    ] 
)

