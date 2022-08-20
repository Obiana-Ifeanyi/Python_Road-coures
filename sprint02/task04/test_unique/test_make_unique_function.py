
def test_make_unique(arg_dictionary):

        for key, value in arg_dictionary.items():
                arg_dictionary = {key : value}

                #  removes all duplicate items in every list
                value = list(set(value))

                # sorts the elements of each list in the given dictionary in an ascending order
                value.sort()

                #  returns the formatted dictionary
                arg_dictionary = {key : value}
                print (arg_dictionary)


arg_dictionary = {
                  "city": ['Kharkiv', 'Kyiv', 'Lviv', 'Dnipro', 'Kyiv', 'Kyiv', 'Kharkiv', 'Kharkiv', 'Lviv'],
                  "age": [16, 16, 17, 18, 19, 19, 19, 18, 20],
                   }
test_make_unique(arg_dictionary)


print ('****')
arg_dictionary =  {
                   "hobby": ['drawing', 'basketball', 'drawing', 'drawing', 'basketball','dancing', 'dancing', 'dancing', 'dancing'],
                   "format": ['individually', 'individually', 'group', 'individually', 'group', 'individually', 'group', 'group', 'group'],
                    }
test_make_unique(arg_dictionary)
