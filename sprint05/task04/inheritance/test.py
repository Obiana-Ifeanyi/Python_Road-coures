clr = ['\033[38;5;208m',  # Phone
       '\033[38;5;112m',  # Computer
       '\033[38;5;87m', # Smartphone
       '\033[38;5;160m',  # IPhone
       '\033[0m']

class Phone(object):
    def __init__(self, number):
        print(f'{clr[0]}[Phone init ({self.__class__.__name__})]{clr[4]}')
        self.number = number


    def make_call(self, number):
        print(f'{clr[0]}[Phone make call ({self.__class__.__name__})]{clr[4]}')
        print (f"Call from {self.number} to {number}.")

class Computer(object):
    def __init__(self, operating_system, cpu, ram_size, input_devices):
        print(f'{clr[1]}[Computer init ({self.__class__.__name__})]{clr[4]}')
        self.operating_system = operating_system
        self.cpu = cpu
        self.ram_size = ram_size
        self.input_devices = input_devices


class Smartphone(Computer, Phone):
    def __init__(self, operating_system, cpu, ram_size, number, battery):
        print(f'{clr[2]}[Smartphone init ({self.__class__.__name__})]{clr[4]}')
        #self.number = number
        input_devices = ['touch screen']
        super().__init__(operating_system, cpu, ram_size, input_devices)
        self.number = number
        self.battery = battery

class IPhone(Computer):
    def __init__(self, cpu, ram_size, number, battery):
        print(f'{clr[3]}[IPhone init ({self.__class__.__name__})]{clr[4]}')
        super().__init__(cpu, ram_size, number, battery)
