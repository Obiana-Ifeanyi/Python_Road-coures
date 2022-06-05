#printing from a function using a variable as argument 
def crystal_ball (courage, intelligence):
 print  (f'reading the future of an adventurer with {courage} courage and {intelligence} intelligence...')


 if courage > 50 and intelligence > 50 :
   print ("i see a great success in your future")
   print ("***")

 elif courage >= 100 or intelligence <= 10 :
   print ("your life is in danger")
   print ("***")

 else :
   print ("your future is a mystery")
   print ("***")


crystal_ball(74, 86)
crystal_ball(164, 7)
crystal_ball(43, 37)
crystal_ball(69, 26)

