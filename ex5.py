numbers = []
finished = False
while not finished:
    numbers_str = input('введите числа через пробел  ')
    if 'o' not in numbers_str:
        for num in numbers_str.split():
            numbers.append(int(num))
        print(sum(numbers))
    else:
        for num in numbers_str.split():
            if num != 'o':
                numbers.append(int(num))
            else:
                print(sum(numbers))
                finished = True
