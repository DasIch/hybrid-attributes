"""
    setup
    ~~~~~

    :copyright: 2016 by Daniel Neuhäuser
    :license: BSD, see LICENSE.rst for details
"""
import os
import re
from pathlib import Path

from setuptools import setup


PROJECT_PATH = Path(__file__).parent.absolute()


setup(
    name='hybrid-attributes',
    version='0.1.0',
    description='Hybrid attributes',
    long_description=(PROJECT_PATH / 'README.rst').read_text('utf-8'),
    url='https://github.com/DasIch/hybrid-attributes/',
    author='Daniel Neuhäuser',
    author_email='ich@danielneuhaeuser.de',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
