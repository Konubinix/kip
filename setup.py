#/usr/bin/env python3
import os
import sys
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
        f = open(os.path.join(os.path.dirname(__file__), fname))
        long_desc = f.read()
        f.close()
        return long_desc

VERSION = __import__('kip').__version__

if sys.version_info < (3,):
    print("kip requires python3.")
    print("Please re-run as: sudo python3 setup.py install")
    sys.exit(1)

setup(
    name="kip",
    version=VERSION,
    author='Graham King',
    author_email='graham@gkgk.org',
    description="kip Keeps Passwords",
    long_description=read('README.md'),
    packages=find_packages(),
    package_data={'kip': ['kip.conf']},
    entry_points={
        'console_scripts':[
            'kip=kip.cli:main'
            ]
    },
    url="https://github.com/grahamking/kip",
    install_requires=['setuptools'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
