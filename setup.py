#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.test import test


setup(
    name='eccrypt',
    version='0.0.5',
    description='Easy encryption and decryption.',
    author='Pierpaolo Rasicci',
    author_email='',
    url='https://github.com/i5ar/eccrypt',
    packages=['eccrypt'],
)
