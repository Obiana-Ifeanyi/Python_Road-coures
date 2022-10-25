def task_process(name, year, delay):
    import datetime
    import time

    todays_date = datetime.date.today()
    age = todays_date.year - year
    time.sleep(delay)
    print(f"{name}, {age} years old")


def start_processes(list_of_dict):
    import multiprocessing
    for i in list_of_dict:
        x = multiprocessing.Process(target=task_process, args=[i['name'], i['year'], i['delay']])
        x.start()
