with open('5.3.txt', 'r', encoding='utf-8') as file:
    print(f'Сотрудники с окладом менее 20к: {", ".join([i.split()[0] for i in file if float(i.split()[1]) < 20000])}')
    file.seek(0)
    payments = [float(i.split()[1]) for i in file]
    print(f'Средняя зп составила {round(sum(payments)/len(payments), 2)} у.е.')
