# coding: utf-8

# The MIT License (MIT)
#
# Copyright 2016 Alan Fachini <https://github.com/alfakini/python-mercadobitcoin>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from distutils.core import setup


INSTALL_REQUIREMENTS = ['requests']

setup(
    name = 'mercadobitcoin',
    description = 'A Python wrapper for Mercado Bitcoin API',
    version = '0.6.0',
    packages = ['mercadobitcoin'],
    author = 'Alan Fachini',
    author_email = 'alfakini@gmail.com',
    url = 'https://github.com/alfakini/python-mercadobitcoin',
    download_url = 'https://github.com/alfakini/python-mercadobitcoin/tarball/0.6.0',
    keywords = ['bitcoin', 'litcoin', 'ethereum', 'ripple', 'mercadobitcoin', 'trade', 'orderbook'],
    install_requires=INSTALL_REQUIREMENTS,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
