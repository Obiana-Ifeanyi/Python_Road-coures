
def start_threads(list_of_dict):
    import threading
    for i in list_of_dict:
        x = threading.Thread(target=task_thread, args=[i['name'], i['path'], i['delay']])
        x.start()
        # x.join()


def task_thread(name, path, delay):
    import time

    with open(path, 'r') as f:
        read_line = f.readlines()
        for i in read_line:
            time.sleep(delay)
            #print(read_line)
            print(f"[{name}]: {i.strip()}")


# Note:
'''
The order in which threads are run is determined by the operating system
and can be quite hard to predict.
It may (and likely will) vary from run to run,
so you need to be aware of that when you design algorithms that use threading.
'''


# using the .join() function.
""".join() a thread, this statement will wait until either kind of thread is finished, 
before starting another thread. Using this function should result to the output below
[Thread 1]: ﬁle 1 line1
[Thread 1]: ﬁle 1 line2
[Thread 1]: ﬁle 1 line3
[Thread 1]: ﬁle 1 line4
[Thread 2]: ﬁle 2 line1
[Thread 2]: ﬁle 2 line2
[Thread 2]: ﬁle 2 line3
[Thread 3]: ﬁle 1 line1
[Thread 3]: ﬁle 1 line2
[Thread 3]: ﬁle 1 line3
[Thread 3]: ﬁle 1 line4
"""


'''
SEE ALSO
- An Intro to Threading in Python Python
- Multithreaded Programming Python
- Date and Time
'https://realpython.com/intro-to-python-threading/'
'''
