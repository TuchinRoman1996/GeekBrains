def fact(n):
    x = 1
    for el in range(1, n+1):
        x *= el
        yield x


for i in fact(4):
    print(i)
