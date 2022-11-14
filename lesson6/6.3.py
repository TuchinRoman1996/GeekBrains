class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def income_sum(self):
        print(self._income['wage'] + self._income['bonus'])


my_object_1 = Position('Виталий', 'Песоцкий', 'Разработчик', 65000, 30000)
my_object_2 = Position('Роман', 'Тучин', 'Аналитик', 45000, 20000)

my_object_1.get_full_name()
my_object_1.income_sum()
my_object_2.get_full_name()
my_object_2.income_sum()

