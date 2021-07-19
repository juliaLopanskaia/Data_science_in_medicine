def fact(N):
    f = 1
    for n in range(1, N+1):
        #print(n)
        f *= n
        yield f

N = 40
for el in fact(N):
    #print('...')
    print(el)
