## Create a script that contains four integer variables and does the following:
   # • assigns the value 1000 to the ﬁrst variable
   # • assigns the value of the ﬁrst variable to the second variable
   # • deﬁnes a third integer variable with the value 999
   # • deﬁnes a fourth integer variable with the value of the third variable plus 1
   # • prints variable addresses using the id  function
   # • compares the address of the ﬁrst variable to the second, third, and fourth using the keyword is
   # • prints the result to the console


first_var = 1000
second_var = 1000
third_var = 999
fourth_var = third_var + 1

print (f"""first_var = {first_var}, address is {id(first_var)}
second_var = {second_var}, address is {id(second_var)}
third_var = {third_var}, address is {id(third_var)} 
fourth_var = {fourth_var}, address is {id(fourth_var)} \n""")



print (f"{first_var} is {second_var} = {first_var is second_var}")
print (f"{first_var} is {third_var} = {first_var is third_var}")
print (f"{first_var} is {fourth_var} = {first_var is fourth_var}")


## NOTE: The id() fn in python is used to print the address of a variable,
# while the 'is' keyword in python is used to check the identicalness of variables in programming
