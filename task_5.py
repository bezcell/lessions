i_num = int(input("Введите число рейтинга: "))
my_list = [7, 5, 3, 3, 2]

i = 0
update = False
for item in my_list:
    if i_num >= item:
        my_list.insert(i, i_num)
        update = True
        break
    i += 1

if not update:
    my_list.append(i_num)

print(my_list)
