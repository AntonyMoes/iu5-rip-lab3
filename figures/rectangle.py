from figures import Figure
from figures.color import Color


class Rectangle(Figure):
    _name = 'Rectangle'

    def __init__(self, width: int, height: int, color: str):
        self._width = width
        self._height = height
        self._color = Color(color)

    def area(self):
        return self._width * self._height

    @classmethod
    def name(cls):
        return cls._name

    def __repr__(self):
        return "{} ({} x {}) with area {} of color {}"\
            .format(self._name, self._width, self._height, self.area(), self._color.value)
