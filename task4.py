def my_func(x, y):
    if not isinstance(y, int) or y >= 0:
        return 'Ошибка, введите целое отрицательное число'
    ci = abs(y)
    i = 0
    result = 1
    while i < ci:
        result *= 1 / x
        i += 1
    return result
    # Ну или просто x ** y :)


print(my_func(400, -1))
