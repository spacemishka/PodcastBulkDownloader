#!/usr/bin/env python

from setuptools import setup

setup(name='Podcast Bulk Downloader',
      version='0.1',
      description='Simple software for downloading all the episodes of a podcast',
      author='Cyril Novel',
      author_email='podcast.bulk@kosmon.fr',
      install_requires=['requests', 'bs4', 'pytest']
     )