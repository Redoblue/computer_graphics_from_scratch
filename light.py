from enum import Enum

from vector import Vector3

Light = Enum('Light', ('Ambient', 'Point', 'Directional'))


class MetaLight(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs, **kwargs)
        if name == 'BaseLight': return
        cls.type = eval(f"Light.{name.replace('Light', '')}")


class BaseLight(metaclass=MetaLight):

    def __init__(self, intensity: float) -> None:
        self.intensity = intensity


class AmbientLight(BaseLight):

    def __init__(self, intensity: float) -> None:
        super().__init__(intensity)


class PointLight(BaseLight):

    def __init__(self, intensity: float, position: Vector3) -> None:
        super().__init__(intensity)
        self.position = Vector3(*position)


class DirectionalLight(BaseLight):

    def __init__(self, intensity: float, direction: Vector3) -> None:
        super().__init__(intensity)
        self.direction = Vector3(*direction)

