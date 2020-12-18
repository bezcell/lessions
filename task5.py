total = 0


def sum_my_numbers(num_str, t):
    numbers = num_str.split(' ')
    for num in numbers:
        if num == 'stop':
            return t, True
        t += int(num)
    return t, False


while True:
    numbers_str = input('Введите числа через пробел (чтобы остановиться, введите stop): ')
    total, stop = sum_my_numbers(numbers_str, total)
    print(total)
    if stop:
        break
