from jb.python_training.oop_vehicles.vehicle_parent import vehicleParent


class TruckObject(vehicleParent):

    def __init__(self,brand,whells_amount):
        self.brand = brand
        self.whells_amount = whells_amount

    def calculate_distance(self,time , speed):
        distance  = time * speed
        return distance

    # def price_calculator(self,price):
    #     total_price = price * 1.18
    #     print (f"the total price is {total_price}")
    #     return total_price