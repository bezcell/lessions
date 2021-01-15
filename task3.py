class OnlyNumbers(Exception):
    def __init__(self, text):
        self.txt = text


my_list = []
while True:
    user_input = input("Введите число: ")
    if user_input == 'stop':
        print(my_list)
        break
    try:
        if not user_input.isdigit():
            try:
                float(user_input)
            except ValueError:
                raise OnlyNumbers("Вводить строки нельзя!")
    except OnlyNumbers as msg:
        print(f"В результате сохранения произошла ошибка: {msg}")
    else:
        my_list.append(user_input)
