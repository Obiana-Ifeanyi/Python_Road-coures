DESCRIPTION

Create a script that contains three classes:
Cargo, Container, and Ship. They are connected in the following way: 
a ship can have many containers; every container can have one cargo. 

Here are more details on the classes: 
    • Cargo class must have 
        – destination property (string) 
        – weight property (integer) 
        – an initializer that sets the given destination and weight 

    • Container class must have 
        – weight_limit property (integer) 
        – cargo property (Cargo instance) 
        – an initializer that sets the given weight_limit and cargo (default is None) 
        – set_cargo() method that sets a passed Cargo instance to the cargo property if its weight is less or equal to the weight_limit 

    • Ship class must have
        – route property (list of strings) 
        – containers property (list of Container instances) 
        – an initializer that sets the given route and containers 
        – add_containers() method that takes a list of Container instances, loops through it, 
          and adds to the containers property those that have a cargo with a destination on the ship's route 

For each of the classes, add an override for the __str__() and the __repr__() methods. 
Using the logging Python module, log to a shipments.log ﬁle. It must be overwritten, not appended to.
