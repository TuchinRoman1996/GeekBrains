class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if (self.b + other.b) < 0:
            return f'{self.a + other.a}{self.b + other.b}i'
        else:
            return f'{self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        if (self.a * other.b + self.b * other.a) < 0:
            return f'{self.a * other.a - self.b * other.b}{self.a * other.b + self.b * other.a}'
        else:
            return f'{self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i'


z1 = ComplexNumbers(5, -6)
z2 = ComplexNumbers(-3, 2)
print(z1 + z2)
print(z1 * z2)
