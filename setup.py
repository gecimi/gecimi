#!/usr/bin/python
#coding=utf-8

from distutils.core import setup
from gecimi import __version__

setup(name='gecimi',
      version=__version__,
      description='A python sdk of gecimi.com',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      py_modules=['gecimi'],
      scripts=['gecimi.py'],
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/gecimi')
