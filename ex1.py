def division():
    x = int(input('введите делимое  '))
    y = int(input('введите делитель  '))
    if y == 0:
        print('не могу делить на ноль!')
    else:
        print(x/y)
        return x/y


division()
