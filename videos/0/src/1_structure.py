#!/usr/bin/env python
"""
Second introduction python program!  
We looked at the print() function, and then showed
you why not to use it!

This program shows a function declaration, and things
about timestamps!
"""
import logging
import os
import sys
import time
from time import gmtime, strftime

__author__ = "Chris Fauerbach"
__copyright__ = "Copyright 2018, Fauerbach Consulting"
__credits__ = ["Chris Fauerbach"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Chris Fauerbach"
__email__ = "chris@fauie.com"
__status__ = "Development"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def what_time_is_it():
  """
  Function to log some information about the current time.  
  returns the current time in a time_struct format
  Example:
  time.struct_time(tm_year=2018, tm_mon=8, tm_mday=11, 
                   tm_hour=1, tm_min=37, tm_sec=34, 
                   tm_wday=5, tm_yday=223, tm_isdst=0)
  """
  float_ts = time.time()
  current_ts = time.gmtime()
  current_ts_string = strftime("%a, %d %b %Y %H:%M:%S +0000", current_ts)
  logging.info("         Float TS: %s", str(float_ts))
  logging.info("       Current TS: %s", current_ts)
  logging.info("Current TS String: %s", current_ts_string)
  return current_ts

if __name__ == "__main__":
  """
  Main function. Primary entry point.
  """
  logging.info(what_time_is_it())
