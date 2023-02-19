class Roads:
    def __init__(self, length, width, density, thickness):
        self._length = length
        self._width = width
        self.density = density
        self.thickness = thickness

    def mass_calc(self):
        res = self._length * self._width * self.density * self.thickness
        print(f'{self._length}м * {self._width}м * {self.density}кг * {self.thickness}см = {res} т')


my_object = Roads(3, 6, 4, 1)
my_object.mass_calc()
