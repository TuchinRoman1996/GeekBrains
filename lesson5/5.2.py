with open('5.2.txt', 'r', encoding='utf-8') as file:
    line = 0
    while True:
        word = len(file.readline().split())
        if word:
            line += 1
            print(f'{line} строка содержит {word} слов')
        else:
            break

    print(f'Всего {line} строк')
