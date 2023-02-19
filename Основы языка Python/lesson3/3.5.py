def all_sum():
    res = 0
    while True:
        data = input('Ввеите числа через пробел:').split()
        for word in data:
            if word.lower() == 'stop':
                return res
            else:
                res += int(word)
        print(res)


all_sum()