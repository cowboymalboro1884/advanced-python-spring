import numpy as np
from typing import List, Union, Any, Dict, Tuple

class HashMixin:
    """
    Hash function: sum of all elements multiplied by matrix dimensions.
    Not collision-resistant! Example collision:
    Matrix([[1,0], [0,0]]) and Matrix([[0,1], [0,0]]) have same hash
    """
    def __hash__(self) -> int:
        total = 0
        for i in range(self.rows):
            for j in range(self.cols):
                total += self.data[i][j] * (i+1) * (j+1)
        return hash(total)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data

class CacheMixin:
    _cache: Dict[Tuple[int, int], 'Matrix'] = {}

    def clear_cache():
        CacheMixin._cache.clear()

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        key = (hash(self), hash(other))
        if key not in CacheMixin._cache:
            if self.cols != other.rows:
                raise ValueError(f"Incompatible dimensions: {self.shape} vs {other.shape}")
            
            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    val = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    row.append(val)
                result.append(row)
            CacheMixin._cache[key] = Matrix(result)
        return CacheMixin._cache[key]

class Matrix(HashMixin, CacheMixin):
    def __init__(self, data: Union[np.ndarray, List[List[Any]]]) -> None:
        if isinstance(data, np.ndarray):
            self.data = data.tolist()
        else:
            self.data = [list(row) for row in data]
        
        self.rows = len(self.data) if self.data else 0
        self.cols = len(self.data[0]) if self.rows else 0
        self.shape = (self.rows, self.cols)
        
        if self.rows:
            for row in self.data:
                if len(row) != self.cols:
                    raise ValueError("All rows must have the same length")

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.shape != other.shape:
            raise ValueError("Matrices must have same dimensions for addition")
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.data])