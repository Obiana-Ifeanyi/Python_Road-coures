• What is inheritance? 
    It refers to defining a new class with little or no modification to an existing class.
    The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
    'https://www.w3schools.com/python/python_inheritance.asp'
    'https://www.geeksforgeeks.org/inheritance-in-python/'
    'https://realpython.com/inheritance-composition-python/#whats-inheritance'

• What is the difference between inheritance and composition?
    Inheritance models what is called an is a relationship. This means that when you have a Derived class that inherits from a Base class, 
    you created a relationship where Derived is a specialized version of Base.

    Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. 
    This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.

 
• What does it mean to have an 'is a' relation (in programming)?
    IS-A Relationship:
    In object-oriented programming, the concept of IS-A is a totally based on Inheritance, 
    which can be of two types Class Inheritance or Interface Inheritance. It is just like saying "A is a B type of thing". 
    For example, Apple is a Fruit, Car is a Vehicle etc. Inheritance is uni-directional.
    For example, House is a Building. But Building is not a House.

• What are the beneﬁts of using inheritance?
    -Use inheritance to express an is a relationship between two classes 
    - multiple inherenace can be used 

• What class do all classes in Python inherit by default? 
    every class you create in Python implicitly derives from the object super class. 
    You could be more explicit and write class MyClass(object): for the parent class, but it’s redundant and unnecessary.
    'https://realpython.com/inheritance-composition-python/#the-object-super-class'

• What is multiple inheritance? 
    Python is one of the few modern programming languages that supports multiple inheritance. 
    Multiple inheritance is the ability to derive a class from multiple base classes at the same time.
    'https://realpython.com/inheritance-composition-python/#inheriting-multiple-classes'

• How to call the __init__() method of the immediate parent class without specifying the name of the parent class?
    by using the super() method
    ex: super().__init__()
    'https://www.geeksforgeeks.org/python-call-parent-class-method/'

