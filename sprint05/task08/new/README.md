DESCRIPTION 

In your script, you will need a logger, a logger decorator, and a class Knight. 
Use the class Knight that you have created for the Task 01 Knight. Add a magic method __new__() to the class. 
Use this method to forbid instantiating the class if there are already four instances made, 
or if the constructor receives a named argument name with the value 'Arthur'. On attempts to do so, 
log a corresponding error message. Pay attention that your logger must log messages to the stdout. 
Add a class attribute 'instances' to store all created instances. 

Create a decorator log(). Apply the decorator on each method of the Knight class. 
The decorator must log the name of the called method and the passed **kwargs in it 
