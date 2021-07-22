finished = False
with open('data.txt', 'w') as holder:
    while not finished:
        line = input('введите строку  ')
        holder.write(line)
        holder.write('\n')
        if line == '':
            finished = True
