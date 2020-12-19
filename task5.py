from functools import reduce


def sum_elements(x, y):
    return x + y


my_list = [item for item in range(100, 1001) if item % 2 == 0]
my_result = reduce(sum_elements, my_list)

print(my_result)
