string = input('Введите строку из нескольких слов разделенную пробелами: ')
for i in range(len(string.split(' '))):
    if string.split(" ")[i] in ' ':
        continue
    elif len(string.split(" ")[i]) > 10:
        print(f'{i + 1}) {string.split(" ")[i][0:9]}')

    else:
        print(f'{i+1}) {string.split(" ")[i]}')