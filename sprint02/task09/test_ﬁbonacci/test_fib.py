# Example of Using Yield In Python (Fibonacci Series)
# Here is a general example that you can use to understand the concept of yield in the most precise manner.
# Here is a Fibonacci program that has been created using the yield keyword instead of return.

def fibonacci(n):

   temp1, temp2 = 0, 1

   total = 0

   while total < n:

       yield temp1

       temp3 = temp1 + temp2

       temp1 = temp2

       temp2 = temp3

       total += 1

fib_object = fibonacci(20)

print(list(fib_object))

# Here, you have created a Fibonacci program that returns the top 20 Fibonacci numbers.
# Instead of storing each number in an array or list and then returning the list,
# you have used the yield method to store it in an object which saves a ton of memory,
# especially when the range is large.
