## How to get input from the user?
    # using the input() fn.


## How to format a string with f-strings?
    # using print(f') fn.


## Create a script that:

    # reads several variables using the input() function
      # – name
      # – quest
      # – color

    # prints the entered information


print ("""BRIDGEKEEPER: Stop.
Who would cross the Bridge of Death must answer me these questions three.""")
name_input = input('BRIDGEKEEPER: What is your name? \n')

quest_input = input('BRIDGEKEEPER: What is your quest? \n')

colour_input = input('BRIDGEKEEPER: What is your favorite color? \n')

print (f"""---------)
Traveler info:
Your name is {name_input} 
Your quest is {quest_input}
Your favorite color is {colour_input}
---------
BRIDGEKEEPER: Right. Off you go.""")
