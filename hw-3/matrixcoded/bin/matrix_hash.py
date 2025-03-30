from copy import deepcopy
from matrix import Matrix

A = Matrix([
    [2, 0],
    [0, 0]
])

C = Matrix([
    [0, 1],
    [0, 0]
])

B = D = Matrix([
    [1, 0],
    [0, 1]
])

assert hash(A) == hash(C)
assert A != C
assert B == D
assert A @ B == C @ D # due to caching

Matrix.clear_cache()

AB = A @ B

Matrix.clear_cache()

CD = C @ D



for name, matrix in [('A', A), ('B', B), ('C', C), ('D', D), ('AB', AB), ('CD', CD)]:
    with open(f'{name}.txt', 'w') as f:
        f.write(str(matrix))

with open('hash.txt', 'w') as f:
    f.write(f"AB hash: {hash(AB)}\nCD hash: {hash(CD)}")