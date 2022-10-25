DESCRIPTION 

Create a script that works with processes. 
The script consists of two functions: 

    • start_processes() that takes a list of dictionaries with process information, 
      creates and starts a process for every item in the given list When creating a new process 
      it uses task_process() as the function to be executed by every process. 
      Takes 'name', 'year', 'delay' as the arguments to be passed to the target function 

    • task_process() takes the process's arguments (name, year, delay), 
      prints the name and age of the person in the current year, 
      and sleeps for the delay number of seconds
