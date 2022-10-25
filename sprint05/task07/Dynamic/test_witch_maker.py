
# base class to be used by the dynamically created child class
class Witch:
    def __init__(self, name):
        self.name = name


# function that dynamically creates a child class with the class above as its base class
def get_witch_class(class_name, specialty, skills = []):

    #meth = skills
    #sub_witch = type(class_name, (Witch,), meth)


    sub_witch = type(class_name, (Witch,), {'specialty': specialty})
    return sub_witch

    # The class must have an attribute specialty, set to the value given as the specialty argument


'''
# base class to be used by the dynamically created child class
class Witch:
    def __init__(self, name):
        self.name = name


# function that dynamically creates a child class with the class above as its base class
def get_witch_class(class_name, specialty, skills = []):
 
    #meth = skills
    #sub_witch = type(class_name, (Witch,), meth)

    for i in skills:
        sub_witch = type(class_name, (Witch,), {'specialty': specialty, i: 'gris'})

        return sub_witch
'''
