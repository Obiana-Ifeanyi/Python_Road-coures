
import sys
import webbrowser
import re
from helper import print_stdout, print_stderr


try:

    URL = sys.argv[1]
    valid_url = re.search('^https?://[a-zA-Z]+.youtube.[a-zA-Z]+', URL)

    if valid_url:
        webbrowser.open(URL)

        print_stdout(f'Opening the YouTube video at {URL}.')
        print_stdout('YouTube video opened.')


    else:
        print_stderr('The URL is invalid.')


except IndexError:
    print_stderr('The site URL was not passed.')





