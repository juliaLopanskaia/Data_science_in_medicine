class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('введите делимое '))
b = int(input('введите делитель '))
try:
    if b == 0:
        raise ZeroDiv('делитель не может равняться нулю!')
    else:
        print(a/b)
except ZeroDiv as err:
    print(err)
