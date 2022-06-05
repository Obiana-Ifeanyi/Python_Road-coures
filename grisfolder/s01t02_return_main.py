def buy_milk (money):

 product = '[milk]'
 price = 25

 if money >= price :
  sub = int(money // price)
  sub1 = product * sub
  return sub1

 elif money < price :
  pass 

buy_milk(79)
buy_milk(23)


def buy_bread (money):

 product = '[bread]'
 price = 19

 if money >= price and money < 38 :
  sub = int(money // price)
  sub1 = product * sub
  return (sub1)

 elif money >= 38 and money < 58:
  sub = int(money // price)
  sub1 = product * sub
  return (sub1)

 elif money >= 58 :
  sub = int(money // price)
  sub1 = product * 3
  return (sub1)

 elif money < price :
  pass

buy_bread(19)
buy_bread(39)
buy_bread(167)




