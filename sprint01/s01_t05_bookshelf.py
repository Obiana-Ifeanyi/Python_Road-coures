# replace value in a list using while loop:
def add_to_bookshelf(book_to_add, bookshelf):
 i = 0

 while i < len(bookshelf):

  if bookshelf[i] == '---':
   bookshelf[i] = book_to_add
   return True

  elif bookshelf[i] != '---':
   return False 

  elif bookshelf == []:
   return False

  i += 1 


add_to_bookshelf('the vampire diary', ['the originals', 'the legend of the seeker', 'beauty and the beast', '---', 'the twelve masked marfians'])
