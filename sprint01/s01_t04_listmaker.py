#conversion of string to list using SPLIT() function
 # syntax 
 # x = txt.split(seperator)
def list_maker (string, delimiter):
 x = string.split (delimiter)
 print (x)

list_maker('hello my name is gris', " ")
list_maker('manksandkhumankboysk', 'k')
# the delimiter 'k' is used in separating the string for every 'k' present in the string



def string_maker (list1):
#conversion of list to string through ITERATING THROUGH LIST (loop)

 # an empty string is initialized to store list elements 
 my_string = " "
 for x in list1:
  my_string += ' ' + x

 print (my_string)

string_maker(['hello', 'my', 'name', 'is', 'gris'])
string_maker(['human', 'being'])
