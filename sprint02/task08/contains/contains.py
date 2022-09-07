# DESCRIPTION
# Create a function contains() that takes a string and a list of substrings.
# The function checks if each substring is present in the string
# and returns a list of substrings that are in the string,
# otherwise it returns an empty list.
# The function must ignore case.

def contains(stringg, listt):
    import re

    newlist = []
    for i in listt:

        # find for list in string regardless of case
        # using regex
        if re.search(i, stringg, re.IGNORECASE):

            # append i to empty list
            newlist.append(i)

    # return a list containing sub string in 'stringg'
    return newlist


