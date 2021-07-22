with open('data2.txt') as holder:
    text = holder.readlines()
print(f'количество строк в тексте : {len(text)}')

for i in range(len(text)):
    print(f'количество слов в строке №{i+1} : {len(text[i].split())}')
