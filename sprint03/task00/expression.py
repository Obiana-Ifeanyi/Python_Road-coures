"""
DESCRIPTION
Create a script that contains a lambda function.
The lambda function must return True or False based on whether n  is divisible by both a and b  with a remainder of 0.
"""

# if-else condition in lambda python
# lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>

result = lambda n, a, b: True if (n % a == 0 and n % b == 0) else False

n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

print (result(n, a, b))
