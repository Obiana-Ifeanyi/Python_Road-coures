def validator (expression):

    # split string into variable in 'number_1 operator number_2 Format.
    number_1, operator, number_2 = expression.split()

    # typecast the two number variables as float
    number_1, number_2 = float(number_1), float(number_2)

    # The operator may be: > , < , >= , <= , or ==. 
    if operator == '>' and number_1 > number_2:
        print (number_1 > number_2)

    elif operator == '<' and number_1 < number_2:
        print (number_1 < number_2)

    elif number_1 == number_2:
        if operator == '>':
            print (f"'{number_1} == {number_2}'")
        elif operator == '<':
            print (f"'{number_1} == {number_2}'")
        elif operator == '==':
            print (True)

    elif operator == '.':
        print (False)

    elif operator == '>=':
        print (f"'{number_1} <= {number_2}'")

    elif operator == '<=':
        print (f"'{number_1} >= {number_2}'")

    elif operator == '==':
        print (f"'{number_1} >= {number_2}' or '{number_1} <= {number_2}'")


validator('6 > 5')
