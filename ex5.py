num_list = [1, 2, 3, 44, 2, 19]

str_list = []
for num in num_list:
    str_list.append(str(num))

with open('data5.txt', 'w') as h_write:
    print(' '.join(str_list), file=h_write)

summa = 0
with open('data5.txt') as h_read:
    for el in h_read.readline().split():
        summa += int(el)
print(f'сумма чисел в файле: {summa}')
