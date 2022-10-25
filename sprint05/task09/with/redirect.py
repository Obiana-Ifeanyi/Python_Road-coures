import sys

class Redirect:  # context manager
    def __init__(self, file_path, stream):
        self.file_path = file_path
        self.stream = stream

        # creating a var that temparary holds stdout and stderr
        self.stdout =  sys.stdout
        self.stderr = sys.stderr


    def __enter__(self):
        self.file = open(self.file_path, 'a')

        if self.stream == 'o':
            # redirect stdout to file path if stream == 'o'
            sys.stdout = self.file

        elif self.stream == 'e':
            # redirect stderr to file path if stream == 'a'
            sys.stderr = self.file

        elif self.stream == 'oe':
            # redirect stdout and stderr to file path if stream == 'oe'
            sys.stdout = self.file
            sys.stderr = self.file


    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        self.file.close()

