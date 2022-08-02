def test_song (verses, chorus):

    if verses[1] in verses:
        return verses[0] + chorus + verses[1] + chorus + chorus

    elif verses[2] in verses:
        return verses[0] + chorus + verses[1] + chorus + verses[2] + chorus + chorus


