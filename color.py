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
        return np.array([Color.clamp(self.r), Color.clamp(self.g), Color.clamp(self.b)])

    def clamp_(self):
        self.r = Color.clamp(self.r)
        self.g = Color.clamp(self.g)
        self.b = Color.clamp(self.b)

    @staticmethod
    def clamp(value, min_value=0, max_value=255):
        return min(max_value, max(min_value, value))

    def __add__(self, other):
        if isinstance(other, (int, float)):
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