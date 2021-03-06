"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from shaktiutils import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='shaktiutils',
    version=__version__,
    description='Utilities for the Shakti ML deployment platform written',
    long_description=long_description,
    url='https://github.com/Dhanush123/shakti-utils',
    author='Dhanush Patel',
    author_email='dhanushpatel101@gmail.com',
    license='have not picked a license yet',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8.1',
    ],
    packages=find_packages(),
    python_requires='>=3.0'
)
