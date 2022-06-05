#Create a script that contains a function called patoi().
# The function must take an argument, cast it to int , and return the result. If the casting attempt fails, the function must return False.
def patoi (gris):

 try:
  val = int(gris)
  return val

 except:
  return False  

patoi(-1)
