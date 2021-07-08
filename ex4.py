str = input('введите строку ')
str_split = str.split()
for i,word in enumerate(str_split):
    print(i, word[:10])
