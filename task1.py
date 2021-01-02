class Matrix:
    matrix = {}

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for row in self.matrix:
            for cell in row:
                res += f"{cell} "
            res += "\n"
        return res

    def __add__(self, other):
        for i_row, row in enumerate(other):
            for i_cell, cell in enumerate(row):
                self.matrix[i_row][i_cell] += cell


test_matrix = [
    [23, 50, 100],
    [54, 12, 2],
    [56, 77, 45]
]
test_matrix2 = [
    [23, 50, 100],
    [54, 12, 2],
    [56, 77, 45]
]

mc = Matrix(test_matrix)
plus = mc + test_matrix2
print(mc)
