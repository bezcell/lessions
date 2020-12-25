num_list = ['1', '20', '100', '2', '33', '33', '445', '5']

with open("debug.txt", "a") as user_file:
    user_file.writelines(" ".join(num_list))

with open("debug.txt") as user_read_file:
    user_line = user_read_file.readline()
    user_sum = 0
    for num in user_line.split(" "):
        user_sum += int(num)
    print(f"Сумма чисел в файле: {user_sum}")
