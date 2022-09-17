from typing import Annotated, Tuple

import numpy as np

from vector import Vector3
from color import Color


class Sphere():

    def __init__(self, center: Tuple[int], radius: int, color: Annotated[Tuple[int], 3]=(0, 0, 0), specular: int=-1) -> None:
        self.center = Vector3(*center)
        self.radius = radius
        self.color = color(*color)
        self.specular = specular
