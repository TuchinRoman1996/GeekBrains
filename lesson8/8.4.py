class Stock:
    def __init__(self, address, square):
        self.address = address
        self.square = square


class OfficeEquipment:
    def __init__(self):
        voltage = '220 В.'
        connector = 'Type C'


class Printer(OfficeEquipment):
    def __init__(self, technology, colorage, print_speed):
        super().__init__()
        self.technology = technology
        self.colorage = colorage
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, technology, optical_res, max_format):
        super().__init__()
        self.technology = technology
        self.optical_res = optical_res
        self.max_format = max_format


class Xerox(OfficeEquipment):
    def __init__(self, technology, trays, paper_density):
        super().__init__()
        self.technology = technology
        self.trays = trays
        self.paper_density = paper_density
