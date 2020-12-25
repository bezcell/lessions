with open("task2.txt", "r") as user_file:
    rows = 0
    for user_line in user_file.readlines():
        rows += 1
        words_list = user_line.split(" ")
        row_len = len(words_list)
        print(f"In line {rows} {row_len} words")


print(f"Count rows: {rows}")
