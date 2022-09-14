from write_ﬁle import write_ﬁle


if __name__ == '__main__':

    write_ﬁle('ﬁle')
    print('***')
    write_ﬁle('ﬁle.txt')
    print('***')
    write_ﬁle('ﬁle', 'Hello there')
    print('***')
    write_ﬁle('new_ﬁle.txt', 'Hello there')
    print('***')
    # check with a non-empty ﬁle
    write_ﬁle('example.txt', 'A new message')
    print('***')
