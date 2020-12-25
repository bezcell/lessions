with open("task3.txt", "r") as user_file:
    all_sum = 0
    str_count = 0
    for user_line in user_file.readlines():
        str_count += 1
        words_list = user_line.split(" ")
        user_name = words_list[0]
        user_sum = int(words_list[1])
        all_sum += user_sum
        if user_sum < 20000:
            print(f"{user_name} зарабатывает мало!")

    mid_sum = all_sum / str_count
    print(f"Средняя зарплата: {mid_sum}")
