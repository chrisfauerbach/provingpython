#!/usr/bin/env python
"""
Focus on dealing with databases within python.  nothing crazy, 
or even a super focus on SQL, RDBMS, NoSQL, etc.
Just some basic patterns.
"""
import logging
import os
import sys 

# SQLite is a super great 'file' based database.   No big engine
# or server to run.  Just a SQL compliant local database.
import sqlite3

__author__ = "Chris Fauerbach"
__copyright__ = "Copyright 2018, Fauerbach Consulting"
__credits__ = ["Chris Fauerbach"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Chris Fauerbach"
__email__ = "chris@fauie.com"
__status__ = "Development"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def database_driven(f):
    """
    This is a special decorator that passes a database cursor
    to the function that needs it.  Great way to manage 
    cursors and transactions
    """
    def database_driven_(*args, **kwargs):    
      conn = sqlite3.connect('fauie.db')
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
    return database_driven_

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
      conn = sqlite3.connect('fauie.db')
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


@database_driven
def more_advanced_database(c):
  for x in range(10):
    # NEVER DO THIS
    # c.execute("INSERT INTO stocks VALUE (%s, 'BUY', 'MMM', %s, %s" % x, x*1000, x**x)
    # HELLA insecure.  Look up SQL Injection
    print(x)
    print(x*1000)
    print(x*x)
    result = c.execute("INSERT INTO stocks VALUES ('2017-02-12', 'BUY', 'MMM', ?, ?)", ( x*1000, x**2,))
    logging.info("Another record into advanced database: %s", result.lastrowid)
    
@database_driven
def get_some_records(c):
  #Pull single record
  c.execute("SELECT * FROM stocks")
  logging.info("One Row: %s", c.fetchone())

  # Iterate over multiple records
  for x in c.execute("SELECT * FROM stocks"):
    logging.info(x)

   
@database_driven_dict
def get_some_records_dict(c): 
  # Iterate over multiple records
  for x in c.execute("SELECT * FROM stocks"):
    logging.info(x)


def basic_database():
  conn = sqlite3.connect('fauie.db')
  c = conn.cursor()
  # Create table
  c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
  
  # Insert a row of data
  for _ in range(10):
    result2 = c.execute("INSERT INTO stocks VALUES ('2016-02-12','BUY','TSLA',1000, 151.04)")
    logging.info("Result from insert is rowid: %s", result2.lastrowid)
  # Save (commit) the changes
  conn.commit()
  
  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  conn.close()

if __name__ == "__main__":
  basic_database()
  more_advanced_database()
  get_some_records()
  get_some_records_dict()