import time


class TrafficLight:
    __color = 'Red'

    def running(self):
        print(self.__color)
        self.__color = 'Yellow'
        time.sleep(7)
        print(self.__color)
        self.__color = 'Green'
        time.sleep(2)
        print(self.__color)
        time.sleep(4)


my_object = TrafficLight()
my_object.running()
