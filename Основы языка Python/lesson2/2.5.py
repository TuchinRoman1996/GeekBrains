my_list = [7, 5, 3, 3, 2]
num = int(input('Введите натуральное число: '))
if num > 9:
    print('Я так не работаю')
elif num in my_list:
    my_list.insert(my_list.index(num) + my_list.count(num), num)
    print(my_list)
elif num < my_list[-1]:
    my_list.append(num)
    print(my_list)
elif num > my_list[0]:
    my_list.insert(0, num)
    print(my_list)
