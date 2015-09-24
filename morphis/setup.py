# Copyright (c) 2014-2015  Sam Maloney.
# License: GPL v2.

from setuptools import setup, find_packages

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

setup(
    name='morphis', 
    version='0.8',
    py_modules = modules, 
    entry_points={'console_scripts': [ 'morphis_node=node:main' ] }, 
    
    packages = [ 'morphis', 'morphis/maalstroom' ],

    package_data = {
        'morphis': [ '*.ico' ]
    }    
)

