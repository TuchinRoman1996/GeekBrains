# Задание 6
revenue = int(input('Введите размер выручки: '))
costs = int(input('Введите размер издержек: '))
profit = revenue-costs
print(f'Размер прибыли составил: {profit} у.е.')

if profit > 0:
    rentable = (profit/revenue)*100
    print(f'Рентабельность выручки: {rentable}')
count_rab = int(input('Введите кол-во сотрудников: '))
print(f'Прибыль на одного сотрудника: {profit/count_rab}')