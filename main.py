from typing import Tuple

import numpy as np

from canvas import Canvas
from color import Color
from light import AmbientLight, DirectionalLight, Light, PointLight
from shape import Sphere
from vector import Vector3



scene = [
    Sphere((0, -1, 3),      1,      (255, 0, 0),    500),
    Sphere((2, 0, 4),       1,      (0, 0, 255),    500),
    Sphere((-2, 0, 4),      1,      (0, 255, 0),    10),
    Sphere((0, -5001, 0),   5000,   (255, 255, 0),  1000)
]

lights = [
    AmbientLight(0.2),
    PointLight(0.6, (2, 1, 0)),
    DirectionalLight(0.2, (1, 4, 4))
]


def compute_lighting(point, normal, view, specular):
    P = point
    N = normal
    V = view

    intensity = 0.

    for light in lights:
        if light.type == Light.Ambient:
            intensity += light.intensity
        else:
            if light.type == Light.Point:
                L = light.position - P
                max_t = 1
            elif light.type == Light.Directional:
                L = light.direction
                max_t = np.inf
            
            # 阴影检测
            shadow_sphere, shadow_t = closest_intersection(P, L, 0.001, max_t)
            if shadow_sphere != None:
                continue

            # 漫反射
            n_dot_l = N.dot(L)
            if n_dot_l > 0:
                intensity += light.intensity * n_dot_l / (N.length * L.length)

            # 镜面反射
            if specular != -1:
                R = 2 * N * N.dot(L) - L
                r_dot_v = R.dot(V)
                if r_dot_v > 0:
                    intensity += light.intensity * np.power(r_dot_v / (R.length * V.length), specular)

    return intensity


def intersect_ray_sphere(origin: Vector3, direction: Vector3, sphere: Sphere) -> Tuple[float, float]:
    O = origin
    D = direction

    r = sphere.radius
    CO = O - sphere.center

    a = D.dot(D)
    b = 2 * CO.dot(D)
    c = CO.dot(CO) - r*r

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return np.inf, np.inf

    t1 = (-b + np.sqrt(discriminant)) / (2 * a)
    t2 = (-b - np.sqrt(discriminant)) / (2 * a)

    return t1, t2


def closest_intersection(origin: Vector3, direction: Vector3, min_t: float=0, max_t: float=np.inf) -> Tuple[Sphere, float]:
    O = origin
    D = direction

    closest_t = np.inf
    closest_sphere = None

    for sphere in scene:
        t1, t2 = intersect_ray_sphere(O, D, sphere)

        if min_t <= t1 <= max_t and t1 < closest_t:
            closest_t = t1
            closest_sphere = sphere

        if min_t <= t2 <= max_t and t2 < closest_t:
            closest_t = t2
            closest_sphere = sphere
    
    return closest_sphere, closest_t


def trace_ray(origin: Vector3, direction: Vector3, min_t: float, max_t: float, background_color: Color):
    O = origin
    D = direction

    closest_sphere, closest_t = closest_intersection(O, D, min_t, max_t)
    if closest_sphere == None:
        return background_color

    # 漫反射计算颜色
    P = O + closest_t * D
    N = P - closest_sphere.center
    N = N.normalize()

    return closest_sphere.color * compute_lighting(P, N, -D, closest_sphere.specular)


def main(canvas_size=(400, 400), viewport_size=(1., 1.), proj_plane_z=1.0, camera_position=(0, 0, 0), background_color=(255, 255, 255)):
    camera_position = Vector3(*camera_position)
    background_color = Color(*background_color)

    canvas = Canvas(size=canvas_size, viewport_size=viewport_size, proj_plane_z=proj_plane_z)
    for r in range(canvas.height):
        for c in range(canvas.width):
            direction = canvas.canvas_to_viewport(r, c)
            color = trace_ray(camera_position, direction, 1, np.inf, background_color=background_color)
            canvas.put_pixel(r, c, color.clamp())
    canvas.show()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--canvas-size', type=int, nargs='+', default=[600, 600])
    parser.add_argument('--viewport-size', type=float, nargs='+', default=[1., 1.])
    parser.add_argument('--proj-plane-z', type=float, default=1.0)
    parser.add_argument('--camera-position', type=float, nargs='+', default=[0., 0., 0.])
    parser.add_argument('--background-color', type=int, nargs='+', default=[255, 255, 255])
    args = parser.parse_args()

    main(args.canvas_size,
        args.viewport_size,
        args.proj_plane_z,
        args.camera_position,
        args.background_color)
