def setZeroes(martix):
    row = len(martix)
    col = len(martix[0])
    row_zero = set()
    col_zero = set()

    for i in range(row):
        for j in range(col):
            if martix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)

    for i in range(row):
        for j in range(col):
            if i in row_zero or j in col_zero:
                martix[i][j] = 0

martix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(martix)
print(martix)