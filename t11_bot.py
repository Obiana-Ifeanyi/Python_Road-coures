input1 = str(input("enter your first string: "))
input2 = str(input("enter your second string: "))

if input1 == "":
  print ("one of this string is empty")

elif input2 == "":
  print ("one of this string is empty")

input6 = input("enter your command: ")

if input6 == "concat":
  print (input1+" "+input2)

elif input6 == "beatbox":
 input9 = int(input("enter first beatbox number: "))
 input8 = int(input("enter second beatbox number: "))
 rex = input1 * input9
 res = input2 * input8
 print (rex+" "+res)

elif input6 == "find":
 t = input1
 result = t.find(input2)
 s = bool(result + 1)
 print (s)


else:
 print ("usage: command find | concat | beatbox")
