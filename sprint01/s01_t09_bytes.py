# Create a script that converts these variables(string, bool and integer) into bytes

def bytess(first_a, second_a, third_a):

    ## Casts the ﬁrst argument to integer, the second to boolean (True, False) and the third to string.
    first_a, second_a, third_a = int(first_a), bool(second_a), str(third_a)


    # Converts these variables into bytes.
    # Python byte() function converts an object to an immutable byte-represented object of given size and data.

        # Syntax : bytes(src, enc, err)

            # Parameters :

            # src : The source object which has to be converted
            # enc : The encoding required in case object is a string
            # err : Way to handle error in case the string conversion fails.


    # converts the int, bool, string variable into byte
    int_bytes = bytes(first_a)
    bool_bytes = bytes(second_a)
    str_bytes = bytes(third_a, 'utf-8')

    # prints the values and their bytes representation.
    print (f'-- The int value is "{first_a}" \nbytes: "{int_bytes}"')
    print (f'-- The bool value is "{second_a}" \nbytes: "{bool_bytes}"')
    print (f'-- The string value is "{third_a}" \nbytes: "{str_bytes}"')


bytess('10', 'true', 'gris')
