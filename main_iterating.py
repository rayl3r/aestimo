#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aestimo 1D Schrodinger-Poisson Solver

main_iterating module:
----------------------
This script shows how we can simulate a design several times while varying a
parameter over a range of values.
"""

__author__    = "For the list of contributors, see ~/AUTHORS.md"
__copyright__ = "Copyright (C) 2013-2017 Sefer Bora Lisesivdin and Aestimo group"
__license__   = "GPLv3+ WITHOUT ANY WARRANTY"
__version__   = "1.2.0"

import matplotlib.pyplot as pl
import numpy as np
import os

# aestimo modules
import aestimo
import config
inputfile = __import__(config.inputfilename) 
import database

### Example: Parameter to loop over.
#thickness of first layer of structure
thicknesses = [8,12,14,16,20] #nm
        
# Initialise structure class
model = aestimo.StructureFrom(inputfile,database)

# Looping over the parameter
"""In order to write the code correctly, it is necessary to have 
understood the Structure class and it's attributes. Some of the 
input file variables and the class's attribute use different names
but they are normally easy to match up. Alternatively, we could vary the 
(runtime values of the) variables within inputfile module's namespace
and then create a fresh Structure class instance.

Equally, we can vary the values in the database module if we want to."""

results = []
output_directory = config.output_directory+'-numpy' # will be our local copy of the original value

for thickness in thicknesses:
    model.material[0][0] = thickness
    #other examples -
    #model.Fapp = ... #equivalent to Fapplied
    #model.subnumber_e = ...
    #model.dx = gridfactor*1e-9
    #database.materialproperty['GaAs']['epsilonStatic']= ...
    
    model.create_structure_arrays() # update the instance's internals
    
    # Perform the calculation
    result= aestimo.Poisson_Schrodinger(model)
    
    results.append(result) #all the results can be stored for further analysis. 
    
    # Set output directory 
    # aestimo_numpy reads the output directory from the config module, so
    config.output_directory = os.path.join(output_directory,'dz0_%dnm' %thickness)

    # Write the simulation results in files
    aestimo.save_and_plot(result,model)
    
    #Plot QW representation
    #aestimo.QWplot(result)#,figno=None) # an alternative to save_and_plot function
                                            # which only plots the QW diagram and doesn't
                                            # save anything.

print("Simulation is finished. All files are closed.")
print("Please control the related files.")
