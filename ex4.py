''' Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости. '''

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('we go')
    def stop(self):
        print('we stop')
    def turn(self, direction):
        print(f'we turn {direction}')
    def show_speed(self):
        print(f'speed is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('you are out of limits')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('you are out of limits')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(70, 'red', 'mazda', True)
car1.go()
car1.stop()
car1.turn('left')
car1.show_speed()

car2 = WorkCar(50, 'red', 'mazda', True)
car2.go()
car2.stop()
car2.turn('left')
car2.show_speed()

car2 = SportCar(50, 'red', 'mazda', True)
car2.go()
car2.stop()
car2.turn('left')
car2.show_speed()
