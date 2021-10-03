""" 😆 create and mix 6 kinds of transport, tricycle, space shuttle, plane, horse, car, ship """
from abc import ABC, abstractmethod


class Undercarriage(ABC):
    """abstract class"""

    @abstractmethod
    def transport_name(self, engine, speed):
        """abstract method"""
        ...


class FuelTank:
    """save fuel, find engine"""

    def __init__(self, fuel):
        """initialize"""
        self.fuel = fuel
        self.engine = ""

    def __str__(self):
        """show fuel and engine"""
        return f"If your fuel is {self.fuel}, then your engine is {self.engine}"

    def __enter__(self):
        print(" - NO, not you again.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(" - What a pity that you are finally leave!")

    def find_engine(self, fuel):
        """find engine"""
        if "grass" in fuel:
            self.engine = "heart"
        elif "oxidant" in fuel:
            self.engine = "jet engine"
        elif "sandwich" in fuel:
            self.engine = "legs"
        elif "gasoline" in fuel:
            self.engine = "internal combustion engine"
        elif "diesel" in fuel:
            self.engine = "motor"
        elif "isotop" in fuel:
            self.engine = "solid fuel engine"


class Transport(FuelTank, Undercarriage):
    """create and mix all kind of transport, find speed"""
    __doc__ = "I will show what ever i whant."

    def __init__(self, move: str, fuel):
        """initialize"""
        super().__init__(fuel)
        self.move = move
        self.speed = ""
        self.name = ""
        self.mix = ""

    def __add__(self, other):
        """mix a plane and space shuttle"""
        if self.class_check(other):
            if self.name == "plane" and other.name == "space shuttle" or \
                    self.name == "space shuttle" and other.name == "plane":
                self.mix = "spaceship"
            return f"{self.name} + {other.name} = {self.mix}"
        else:
            print("Not a Transport class object")

    def __eq__(self, other):
        """comparison transports"""
        if self.class_check(other):
            if self.name == other.name:
                return f"{self.name} and {other.name} are equal"
            else:
                return "Not equal"
        else:
            print("Not a Transport class object")

    def __call__(self, *args, **kwargs):
        print("Hello sir!")

    @staticmethod
    def class_check(val):
        """check value"""
        if isinstance(val, Transport):
            return True
        return False

    def find_speed(self, move):
        """find the speed of transport"""
        if "hooves" in move:
            self.speed = "wain"
        elif "wings" in move:
            self.speed = "bird"
        elif "screw" in move:
            self.speed = "fish"
        elif "wheels" in move:
            self.speed = "ostrich"
        elif "pedals" in move:
            self.speed = "grasshopper"
        elif "gyroscope" in move:
            self.speed = "comet"

    def transport_name(self, engine, speed):
        """create and show a names"""
        if "legs" in engine and "grasshopper" in speed:
            self.name = "tricycle"
            print(f"Looks like a {self.name}")
        elif "solid fuel" in engine and "comet" in speed:
            self.name = "space shuttle"
            print(f"Looks like a {self.name}")
        elif "jet" in engine and "bird" in speed:
            self.name = "plane"
            print(f"Looks like a {self.name}")
        elif "motor" in engine and "fish" in speed:
            self.name = "ship"
            print(f"Looks like a {self.name}")
        elif "internal" in engine and "ostrich" in speed:
            self.name = "car"
            print(f"Looks like a {self.name}")
        elif "heart" in engine and "wain" in speed:
            self.name = "horse"
            print(f"Looks like a {self.name}")

    # def __str__(self):
    #     return f"If you hav {self.move}, you're fast as {self.speed}"


class Wain(Transport):
    """create horse and show the specifications"""

    def draw_my_speed(self):
        """show undercarriage and speed of a horse"""
        print(f"If you hav {self.move}, you're fast as {self.speed}")

    def draw_my_engine(self):
        """show fuel and the engine of a horse"""
        print(f"If your fuel is {self.fuel}, then your engine is {self.engine}")

    def transport_name(self, engine, speed):
        """create and show horse name"""
        if "heart" in engine and "wain" in speed:
            self.name = "horse"
            print(f"Looks like a {self.name}")


class Car(Transport):
    """create Car and show the specifications"""

    def draw_my_speed(self):
        """show undercarriage and speed of a Car"""
        print(f"If you hav {self.move}, you're fast as {self.speed}")

    def draw_my_engine(self):
        """show fuel and the engine of a Car"""
        print(f"If your fuel is {self.fuel}, then your engine is {self.engine}")

    def transport_name(self, engine, speed):
        """create and show Car name"""
        if "internal" in engine and "ostrich" in speed:
            self.name = "car"
            print(f"Looks like a {self.name}")


class Ship(Transport):
    """create Ship and show the specifications"""

    def draw_my_speed(self):
        """show undercarriage and speed of a Ship"""
        print(f"If you hav {self.move}, you're fast as {self.speed}")

    def draw_my_engine(self):
        """show fuel and the engine of a Ship"""
        print(f"If your fuel is {self.fuel}, then your engine is {self.engine}")

    def transport_name(self, engine, speed):
        """create and show Ship name"""
        if "motor" in engine and "fish" in speed:
            self.name = "ship"
            print(f"Looks like a {self.name}")


class Plane(Transport):
    """create Plane and show the specifications"""

    def draw_my_speed(self):
        """show undercarriage and speed of a Plane"""
        print(f"If you hav {self.move}, you're fast as {self.speed}")

    def draw_my_engine(self):
        """show fuel and the engine of a Plane"""
        print(f"If your fuel is {self.fuel}, then your engine is {self.engine}")

    def transport_name(self, engine, speed):
        """create and show Plane name"""
        if "jet" in engine and "bird" in speed:
            self.name = "plane"
            print(f"Looks like a {self.name}")


class SpaceShuttle(Plane, Ship, Car, Wain):
    """create SpaceShuttle and show the specifications"""

    def draw_my_speed(self):
        """show undercarriage and speed of a Space Shuttle"""
        print(f"If you hav {self.move}, you're fast as {self.speed}")

    def draw_my_engine(self):
        """show fuel and the engine of a Space Shuttle"""
        print(f"If your fuel is {self.fuel}, then your engine is {self.engine}")

    def transport_name(self, engine, speed):
        """create and show Space Shuttle name"""
        if "solid fuel" in engine and "comet" in speed:
            self.name = "space shuttle"
            print(f"Looks like a {self.name}")


# undercarriage_fuel = {"four hooves": "grass", "wings": "oxidant", "pedals": "sandwich",
#                      "wheels": "gasoline", "screw": "diesel", "gyroscope": "isotop"}

# input undercarriage and fuel

# brichka = Wain("four hooves", "grass")
# brichka.find_speed(brichka.move)
# brichka.find_engine(brichka.fuel)
# brichka.draw_my_speed()
# brichka.draw_my_engine()
# brichka.transport_name(brichka.engine, brichka.speed)
apolon21 = Transport("pedals", "sandwich")
apolon21.find_speed(apolon21.move)
apolon21.find_engine(apolon21.fuel)
print(apolon21)
apolon21.transport_name(apolon21.engine, apolon21.speed)

car1 = Transport("gyroscope", "isotop")
car1.find_speed(car1.move)
car1.find_engine(car1.fuel)
print(car1)
car1.transport_name(car1.engine, car1.speed)

car2 = Transport("gyroscope", "isotop")
car2.find_speed(car2.move)
car2.find_engine(car2.fuel)
print(car2)
car2.transport_name(car2.engine, car2.speed)

# magic methods
print(apolon21 + car1)
print(apolon21 == car1, "------", car1 == car2)
print(Transport.__doc__)
Transport.__call__(car1)
with FuelTank(car1) as file:
    print("- so, can i go?")
