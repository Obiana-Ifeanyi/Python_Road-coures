def cube(int_num):
    # Cube of Number(x) = x to the power of 3; .where x = number

    # The number decreases by one at each iteration
    for i in range(int_num, -1, -1):

        if i > 0:
            # cube_of_number = i * i * i
            cube_of_number = i**3
            yield cube_of_number


