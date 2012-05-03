#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'Facebook',
    version = '0.0',
    description = 'Facebook makes it even easier to interact with Facebook\'s Graph API',
    long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author = 'Johannes Gorset',
    author_email = 'jgorset@gmail.com',
    url = 'http://github.com/jgorset/facebook',
    packages = [
        'facebook'
    ]
)
