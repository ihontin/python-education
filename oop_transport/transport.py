"""Calculates and prints data characteristics of different types of transport"""
from abc import ABC, abstractmethod
from math import radians, cos, sin, sqrt, atan2


class Mechanisms(ABC):
    """Abstraction"""

    @abstractmethod
    def travel_time(self):
        pass


class Wheels:

    def __init__(self, wheels):
        self.wheels = wheels


class Transport(Wheels):
    """Calculate distance travel times, prints Transport characteristics"""

    def __init__(self, brand, max_speed, two_points, kind=None, wheels=None):
        super().__init__(wheels)
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind
        self.two_points = two_points

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} имеет {self.wheels} " \
               f"колеса и может развить скорость {self.max_speed} км/ч"

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = abs(lon2 - lon1)
        dlat = abs(lat2 - lat1)
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        return c * r

    @classmethod
    def time_pasted(cls, speed, two_points):
        """Calculate travel time"""
        a1, b1, a2, b2 = two_points
        res = Transport.haversine(a1, b1, a2, b2) / speed
        if res < 1:
            return round(res, 4)
        return res


class Car(Transport, Mechanisms):
    """Prints Car refueling and characteristics"""

    def __init__(self, brand, max_speed, mileage, gasoline_residue, two_points, wheels, kind):
        super().__init__(brand, max_speed, two_points, wheels, kind)
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    def __eq__(self, other):
        if self.max_speed == other.max_speed:
            return "равны!"
        return "не равны!"

    def __subclasscheck__(self, subclass):
        print(f"Класс Car наследуется от класса Mechanisms")

    @property
    def gasoline(self):
        """Prints fuel remaining"""
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, plus):
        """Prints Car refueling"""
        if isinstance(plus, int):
            self.__gasoline_residue += plus
            print(f"Объем топлива увеличен на {plus} л и составляет {self.__gasoline_residue} л")
        else:
            print("Ошибка заправки автомобиля")

    def travel_time(self):
        """Return travel times"""
        return Transport.time_pasted(self.max_speed, self.two_points)


class Boat(Transport, Mechanisms):
    """Prints Boat characteristics"""

    def __init__(self, brand, max_speed, owners_name, two_points):
        super().__init__(brand, max_speed, two_points, kind="Boat")
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}. " \
               f"Лодка преодолеет расстояние от Москвы до Харькова за {Boat.travel_time(self)} часа"

    def travel_time(self):
        """Return travel times"""
        return Transport.time_pasted(self.max_speed, self.two_points)


class Plane(Transport, Mechanisms):
    """Prints Plane characteristics"""

    def __init__(self, brand, max_speed, capacity, two_points):
        super().__init__(brand, max_speed, two_points, kind="Plane")
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей. " \
               f"Расстояние от Москвы до Харькова приодолеет за {Plane.travel_time(self)} часа"

    def travel_time(self):
        """Return travel times"""
        return Transport.time_pasted(self.max_speed, self.two_points)


class Rocket(Transport, Mechanisms):
    """Prints Rocket characteristics"""

    def __init__(self, brand, max_speed, capacity, two_points):
        super().__init__(brand, max_speed, two_points, kind="Plane")
        self.capacity = capacity

    def __str__(self):
        return f"Ракета марки {self.brand} вмещает в себя {self.capacity} человека. " \
               f"Расстояние от Москвы до Харькова приодолеет за {Rocket.travel_time(self)} часа"

    def travel_time(self):
        """Return travel times"""
        return Transport.time_pasted(self.max_speed, self.two_points)


Kharkov = 49.97638919268169, 36.20737489756571  # Долгота и широта
Moscow = 55.76388395503755, 37.63016737496982  # Долгота и широта

transport = Transport('Selo', 10, (*Kharkov, *Moscow), 'Telega', 4)
print(transport)
bike = Transport('shkolnik', 20, (*Kharkov, *Moscow), 'bike', 2)
print(bike)
first_plane = Plane('Virgin Atlantic', 700, 450, (*Kharkov, *Moscow))
print(first_plane)
first_car = Car('BMW', 230, 75000, 300, (*Kharkov, *Moscow), 'Car', 4)
print(first_car)
print(first_car.gasoline)
first_car.gasoline = 20
print(first_car.gasoline)
second_car = Car('Audi', 230, 70000, 130, (*Kharkov, *Moscow), 'Car', 4)
second_car.gasoline = [None]
first_boat = Boat('Yamaha', 40, 'Petr', (*Kharkov, *Moscow))
print(first_boat)
first_rocket = Rocket('Union', 43200, 2, (*Kharkov, *Moscow))
print(first_rocket)
print("Максимальные скорости автомобилей", first_car == second_car)  # Реализация метода __eq__
# issubclass(Mechanisms, first_car)  # Реализация метода __subclasscheck__
