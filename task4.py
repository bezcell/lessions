my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def count_elements(list_items, value):
    count = 0
    for item in list_items:
        if item == value:
            count += 1
    return count


result_list = [item for item in my_list if count_elements(my_list, item) == 1]


print(result_list)
