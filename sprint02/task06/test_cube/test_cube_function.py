def cubes(number):
    # Cube of Number(x) = x to the power of 3
    # where x = number

    return number*number*number


def getCubes(int_num):

    for i in range(1, (int_num + 1)):
        if i > 0:
            yield cubes(i)


int_num = 10
getCubes(int_num)

for num in getCubes(int_num):
    print (num)
