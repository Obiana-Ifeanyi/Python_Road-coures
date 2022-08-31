# DESCRIPTION
# Create a function contains() that takes a string and a list of substrings.
# The function checks if each substring is present in the string
# and returns a list of substrings that are in the string,
# otherwise it returns an empty list.
# This function does ignore case, but converts the string to search into lower cases and finds the substring from the string

def contain2(string1, list1):

    list2 = []
    for s in list1:

        # find for list in string regardless of case
        # without regex
        # the given string is first converted to lowercase before searching for substring
        if s.lower() in string1.lower():

            # append s to empty list
            list2.append(s.lower())

    # return a list containing sub string in 'stringg'
    return list2
