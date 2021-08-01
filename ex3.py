class Cell():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        new_num = self.num - other.num
        if new_num > 0:
            return Cell(new_num)
        else:
            print('не могу сделать вычетание')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def __str__(self):
        return f'object {self.__class__.__name__} has {self.num} cells'

    def make_order(self, n_row):
        for row in range(self.num // n_row):
            for el in range(n_row):
                print("*", end = '')
            print()
        ostatok = self.num - self.num // n_row * n_row
        if ostatok > 0:
            for el in range(ostatok):
                print("*", end = '')
            print()




c1 = Cell(10)
c2 = Cell(3)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
c1.make_order(4)
