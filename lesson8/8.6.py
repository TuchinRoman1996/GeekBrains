class Validator(Exception):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    def __init__(self, address, availability):
        try:
            self.address = str(address)
            self.availability = availability
            if type(self.availability) != list:
                raise Validator('Наличие д.б. списком')
        except ValueError:
            print('Адрес д.б. строкой')
        except Validator as err:
            print(err)

    def to_accept(self, other):
        my_dict = {}
        for i in other.__dict__:
            my_dict[i] = other.__getattribute__(i)
        try:
            self.availability.append(my_dict)
            print(self.availability)
        except AttributeError:
            print('Нужен список')

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
        try:
            self.count = int(count)
        except ValueError:
            print('Только числа')


class Scanner(OfficeEquipment):
    def __init__(self, model, technology, optical_res, max_format, count):
        super().__init__()
        self.model = model
        self.technology = technology
        self.optical_res = optical_res
        self.max_format = max_format
        try:
            self.count = int(count)
        except ValueError:
            print('Только числа')


class Xerox(OfficeEquipment):
    def __init__(self, model, technology, trays, paper_density, count):
        super().__init__()
        self.model = model
        self.technology = technology
        self.trays = trays
        self.paper_density = paper_density
        try:
            self.count = int(count)
        except ValueError:
            print('Только числа')


my_stock = Stock('Москва, ЛЦ Внуково EMS1-СМ', '234')                  # Передадим в качестве аргумента строку
my_printer = Printer('Has-123', 'Jet', 'Black and White', 'A4', 'фывыфв')  # Передадим в качестве аргумента символ

