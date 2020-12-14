my_str = input("Введите предложение: ")
words = my_str.split(" ")

i = 1
for word in words:
    if len(word) > 10:
        word = word[:10]
    print(f"{i}: {word}")
    i += 1
