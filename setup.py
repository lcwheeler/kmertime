import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command, Extension
import numpy


if sys.version_info[0] < 3:
    sys.exit('Sorry, Python < 3.x is not supported')

# Try using setuptools first, if it's installed
from setuptools import setup, find_packages

# set up binding polynomial C extension
ext = Extension('kmertime.kmercounter',['kmertime/kmercounter.c'])

# Need to add all dependencies to setup as we go!
setup(name='kmertime',
    packages=find_packages(),
    version='0.1',
    description="Python software package for counting kmers in sequence data",
    author='Lucas C. Wheeler',
    author_email='lwheeler9@gmail.com',
    url='https://github.com/lcwheeler/kmertime',
    zip_safe=False,
    install_requires=["matplotlib","scipy","numpy","pandas", "cython", "biopython"],
    package_data={"":["*.h","src/*.h"]},
    classifiers=['Programming Language :: Python'],
    ext_modules=[ext])



