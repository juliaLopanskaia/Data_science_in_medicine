list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
j = 0
for i in range(len(list)//2):
    list[j],list[j+1] = list[j+1],list[j]
    j += 2

print(list)
