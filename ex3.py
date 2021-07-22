data = []
summa = 0

with open('data3.txt') as holder:
    lines = holder.readlines()
    for line in lines:
        data.append(line.split())
    print('зарплату меньшую 20000р имеют:')
    for line in data:
        summa += int(line[1])
        if int(line[1]) < 20000:
            print(line[0])
    print(f'средняя зарплата: {summa/len(data)}')
    #salory.append(line)
