
import numpy as np
class Matrix:

    def __init__(self,matrix):
        self._matrix = np.array(matrix)
        self._size = self.matrix.shape

    def __add__(self, other):
        if isinstance(other,Matrix):
            if other.size == self.size:
                new_matrix = self._matrix + other.matrix

        return Matrix(new_matrix)

    def __sub__(self, other):
        if isinstance(other,Matrix):
            if other.size == self.size:
                new_matrix = self._matrix - other.matrix

        return Matrix(new_matrix)

    def __mul__(self, other):
        if isinstance(other,int):
            if other == 1 or other == -1 or other == 0:
                new_matrix = self._matrix * other

        return Matrix(new_matrix)

    def __rmul__(self, other):
        return self * other


    @property
    def size(self):
        return self._size

    @property
    def matrix(self):
        return self._matrix