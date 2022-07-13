## Create a script that asks the user for input and outputs a message that will be different depending on the input.
  ## :
    # If the user enters the word 'right', the output message must be 'The right sign says: "DEAD PEOPLE ONLY"'.
    # If the user enters the word 'left', the output message must be 'The left sign says: "BEWARE!"'.
    # If the user enters the word 'middle', the output message must be 'The middle sign says: "CERTAIN DEATH"'.
    # In all other cases the output message must be 'There is no [entered input] sign'.

print ("There are 3 signs in front of you. 'right', 'left' and 'middle'. ")
 
users_input = input('Which one would you like to read? ')


if users_input == 'right':
    print ('The right sign says: "DEAD PEOPLE ONLY"')

elif users_input == 'left':
    print ('The left sign says: "BEWARE!"')

elif users_input == 'middle':
    print ('The middle sign says: "CERTAIN DEATH"')

else:
    print (f'There is no {users_input.upper()} sign')
