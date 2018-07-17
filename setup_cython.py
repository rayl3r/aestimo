#!/bin/env python
# -*- coding: utf-8 -*-
"""Aestimo 1D Schrodinger-Poisson Solver

setup_cython module:
--------------------
This module compiles the cythonised version of the psi_at_inf function used
by the aestimo.py shooting method (but not by aestimo_eh.py). See 
psi_at_inf_cython.pyx

Compile the cythonised function with the command:
   python setup_cython.py build_ext --inplace
or on windows:
   python setup_cython.py build_ext --inplace --compiler=mingw32

aestimo.py will then automatically use this faster version as long as the 
config.py module contains `use_cython = True`.
"""

__author__    = "For the list of contributors, see ~/AUTHORS.md"
__copyright__ = "Copyright (C) 2013-2017 Sefer Bora Lisesivdin and Aestimo group"
__license__   = "GPLv3+ WITHOUT ANY WARRANTY"
__version__   = "1.2.0"

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [Extension("psi_at_inf_cython", ["psi_at_inf_cython.pyx"])]

setup(
  name = 'psi_at_inf',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  include_dirs=[numpy.get_include()]
)
