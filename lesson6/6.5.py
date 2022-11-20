class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка "{self.title}" - тонкие четкие линии')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка "{self.title}" - линии разной толщины')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка "{self.title}" - толстые линии')


my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')

my_pen.draw()
my_pencil.draw()
my_handle.draw()
