# Copyright (c) 2014-2015  Sam Maloney.
# License: GPL v2.

from setuptools import setup

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
    py_modules = modules, 
    entry_points={'console_scripts': [ 'morphis_node=node:main'] }, 
    packages = [ "maalstroom" ],
    data_files = [ 
        (
            'bitmaps', 
            [ 'bitmaps/favicon.ico' ] 
        ), 

        (
            'version', 
            [ 'VERSION' ] 
        ), 

        (
            os.path.join('maalstroom' ,'resources'), 
            [ os.path.join('maalstroom', 'resources', 'style.css') ]
        ), 

        (
            os.path.join('maalstroom' ,'resources', 'images', 'dmail'), 
            glob.glob(os.path.join('maalstroom', 'resources', 'images', 'dmail', '*')) 
        ), 

        (
            os.path.join('maalstroom' ,'templates' ,'main'), 
            glob.glob(os.path.join('maalstroom', 'templates', 'main', '*')) 
        ), 

        (
            os.path.join('maalstroom' ,'templates' ,'dmail'),
            glob.glob(os.path.join('maalstroom', 'templates', 'dmail', '*')) 
        ) 
    ] 
)

