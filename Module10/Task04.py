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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        """Simulate one hour of the race."""
        for car in self.cars:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)

    def print_status(self):
        """Print the current race status."""
        print(f"\n{'Registration':<10} {'Max Speed (km/h)':<17} {'Current Speed (km/h)':<22} {'Distance (km)':<15}")
        print("-" * 70)
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.maximum_speed:<17} {car.current_speed:<22} {car.travelled_distance:<15.1f}")

    def race_finished(self):
        """Return True if any car has reached or exceeded the race distance."""
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))


race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
print(f"\nStarting race: {race.name} ({race.distance} km)\n")

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\n--- Hour {hours} ---")
        race.print_status()

print(f"\nRace finished in {hours} hours!")
race.print_status()
