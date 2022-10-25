import time
from multiprocessing import Process, Queue
from queue import Empty

# leave class Ball as is, don't edit it
class Ball:
    def __init__(self, name, n_bounces):
        self.name = name
        self.n_bounces = n_bounces

    def __str__(self):
        return f'{self.name} ({self.n_bounces})'

# edit the function as described in comments
def bounce(name, delay, task_queue, done_queue):
    while True:
        time.sleep(delay)

        # - stop if done_queue is full
        if done_queue.full():
            print (f"[{name}] done_queue is full. Process will stop.")
            break

        try:
            # - get a ball from task_queue (wait for it max 1 second)
            getball = task_queue.get(block=True, timeout=1)

        except Empty:
            print(f'queue.Empty exception.')

        else:
            # - update the ball's counter
            getball.n_bounces -= 1

            # - put ball either back to the task_queue, or to the done_queue
            if getball.n_bounces == 0:
                done_queue.put(getball)
            else:
                task_queue.put(getball)
            print(f'{name} bounces the {getball.name} ({getball.n_bounces}).')

# edit the contents of this function in the allowed section
def run_processes(balls, args):
    processes = []
    task_queue = Queue()
    done_queue = Queue(maxsize= len(balls)) # edit to make done_queue limited to the correct size

    # - create and start processes for each item of args
    for name, delay in args:
        px = Process(target= bounce, args= (name, delay, task_queue, done_queue))
        px.start()
        processes.append(px)

    # - put all the balls into the task_queue
    '''
    if we have put the ball in balls indiviually the a for loop can be used to iterate through balls while adding
    each items to the task_queue
    ex:
    '''
    for ball in balls:
        task_queue.put(ball)

    for p in processes:
        p.join()
