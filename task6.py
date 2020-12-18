def int_func(word):
    return word.capitalize()


words = input('Введите слова через пробел: ')
words_split = words.split(' ')
title_words = []
for w in words_split:
    title_word = int_func(w)
    title_words.append(title_word)


print(' '.join(title_words))
# Либо еще проще
print(words.title())
