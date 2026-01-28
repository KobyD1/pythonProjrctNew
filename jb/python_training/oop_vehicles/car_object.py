from jb.python_training.oop_vehicles.vehicle_parent import vehicleParent


class car(vehicleParent):
    def __init__(self,brand,is_electric):
        self.brand = brand
        self.is_electric = is_electric

    pass