def read_file(filename):   #inside the function parethesis (filename: str)
    import os


    if isinstance(filename, str):
        f = open(filename, 'rt')
        print (f'File "{filename}" has the following message:')  # can also make use of <file.name> to print for file name
        print (f.read())
        f.close()
