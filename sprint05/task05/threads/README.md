DESCRIPTION

Create a script that reads ﬁles using threads. 
The script consists of two functions:
 
    • start_threads() that takes a list of dictionaries of thread information, 
      creates and starts a thread for every item in the given list When creating 
      a new thread it uses: task_thread() as the function to be executed by every thread, 
      and tha values of 'name', 'path', 'delay' of the item as the arguments 
      to be passed to the target function 

    • task_thread() takes the thread's arguments (name, path, and delay), 
      prints the contents of the ﬁle at the given path line by line, 
      and sleeps after every line for the delay number of seconds
