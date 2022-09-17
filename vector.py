import numpy as np
from numpy.typing import ArrayLike


class Vector():

    def __init__(self, *coords) -> None:
        self.__vec = np.array(coords)

    @classmethod
    def from_array(cls, array: ArrayLike):
        val_list = array.flatten().tolist()

        if cls.__name__ == 'Vector2':
            assert len(val_list) == 2, "number of elements should equal 2"
        elif cls.__name__ == 'Vector3':
            assert len(val_list) == 3, "number of elements should equal 3"
        
        return cls(*val_list)

    @property
    def vector(self):
        return self.__vec

    @property
    def length(self):
        return np.linalg.norm(self.__vec)

    def normalize(self):
        return self.__vec / self.length
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__vec.tolist()})"

    def __sub__(self, other):
        assert self.__class__ == other.__class__, "vector types doesn't match"
        return self.__class__.from_array(self.vector - other.vector)


class Vector2(Vector):

    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    @property
    def xy(self):
        return self.__vec

    @property
    def x(self):
        return self.__vec[0]

    @property
    def y(self):
        return self.__vec[1]


class Vector3(Vector):

    def __init__(self, x, y, z) -> None:
        super().__init__(x, y, z)

    @property
    def xyz(self):
        return self.__vec

    @property
    def x(self):
        return self.__vec[0]

    @property
    def y(self):
        return self.__vec[1]

    @property
    def z(self):
        return self.__vec[2]


if __name__ == '__main__':
    vec1 = Vector3.from_array(np.array([1, 2, 3]))
    print(vec1.vector)

    vec2 = Vector3(1, 2, 3)
    print(vec2.vector)

    import ipdb; ipdb.set_trace()