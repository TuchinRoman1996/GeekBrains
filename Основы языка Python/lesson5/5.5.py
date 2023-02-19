with open('5.5.txt', 'r', encoding='utf-8') as file:
    try:
        print(sum([float(i) for i in file.readline().split()]))
    except ValueError:
        print('В файле должны быть только числа')