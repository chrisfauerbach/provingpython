import json
import logging
import os
import sys
import time
from time import gmtime, strftime

### pipenv install flask
### Import 3rd party libraries AFTER built ins
### That's some standard.  Follow it!

from flask import Flask

__author__ = "Chris Fauerbach"
__copyright__ = "Copyright 2018, Fauerbach Consulting"
__credits__ = ["Chris Fauerbach"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Chris Fauerbach"
__email__ = "chris@fauie.com"
__status__ = "Development"

#Global scope logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#Global scope app
app = Flask(__name__)

@app.route("/")
def hello():
  """
  Returns a simple string the web client.
  """
  logging.debug("About to return a string!")
  return "Hello World!"


@app.route("/json")
def foo():
  """
  Makes a dict (we'll get to that), uses the json library
  to make an output string, retval, then returns it.
  """
  logging.debug("Setting a string, then returning")
  ### See the embedded dict? foo=bar
  retval  = json.dumps({"foo":"bar"})
  return(retval)
 