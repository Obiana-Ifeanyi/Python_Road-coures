'''
DESCRIPTION
Create a script that contains a function called multiplier().
It takes a list of numbers: int and/or ﬂoat,
and returns the result of their multiplication.
If the argument is not of type list or its elements are not all numerical (use the all() function),
raise a ValueError with a message 'The given data is invalid.'.
Use a lambda function in combination with the reduce() function in your implementation.
Import the appropriate module.
'''


def multiplier(list_of_num):
    from functools import reduce

    list_of_num != list(list_of_num)

    for i in list_of_num:
        if i != float(i) or all(list_of_num) is False:
            raise ValueError('The given data is invalid.')

        else:
            result = reduce(lambda a, b:a * b, list_of_num)
            return result




# REFERENCE MATERIALS
# **** #
# 'https://www.programiz.com/python-programming/methods/built-in/all'
# 'https://www.geeksforgeeks.org/python-all-function/'
# 'https://www.geeksforgeeks.org/functools-module-in-python/'
# 'https://realpython.com/lessons/functools-module/'
# 'https://realpython.com/python-reduce-function/'
# 'https://www.geeksforgeeks.org/reduce-in-python/'
