'''
DESCRIPTION
Create a script with a function extractor()
that ﬁlters a dictionary according to a certain data type of the values.
It takes two arguments: a dictionary extractable
and a data type value_type (an instance of class type, e.g., int, bool, etc).
value_type has the default value of str.
The function uses ﬁlter()
to create a new dictionary that only contains the items from extractable that have a value of type value_type.
'''


def  extractor(extractable, value_type = str):
    # using isinstance and dictionary comprehension
    rex = {key : val for key, val in extractable.items() if isinstance(val, value_type)}
    return rex

