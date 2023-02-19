from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def consumption(self):
        return 2 * self.growth + 0.3


my_coat = Coat(9)
my_costume = Costume(4)
print(f'Расход ткани на пальто: {my_coat.consumption}')
print(f'Расхож ткани на костюм: {my_costume.consumption}')
print(f'Общий расход ткани: {my_coat.consumption+my_costume.consumption}')
