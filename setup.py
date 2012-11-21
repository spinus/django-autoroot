#!/usr/bin/env python
# encoding: utf-8
from distutils.core import setup
from setuptools import find_packages

setup(author="Tomek Czyż",
      author_email='tomekczyz@gmail.com',
      description='automaticly creates `root` user after syncdb if not exists',
      long_description=open('README.rst').read(),
      license="BSD",
      platforms='OS Independent',
      name="django-autoroot",
      url="http://github.com/spinus/django-autoroot",
      classifiers=[
                   "Environment :: Web Environment",
                   "Framework :: Django",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      version="0.1.1",
      keywords="django user create syncdb",
      packages=find_packages('.'),
      )
