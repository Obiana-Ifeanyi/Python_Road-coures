# Python3 program for Bubble Sort Algorithm Implementation

def bubbleSort(mylist):

        n = len(mylist)

        # For loop to traverse through all
        # element in an array
        for i in range(n):
                for j in range( n - 1):

                        # Range of the array is from 0 to n-i-1
                        # Swap the elements if the element found
                        #is greater than the adjacent element
                        if mylist[j] > mylist[j + 1]:
                                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]


        print (mylist)

# Driver code

# Examples to test the above code

mylist =  [1, 2, 3, -1230]
bubbleSort(mylist)

bubbleSort([19, 13, 6, 2, 18, 8])

mylist = [3, 2, 1, 2, 2, 2, 3, 9, 8, 1, 3, 12, 32]
bubbleSort(mylist)

