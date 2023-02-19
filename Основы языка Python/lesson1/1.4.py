# Задание 4
num = int(input('Введите целое положительное число:'))
max_num = 0
while num > 0:
    if max_num == 9:
        break
    elif max_num < num % 10:
        max_num = num % 10
    num //= 10

print(f'Максимальная цифра в числе: {max_num}')