# Copyright (c) 2014-2015  Sam Maloney.
# License: GPL v2.

from distutils.core import setup
from Cython.Build import cythonize

modules = [\
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
    "sshtype"\
]

#setup(
#    name = 'morphis',
#    ext_modules = cythonize(\
#        [x + ".py" for x in modules]),
#    scripts = [ "node.py" ]
#)

setup(name='morphis', py_modules = modules, scripts = [ "morphis_node.sh" ], packages = [ "maalstroom" ])
