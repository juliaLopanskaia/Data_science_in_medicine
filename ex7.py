import json

pribil_firms = {}
pribil_average = {}
summa = 0
N = 0

with open('data7.txt') as holder:
    for n, line in enumerate(holder):
        pribil_firms[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])
        if (pribil_firms[line.split()[0]]) > 0:
            summa += pribil_firms[line.split()[0]]
            N += 1
    pribil_average['average_profit'] = summa/N

print(pribil_firms)
print(pribil_average)

my_list = [pribil_firms, pribil_average]
#print(my_list)

with open('data7_out.json', 'w') as holder:
    json.dump(my_list, holder)
