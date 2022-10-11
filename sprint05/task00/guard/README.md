DESCRIPTION

Create a class Guard that:

    • has an initializer __init__() that takes a dynamic number of named parameters **kwargs.
      Parameters name and salary must be set in the __init__().
      If the name is not passed, set it to None.
      If the salary is not passed, set it to 0

    • has two methods:
     – greet() prints to the console: 'Hello, my name is [name]!'
    

     – receive_bribe() takes a number and prints a message.
      If the amount passed is greater than the salary of the guard, print: 'You may pass.'
      Otherwise, print: 'I am not letting you pass.' 
