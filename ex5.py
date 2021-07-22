class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        super().draw()
        print('we draw a pen')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        super().draw()
        print('we draw a pencil')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        super().draw()
        print('we draw a handle')


pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()
