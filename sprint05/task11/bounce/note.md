QUEUE IN PROGRAMMING?
 
A queue is an abstract data type that holds an ordered, linear sequence of items. you can describe it as a
first in first out (FIFO) structure, the first element to be added to the queue will be the first element to
be removed from the queue.
    new element are added to the back or rear of the queue.

what is a queue?
a queue can be defined as an oredred list which enables insert operations to be performed at one end called 
rear and deleted operations to be performed at another end called front

         delete-operations  1, 3, 4, 6, 7, ,9 ,10, 12, 13 add-operations

as items are added to the queue they are deleted at the front whereas more items are added at the rear

'https://superfastpython.com/multiprocessing-queue-in-python/'
'https://www.geeksforgeeks.org/queue-in-python/'



------- task logic-------
From this task script 'balls_for_queue' is the task queue that contains 
a list of instances/object created from the Ball Class. a getball variable is created 
which can reference the parameters of our ball class object in the task_queue 
example:
x =  Ball(name= red, ball_count = 5)

getball = task_queue.get(block=True, timeout=1)
therefore: getball.ball_count can reference the parameter for the Ball class

the logic of this task is that the ball bounces onces per iteration in a FIFO pattern 
(first ball bounces onces and decriments by 1 then checks the condition and move on to the next ball) 
the condition is such that the ball is added to the 'done_queue' if counter is decrimented to 0, 
else it adds it back to the 'task_queue', finally the loop is exited if 'done_queue' is full


