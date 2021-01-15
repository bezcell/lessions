class ComplexOperations:
    num = 0

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


num_1 = ComplexOperations(1 + 1j)
num_2 = ComplexOperations(2 + 2j)
print(num_1 + num_2)
print(num_1 * num_2)
