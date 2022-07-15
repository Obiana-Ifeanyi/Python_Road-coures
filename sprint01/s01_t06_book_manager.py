#Create a script with a function get_anonymous()
#the script will take a list of manga and return a new list containing manga that don't include an author.

def get_anonymous (manga):

 x = ' by '

#using list comprehension to check substring within ever element in the list (manga) for the presence of ' by '
 pex = [i for i in manga if x not in i]
 authurless_manga = []

#Appending the list(pex) into the argument/list (authurless_manga) using the Extend() fn
 authurless_manga.extend(pex)

 print (authurless_manga)

get_anonymous(['Naruto by Masashi Kishimoto', 'One piece by Eiichiro Oda', 'Demon slayer by Koyoharu Gotouge', 'me', 'gris na bad gsy',
'Kuroko no basket by Tadatoshi Fujimaki', 'Spy x family by Tatsuya Endo'])
