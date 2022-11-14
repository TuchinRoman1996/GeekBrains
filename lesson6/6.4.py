class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км\ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(f'Текущая скорость Town Car: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(f'Текущая скорость Work Car: {self.speed}')


class PoliceCar(Car):
    pass


TownCar = TownCar(70, 'Черный', 'Lincoln-20x', False)
SportCar = SportCar(200, 'Зеленый', 'Ferrari GT', False)
WorkCar = WorkCar(40, 'Желтый', 'ПАЗ-21', False)
PoliceCar = PoliceCar(100, 'Черно-белый', 'kia optima', True)

# Доступ к атрибутам:
print(TownCar.speed)
print(SportCar.color)
print(WorkCar.name)
print(PoliceCar.is_police)

# Доступ к методам:
TownCar.go()
SportCar.stop()
WorkCar.turn('направо')
PoliceCar.show_speed()



