from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
import aestimo_eh
import aestimo

import database as adatabase
from pprint import pprint

pprint(adatabase.materialproperty['AlGaN'])