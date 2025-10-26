class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor : {self.current_floor}")
        else:
            print("Elevator is at the top floor!")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor!")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor number.")
            return

        print(f"Moving elevator from floor {self.current_floor} to {target_floor}")

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Elevator arrived at floor: {self.current_floor}\n")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))
        print(f"Building created with {num_elevators} elevators "
              f"({bottom_floor} to {top_floor}).")

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number.")
            return
        print(f"\nRunning elevator {elevator_number}:")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

building = Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.run_elevator(3, 3)
building.run_elevator(1, 1)

