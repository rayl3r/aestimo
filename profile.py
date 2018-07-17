#!/bin/env python
# -*- coding: utf-8 -*-
"""Aestimo 1D Schrodinger-Poisson Solver

profile module:
---------------
Simple script for profiling aestimo using the cProfile module.
"""

__author__    = "For the list of contributors, see ~/AUTHORS.md"
__copyright__ = "Copyright (C) 2013-2017 Sefer Bora Lisesivdin and Aestimo group"
__license__   = "GPLv3+ WITHOUT ANY WARRANTY"
__version__   = "1.2.0"

import cProfile
command = """import main"""
cProfile.runctx( command, globals(),locals(),filename="aestimo_numpy-0.8.3.profile")

#command = """import aestimo"""
#cProfile.runctx( command, globals(), locals(), filename="aestimo_t8.profile" )

#command = """import main"""
#cProfile.runctx( command, globals(), locals(), filename="aestimo_numpy.profile" )
