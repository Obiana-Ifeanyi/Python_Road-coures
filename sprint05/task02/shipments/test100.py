class Cargo:
    def __init__(self, destination:str, weight:int):
        self.destination = destination
        self.weight = weight

    def __str__(self) -> str:
        return f'Cargo to {self.destination} with weight {self.weight}'

    def __repr__(self) -> str:
        return f'Cargo(destination={self.destination}, weight={self.weight})' 


class Container:
    def __init__(self, weight_limit:int, cargo = None):
        self.weight_limit = weight_limit
        self.agg_cargo = cargo


    def set_cargo(self, cargo = None):

        if self.weight_limit:
            self.agg_cargo = cargo
        else:
            return'cargo is grater than'


    def __str__(self) -> str:
        return f'Container up to {self.weight_limit} with {str(self.agg_cargo)}'

    def __repr__(self) -> str:
        return f'Cargo(weight_limit={self.weight_limit}, cargo={repr(self.agg_cargo)})' 



class Ship:
    def __init__(self, route, containers:list):
        self.route = route
        self.containers = containers


    def add_containers(self, containers):
        for i in containers:
            self.containers.append(i)
        #self.containers.append(containers)
        #self.containers.extend(containers)



    def __str__(self) -> str:
        for cont in self.containers:
            return f'Ship to {self.route} with containers:\n{cont}'


    def __repr__(self) -> str:
        for contt in self.containers:
            return f'Ship(route={self.route}, containers={contt})'
