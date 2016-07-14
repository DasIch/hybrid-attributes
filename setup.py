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


_version_re = re.compile("__version__ = '(\d+\.\d+\.\d+)'")
def get_version():
    with (PROJECT_PATH / 'hybrid_attributes.py').open(encoding='utf-8') as f:
        for line in f:
            match = _version_re.match(line)
            if match:
                return match.group(1)
    raise ValueError('__version__ not found')


if __name__ == '__main__':
    setup(
        name='hybrid-attributes',
        version=get_version(),
        description='Hybrid attributes',
        long_description=(PROJECT_PATH / 'README.rst').read_text('utf-8'),
        url='https://github.com/DasIch/hybrid-attributes/',
        author='Daniel Neuhäuser',
        author_email='ich@danielneuhaeuser.de',
        classifiers=[
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: Implementation :: CPython'
        ],
        py_modules=['hybrid_attributes']
    )
