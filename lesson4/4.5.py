from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]


def my_fn(a, b):
    return a * b


print(reduce(my_fn, my_list))
