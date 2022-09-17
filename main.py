import argparse
from typing import Tuple

import numpy as np
from numpy.typing import ArrayLike

from canvas import Canvas
from light import AmbientLight, DirectionalLight, Light, PointLight
from shape import Sphere


scene = [
    Sphere((0, -1, 3),      1,      (255, 0, 0),    500),
    Sphere((2, 0, 4),       1,      (0, 0, 255),    500),
    Sphere((-2, 0, 4),      1,      (0, 255, 0),    10),
    Sphere((0, -5010, 0),   5000,   (255, 255, 0),  1000)
]

lights = [
    AmbientLight(0.2),
    PointLight(0.6, (2, 1, 0)),
    DirectionalLight(0.2, (1, 4, 4))
]


def compute_lighting(point, normal, view, specular):
    intensity = 0.
    for light in lights:
        if light.type == Light.Ambient:
            intensity += light.intensity
        else:
            if light.type == Light.Point:
                L = light.position - point
            elif light.type == Light.Directional:
                L = light.direction

            # 漫反射
            n_dot_l = np.dot(normal, L)
            if n_dot_l > 0:
                intensity += light.intensity * n_dot_l / (np.linalg.norm(normal) * np.linalg.norm(L))

            # 镜面反射
            if specular != -1:
                R = 2 * normal * np.dot(normal, L) - L
                r_dot_v = np.dot(R, view)
                if r_dot_v > 0:
                    intensity += light.intensity * np.power(r_dot_v / (np.linalg.norm(R) * np.linalg.norm(view)), specular)

    return intensity


def intersect_ray_sphere(origin: ArrayLike, direction: ArrayLike, sphere: Sphere) -> Tuple[float, float]:
    r = sphere.radius
    CO = origin - sphere.center

    a = np.dot(direction, direction)
    b = 2 * np.dot(CO, direction)
    c = np.dot(CO, CO) - r*r

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return np.inf, np.inf

    t1 = (-b + np.sqrt(discriminant)) / (2 * a)
    t2 = ( b + np.sqrt(discriminant)) / (2 * a)

    return t1, t2


def trace_ray(origin: ArrayLike, direction: ArrayLike, min_t: float, max_t: float):
    closest_t = np.inf
    closest_sphere = None

    for sphere in scene:
        t1, t2 = intersect_ray_sphere(origin, direction, sphere)

        if min_t <= t1 <= max_t and t1 < closest_t:
            closest_t = t1
            closest_sphere = sphere

        if min_t <= t2 <= max_t and t2 < closest_t:
            closest_t = t2
            closest_sphere = sphere

    if closest_sphere == None:
        return np.array([255, 255, 255])

    # 漫反射计算颜色
    point = origin + closest_t * direction
    normal = point - closest_sphere.center
    normal = normal / np.linalg.norm(normal)

    return closest_sphere.color * compute_lighting(point, normal, -direction, closest_sphere.specular)


def main(size=(600, 600)):
    p_camera = np.array([0, 0, 0], dtype=np.float32)

    canvas = Canvas(size=size, viewport_size=(1, 1))
    width, height = canvas.size
    for r in range(height):
        for c in range(width):
            v_direction = canvas.canvas_to_viewport(r, c)
            color = trace_ray(p_camera, v_direction, 1, np.inf)
            canvas.put_pixel(r, c, color)
    canvas.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, nargs='+', default=[600, 600])
    args = parser.parse_args()

    main(args.size)
