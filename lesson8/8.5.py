class Stock:
    def __init__(self, address, availability):
        try:
            self.address = str(address)
            self.availability = list(availability)
        except (ValueError, TypeError):
            print('Адрес - строка\nНаличие - справочник')

    def to_accept(self, other):
        my_dict = {}
        for i in other.__dict__:
            my_dict[i] = other.__getattribute__(i)
        self.availability.append(my_dict)
        print(self.availability)

    def hend_over(self, other, position):
        other.availability.append(self.availability.pop(position))


class OfficeEquipment:
    def __init__(self):
        voltage = '220 В.'
        connector = 'Type C'


class Printer(OfficeEquipment):
    def __init__(self, model, technology, colorage, print_speed, count):
        super().__init__()
        self.model = model
        self.technology = technology
        self.colorage = colorage
        self.print_speed = print_speed
        self.count = int(count)


class Scanner(OfficeEquipment):
    def __init__(self, model, technology, optical_res, max_format, count):
        super().__init__()
        self.model = model
        self.technology = technology
        self.optical_res = optical_res
        self.max_format = max_format
        self.count = int(count)


class Xerox(OfficeEquipment):
    def __init__(self, model, technology, trays, paper_density, count):
        super().__init__()
        self.model = model
        self.technology = technology
        self.trays = trays
        self.paper_density = paper_density
        self.count = int(count)


my_stock = Stock('Москва, ЛЦ Внуково EMS1-СМ', [])                     # Создаем объект первого склада
my_printer = Printer('Has-123', 'Jet', 'Black and White', 'A4', '23')  # Создаем объект принтера
my_stock.to_accept(my_printer)                                         # Примем принтер на первый склад
my_stock2 = Stock('Нижний новгород, ул.Пискунова, д.2к1', [])          # Создадим второй склад (в подразделении)
my_stock.hend_over(my_stock2, 0)                                       # Передадим этот принтер в наш филиал
print(my_stock.availability)                                           # Теперь на первом складе его нет
print(my_stock2.availability)                                          # Принтер появился на складе филиала в НН
