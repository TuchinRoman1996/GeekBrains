my_list = []
for i in range(5):
    el = input(f'Введите значение элмента {i}/4: ')
    my_list.insert(i-1, el) if i % 2 else my_list.append(el)
print(my_list)
