translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
transl_data = []

with open('data4.txt') as holder:
    for line in holder:
        transl_data.append([translation[line.split()[0]], line.split()[1], line.split()[2], '\n'])

print(transl_data)
with open('data4_out.txt', 'w') as w_holder:
    for line in transl_data:
        line_str = ' '.join(line)
        w_holder.writelines(line_str)
