def my_func(x, y, z):
    numbers = []
    numbers.append(x)
    numbers.append(y)
    numbers.append(z)
    numbers.sort(reverse=True)
    print(numbers[0] + numbers[1])
    return(numbers[0] + numbers[1])


my_func(x=8,z=2,y=8)
