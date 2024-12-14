class Airplane:
    def __init__(self, model, passengers_count):
        self.model = model
        self.passengers_count = passengers_count
    
    def __str__(self):
        return self.model
    
    def __int__(self):
        return self.passengers_count
    
    def __eq__(self, value):
        return self.model == value
    
    def __add__(self, other):
        return self.passengers_count + other
    
    def __sub__(self, other):
        return self.passengers_count - other
    
    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers_count > other.passengers_count

plane1 = Airplane("Boeing 747", 416)
plane2 = Airplane("Airbus A320", 150)

print("Plane 1 model: ", plane1)
print("Plane 2 model: ", plane2)

print("Plane 1 passenger count: ", int(plane1))
print("Plane 2 passenger count", int(plane2))

print("Is Plane 1 model equal 'Boeing 747': ", plane1 == "Boeing 747")
print("Is Plane 1 model equal 'Boeing 747': ", plane2 == "Boeing 747")

print("Plane 1 passenger count: ", plane1 + 50)
print("Plane 2 passenger count: ", plane2 + 200)

print("Plane 1 passenger count: ", plane1 - 50)
print("Plane 2 passenger count: ", plane2 - 100)

print("Is Plane 1 greater then plane 2: ", plane1 > plane2)
print("Is Plane 2 greater then plane 1: ", plane1 < plane2)
