def test_contains(stringg, listt):

    list2 = []
    for i in listt:

        # find if the elements of list is a substring of the string arg
        if i in stringg:

            # append i to empty list
            list2.append(i)

    return list2


stringg = "whenever i'm broken, you make me feel whole, whenever i'm loney you there for my soul"
listt = ['broke', 'loney', 'game', 'soul', 'pig', ]

print (test_contains(stringg, listt))
