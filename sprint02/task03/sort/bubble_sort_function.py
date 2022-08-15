# Python3 program for Bubble Sort Algorithm Implementation

def bubble_sort(mylist):

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


        return mylist
