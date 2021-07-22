my_dict = {}
summa = 0
with open('data6.txt') as holder:
    for line in holder:
        for i in 1,2,3:
            num = line.split()[i].split('(')[0]
            if num != '-':
                summa += int(num)
        my_dict[line.split(':')[0]] = summa
        summa = 0

print(my_dict)
