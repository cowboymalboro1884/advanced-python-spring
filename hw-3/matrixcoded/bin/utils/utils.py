from matrixcoded import Matrix

def write_matrix_to_file(matrix: Matrix, filename: str) -> None:
    with open(filename, 'w') as f:
        for row in matrix.data:
            f.write(" ".join(map(str, row)) + "\n")
