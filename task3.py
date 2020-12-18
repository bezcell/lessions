def my_func(x, y, z):
    array = [x, y, z]
    array.sort(reverse=True)
    return array[0] + array[1]


res = my_func(11, 2, 4)
print(res)
