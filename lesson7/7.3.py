class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        return '*' * (self.count_cell + other.count_cell)

    def __sub__(self, other):
        res = self.count_cell - other.count_cell
        if res > 0:
            return '*' * res
        else:
            print('Разность клеток меньше нуля')

    def __mul__(self, other):
        return '*' * self.count_cell * other.count_cell

    def __truediv__(self, other):
        return '*' * round(self.count_cell / other.count_cell)

    def __iter__(self):
        return iter(str(self.count_cell))

    def make_order(self, cells, in_row):
        for i in range(len(cells)):
            if ((i + 1) % in_row) == 0:
                print('*' * in_row)


my_cell = Cell(30)
my_cell_2 = Cell(10)
# Произведение ячеек выполним отдельно
my_cell_3 = my_cell * my_cell_2
print(f'Сложение ячеек: {my_cell + my_cell_2}')
print(f'Разность ячеек: {my_cell - my_cell_2}')
print(f'Деление ячеек: {my_cell / my_cell_2}')
print('Произведение ячеек:')
my_cell.make_order(my_cell_3, 10)
