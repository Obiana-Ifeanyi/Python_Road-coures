from songs import song1

verses = (("There's nothing you can do that can't be done",
           "Nothing you can sing that can't be sung",
           'Nothing you can say but you can learn how to play the game',
           "It's easy\n"),
           ("Nothing you can know that isn't known",
            "Nothing you can see that isn't shown",
            "Nowhere you can be that isn't where you're meant to be",
            "It's easy\n"))

chorus = ('All you need is love', 'All you need is love',
          'All you need is love, love', 'Love is all you need\n')




test_verses = (('verse1 line1', 'verse1 line2'),
          ('verse2 line1', 'verse2 line2', 'verse2 line3'),
          ('verse3 line1',))

test_chorus = ('** CHORUS line1', '** CHORUS line2')



def test_script(verses, chorus, test_description):
    print ('\n' + f'test - {test_description}'.center(40, '_'))
    print ('[start]', *song1(verses, chorus), '[end]', sep='\n')



if __name__ == '__main__':
    test_script(test_verses, test_chorus, 'simple')
    test_script(verses, chorus, 'normal song')


