#DESCRIPTION:

# Create a script with a function song() that generates a song from given verses and chorus.
# It takes two tuple arguments: verses and chorus, and returns a tuple of strings.
# The verses is a tuple of tuples of strings, and the chorus is a tuple of strings.
# Each string is meant to be a line of a song.

# The formula for a song that your function must use is: "add a chorus after every verse, and add one more chorus in the end of the song".
# So, for example, if the given arguments are:

# • verses: (('a', 'b'), ('c', 'd'))
# • chorus: ('x', 'y')

# Then the function must

# return ('a', 'b', 'x', 'y', 'c', 'd', 'x', 'y', 'x', 'y').


def song (verses, chorus):
    # test for values in tuple of tuple
    # using len() fn and '==' operator.
    if len(verses) == 2:
        return verses[0] + chorus + verses[1] + chorus + chorus

    elif len(verses) == 0:
        return chorus

    elif len(verses) == 0 and len(chorus) == 0:
        return ()

    elif len(verses) == 3:
        return verses[0] + chorus + verses[1] + chorus + verses[2] + chorus + chorus



