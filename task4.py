dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open("task4.txt", "r") as user_file:
    for user_line in user_file.readlines():
        words_list = user_line.split(" - ")
        word_num = words_list[0]
        num_num = words_list[1]
        with open("debug.txt", "a") as new_file:
            new_file.writelines(f"{dictionary[word_num]} - {num_num}")
