# Copyright (c) 2014-2015  Sam Maloney.
# License: GPL v2.

from setuptools import setup, find_packages

setup(
    name='morphis', 
    version='0.9',
    entry_points = { 'console_scripts': [ 'morphis_node = morphis.node:main' ] }, 
    
    packages = find_packages(),

    package_data = {
        'morphis': [ '*.ico' , 'VERSION', 'maalstroom/templates/main/*', 'maalstroom/templates/dmail/*' , 'maalstroom/resources/style.css', 'maalstroom/resources/images/dmail/*' ]
    }    
)

