class MyException(Exception):
    def __init__(self, text):
        self.txt = text


first_num = int(input("Введите делимое число: "))
second_num = int(input("Введите делитель: "))

try:
    if second_num == 0:
        raise MyException("На ноль делить нельзя!")
    result = first_num / second_num
except MyException as msg:
    print(f"В результате деления произошла ошибка: {msg}")
else:
    print(result)
