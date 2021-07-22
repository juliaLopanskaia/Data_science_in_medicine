from time import sleep
import itertools


class TrafficLight():
    __color = 'red'
    def running(self):
        for color in itertools.cycle(['red', 'yellow', 'green']):
            self.__color = color
            print(self.__color)
            if self.__color == 'red':
                sleep(7)
            elif self.__color == 'yellow':
                sleep(2)
            else:
                sleep(0.5)


trlight = TrafficLight()
trlight.running()
