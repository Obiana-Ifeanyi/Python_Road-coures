## Create a script that contains two functions, each of which encrypts a message given as an argument.
# The functions uses the algorithms md5 and sha1 per function.

import hashlib

def md5_hash(strin):  #-MD5 Hash: This hash function accepts sequence of bytes and returns 128 bit hash value.

    # Convert string to bytes
    str2bytes = bytes(strin, 'utf-8')    # String can also be converted to bytes using the encode() fn.

    # Using the md5 hash algorithm imported from hashlib
    # convert bytes to hash
    bytes2hash = hashlib.md5(str2bytes)

    # Print the encoded data in hexadecimal format using the hexdigest() fn.
    print ('Original string:', strin, end = '\n')
    print ('md5 hash generated is')
    print (bytes2hash.hexdigest())

md5_hash('geeksforgeeks')


print ()


def sha1_hash(str_ing):  #-SHA-1: This hash function takes an input and produces a 160-bit (20-byte) hash value.

    # Convert string to bytes
    str2bytes = bytes(str_ing, 'utf-8')

    # Using the SHA-1 hash algorithm imported from hashlib
    # convert bytes to hash
    bytes2hash = hashlib.sha1(str2bytes)

    print ('Original string:', str_ing, end = '\n')
    print ('md5 hash generated is')
    print (bytes2hash.hexdigest())

sha1_hash('gris')


# NOTE: digest() fn returns the hash value in byte format.






# What is Cryptographic hash function?

# A cryptographic hash function is a special class of hash function that has certain properties which make it suitable for use in cryptography.
# It is a mathematical algorithm that maps data of arbitrary size to a bit string of a fixed size (a hash function) which is designed to also be a one-way function,
# that is, a function which is infeasible to invert (Source : Wiki). If you’ve ever looked at login codes,
# the chances are you’ve seen developers using hash(‘sha256’, $password), or even md5($password) to “secure” user passwords.
# Passwords hashes generated this way are laughably easy to cracks;
# with weak algorithms and no salting or stretching in places you’re almost giving your passwords to an attacker who gains access.




                                ##########################
# MessageDigest Class provides following cryptographic hash function to find hash value of a text as follows:

# .MD2
# .MD5
# .SHA-1
# .SHA-224
# .SHA-256
# .SHA-384
# .SHA-512
