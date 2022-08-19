# note this file contain other methods which was put into account when solving for this task
# this function maybe edited in future time to yield a more suitable result.

def song2 (verses, chorus):
    # test for values in tuple of tuple
    # using any()
    if (any(verses[1] in i for i in verses)):
        return verses[0] + chorus + verses[1] + chorus + chorus

    elif (any(verses[2] in i for i in verses)):
        return verses[0] + chorus + verses[1] + chorus + verses[2] + chorus + chorus



def song1 (verses, chorus):
    # test for values in tuple of tuple
    # using itertools.chain()
    import itertools

    if (verses[1] in itertools.chain(verses)) :
        return verses[0] + chorus + verses[1] + chorus + chorus

    elif (verses[2] in itertools.chain(verses)) :
        return verses[0] + chorus + verses[1] + chorus + verses[2] + chorus + chorus


