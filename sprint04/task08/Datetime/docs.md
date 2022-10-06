

Python datetime module

In Python, date and time are not a data type of their own,
but a module named datetime can be imported to work with the date as well as time.
Python Datetime module comes built into Python, so there is no need to install it externally. 
Python Datetime module supplies classes to work with date and time.
These classes provide a number of functions to deal with dates, times and time intervals. Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps. 


The DateTime module is categorized into 6 main classes – 

date – An idealized naive date, assuming the current Gregorian calendar always was,
and always will be, in effect. Its attributes are year, month and day.

time – An idealized time, independent of any particular day,
assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.

datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.

timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

tzinfo – It provides time zone information objects.

timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).


Date class
The date class is used to instantiate date objects in Python. When an object of this class is instantiated,
it represents a date in the format YYYY-MM-DD. Constructor of this class needs three mandatory arguments year, month and date.


Constructor syntax:  class datetime.date(year, month, day)


Example 1: Date object representing date in Python
# Python program to
# demonstrate date class

# import the date class
from datetime import date

# initializing constructor
# and passing arguments in the
# format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

# Uncommenting my_date = date(1996, 12, 39)
# will raise an ValueError as it is
# outside range

# uncommenting my_date = date('1996', 12, 11)
# will raise a TypeError as a string is
# passed instead of integer


source: 'https://www.geeksforgeeks.org/python-datetime-module/'





Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

Example
Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()

print(x)


output:
2022-09-27 19:48:01.076197

source: 'https://www.w3schools.com/python/python_datetime.asp'



Python | Create an empty text file with current date as its name
source: 'https://www.geeksforgeeks.org/python-create-an-empty-text-file-with-current-date-as-its-name/?ref=rp'



some other web resource on datetime module:

'https://docs.python.org/3/library/datetime.html'
'https://www.geeksforgeeks.org/get-current-date-and-time-using-python/'
'https://www.programiz.com/python-programming/datetime/current-datetime'


Also read on:
time module in python:
'https://realpython.com/python-time-module/'
'https://www.geeksforgeeks.org/python-time-module/'
