from figures import Rectangle


class Square(Rectangle):
    _name = 'Square'

    def __init__(self, side: int, color: str):
        super().__init__(side, side, color)
        self._side = side

    def area(self):
        return super().area()

    @classmethod
    def name(cls):
        return cls._name

    def __repr__(self):
        return "{} with side {} and area {} of color {}"\
            .format(self._name, self._side, self.area(), self._color.value)
