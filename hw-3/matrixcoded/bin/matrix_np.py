import numpy as np

class ArithmeticMixin:
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.shape != other.shape:
            raise ValueError("Matrix dimensions must match for addition")
        return self.__class__(self.data + other.data)
    
    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.shape != other.shape:
            raise ValueError("Matrix dimensions must match for element-wise multiplication")
        return self.__class__(self.data * other.data)
    
    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError(f"Matrix multiplication mismatch: {self.shape} vs {other.shape}")
        return self.__class__(self.data @ other.data)

class FileIOMixin:
    def save_to_file(self, filename: str) -> None:
        np.savetxt(filename, self.data, fmt='%d')

class DisplayMixin:
    def __str__(self) -> str:
        return np.array2string(self.data, formatter={'int': lambda x: f'{x}'})

class PropertyMixin:
    @property
    def data(self) -> np.ndarray:
        return self._data
    
    @data.setter
    def data(self, value) -> None:
        if isinstance(value, np.ndarray):
            if value.ndim != 2:
                raise ValueError("Matrix must be 2-dimensional")
            self._data = value
        else:
            try:
                arr = np.array(value, dtype=int)
                if arr.ndim != 2:
                    raise ValueError
                self._data = arr
            except:
                raise ValueError("Invalid matrix data format")

    @property
    def rows(self) -> int:
        return self.data.shape[0]
    
    @property
    def cols(self) -> int:
        return self.data.shape[1]
    
    @property
    def shape(self) -> tuple[int, int]:
        return self.data.shape

class Matrix(ArithmeticMixin, FileIOMixin, DisplayMixin, PropertyMixin):
    def __init__(self, data) -> None:
        self.data = data

np.random.seed(0)
m1 = Matrix(np.random.randint(0, 10, (10, 10)))
m2 = Matrix(np.random.randint(0, 10, (10, 10)))
print(m1)
print(m2)

(m1 + m2).save_to_file('matrix+.txt')
(m1 * m2).save_to_file('matrix*.txt')
(m1 @ m2).save_to_file('matrix@.txt')