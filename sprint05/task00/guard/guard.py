class Guard:

    def __init__(self, name = None, salary = 0):
        self.name = name
        self.salary = salary

    def greet(self):
        ret = f'Hello, my name is {self.name}'
        return ret

    def receive_bribe(self, numb):
        if numb > self.salary:
            return 'You may pass.'

        else:
            return 'I am not letting you pass.'
