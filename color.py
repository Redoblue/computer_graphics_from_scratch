import numpy as np


class Color:

    def __init__(self, r, g, b) -> None:
        self.r = r
        self.g = g
        self.b = b

    @property
    def array(self):
        return np.array([self.r, self.g, self.b])

    def clamp(self):
        return Color(Color._clamp(self.r), Color._clamp(self.g), Color._clamp(self.b))

    def clamp_(self):
        self.r = Color._clamp(self.r)
        self.g = Color._clamp(self.g)
        self.b = Color._clamp(self.b)

    @staticmethod
    def _clamp(value, min_value=0, max_value=255):
        return min(max_value, max(min_value, value))

    def __add__(self, other):
        if isinstance(other, Color):
            r = self.r + other.r
            g = self.g + other.g
            b = self.b + other.b
            return Color(r, g, b)
        elif isinstance(other, (int, float)):
            r = int(self.r + other)
            g = int(self.g + other)
            b = int(self.b + other)
            return Color(r, g, b)
        raise TypeError
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            r = int(self.r * other)
            g = int(self.g * other)
            b = int(self.b * other)
            return Color(r, g, b)
        raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self) -> str:
        return self.__class__.__name__ + f'({self.r}, {self.g}, {self.b})'