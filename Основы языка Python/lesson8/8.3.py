class OnlyNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    try:
        num = input('Введите число:')
        if num == 'stop':
            print(my_list)
        elif num not in '0123456789':
            raise OnlyNumber('Только числа')
        else:
            my_list.append(int(num))
    except OnlyNumber as err:
        print(err)
