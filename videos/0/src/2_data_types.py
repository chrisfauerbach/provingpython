import json


### Removing the proper way to output logs, and using
### print() instead.  print is still 100% acceptable when
### sending data to the standard out.  It's just not acceptable
### for logging!! 


__author__ = "Chris Fauerbach"
__copyright__ = "Copyright 2018, Fauerbach Consulting"
__credits__ = ["Chris Fauerbach"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Chris Fauerbach"
__email__ = "chris@fauie.com"
__status__ = "Development" 

### I'll use underscores to create a variable with the name
### of the data type
_int = 3
print(_int)
print(type(_int))

_float = 1.4
print(_float)
print(type(_float))

_complex = 3.14j
print(_complex)
print(type(_complex))  #Yeah, this is math stuff


_str = "This is a string!"
print(_str)
print(type(_str))

_str2 =  "Hello, 🌎!"
print(_str2)
print(type(_str2))
### Don't forget, arrays are all 0 based, 
### cause you know, computers.
print(_str2[0]) # First Character
print(_str2[3:5]) # 3rd through 5, exclusive
print(_str2[-1:]) # Last character
print(_str2[-2:-1]) # Second to last
print(_str2[2:]) # 2nd to the end!

_long_string = """This is a pre formatted
string that the user
will be able to view as is."""
print(_long_string)
print(_long_string.replace("\n","|"))


_list = ["One Fish", "Two Fish", "Red Fish"]
print(_list)
print(type(_list))
_list.append("Blue Fish")
print(_list)
_list.insert(0, "Dr. Seuss Says:")
print(_list)
### BEST FUNCTION EVER
print(", ".join(_list))
print(_list[0:1])
print(_list[-2:])
print("Same as a string.")

### Use a list as a stack, pseudo type
### Last in, first out.  Push(append) and pop (built in)
_stack = []
_stack.append("First")
_stack.append("Second")
_stack.append("Third")
print(_stack)
print(_stack.pop())
print(_stack)
print(_stack.pop())
print(_stack)
print(_stack.pop())
print(_stack)

### Use a list as a queue, pseudo type
### First in, First out.  Insert, pop
_queue = []
_queue.insert(0, "First")
_queue.insert(0, "Second")
_queue.insert(0, "Third")
print(_queue)
print(_queue.pop())
print(_queue)
print(_queue.pop())
print(_queue)
print(_queue.pop())
print(_queue)


### Onto the tuple!
### Like a list, but in parenthesis
_tuple = ('one,', 'two','three',)

try: 
  _tuple[1] = 'dog'
except:
  ### Fixed size, immutable, read-onl
  print("Just kidding!   READ ONLY!")

print(_tuple)
print(type(_tuple))
print(_tuple[1:])
print("Yep.. same!")

### Dictionary.  My favorite!

_dict = {"foo":"bar"}
print(_dict)
print(type(_dict))
### <class 'dict'>  That's new.  We'll get to that
_dict["state"] = "Virginia"
_dict[1] = "Integer Value"
_dict["likes"] = ['Walking on the beach','Reading a book','Pizza']
print(_dict)
print(json.dumps(_dict)) ### Note the KEY of "1"









