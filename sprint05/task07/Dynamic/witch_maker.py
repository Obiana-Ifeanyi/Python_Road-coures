# base class to be used by the dynamically created child class
class Witch:
    def __init__(self, name):
        self.name = name

# function that dynamically creates a child class with the class above as its base class
def get_witch_class(class_name, specialty, skills = []):

    '''
    create a dictionary that takes in attributes and methods as the 3rd argument of the type function takes a dictionary
    '''
    dictt = {}
    dictt['specialty'] = specialty

    # for methods in skills add method to dictionary, method name as key and method as value
    for method in skills:
        dictt[method.__name__] = method

    # creating class dynamically
    sub_witch = type(class_name, (Witch,), dictt)
    return sub_witch
