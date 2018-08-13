print("Hello, World!")
print("Hello, 🌎")
print('Hello, 🌝')

import sys
print("To the error!", file=sys.stderr)

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("This is a log message.")
logging.info("My info for: %s", "Chris")
logging.warn("I'm WARNing you, it's coming!")
logging.error("Escalating to an %s", "ERROR")
logging.critical("RED ALERT RED ALERT - CRITICAL")




