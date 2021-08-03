class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


class DataWrite():
    def __init__(self):
        self.data = []

    def get_data(self, num):
        if self.check(num):
            self.data.append(int(num))

    def check(self, x):
        try:
            try:
                int(x)
                return True
            except ValueError:
                raise NotNumber('вы ввели строку')
        except NotNumber:
            print('the string was ignored')
            return False

    def __str__(self):
        print(*self.data)
        return ''


data = DataWrite()
while True:
    x = input('input a number   ')
    if x != 'stop':
        data.get_data(x)
    else:
        break

print(data)
