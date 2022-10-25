'''
def log_decorator(func):
    log() decorator that prints the class name and the name of the called function
    import logging
    import functools

    logging.basicConfig(format= '%(levelname) s%(message)s', level=logging.INFO)

    @functools.wraps(func)
    def wrapped_log_decorator(*args, **kwargs):

        logging.info(f" {func.__name__} with {kwargs}")
        func(*args, **kwargs)

        return func(*args, **kwargs)
    return wrapped_log_decorator



class Knight:

    # instances is class attr(list) that contains all instance of the class
    instances = []

    # limit is also a class attr that sets the number of instances a the init method shouldnt exceed
    limit = 4

    @log_decorator
    def __new__(cls, *args, **kwargs):
        instance = super(Knight, cls).__new__(cls)
        return instance


    @log_decorator
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        Knight.instances.append(self)
'''













def log_decorator(func):
    '''log() decorator that prints the class name and the name of the called function '''
    import logging
    import functools

    logging.basicConfig(format= '%(levelname) s%(message)s', level=logging.INFO)

    @functools.wraps(func)
    def wrapped_log_decorator(*args, **kwargs):

        logging.info(f" {func.__name__} with {kwargs}")

        #func(*args, **kwargs) calling this function will result to a double print of the output

        return func(*args, **kwargs)
    return wrapped_log_decorator





class Knight(object):

    # instances is class attr(list) that contains all instance of the class
    instances = []

    # limit is also a class attr that sets the number of instances a the init method shouldnt exceed
    limit = 4
    @log_decorator
    def __new__(cls, **kwargs):
        import logging

        if len(cls.instances) < cls.limit and 'Arthur' not in kwargs.values():
            inst = super(Knight, cls).__new__(cls)
            return inst
        elif len(cls.instances) >= cls.limit:
            logging.error(f" Cannot create a Knight. The Round Table can only ﬁt {cls.limit} Knights.")
        elif kwargs['name'] == 'Arthur':
            logging.error(f" Cannot create a Knight with the name Arthur. Arthur is the King")


    @log_decorator
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        Knight.instances.append(self)























