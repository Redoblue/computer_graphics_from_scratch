from typing import Tuple

from vector import Vector3
from color import Color


class Sphere():

    def __init__(self, center: Tuple[float, float, float], radius: int, color: Tuple[int, int, int]=(0, 0, 0), specular: int=-1) -> None:
        self.center = Vector3(*center)
        self.radius = radius
        self.color = Color(*color)
        self.specular = specular
