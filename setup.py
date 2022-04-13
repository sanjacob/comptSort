#!/usr/bin/env python3

"""Setup script for comptSort."""

from comptSort.__about__ import (__author__, __email__, __license__,
                                 __summary__, __title__, __uri__, __version__)
from setuptools import setup

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    url=__uri__,
    author=__author__,
    author_email=__email__,
    license=__license__)
