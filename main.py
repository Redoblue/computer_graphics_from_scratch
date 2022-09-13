import argparse
from typing import Tuple

import numpy as np
from numpy.typing import ArrayLike

from canvas import Canvas


class Sphere():

    def __init__(self, center: Tuple[int], radius: int, color: Tuple[int]=(0, 0, 0)) -> None:
        self.center = np.array(center)
        self.radius = radius
        self.color = color


scenes = [
    Sphere((0, -1, 3), 1, (255, 0, 0)),
    Sphere((2, 0, 4), 1, (0, 0, 255)),
    Sphere((-2, 0, 4), 1, (0, 255, 0))
]


def intersect_ray_sphere(O: ArrayLike, D: ArrayLike, sphere: Sphere) -> Tuple[float, float]:
    r = sphere.radius
    CO = O - sphere.center

    a = np.dot(D, D)
    b = 2 * np.dot(CO, D)
    c = np.dot(CO, CO) - r*r

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return np.inf, np.inf
    
    t1 = (-b + np.sqrt(discriminant)) / (2 * a)
    t2 = (b + np.sqrt(discriminant)) / (2 * a)

    return t1, t2


def trace_ray(O: ArrayLike, D: ArrayLike, t_min: float, t_max: float):
    closest_t = np.inf
    closest_sphere = None

    for sphere in scenes:
        t1, t2 = intersect_ray_sphere(O, D, sphere)

        if t_min <= t1 <= t_max and t1 < closest_t:
            closest_t = t1
            closest_sphere = sphere
        
        if t_min <= t2 <= t_max and t2 < closest_t:
            closest_t = t2
            closest_sphere = sphere
    
    if closest_sphere == None:
        return (255, 255, 255)
    
    return closest_sphere.color


def main(size=(800, 800)):
    O = np.array([0, 0, 0], dtype=np.float32)

    canvas = Canvas(size=size, viewport_size=(1, 1))
    width, height = canvas.size
    for r in range(height):
        for c in range(width):
            D = canvas.canvas_to_viewport(r, c)
            color = trace_ray(O, D, 1, np.inf)
            canvas.put_pixel(r, c, color)
    canvas.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, nargs='+', default=[800, 800])
    args = parser.parse_args()

    main(args.size)
