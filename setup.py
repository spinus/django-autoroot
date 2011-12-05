#!/usr/bin/env python
# encoding: utf-8
from distutils.core import setup
from setuptools import find_packages
from os import path 

setup(author="Tomek Czyż",
      author_email='tomekczyz@gmail.com',
      description='automaticly creates root user after syncdb if not exists',
      long_description='''
      After syncdb's signal is called, root user is created (if not exists).
      Default settings creates root:root@localhost:qqq user, but
      you can customize it in settings by 

      AUTOROOT_NAME
      AUTOROOT_EMAIL
      AUTOROOT_PASSWORD

      and 

      AUTOROOT_DEBUG_ONLY (default True)

      Code is stolen from:
      http://djangosnippets.org/snippets/1875/
      ''',

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
      keywords="django user create syncdb root",
      packages=find_packages('.'),
      )
