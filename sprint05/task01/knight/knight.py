
class Knight:

    def __init__(self, **kwarg):
        self.__dict__.update(kwarg)

    def greet(self):

        # checking if self have the attr 'name' and 'title'
        if hasattr(self, 'name') and hasattr(self, 'title'):
            rx_msg = f"Hello, I'm Sir {self.name} the {self.title}!"
            print (rx_msg)

        else:
            gx_msg = 'Hello!'
            print (gx_msg)


