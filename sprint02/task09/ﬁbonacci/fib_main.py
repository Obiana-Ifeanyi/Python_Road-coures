def fib(n):

    if n <= 1:
        return n

    # returns the Fibonacci Sequence
    return fib(n-1) + fib(n-2)


def fib_generator(a):

   temp1, temp2 = 0, 1

   total = 0

   for i in range(a):

       yield temp1

       temp3 = temp1 + temp2

       temp1 = temp2

       temp2 = temp3

       total += 1


