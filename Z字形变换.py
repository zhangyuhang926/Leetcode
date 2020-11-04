def convert(s, numRows):
    if numRows < 2:
        return s

    res = ["" for i in range(numRows)]

    flag, i = -1, 0
    for j in s:
        res[i] += j
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return "".join(res)

s = 'LEETCODEISHIRING'
print(convert(s, 3))