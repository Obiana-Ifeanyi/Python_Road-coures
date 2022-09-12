def  extractor(extractable, value_type = str):
    # using for loop to search the value of dictionary
    for key, value in extractable.items():

        # value_type should be an instance of Data-type, e.g., int, bool, etc.

        # using isinstance() fn with value form dictionary
        # check if a value is of a certain data type ?
        if isinstance(value, value_type):
            result = f"{key}: {value} is a {value_type}"
            print  (result)
            #return result

            # using filter() fn.




brian = { 'name': 'Brian', 'email': 'very_naughty_boy@gmail.com', 'age': 33, 'star_sign': 'Capricorn', 'legs': 2, 'arms': 2.5 } 

extractor(brian, int)
