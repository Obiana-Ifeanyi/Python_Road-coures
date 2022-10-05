import logging

logging.basicConfig(format='%(levelname) s%(message)s', filename='shipments.log', filemode='w', level=logging.INFO,)


class Cargo:
    def __init__(self, destination:str, weight:int):
        self.destination = destination
        self.weight = weight

        logging.info(f" [Cargo] initialized: Cargo(destination={self.destination}, weight={self.weight})")

    def __str__(self) -> str:
        return f'Cargo to {self.destination} with weight {self.weight}'

    def __repr__(self) -> str:
        return f'Cargo(destination={self.destination}, weight={self.weight})'


class Container:
    def __init__(self, weight_limit:int, cargo = None):
        self.weight_limit = weight_limit
        self.agg_cargo = cargo

        logging.info(f" [Container] initialized: Container(weight_limit={self.weight_limit}, cargo={self.agg_cargo})")

    def set_cargo(self, cargo = None):

        if self.weight_limit:
            self.agg_cargo = cargo
        else:
            return'cargo is grater than'

        logging.info(f" [Container] Cargo set: {str(self.agg_cargo)}")


    def __str__(self) -> str:
        return f'Container up to {self.weight_limit} with {str(self.agg_cargo)}'

    def __repr__(self) -> str:
        return f'Cargo(weight_limit={self.weight_limit}, cargo={repr(self.agg_cargo)})'


class Ship:
    def __init__(self, route:list, containers):
        self.route = route          # list of string
        self.agg_containers = containers   # list of container instances/object from the container class


    '''
    def add_containers(self):
        for i in # list of container instances:

    # logging.info(f" [Ship] Added Container {str(self.agg_containers)}")
    '''

    def __str__(self) -> str:
        return f'ship to {self.route} with containers: Container up to {str(self.agg_containers)},'


    def __repr__(self) -> str:
        return f'Ship(route={self.route}, containers={repr(self.agg_containers)}'









# when working with aggregation for this task
# the instance of the cargo class is set to be the cargo property of the container class,
# and the instances of the container class is set to be the containers property of the of the ship class which is a list

