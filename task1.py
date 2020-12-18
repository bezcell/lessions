def division(num1, num2):
    if num2 == 0:
        return 'Division by zero!'
    return num1 / num2


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print(division(num1, num2))
