class Color:
    def __init__(self, color: str = ""):
        self._value = color

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, color: str):
        self._value = color
