def int_func(word):
    print(word.capitalize())


data = input('Введите строку из слов: ')
for word in data.split():
    int_func(word)