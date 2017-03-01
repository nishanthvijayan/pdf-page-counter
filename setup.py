#!/usr/bin/env python

from setuptools import setup

setup(name='pdf-page-counter',
      version='0.1',
      description='Sum up the pages of all pdf files in a folder',
      url='http://github.com/nishanthvijayan/pdf-page-counter',
      author='Nishanth Vijayan',
      author_email='nishanththegr8@gmail.com',
      license='MIT',
      scripts=['bin/pdf-page-counter'],
      packages=['pdf-page-counter'],
      zip_safe=False)
