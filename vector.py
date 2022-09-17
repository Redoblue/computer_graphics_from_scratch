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
    
    @property
    def dtype(self):
        return self.__vec.dtype
    
    def astype(self, dtype):
        return self.__vec.astype(dtype)

    def normalize(self):
        return self.div(self.length)
    
    def dot(self, other):
        return np.dot(self.vector, other.vector)
    
    def add(self, other):
        if self.__class__ == other.__class__:
            return self.__class__.from_array(self.vector + other.vector)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__.from_array(self.vector + other)
        raise TypeError

    def sub(self, other):
        if self.__class__ == other.__class__:
            return self.__class__.from_array(self.vector - other.vector)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__.from_array(self.vector - other)
        raise TypeError

    def mul(self, other):
        if self.__class__ == other.__class__:
            return self.__class__.from_array(self.vector * other.vector)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__.from_array(self.vector * other)
        raise TypeError

    def div(self, other):
        if self.__class__ == other.__class__:
            return self.__class__.from_array(self.vector / other.vector)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__.from_array(self.vector / other)
        raise TypeError

    def __add__(self, other):
        return self.add(other)
    
    def __radd__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)
    
    def __rsub__(self, other):
        if self.__class__ == other.__class__:
            return self.__class__.from_array(other.vector - self.vector)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__.from_array(other / self.vector)
        raise TypeError

    def __mul__(self, other):
        return self.mul(other)
    
    def __rmul__(self, other):
        return self.mul(other)

    def __truediv__(self, other):
        return self.div(other)
    
    def __rtruediv__(self, other):
        if self.__class__ == other.__class__:
            return self.__class__.from_array(other.vector / self.vector)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__.from_array(other / self.vector)
        raise TypeError

    def __neg__(self):
        return self.__class__.from_array(-self.vector)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__vec.tolist()})"


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