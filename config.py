#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aestimo 1D Schrodinger-Poisson Solver

config module:
--------------
This module contains aestimo's global configuration settings for aestimo.py
and aestimo_eh.py. It contains parameters for controlling the algorithms that are 
used to calculate the bandstructures. 

The 'inputfilename' variable defines the default input file used when aestimo.py
or main.py is run directly as a script. There are also parameters that define the
defaults for saving and presenting results; as well as for logging messages.
"""

__author__    = "For the list of contributors, see ~/AUTHORS.md"
__copyright__ = "Copyright (C) 2013-2017 Sefer Bora Lisesivdin and Aestimo group"
__license__   = "GPLv3+ WITHOUT ANY WARRANTY"
__version__   = "1.2.0"

q = 1.602176e-19 #C
meV2J=1e-3*q #meV to Joules

# CONFIGURATION 

# Default Input File(s)
# -------------
#inputfilename = "sample_qw_barrierdope"
#inputfilename = "sample_qw_qwdope"
#inputfilename = "sample_moddop"
#inputfilename = "sample_qw_HarrisonCh3_3"
#inputfilename = "sample_qw_barrierdope_p"
#inputfilename = "sample_multi_qw_barrierdope_p"
#inputfilename = "sample_double_qw"
#inputfilename = "sample_qw_barrierdope_p_ingan"
#inputfilename = "sample_qw_barrierdope_p_cdzno"
#inputfilename = "sample_multi_qw_barrierdope_p_ingan"
#inputfilename = "sample_qw_wide_isbt"
#inputfilename = "sample_qw_barrierdope_p_InGaAsP"
inputfilename = "sample_qw_barrierdope_p_AlGaInN"
#inputfilename = "sample_qw_barrierdope_p_AlGaInN_2"
# Calculation
# -----------
# Aestimo
use_cython = True #provides a speed up for aestimo
# Shooting method parameters for Schrödinger Equation solution
delta_E = 0.5*meV2J #Energy step (Joules) for initial search. Initial delta_E is 1 meV. 
d_E = 1e-5*meV2J #Energy step (Joules) within Newton-Raphson method when improving the precision of the energy of a found level.
E_start = 0.0    #Energy to start shooting method from (if E_start = 0.0 uses minimum of energy of bandstructure)
Estate_convergence_test = 1e-9*meV2J
# FermiDirac
FD_d_E = 1e-9 #Initial and minimum Energy step (meV) for derivative calculation for Newton-Raphson method to find E_F
FD_convergence_test = 1e-6 #meV
np_d_E = 1.0 # Energy step (meV) for dispersion calculations
# Poisson Loop
damping = 0.5    #averaging factor between iterations to smooth convergence.
max_iterations=80 #maximum number of iterations.
convergence_test=1e-6 #convergence is reached when the ground state energy (meV) is stable to within this number between iterations.

# Aestimo_eh
anti_crossing_length=1 # the lower lenght limit to consider anti-crossing (nm)
strain =True # for aestimo_eh
piezo=True # directly calculationg the induced electric field.
#--------------
parameters=False

# Output Files
# ------------
output_directory = "outputs"
parameters = True
electricfield_out = True
potential_out = True
sigma_out = True
probability_out = True
states_out = True

# Result Viewer
# -------------
resultviewer = True
wavefunction_scalefactor = 200 # scales wavefunctions when plotting QW diagrams
# Messages
# --------
messagesoff = False
logfile = 'aestimo.log'

