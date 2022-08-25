import re

def  check_address(meme):

        for key, value in meme.items():

                # block of code for this task uses re.match() function
                address = re.search('^[A-Za-z]*,\s+[A-Za-z\s-]*,\s+[A-Za-z\s-]*\s+\d{1,6},\s+[0-9]{5}$', value)

                if address:
                    print (f"The address of {key} is valid.")

                else:
                    print (f"The address of {key} is invalid.")



meme = {
        'Dmitry Chaykin': ' Ukraine ,  Kyiv  ,  Dorohozhytska    3,  04119 ',
        'Andrey Myskin': 'Ukraine, Lviv, volodymyra velykoho 52, 79053',
        'Tatyana Tsareva': 'Ukraine, Kyiv , Mykola Grinchenko 4, 03038',
        'Zhanna Akopyan': 'Ukraine, Kharkiv, 23 August 33, 61000',
        'Viktor Vasilyev': 'Ukraine, 5 Pasternaka Street Lviv 79000',
        'Andrey Sharov': '271 Akademika Pavlova Street, Kharkiv, Ukraine',
        }

check_address(meme)
