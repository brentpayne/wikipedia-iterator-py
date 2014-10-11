#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


requirements = [
    'kennyg>=0.0.0'
]

setup(
    name='wikipedia-iterator-py',
    version='0.0.1a0',
    description='Creates iterators that traverse bulk Wikipedia download files.',
    long_description="An extraction of the WikiExtractor.py's code to convert mikimedia text into raw unicode. "
                     "See http://medialab.di.unipi.it/wiki/Wikipedia_Extractor for original project.  "
                     "This purpose of this project is to maintain that section of code and place it in a module"
                     "that is easy to distribute, aka PYPI accessible.",
    author='Brent Payne',
    author_email='brent.payne@gmail.com',
    url='http://www.github.com/brentpayne/wikipedia-iterator-py',
    packages=find_packages(exclude=('test*',)),
    install_requires=requirements,
    keywords=['wikipedia', 'wikimedia', 'parse', 'parsing', '2text'],
    classifiers=[
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Lesser General Public License v3" +
         " (LGPLv3)")
    ]
)
