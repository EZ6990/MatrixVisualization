from DataObject.Matrix import Matrix


class CMatrix:

    def __init__(self,matrices,pattern):
        self._matrices = matrices
        self._pattern = pattern
        self._size = len(self.matrices)
        M1 = self._matrices[0].size[0]
        M2 = self._matrices[0].size[1]
        self._value = Matrix([[0 for i in range(M1)] for j in range(M2)])
        for i,matrix in enumerate(self._matrices):
            if self._pattern[i] == 1 or self._pattern[i] == 0 or self._pattern[i] == -1:
                self._value += self._pattern[i] * matrix
            else:
                raise ("pattern must be a combination of the numbers (%d, %d, %d)" %(-1, 0, 1))

    @property
    def cvalue(self):
        return self._value
    @property
    def pattern(self):
        return self._pattern

    @property
    def size(self):
        return self._size

    @property
    def matrices(self):
        return self._matrices

