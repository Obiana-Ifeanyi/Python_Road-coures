'''
What is the purpose of the method __new__()?
    When we talk about magic method __new__ we also need to talk about __init__
    These methods will be called when you instantiate(The process of creating instance from class is called instantiation). 
    That is when you create instance. The magic method __new__ will be called when instance is being created. 
    Using this method you can customize the instance creation. This is only the method which will be called first then __init__ will be 
    called to initialize instance when you are creating instance.

    Method __new__ will take class reference as the first argument followed by arguments which are passed to 
    constructor(Arguments passed to call of class to create instance). Method __new__ is responsible to create instance, 
    so you can use this method to customize object creation. Typically method __new__ will return the created instance object reference. 
    Method __init__ will be called once __new__ method completed execution.

    You can create new instance of the class by invoking the superclass’s __new__ method using super. 
    Something like super(currentclass, cls).__new__(cls, [,….])

    You can create instance inside __new__  method either by using super function in the __new__ method or 
    by directly calling __new__ method over object  Where if parent class is object. That is,


    EXAMPLE:
    instance = super(MyClass, cls).__new__(cls, *args, **kwargs)
    return instance
    or
    instance = object.__new__(cls, *args, **kwargs)

    'https://howto.lintel.in/python-__new__-magic-method-explained/'
    'https://www.geeksforgeeks.org/__new__-in-python/'
    'https://www.pythontutorial.net/python-oop/python-__new__/'
    'https://www.codevoila.com/post/68/new-and-init-in-python'
    'https://realpython.com/python-class-constructor/#object-creation-with-__new__'

What does __new__() return?
    The __new__() method should return a new object of the class. But it doesn’t have to.


How to count the instances of a class?
     
Ex1:
class Obj:
    _counter = 0
    def __init__(self):
        Obj._counter += 1
        self.id = Obj._counter

Ex2:
global_next_id = 1

class Obj:
  def __init__(self):
    global global_next_id
    self.id = global_next_id

    global_next_id += 1

'https://www.geeksforgeeks.org/how-to-count-number-of-instances-of-a-class-in-python/'
