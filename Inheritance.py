class Vehicle:
    def __init__(self, name, max_speed, bhp):
        self.name = name
        self.max_speed = max_speed
        self.bhp = bhp

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
  # Overriding seating_capacity method

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

School_bus = Bus("School Volvo", 180, 145)
print(School_bus.seating_capacity())

# --------------------------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, name, bhp, capacity):
        self.name = name
        self.bhp = bhp
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount = amount + amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 140, 50)
print("Total Bus fare is:", School_bus.fare())

