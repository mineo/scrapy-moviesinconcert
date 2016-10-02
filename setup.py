#!/usr/bin/env python2
from __future__ import print_function
from codecs import open
from setuptools import setup


setup(name="scrapy-moviesinconcert",
      author="Wieland Hoffmann",
      author_email="themineo@gmail.com",
      packages=["scrapy_moviesinconcert"],
      package_dir={"scrapy_moviesinconcert": "scrapy_moviesinconcert"},
      download_url=["https://github.com/mineo/scrapy-moviesinconcert/tarball/master"],
      url=["http://github.com/mineo/scrapy-moviesinconcert"],
      license="MIT",
      classifiers=["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7"],
      description="",
      long_description=open("README.txt", encoding="utf-8").read(),
      setup_requires=["setuptools_scm"],
      use_scm_version={"write_to": "scrapy_moviesinconcert/version.py"},
      extras_require={
          'docs': ['sphinx']
      }
      )
