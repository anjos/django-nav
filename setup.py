#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 14 Set 2009 14:42:06 CEST 

"""Installation instructions for djangoogle
"""

from setuptools import setup, find_packages

setup(

    name = "nav",
    version = "0.1.1", 
    packages = find_packages(),

    # we also need all translation files and templates
    package_data = {
      'nav': [
        'locale/*/LC_MESSAGES/django.po',
        'locale/*/LC_MESSAGES/django.mo',
        ],
      },

    zip_safe=False,

    install_requires = [
      'Django>=1.1',
      'docutils',
      ],

    dependency_links = [
      'http://docutils.sourceforge.net/docutils-snapshot.tgz',
      ],

    # metadata for upload to PyPI
    author = "Andre Anjos",
    author_email = "andre.dos.anjos@gmail.com",
    description = "Provides re-arrangeable menus with translations",
    license = "PSF",
    keywords = "django menu",
    url = "",   # project home page, if any
    
)

