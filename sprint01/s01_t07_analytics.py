def print_str_analytics (x):

    print ("|-------------------------------------------|")
    print ("|              String analysis              |")
    print ("|-------------------------------------------|")
    print (f"| '{x}'                                    |")
    print ("|-------------------------------------------|")
    # using list comprehension and len() fn to print the length of the following characters in the string.
    # isprintable(), isalnum(), isalpha(), isdecimal(), islower(), isupper() and isspace(). 
    print (f"| Number of  printable characters is: {len(''.join(c for c in x if c.isprintable()))}")

    print (f"| Number of alphanumeric characters is: {len(''.join(c for c in x if c.isalnum()))}")

    print (f"| Number of alphabetic characters is: {len(''.join(c for c in x if c.isalpha()))}")

    print (f"| Number of decimal characters is: {len(''.join(c for c in x if c.isdecimal()))}")

    print (f"| Number of lowercase letters is: {len(''.join(c for c in x if c.islower()))}")

    print (f"| Number of uppercase letters is: {len(''.join(c for c in x if c.isupper()))}")

    print (f"| Number of whitespace characters is: {len(''.join(c for c in x if c.isspace()))}")

    print ("|-------------------------------------------|")

print_str_analytics('hello my name is gris')
