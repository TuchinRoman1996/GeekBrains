def division(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('Деление на ноль запрещено!\n\np.s.За Вами выехали')
    except TypeError:
        print('Только числа')


print(division(int(input('Введите a:')), input('Введите b:')))
