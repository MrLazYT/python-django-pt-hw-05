from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, name, max_speed, length, engine_type, decks):
        self.name = name
        self.max_speed = max_speed
        self.length = length
        self.engine_type = engine_type
        self.decks = decks
    
    @abstractmethod
    def info(self):
        pass

class Frigate(Ship):
    def __init__(self, name, max_speed, length, engine_type, decks, role, anti_air_systems, radar_systems, torpedo_tubes):
        super().__init__(name, max_speed, length, engine_type, decks)
        self.role = role
        self.anti_air_systems = anti_air_systems
        self.radar_systems = radar_systems
        self.torpedo_tubes = torpedo_tubes
    
    def info(self):
        return f"Type: Frigate\nName: {self.name}\nMax Speed: {self.max_speed}\nLength: {self.length}\nEngine Type: {self.engine_type}\nDecks: {self.decks}\nRole: {self.role}\nAnti Air Systems: {self.anti_air_systems}\nRadars: {self.radar_systems}\nTorpedo Tubes: {self.torpedo_tubes}"

class Destroyer(Ship):
    def __init__(self, name, max_speed, length, engine_type, decks, missile_launchers, maneuver_speed, armor):
        super().__init__(name, max_speed, length, engine_type, decks)
        self.missile_launchers = missile_launchers
        self.maneuver_speed = maneuver_speed
        self.armor = armor
    
    def info(self):
        return f"Type: Destroyer\nName: {self.name}\nMax Speed: {self.max_speed}\nLength: {self.length}\nEngine Type: {self.engine_type}\nDecks: {self.decks}\nMissile Launchers: {self.missile_launchers}\nManeuver Speed: {self.maneuver_speed}\nArmor: {self.armor}"

class Cruiser(Ship):
    def __init__(self, name, max_speed, length, engine_type, decks, firepower, aircraft_capacity, anti_aircraft_guns):
        super().__init__(name, max_speed, length, engine_type, decks)
        self.firepower = firepower
        self.aircraft_capacitty = aircraft_capacity
        self.anti_aircraft_guns = anti_aircraft_guns
    
    def info(self):
        return f"Type: Cruiser\nName: {self.name}\nMax Speed: {self.max_speed}\nLength: {self.length}\nEngine Type: {self.engine_type}\nDecks: {self.decks}\nFirepower: {self.firepower}\nAircraft Capacity: {self.aircraft_capacitty}\nAnti Aircraft Guns: {self.anti_aircraft_guns}"

frigate = Frigate(
    name="USS Freedom",
    max_speed=47,
    length=115,
    engine_type="Diesel-electric",
    decks=3,
    role="Patrolling",
    anti_air_systems=2,
    radar_systems = 6,
    torpedo_tubes=4
)

destroyer = Destroyer(
    name="USS Arleigh Burke",
    max_speed=30,
    length=155,
    engine_type="Gas turbine",
    decks=5,
    missile_launchers=10,
    maneuver_speed=28,
    armor=1
)

cruiser = Cruiser(
    name="USS Ticonderoga",
    max_speed=32,
    length=172,
    engine_type="Gas turbine",
    decks=6,
    firepower=100,
    aircraft_capacity=2,
    anti_aircraft_guns=16,
)

print("-------------------------------")
print(frigate.info())
print("-------------------------------")
print(destroyer.info())
print("-------------------------------")
print(cruiser.info())
print("-------------------------------")