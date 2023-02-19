from sys import argv

name, hour, rate, prem = argv
print(f'Зарплата сотрудника = {int(hour)*int(rate)+int(prem)} руб.')