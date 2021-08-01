from abc import ABC, abstractmethod

class Maket(ABC):
    @abstractmethod
    def rashod(self):
        pass

class Clothes(Maket):
    def __init__(self, name, val):
        self.name = name
        self.val = val
    @property
    def rashod(self):
        return 'считатаем материалы'

class Coat(Clothes):
    def __init__(self, name, val):
        super().__init__(name, val)
    @property
    def rashod(self): # переопределение свойства
        return f'на {self.name} нужно ткани: {self.val / 6.5 + 0.5}'

class Dress(Clothes):
    def __init__(self, name, val):
        super().__init__(name, val)
    @property
    def rashod(self):
        return f'на {self.name} нужно ткани: {2 * self.val + 0.3}'


coat = Coat('пальто', 100)
costume = Dress('костюм', 55)
print(coat.rashod)
print(costume.rashod)
