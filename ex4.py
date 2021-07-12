def my_func1(x, y):
    return x**y

def my_func2(x, y):
    z = 1
    for i in range(abs(y)):
        z /= x
    return z

z = my_func2(2, -3)
print(z)
