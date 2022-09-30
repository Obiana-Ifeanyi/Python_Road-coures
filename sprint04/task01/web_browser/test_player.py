
import sys
import webbrowser
import re
from helper import print_stdout, print_stderr

URL = 'https://www.youtube.com/watch\?v\=yKQ_sQKBASM'
valid_url = re.search('^https?://[a-zA-Z]+.youtube.[a-zA-Z]+', URL)

if valid_url:

    try:
        webbrowser.open(URL)

        print_stdout(f'Opening the YouTube video at {URL}.')
        print_stdout('YouTube video opened.')


    except IndexError:
        print_stderr('The site URL was not passed.')





elif URL == "":
    print_stderr('The site URL was not passed.')



else:
    print_stderr('The URL is invalid.')



#print ("\nName of Python script:", sys.argv[0])

