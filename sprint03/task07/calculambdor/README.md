Create a script that contains a function calculator() and a global variable operations.
The function takes three arguments: a string with a name of a mathematical operation and two numbers (int or ﬂoat).
The calculator() function returns the result of the given operation on the two numbers.
Available operations and their names:

    • + - add

    • - - sub

    • * - mul

    • / - div

    • ** - pow

operations must be a dictionary of lambda functions,
where the operation names listed above are the keys, and the lambdas are the values.
If the passed values are invalid, raise a ValueError with a relevant message:

    'Invalid numbers. Second and third arguments must be numerical.' or

    'Invalid operation. Available operations: add, sub, mul, div, pow.'.
