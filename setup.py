
#!/usr/bin/python
#coding=utf-8

import sys
sys.path.append('./src')

from distutils.core import setup
from gecimi import __version__

setup(name='gecimi',
      version=__version__,
      description='A python sdk of gecimi.com',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      packages=['gecimi'],
      package_dir={'gecimi': 'src/gecimi'},
      package_data={'gecimi': ['stuff']},
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/gecimi')
