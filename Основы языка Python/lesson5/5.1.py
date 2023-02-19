file = open('5.1.txt', 'w+', encoding='utf-8')
while True:
    string = input('Введите что-либо:')
    if string:
        file.writelines(string+'\n')
    else:
        break
