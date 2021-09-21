"""The CODESTYLE method is designed to elevate writing to the rank of art"""


class Calcul:
    """Simplest calculator"""

    def __init__(self, name, number):
        """Name and number"""
        self.name = name
        self.number = number

    @staticmethod
    def obj_calcul_check(obj):
        """ostaticmethod obj must be A Calcul class object"""
        return isinstance(obj, Calcul)

    def __add__(self, obj):
        """Addition"""
        if Calcul.obj_calcul_check(obj):
            return f"{self.name + obj.name} : {self.number + obj.number}"
        raise TypeError("A Calcul type object was expected")

    def __mul__(self, obj):
        """Multiplication"""
        if Calcul.obj_calcul_check(obj):
            return f"{self.name} * {obj.name} : {self.number * obj.number}"
        raise TypeError("A Calcul type object was expected")

    def __sub__(self, obj):
        """Subtraction"""
        if Calcul.obj_calcul_check(obj):
            return f"{obj.name[:3]}{self.name[-3:]} : {self.number - obj.number}"
        raise TypeError("A Calcul type object was expected")

    def __truediv__(self, obj):
        """True division"""
        if Calcul.obj_calcul_check(obj):
            return f"{self.name[-1:] + obj.name[-3:]} : {self.number // obj.number}"
        raise TypeError("A Calcul type object was expected")


# from calc import Calcul

back = Calcul("after", 20)
fire = Calcul("math", 5)
mile = Calcul("brain", 2)
stone = Calcul("storm", 10)
print(back + fire)
print(back - fire)
print(fire * stone)
print(stone / mile)
