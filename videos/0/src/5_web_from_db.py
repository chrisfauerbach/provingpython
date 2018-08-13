import json
import logging
import os
import sys
import time
from time import gmtime, strftime
import sqlite3



### pipenv install flask
### Import 3rd party libraries AFTER built ins
### That's some standard.  Follow it!

from flask import Flask
from flask import jsonify
from flask import request


__author__ = "Chris Fauerbach"
__copyright__ = "Copyright 2018, Fauerbach Consulting"
__credits__ = ["Chris Fauerbach"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Chris Fauerbach"
__email__ = "chris@fauie.com"
__status__ = "Development"

def dict_factory(cursor, row):
    """
    Super simple function to convert a row to a dict.
    Using meta-data (description) from the cursor. we'll
    make a dict, populate it, and return it.
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def database_driven_dict(f):
    """
    This is a special decorator that passes a database cursor
    to the function that needs it.  Great way to manage 
    cursors and transactions
    """
    def database_driven_dict_(*args, **kwargs):    
      conn = sqlite3.connect('fauie2.db')
      conn.row_factory = dict_factory
      c = conn.cursor()
      try:
        rv = f(c, *args, **kwargs)
      except Exception:
        conn.rollback()
        raise
      else:
        conn.commit() # or maybe not
      finally:
        conn.close()
      return rv
    return database_driven_dict_




#Global scope logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#Global scope app
app = Flask(__name__)


@app.before_first_request
@database_driven_dict
def create_database(c): 
  # Create table
  try:
    c.execute("""CREATE TABLE blog_posts
             ( id INTEGER PRIMARY KEY AUTOINCREMENT
             , subject varchar
             , message varchar
             , ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
  except:
    logging.info("Database table probably already exists.")
 

@database_driven_dict
def get_post_by_id(c, post_id):
  c.execute("select * from blog_posts where id = ?", (post_id,))
  return c.fetchone() or {}
  

@database_driven_dict
def add_new_record(c, data_record):
  # logging.info("IN THE INSERT: %s", str(data_record))
  # logging.info(data_record.get('subject',''))
  # logging.info(data_record.get('message',''))
  c.execute("INSERT INTO blog_posts(subject, message) values(?, ?)", 
            (data_record.get('subject',''), data_record.get('message',''),)
  )

@database_driven_dict
def get_post_ids(c): 
  retval = []
  # Iterate over multiple records
  for x in c.execute("SELECT id FROM blog_posts"):
    logging.info(x)
    retval.append(x)
  return retval


@app.route("/")
def posts():
  """
  Returns a simple string the web client.
  """
  logging.debug("About to return some database records.")
  records = get_post_ids()
  return jsonify(records)


@app.route("/<int:post_id>",)
def posts_by_id(post_id):
  """
  Makes a dict (we'll get to that), uses the json library
  to make an output string, retval, then returns it.
  """
  logging.debug("Setting a string, then returning")
  ### See the embedded dict? foo=bar
  retval  = json.dumps({"foo":"bar"})
  return jsonify(get_post_by_id(post_id))
 
@app.route('/', methods=['POST'])
def post_new_post():
  request_data = json.loads(request.data)
  print(request_data)
  # logging.info(json.dumps(request_data))
  add_new_record(request_data)
  return jsonify(request_data)