DESCRIPTION 

Create a class Witch and a function get_witch_class() that dynamically creates and 
returns a child class of Witch. 

The class Witch must have an __init__() method that takes a parameter name and sets 
the instance's name to that value. 

The function get_witch_class() takes three positional arguments: 
    • class_name - the name of the class to be created 

    • specialty - the value of the specialty class attribute 

    • skills - a list of functions that must become the methods of the new class 

The function must create a class with the name given as the class_name argument. 
The newly created class must inherit the class Witch. The class must have an attribute specialty, 
set to the value given as the specialty argument. 

Also, the class must have the methods given as a list in the skills attribute.
