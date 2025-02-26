class Vehicle:
    def __init__(self, make, model):
        self._make = make  
        self._model = model

    def describe(self):
        return f"This is a {self._make} {self._model}."

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors  

    def describe(self):
        return f"This is a {self._make} {self._model} with {self._num_doors} doors."


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def describe(self):
        return f"This is a bike: {self._make} {self._model}."


def vehicle_info(vehicle):
    print(vehicle.describe())


car = Car("Toyota", "Bajaj", 4)
bike = Bike("Yamaha", "R15")

vehicle_info(car)
vehicle_info(bike)
