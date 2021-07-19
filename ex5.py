import functools

my_list = [num for num in range(100, 1000+1) if num%2 == 0]

def multiplier(num1, num2):
    return num1 * num2

print(functools.reduce(multiplier, my_list))
