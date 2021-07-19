import itertools

n = 0
for j in itertools.cycle('marie + vova + '):
    print(j)
    n += 1
    if n > 33:
        break
