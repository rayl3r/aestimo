#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aestimo 1D Schrodinger-Poisson Solver

main module:
------------
This file is one method of running aestimo. Simply define the input file in 
the config.py module and run this script. We could also run aestimo.py directly
to achieve the same effect. 

Alternatively, many of the example input files show how we can transform them
into scripts that can be run directly to perform the simulations. That approach
also allows us to tailor each simulation even more to our needs.
"""

__author__    = "For the list of contributors, see ~/AUTHORS.md"
__copyright__ = "Copyright (C) 2013-2017 Sefer Bora Lisesivdin and Aestimo group"
__license__   = "GPLv3+ WITHOUT ANY WARRANTY"
__version__   = "1.2.0"

#import matplotlib.pyplot as pl
#import numpy as np
#import time
#import sys 

import config

#import aestimo_eh as aestimo
import aestimo
    

# Import from config file
inputfile = __import__(config.inputfilename)
aestimo.logger.info("inputfile is %s" %config.inputfilename)

if __name__=="__main__":
    aestimo.run_aestimo(inputfile)


