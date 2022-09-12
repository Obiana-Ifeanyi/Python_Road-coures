'''
DESCRIPTION
Create a script that contains a function read_ﬁle() that:
    • takes one argument: ﬁlename as a string
      (You are not required to handle cases when the argument is not of type str .)
    • if the ﬁle is present in the current directory
      (and the user has read permissions for it):

       – opens the ﬁle
       – reads the ﬁle and saves its contents in a variable
       – prints the ﬁle contents in the following format:
         'File "[ﬁlename]" has the following message: [ﬁle contents]'
       – closes the ﬁle
    • if there is no such ﬁle in the current directory
      (or the user has no read permissions for the requested ﬁle):
       – prints the message: 'Failed to read ﬁle "[ﬁlename]".
'''

def read_file(filename):   #inside the function parethesis (filename: str)
    import os

    try:
        if isinstance(filename, str):
            if os.path.exists(filename):
                f = open(filename, 'rt')
                text = f.read()
                print (f'File "{filename}" has the following message:')  # can also make use of <file.name> to print for file name
                print (text)
                f.close()

    except PermissionError:
        print (f'Failed to read ﬁle "{filename}"')

