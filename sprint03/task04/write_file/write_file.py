'''
DESCRIPTION
Create a script that contains a function write_ﬁle().
This function:

    • takes two arguments:
         – ﬁlename as a string
           If the given ﬁlename does not end with .txt, prints two consecutive messages:
           'Please enter the ﬁlename in the format "ﬁlename.txt".'
           'Failed to write to ﬁle "[ﬁlename]".'

         – message to be added (Assume that the function will receive only strings for both arguments.
           There is no need to handle other cases.)
           The default value of the message argument must be set to 'None'.

     • creates a ﬁle with the given name (if it doesn't exist yet) and opens it for writing
     • writes the given message to the ﬁle and closes the ﬁle
     • opens the ﬁle again to check if it is not empty
         – if the ﬁle is empty or its contents are not equal to the provided message,
           prints the message: 'Something went wrong...'

         – otherwise, prints two consecutive messages:
             * 'Your message has been written to ﬁle "[ﬁlename]".'
             * 'File "[ﬁlename]" now contains the following text: [message]'

For this task, use the with statement in your solution.
'''


def write_file(Grisfile: str, message= 'None'):
    import os
    import re
    text_regex = re.compile(r".txt$")


    if re.search(text_regex, Grisfile):

        # using WITH STATEMENT open and write content to file
        with open(Grisfile, 'wt') as write_file:
            write_file.write(message)
            write_file.close()


        with open(Grisfile, "rt") as write_file:
            read_text = write_file.read()
            #print (read_text)
            write_file.close()

            if len(read_text) < 0 or read_text != message:
                print ('Something went wrong...')

            elif len(read_text) > 0 or read_text == message:
                print (f'Your message has been written to ﬁle "{Grisfile}".')
                print (f'File "{Grisfile}" now contains the following text: \n{message}')

    else:
        print ('Please enter the ﬁlename in the format "ﬁlename.txt".')
        print (f'Failed to write to ﬁle "{Grisfile}".')

