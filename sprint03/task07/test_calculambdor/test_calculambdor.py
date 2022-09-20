def calculator(math_operations, num_1, num_2):

    # NUMBER MUST BE (int or ﬂoat).
    if num_1 != float(num_1) or num_2 != float(num_2):
        raise ValueError('Invalid numbers. Second and third arguments must be numerical.')


    # MATH OPERATIONS
    if math_operations == 'add':
        result = num_1 + num_2
        return result

    elif math_operations == 'sub':
        result = num_1 - num_2
        return result

    elif math_operations == 'mul':
        result = num_1 * num_2
        return result

    elif math_operations == 'div':
        result = num_1 / num_2
        return result

    elif math_operations == 'pow':
        result = num_1 ** num_2
        return result

    elif math_operations != 'add' or math_operations != 'div' or math_operations != 'sub' or math_operations != 'mul' or math_operations != 'pow':
        raise ValueError('Invalid operation. Available operations: add, sub, mul, div, pow.')




math_operations = 'mul'
num_1 = 9
num_2 = 2.4


print (calculator(math_operations, num_1, num_2))
