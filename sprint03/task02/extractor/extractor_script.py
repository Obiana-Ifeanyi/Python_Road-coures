
from extractor import extractor


if __name__ == '__main__':
    brian = {
        'name': 'Brian',
        'email':
        'very_naughty_boy@gmail.com',
        'age': 33,
        'star_sign': 'Capricorn',
        'legs': 2,
    }

    print (f'***\nbrian, str: {extractor(brian, str)}')
    print (f'***\nbrian, int: {extractor(brian, int)}')
    print (f'***\nbrian, list: {extractor(brian, list)}')

    monty_python = {
        'title': 'Monty Python',
        'media': ['ﬁlm', 'tv', 'radio', 'audio', 'literature'],
        'country of origin': 'United Kingdom',
        'ﬁrst aired': 1969,
        'genres': ['satire', 'surreal', 'black comedy'],
        'key members': {'Graham Chapman',
            'John Cleese',
            'Terry Gilliam',
            'Eric Idle',
            'Terry Jones',
            'Michael Palin'},
        'ofﬁcial website': 'montypython.com',
        'nb of ﬁlms': 5,
        'nb of tv series': 3,
        'average sketch length': 30.5,
        'songs': {
            'The Meaning Of Life': ['Accountancy Shanty', 'Galaxy Song'],
            'Monty Python And The Holy Grail': ['The Tale Of Sir Robin', 'Camelot Song'],
            'Life Of Brian': ['Brian Song', 'Always Look On The Bright Side Of Life'],
            'Monty Python’s Flying Circus': ['The Liberty Bell', 'Lumberjack Song', 'Spam Song']},
        'name has meaning': False,}

    print (f'***\nmonty_python, list:\n{extractor(monty_python, list)}')
    print (f'***\nmonty_python, ﬂoat:\n{extractor(monty_python, ﬂoat)}')
    print (f'***\nmonty_python, dict:\n{extractor(monty_python, dict)}')
    print (f'***\nmonty_python, no data type given:\n{extractor(monty_python)}')
    print (f'***\nempty, int:\n{extractor({}, dict)}')
