txt_input = input("Перечислите элементы списка через запятую (1,2,3): ")
arr_input = txt_input.split(",")

length = len(arr_input)
for key, item in enumerate(arr_input):
    if key % 2 == 0 and key + 1 < length:
        save = item
        arr_input[key] = arr_input[key + 1]
        arr_input[key + 1] = save

print(arr_input)
