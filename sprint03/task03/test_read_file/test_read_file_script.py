import os

from test_read_file import read_file


if __name__ == '__main__':
    strings = ['test_sample.txt', 'test_sample1.txt', 'test_no_permission.txt']
    # remove read permissions from one ﬁle to check error handling
    os.chmod('test_no_permission.txt', 000)
    for string in strings:
        read_ﬁle(string)
        print ('***')
