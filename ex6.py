list = []
for i in range(3):
    list.append([i, dict()])
    list[i][1]['название'] = input('введите название товара  ')
    list[i][1]['цена'] = int(input('введите цену товара  '))
    list[i][1]['количество'] = input('введите количество товара  ')
    list[i][1]['ед'] = input('введите единицы измерения товара  ')
print(list)


dict = {}
dict['название'] = []
dict['цена'] = []
dict['количество'] = []
dict['ед'] = []
for item in list:
    dict['название'].append(item[1]['название'])
    dict['цена'].append(item[1]['цена'])
    dict['количество'].append(item[1]['количество'])
    dict['ед'].append(item[1]['ед'])

print(dict)
