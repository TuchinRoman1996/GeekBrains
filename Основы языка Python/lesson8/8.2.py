class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    numerator = int(input('Введите чеслитель:'))
    denominator = int(input('Введите знаменатель:'))
    if denominator == 0:
        raise MyZeroDivisionError('Деление на ноль запрещено')
    else:
        print(f'Результат: {numerator / denominator}')
except (ValueError, MyZeroDivisionError) as err:
    print(err)
