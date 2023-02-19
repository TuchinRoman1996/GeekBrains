def my_degree(x, y):
    return x**y


def my_degree_2(x, y):
    res = 1/x
    for i in range(1, abs(y)):
        res *= 1/x
    return res


print(f'Первый способ: {my_degree(6, -2)}')
print(f'Второй способ: {my_degree_2(6,-2)}')
