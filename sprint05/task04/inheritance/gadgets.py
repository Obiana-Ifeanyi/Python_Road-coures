# colors to prettify output.

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
        self.number2 = number
        print (f"Call from {self.number} to {self.number2}")

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
        input_devices = ['touch screen']   # local variable 'input_device' should be referenced before assignment
        Computer.__init__(self, operating_system, cpu, ram_size, input_devices)
        Phone.__init__(self, number)
        self.battery = battery


class IPhone(Smartphone, Computer, Phone):
    def __init__(self, cpu, ram_size, number, battery):
        print(f'{clr[3]}[IPhone init ({self.__class__.__name__})]{clr[4]}')
        operating_system = 'iOS'   # local variable 'operating_system' should be referenced before assignment
        Smartphone.__init__(self, operating_system, cpu, ram_size, number, battery)

        # there is no read to reference the class Computer andd phone as they are already called from the iphone class

        #input_devices = 'testme2'
        #Computer.__init__(self, operating_system, cpu, ram_size, input_devices)
        #Phone.__init__(self, number)


