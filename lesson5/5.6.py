my_dict = {}
with open('5.6.txt', 'r', encoding='utf-8') as file:
    for i in file:
        my_dict[i.split()[0]] = sum([int(x.split('-')[0].split('(')[0]) for x in i.split()[1:] if
                                     x.split('-')[0].split('(')[0] not in (' ', '—', '')])
    print(my_dict)
