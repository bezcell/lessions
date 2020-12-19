my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


formatted_list = [item for key, item in enumerate(my_list) if key > 0 and item > my_list[key - 1]]


print(formatted_list)
