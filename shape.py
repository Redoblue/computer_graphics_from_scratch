from typing import Annotated, Tuple

import numpy as np


class Sphere():

    def __init__(self, center: Tuple[int], radius: int, color: Annotated[Tuple[int], 3]=(0, 0, 0), specular: int=-1) -> None:
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color)
        self.specular = specular
