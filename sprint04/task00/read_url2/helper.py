'''
create a ﬁle-module helper.py
that contains two functions:
• print_stderr() prints a given error message to stderr in the format 'ERROR| [message].'
  and exits the program

• print_stdout() prints a given info message to stdout in the format 'INFO| [message].'
'''


import sys
def print_stdout(rex):

    b = f"INFO| {rex}"
    print (b)  # note by default print fn are sent to standard output



import sys
def print_stderr(err):

    b = f"ERROR| {err}"
    print (b, file = sys.stderr)



# REFERENCE:
# 'https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/'
