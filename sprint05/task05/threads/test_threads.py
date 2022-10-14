def task_thread(name, path, delay):
    import time

    with open(path, 'r') as f:
        read_line = f.readlines()
        for i in read_line:
            time.sleep(delay)
            #print(read_line)
            print(f"[{name}]: {i.strip()}")


def start_threads(list_of_dict):
        import threading
        for i in list_of_dict:
            x = threading.Thread(target=task_thread, args=[i['name'], i['path'], i['delay']])
            x.start()
