class Matrix():

    def __init__(self, mlist):
        self.mlist = mlist
        print('we created a matrix')

    def __str__(self):
        for row in self.mlist:
            print(*row)
        return ''

    def __add__(self, other):
        new_list = []
        for i, row in enumerate(self.mlist):
            temp = []
            for j, el in enumerate(row):
                temp.append(el + other.mlist[i][j])
            new_list.append(temp)
        return Matrix(new_list)



m1 = Matrix([[1, 1, 6], [2, 7, 50], [34, 33, 91]])
m2 = Matrix([[10, 2, 1], [24, 17, 32], [31, 34, 91]])
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
