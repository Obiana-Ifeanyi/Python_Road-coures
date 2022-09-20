add = lambda n1, n2: n1 + n2
sub = lambda n1, n2: n1 - n2
mul = lambda n1, n2: n1 * n2
div = lambda n1, n2: n1 / n2
pow = lambda n1, n2: n1 ** n2

operations = {
    'add': (add),
    'sub': (sub),
    'mul': (mul),
    'div': (div),
    'pow': (pow)
    }


def calculator(math_operations, num_1, num_2):
    global operations

    if num_1 != float(num_1) or num_2 != float(num_2):
        raise ValueError('Invalid numbers. Second and third arguments must be numerical.')

    if math_operations == 'add':
        result = add(num_1, num_2)
        return result

    elif math_operations == 'sub':
        result = sub(num_1, num_2)                   #num_1, operations['sub'], num_2
        return result

    elif math_operations == 'mul':
        result = mul(num_1, num_2)              #num_1, operations['mul'], num_2
        return result

    elif math_operations == 'div':
        result = div(num_1, num_2)                  #num_1, operations['div'], num_2
        return result

    elif math_operations == 'pow':
        result = pow(num_1, num_2)                   #num_1, operations['pow'], num_2
        return result

    elif operations != 'add' or operations != 'div' or operations != 'sub' or operations != 'mul' or operations != 'pow':
        raise ValueError('Invalid operation. Available operations: add, sub, mul, div, pow.')

math_operations = 'div'
num_1 = 3
num_2 = 2


print (calculator(math_operations, num_1, num_2))

