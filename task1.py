while True:
    user_str = input("Введите строку: ")
    if user_str == '':
        break
    with open("task1.txt", "a") as user_file:
        user_file.writelines(f"{user_str}\n")
