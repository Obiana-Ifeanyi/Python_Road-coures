'''
DESCRIPTION
Create a script that contains a function called raise_error().
The function takes two strings: a key and a message,
and raises an error corresponding to the given key with the message.
If the key is not one of the following:

• 'value'
• 'key'
• 'index'
• 'memory'
• 'name'
• 'eof'

raise a ValueError with a message 'No error with such key.'.
'''

def raise_error(key, message):

    if key == 'value':
        raise ValueError(message)
    elif key == 'key':
        raise KeyError(message)
    elif key == 'index':
        raise IndexError(message)
    elif key == 'memory':
        raise MemoryError(message)
    elif key == 'name':
        raise NameError(message)
    elif key == 'eof':
        raise EOFError(message)
    else:
        message = 'No error with such key.'
        raise ValueError(message)
