class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number =  registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC 123", 142, )

print(f"{car.registration_number:s} has maximum speed of {car.maximum_speed: }km/h ,travelled distance is {car.travelled_distance: }km and current speed is {car.current_speed: }km/h.")