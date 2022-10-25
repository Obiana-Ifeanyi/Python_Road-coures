def log_decorator(func):
    '''log() decorator that prints the class name and the name of the called function '''
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
        if len(cls.instances) > cls.limit:
            import logging
            logging.error(f" Cannot create a Knight. The Round Table can only ﬁt {cls.limit} Knights. ")

        elif kwargs['name'] == 'Arthur':
            import logging
            logging.error(f" Cannot create a Knight with the name Arthur. Arthur is the King.")

        '''
        elif len(cls.instances) > cls.limit:
            import logging
            logging.error(f" Cannot create a Knight. The Round Table can only ﬁt {cls.limit} Knights. ")
        '''

        instance = super(Knight, cls).__new__(cls)
        return instance


    @log_decorator
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        Knight.instances.append(self)



    def greet(self):
        # checking if self have the attr 'name' and 'title'
        if hasattr(self, 'name') and hasattr(self, 'title'):
            rx_msg = f"Hello, I'm Sir {self.name} the {self.title}!"
            print (rx_msg)

        else:
            gx_msg = 'Hello!'
            print (gx_msg)

