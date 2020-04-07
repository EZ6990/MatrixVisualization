import re
import numpy as np
import math
from DataObject.CMatrix import CMatrix
from DataObject.Matrix import Matrix


def _parse_solutions(filepath):
    f = open(filepath, "r")
    solutions = []
    solution = []
    for line in f:
        line = line.rstrip()
        if re.search("\-{12}\d+\-{12}", line):
            solutions.append(solution)
            solution = []
        elif not re.search("^\s*$", line):
            solution.append(line)
    return solutions

def _parse_solution(str_solution):

    int_list = lambda lst: list(map(int, lst))
    str_patterns = str_solution[0]
    str_matrices = str_solution[1]

    arr_patterns = re.findall("{(.*?)}", str_patterns[1:len(str_patterns)-1])
    arr_matrices = re.findall("{(.*?)}", str_matrices[1:len(str_matrices) - 1])

    num = len(arr_matrices)

    patterns = [re.findall("(\-?\d+)", str_pattern) for str_pattern in arr_patterns]
    matrices = [re.findall("(\-?\d+)", str_matrix) for str_matrix in arr_matrices]

    #convert to int
    patterns = list(map(int_list,patterns))
    matrices = list(map(int_list,matrices))

    #reshape
    n = (int)(math.sqrt(len(matrices[0])))
    matrices = np.reshape(matrices,(num,n,n))

    return matrices,patterns



def get_solutions(filepath):
    arr_solutions = _parse_solutions(filepath)
    solutions = []
    for str_solution in arr_solutions:
        arr_matrices,arr_patterns = _parse_solution(str_solution)
        matrices = [Matrix(matrix) for matrix in arr_matrices]
        solutions.append([CMatrix(matrices, pattern) for pattern in arr_patterns])

    return solutions
