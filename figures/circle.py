from figures import Figure
from figures.color import Color
from math import pi


class Circle(Figure):
    _name = 'Circle'

    def __init__(self, radius: int, color: str):
        self._color = Color(color)
        self._radius = radius

    def area(self):
        return pi * self._radius ** 2

    @classmethod
    def name(cls):
        return cls._name

    def __repr__(self):
        return "{} with radius {} and area {:.2f} of color {}"\
            .format(self._name, self._radius, self.area(), self._color.value)
