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

h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)