# -*- coding: utf-8 -*-
import os
import re
from distutils.core import setup
from setuptools.command.test import test


def get_readme(readme):
    """Get long description."""
    with open(readme) as f:
        return f.read()


def get_version(package):
    """Return package version as listed in ``__version__`` in ``init.py``."""
    f = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", f).group(1)


setup(
    name='eccrypt',
    version=get_version('eccrypt'),
    description='Easy encryption and decryption.',
    long_description=get_readme('README.rst'),
    author='Pierpaolo Rasicci',
    url='https://github.com/i5ar/eccrypt',
    packages=['eccrypt'],
    install_requires=[
        'future',
        'pycryptodomex',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Communications',
    ],
    scripts=['bin/eccrypt'],
    zip_safe=False,
    test_suite='tests',
)
