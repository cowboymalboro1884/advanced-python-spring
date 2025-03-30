import numpy as np
from typing import List, Union, Any

class Matrix:
    def __init__(self, data: Union[np.ndarray, List[List[Any]]]) -> None:
        if isinstance(data, np.ndarray):
            self.data = data.tolist()
        else:
            self.data = data
        
        self.rows: int = 0
        self.cols: int = 0
        self.shape: tuple[int, int] = (self.rows, self.cols)
        
        if len(self.data) > 0:
            self.rows = len(self.data)
            self.cols = len(self.data[0])
            for row in self.data:
                if len(row) != self.cols:
                    raise ValueError("All rows must have the same length")
            self.shape = (self.rows, self.cols)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for component-wise multiplication")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError(f"Incompatible dimensions: {self.shape} vs {other.shape}")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                val = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(val)
            result.append(row)
        return Matrix(result)
