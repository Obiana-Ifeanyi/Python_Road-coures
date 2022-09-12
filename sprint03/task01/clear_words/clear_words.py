def clear_words(text):
    import re

    # var that stores our regex pattern
    text_regex = re.compile(r'[?!.:;,-]+')

    # check if pattern is text
    if re.search(text_regex, text):

        # split string per whitespace
        list1 = text.split(" ")

        # uses the function map() with a lambda expression to remove all punctuation marks in the split words
        result = list(map(lambda list1: re.sub(text_regex, '', list1), list1))

        return result
