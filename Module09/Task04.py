import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

game_started = True
number_of_hours=0

while game_started==True:
    number_of_hours += 1
    for car in cars:
        change_of_speed = random.randint(-10, 15)
        car.accelerate(change_of_speed)
        car.drive(1)
        if car.travelled_distance >= 10000:
            game_started=False

print(f"\nRace finished in {number_of_hours} hours!\n")
print(f"{'Registration':<10} {'Max Speed (km/h)':<17} {'Current Speed (km/h)':<22} {'Distance (km)':<15}")
print("-" * 70)
for car in cars:
    print(f"{car.registration_number:<10} {car.maximum_speed:<17} {car.current_speed:<22} {car.travelled_distance:<15.1f}")
